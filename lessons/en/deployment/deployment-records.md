---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "en"
order_index: 6
title: "Deployment Records"
description: "Learn to reconstruct a deployment and rollback from a short release timeline."
meta_title: "Deployment Records - Deployment"
meta_description: "Learn to reconstruct a deployment and rollback from a short release timeline."
meta_keywords: "deployment records, deployment, devops, Linux Journey"
---

A deployment record helps another person connect a user-visible result to a change. Start with the time, environment, source revision, and artifact. Add the result of the check and any action taken afterward.

## Naming What Changed

This practice record tracks one rollout. The identifiers are shortened for readability.

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200 means a successful response. HTTP 503 reports that the service was unavailable for that request. Keep the check and address with the result in a real record.

:::single-choice{#deployment-records-first-prod-change} Which row records the first observed production behavior for digest-C?

::option[The 09:12 prod row.]{#deployment-records-first-prod-change-b .correct explanation="It shows the attempted production version and the failed check."}
::option[The 09:00 staging row.]{#deployment-records-first-prod-change-a explanation="That check ran in a different environment."}
::option[The 09:18 prod row.]{#deployment-records-first-prod-change-c explanation="This row records a different artifact after rollback."}
:::

![Simulated release timeline showing staging success, a production 503, and a rollback to version 2](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## Explaining the Rollback

The last row shows a return to digest-B. The version check and the homepage result describe the outcome after the rollback. They give no detailed cause for the earlier failure. Keep any hypothesis separate until you have supporting evidence.

:::single-choice{#deployment-records-rollback-evidence} What can you say about the 09:18 result?

::option[The 09:12 failure was caused by a missing database.]{#deployment-records-rollback-evidence-b explanation="No dependency evidence appears in this record."}
::option[All requests succeeded from then on.]{#deployment-records-rollback-evidence-c explanation="One successful check gives evidence for that request."}
::option[Production returned to version 2 and that homepage request succeeded.]{#deployment-records-rollback-evidence-a .correct explanation="The row records the restored version and the observed HTTP response."}
:::

## Handing Off the Record

A new reviewer needs to reproduce the scope of the observation. Include how it was measured, a timestamp with its time zone, and a link to the producing build when available. State what to inspect next if the cause remains unknown.

:::single-choice{#deployment-records-handoff-detail} Which detail would help the next reviewer repeat the homepage check?

::option[The identifier of the prior release only.]{#deployment-records-handoff-detail-a explanation="The earlier version can aid comparison. It cannot tell the reviewer where and when this check ran."}
::option[The exact target address and time of the check.]{#deployment-records-handoff-detail-c .correct explanation="These details let someone verify the same path and compare other signals in the relevant window."}
::option[The time at which the source commit was created.]{#deployment-records-handoff-detail-b explanation="The commit time identifies an earlier event. The reviewer needs the time and destination of the check."}
:::

## Recording What Actually Ran

A tag in a deployment note may move after a release. If the service already reports version 2, record the artifact that is actually running as well as its readable label. Those two values let someone compare the release later even if its registry tag moved.

:::single-choice{#deployment-records-final-application} The release note says site:2. What additional detail makes later comparison more reliable?

::option[The digest from whoever most recently pulled site:2.]{#deployment-records-final-application-c explanation="A later pull can receive different content from the running service."}
::option[The full digest of the image that actually ran.]{#deployment-records-final-application-a .correct explanation="It identifies the selected content when a readable tag might later point somewhere else."}
::option[The friendly tag copied into a second field.]{#deployment-records-final-application-b explanation="Repeating the tag still leaves the same ambiguity."}
:::

## Summary

You can now read a release timeline and hand it to someone else.

1. Identify the environment, revision, and artifact in a record.
2. Describe a rollback using the observed result.
3. Preserve enough detail for the next check.
