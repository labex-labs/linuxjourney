---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "en"
order_index: 7
title: "Workflow Permissions"
description: "Learn to give a routine CI check only the repository access it needs."
meta_title: "Workflow Permissions - Continuous Integration"
meta_description: "Learn to give a routine CI check only the repository access it needs."
meta_keywords: "workflow permissions, continuous integration, devops, Linux Journey"
---

A CI job can run commands and may also receive credentials. A **permission** sets what those credentials may read or change. A job that only checks the page usually needs to read source files.

## Giving a Check Read Access

This GitHub Actions excerpt limits the workflow's built-in token to read access for repository contents.

```yaml
permissions:
  contents: read
```

The checkout and local test can read the repository. A job that publishes a package needs access to a different action on a different resource. Give publishing access to the specific job that needs it.

:::single-choice{#ci-workflow-permissions-choose-permission} A job reads the page and runs grep. Which repository content permission fits?

::option[Write, because test output is written to the terminal.]{#ci-workflow-permissions-choose-permission-a explanation="Writing to the terminal does not require permission to change repository contents."}
::option[Read.]{#ci-workflow-permissions-choose-permission-c .correct explanation="The job needs to retrieve content and has no repository edit to perform."}
::option[Write, because the source is in a Git repository.]{#ci-workflow-permissions-choose-permission-b explanation="Reading source files is enough for the check described."}
:::

## Handling Sensitive Values

A **secret** is a value such as a private token. Use the platform's secret storage when an approved job needs one. Keep ordinary page settings separate from secrets. Routine checks against a local sample should work without publishing credentials.

:::single-choice{#ci-workflow-permissions-secret-needed} Which value belongs in controlled secret storage?

::option[A private credential for uploading a package.]{#ci-workflow-permissions-secret-needed-a .correct explanation="A credential can grant access to another system."}
::option[The text Welcome used in the test.]{#ci-workflow-permissions-secret-needed-b explanation="This is public example content."}
::option[The output directory name dist.]{#ci-workflow-permissions-secret-needed-c explanation="The directory name is ordinary configuration."}
:::

## Keeping Logs Useful

Workflow logs can be shared with other people. Report the action and its result without printing secret values. A failure can say that a required credential was unavailable or that access was denied. Give a maintainer the job name and revision to investigate. Keep the credential's value out of the message.

:::single-choice{#ci-workflow-permissions-safe-diagnostic} A publish job cannot authenticate. Which log message helps a reviewer without exposing the credential?

::option[Print the complete credential so it can be copied.]{#ci-workflow-permissions-safe-diagnostic-a explanation="Anyone with log access could see a printed credential."}
::option[Print all environment values to show the job state.]{#ci-workflow-permissions-safe-diagnostic-c explanation="Broad environment output can contain sensitive values."}
::option[Report which publish step failed and its access result.]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="The reviewer can locate the failure and check configured access independently."}
:::

## Reviewing a New Job

A proposed workflow runs page checks on pull requests and adds a package publisher. The two jobs need different access. Keep the check's read permission narrow and grant any approved publishing permission only where the workflow actually publishes.

:::single-choice{#ci-workflow-permissions-final-application} Which revision of the proposal best matches the two jobs' needs?

::option[Give both jobs write access to the repository.]{#ci-workflow-permissions-final-application-b explanation="The check only reads the source, and repository write may not be the permission needed for package publication."}
::option[Use one shared upload credential in all steps so reruns behave consistently.]{#ci-workflow-permissions-final-application-c explanation="An upload credential is only needed in the job that publishes."}
::option[Keep checks read-only and grant the publishing job only its required package access.]{#ci-workflow-permissions-final-application-a .correct explanation="This preserves enough access for each job and reduces privileges elsewhere."}
:::

## Summary

You can now reason about access for a small CI pipeline.

1. Match repository permissions to the work a job needs.
2. Store private credentials through controlled inputs.
3. Record useful errors while protecting credential values.
