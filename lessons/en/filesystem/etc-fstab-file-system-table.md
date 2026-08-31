---
lesson_id: "etc-fstab-file-system-table"
course_id: "filesystem"
lang: "en"
order_index: 7
title: "/etc/fstab"
description: "Learn how to define persistent filesystem and swap attachments in `/etc/fstab` and validate them safely."
meta_title: "/etc/fstab - The Filesystem"
meta_description: "Learn how to use the /etc/fstab file in Linux to automatically mount filesystems at boot. This guide covers the fstab syntax, how to edit the etc fstab file safely, and its role in system startup."
meta_keywords: "fstab, fstab linux, etc fstab, /etc/fstab, fstab file, mount filesystems, Linux boot, fstab tutorial"
---

`/etc/fstab`, the filesystem table, declares filesystems, swap areas, bind mounts, network sources, and other attachments that system tools may mount or activate. Entries can participate in boot, but options such as `noauto`, automount integration, and service-manager policy affect when or whether that happens.

## The Six Fields

A conventional entry has six whitespace-separated fields:

```text
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /data ext4 defaults,nosuid,nodev 0 2
```

1. **Source**: a device path, `UUID=`, `LABEL=`, network source, or another supported specification.
2. **Target**: mount point, or `none` for uses such as swap where appropriate.
3. **Type**: filesystem type, `swap`, `none`, or an accepted automatic type.
4. **Options**: a comma-separated list interpreted by mount helpers and integration layers.
5. **Dump field**: historically controls the `dump` backup utility; `0` commonly disables participation.
6. **Pass field**: controls boot-time `fsck` ordering where applicable; `0` disables automatic checking through this mechanism.

Whitespace inside a field must be escaped using fstab syntax such as `\040` for a space. A `#` begins a comment outside a field.

:::single-choice{#fstab-field-count}
How many fields does a normal `/etc/fstab` entry contain?

::option[Four.]{#fstab-four-fields explanation="Source, target, type, and options are followed by the dump and pass fields."}
::option[Eight.]{#fstab-eight-fields explanation="Eight is not the standard field count for one fstab record."}
::option[Six.]{#fstab-six-fields .correct explanation="The traditional format contains source, target, type, options, dump, and pass fields."}
:::

## Stable Source Identifiers

For local filesystems, a filesystem UUID is often more stable than `/dev/sdX` enumeration:

```bash
$ lsblk -f
$ sudo blkid
```

Use `UUID=...` only after confirming the identifier belongs to the intended filesystem. Reformatting creates a new UUID, and block-level clones can duplicate one. `PARTUUID=` instead identifies a partition-table entry and has different semantics.

:::single-choice{#fstab-uuid-source}
What does `UUID=...` in the source field normally identify?

::option[The user account that owns the mount point.]{#fstab-user-uuid explanation="Account identity is not selected through the filesystem UUID source syntax."}
::option[Filesystem metadata carrying that UUID.]{#fstab-filesystem-uuid .correct explanation="Mount resolves the filesystem identifier to an available block device rather than relying on enumeration name."}
::option[The process that last unmounted the filesystem.]{#fstab-process-uuid explanation="Process history is not encoded by this source field."}
:::

## Mount Options and Check Fields

`defaults` expands to an implementation-defined conventional option set; it is not necessarily the safest policy for every mount. Add options based on trust and workload, such as read-only access or restrictions on device nodes and setuid behavior. Network and removable filesystems can need timeout, dependency, or failure-tolerance policy so boot does not stall unexpectedly.

For filesystems supported by `fsck`, the root filesystem conventionally uses pass `1` and other checked local filesystems pass `2`. Filesystem-specific practice can differ—for example, some types do not use generic boot-time fsck—so follow the installed filesystem and distribution documentation rather than assigning `2` mechanically.

:::single-choice{#fstab-pass-zero}
What does a sixth-field value of `0` request?

::option[Skip automatic fsck ordering through fstab for that entry.]{#fstab-pass-zero-skip .correct explanation="Pass zero excludes the entry from the boot-time checking sequence governed by this field."}
::option[Mount the filesystem read-only in every circumstance.]{#fstab-pass-zero-readonly explanation="Read-only behavior belongs in the mount-options field."}
::option[Erase the filesystem before each boot.]{#fstab-pass-zero-erase explanation="The pass field does not format or wipe a filesystem."}
:::

## Editing with a Recovery Path

An invalid root, boot, or required network entry can interrupt startup. Before editing:

1. Confirm a current backup and console or rescue access.
2. Copy the existing file while preserving permissions.
3. Verify source identity and create the intended mount point.
4. Make one scoped change.
5. Validate and test before rebooting.

Do not put credentials directly in a world-readable fstab entry. Use the relevant mount helper's protected credential mechanism.

:::single-choice{#fstab-editing-recovery}
Why should rescue access be confirmed before changing a critical fstab entry?

::option[Fstab edits always erase the partition table immediately.]{#fstab-no-partition-erase explanation="The text edit itself does not rewrite disk partitions, though later mounts can have effects."}
::option[The file can be edited only from another operating system.]{#fstab-other-os-only explanation="It can be edited on Linux with suitable privilege and safeguards."}
::option[A bad entry can prevent normal boot from reaching a usable system.]{#fstab-boot-failure .correct explanation="Critical mount failures can enter emergency mode or otherwise block dependent services."}
:::

## Validating Without Assuming Success

Start with a static check where supported:

```bash
$ sudo findmnt --verify --verbose
```

Then test the specific new entry under controlled conditions, confirm it with `findmnt`, and unmount if the test was temporary. `mount -a` attempts many eligible entries and can contact networks or attach unintended sources; it also skips already mounted and `noauto` entries, so it is neither a harmless syntax checker nor complete proof.

On systemd-based systems, reload manager configuration after editing fstab so generated mount units are refreshed, then verify dependencies and boot behavior according to local documentation.

:::single-choice{#fstab-mount-a-limit}
Why is `mount -a` not a complete fstab validation by itself?

::option[It always reformats every listed device before mounting.]{#fstab-mount-a-formats explanation="Mount does not normally create filesystems."}
::option[It can skip entries and exercise broad real mount operations rather than only syntax.]{#fstab-mount-a-incomplete .correct explanation="Already mounted or `noauto` records may not be tested, while eligible sources can have live effects."}
::option[It reads only shell history and ignores fstab.]{#fstab-mount-a-history explanation="The command does consult fstab for eligible entries."}
:::

Practice in [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) with the lab's recovery-safe secondary storage.

## Summary

You can now read and validate a persistent filesystem-table entry.

1. Parse source, target, type, options, dump, and pass fields.
2. Select a verified identifier with the intended identity semantics.
3. Choose mount and checking policy for the actual filesystem.
4. Preserve rescue access and make one scoped edit.
5. Combine static validation, targeted mounting, and boot-policy checks.
