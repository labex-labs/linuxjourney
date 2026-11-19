---
lesson_id: "git-revert-command"
course_id: "git"
lang: "en"
order_index: 8
title: "git revert"
description: "Learn how git revert records an undo operation without rewriting the original commit."
meta_title: "git revert - Git"
meta_description: "Learn how git revert records an undo operation without rewriting the original commit."
meta_keywords: "git revert, git, devops, Linux Journey"
---

A change that has already been shared can still be undone. Use `git revert` to apply the opposite change as a new commit. The history then shows both the original change and the decision to undo it.

## Finding the Change to Undo

In the practice repository, `main` contains the homepage and health page commits. Use short history to confirm the newest entry. The identifiers below are illustrative.

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD` refers to the commit you currently have checked out. Check that it is the change you intend to undo. Check `git status` for a clean working tree before proceeding.

:::single-choice{#git-revert-command-newest-commit} Which change would reverting HEAD undo in this sample?

::option[The older homepage heading change.]{#git-revert-command-newest-commit-b explanation="The heading change is the previous commit."}
::option[Both changes in a single operation.]{#git-revert-command-newest-commit-c explanation="Here HEAD names one commit and the revert applies to that commit."}
::option[The addition of the health page.]{#git-revert-command-newest-commit-a .correct explanation="HEAD is on the newest entry shown on this branch."}
:::

## Recording the Undo

In the clean practice repository, revert the health page commit. This changes the files in your working tree and creates a commit. Use `--no-edit` to keep Git's proposed revert message.

```bash
$ git revert --no-edit HEAD
```

This example removes the health file because the original commit added it. If newer work changed the same lines, Git can stop and ask for help reconciling the changes. Read status before continuing.

:::single-choice{#git-revert-command-undo-effect} When the sample revert succeeds, which project file change should you observe?

::option[The homepage file is deleted along with the health page.]{#git-revert-command-undo-effect-a explanation="The older homepage commit remains in effect."}
::option[The health page file is removed.]{#git-revert-command-undo-effect-b .correct explanation="The revert reverses the addition made by the selected commit."}
::option[The health page is added a second time.]{#git-revert-command-undo-effect-c explanation="Revert applies an inverse change and does not replay the addition."}
:::

![Git history showing the new revert entry and the original health page commit](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## Checking History After the Undo

Run `git log --oneline` again. Expect a new revert entry above the original health page entry. Check `git status --short` for remaining local changes. The new commit can be reviewed and shared through the same process as other changes.

:::single-choice{#git-revert-command-history-after-revert} What should still appear below the new revert entry?

::option[The original health page commit.]{#git-revert-command-history-after-revert-c .correct explanation="The pair records the original change and its undo."}
::option[Only the initial heading commit.]{#git-revert-command-history-after-revert-a explanation="The original health page commit remains present in history."}
::option[No commits at all.]{#git-revert-command-history-after-revert-b explanation="A revert adds a commit without replacing the branch history."}
:::

## Leaving Other Work in Place

Suppose the history contains three separate changes. The health file was added first, a typo was fixed in the homepage next, and both were shared. Reverting the identified health-file commit can undo that addition while keeping the unrelated typo fix. Read the history and the affected files before choosing a commit.

:::single-choice{#git-revert-command-final-application} Which check shows that the undo kept the intended work?

::option[The health-file commit disappeared from the log.]{#git-revert-command-final-application-b explanation="A revert leaves the original entry in the history."}
::option[The typo fix also disappeared from the homepage.]{#git-revert-command-final-application-c explanation="The typo fix was a separate change and should remain."}
::option[The health file is gone, the corrected homepage remains, and history shows the revert.]{#git-revert-command-final-application-a .correct explanation="These observations cover the selected inverse, the unrelated change, and the new history entry."}
:::

## Summary

You can now undo a committed change while keeping a trace of both actions.

1. Identify the exact commit to reverse.
2. Revert it in a clean working tree.
3. Verify both entries in the history.
