---
index: 6
lang: "en"
title: "Vim Inserting and Appending Text"
meta_title: "Vim Inserting and Appending Text - Advanced Text-Fu"
meta_description: "Learn Vim insert and append modes. Understand 'i', 'a', 'I', 'A', 'o', 'O' commands for efficient text editing. Improve your Vim skills now!"
meta_keywords: "Vim insert mode, Vim append, Vim commands, Vim tutorial, Linux text editor, beginner Vim, Vim guide, Vim 'i' 'a'"
---

## Lesson Content

Vim has two main modes you will use often: Normal mode (for commands) and Insert mode (for typing text).

- Press `Esc` to return to Normal mode at any time.

Enter Insert mode in different ways depending on where you want to type:

- `i` – insert before the cursor
- `a` – append after the cursor
- `I` – insert at the beginning of the current line
- `A` – append at the end of the current line
- `o` – open a new line below the current line and start inserting
- `O` – open a new line above the current line and start inserting

Tip: You can prefix these with a count. For example, `3o` opens three new lines below.

When you are done inserting text, press `Esc` to go back to Normal mode.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Vim's text editing capabilities:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both vi/vim and nano. This lab will help you master the fundamental skills of using Vim's Normal and Insert modes.

This lab will help you apply the concepts in real scenarios and build confidence with text editing in Linux using Vim.

## Quiz Question

Which key enters Insert mode before the cursor?

## Quiz Answer

i
