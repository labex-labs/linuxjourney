---
index: 7
lang: "en"
title: "Vim Editing"
meta_title: "Vim Editing - Advanced Text-Fu"
meta_description: "Learn Vim editing basics: delete, change, copy, and paste text efficiently. Master essential Vim commands for beginners and improve your Linux text editing skills."
meta_keywords: "Vim editing, Vim commands, Linux text editor, Vim tutorial, Vim guide, beginner Vim, dd command, Vim delete"
---

## Lesson Content

Editing in Vim is done from Normal mode using operators and motions. You can delete, change, copy (yank), paste (put), and replace text efficiently.

- Press `Esc` to ensure you are in Normal mode before using these commands.

Deletes (operator `d`):

- `x` – delete the character under the cursor
- `dw` – delete from cursor to start of next word
- `d$` – delete from cursor to end of line
- `dd` – delete the current line
- Counts apply: `3dd` deletes three lines; `2dw` deletes two words

Changes (operator `c`, delete then enter Insert mode):

- `cw` – change word from cursor
- `c$` – change to the end of the line
- `cc` – change the whole line

Yank and Put (copy/paste):

- `yw` – yank word
- `yy` – yank the current line
- `p` – put (paste) after the cursor or below the line
- `P` – put (paste) before the cursor or above the line

Replace and other handy edits:

- `r{char}` – replace the character under cursor with `{char}`
- `R` – enter Replace mode to overwrite text
- `J` – join the current line with the next line
- `.` – repeat the last change

Combine operators with motions for power: `d}` deletes to next paragraph; `caw` changes “a word” (word under cursor including surrounding space).

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of text editing in Vim:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both vi/vim and nano. This lab will help you master the fundamental editing commands discussed, such as deleting, changing, yanking, and putting text.

This lab will help you apply the concepts in real scenarios and build confidence with text editing in Linux.

## Quiz Question

Which command deletes the current line in Vim?

## Quiz Answer

dd
