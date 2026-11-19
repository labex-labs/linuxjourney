---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "en"
order_index: 3
title: "File Integrity"
description: "Learn to compare a file's contents and permissions using a hash and metadata."
meta_title: "File Integrity - System Auditing"
meta_description: "Learn to compare a file's contents and permissions using a hash and metadata."
meta_keywords: "file integrity, system auditing, cybersecurity, Linux Journey"
---

An integrity check asks whether a file still matches a reference. Check contents and metadata separately. Contents are the bytes inside the file. **Metadata** includes details such as its access permissions.

## Recording a Content Hash

In an empty practice folder, create a tiny configuration file. The redirection replaces an existing file of that name, so use a new folder.

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

The first field is the **hash**, a fixed-length value calculated from the file's bytes. Use the same method on the same file later. A changed hash indicates different input bytes.

:::single-choice{#host-file-integrity-changed-hash} The SHA-256 value changes after the file is edited. What does the comparison show?

::option[Its content differs from the bytes measured earlier.]{#host-file-integrity-changed-hash-a .correct explanation="The hash changes with the content supplied to the calculation."}
::option[The edit was necessarily unauthorized.]{#host-file-integrity-changed-hash-b explanation="Approval is a separate question."}
::option[An account's permissions definitely changed.]{#host-file-integrity-changed-hash-c explanation="A content hash does not record permissions."}
:::

## Recording Its Permissions

On Linux, `stat -c` prints selected metadata. The `%a` field prints the numeric permission mode and `%n` prints the name.

```bash
$ stat -c '%a %n' site.conf
```

The exact starting mode can depend on how the file was created. Record it alongside the content hash so you can compare both properties later.

:::single-choice{#host-file-integrity-mode-vs-content} The hash matches the reference and stat reports a different mode. What changed according to these checks?

::option[The file bytes changed, and its mode stayed the same.]{#host-file-integrity-mode-vs-content-a explanation="The hash matches and the mode differs."}
::option[The file was necessarily deleted.]{#host-file-integrity-mode-vs-content-c explanation="Both checks returned information about the file."}
::option[Its permissions changed while the observed content hash stayed the same.]{#host-file-integrity-mode-vs-content-b .correct explanation="These two tools measure different properties."}
:::

## Testing a Mode Change

The next command changes the permissions of this disposable file to `640`. It grants the owner read and write access and the group read access. Run the two checks again and compare the results.

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

The mode should report 640 and the content hash should match the first measurement.

:::single-choice{#host-file-integrity-repeat-check} Which check would detect a later edit to mode=preview inside the file?

::option[The filename from stat alone.]{#host-file-integrity-repeat-check-a explanation="The name can remain the same after editing."}
::option[A new SHA-256 check compared with the original.]{#host-file-integrity-repeat-check-c .correct explanation="A content change would produce a different hash."}
::option[The owner permission number alone.]{#host-file-integrity-repeat-check-b explanation="Permission changes are independent of most content edits."}
:::

![Recorded LabEx output showing a permission mode change to 640 with an unchanged content hash](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## Summary

You can now compare file contents and access permissions independently.

1. Record a SHA-256 content hash.
2. Read the mode using stat.
3. Verify the effect of a permission change.
