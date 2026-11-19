---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "en"
order_index: 4
title: "Integrity Baselines"
description: "Learn to interpret an integrity report and choose when to approve a new baseline."
meta_title: "Integrity Baselines - System Auditing"
meta_description: "Learn to interpret an integrity report and choose when to approve a new baseline."
meta_keywords: "integrity baselines, system auditing, cybersecurity, Linux Journey"
---

A **baseline** is a trusted record of expected file properties at a known point. A later integrity check can compare the current files with it and report differences.

## Reading a Difference Report

This simulated excerpt compares a host against its last approved state.

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

The first row shows a change to bytes. The second shows a permissions change. The third reports that a previously tracked file was absent during the check.

:::single-choice{#file-integrity-baselines-report-mode} Which row reports changed access permissions?

::option[The site.conf row.]{#file-integrity-baselines-report-mode-a explanation="It reports a change in content hash."}
::option[The banner.txt row.]{#file-integrity-baselines-report-mode-b .correct explanation="The mode changed from 644 to 640."}
::option[The site.prev row.]{#file-integrity-baselines-report-mode-c explanation="This row records whether the path was present."}
:::

![Simulated integrity report comparing file contents, access mode, and presence](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## Checking the Reference

The report is only useful if the earlier reference was trusted. Preserve its identity and creation date. An earlier file captured while something was already wrong can yield a misleading comparison. Ask which approved state the baseline represents.

:::single-choice{#file-integrity-baselines-reference-source} Which baseline is most useful for reviewing today's configuration?

::option[A recorded, approved copy from before the change.]{#file-integrity-baselines-reference-source-a .correct explanation="It gives a known reference the reviewer can verify."}
::option[A baseline created from today's unexplained files.]{#file-integrity-baselines-reference-source-b explanation="It would absorb the differences before the review."}
::option[An unrelated host's settings with no comparison context.]{#file-integrity-baselines-reference-source-c explanation="Different roles can expect different files and permissions."}
:::

## Reviewing Before Updating

Compare each difference with an approved change and verify the service result. If the banner mode change was planned but the configuration change was not, review them separately. Update the reference after authorized differences are understood and approved. Keep a record of the older reference.

:::single-choice{#file-integrity-baselines-update-timing} The banner mode change is approved and the site.conf change is unexplained. What should happen before accepting a new baseline?

::option[Approve everything because one row was expected.]{#file-integrity-baselines-update-timing-a explanation="The file differences concern separate changes."}
::option[Throw away the difference report.]{#file-integrity-baselines-update-timing-b explanation="It records what still needs review."}
::option[Investigate the unexplained site.conf change.]{#file-integrity-baselines-update-timing-c .correct explanation="A new baseline should follow review of the current state."}
:::

To create and compare an integrity reference in a practice environment, try [File Integrity Monitoring](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122).

## Summary

You can now use a baseline as evidence for a specific comparison.

1. Distinguish content, mode, and presence in a report.
2. Check that the reference represents a trusted state.
3. Review unexpected differences before accepting a new reference.
