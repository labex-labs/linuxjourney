---
lesson_id: "git-repositories"
course_id: "git"
lang: "en"
order_index: 1
title: "Repositories"
description: "Learn what a Git repository stores and start an empty repository for a small website."
meta_title: "Repositories - Git"
meta_description: "Learn what a Git repository stores and start an empty repository for a small website."
meta_keywords: "repositories, git, devops, Linux Journey"
---

A website starts with a few files. Git gives you a way to record what those files looked like at particular points in time. The project files and the history together make up your local Git workspace.

## Creating a Repository

Start in a practice directory where you can create a new folder. Run the following commands once. The dollar sign shows the shell prompt.

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

The new folder is your **working tree**, where you edit project files. Git creates a hidden `.git` directory there to store history and settings. This new repository has no saved changes yet. Git calls the initial line of work `main`.

:::single-choice{#git-repositories-empty-history} You initialize a repository that already contains index.html. What happens to that file's history?

::option[Git immediately records the file as its first commit.]{#git-repositories-empty-history-b explanation="Initializing does not capture any project files."}
::option[Git can record it in a future commit.]{#git-repositories-empty-history-a .correct explanation="Initialization prepares the repository. Saving a snapshot is a separate action."}
::option[Git moves the file into the hidden Git directory.]{#git-repositories-empty-history-c explanation="Project files stay in the working tree where you can edit them."}
:::

![LabEx terminal showing an empty Git repository initialized and the practice folder reported as its root](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## Recognizing the Working Tree

Use `git rev-parse --show-toplevel` to print the root of the current repository. A shell inside the practice folder should report a path ending in `journey-git`. A folder inside that working tree still belongs to the same repository unless it contains a separate repository of its own.

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} You enter a subdirectory named images in journey-git. Which directory should Git report as the top level?

::option[The journey-git directory.]{#git-repositories-find-root-b .correct explanation="Git finds the repository root above your current location."}
::option[The images subdirectory.]{#git-repositories-find-root-a explanation="The top level belongs to the repository, even when your shell is in a subdirectory."}
::option[The hidden .git directory.]{#git-repositories-find-root-c explanation="The command reports the working tree root, where the project files are kept."}
:::

## Starting with Existing History

Use `git clone` when there is already a repository you want to copy. A normal clone creates a new local working tree and imports the existing repository history. Use `git init` for a project whose history you are starting locally. You will keep using `journey-git` in the following lessons.

:::single-choice{#git-repositories-choose-start} A teammate gave you the address of a repository whose history you need. Which starting action fits?

::option[Create an empty folder and initialize it.]{#git-repositories-choose-start-a explanation="A new repository starts without the teammate's history."}
::option[Copy only the visible website files.]{#git-repositories-choose-start-b explanation="The visible files give you one version and leave out the repository history."}
::option[Clone the teammate's repository.]{#git-repositories-choose-start-c .correct explanation="Cloning copies the shared history and gives you a local working tree."}
:::

## Summary

You can now choose how to start a local Git repository.

1. Identify the working tree and Git's hidden directory.
2. Find the root when you are in a subdirectory.
3. Choose initialization for a new history or cloning for an existing history.
