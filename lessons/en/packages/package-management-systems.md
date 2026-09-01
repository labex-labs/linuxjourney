---
lesson_id: "package-management-systems"
course_id: "packages"
lang: "en"
order_index: 6
title: "yum and apt"
description: "Learn the repository-aware APT and DNF workflows for inspecting, installing, removing, and upgrading packages."
meta_title: "yum and apt - Packages"
meta_description: "Explore the key differences in the yum vs apt debate. This guide covers how to use yum and apt for installing, removing, and updating packages on RPM and Debian-based Linux systems."
meta_keywords: "yum vs apt, yum apt, linux package management, apt, yum, debian, red hat, install packages, update packages, linux commands"
---

Repository-aware package managers retrieve metadata, solve dependencies, verify authenticated content, and coordinate transactions. Debian-family systems commonly use APT. Current Fedora and Red Hat Enterprise Linux releases use DNF; on current RHEL, the `yum` command remains as a compatibility alias for DNF, while older systems used the original YUM implementation.

Always follow the documentation for the installed distribution and release rather than assuming one command set applies everywhere.

## Refreshing and Inspecting Metadata

APT separates metadata refresh from package upgrades:

```bash
Debian family: $ sudo apt update
```

Search and inspect before installation:

```bash
Debian family: $ apt search package-name
Debian family: $ apt show package-name
RPM family:    $ dnf search package-name
RPM family:    $ dnf info package-name
```

Repository configuration determines what these commands can discover. Read source names, architectures, versions, and signing errors carefully.

:::single-choice{#package-management-systems-apt-show} Which command displays APT package details for `package-name`?

::option[`apt remove package-name`]{#package-management-systems-apt-remove-command explanation="The `remove` subcommand proposes uninstalling the package."}
::option[`dnf search package-name`]{#package-management-systems-dnf-search-command explanation="This searches RPM-family repositories and is not the APT detail command."}
::option[`apt show package-name`]{#package-management-systems-apt-show-command .correct explanation="The `show` subcommand presents metadata for the named binary package."}
:::

## Installing Packages

Install by repository package name with:

```bash
Debian family: $ sudo apt install package-name
RPM family:    $ sudo dnf install package-name
```

The manager proposes dependencies and any conflicts or replacements. Do not confirm automatically until you have reviewed package origin, version, architecture, download size, disk change, removals, and newly installed dependencies.

:::single-choice{#package-management-systems-dnf-install} Which current command installs `package-name` from configured RPM-family repositories?

::option[`rpm -qa package-name`]{#package-management-systems-rpm-query-command explanation="This is an RPM installed-database query, not a repository install request."}
::option[`dnf install package-name`]{#package-management-systems-dnf-install-command .correct explanation="DNF is the current repository-aware manager on Fedora and recent RHEL releases."}
::option[`apt update package-name`]{#package-management-systems-apt-update-package explanation="APT update refreshes indexes and does not install a named RPM-family package."}
:::

## Removing Packages

Request removal with:

```bash
Debian family: $ sudo apt remove package-name
RPM family:    $ sudo dnf remove package-name
```

Removal can affect dependent packages or leave now-unused dependencies and configuration. Review the proposed transaction, distinguish remove from purge semantics on Debian-family systems, and preserve application data according to its own backup and retention procedure. Package removal does not promise to delete user-created data.

:::single-choice{#package-management-systems-remove-review} Why should you review a removal transaction before confirming it?

::option[Removal always reformats the filesystem containing the package.]{#package-management-systems-removal-format explanation="Package managers remove managed files and state; they do not ordinarily format a filesystem."}
::option[Package managers cannot display a proposed change set.]{#package-management-systems-no-proposal explanation="Interactive managers normally show the planned transaction precisely so it can be reviewed."}
::option[Other packages can depend on the selected package and may also be affected.]{#package-management-systems-dependent-removal .correct explanation="Dependency constraints can expand a request beyond the one package name originally entered."}
:::

## Applying Updates

On an APT system, refresh metadata and then review upgrades as separate successful steps:

```bash
$ sudo apt update
$ apt list --upgradable
$ sudo apt upgrade
```

On a DNF system, inspect and apply available updates with the locally documented workflow:

```bash
$ dnf check-update
$ sudo dnf upgrade
```

An update command can change core libraries, services, kernels, and dependencies. Use backups, maintenance policy, release notes, and restart or reboot planning appropriate to the system. Check command exit semantics: for example, some “check update” operations use a nonzero status to report that updates are available rather than an execution failure.

:::single-choice{#package-management-systems-apt-update-upgrade} What is the relationship between `apt update` and `apt upgrade`?

::option[`update` removes packages; `upgrade` restores their configuration files.]{#package-management-systems-apt-remove-restore explanation="Neither command has that remove-and-restore relationship."}
::option[`update` refreshes metadata; `upgrade` applies an approved package upgrade plan.]{#package-management-systems-apt-two-steps .correct explanation="APT separates catalog refresh from installation of newer package versions."}
::option[They are identical names for one operation.]{#package-management-systems-apt-identical explanation="They perform distinct stages and should be checked separately."}
:::

## Choosing `dnf` or `yum`

Use `dnf` in current Fedora and RHEL documentation. A `yum` command on a recent RHEL system can invoke DNF compatibility behavior, but scripts should not infer the implementation from the executable name alone. On legacy hosts, verify the installed version and supported syntax before translating instructions.

:::single-choice{#package-management-systems-yum-current-rhel} What does `yum` commonly represent on a current RHEL system?

::option[A compatibility command backed by DNF.]{#package-management-systems-yum-dnf-alias .correct explanation="Recent RHEL releases use DNF while preserving the yum command name for compatibility."}
::option[The Debian low-level `.deb` archive tool.]{#package-management-systems-yum-dpkg explanation="Debian systems use tools such as APT and dpkg rather than YUM for native package management."}
::option[A compressor for repository metadata only.]{#package-management-systems-yum-compressor explanation="YUM and DNF are package-management interfaces, not standalone compression formats."}
:::

Practice APT in [Installing and Removing Packages](https://labex.io/labs/linux-installing-and-removing-packages-385380) and DNF/YUM-family concepts in [Query and Update Packages with YUM](https://labex.io/labs/rhel-query-and-update-packages-with-yum-in-linux-590869).

## Summary

You can now choose and review common repository package operations.

1. Use APT on Debian-family systems and DNF on current RPM-family systems.
2. Inspect metadata and proposed dependency changes before installation.
3. Treat removal as a dependency-aware transaction, not a single-file deletion.
4. Separate metadata refresh from upgrade application where the tool does.
5. Verify whether `yum` is legacy YUM or a DNF compatibility command.
