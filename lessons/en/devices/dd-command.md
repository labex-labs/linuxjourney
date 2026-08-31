---
lesson_id: "dd-command"
course_id: "devices"
lang: "en"
order_index: 7
title: "dd"
description: "Learn how `dd` copies block streams and how to prevent destructive input, output, and size mistakes."
meta_title: "dd - Devices"
meta_description: "Explore the powerful dd tool in Linux. This guide explains how to use the dd linux command for efficient data copying, disk imaging, and backups. Learn key options like if, of, and bs."
meta_keywords: "dd command, dd linux, dd tool, copy data, disk imaging, Linux tutorial, beginner, guide, data backup"
---

`dd` copies data from an input stream to an output stream while applying requested block sizes and conversions. It does not understand filesystems, partition boundaries, or whether an output target contains valuable data. That makes it useful for images and raw devices—and immediately destructive when the target is wrong.

## Input, Output, and Block Size

A command has this general shape:

```bash
$ dd if=input.img of=output.img bs=4M status=progress
```

- `if=` selects the input; without it, `dd` reads standard input.
- `of=` selects the output; without it, `dd` writes standard output.
- `bs=` sets the input and output block size for ordinary copying.
- `status=progress` asks GNU `dd` to report periodic transfer progress.

`dd` copies blocks, not inherently one byte at a time. A larger `bs` can reduce system-call overhead, but the optimal value depends on devices, alignment, caching, and workload. It does not change the logical data copied.

:::single-choice{#dd-command-output-operand}
Which operand selects the destination written by `dd`?

::option[`if=`]{#dd-command-input-file explanation="`if` identifies the input source."}
::option[`of=`]{#dd-command-output-file .correct explanation="`of` names the output stream or file that receives copied data."}
::option[`bs=`]{#dd-command-block-size explanation="`bs` chooses a transfer block size rather than a path."}
:::

## Limiting the Copy

`count=` limits the number of input blocks processed. For a regular input file:

```bash
$ dd if=source.img of=prefix.img bs=1M count=2 status=progress
```

This requests two input blocks of up to 1 MiB each, so it copies at most 2 MiB. Short reads can complicate the simple multiplication for streams such as pipes; GNU `dd` offers `iflag=fullblock` when complete input blocks are required. Distinguish binary units and suffix syntax according to the local implementation.

:::single-choice{#dd-command-count-result}
For a regular file, what maximum amount does `bs=1M count=2` request?

::option[1 MiB.]{#dd-command-one-mib explanation="That would be one block at the selected size."}
::option[2 MiB.]{#dd-command-two-mib .correct explanation="Two input blocks multiplied by 1 MiB per block gives a maximum of 2 MiB."}
::option[2 GiB.]{#dd-command-two-gib explanation="The `M` suffix denotes mebibyte-sized blocks in GNU `dd`, not gibibytes."}
:::

## Writing an Image to a Block Device

A raw restoration can look like:

```bash
$ sudo dd if=backup.img of=/dev/sdX bs=4M status=progress conv=fsync
```

`/dev/sdX` is deliberately a placeholder, not a command to copy. Before replacing it:

1. Maintain a tested backup of all valuable data.
2. Identify the target by model, serial, size, transport, and persistent link using `lsblk`, `udevadm`, or equivalent tools.
3. Confirm that no target partition is mounted, used as swap, part of RAID or LVM, or opened by another service.
4. Recheck the device after any unplug, reboot, or topology change.
5. Ensure the image fits and that writing the whole device is truly intended.

The output device is overwritten from its beginning. Reversing `if` and `of`, selecting the system disk, or using a whole disk when a partition was intended can destroy data without a confirmation prompt.

:::single-choice{#dd-command-target-verification}
Which is the strongest reason to verify model, serial, size, and active use before a raw-device write?

::option[Device letters can change, and `dd` overwrites the selected target without understanding its contents.]{#dd-command-target-can-change .correct explanation="Identity and usage checks reduce the risk of destroying a different disk or an active storage stack."}
::option[`dd` refuses to write unless the filesystem label matches the image.]{#dd-command-label-check explanation="The tool performs no such filesystem-aware safety check."}
::option[Block devices cannot be opened while any backup exists.]{#dd-command-backup-prevents-open explanation="A backup does not technically prevent writes; it provides recovery if maintained and tested."}
:::

## Creating a Consistent Image

Reading a live block device while its filesystem is changing can produce an internally inconsistent image. Prefer an unmounted filesystem, an application-consistent snapshot, or a documented freeze/snapshot workflow. Databases and virtual machines can require their own quiescing procedures.

A raw device image copies blocks, including filesystem metadata and unused regions, so it can be much larger than a file-level backup and can reproduce identifiers that must be changed before mounting a clone alongside the original.

:::single-choice{#dd-command-live-filesystem-image}
Why can imaging a mounted, changing filesystem be unreliable?

::option[Mounted filesystems never permit block-device reads.]{#dd-command-mounted-no-read explanation="Raw reads can be possible, which is why consistency must be planned rather than assumed."}
::option[Different blocks can be read from different moments of filesystem state.]{#dd-command-inconsistent-moments .correct explanation="Concurrent modifications can make the collected block image fail to represent one consistent point in time."}
::option[`dd` automatically converts the filesystem to a tar archive.]{#dd-command-converts-tar explanation="The tool copies raw data and does not create a filesystem-aware archive."}
:::

## Completion and Verification

The command completing without an I/O error does not prove that the intended source and target were selected or that the image is usable. Record the exact identities and sizes, ensure buffered output has reached storage, compare an appropriately bounded read-back or cryptographic hashes, and test recovery according to the backup plan.

Do not advertise `dd` overwrite passes as guaranteed secure erasure for SSDs, flash translation layers, thin-provisioned storage, snapshots, or remapped sectors. Use device- and platform-supported sanitization plus an explicit data-destruction policy.

:::single-choice{#dd-command-success-meaning}
What does a zero exit status from `dd` fail to prove by itself?

::option[That the command parsed all supplied operands.]{#dd-command-parsed-operands explanation="Invalid operands normally cause an error rather than a successful completion."}
::option[That the operator selected the intended source and destination.]{#dd-command-does-not-prove-intent .correct explanation="The tool can successfully copy to the wrong target because it cannot infer operator intent."}
::option[That the process reached its normal termination path.]{#dd-command-normal-exit explanation="A zero status does indicate normal command-level success, though not semantic correctness of the chosen targets."}
:::

Practice only with regular files or disposable virtual disks before touching raw hardware. Partition and filesystem concepts in [Manage Linux Partitions and Filesystems](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) provide essential context.

## Summary

You can now reason about `dd` as a raw block-copy tool with no intent awareness.

1. Distinguish `if`, `of`, `bs`, and `count`.
2. Verify persistent target identity and every active consumer.
3. Create images from a consistent storage state.
4. Flush, verify, and test recovery after a copy.
5. Treat every raw-device output as potentially destructive.
