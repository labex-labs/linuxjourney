---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "en"
order_index: 6
title: "Service Alerts"
description: "Learn to interpret an alert's condition, time window, and next action."
meta_title: "Service Alerts - Service Monitoring"
meta_description: "Learn to interpret an alert's condition, time window, and next action."
meta_keywords: "service alerts, service monitoring, devops, Linux Journey"
---

A dashboard shows measurements. An **alert** asks someone to look at a condition that may need a response. A useful alert gives the reader a way to tell what happened and what to check.

## Reading the Condition

Consider a rule that checks if more than 5 percent of homepage requests in a five-minute window fail. It also requires at least 100 requests so the alert describes a useful sample for this service.

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

Twelve failures out of 120 is 10 percent. Both parts of the rule are satisfied. The notice points to the homepage's observed failures.

:::single-choice{#service-alerts-condition-match} Would the same rule alert for one failure out of ten requests?

::option[No, because the minimum request count was not met.]{#service-alerts-condition-match-b .correct explanation="Both the rate and count must satisfy this example rule."}
::option[Yes, because the error rate exceeds 5 percent.]{#service-alerts-condition-match-a explanation="This condition also requires at least 100 requests."}
::option[No, because one failure out of ten is 1 percent.]{#service-alerts-condition-match-c explanation="One out of ten is 10 percent, but the request count is still too small for this rule."}
:::

## Checking the Time Window

Use the window shown by the alert, even if the current dashboard now looks healthy. The notice may describe an earlier condition. Check whether the signal has returned to its usual range, and whether important user behavior is working again.

:::single-choice{#service-alerts-alert-window} The alert arrived at 09:16 and described 09:10 to 09:15. Where should you first look for matching errors?

::option[Only in a report from the previous week.]{#service-alerts-alert-window-b explanation="It may provide a baseline and does not show the affected window."}
::option[Only after 09:16.]{#service-alerts-alert-window-c explanation="Waiting for notification can make the notice arrive after the affected observations."}
::option[In the alert's recorded time window.]{#service-alerts-alert-window-a .correct explanation="That is the period in which the rule counted its errors."}
:::

## Taking a Useful Next Step

An alert about failed homepage requests can link to that route's metrics and recent logs. Verify user impact and look for the cause separately. If the service recovered, save enough context to investigate recurring alerts.

:::single-choice{#service-alerts-next-check} Which first action directly checks whether the homepage still fails?

::option[Count every container image in the cache.]{#service-alerts-next-check-a explanation="The alert describes live request outcomes."}
::option[Make an approved test request to the affected route.]{#service-alerts-next-check-c .correct explanation="A fresh request checks whether the reported problem still affects that path."}
::option[Disable the rule so the page is quiet.]{#service-alerts-next-check-b explanation="This changes notifications without checking service behavior."}
:::

## Summary

You can now read an alert and decide what to verify.

1. Check the metric, threshold, and minimum sample.
2. Use the alert's time window to find matching evidence.
3. Verify the user-facing symptom with an appropriate check.
