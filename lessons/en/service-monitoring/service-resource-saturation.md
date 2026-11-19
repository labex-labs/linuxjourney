---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "en"
order_index: 5
title: "Resource Saturation"
description: "Learn to use utilization and queues to decide where a service may be reaching capacity."
meta_title: "Resource Saturation - Service Monitoring"
meta_description: "Learn to use utilization and queues to decide where a service may be reaching capacity."
meta_keywords: "resource saturation, service monitoring, devops, Linux Journey"
---

When a service has more work than a resource can handle immediately, requests may wait. A sustained wait can show up in a queue and in slower responses.

## Reading Capacity and Demand

**Utilization** is how much of a resource is being used. A worker pool, for example, might allow four jobs at once. Four busy workers means the pool is fully used at that moment. If another job arrives, it can wait in a queue until a worker becomes free.

:::single-choice{#service-resource-saturation-worker-capacity} Four workers are busy and three jobs are queued. What do you know?

::option[Exactly seven workers are running.]{#service-resource-saturation-worker-capacity-b explanation="Three of the jobs are waiting rather than occupying worker slots."}
::option[Every request has already failed.]{#service-resource-saturation-worker-capacity-c explanation="Waiting work can still finish when a worker is available."}
::option[All slots are busy and some work is waiting.]{#service-resource-saturation-worker-capacity-a .correct explanation="The worker count describes current usage and the queue exposes extra demand."}
:::

## Comparing Over Time

A short burst is different from a queue that grows across several observations. Compare the queue with request latency and traffic in the same window.

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

The full worker pool and growing queue suggest that the work is arriving faster than it completes in this example. Check what occupies the workers.

:::single-choice{#service-resource-saturation-sustained-pressure} Which observation most strongly suggests continuing pressure?

::option[Two busy workers at 09:10.]{#service-resource-saturation-sustained-pressure-a explanation="That row shows capacity remained and no jobs waited."}
::option[The queue grows while all workers remain busy.]{#service-resource-saturation-sustained-pressure-b .correct explanation="Waiting work is accumulating as capacity stays occupied."}
::option[One slower response while the queue remains empty.]{#service-resource-saturation-sustained-pressure-c explanation="One slow result can justify a closer look. A growing queue across full-capacity samples gives stronger evidence of sustained pressure."}
:::

![Simulated worker metrics showing full utilization and a growing queue](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## Checking the Cause

The workers can be busy because requests arrived faster, because a dependency slowed down, or because a recent change made each job take longer. Compare request volume, service time, and dependency observations. An additional signal helps choose a response.

:::single-choice{#service-resource-saturation-next-observation} Request volume stayed steady while work began taking longer. What might clarify the backlog?

::option[Check job duration and dependency timing together.]{#service-resource-saturation-next-observation-c .correct explanation="That helps locate why work now occupies slots longer."}
::option[Change capacity before gathering any further evidence.]{#service-resource-saturation-next-observation-a explanation="More capacity may not address work blocked on a dependency."}
::option[Count the roles in the repository.]{#service-resource-saturation-next-observation-b explanation="Those roles do not measure what the workers wait for."}
:::

## Summary

You can now distinguish a busy resource from a sustained backlog.

1. Link worker counts to the pool's capacity.
2. Compare queues with request behavior over time.
3. Investigate the work that occupies a constrained resource.
