"""Run LabEx's learning sync with serial, rate-limited HTTP requests."""

from email.utils import parsedate_to_datetime
import sys
import time

import requests

from labex_cli.labex.commands.lesson.sync_v2 import sync_learning_command
from labex_cli.labex.utils import http


MIN_REQUEST_INTERVAL = 1
BACKOFF_SECONDS = (2, 4, 8, 16, 32)


def retry_after_seconds(value):
    value = (value or "").strip()
    if not value:
        return 0
    if value.isdecimal():
        return int(value)
    try:
        return max(0, parsedate_to_datetime(value).timestamp() - time.time())
    except (ValueError, OverflowError, OSError):
        return 0


class SyncTransport:
    def __init__(self):
        self.next_request_at = 0
        self.rate_limit_error = None

    def request(self, method, url, **kwargs):
        # A serial CLI worker may already have more files queued when a request fails.
        if self.rate_limit_error is not None:
            raise SystemExit(self.rate_limit_error)

        for attempt in range(len(BACKOFF_SECONDS) + 1):
            delay = self.next_request_at - time.monotonic()
            if delay > 0:
                time.sleep(delay)
            self.next_request_at = time.monotonic() + MIN_REQUEST_INTERVAL

            response = requests.request(method, url, **kwargs)
            if response.status_code != 429:
                return response

            retry_after = retry_after_seconds(response.headers.get("Retry-After"))
            response.close()
            if attempt == len(BACKOFF_SECONDS):
                self.rate_limit_error = (
                    f"LabEx still returned HTTP 429 after {attempt} retries; stopping sync."
                )
                raise SystemExit(self.rate_limit_error)

            backoff = max(BACKOFF_SECONDS[attempt], retry_after)
            print(f"LabEx returned HTTP 429. Retrying request in {backoff:.1f}s.", flush=True)
            self.next_request_at = time.monotonic() + backoff

    def post(self, url, **kwargs):
        return self.request("POST", url, **kwargs)


if __name__ == "__main__":
    # Replace the CLI HTTP module's transport in this process so login and sync
    # requests share the same rate limit. Keep the CLI's validation and sync order.
    http.requests = SyncTransport()
    sync_learning_command(args=[*sys.argv[1:], "--workers", "1"])
