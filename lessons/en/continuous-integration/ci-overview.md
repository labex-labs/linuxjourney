---
lesson_id: "ci-overview"
course_id: "continuous-integration"
lang: "en"
order_index: 1
title: "Continuous Integration"
description: "Learn how continuous integration checks small changes before they enter a shared branch."
meta_title: "Continuous Integration - Continuous Integration"
meta_description: "Learn how continuous integration checks small changes before they enter a shared branch."
meta_keywords: "continuous integration, devops, Linux Journey"
---

A homepage change can look fine in one person's browser and still break when someone else tries it. **Continuous integration**, or CI, brings changes together frequently and runs repeatable checks against specific revisions.

## Connecting a Change to a Check

A revision identifies the version of the files being checked. When a proposed change modifies `index.html`, CI can run a check against that version and report whether it meets an expectation. For this site, a check might look for the required heading. The team can use the result while deciding whether to merge.

:::single-choice{#ci-overview-revision-result} A check passed on Monday. A new commit changes the page on Tuesday. What does the old pass establish?

::option[Both revisions meet the check.]{#ci-overview-revision-result-b explanation="The later commit needs its own result."}
::option[The Monday revision met that check.]{#ci-overview-revision-result-a .correct explanation="The result belongs to the revision the check ran against."}
::option[The new page is visible to visitors.]{#ci-overview-revision-result-c explanation="A check against source files gives no evidence of a live deployment."}
:::

## Reading a Failed Check

Suppose a check says the expected heading is missing. This gives the author a narrow place to investigate. Read the expectation and the result before changing the page. Sometimes the author made a mistake. Sometimes the intended behavior changed and the check needs a corresponding edit.

:::single-choice{#ci-overview-failed-action} What should you inspect first when the heading check fails?

::option[The expected heading and the file in the checked revision.]{#ci-overview-failed-action-b .correct explanation="Comparing them shows what caused this particular mismatch."}
::option[The artifact from the previous successful run first.]{#ci-overview-failed-action-a explanation="That artifact describes older output. The failing check and current file give more direct evidence."}
::option[The visitors' network settings.]{#ci-overview-failed-action-c explanation="This check reads a file and makes no browser request."}
:::

## Distinguishing Checks and Delivery

A pipeline can check files, build an output, and hand that output to a later deployment. A **build** prepares something downstream steps can use, such as a directory of ready-to-serve files. A **deployment** installs or starts a version in an environment. Your first CI workflow will check a page before it goes anywhere.

:::single-choice{#ci-overview-output-vs-live} Tests passed and a site archive was produced. What evidence would show visitors can use that version?

::option[A second copy of the check log.]{#ci-overview-output-vs-live-a explanation="The log describes the check and build."}
::option[The existence of the archive.]{#ci-overview-output-vs-live-b explanation="An archive can exist without being served."}
::option[A deployment record and a successful request to the intended page.]{#ci-overview-output-vs-live-c .correct explanation="These connect the built version to a response from the target."}
:::

## Summary

You can now explain where CI fits in a change's path.

1. Associate a check with a specific revision.
2. Use a failed check to identify the first question to investigate.
3. Distinguish checking, building, and deploying.
