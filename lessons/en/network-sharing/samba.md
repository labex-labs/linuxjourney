---
lesson_id: "samba"
course_id: "network-sharing"
lang: "en"
order_index: 5
title: "Samba"
description: "Learn how to configure, validate, access, and secure a basic Samba file share."
meta_title: "Samba - Network Sharing"
meta_description: "Learn how to set up a Samba network share on Linux. This guide covers the Samba protocol, installation, configuration, and using smb linux clients to connect to shares."
meta_keywords: "Samba, smb linux, linux smb, samba network, samba protocol, smb samba, file sharing, smb.conf, cifs, smbclient, linux tutorial"
---

Samba implements the Server Message Block protocol on Unix-like systems, allowing Linux, Windows, macOS, and other clients to share files and printers. Modern deployments use current SMB dialects; the older term CIFS is still visible in Linux client tooling but should not be read as a reason to enable obsolete SMB1.

## Planning the Share

Before installing or changing Samba, define the authorized clients, identities, read/write needs, network zone, data owner, backup policy, and required SMB dialect. Use a dedicated directory rather than exposing a home or system tree unintentionally.

Access is controlled by both Samba policy and underlying filesystem permissions. Allowing writes in `smb.conf` cannot grant an account filesystem access it does not have.

:::single-choice{#samba-two-permission-layers} What must allow a user to write through a Samba share?

::option[Only the share's displayed comment.]{#samba-comment-permission explanation="A comment is descriptive text and does not grant access."}
::option[Both Samba rules and filesystem permissions.]{#samba-policy-and-filesystem .correct explanation="The request must pass the protocol-level rules and local filesystem authorization."}
::option[Only the client's desktop wallpaper setting.]{#samba-wallpaper explanation="Client appearance settings do not control server files."}
:::

## Defining a Basic Share

The main configuration is commonly `/etc/samba/smb.conf`. A restricted example is:

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

Create the directory and apply reviewed ownership and permissions for the Unix group:

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

The set-group-ID bit helps new entries inherit the directory group, but collaborative access may also require an ACL or a carefully chosen create mask. Test the actual file and directory results rather than assuming inheritance is sufficient.

:::single-choice{#samba-valid-users} What does `valid users = @teamshare` express?

::option[Every anonymous network user receives write access.]{#samba-every-anonymous explanation="The rule restricts access rather than enabling guest writes."}
::option[The server must rename the share to `teamshare`.]{#samba-rename-share explanation="The visible share name remains the section name `[team]`."}
::option[Only members of the named group are allowed by this share rule.]{#samba-valid-group .correct explanation="The `@` form refers to a group in Samba's user-list syntax."}
:::

## Configuring Identity

In a standalone Samba configuration, an account generally needs a corresponding Unix identity and an enabled Samba credential:

```bash
$ sudo smbpasswd -a alice
```

Directory-domain deployments use a different identity design. Do not place passwords in shell history or configuration readable by unrelated users, and do not assume a Samba password is automatically identical to the Unix account password.

:::single-choice{#samba-password-database} What does `smbpasswd -a alice` commonly do on a standalone server?

::option[Deletes the Unix user's home directory.]{#samba-delete-home explanation="The command manages Samba credentials and does not perform home-directory removal."}
::option[Adds or initializes Samba credentials for the account.]{#samba-add-credential .correct explanation="The SMB authentication database is managed separately from merely creating a Unix user."}
::option[Mounts every visible SMB share as Alice.]{#samba-mount-all explanation="Server credential enrollment is separate from client mounting."}
:::

## Validating and Applying Configuration

Check the parsed configuration before reloading services:

```bash
$ testparm -s
```

Review unexpected defaults and errors, then reload the distribution's Samba service through its service manager. Service names vary, commonly including `smbd.service` or `smb.service`. A reload is less disruptive than a restart when supported, but still verify status, listening sockets, firewall scope, and logs.

Test from a client with an explicit user:

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose} Why run `testparm -s` before applying a Samba change?

::option[It copies every shared file to a backup server.]{#samba-testparm-backup explanation="The tool parses and reports configuration rather than copying share data."}
::option[It validates and displays the effective Samba configuration.]{#samba-testparm-validate .correct explanation="Parser output catches configuration errors and reveals interpreted settings before service impact."}
::option[It grants all clients administrative privileges.]{#samba-testparm-admin explanation="Validation does not alter client authorization."}
:::

## Mounting from Linux

Linux clients commonly use the `cifs` filesystem driver and mount helpers. Avoid passwords in the command line because arguments can leak through history or process inspection. Use a root-readable credentials file or an approved credential mechanism:

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

Protect the credential file, confirm the dialect supported by both sides, and define UID, GID, permission, and encryption requirements deliberately. After mounting, verify with `findmnt`, perform authorized read/write tests, and unmount after coordinating active users.

:::single-choice{#samba-command-line-password} Why avoid `password=...` directly in a mount command?

::option[It can expose the secret through history or process arguments.]{#samba-password-exposure .correct explanation="A protected credential source reduces accidental disclosure, though it still requires careful permissions."}
::option[SMB supports no form of password authentication.]{#samba-no-passwords explanation="Password-based SMB authentication is common, although other identity systems also exist."}
::option[The option makes the share permanently read-only.]{#samba-password-readonly explanation="Secret placement does not determine write policy."}
:::

## Summary

You can now configure a Samba share while accounting for both protocol and filesystem security.

1. Define clients, identities, network scope, and data policy first.
2. Restrict the share and align underlying permissions.
3. Manage Samba credentials through the correct identity model.
4. Validate with `testparm` and perform an end-to-end client test.
5. Protect client credentials and verify mounted access.
