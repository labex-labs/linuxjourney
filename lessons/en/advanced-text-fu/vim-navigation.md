---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "en"
order_index: 5
title: "Vim Navigation"
description: "Learn how to move by characters, words, lines, and file positions in Vim's Normal mode."
meta_title: "Vim Navigation - Advanced Text-Fu"
meta_description: "Learn Vim navigation basics using h, j, k, l keys. Understand essential Vim movement for beginners and improve your Linux command line skills."
meta_keywords: "Vim navigation, Vim tutorial, Linux Vim, Vim movement, Vim basics, beginner Vim, Linux text editor, Vim guide"
---

Vim provides keyboard motions that work in a terminal without requiring a mouse. Some Vim configurations also support mouse input, but learning motions makes navigation composable with editing commands.

Press `Esc` before practicing to return to Normal mode.

## Moving by Characters and Screen Lines

The foundational Normal-mode motions are:

- `h`: Move one character left.
- `j`: Move one screen line down.
- `k`: Move one screen line up.
- `l`: Move one character right.

Arrow keys commonly perform similar movement, but `h`, `j`, `k`, and `l` keep your hands near other commands. On a wrapped display line, `j` and `k` normally move by file lines; `gj` and `gk` move by displayed screen lines.

:::single-choice{#vim-navigation-down} In Normal mode, which key moves the cursor down one line?

::option[`k`]{#vim-nav-k-up explanation="The `k` motion moves upward one line."}
::option[`l`]{#vim-nav-l-right explanation="The `l` motion moves one character to the right."}
::option[`j`]{#vim-nav-j-down .correct explanation="The `j` motion moves downward one line in Normal mode."}
:::

## Prefixing Motions with Counts

Type a positive count before many motions to repeat them. For example:

```text
5j
3l
```

`5j` moves down five lines, while `3l` moves right three character positions when possible. Counts also combine with word and editing commands.

:::single-choice{#vim-navigation-count} What does `4k` do in Normal mode?

::option[Moves down four lines when possible.]{#vim-nav-four-down explanation="Downward movement uses `j`; `k` moves in the opposite direction."}
::option[Moves up four lines when possible.]{#vim-nav-four-up .correct explanation="The count `4` repeats the upward `k` motion four times."}
::option[Deletes four lines above the cursor.]{#vim-nav-delete-four explanation="A motion by itself changes the cursor position. Deletion would require an operator such as `d`."}
:::

## Moving by Words

Useful word motions include:

- `w`: Move to the beginning of the next word.
- `b`: Move to the beginning of the current or previous word.
- `e`: Move to the end of the current or next word.

Uppercase `W`, `B`, and `E` use whitespace-delimited WORDS, treating punctuation differently. Prefix a count to move through several words, such as `3w`.

:::single-choice{#vim-navigation-next-words} Which Normal-mode command moves forward to the beginning of the third following word position?

::option[`3w`]{#vim-nav-three-words .correct explanation="The count applies the next-word motion three times."}
::option[`w3`]{#vim-nav-word-three explanation="Counts precede motions in this command form; placing `3` afterward does not express the requested movement."}
::option[`3b`]{#vim-nav-three-back explanation="The `b` motion travels toward earlier word beginnings rather than forward."}
:::

## Moving within a Line

These motions target positions on the current line:

- `0`: Move to column zero.
- `^`: Move to the first nonblank character.
- `$`: Move to the end of the line.

The difference between `0` and `^` matters on indented lines.

:::single-choice{#vim-navigation-first-nonblank} Which motion moves to the first nonblank character of an indented line?

::option[`0`]{#vim-nav-column-zero explanation="Zero moves to the first column, which can contain indentation whitespace."}
::option[`$`]{#vim-nav-line-end explanation="The dollar motion targets the end of the line."}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="The caret motion skips leading blanks and lands on the first nonblank character."}
:::

## Moving through the File

Use these Normal-mode commands for larger jumps:

- `gg`: Move to the first line.
- `G`: Move to the final line.
- `42G`: Move to line 42.
- `Ctrl+F`: Move forward approximately one screen.
- `Ctrl+B`: Move backward approximately one screen.

The command `:42` followed by Enter is another way to jump to line 42.

:::single-choice{#vim-navigation-file-end} Which Normal-mode command moves to the final line of the buffer?

::option[`gg`]{#vim-nav-first-line explanation="Lowercase `gg` moves to the first line, not the final one."}
::option[`$`]{#vim-nav-current-line-end explanation="The dollar motion goes to the end of the current line rather than the end of the file."}
::option[`G`]{#vim-nav-last-line .correct explanation="Uppercase `G` with no count jumps to the final line."}
:::

To practice keyboard navigation while editing a disposable file, try this hands-on lab:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both Vim and Nano in a real Linux environment.

## Summary

You can now navigate a Vim buffer at several useful scales.

1. Move by characters or lines with `h`, `j`, `k`, and `l`.
2. Repeat motions with a numeric prefix.
3. Move between word boundaries with `w`, `b`, and `e`.
4. Target the start, first text, or end of a line.
5. Jump to file positions with `gg`, `G`, or a line number.
