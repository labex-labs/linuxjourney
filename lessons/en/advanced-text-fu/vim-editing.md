---
index: 7
lang: "en"
title: "Vim Editing"
meta_title: "Vim Editing - Advanced Text-Fu"
meta_description: "A beginner Vim tutorial on essential editing commands. Learn how to delete, change, copy (yank), and paste text in the Vim text editor to improve your Linux workflow."
meta_keywords: "Vim editing, Vim commands, Linux text editor, Vim tutorial, Vim guide, beginner Vim, dd command, Vim delete"
---

## Lesson Content

Editing text in Vim is a powerful feature that relies on combining operators and motions from Normal mode. This approach allows you to efficiently delete, change, copy (yank), and paste (put) text. Before executing any commands, press `Esc` to ensure you are in Normal mode.

### Understanding Vim Operators and Motions

The core of Vim editing is the formula: `operator + motion`. An operator is an action (like `d` for delete), and a motion is a movement (like `w` for word). For example, `dw` combines the delete operator with the word motion to delete a word. You can also use counts to repeat an action, such as `2dw` to delete two words.

### Deleting Text in Vim

The delete operator is `d`. It's one of the most common Vim commands for text manipulation.

- `x` – Deletes the character directly under the cursor.
- `dw` – Deletes from the cursor to the beginning of the next word.
- `d$` – Deletes from the cursor to the end of the current line.
- `dd` – The `dd` command deletes the entire current line.
- `3dd` – Deletes three lines, starting from the current line.

### Changing Text

The change operator, `c`, works similarly to delete but places you into Insert mode after performing the action. This is useful for replacing text.

- `cw` – Changes the text from the cursor to the end of the word.
- `c$` – Changes text from the cursor to the end of the line.
- `cc` – Changes the entire current line.

### Copying and Pasting in Vim

In Vim, copying is called "yanking" (operator `y`), and pasting is called "putting."

- `yw` – Yanks (copies) a word.
- `yy` – Yanks the entire current line.
- `p` – Puts (pastes) the yanked text after the cursor or on the line below.
- `P` – Puts the text before the cursor or on the line above.

### Other Useful Editing Commands

This Vim guide wouldn't be complete without a few other handy commands.

- `r{char}` – Replaces the single character under the cursor with the specified character.
- `R` – Enters Replace mode, allowing you to overwrite text continuously until you press `Esc`.
- `J` – Joins the current line with the next one.
- `.` – Repeats the last change you made, a very powerful and efficient command.

Combining operators with different motions unlocks the full potential of this Linux text editor. For instance, `d}` deletes to the next paragraph, and `caw` changes "a word" (the word under the cursor including any surrounding space).

## Exercise

To put your knowledge into practice, we recommend the following hands-on lab. It will help you master the fundamental editing commands discussed in this Vim tutorial.

1.  **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both vi/vim and nano. This lab will help you apply concepts like deleting, changing, yanking, and putting text in real scenarios.

## Quiz Question

Which command deletes the current line in Vim? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

dd
