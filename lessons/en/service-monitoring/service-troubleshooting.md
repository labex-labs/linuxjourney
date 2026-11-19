---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "en"
order_index: 7
title: "Service Troubleshooting"
description: "Learn to choose the next check for service stoppage, dependency errors, and slow requests."
meta_title: "Service Troubleshooting - Service Monitoring"
meta_description: "Learn to choose the next check for service stoppage, dependency errors, and slow requests."
meta_keywords: "service troubleshooting, service monitoring, devops, Linux Journey"
---

Start with one concrete symptom, such as a failed request to the homepage. Then compare observations made near the same time and from the location that matters to users.

## When a Server Stops

In the first case, the browser reports a refused connection and the service's container shows `Exited (1)`. Both observations justify checking why the program stopped. Use its retained logs. Keep the time of the exit in view before comparing it with other events.

:::single-choice{#service-troubleshooting-stopped-case} Which check is most likely to explain the stopped process?

::option[Request the same homepage again to get a more recent status.]{#service-troubleshooting-stopped-case-a explanation="A retry checks the symptom. The retained logs may explain why the program exited."}
::option[Read the container's last available log lines.]{#service-troubleshooting-stopped-case-b .correct explanation="Startup or exit messages can identify where the program stopped."}
::option[Inspect logs from a different running container using the same image.]{#service-troubleshooting-stopped-case-c explanation="That container has a separate runtime history and may never have encountered the failure."}
:::

## When a Dependency Fails

In the second case, the web process is running but the page returns a server error. Its log names a timeout while contacting the catalog for request `r17`. That is a reason to examine the dependency's records for the same request. A healthy first hop does not show that every other service is healthy.

:::single-choice{#service-troubleshooting-dependency-case} What is the next evidence to seek for r17?

::option[The catalog record for that request and time.]{#service-troubleshooting-dependency-case-a .correct explanation="It shows what happened during the dependency call."}
::option[The archived Docker image size.]{#service-troubleshooting-dependency-case-b explanation="That does not describe the live call."}
::option[A successful unrelated homepage check from yesterday.]{#service-troubleshooting-dependency-case-c explanation="That check describes a different time and cannot explain this request."}
:::

## When Requests Get Slower

A third sample shows mostly successful responses, but users report delays. Latency rises in the same window that a worker queue grows. Check demand and worker activity before attributing cause. If a change is made, repeat the user-facing check and review the same signals afterward.

:::single-choice{#service-troubleshooting-slow-case} Which comparison best checks whether a change helped this case?

::option[Before and after screenshots of the source repository.]{#service-troubleshooting-slow-case-a explanation="Those do not measure request times or queues."}
::option[The cache size compared with the number of deployed branches.]{#service-troubleshooting-slow-case-b explanation="Neither addresses the reported waiting time."}
::option[Comparable user request times and worker queues before and after.]{#service-troubleshooting-slow-case-c .correct explanation="This checks the original symptom and the suspected constraint."}
:::

## Reading Conflicting Checks

Suppose a local probe succeeds while users still see errors. Record which path each check used. A local probe can demonstrate that a process answers on the host while a client request reveals an issue on the route to that host.

:::single-choice{#service-troubleshooting-final-application} Which result should guide a follow-up about affected users?

::option[A check from the route and location those users use.]{#service-troubleshooting-final-application-a .correct explanation="It observes the part of the service that produced their reported symptom."}
::option[The result from the host only.]{#service-troubleshooting-final-application-b explanation="That result is valuable for locating the boundary and leaves the outside path untested."}
::option[The current capacity of the image registry.]{#service-troubleshooting-final-application-c explanation="The registry can serve images while the user-facing route has a separate problem."}
:::

## Summary

You can now choose a next check based on the evidence you have.

1. Use process state and logs to investigate a stop.
2. Follow a failed request to its dependency.
3. Verify an improvement against the original user-visible symptom.
