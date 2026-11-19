---
lesson_id: "git-remotes"
course_id: "git"
lang: "en"
order_index: 6
title: "Remotes"
description: "Learn how a Git remote connects repositories and distinguish fetching from pushing."
meta_title: "Remotes - Git"
meta_description: "Learn how a Git remote connects repositories and distinguish fetching from pushing."
meta_keywords: "remotes, git, devops, Linux Journey"
---

A **remote** is a named address that your local Git repository can use to contact another repository. The other repository can live on a hosting service or in a directory on the same machine. This practice example uses a separate local directory, so it works without a hosting account.

## Adding an Address

From the practice repository, create a separate **bare** repository. A bare repository holds history and refs without a project working tree. It can receive commits from your workspace. A fresh practice run needs an unused `journey-remote.git` directory.

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

The name `origin` is a common convention. The remotes listing shows which address that name refers to.

:::single-choice{#git-remotes-add-address} You ran git remote add and saw origin in the list. What did Git do?

::option[Saved a name for the other repository.]{#git-remotes-add-address-b .correct explanation="You can refer to that address as origin in later commands."}
::option[Uploaded all local commits.]{#git-remotes-add-address-a explanation="Adding a remote records an address. An upload uses push."}
::option[Cloned another working tree into your project.]{#git-remotes-add-address-c explanation="The existing working tree stays where it was."}
:::

## Sending a Branch

Use `git push` to send local commits and ask the remote to update its branch. The `-u` option records the remote branch as the upstream, the branch Git associates with your local one for later commands.

```bash
$ git push -u origin main
```

This pushes only to the separate practice directory. A shared remote may require authorization and can reject updates, so check its response before treating a push as successful.

:::single-choice{#git-remotes-push-direction} Which command sends a new local main commit to this remote?

::option[git fetch origin]{#git-remotes-push-direction-b explanation="Fetch gets information from the remote into the local repository."}
::option[git remote -v]{#git-remotes-push-direction-c explanation="This displays which address origin uses."}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="Push transfers the commits the remote needs and requests a branch update."}
:::

## Receiving an Update

Use `git fetch origin` to refresh your local view of remote history. Git uses a **remote-tracking branch**, such as `origin/main`, to record what it last learned. You can inspect it with `git log --oneline origin/main`. Fetch by itself leaves the checked-out working tree on your current local branch.

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} origin/main moved after a fetch, but your local main stayed put. Which statement fits?

::option[Fetch rewrote the files you were editing.]{#git-remotes-after-fetch-a explanation="Fetch updates the recorded view of the remote branch."}
::option[Git learned about the remote change, and integration is a separate step.]{#git-remotes-after-fetch-c .correct explanation="Your local branch can remain where it was while origin/main advances."}
::option[Your push updated the remote during the fetch.]{#git-remotes-after-fetch-b explanation="Fetch transfers information in the receive direction."}
:::

## Summary

You can now track which repository a Git command affects.

1. Add and inspect a remote address.
2. Push a branch and identify its upstream.
3. Fetch new remote history without changing the checked-out files.
