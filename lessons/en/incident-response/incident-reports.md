---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "en"
order_index: 6
title: "Incident Reports"
description: "Learn to write a concise incident update grounded in observed evidence and open questions."
meta_title: "Incident Reports - Incident Response"
meta_description: "Learn to write a concise incident update grounded in observed evidence and open questions."
meta_keywords: "incident reports, incident response, cybersecurity, Linux Journey"
---

A short incident report helps another person take over without reconstructing the whole investigation. Include the affected service, a few timestamped observations, and the next action.

## Reporting Observations

Here are three simulated records from the service incident.

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

These records describe a change, a failure, and a successful check after recovery. Include the affected path and time. Keep the specifics of what was tested.

:::single-choice{#incident-reports-report-claim} Which statement can you make directly from the records?

::option[The homepage check failed at 09:22 and succeeded after rollback.]{#incident-reports-report-claim-b .correct explanation="This summarizes the observed results and their order."}
::option[Version 3 definitely broke the database.]{#incident-reports-report-claim-a explanation="The records do not show the failure mechanism."}
::option[All users were affected throughout the whole window.]{#incident-reports-report-claim-c explanation="The provided results do not measure every request."}
:::

![Simulated incident evidence showing a production change, a 503, and a successful recovery check](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## Explaining Uncertainty

A rollback followed by a successful request can make the deployment worth investigating. Keep the cause open until evidence supports it. For example, a maintainer can compare the two versions' service logs during the failed request window.

:::single-choice{#incident-reports-uncertainty-statement} Which sentence belongs under an open question?

::option[There is nothing useful to investigate.]{#incident-reports-uncertainty-statement-b explanation="The release and error records narrow a useful next check."}
::option[The service was unavailable forever.]{#incident-reports-uncertainty-statement-c explanation="The later successful result contradicts that claim for the test request."}
::option[The cause of the 503 is still undetermined.]{#incident-reports-uncertainty-statement-a .correct explanation="The evidence shows a failure and a recovery check, and the cause still needs support."}
:::

## Giving the Next Reviewer a Task

Name who can take the next action, which records to look for, and what result would answer the open question. Keep secrets and personal details out of broad updates. A short report can link to protected evidence for approved reviewers.

:::single-choice{#incident-reports-useful-handoff} Which next action best follows from this case?

::option[Ask someone to make a general screenshot with no time or service.]{#incident-reports-useful-handoff-a explanation="This does not specify evidence for the failure."}
::option[Ask the service maintainer to inspect version 3's logs for the failed homepage request window.]{#incident-reports-useful-handoff-c .correct explanation="It assigns a specific source and time to the open question."}
::option[Ask the maintainer to repeat the already successful version 2 check only.]{#incident-reports-useful-handoff-b explanation="That may confirm recovery again. It will not explain the earlier version 3 failure."}
:::

## Recording the Scope of Recovery

A report may need both a recovery observation and an unresolved impact estimate. A successful homepage check after rollback supports recovery for the tested path. To estimate affected visitors, a reviewer still needs request counts or other suitable observations from the failure window.

:::single-choice{#incident-reports-final-application} Which handoff accurately describes both kinds of evidence?

::option[Every visitor recovered because a single request returned 200.]{#incident-reports-final-application-b explanation="The successful request only verifies the path and time tested."}
::option[The failed check should be removed from the report now that recovery passed.]{#incident-reports-final-application-c explanation="The earlier failure is part of the incident evidence."}
::option[The homepage check recovered after rollback, and the total affected requests are still unknown.]{#incident-reports-final-application-a .correct explanation="The report distinguishes a verified recovery check from a count the available records do not provide."}
:::

For a longer exercise after you have practiced packet and host evidence, see [SOC Foundations Review](https://labex.io/courses/project-soc-foundations-review).

## Summary

You can now hand off an incident using facts, uncertainty, and a next action.

1. State the affected path and observed timeline.
2. Separate a suspected cause from confirmed evidence.
3. Assign a follow-up grounded in a source and time window.
