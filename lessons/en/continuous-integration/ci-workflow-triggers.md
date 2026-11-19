---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "en"
order_index: 2
title: "Workflow Triggers"
description: "Learn to predict when a GitHub Actions workflow runs from its event and branch filters."
meta_title: "Workflow Triggers - Continuous Integration"
meta_description: "Learn to predict when a GitHub Actions workflow runs from its event and branch filters."
meta_keywords: "workflow triggers, continuous integration, devops, Linux Journey"
---

A workflow needs a reason to run. In GitHub Actions, the `on` section names events that can start it. An **event** can be a push to a branch, a change to a pull request, or another supported action.

## Checking a Push

Read this excerpt from a workflow. YAML uses the indentation to show that `branches` is a setting for `push`.

```yaml
on:
  push:
    branches:
      - main
```

This workflow runs when a commit is pushed to the `main` branch, assuming the workflow is enabled and other required conditions are met. Committing in a local terminal does not send the change to GitHub. The push is what this excerpt watches.

:::single-choice{#ci-workflow-triggers-push-filter} Which action matches that push trigger?

::option[Committing locally on main.]{#ci-workflow-triggers-push-filter-a explanation="The trigger watches a repository event on GitHub."}
::option[Pushing a commit to a branch named draft.]{#ci-workflow-triggers-push-filter-b explanation="The branch filter selects main."}
::option[Pushing the commit to main.]{#ci-workflow-triggers-push-filter-c .correct explanation="That event matches both push and the branch filter."}
:::

## Checking a Pull Request

A second event can cover proposed changes before they are merged. In this excerpt the branch filter applies to the pull request's target branch.

```yaml
on:
  pull_request:
    branches:
      - main
```

A proposal from `health-page` into `main` matches that filter. With the default activity types, opening the request and pushing another commit to its head branch are examples of changes that can trigger the workflow.

:::single-choice{#ci-workflow-triggers-pr-target} A pull request proposes notes into main. Which name matters for this branch filter?

::option[Notes, the source branch.]{#ci-workflow-triggers-pr-target-b explanation="Notes contains the work being proposed."}
::option[Main, the target branch.]{#ci-workflow-triggers-pr-target-a .correct explanation="The pull request branch filter applies to the base or receiving branch."}
::option[The filename edited by the proposal.]{#ci-workflow-triggers-pr-target-c explanation="The excerpt filters on branch names."}
:::

## Reading More Than One Trigger

A file can list both events below the same `on` key. A pull request run may cover the proposed integration. After a merge updates `main`, a push run can cover the state now on that branch. These results belong to the event and revision shown in each run.

:::single-choice{#ci-workflow-triggers-after-merge} A workflow has the two triggers shown above. A merge updates main. Which listed event matches that update?

::option[A push to main.]{#ci-workflow-triggers-after-merge-b .correct explanation="The receiving branch was updated and matches the push filter."}
::option[A pull request being opened on a new branch.]{#ci-workflow-triggers-after-merge-a explanation="The action described is an update to main after merging."}
::option[A local commit with no remote update.]{#ci-workflow-triggers-after-merge-c explanation="Main on GitHub already changed in the scenario."}
:::

## Summary

You can now match a workflow trigger to a repository event.

1. Read a push event and its branch filter.
2. Identify the target branch of a pull request trigger.
3. Connect a workflow result to its triggering event.
