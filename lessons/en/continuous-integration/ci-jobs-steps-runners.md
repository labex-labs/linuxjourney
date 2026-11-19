---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "en"
order_index: 3
title: "Jobs, Steps, and Runners"
description: "Learn to find a workflow's jobs, steps, and runner in a short GitHub Actions file."
meta_title: "Jobs, Steps, and Runners - Continuous Integration"
meta_description: "Learn to find a workflow's jobs, steps, and runner in a short GitHub Actions file."
meta_keywords: "jobs, steps, and runners, continuous integration, devops, Linux Journey"
---

A workflow is the whole automated process. A **job** groups work assigned to a **runner**, which is the machine or environment that executes it. A **step** is one operation inside a job.

## Reading a Small Workflow

This example runs one job on a GitHub-hosted Ubuntu runner. A workflow like this lives under `.github/workflows/` in a GitHub repository.

```yaml
name: Page check
on: push
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the repository
        uses: actions/checkout@v6
      - name: Find the heading
        run: grep -q '<h1>Welcome</h1>' index.html
```

The job ID is `check`. The `runs-on` field selects the environment. `uses` invokes a reusable action, here to make repository files available. `run` executes a command on the runner.

:::single-choice{#ci-jobs-steps-runners-job-fields} Which field selects where the check job runs?

::option[Runs-on.]{#ci-jobs-steps-runners-job-fields-a .correct explanation="It specifies the runner type for the job."}
::option[Uses.]{#ci-jobs-steps-runners-job-fields-b explanation="This step invokes the checkout action."}
::option[Name.]{#ci-jobs-steps-runners-job-fields-c explanation="The name gives the workflow a label."}
:::

## Following the Steps

Steps in one job run in their listed order by default. The check reads a file from the repository, so checkout comes first. A later step in the same job can use files written by an earlier step.

:::single-choice{#ci-jobs-steps-runners-step-order} What would the grep step be missing if checkout were moved after it on a fresh runner?

::option[The name of the job.]{#ci-jobs-steps-runners-step-order-a explanation="The job is already selected by the workflow."}
::option[The Ubuntu runner itself.]{#ci-jobs-steps-runners-step-order-c explanation="The runner is selected before executing the steps."}
::option[The project file it needs to read.]{#ci-jobs-steps-runners-step-order-b .correct explanation="Checkout makes the repository files available before the check."}
:::

## Keeping Jobs Separate

Separate jobs may run at the same time. Each GitHub-hosted job gets its own runner, so a file written in one job is unavailable in another unless the workflow transfers it. If one job depends on another job's success, declare the dependency with `needs` and use an artifact to move files when required.

:::single-choice{#ci-jobs-steps-runners-separate-jobs} A build job writes site.tar.gz. A later job runs on another hosted runner. How should it receive the file?

::option[Assume it stayed in the same working directory.]{#ci-jobs-steps-runners-separate-jobs-a explanation="A separate hosted runner starts with its own filesystem."}
::option[Transfer the file as an artifact.]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="The workflow can upload it in one job and download it in the other."}
::option[Set needs so the second job waits for the build.]{#ci-jobs-steps-runners-separate-jobs-b explanation="Needs controls ordering. The build file still needs to be transferred between runners."}
:::

To write and run a workflow in a GitHub repository, try [GitHub Actions for Beginners](https://labex.io/courses/github-actions-for-beginners). The lab course requires a GitHub account.

## Summary

You can now read the main parts of a CI workflow.

1. Find a job and its runner.
2. Interpret a reusable action and a shell step.
3. Recognize when jobs need a dependency or a file transfer.
