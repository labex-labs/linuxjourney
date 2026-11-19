---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "en"
order_index: 7
title: "Web Access Logs"
description: "Learn to use HTTP access logs to answer what a service returned without exposing credentials."
meta_title: "Web Access Logs - Web Security"
meta_description: "Learn to use HTTP access logs to answer what a service returned without exposing credentials."
meta_keywords: "web access logs, web security, cybersecurity, Linux Journey"
---

A web server can save one **access log** record for each request. The log might include a time, path, response code, and request ID. Use only the fields needed for the question you are investigating.

## Reading the Request Result

This simulated excerpt uses named fields. The two requests went to different paths.

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

A `403` indicates that the service refused the request. Check the exact path and request ID before comparing the response with another record.

:::single-choice{#web-access-logs-log-result} Which request should you follow to investigate the refusal?

::option[r31 on /health.]{#web-access-logs-log-result-a explanation="That row reports a successful health request."}
::option[r32 on /staff.]{#web-access-logs-log-result-b .correct explanation="Its status is 403, the refusal in this excerpt."}
::option[Both as if they were the same request.]{#web-access-logs-log-result-c explanation="The names and paths distinguish them."}
:::

## Looking for the Access Decision

The access log records what the server returned. It may give no reason for a particular permission decision. If the application also records authorization decisions, match the request ID and time. That can tell you which rule applied in this example.

:::single-choice{#web-access-logs-refusal-reason} The access row says 403. Which additional record would best explain why?

::option[The application's permission decision for r32.]{#web-access-logs-refusal-reason-a .correct explanation="The matching record can say which rule applied."}
::option[A success response from another site.]{#web-access-logs-refusal-reason-b explanation="It has no link to this refusal."}
::option[An earlier request for the health path.]{#web-access-logs-refusal-reason-c explanation="It records a different operation and outcome."}
:::

## Keeping Credentials Out of Logs

Avoid logging values that allow someone to use another person's session, such as a full session cookie or an authorization token. A request ID and response status can still support troubleshooting. When you share a log sample, remove sensitive fields and retain only the details needed for the investigation.

:::single-choice{#web-access-logs-safe-fields} Which pair can help trace the refused request without copying a credential?

::option[The full session cookie and the account password.]{#web-access-logs-safe-fields-a explanation="Both values are sensitive and should be kept out of shared logs."}
::option[The authorization token and a public path.]{#web-access-logs-safe-fields-b explanation="The path can be useful while the token is a private credential."}
::option[The request ID and its response status.]{#web-access-logs-safe-fields-c .correct explanation="These allow comparison with the relevant records without revealing a session value."}
:::

## Sharing a Small Excerpt

Imagine a reviewer needs context for a refused request. Keep the time, ID, method, sanitized path, and status when those fields are sufficient. Some paths can contain private values in their query strings. Check the excerpt before sharing it.

:::single-choice{#web-access-logs-final-application} Which excerpt best serves that review?

::option[The entire request and every header by default.]{#web-access-logs-final-application-b explanation="Requests can contain credentials or unnecessary personal data."}
::option[Only the status code with all identifiers removed.]{#web-access-logs-final-application-c explanation="The code alone may be hard to match to the related policy record."}
::option[A sanitized path with the request time, ID, and response status.]{#web-access-logs-final-application-a .correct explanation="It preserves the necessary correlation fields without sharing session values."}
:::

## Summary

You can now interpret a basic access log and preserve useful context safely.

1. Match the request ID, path, and response.
2. Find a related policy record when the reason matters.
3. Keep credentials out of captured and shared logs.
