---
lesson_id: "git-diff-command"
course_id: "git"
lang: "en"
order_index: 3
title: "git diff"
description: "Learn to compare working-tree and staged versions of a file with git diff."
meta_title: "git diff - Git"
meta_description: "Learn to compare working-tree and staged versions of a file with git diff."
meta_keywords: "git diff, git, devops, Linux Journey"
---

Status shows which files changed. Use `git diff` to see the lines that changed. In this example, `index.html` already contains a staged Hello heading from the previous lesson.

## Comparing a File with Its Staged Copy

Replace the heading in the practice file and compare the working copy with the staged copy.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

The `--` separates options from the path you want to inspect. In the output, the line beginning with `-` is from the earlier copy. The line beginning with `+` is the replacement. The two lines below are the part of the diff that describes the edit.

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} Which heading is currently in the working copy?

::option[Welcome.]{#git-diff-command-changed-heading-b .correct explanation="The plus line shows the new working-tree text in this comparison."}
::option[Hello.]{#git-diff-command-changed-heading-a explanation="The minus line gives the earlier staged text."}
::option[Both headings.]{#git-diff-command-changed-heading-c explanation="The two lines describe the before and after versions of one line."}
:::

## Comparing the Staging Area with History

Use `git diff --staged -- index.html` to compare the staged version with the most recent commit. Before a first commit, Git compares against an empty starting point. Here, that output shows the staged Hello heading as an addition. At the same time, plain `git diff` shows the later Welcome edit.

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} Which command lets you preview the version that would enter a commit right now?

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="This compares the current working file with the staged file."}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="Status shows where changes exist and omits the changed lines."}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="It compares the selected contents with the previous snapshot."}
:::

![LabEx terminal comparing the Welcome working-tree heading with the staged Hello heading](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## Knowing What an Empty Diff Means

Add the current file again to update the staged copy.

```bash
$ git add index.html
$ git diff -- index.html
```

Plain `git diff` can now be empty because the working file and staged copy match. Use the staged comparison to see the change that still awaits a commit. Git also leaves untracked files out of these ordinary file comparisons. Check status when you are unsure where a change stands.

:::single-choice{#git-diff-command-empty-diff} Plain git diff is empty immediately after you stage the edit. Where can you still see the change against history?

::option[In a second run of plain git diff.]{#git-diff-command-empty-diff-a explanation="Repeating the same comparison still compares equal copies in this case."}
::option[In git diff --staged.]{#git-diff-command-empty-diff-c .correct explanation="This compares the staged copy with the baseline in history."}
::option[Only after you create a commit.]{#git-diff-command-empty-diff-b explanation="You can inspect the planned commit before saving it."}
:::

## Summary

You can now choose a diff that answers the question you have.

1. Read removed and added lines in a diff.
2. Compare the working file with the staging area.
3. Preview the staged changes before a commit.
