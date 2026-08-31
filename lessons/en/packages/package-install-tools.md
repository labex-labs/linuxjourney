---
lesson_id: "package-install-tools"
course_id: "packages"
lang: "en"
order_index: 5
title: "rpm and dpkg"
description: "Learn how `dpkg` and `rpm` inspect and modify their native package databases and local archives."
meta_title: "rpm and dpkg - Packages"
meta_description: "Learn to install, remove, and list packages using rpm and dpkg commands. Understand direct package management for .deb and .rpm files. Start your Linux journey!"
meta_keywords: "rpm, dpkg, Linux package management, .deb, .rpm, Linux tutorial, beginner guide, install packages"
---

`dpkg` is the low-level package tool on Debian-family systems, while `rpm` serves a similar role for RPM-family systems. They unpack native archives, run package lifecycle actions, and update installed-package databases. Repository-aware tools such as APT and DNF build on these lower-level mechanisms.

## Inspecting an Archive Before Installation

A package archive is not equivalent to one executable file. It can contain many payload files, metadata, configuration handling, and privileged lifecycle scripts. Inspect its origin, signature or authenticated download path, metadata, and contents before installation.

```bash
Debian: $ dpkg-deb --info ./some-package.deb
Debian: $ dpkg-deb --contents ./some-package.deb
RPM:    $ rpm -qip ./some-package.rpm
RPM:    $ rpm -qlp ./some-package.rpm
```

The `p` in the shown RPM query forms means “query a package file” rather than the installed database. Query output helps review a package but cannot prove that its scripts or programs are safe.

:::single-choice{#package-install-tools-native-format}
Which low-level tool manages Debian `.deb` packages and their installed database?

::option[`rpm`]{#package-install-tools-rpm-debian explanation="RPM manages its own native format and database on RPM-family systems."}
::option[`tar`]{#package-install-tools-tar-debian explanation="Tar can read archives but does not implement the Debian installed-package lifecycle."}
::option[`dpkg`]{#package-install-tools-dpkg-debian .correct explanation="Debian-family systems use `dpkg` for low-level `.deb` archive and package-database operations."}
:::

## Installing a Local Archive

Direct low-level installation uses:

```bash
Debian: $ sudo dpkg -i ./some-package.deb
RPM:    $ sudo rpm -U ./some-package.rpm
```

`dpkg -i` can unpack and configure the requested archive, but it does not fetch missing repository dependencies. Raw `rpm` similarly does not provide the normal repository solver workflow. A higher-level command is usually preferable for a local archive because it can resolve dependencies from configured sources:

```bash
Debian: $ sudo apt install ./some-package.deb
RPM:    $ sudo dnf install ./some-package.rpm
```

Review the transaction before confirming. A leading `./` distinguishes a local Debian archive path from a repository package name in APT.

:::single-choice{#package-install-tools-local-dependencies}
Which shown command can install a local `.deb` while resolving available repository dependencies?

::option[`dpkg -l ./some-package.deb`]{#package-install-tools-dpkg-list-file explanation="`dpkg -l` lists installed-package selections and is not the local dependency-resolving install workflow."}
::option[`rpm -qa ./some-package.deb`]{#package-install-tools-rpm-query-deb explanation="RPM query syntax does not install a Debian archive."}
::option[`apt install ./some-package.deb`]{#package-install-tools-apt-local .correct explanation="APT recognizes the explicit local path and can use configured repositories to satisfy declared dependencies."}
:::

## Removing an Installed Package

Removal targets an installed package name, not the archive filename used earlier:

```bash
Debian: $ sudo dpkg --remove package-name
RPM:    $ sudo rpm --erase package-name
```

On Debian, `--remove` normally retains configuration files classified as conffiles; `--purge` requests their removal as well, subject to package scripts and unmanaged data. Neither command guarantees deletion of user-created data. Higher-level `apt remove` or `dnf remove` is generally better because it can evaluate related packages and present a complete transaction.

:::single-choice{#package-install-tools-remove-operand}
What operand does `dpkg --remove` expect for an installed package?

::option[The URL of the repository index.]{#package-install-tools-remove-url explanation="Repository location is not the package identity passed to low-level removal."}
::option[The installed package name.]{#package-install-tools-remove-name .correct explanation="Removal addresses the package record, such as `example`, rather than requiring its former `.deb` path."}
::option[The PID of a process started by the package.]{#package-install-tools-remove-pid explanation="Process IDs are unrelated to the installed package database key."}
:::

## Querying Installed State

List installed or known package records with:

```bash
Debian: $ dpkg-query -l
RPM:    $ rpm -qa
```

For targeted inspection, prefer a specific package name and machine-readable format where scripting reliability matters. Package databases describe managed state; local administrators or applications can still modify files afterward, so use verification features when you need to compare installed files with recorded metadata.

:::single-choice{#package-install-tools-rpm-list-installed}
Which command queries all packages recorded as installed in the RPM database?

::option[`rpm -qa`]{#package-install-tools-rpm-query-all .correct explanation="`-q` selects query mode and `-a` expands it to all installed package records."}
::option[`rpm -e`]{#package-install-tools-rpm-erase explanation="`-e` requests package removal rather than a read-only listing."}
::option[`dpkg-deb --contents`]{#package-install-tools-deb-contents explanation="This inspects the payload of a Debian archive file, not the RPM installed database."}
:::

Use [Managing Packages with RPM](https://labex.io/labs/rhel-managing-packages-with-rpm-in-linux-590868) to practice archive queries and integrity checks in an isolated system.

## Summary

You can now distinguish low-level package operations from repository transactions.

1. Inspect local archive metadata and contents before installation.
2. Use `dpkg` for `.deb` and `rpm` for `.rpm` low-level operations.
3. Prefer APT or DNF when dependencies must be resolved.
4. Remove by installed package name and verify managed state separately.
