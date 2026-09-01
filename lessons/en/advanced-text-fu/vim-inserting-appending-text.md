---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "en"
order_index: 6
title: "Vim Inserting and Appending Text"
description: "Learn how Vim enters Insert mode before, after, above, or below the current cursor position."
meta_title: "Vim Inserting and Appending Text - Advanced Text-Fu"
meta_description: "Learn the difference between Vim insert vs append modes. Master commands like 'i', 'a', and 'o' to efficiently edit text, vim append content, and vim add line."
meta_keywords: "vim append, append vs insert vim, vim insert vs append, vim add line, vim text editing, vim commands, vim tutorial, insert mode, append mode"
---

In Normal mode, Vim interprets keys as commands. Insert mode inserts typed text into the buffer. Several Normal-mode commands enter Insert mode at different positions, letting you begin typing without separate navigation.

Press `Esc` to leave Insert mode and return to Normal mode. If you are unsure which mode is active, pressing `Esc` is a safe way to reestablish Normal mode, although it can cancel a pending operation.

:::single-choice{#vim-insert-return-normal} Which key normally returns from Insert mode to Normal mode?

::option[`Esc`]{#vim-insert-escape .correct explanation="Escape ends the current insertion and returns Vim to Normal mode."}
::option[`Enter`]{#vim-insert-enter explanation="Enter inserts a line break while remaining in Insert mode."}
::option[`Tab`]{#vim-insert-tab explanation="Tab inserts indentation or triggers configured completion behavior; it does not normally leave Insert mode."}
:::

## Inserting before or after the Cursor

From Normal mode:

- `i`: Enter Insert mode before the cursor.
- `a`: Enter Insert mode after the cursor.

For example, if the cursor is on `b` in `abc`, `i` begins before `b`, while `a` begins after `b`. Both commands change modes; the text you type afterward performs the insertion.

:::single-choice{#vim-insert-before-cursor} Which Normal-mode key enters Insert mode immediately before the cursor?

::option[`a`]{#vim-insert-a-after explanation="Lowercase `a` appends after the cursor rather than inserting before it."}
::option[`o`]{#vim-insert-o-below explanation="Lowercase `o` opens a new line below the current line before entering Insert mode."}
::option[`i`]{#vim-insert-i-before .correct explanation="Lowercase `i` begins insertion at the current cursor position, before the character under it."}
:::

## Inserting at Line Boundaries

Uppercase commands target meaningful positions on the current line:

- `I`: Enter Insert mode before the first nonblank character.
- `A`: Enter Insert mode at the end of the line.

On an indented line, `I` skips indentation and begins before the first nonblank text. Use `0i` if you specifically need to insert at column zero.

:::single-choice{#vim-insert-first-nonblank} Which Normal-mode command begins insertion before the first nonblank character of the current line?

::option[`i`]{#vim-insert-lower-i explanation="Lowercase `i` uses the current cursor position and does not first target the line's initial text."}
::option[`A`]{#vim-insert-capital-a explanation="Uppercase `A` begins insertion at the end of the current line."}
::option[`I`]{#vim-insert-capital-i .correct explanation="Uppercase `I` moves to the first nonblank character and enters Insert mode before it."}
:::

:::single-choice{#vim-append-line-end} Which Normal-mode command moves to the end of the current line and enters Insert mode?

::option[`A`]{#vim-append-capital-a .correct explanation="Uppercase `A` combines an end-of-line jump with entry into Insert mode."}
::option[`$`]{#vim-move-line-end explanation="The dollar motion reaches the line end but remains in Normal mode."}
::option[`a`]{#vim-append-one-position explanation="Lowercase `a` begins after the current cursor rather than jumping to the line end."}
:::

## Opening a New Line

From Normal mode:

- `o`: Open a new line below the current line and enter Insert mode.
- `O`: Open a new line above the current line and enter Insert mode.

Vim applies indentation according to current settings and filetype rules. A count can repeat the open-line operation, but first learn the single-line form so the resulting cursor position is predictable.

:::single-choice{#vim-open-line-above} Which Normal-mode command opens a new line above the current line and enters Insert mode?

::option[`o`]{#vim-open-lower-o explanation="Lowercase `o` opens below the current line."}
::option[`O`]{#vim-open-upper-o .correct explanation="Uppercase `O` opens a new line above and starts insertion there."}
::option[`A`]{#vim-open-upper-a explanation="Uppercase `A` appends at the end of the existing line and does not open a new one above."}
:::

To practice moving between Normal and Insert modes, try this hands-on lab:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both vi/vim and nano. This lab will help you master the fundamental skills of using Vim's Normal and Insert modes.

## Summary

You can now enter Insert mode at the position where new text belongs.

1. Return to Normal mode with `Esc`.
2. Insert before or after the cursor with `i` or `a`.
3. Insert at the first text or line end with `I` or `A`.
4. Open a line below with `o`.
5. Open a line above with `O`.
