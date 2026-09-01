---
lesson_id: "tracking-processes-lsof-fuser"
course_id: "process-utilization"
lang: "en"
order_index: 2
title: "lsof and fuser"
description: "Learn how to identify processes using files, directories, mount points, and network sockets."
meta_title: "lsof and fuser - Process Utilization"
meta_description: "Explore the lsof and fuser commands in Linux to identify which processes are using specific files. Learn to resolve 'Device or Resource Busy' errors, compare fuser vs lsof, and use options like fuser -k to manage open files effectively."
meta_keywords: "lsof, fuser, fuser command, linux fuser, fuser vs lsof, lsof vs fuser, fuser -k linux, open files, process management, device busy, Linux commands"
---

A filesystem can remain busy because a process has an open file, maps a file into memory, or uses a directory as its current working directory. `lsof` and `fuser` help identify those relationships. Inspect first; stopping processes is a separate decision with operational consequences.

## Listing Open Files with lsof

`lsof` means “list open files.” Query a path to see matching open-file records:

```bash
$ sudo lsof -- /mnt/usb
```

For a whole directory tree on the same filesystem, implementations commonly support `+D`, but recursive scans can be expensive:

```bash
$ sudo lsof +D /mnt/usb
```

Useful columns include `COMMAND`, `PID`, `USER`, file descriptor (`FD`), type, device, and `NAME`. A record whose `FD` is `cwd` indicates that the process uses the directory as its current working directory. Unprivileged output may be incomplete for processes owned by other users.

:::single-choice{#lsof-cwd-record} What does `cwd` in the `FD` column indicate?

::option[The process uses that directory as its current working directory.]{#lsof-current-directory .correct explanation="A process current directory can keep a mounted filesystem busy."}
::option[The file was closed while it was being written.]{#lsof-closed-write explanation="The marker describes a directory relationship, not a close event."}
::option[The process owns the filesystem device.]{#lsof-device-owner explanation="Filesystem ownership is not represented by the `cwd` descriptor label."}
:::

## Identifying Users with fuser

`fuser` reports process IDs using a specified file or filesystem. Verbose output adds users, access types, and command names:

```bash
$ sudo fuser -v /mnt/usb
```

To treat the argument as a mounted filesystem and find processes accessing files within it, use the mount option supported by procps `fuser`:

```bash
$ sudo fuser -vm /mnt/usb
```

Verify that the path is the intended mount point with tools such as `findmnt --target /mnt/usb`. Bind mounts, namespaces, permissions, and races can affect what a single query reveals.

:::single-choice{#fuser-verbose-purpose} Why use `fuser -v` instead of plain `fuser` during investigation?

::option[It automatically unmounts the selected filesystem.]{#fuser-verbose-unmount explanation="Verbose mode reports details and does not request an unmount."}
::option[It adds context such as user, access type, and command.]{#fuser-verbose-details .correct explanation="The extra columns help assess which processes are safe to coordinate or stop."}
::option[It permanently prevents the processes from reopening files.]{#fuser-verbose-prevent explanation="Reporting does not create an access-control rule."}
:::

## Handling a Busy Filesystem

Use a deliberate sequence rather than immediately killing every matching PID:

1. Confirm the host, path, mount source, and intended maintenance.
2. Identify processes with both tools when practical.
3. Determine whether each process can be stopped, moved out of the directory, or allowed to finish.
4. Stop it through its service manager or application interface when available.
5. Query again, then unmount and verify the result.

`fuser -k` sends a signal to matching processes. Its default signal is `SIGKILL` on common procps implementations, so it does not provide an orderly shutdown. If an explicitly approved termination is necessary, select an appropriate signal, verify the PID and owner, and understand that the process set can change between inspection and action.

:::single-choice{#fuser-k-risk} Why is `fuser -k /mnt/usb` a poor first troubleshooting step?

::option[It only prints filesystem free space.]{#fuser-k-space explanation="The option targets processes rather than reporting capacity."}
::option[It can kill multiple matching processes without orderly cleanup.]{#fuser-k-kills .correct explanation="The broad signal action can interrupt writes or services, so investigation and coordination should come first."}
::option[It changes every matching process's working directory.]{#fuser-k-chdir explanation="It sends a signal and does not relocate process directories."}
:::

## Choosing the Tool

Use `lsof` when you need detailed open-file records, descriptors, or socket information. Use `fuser` for a path-oriented view of matching PIDs and access types. Neither result alone tells you whether a process is safe to terminate.

For network sockets, use an explicit protocol namespace with `fuser` or a socket-focused tool such as `ss`:

```bash
$ sudo fuser -v 22/tcp
$ sudo ss -lntp
```

:::single-choice{#lsof-fuser-tool-choice} Which tool is suited to a detailed list of open-file descriptors and owning processes?

::option[`lsof`]{#lsof-detailed-records .correct explanation="Its output is organized around open-file records and their process metadata."}
::option[`uptime`]{#lsof-uptime explanation="Uptime reports runtime and load averages, not open descriptors."}
::option[`free`]{#lsof-free explanation="Free summarizes memory rather than file use."}
:::

## Summary

You can now investigate file and filesystem use without treating termination as the default response.

1. Use `lsof` for detailed open-file records.
2. Use `fuser` for path-oriented PID and access information.
3. Confirm the mount and account for permissions and races.
4. Coordinate an orderly stop before considering a signal.
5. Query again and verify the unmount or service outcome.
