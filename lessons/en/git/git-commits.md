---
lesson_id: "git-commits"
course_id: "git"
lang: "en"
order_index: 4
title: "Commits"
description: "Learn to save a staged snapshot and identify it in Git history."
meta_title: "Commits - Git"
meta_description: "Learn to save a staged snapshot and identify it in Git history."
meta_keywords: "commits, git, devops, Linux Journey"
---

A **commit** records the files selected in the staging area. It also records a message, an author, and how it connects to earlier commits. You can use the identifier Git assigns to find that exact point in the history.

## Setting an Identity for the Practice Repository

Git records a name and email with a commit. Set example values for this repository only. These values are labels in the history, so they do not grant access to a remote service.

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

Use the practice repository with `index.html` staged. Run `git status` if you need to check which files will go into the commit.

:::single-choice{#git-commits-identity-scope} What does the --local choice do here?

::option[It signs you in to a shared hosting service.]{#git-commits-identity-scope-b explanation="Name and email are commit metadata. Remote authentication is separate."}
::option[It sets the author information for this repository.]{#git-commits-identity-scope-a .correct explanation="The local settings apply to the current repository."}
::option[It changes the author on all existing commits.]{#git-commits-identity-scope-c explanation="The settings are used for future commits."}
:::

## Saving the Snapshot

Run `git commit` after staging the version you want. The `-m` option supplies the message on the command line.

```bash
$ git commit -m "Set the homepage heading"
```

A commit captures the staged version of a file. If you edit the working tree again after staging, that later edit remains outside the commit until you stage it.

:::single-choice{#git-commits-staged-snapshot} You staged Welcome and then typed Hi in the file without staging again. Which heading will the commit contain?

::option[Welcome, because that was the version you staged.]{#git-commits-staged-snapshot-c .correct explanation="Commit reads the staged contents for the snapshot."}
::option[Hi, because it is the newest text on disk.]{#git-commits-staged-snapshot-a explanation="The newest working copy can differ from the staged copy."}
::option[Both, because Git saves every edit automatically.]{#git-commits-staged-snapshot-b explanation="The staged snapshot contains one selected version of the file."}
:::

## Reading a Short History

Use `git log --oneline` to see compact history. Each row starts with an abbreviated commit identifier, followed by its message. Your identifier will differ from the example.

```text
$ git log --oneline
a12c345 Set the homepage heading
```

Use the identifier to refer to the exact commit, since separate commits can carry identical messages. The display normally starts with the newest commit in the current line of history.

:::single-choice{#git-commits-identify-snapshot} Two commits have the message Set the homepage heading. What distinguishes their individual snapshots?

::option[The shared commit message.]{#git-commits-identify-snapshot-a explanation="The same text can appear on multiple commits."}
::option[The filename affected by both changes.]{#git-commits-identify-snapshot-c explanation="The same file may be part of many commits."}
::option[The commit identifier.]{#git-commits-identify-snapshot-b .correct explanation="Each identifier lets you refer to a particular entry."}
:::

To practice staging and committing in a browser terminal, try [Your First Git Lab](https://labex.io/tutorials/git-your-first-git-lab-92739).

## Summary

You can now save staged work and locate it in history.

1. Set a commit identity for a practice repository.
2. Save the staged snapshot with a clear message.
3. Identify a commit in the abbreviated history.
