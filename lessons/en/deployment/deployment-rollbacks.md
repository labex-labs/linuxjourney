---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "en"
order_index: 5
title: "Rollbacks"
description: "Learn to choose a known working version and check whether application rollback is sufficient."
meta_title: "Rollbacks - Deployment"
meta_description: "Learn to choose a known working version and check whether application rollback is sufficient."
meta_keywords: "rollbacks, deployment, devops, Linux Journey"
---

A **rollback** returns a service to a previous known working release. Use the deployment history to choose the target. Check whether the release also changed shared data or settings before undoing anything.

## Choosing a Previous Release

This example shows a new release followed by a failed request. The last verified version was 2. The reference labels below stand for complete image digests in an actual record.

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

Version 2 is a sensible rollback candidate if it still works with the environment. Use the recorded artifact identity to find it.

:::single-choice{#deployment-rollbacks-previous-version} Which image would you investigate first as the rollback target?

::option[The newest cached image on the host.]{#deployment-rollbacks-previous-version-a explanation="Cache order does not identify a working release."}
::option[Digest-C because the deployment happened most recently.]{#deployment-rollbacks-previous-version-c explanation="The record links this artifact to the failed check."}
::option[Digest-B, which previously passed the relevant checks.]{#deployment-rollbacks-previous-version-b .correct explanation="The record links it to the last verified version."}
:::

## Checking Data Compatibility

An application release may also change a database or another shared resource. Starting an older image leaves that external state as it is. Ask whether the older application can read the current data. If a data restore is needed, use the team's recovery plan and consider changes made since the backup.

:::single-choice{#deployment-rollbacks-external-state} Version 3 changed a database format. What must you check before starting version 2 against it?

::option[Whether version 2 passed the old homepage check.]{#deployment-rollbacks-external-state-b explanation="The earlier check makes version 2 a candidate. It gives no evidence about the current database format."}
::option[Whether version 2 supports the current format.]{#deployment-rollbacks-external-state-a .correct explanation="Changing the application image does not revert shared data."}
::option[Whether the database name appears in release notes.]{#deployment-rollbacks-external-state-c explanation="The practical question is whether the older code can use the present data."}
:::

## Confirming the Result

After the rollback, verify the running version and repeat the same user-focused check that failed. Observe important dependencies again. Record the time, restored version, and results so someone can distinguish the original failure from the recovery.

:::single-choice{#deployment-rollbacks-rollback-proof} The rollback command finished. Which pair supports that the service recovered?

::option[The endpoint reports version 2 and the failed check now passes.]{#deployment-rollbacks-rollback-proof-c .correct explanation="These observations confirm the target version and the affected behavior."}
::option[Two successful image downloads.]{#deployment-rollbacks-rollback-proof-a explanation="Downloads prepare files and do not test the running service."}
::option[An earlier screenshot of version 2.]{#deployment-rollbacks-rollback-proof-b explanation="The screenshot shows a historical state."}
:::

## Summary

You can now plan a rollback around evidence.

1. Choose a release with a verified history.
2. Check shared data and configuration compatibility.
3. Verify the restored version and the affected user behavior.
