---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "en"
order_index: 2
title: "Service Logs"
description: "Learn to follow one request across service logs using a request ID and time."
meta_title: "Service Logs - Service Monitoring"
meta_description: "Learn to follow one request across service logs using a request ID and time."
meta_keywords: "service logs, service monitoring, devops, Linux Journey"
---

A user sees an error. A service log can tell you which part of the work failed for that request. Begin with the time, then look for a **request ID**, a label passed along to records for the same request.

## Reading One Request

The sample below shows two services. A **dependency** is a service another program needs to finish its work. Here the web service asks a catalog service for a list of items.

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

The web row shows a failed response for `r17`. The catalog row with the same ID gives a timeout. The nearby successful catalog request belongs to `r18`.

:::single-choice{#service-logs-matching-request} Which catalog result belongs to the web failure for r17?

::option[The successful result for r18.]{#service-logs-matching-request-a explanation="That row belongs to a different request."}
::option[Both catalog results.]{#service-logs-matching-request-c explanation="Close timestamps can still name separate requests."}
::option[The timeout for r17.]{#service-logs-matching-request-b .correct explanation="The shared ID links the two records for this request."}
:::

## Filtering the Sample

Save the three lines above as `requests.log` in a practice directory. Use `grep -F` to look for exact text. Include the space after the identifier to match the field boundary in this sample.

```bash
$ grep -F 'request=r17 ' requests.log
```

Expect the web and catalog lines for `r17`. Real logs may change their format or omit the request ID, so check that the fields you search represent the same thing across services.

:::single-choice{#service-logs-choose-filter} Why include the whole request field rather than search for the word timeout?

::option[It guarantees that all traffic had the same error.]{#service-logs-choose-filter-b explanation="This filters records for one request."}
::option[It returns the matching web and catalog records even though only one contains timeout.]{#service-logs-choose-filter-a .correct explanation="The shared ID follows the request through both services."}
::option[It changes the log so later searches find the right result.]{#service-logs-choose-filter-c explanation="Grep reads the file and prints matching lines."}
:::

![Grep output linking the web error and catalog timeout for request r17](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## Reporting Scope

The timeout locates the failure seen by this request. It does not identify which component inside the catalog slowed down. Check the dependency's own metrics or recent records next. When giving a teammate a log excerpt, preserve the request ID and remove secrets or personal data that they do not need.

:::single-choice{#service-logs-evidence-limit} What should you state in a first report?

::option[The catalog timed out during r17 and needs a closer check.]{#service-logs-evidence-limit-c .correct explanation="This summarizes the matching records without guessing the underlying cause."}
::option[All catalog requests timed out.]{#service-logs-evidence-limit-a explanation="The sample includes a separate successful catalog request."}
::option[A specific database disk failed.]{#service-logs-evidence-limit-b explanation="No disk observation appears in the records."}
:::

To practice querying service records on a Linux host, try [Analyze Logs for Incident Response](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586).

## Summary

You can now follow a request through multiple service logs.

1. Match a request ID across the relevant records.
2. Use a literal filter to narrow a sample.
3. Report what the records support and ask the next question.
