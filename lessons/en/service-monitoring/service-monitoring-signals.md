---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "en"
order_index: 1
title: "Monitoring Signals"
description: "Learn to choose a monitoring signal that answers a question about a web service."
meta_title: "Monitoring Signals - Service Monitoring"
meta_description: "Learn to choose a monitoring signal that answers a question about a web service."
meta_keywords: "monitoring signals, service monitoring, devops, Linux Journey"
---

A visitor says the page feels slow. Start with what the visitor experienced, then choose a measurement that can describe it. A **signal** is an observation such as a count, a measurement, or a saved event.

## Checking the User's Experience

**Availability** describes whether the service can do the expected work. A check might request the homepage and verify a successful response. **Latency** is the time the request takes. A page can open successfully and still take several seconds.

:::single-choice{#service-monitoring-signals-slow-page} Visitors receive the page, but it takes several seconds. Which signal describes the symptom most directly?

::option[The number of containers on the server.]{#service-monitoring-signals-slow-page-b explanation="That does not measure the time visitors wait."}
::option[The time it takes to receive the page.]{#service-monitoring-signals-slow-page-a .correct explanation="Latency measures how long the request took."}
::option[The number of bytes in the source repository.]{#service-monitoring-signals-slow-page-c explanation="Repository size does not describe request timing."}
:::

## Counting Requests and Errors

**Traffic** is the demand on the service, such as requests per minute. Track the total alongside the count of failed requests. Five errors during 1,000 requests tell a different story from five errors during ten requests.

:::single-choice{#service-monitoring-signals-count-context} You see five failures in each of two windows. What helps compare the user impact?

::option[The total requests in each window.]{#service-monitoring-signals-count-context-b .correct explanation="Both counts need their denominators to compare error rates."}
::option[The name of the dashboard.]{#service-monitoring-signals-count-context-a explanation="The name tells you where the chart appears and gives no measure of traffic."}
::option[The order of the services in the list.]{#service-monitoring-signals-count-context-c explanation="List order does not measure the number of affected requests."}
:::

## Checking for Resource Pressure

**Saturation** tells you how close a resource is to its capacity. A service might have work waiting for its database even when the web process is running. Compare user-visible behavior with the resource signal before drawing a conclusion.

:::single-choice{#service-monitoring-signals-saturation-check} Requests slow down at the same time as the backlog grows. What is a reasonable next step?

::option[Say the backlog is definitely the root cause.]{#service-monitoring-signals-saturation-check-a explanation="The two changes make a useful lead, and more evidence is needed for causation."}
::option[Recount the images stored on the host.]{#service-monitoring-signals-saturation-check-b explanation="Image availability does not explain a queue of waiting requests."}
::option[Check the resource that serves the waiting work.]{#service-monitoring-signals-saturation-check-c .correct explanation="Examining that resource can show whether it is failing to keep up."}
:::

## Summary

You can now choose a signal based on what a user noticed.

1. Distinguish availability and latency.
2. Interpret failures alongside request volume.
3. Use saturation as a clue about capacity.
