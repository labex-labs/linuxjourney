---
lesson_id: "service-latency"
course_id: "service-monitoring"
lang: "en"
order_index: 4
title: "Latency"
description: "Learn to compare typical request times with the slowest observations."
meta_title: "Latency - Service Monitoring"
meta_description: "Learn to compare typical request times with the slowest observations."
meta_keywords: "latency, service monitoring, devops, Linux Journey"
---

**Latency** is how long a request takes. A single number can hide different experiences. Compare the typical request with the slower ones, using the same route and time window.

## Reading a Small Sample

The following five times are in milliseconds. Four requests finished in under 100 milliseconds and one took two seconds.

```text
40  50  60  70  2000
```

The **median**, also called the 50th percentile, is the middle value when the sample is sorted. It is 60 milliseconds here. The slowest observation is 2,000 milliseconds. The mean, found by dividing the sum by five, is 444 milliseconds.

:::single-choice{#service-latency-sample-median} Which value describes the middle request in this sorted sample?

::option[444 milliseconds.]{#service-latency-sample-median-a explanation="This is the mean, which includes the weight of the slow result."}
::option[60 milliseconds.]{#service-latency-sample-median-b .correct explanation="The third of the five sorted values is the median."}
::option[2,000 milliseconds.]{#service-latency-sample-median-c explanation="That is the largest observed value."}
:::

## Examining the Slow End

A **percentile** summarizes where a share of observations falls. A 95th-percentile latency, often shown as p95, describes a threshold near the slow end of a larger sample. Use a dashboard's definition consistently. Tiny samples make estimates of the slow end unstable.

:::single-choice{#service-latency-slow-end} The median barely changes, but visitors still report intermittent delays. Which view would help?

::option[The slow end of the latency distribution, with the request count.]{#service-latency-slow-end-a .correct explanation="Slow responses can change while the middle remains similar."}
::option[Only the median again.]{#service-latency-slow-end-b explanation="This can miss changes affecting a small share of visits."}
::option[The total size of the log file.]{#service-latency-slow-end-c explanation="File size does not show how long requests took."}
:::

## Comparing Similar Requests

Compare the same route under similar traffic. A download can reasonably take longer than a small status check. If a slow route stands out, inspect its request logs and dependencies during the same time window. Use the metric to locate the problem and the other evidence to investigate it.

:::single-choice{#service-latency-compare-route} Which comparison best tests whether the same homepage got slower after a release?

::option[Homepage responses today against downloads from last month.]{#service-latency-compare-route-a explanation="Different work and time periods make the comparison hard to interpret."}
::option[Only one request per release with no time context.]{#service-latency-compare-route-b explanation="An isolated measurement will miss variation."}
::option[Homepage latency from comparable windows before and after the release.]{#service-latency-compare-route-c .correct explanation="Matching the route and workload makes the change easier to interpret."}
:::

## Summary

You can now read typical and slow request times together.

1. Find the median in a small sorted sample.
2. Look at the slow end alongside counts.
3. Compare similar requests before investigating differences.
