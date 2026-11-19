---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "en"
order_index: 7
title: "Pull Requests"
description: "Learn to read a pull request and identify what a review or automated check actually covers."
meta_title: "Pull Requests - Git"
meta_description: "Learn to read a pull request and identify what a review or automated check actually covers."
meta_keywords: "pull requests, git, devops, Linux Journey"
---

A **pull request**, often shortened to PR, proposes that changes from one branch enter another branch. Git tracks commits and branches. A hosting service adds the review page, discussion, and checks around those changes.

## Reading the Source and Target

Suppose a teammate proposes a status page for the site. The review page shows `health-page → main`. The source, sometimes called the **head**, supplies the proposed work. The target, sometimes called the **base**, is the branch that would receive it.

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

At this stage the review page describes a proposed change. The target branch receives the change when the PR is merged.

:::single-choice{#git-pull-requests-pr-direction} Which branch receives the health page when this PR is merged?

::option[A branch named after the commit ID.]{#git-pull-requests-pr-direction-a explanation="That value identifies a snapshot, not the target branch."}
::option[Main.]{#git-pull-requests-pr-direction-b .correct explanation="The target is main, so it receives the reviewed change."}
::option[Health-page.]{#git-pull-requests-pr-direction-c explanation="Health-page is the source providing the change."}
:::

## Checking the Diff

Open the changed-files view and read the diff relative to the PR's target. A one-line addition to `health.txt` is consistent with a small health page. If the review also shows a change to `index.html`, check whether that change belongs in the same proposal. Review the files the PR actually lists.

:::single-choice{#git-pull-requests-unexpected-file} A PR titled Add a health page also edits the homepage. Where do you verify the exact edit?

::option[In the changed-files diff.]{#git-pull-requests-unexpected-file-a .correct explanation="The diff shows which lines the proposal changes."}
::option[In the title alone.]{#git-pull-requests-unexpected-file-b explanation="The title summarizes intent and can omit details."}
::option[In the branch name.]{#git-pull-requests-unexpected-file-c explanation="The branch name labels a line of work and does not describe every change."}
:::

## Reading Automated Checks

A hosting service can run a test when a PR changes. Look for the commit or revision the result covers. If another commit is pushed after a passing run, verify that the updated revision has the required checks. A passing result says the checks that actually ran passed.

:::single-choice{#git-pull-requests-changed-revision} A test passed for 3ab4501. The PR now points to 78ac900. What should you check before relying on the result?

::option[Whether the original commit message was well written.]{#git-pull-requests-changed-revision-a explanation="The message does not show test coverage for the newer commit."}
::option[Whether the PR still has the same title.]{#git-pull-requests-changed-revision-b explanation="The title can stay the same as the code changes."}
::option[Whether the checks ran for the updated revision.]{#git-pull-requests-changed-revision-c .correct explanation="The earlier result covered a different revision."}
:::

## Summary

You can now read what a pull request proposes and what evidence supports merging it.

1. Find the source and target branches.
2. Verify the proposed edits in the changed-files view.
3. Check which revision the automated result covers.
