---
lesson_id: "vim-saving-and-exiting"
course_id: "advanced-text-fu"
lang: "en"
order_index: 8
title: "Vim Saving and Exiting"
description: "Learn how to write, quit, save under another name, or deliberately discard Vim buffer changes."
meta_title: "Vim Saving and Exiting - Advanced Text-Fu"
meta_description: "Learn how to save in Vim editor using commands like :w. Master how to save and quit with :wq or ZZ. This guide covers the essential linux wq and vi write and quit commands for efficient file management in Vim."
meta_keywords: "vim how to save, linux wq, vi write and quit, vim how to save and quit, how to save in vim editor, save file vim, exit vim, vim commands"
---

Writing and quitting are separate Vim operations. Before entering an Ex command, press `Esc` to return to Normal mode, type `:`, enter the command, and press Enter. Read Vim's status or error message before assuming a write succeeded.

## Writing the Current Buffer

Use `:w` to write the current buffer to its associated file without closing the window:

```vim
:w
```

A write can fail because the buffer has no filename, the directory is not writable, the filesystem is full, or another condition prevents the operation. Check the message Vim reports.

Use `:w copy.txt` to write the current buffer to another pathname while keeping the current buffer's existing name. Use `:saveas copy.txt` when the buffer should adopt the new pathname.

:::single-choice{#vim-save-without-quit} Which Vim command writes the current buffer to its associated file without quitting?

::option[`:q`]{#vim-save-q explanation="`:q` requests a quit and does not write a modified buffer."}
::option[`:w`]{#vim-save-w .correct explanation="The `:write` command saves the current buffer and leaves the editing window open."}
::option[`:q!`]{#vim-save-q-force explanation="`:q!` abandons unsaved changes and quits; it does not save them."}
:::

## Quitting an Unmodified Buffer

Use `:q` to close the current window when doing so will not abandon unsaved buffer changes:

```vim
:q
```

If the current buffer is modified and its changes would be lost, Vim normally refuses and reports a warning. This safeguard gives you a chance to write or reconsider.

:::single-choice{#vim-quit-clean-buffer} Which command quits the current Vim window when no unsaved changes would be lost?

::option[`:w`]{#vim-quit-w explanation="This writes the buffer but leaves the current window open."}
::option[`:q`]{#vim-quit-q .correct explanation="The ordinary quit command closes the window when Vim's modified-buffer safeguards allow it."}
::option[`u`]{#vim-quit-u explanation="Normal-mode `u` undoes a change and does not close the editor window."}
:::

## Discarding Unsaved Changes

Use `:q!` only when you intentionally want to close the current window and abandon changes that would otherwise block quitting:

```vim
:q!
```

The exclamation mark overrides the unsaved-change warning. Those buffer changes are not written, so verify that they are truly disposable before pressing Enter.

:::single-choice{#vim-quit-discard-changes} The current buffer has changes you deliberately do not want to save. Which command quits the current window and abandons them?

::option[`:q`]{#vim-discard-plain-q explanation="Plain `:q` normally refuses when quitting would lose modified-buffer changes."}
::option[`:wq`]{#vim-discard-wq explanation="`:wq` writes the changes before quitting, the opposite of discarding them."}
::option[`:q!`]{#vim-discard-q-force .correct explanation="The bang overrides the modified warning and closes without writing the unsaved changes."}
:::

## Writing and Quitting Together

Use `:wq` when the buffer should be written and the current window should close after a successful write:

```vim
:wq
```

If writing fails, Vim does not complete the requested quit. Resolve the error rather than assuming the data reached disk.

:::single-choice{#vim-write-and-quit} Which command writes the current buffer and then quits the current window if writing succeeds?

::option[`:wq`]{#vim-save-wq .correct explanation="This combines a write with a quit, and the quit depends on successful writing."}
::option[`:q!`]{#vim-save-force-quit explanation="This quits while discarding changes rather than writing them."}
::option[`:w copy.txt`]{#vim-save-copy explanation="This writes another pathname but keeps the editing window open."}
:::

## Using :x and ZZ

`:x` writes the buffer only if it is modified, then quits. In Normal mode, uppercase `ZZ` performs the same write-if-modified-and-quit behavior:

```vim
:x
```

```text
ZZ
```

This differs subtly from `:wq`, which requests a write even when the buffer is unchanged. Uppercase `ZQ` is the Normal-mode counterpart for quitting without writing, similar to `:q!`.

:::single-choice{#vim-write-if-modified-quit} Which Normal-mode command writes only when the buffer is modified and then quits?

::option[`ZZ`]{#vim-save-zz .correct explanation="Uppercase `ZZ` performs the write-if-modified-and-quit behavior associated with `:x`."}
::option[`zz`]{#vim-center-screen explanation="Lowercase `zz` recenters the current line in the window; it does not save or quit."}
::option[`ZQ`]{#vim-quit-zq explanation="Uppercase `ZQ` quits without writing, so it discards unsaved changes rather than saving them."}
:::

When several windows or buffers are involved, a command may close only the current window. Commands such as `:qa`, `:wqa`, and `:qa!` act across windows, but review every modified buffer before using an all-windows force command.

To practice writing and quitting on a disposable file, try this hands-on lab:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both Vim and Nano. This lab will solidify your understanding of basic Vim operations, including how to save and quit.

## Summary

You can now choose a Vim exit command that matches your intent for unsaved data.

1. Write without quitting with `:w`.
2. Quit safely with `:q` when no changes would be lost.
3. Discard changes deliberately with `:q!`.
4. Write and quit with `:wq`.
5. Use `:x` or `ZZ` for write-if-modified behavior.
