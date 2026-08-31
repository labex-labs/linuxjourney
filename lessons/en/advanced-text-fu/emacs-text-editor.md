---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "en"
order_index: 9
title: "Emacs"
description: "Learn how to start Emacs, interpret its key notation, and distinguish buffers, windows, and frames."
meta_title: "Emacs - Advanced Text-Fu"
meta_description: "Learn Emacs, a powerful and extensible text editor for Linux. Understand Emacs buffers and basic usage. Start your Emacs journey today!"
meta_keywords: "Emacs, Linux text editor, Emacs tutorial, Emacs buffers, Linux commands, beginner, guide"
---

GNU Emacs is an extensible text editor whose behavior can be customized with Emacs Lisp. It supports plain-text editing, programming modes, file and buffer management, and many optional packages. You can learn its core editing commands without adopting every extension.

## Checking and Starting Emacs

Do not assume Emacs is installed. Check how the shell resolves it:

```bash
$ command -v emacs
/usr/bin/emacs
```

Start Emacs with its normal display selection:

```bash
$ emacs
```

In a graphical session this may create a graphical frame. Use `-nw`, short for no window system, when Emacs should remain inside the current terminal:

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start}
Which command starts Emacs inside the current terminal instead of using a graphical window system?

::option[`emacs -w`]{#emacs-window-option explanation="This is not the documented no-window-system form introduced here."}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="The `-nw` option tells Emacs not to use a graphical window system and to run on the terminal."}
::option[`command -v emacs`]{#emacs-check-only explanation="This checks command resolution and does not start the editor."}
:::

## Opening a File

Pass a pathname to visit a file when Emacs starts:

```bash
$ emacs notes.txt
```

If the file exists, Emacs reads it into a buffer. If it is missing, Emacs creates a new buffer associated with that pathname; the file is created only after a successful save. Filesystem permissions still determine whether a write can succeed.

:::single-choice{#emacs-open-file-buffer}
What does `emacs notes.txt` normally do when `notes.txt` does not yet exist?

::option[Opens a new buffer associated with that pathname.]{#emacs-new-file-buffer .correct explanation="The buffer can hold new text for `notes.txt`, while the actual file is deferred until saving."}
::option[Creates the file on disk before the editor starts.]{#emacs-immediate-file explanation="Emacs can associate a new buffer with the pathname without creating the disk file until a save succeeds."}
::option[Refuses to start because every visited file must exist.]{#emacs-refuse-new-file explanation="Emacs supports composing new files through buffers associated with missing pathnames."}
:::

## Understanding Buffers, Windows, and Frames

Emacs uses related but distinct objects:

- A **buffer** holds text or other editor state. A visited file's content lives in a buffer.
- A **window** is an area within an Emacs frame that displays a buffer.
- A **frame** is a top-level Emacs display, such as a graphical frame or terminal frame.

Several buffers can exist without being visible, and two windows can display the same buffer. Closing a window does not necessarily kill its buffer or delete a file.

:::single-choice{#emacs-buffer-definition}
What is an Emacs buffer?

::option[A top-level graphical application frame.]{#emacs-buffer-frame explanation="A frame is the top-level display object; a buffer holds editor content or state."}
::option[An object that holds editable text or other editor state.]{#emacs-buffer-content .correct explanation="Visited file contents and many non-file views live in Emacs buffers."}
::option[A shell history file containing previous commands.]{#emacs-buffer-history explanation="Shell history is separate from Emacs buffer storage."}
:::

## Reading Emacs Key Notation

Emacs documentation uses compact notation:

- `C-x` means hold Control and press `x`.
- `M-x` means hold Meta and press `x`; Alt commonly acts as Meta in modern terminals and desktops.
- `C-x C-f` is a key sequence: press Control+x, then Control+f.

The exact terminal may intercept or remap some keys. `Esc` followed by a key can often stand in for a Meta chord.

:::single-choice{#emacs-key-sequence-notation}
How do you enter the Emacs key sequence written `C-x C-f`?

::option[Hold Control for `x`, then hold Control for `f`.]{#emacs-control-x-f .correct explanation="Each `C-` prefix applies to its following key, and the two chords are entered in sequence."}
::option[Type the literal characters `C-x C-f` into the buffer.]{#emacs-literal-key-text explanation="The notation describes control-key events rather than text to insert."}
::option[Hold Control, `x`, and `f` simultaneously as one chord.]{#emacs-simultaneous-x-f explanation="The notation contains two successive chords, not one three-key chord."}
:::

## Starting the Built-In Tutorial

Inside Emacs, type `C-h t` to open the interactive tutorial. It teaches movement, insertion, saving, and quitting in a safe practice buffer. `C-h` is the help prefix; `C-h C-h` shows help about using help.

If Emacs displays a menu or welcome buffer, the tutorial remains the better structured starting point than experimenting on an important file.

:::single-choice{#emacs-open-tutorial}
Which Emacs key sequence opens the built-in tutorial?

::option[`C-x C-s`]{#emacs-save-buffer explanation="This sequence saves the current buffer; it does not open the tutorial."}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="This sequence begins exiting Emacs rather than starting a lesson."}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="The help prefix `C-h` followed by `t` starts the Emacs tutorial."}
:::

## Summary

You can now start Emacs and interpret its foundational interface concepts.

1. Check whether the `emacs` command is available.
2. Choose graphical or terminal operation with `-nw`.
3. Visit an existing or new pathname in a buffer.
4. Distinguish buffers, windows, and frames.
5. Read key notation and open the built-in tutorial.
