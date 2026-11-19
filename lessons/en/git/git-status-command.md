---
lesson_id: "git-status-command"
course_id: "git"
lang: "en"
order_index: 2
title: "git status"
description: "Learn to identify untracked, staged, and modified files with git status."
meta_title: "git status - Git"
meta_description: "Learn to identify untracked, staged, and modified files with git status."
meta_keywords: "git status, git, devops, Linux Journey"
---

When you work inside a repository, `git status` tells you what Git sees in the working tree and what you have selected to save next. Use the empty `journey-git` repository from the previous lesson.

## Finding a New File

Create a small page, then use the short output format to keep the example compact.

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

Here `>` writes to the named file and replaces its contents if it already exists. For a new file, the short status line is `?? index.html`. Git calls it **untracked**. The file exists, but Git has yet to select it for a saved snapshot.

:::single-choice{#git-status-command-untracked-file} Git prints two question marks next to a new file. What does that say about the file?

::option[It is part of the last saved snapshot.]{#git-status-command-untracked-file-a explanation="An untracked file has no entry in that snapshot."}
::option[It was removed from the working tree.]{#git-status-command-untracked-file-c explanation="Git sees this file in your working tree."}
::option[It exists and is outside the next snapshot so far.]{#git-status-command-untracked-file-b .correct explanation="You can choose to add the file to the staging area."}
:::

![Git short status showing index.html move from untracked to staged](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## Looking at Staged Changes

Run `git add` to select the current contents of the file for the next saved snapshot, called a **commit**. The **staging area** is that selection. The abbreviated status now shows an `A` in the first column for the addition waiting to be saved.

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} After git add, where is the selected version of index.html?

::option[In a new commit already.]{#git-status-command-staged-new-a explanation="Git add prepares the next commit. It does not create one."}
::option[In the staging area.]{#git-status-command-staged-new-c .correct explanation="Git has selected the contents that were present when you ran git add."}
::option[In another person's repository.]{#git-status-command-staged-new-b explanation="This changes only your local staging area."}
:::

## Checking Two Kinds of Change

Short status has two columns before the filename. Read the first for staged changes and the second for changes you made since staging. For example, `AM index.html` means Git has staged a new file and you have since modified your working copy. If you prefer headings, plain `git status` lists the details in groups.

:::single-choice{#git-status-command-two-columns} You see AM beside index.html. What should you check before the next commit?

::option[Whether the staged copy includes the edit you want to save.]{#git-status-command-two-columns-a .correct explanation="The second-column M tells you that the working copy contains a later edit."}
::option[Whether the repository has another file called AM.]{#git-status-command-two-columns-b explanation="AM is a pair of status markers for index.html."}
::option[Whether the file has been deleted from disk.]{#git-status-command-two-columns-c explanation="The M describes a modification in the working tree."}
:::

## Summary

You can now check which changes Git would save next.

1. Recognize a new untracked file.
2. Stage a file with git add.
3. Read staged and working-tree changes separately.
