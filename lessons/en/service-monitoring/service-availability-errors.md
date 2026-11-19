---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "en"
order_index: 3
title: "Availability and Errors"
description: "Learn to compare request errors using a time window and total request count."
meta_title: "Availability and Errors - Service Monitoring"
meta_description: "Learn to compare request errors using a time window and total request count."
meta_keywords: "availability and errors, service monitoring, devops, Linux Journey"
---

A service can respond to most visitors while some requests fail. Use the total request count and the failures in the same time window to estimate what share of observed requests failed.

## Calculating the Error Rate

The **error rate** divides the number of failed requests by the number observed. Multiply by 100 to express it as a percentage.

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

The first window has two failures per hundred requests, or 2 percent. The next window also has two failures, this time out of twenty requests, or 10 percent.

:::single-choice{#service-availability-errors-compare-windows} Which window had a larger share of failures?

::option[09:05 to 09:10.]{#service-availability-errors-compare-windows-b .correct explanation="Two failures in twenty requests is a larger share than two in a hundred."}
::option[Both were equal because each had two failures.]{#service-availability-errors-compare-windows-a explanation="The denominators differ."}
::option[09:00 to 09:05 because it had more traffic.]{#service-availability-errors-compare-windows-c explanation="Its larger total makes the same failure count a smaller fraction."}
:::

## Choosing Equal Scope

Keep the time window, route, and definition of failure in view. A health endpoint may answer successfully even while a page that needs a dependency fails. If you are checking the experience of people using the page, count requests for that page.

:::single-choice{#service-availability-errors-route-scope} The health endpoint always returns success, but shoppers report errors on checkout. What should you examine?

::option[Only health endpoint responses.]{#service-availability-errors-route-scope-b explanation="Those responses describe a different operation."}
::option[The name of the service account.]{#service-availability-errors-route-scope-c explanation="That does not count the affected requests."}
::option[Checkout requests and their failures.]{#service-availability-errors-route-scope-a .correct explanation="The reported experience belongs to that route."}
:::

## Interpreting Low Traffic

If two requests arrive and one fails, the observed rate is 50 percent. That result describes the sample. A few requests can produce large swings, so keep the count next to the percentage. With zero requests, an error percentage for real traffic is undefined. A separate scheduled test can still tell you whether a request succeeded.

:::single-choice{#service-availability-errors-zero-traffic} A window has no visitor requests. What should you report about the visitor error percentage?

::option[It proves perfect availability.]{#service-availability-errors-zero-traffic-a explanation="No visitor request was observed to establish that."}
::option[The window has no request data for an error percentage.]{#service-availability-errors-zero-traffic-c .correct explanation="Use a separate test if you need evidence about whether the service responds."}
::option[It is definitely 100 percent.]{#service-availability-errors-zero-traffic-b explanation="There were no observed requests in the denominator."}
:::

## Summary

You can now explain an error rate with the context it needs.

1. Compare failures to total requests in the same window.
2. Match the route and definition of failure to the question.
3. Keep counts visible when traffic is sparse.
