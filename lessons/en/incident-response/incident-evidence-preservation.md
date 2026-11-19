---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "en"
order_index: 2
title: "Evidence Preservation"
description: "Learn to keep a practice record, copy, and checksum usable for later review."
meta_title: "Evidence Preservation - Incident Response"
meta_description: "Learn to keep a practice record, copy, and checksum usable for later review."
meta_keywords: "evidence preservation, incident response, cybersecurity, Linux Journey"
---

During a response, a log excerpt can help explain what happened. Preserve the original source or the approved export, together with the details a second reviewer needs to understand it.

## Recording Context

Write down the host, source, time zone, and time window. Note who collected the records and what filter they used. A copied line without this context may have the same text as a line from a different machine.

:::single-choice{#incident-evidence-preservation-context-fields} A colleague receives a line with time 09:22 and no other context. What should you add?

::option[The path where the copy was saved locally.]{#incident-evidence-preservation-context-fields-b explanation="The receiving path helps locate the copy and leaves its original source and time unknown."}
::option[A guessed explanation for the cause.]{#incident-evidence-preservation-context-fields-c explanation="Record the collection details separately from interpretation."}
::option[The source host, time zone, and capture window.]{#incident-evidence-preservation-context-fields-a .correct explanation="These details let the reviewer place the line on the correct timeline."}
:::

## Comparing a Copy

In a new practice folder, save a harmless sample line, copy it, and calculate SHA-256 values for both files. Use only the example file. The writes replace files of the same names in this folder.

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

The first column gives a content hash. The two values should match. This verifies the bytes of this copy against the original when checked. It cannot tell you whether the original event was logged accurately.

:::single-choice{#incident-evidence-preservation-copy-meaning} What does the matching hash support?

::option[The source timestamp must be true.]{#incident-evidence-preservation-copy-meaning-a explanation="Hashing measures file contents and cannot validate a clock."}
::option[The review copy has the same measured bytes as the sample.]{#incident-evidence-preservation-copy-meaning-b .correct explanation="Both hashes were calculated with the same algorithm."}
::option[The copy was approved for public sharing.]{#incident-evidence-preservation-copy-meaning-c explanation="Approval concerns who may see the file, not its hash."}
:::

![Recorded LabEx checksum output showing matching hashes for a practice file and its review copy](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## Preparing a Safe Review Copy

Keep the original record intact and restrict access. If another team needs only a few fields, prepare a separate excerpt and remove sensitive information from that excerpt. Document that it was reduced, and keep the link to its protected source.

:::single-choice{#incident-evidence-preservation-redact-copy} Which file should you redact for sharing?

::option[A separate review excerpt.]{#incident-evidence-preservation-redact-copy-c .correct explanation="This preserves the source and limits the shared material."}
::option[The protected original, so every copy changes.]{#incident-evidence-preservation-redact-copy-a explanation="This would alter the evidence you want to preserve."}
::option[The checksum text so a changed file still looks the same.]{#incident-evidence-preservation-redact-copy-b explanation="Keep the measured values and the files they describe."}
:::

## Summary

You can now prepare evidence that another reviewer can interpret.

1. Record where and when the material was collected.
2. Check that a copy matches its source bytes.
3. Redact a separate excerpt when sharing.
