---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "en"
order_index: 2
title: "Text Editors"
description: "Learn how to choose and configure a terminal text editor for Linux administration and development."
meta_title: "Text Editors - Advanced Text-Fu"
meta_description: "Learn about Linux text editors like Vim and Emacs. Discover their uses and importance for system navigation. Start your Linux text editor journey!"
meta_keywords: "Linux text editors, Vim, Emacs, Linux commands, Linux tutorial, beginner Linux, Linux guide"
---

Linux configuration, scripts, source code, and logs are commonly stored as plain text. A terminal editor lets you work with those files in a local terminal, a remote SSH session, or an environment without a graphical desktop.

## Choosing an Editor for the Environment

No single editor is best for every person or task. Graphical editors, terminal editors, and integrated development environments can all be appropriate. For command-line work, choose an editor that is installed, that you can exit safely, and whose basic editing model you understand.

Do not assume Vim or Emacs is installed. Check command resolution in the current shell:

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

An empty result with a nonzero status means that name was not found through the current command search. Minimal systems may provide `vi`, while others include Nano or no interactive editor at all.

:::single-choice{#editors-check-availability} Which command checks whether the current shell can resolve an executable named `vim`?

::option[`vim --install`]{#editors-vim-install explanation="Vim does not use this command as a portable installation check, and package installation is distribution-specific."}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="This classifies one configuration pathname if it exists; it does not determine whether `vim` is resolvable."}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="The shell builtin checks command resolution and prints the resolved form when available."}
:::

## Understanding Vim's Model

Vim is a modal editor. The same key can have different meanings depending on the current mode:

- Normal mode interprets keys as navigation and editing commands.
- Insert mode inserts typed text.
- Command-line mode accepts commands such as writing or quitting.

This model makes repeated keyboard editing efficient after practice, but new users must keep track of the active mode. Later lessons introduce Vim one operation at a time.

:::single-choice{#editors-vim-modal-meaning} What does it mean that Vim is modal?

::option[Every file opens in a separate graphical window.]{#editors-vim-windows explanation="Windows and buffers are separate concepts. Modal refers to how key behavior changes with editor state."}
::option[Vim can edit only one kind of text file at a time.]{#editors-vim-file-type explanation="Vim supports many file types. The word modal describes its interaction model, not a file restriction."}
::option[Keys perform different actions depending on the active mode.]{#editors-vim-modes .correct explanation="For example, a key can issue a command in Normal mode but insert text in Insert mode."}
:::

## Understanding Emacs's Model

Emacs commonly uses key combinations and named commands within an extensible environment. Files are visited in buffers, and major and minor modes customize behavior for different content and tasks. Emacs can run in a terminal or a graphical frame.

Vim and Emacs both support far more than basic editing through configuration and extensions. Begin with opening, changing, saving, and closing a plain-text file before adding customization.

:::single-choice{#editors-emacs-buffer} In Emacs terminology, where is a visited file's editable text normally held?

::option[In a buffer.]{#editors-emacs-buffer-answer .correct explanation="Emacs visits a file in a buffer, which holds the text being viewed or edited."}
::option[In the shell's alias table.]{#editors-emacs-alias-table explanation="Aliases belong to shell command resolution and do not store editor text."}
::option[Only in the terminal scrollback.]{#editors-emacs-scrollback explanation="Terminal scrollback records displayed output, while Emacs manages editable text in buffers."}
:::

## Setting a Preferred Editor

Many command-line programs consult `VISUAL` or `EDITOR` when they need to start an editor. For example, choose Vim for commands launched from the current Bash session and its children:

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

These variables express a preference; they do not install the program. Use a command that actually exists, and place the exports in the appropriate shell startup file only after testing them.

:::single-choice{#editors-editor-variable} What does `export EDITOR=vim` do?

::option[It tells future child processes that `vim` is the preferred editor value.]{#editors-export-preference .correct explanation="Export places the preference in the environment inherited by commands started from the current shell."}
::option[It installs Vim for every user on the system.]{#editors-install-vim explanation="Environment-variable assignment does not install packages or change other users' systems."}
::option[It makes every program obey Vim's key bindings.]{#editors-global-bindings explanation="Programs may consult the variable to launch an editor, but it does not replace their own interaction model."}
:::

## Practicing without Risking Important Files

Learn on a disposable file in a directory you own:

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

Avoid beginning with system configuration or another user's data. Make a backup before changing an important file, understand how to save and exit, and review the result with a read-only command such as `cat` or `diff`.

:::single-choice{#editors-first-practice-file} What is the safest first file for practicing an unfamiliar editor?

::option[A critical boot configuration file opened as root.]{#editors-boot-file explanation="An accidental change could prevent normal startup, and elevated access increases the impact of mistakes."}
::option[A disposable text file in a directory you own.]{#editors-disposable-file .correct explanation="A practice file limits the consequences of accidental edits while you learn navigation, saving, and quitting."}
::option[A shared production file with no backup.]{#editors-production-file explanation="Unreviewed practice on shared data can disrupt others and offers no simple recovery path."}
:::

To practice opening, editing, and saving terminal text files, try this hands-on lab:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both vi/vim and nano, essential skills for any Linux user.

## Summary

You can now choose a terminal editor and prepare a safe practice workflow.

1. Check whether an editor command is available.
2. Recognize Vim's modal interaction model.
3. Recognize Emacs buffers and extensible modes.
4. Set an editor preference without confusing it with installation.
5. Practice on disposable text before editing important files.
