---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "en"
order_index: 5
title: "Traffic Baselines"
description: "Learn to compare similar traffic windows before treating a change as anomalous."
meta_title: "Traffic Baselines - Network Monitoring"
meta_description: "Learn to compare similar traffic windows before treating a change as anomalous."
meta_keywords: "traffic baselines, network monitoring, cybersecurity, Linux Journey"
---

A **baseline** describes behavior you usually observe under specified conditions. For traffic monitoring, that can mean a typical count or range for the same service and time of day.

## Choosing Comparable Windows

A public page may receive more traffic during working hours. Compare windows with a similar routine if you want to detect a change. This example counts requests to one service in five-minute windows.

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

The 230 requests stand out from the weekday morning range. The overnight range would be a less useful comparison.

:::single-choice{#network-traffic-baselines-baseline-fit} Which row provides the useful baseline for today's 09:00 window?

::option[Typical nights at 02:00.]{#network-traffic-baselines-baseline-fit-b explanation="That describes a different traffic pattern."}
::option[The 230 requests observed today on their own.]{#network-traffic-baselines-baseline-fit-c explanation="One current count needs a comparison to establish what changed."}
::option[Typical weekdays at 09:00.]{#network-traffic-baselines-baseline-fit-a .correct explanation="It matches the time of day and service being reviewed."}
:::

## Looking for Context

A banner announcement or a scheduled job can explain a change. Look at the routes, timing, and approved changes before deciding whether to investigate further. The baseline highlights a difference and gives you a starting question.

:::single-choice{#network-traffic-baselines-baseline-explain} Traffic doubled after an announced launch. What should you check?

::option[Treat the difference as proof that an account was compromised.]{#network-traffic-baselines-baseline-explain-a explanation="The count alone does not show cause or an account event."}
::option[Compare the timing and paths with what the launch was expected to produce.]{#network-traffic-baselines-baseline-explain-b .correct explanation="This tests a plausible explanation with related observations."}
::option[Ignore the change because launches always explain every spike.]{#network-traffic-baselines-baseline-explain-c explanation="An expected change can coexist with unrelated activity."}
:::

## Reviewing the Measurement

A collector change can affect a count without a real traffic change. If monitoring started to cover an extra network yesterday, verify which traffic each window includes. Record the service, observation point, time, and unit with the comparison.

:::single-choice{#network-traffic-baselines-changed-coverage} The collector started recording a second site. What makes the next comparison more useful?

::option[Compare counts using the same site and source coverage.]{#network-traffic-baselines-changed-coverage-c .correct explanation="Consistent scope helps distinguish traffic change from coverage change."}
::option[Compare the two total counts without checking their scope.]{#network-traffic-baselines-changed-coverage-a explanation="The collection change makes those totals less comparable."}
::option[Compare the new total with yesterday's total after lengthening the time window.]{#network-traffic-baselines-changed-coverage-b explanation="A longer window still mixes scopes unless you align which sites and sources the totals include."}
:::

## Summary

You can now decide whether a network comparison has a usable baseline.

1. Match the service, time, and unit.
2. Look for expected changes before interpreting a difference.
3. Check whether collection coverage changed.
