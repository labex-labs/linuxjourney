---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "en"
order_index: 4
title: "NFS"
description: "Learn how to discover, mount, validate, and safely automate an NFS client mount."
meta_title: "NFS - Network Sharing"
meta_description: "Discover how to use the Network File System (NFS) in Linux. This lesson covers setting up an NFS client, using the mount command, and configuring automount for seamless access to network shares."
meta_keywords: "NFS, NFS client, automount, Network File System, Linux networking, mount command, Linux tutorial, beginner"
---

Network File System lets a client access a server export through the local filesystem namespace. The server controls exports and much of the access policy; the client controls where and when an authorized export is mounted.

## Preparing the Client

Install the distribution's NFS client utilities, commonly packaged as `nfs-common` on Debian-family systems or `nfs-utils` on Red Hat-family systems. Confirm DNS or address reachability, allowed NFS versions, firewall policy, and the exact export path with the server administrator.

`showmount -e SERVER` can list exports provided through the older mount protocol, but it is not authoritative for every NFSv4-only server. A failed listing does not prove that no authorized NFSv4 export exists.

:::single-choice{#nfs-showmount-limit} Why can `showmount -e` be incomplete for an NFSv4 server?

::option[It queries an older export-listing protocol that may not be exposed.]{#nfs-showmount-protocol .correct explanation="NFSv4 can operate without making that separate listing service available."}
::option[It only displays local CPU temperature.]{#nfs-showmount-temperature explanation="The command concerns NFS server export information."}
::option[It permanently disables every listed export.]{#nfs-showmount-disables explanation="Listing is a read-only discovery request."}
:::

## Mounting an Export

Create an empty, dedicated mount point and mount the approved export:

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

Specify a version only when policy or compatibility requires it, for example `-o vers=4.2`. Do not guess performance or security options. Confirm the resulting source, type, and options:

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands} In the mount command, what is `server.example.net:/srv/team`?

::option[The local directory that hides the remote export.]{#nfs-local-mountpoint explanation="The local mount point in the example is `/mnt/team`."}
::option[The name of the client package to install.]{#nfs-package-name explanation="Package names are distribution-specific and are not mount source operands."}
::option[The server and exported remote path.]{#nfs-remote-export .correct explanation="The host and colon-prefixed path identify the NFS source."}
:::

## Understanding Identity and Permissions

NFS access combines server export rules, protocol security, numeric identities or directory services, and filesystem permissions. Matching usernames displayed on two hosts do not guarantee matching numeric IDs. Traditional `AUTH_SYS` sends client-provided numeric identities and depends heavily on trusted client and network controls; stronger environments can use Kerberos security modes when configured end to end.

The server commonly maps remote root to an unprivileged identity through root squashing. Do not disable that protection merely to fix a permission error; inspect IDs, directory ownership, export policy, and the intended security model.

:::single-choice{#nfs-name-versus-id} Why can two users with the same displayed name receive different NFS permissions?

::option[NFS permissions can depend on numeric identity mapping.]{#nfs-numeric-mapping .correct explanation="Name agreement alone does not establish that client and server resolve the same UID and groups."}
::option[NFS ignores all filesystem permissions.]{#nfs-ignores-permissions explanation="Filesystem and export permissions remain part of authorization."}
::option[Every mount automatically changes the server's account database.]{#nfs-changes-accounts explanation="A client mount does not rewrite server identities."}
:::

## Automating Network Mounts

A plain boot-time `/etc/fstab` mount can delay startup when networking or the server is unavailable. Depending on the host, use `autofs` for on-demand maps or systemd mount options such as `_netdev,nofail,x-systemd.automount` after testing their exact semantics:

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

Before editing fstab, preserve recovery access and validate with a non-destructive parser or a controlled mount test. An automount improves availability behavior but does not fix authorization, DNS, or server outages.

:::single-choice{#nfs-automount-benefit} What is a primary benefit of on-demand automounting for an NFS share?

::option[It grants every client root access to the export.]{#nfs-automount-root explanation="Mount timing does not override server authorization."}
::option[It can avoid requiring the server to be available during initial boot.]{#nfs-automount-boot .correct explanation="The connection is triggered on access rather than necessarily blocking early startup."}
::option[It copies the complete server filesystem onto local disk.]{#nfs-automount-copy explanation="A mount presents remote access and is not a full local copy."}
:::

## Unmounting and Verification

Before unmounting, stop or coordinate processes using the share and flush application work. Then unmount the mount point and verify it is gone:

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

A forced or lazy unmount can hide active references and risk application errors; reserve such options for a diagnosed failure with an explicit recovery plan.

:::single-choice{#nfs-safe-unmount} What should precede a normal NFS unmount?

::option[Coordinate processes using the share and finish important writes.]{#nfs-coordinate-writers .correct explanation="Removing a live filesystem from applications can interrupt I/O or leave work incomplete."}
::option[Delete the export directory on the server.]{#nfs-delete-export explanation="Client unmounting does not require destroying server data."}
::option[Disable all client network interfaces.]{#nfs-disable-network explanation="That can make orderly completion harder and is not the normal sequence."}
:::

## Summary

You can now operate an NFS client mount with explicit identity and availability assumptions.

1. Confirm client tools, export path, protocol, and network policy.
2. Mount to a dedicated path and verify the effective source and options.
3. Diagnose permissions through identity and export policy.
4. Use tested on-demand mounting when boot availability matters.
5. Coordinate users, unmount normally, and verify removal.
