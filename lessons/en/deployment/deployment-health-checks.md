---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "en"
order_index: 4
title: "Health Checks"
description: "Learn to combine a process check, a service check, and a client request after deployment."
meta_title: "Health Checks - Deployment"
meta_description: "Learn to combine a process check, a service check, and a client request after deployment."
meta_keywords: "health checks, deployment, devops, Linux Journey"
---

A newly started program can be running before it is ready. Check the service in stages so a single passing indicator has a clear meaning.

## Checking the Process

A container list can show that the main program is running. That answers an important first question for a new deployment. It cannot tell you whether the program finished initializing or whether a browser can reach it.

:::single-choice{#deployment-health-checks-process-scope} The new container shows Up. Which conclusion is supported?

::option[Visitors are definitely getting the new page.]{#deployment-health-checks-process-scope-a explanation="A container state does not describe a visitor's request."}
::option[The container's main program is running at the time checked.]{#deployment-health-checks-process-scope-b .correct explanation="Up reports the process state."}
::option[Every dependency passed a check.]{#deployment-health-checks-process-scope-c explanation="No dependency results are shown."}
:::

## Checking a Service Endpoint

An **endpoint** is an address and path the service handles. Check a path that matches the behavior you care about. To try this locally, use an empty practice folder. The redirection writes the version file. Leave the Python server running on loopback in this terminal and stop it with Ctrl+C after practice.

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

In a second terminal, request the version file. Curl's `-f` option reports HTTP error responses as failures, while `-sS` keeps normal output quiet and still shows errors.

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

The expected practice result is `2`. A successful request to a version file confirms far less than a complete test of the site.

:::single-choice{#deployment-health-checks-endpoint-mismatch} The request succeeds and prints 1. What should you investigate?

::option[Which version is answering at that address.]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="Network access worked, but the observed version differs from the intended one."}
::option[Why curl cannot connect at all.]{#deployment-health-checks-endpoint-mismatch-b explanation="The returned value shows that a connection and response succeeded."}
::option[Whether the service name contains a digit.]{#deployment-health-checks-endpoint-mismatch-c explanation="The service name gives no evidence about the version returned."}
:::

![Loopback version endpoint returning version 2 from the LabEx practice server](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## Checking from the Client's Location

If a request on the service host works, repeat a safe check where users normally connect. A load balancer, proxy, or network rule can change the path they take. Record which address you checked and what came back. If the result does not match the release, keep the deployment under investigation.

:::single-choice{#deployment-health-checks-user-path} A local request returns 2, but the public test address returns 1. Which check is most useful next?

::option[Count how many lines the local request printed.]{#deployment-health-checks-user-path-a explanation="Line count does not identify what serves the public address."}
::option[Repeat only the same local check.]{#deployment-health-checks-user-path-b explanation="The local path already produced version 2."}
::option[Check which service version the public route selects.]{#deployment-health-checks-user-path-c .correct explanation="The two paths reached different responses."}
:::

## Summary

You can now tell what each post-deployment check verified.

1. Confirm the main program is running.
2. Request an endpoint that reports the expected version.
3. Verify the user-facing path separately.
