---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "en"
order_index: 5
title: "Configuration Changes"
description: "Learn to combine an approved change, a file difference, and an audit event."
meta_title: "Configuration Changes - System Auditing"
meta_description: "Learn to combine an approved change, a file difference, and an audit event."
meta_keywords: "configuration changes, system auditing, cybersecurity, Linux Journey"
---

A change ticket records an intended action. A file comparison records what differs now. An audit event describes an observed action within its coverage. Use all three to work out what you can say about a configuration change.

## Matching the Expected Change

Review this simulated maintenance entry.

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

It states which file and property were approved. A difference elsewhere needs a separate explanation, even if it appears during the same window.

:::single-choice{#auditing-configuration-changes-approve-scope} Which change matches the approved action as described?

::option[Site.conf contents changed on web-01.]{#auditing-configuration-changes-approve-scope-b explanation="That configuration file is outside this approval."}
::option[Banner.txt disappeared from another host.]{#auditing-configuration-changes-approve-scope-c explanation="Both the reported operation and host differ."}
::option[Banner.txt mode changed to 640 on web-01.]{#auditing-configuration-changes-approve-scope-a .correct explanation="It matches the file, property, host, and approved result in the entry."}
:::

## Comparing Observations

A comparison reports that the banner mode changed and the bytes of `site.conf` changed. A separate audit event at 09:15 records a write to `site.conf` on `web-01`. The audit event gives you a time to investigate. It does not explain whether the action was approved.

:::single-choice{#auditing-configuration-changes-source-comparison} Which conclusion follows from the two observations about site.conf?

::option[The write was authorized because its time is within the window.]{#auditing-configuration-changes-source-comparison-a explanation="The ticket names a different action."}
::option[The recorded write and the changed bytes make this file worth reviewing.]{#auditing-configuration-changes-source-comparison-b .correct explanation="The comparison gives the difference and the audit event narrows the time."}
::option[The banner change caused the write.]{#auditing-configuration-changes-source-comparison-c explanation="These observations do not establish that one action caused the other."}
:::

## Writing the Review Note

State which difference matches the plan and which remains unexplained. Include the file, host, time, and source reference. A useful next step is to compare the current configuration with the approved copy and check whether another approved change covers it.

:::single-choice{#auditing-configuration-changes-useful-review} What should the handoff say about site.conf?

::option[Name the difference, cite the observed write, and ask for supporting approval.]{#auditing-configuration-changes-useful-review-c .correct explanation="The note preserves the evidence and the question that remains."}
::option[Mark it approved and omit its path.]{#auditing-configuration-changes-useful-review-a explanation="That loses the target and assumes an approval the records do not show."}
::option[Attribute it to the owner of the banner change.]{#auditing-configuration-changes-useful-review-b explanation="The records do not establish that attribution."}
:::

## Comparing Two Maintenance Notes

Another ticket authorizes a later edit to site.conf. Compare the observed time, target host, and file with the ticket before closing the review. An approved change to the right file can still fail to explain an earlier event.

:::single-choice{#auditing-configuration-changes-final-application} The ticket covers site.conf on web-01 from 09:40 to 10:00. What remains open about the write recorded at 09:15?

::option[Whether site.conf exists outside the ticket system.]{#auditing-configuration-changes-final-application-b explanation="The file comparison already observes the configuration."}
::option[Whether the later ticket should automatically explain every past write.]{#auditing-configuration-changes-final-application-c explanation="Approval applies to its specified action and time."}
::option[Whether separate approval covers that earlier write.]{#auditing-configuration-changes-final-application-a .correct explanation="The host and path match, but the recorded time falls outside the approved window."}
:::

## Summary

You can now reconstruct what is known about a configuration change.

1. Read the intended scope from the approved change.
2. Use comparisons and audit events to describe what was observed.
3. Explain an evidence gap and choose the next check.
