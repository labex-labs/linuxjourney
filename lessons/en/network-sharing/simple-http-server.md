---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "en"
order_index: 3
title: "Simple HTTP Server"
description: "Learn how to expose a controlled directory temporarily with Python's HTTP server."
meta_title: "Simple HTTP Server - Network Sharing"
meta_description: "Learn how to quickly set up a simple HTTP server in Linux using Python's http.server module. This guide explains how to create a simple Linux web server for easy file sharing across your network."
meta_keywords: "linux simple http server, simple http server linux, simple linux web server, python http.server, what is python simplehttpserver, file sharing, network server"
---

Python's `http.server` module can serve static files for a short-lived test or trusted transfer. It is not a production web server and does not provide authentication, authorization, TLS, rate limiting, or hardened handling of hostile traffic.

## Preparing a Share Directory

Create a dedicated directory containing only files intended for exposure. Review hidden files, symlinks, permissions, and sensitive metadata before starting. Avoid serving a home directory, repository root, credential directory, or system path.

Use `--directory` so the shared root is explicit:

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

When no index file is present, the module normally generates a directory listing. Anyone who can reach the listener may be able to enumerate and download served content.

:::single-choice{#http-server-directory-option} Why use `--directory /srv/temporary-share`?

::option[It encrypts every HTTP response automatically.]{#http-server-directory-tls explanation="The directory option does not add TLS."}
::option[It creates an account for each downloader.]{#http-server-directory-accounts explanation="The basic module does not provide user authentication."}
::option[It makes the intended document root explicit.]{#http-server-explicit-root .correct explanation="An explicit, reviewed root reduces the chance of exposing files from an accidental working directory."}
:::

## Controlling the Listening Address

Bind to loopback when only the same host should connect:

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

To share on a trusted network, bind deliberately to an appropriate interface address and confirm firewall policy. Running without a restrictive bind commonly listens on all available interfaces, which may expose the directory beyond the intended network.

:::single-choice{#http-server-loopback-bind} Who can normally reach a server bound to `127.0.0.1`?

::option[Clients on the same host.]{#http-server-local-clients .correct explanation="The loopback bind is suitable for local testing or use behind a deliberately configured tunnel."}
::option[Any host on the public Internet.]{#http-server-public explanation="Loopback is local to the same network namespace and is not a public interface."}
::option[Only devices connected through Bluetooth.]{#http-server-bluetooth explanation="The address is unrelated to Bluetooth transport."}
:::

## Testing Access

From the serving host, request a known file and inspect the response:

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

For an authorized remote test, use the selected interface address instead of loopback. Confirm both that the intended file is accessible and that a file outside the document root is not. Browser success alone does not establish appropriate exposure or confidentiality.

:::single-choice{#http-server-default-port-command} What port is selected explicitly in `python3 -m http.server 8000`?

::option[22]{#http-server-port-22 explanation="Port 22 is commonly associated with SSH and is not selected here."}
::option[8000]{#http-server-port-8000 .correct explanation="The positional port operand tells the module where to listen."}
::option[443]{#http-server-port-443 explanation="The command does not configure HTTPS on port 443."}
:::

## Stopping and Cleaning Up

Run the temporary service in a supervised terminal and stop it with `Ctrl-C` when the transfer finishes. Verify the listener is gone:

```bash
$ ss -ltn 'sport = :8000'
```

Remove temporary copies according to data-handling policy and revert any temporary firewall rule. For persistent, authenticated, or Internet-facing distribution, use a maintained server configured with access control and TLS.

:::single-choice{#http-server-completion-check} What should happen after the temporary transfer is complete?

::option[Stop it and verify the port is no longer listening.]{#http-server-stop-verify .correct explanation="Verification confirms that the temporary network service actually ended."}
::option[Leave the listener running in case someone needs it later.]{#http-server-leave-running explanation="Unnecessary exposure should be removed when the authorized purpose ends."}
::option[Copy additional private files into the document root.]{#http-server-add-private explanation="Only intentionally shared content belongs in the served directory."}
:::

## Summary

You can now run a temporary Python HTTP server with a bounded exposure.

1. Serve only a dedicated, reviewed directory.
2. Bind to the narrowest appropriate address.
3. Test intended access and unintended boundaries.
4. Stop the listener and clean up temporary access afterward.
