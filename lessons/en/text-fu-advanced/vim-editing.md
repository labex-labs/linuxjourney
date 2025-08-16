---
title: "Vim Editing"
description: "Learn Vim editing basics: delete, change, copy, and paste text efficiently. Master essential Vim commands for beginners and improve your Linux text editing skills."
keywords: "Vim editing, Vim commands, Linux text editor, Vim tutorial, Vim guide, beginner Vim, dd command, Vim delete"
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

Open a file with `vim [file]` and try: `dw`, `cw`, `yy` then `p`, `dd`, `J`, and `.` to repeat a change.

## Quiz Question

Which command deletes the current line in Vim?

## Quiz Answer

dd
