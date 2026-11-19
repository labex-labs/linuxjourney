---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "en"
order_index: 5
title: "Workflow Logs"
description: "Learn to find a failing workflow step and interpret the first actionable log message."
meta_title: "Workflow Logs - Continuous Integration"
meta_description: "Learn to find a failing workflow step and interpret the first actionable log message."
meta_keywords: "workflow logs, continuous integration, devops, Linux Journey"
---

A workflow result gives you an overall status. To understand a failure, expand the failing job and read its steps in order. A later step can be skipped because an earlier one did not complete successfully.

## Finding the First Failure

This simulated run shows the state of each step in the page check job.

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

Start with `Build page`. The skipped checks give no result for the page. Once the failure is fixed, verify the later steps in a new run.

:::single-choice{#ci-workflow-logs-first-failure} Which step's output should you read first?

::option[Package site, because it appears last.]{#ci-workflow-logs-first-failure-a explanation="The package command was skipped in this run."}
::option[Check heading, because the workflow is for a page.]{#ci-workflow-logs-first-failure-c explanation="The status says the heading check did not run."}
::option[Build page, because it failed before the other steps ran.]{#ci-workflow-logs-first-failure-b .correct explanation="Its log gives the reason the following steps were skipped."}
:::

![Simulated CI run showing a failed build and skipped downstream steps](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## Following the Error Message

The failing step shows these lines.

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

The message names the destination path. If the parent directory `dist` is missing, the copy cannot create a file inside it. Check whether an earlier command created that directory before copying. Exit code 1 tells you the command failed. The message gives you the place to look.

:::single-choice{#ci-workflow-logs-actionable-log} Given that dist is missing, which change addresses the reported problem?

::option[Change the heading checked by grep.]{#ci-workflow-logs-actionable-log-b explanation="The heading check did not run and gives no evidence of bad text."}
::option[Create dist before copying the file.]{#ci-workflow-logs-actionable-log-a .correct explanation="The destination requires its parent directory."}
::option[Download an artifact from the skipped step.]{#ci-workflow-logs-actionable-log-c explanation="The package step produced no artifact here."}
:::

## Checking a New Run

After fixing the build, compare the new run's revision and step statuses. A successful copy establishes that the output file exists. Read the test and package results before saying the whole process passed. Keep the first useful error with its step name when reporting a problem.

:::single-choice{#ci-workflow-logs-rerun-evidence} A new run shows Build page passed and Check heading failed. What changed?

::option[The build succeeded and the heading check now has a result to investigate.]{#ci-workflow-logs-rerun-evidence-c .correct explanation="The first remaining failure has moved to the test step."}
::option[The new run is irrelevant because the old build failed.]{#ci-workflow-logs-rerun-evidence-a explanation="Each run gives evidence for its own revision."}
::option[The package must have passed because the build passed.]{#ci-workflow-logs-rerun-evidence-b explanation="A later step may still fail or be skipped."}
:::

## Summary

You can now read a workflow failure in context.

1. Locate the first unsuccessful step that ran.
2. Use the log line to identify what to inspect.
3. Check the new revision and later steps after a fix.
