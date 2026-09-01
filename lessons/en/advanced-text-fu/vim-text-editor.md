---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "en"
order_index: 3
title: "Vim (Vi Improved)"
description: "Learn what Vim is, how it relates to vi, and how to open files, help, and guided practice."
meta_title: "Vim (Vi Improved) - Advanced Text-Fu"
meta_description: "Discover Vim, the powerful and lightweight text editor known as vi improved. This lesson introduces the essentials of vim vi improved, a tool pre-installed on most Linux systems."
meta_keywords: "Vim, vi improved, vim vi improved, Linux text editor, Vim tutorial, Vi editor, vim improved, Linux commands"
---

Vim is a configurable text editor whose name means **Vi Improved**. It preserves the modal editing model associated with the original `vi` editor and adds features such as multilevel undo, syntax support, scripting, and an extensive help system.

## Relating Vim and vi

`vi` describes both a historical editor and a common command interface. On one Linux system, `vi` may start Vim in a compatibility-oriented mode; on another, it may start a different vi implementation. Do not assume that every `vi` command provides every Vim feature.

Check what the current shell resolves:

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

The resolved path does not by itself identify whether `vi` and `vim` are the same implementation. `type -a vi vim` and the editor's version output can provide more detail.

:::single-choice{#vim-name-origin} What does the name Vim mean?

::option[Visual Input Manager]{#vim-visual-input explanation="This expansion is not the origin of the editor's name."}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="Vim does use modes, but this phrase is not what the name represents."}
::option[Vi Improved]{#vim-vi-improved .correct explanation="Vim began as an improved vi-compatible editor, which is reflected in its name."}
:::

:::single-choice{#vim-check-command} Which command checks whether Bash can currently resolve the name `vim`?

::option[`vim --create`]{#vim-create-option explanation="This is not the shell-resolution check and is not how Vim is installed or discovered."}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="The shell builtin reports the command that would be used for the name, if one is available."}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="This examines one possible configuration file and says nothing definitive about whether the Vim executable is available."}
:::

## Opening Vim and Files

Start Vim with an unnamed buffer:

```bash
$ vim
```

Pass a pathname to edit that file:

```bash
$ vim filename.txt
```

If `filename.txt` exists and is readable, Vim loads its content into a buffer. If the path does not exist, Vim opens a new buffer associated with that name; no file is created until you successfully write the buffer.

Vim does not bypass filesystem permissions. Opening a file does not guarantee that your account can save changes to its pathname.

:::single-choice{#vim-open-missing-path} What normally happens when `vim draft.txt` names a path that does not yet exist?

::option[Vim opens a new buffer and creates the file only when it is written.]{#vim-new-buffer .correct explanation="The pathname is remembered for the buffer, while disk creation is deferred until a successful save."}
::option[Vim creates an empty file on disk before opening the interface.]{#vim-immediate-create explanation="The new buffer is associated with the pathname, but the file is not created until a successful write."}
::option[Vim refuses to start because every pathname must already exist.]{#vim-refuse-missing explanation="Vim can open a new buffer for a missing pathname so you can compose a new file."}
:::

## Using Built-In Learning Resources

If the Vim installation includes `vimtutor`, run it from the shell for an interactive practice lesson:

```bash
$ vimtutor
```

Inside Vim, enter Normal mode with `Esc`, type `:help`, and press Enter to open the help system. A specific topic can follow the command:

```vim
:help user-manual
:help :write
```

Help tags are precise, so punctuation can matter. Use `Ctrl+]` on a help link to follow it and `Ctrl+T` to return.

:::single-choice{#vim-guided-tutorial} Which shell command starts Vim's guided tutorial when it is installed?

::option[`vim --quiz`]{#vim-quiz-option explanation="Vim does not use this option as its standard guided tutorial interface."}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor` opens a copy of the interactive tutorial designed for safe hands-on practice."}
::option[`help vim`]{#vim-shell-help explanation="Bash `help` documents shell builtins; it does not start Vim's interactive tutorial."}
:::

## Practicing with a Disposable File

Begin with a file in a directory you own:

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

The following lessons introduce searching, navigation, insertion, editing, and saving. Until you know how to leave safely, remember that `Esc` returns to Normal mode and `:q!` followed by Enter abandons unsaved changes in the current window. Use that command only when discarding those changes is intentional.

:::single-choice{#vim-abandon-practice-changes} In a disposable practice file, which Vim command quits the current window and discards its unsaved changes?

::option[`:w`]{#vim-write-only explanation="`:w` writes the buffer but does not quit the current window."}
::option[`:wq`]{#vim-write-quit explanation="`:wq` saves changes before quitting, so it does not discard them."}
::option[`:q!`]{#vim-quit-force .correct explanation="The `!` tells Vim to abandon the modified-buffer warning and quit without writing those changes."}
:::

To practice opening, editing, and saving with Vim, try this hands-on lab:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both Vim and Nano in a real Linux environment.

## Summary

You can now identify Vim, open a buffer, and find safe learning resources.

1. Explain how Vim relates to vi without assuming one implementation.
2. Check whether the `vim` command is available.
3. Open an existing file or a new named buffer.
4. Start `vimtutor` or open Vim's built-in help.
5. Abandon unsaved practice changes only when intended.
