---
lesson_id: "git-branches"
course_id: "git"
lang: "en"
order_index: 5
title: "Branches"
description: "Learn how Git branches identify different lines of work and how a merge brings a change into main."
meta_title: "Branches - Git"
meta_description: "Learn how Git branches identify different lines of work and how a merge brings a change into main."
meta_keywords: "branches, git, devops, Linux Journey"
---

A **branch** is a name that points to a commit. When you make a new commit on your current branch, its name advances to the new entry. Another branch keeps its own position until you update it.

## Starting a Separate Line of Work

From `main` in the practice repository, create and switch to a branch named `health-page`. The `-c` option on `git switch` means create.

```bash
$ git switch -c health-page
```

Both names point to the same commit at first. Use `git branch --show-current` to check which name your next commit will advance.

:::single-choice{#git-branches-start-pointer} Right after git switch -c health-page, which commit does the new name point to?

::option[An empty commit created by the command.]{#git-branches-start-pointer-a explanation="The branch command creates a name attached to an existing commit."}
::option[A commit in someone else's repository.]{#git-branches-start-pointer-c explanation="This command creates a local branch in your current repository."}
::option[The commit you started from.]{#git-branches-start-pointer-b .correct explanation="Both names initially point to the same snapshot."}
:::

## Saving a Change on the Branch

Add a one-line status file and commit it while `health-page` is current.

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

Imagine the homepage commit is A and the health page commit is B.

```text
A (main) --- B (health-page)
```

Only `health-page` moved to B. Switching back to `main` with a clean working tree returns your files to the snapshot at A.

:::single-choice{#git-branches-branch-snapshot} Before merging, which branch contains the health page commit?

::option[Both branches, because they share a repository.]{#git-branches-branch-snapshot-a explanation="Branches in one repository can point to different snapshots."}
::option[Health-page only.]{#git-branches-branch-snapshot-c .correct explanation="That was the current branch when commit B was created."}
::option[Main only, because you started there.]{#git-branches-branch-snapshot-b explanation="Main did not move when you committed on health-page."}
:::

## Merging into Main

Switch to the branch that should receive the change, then name the branch you want to merge from.

```bash
$ git switch main
$ git merge health-page
```

Here `main` has no changes of its own after A. Git can move it directly to B, an operation called a **fast-forward**. If the two branches each have new commits, Git may have to combine their changes. Read the result before assuming the merge finished.

:::single-choice{#git-branches-merge-direction} You want main to receive health-page's change. Where do you run the merge?

::option[On main, naming health-page as the source.]{#git-branches-merge-direction-a .correct explanation="The current branch receives the result of the merge."}
::option[On health-page, naming main as the source.]{#git-branches-merge-direction-b explanation="That command would update health-page."}
::option[On a new branch that neither side uses.]{#git-branches-merge-direction-c explanation="Main would keep its original position until it receives the change."}
:::

## Summary

You can now follow a change from a local branch into main.

1. Create a branch at the current commit.
2. Save a change on the intended branch.
3. Merge the change into the branch that should receive it.
