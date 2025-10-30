---
index: 11
lang: "en"
title: "Emacs Buffer Navigation"
meta_title: "Emacs Buffer Navigation - Advanced Text-Fu"
meta_description: "Learn Emacs buffer navigation commands. Switch, close, and split buffers efficiently with this beginner-friendly Emacs tutorial. Improve your workflow!"
meta_keywords: "Emacs buffer navigation, Emacs commands, C-x b, C-x k, Linux tutorial, Emacs guide, beginner Emacs"
---

## Lesson Content

To move around buffers (or files you're visiting), use the following commands:

### Switch buffers

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### Close the buffer

```
C-x k
```

### Split the current buffer

```
C-x 2
```

This allows you to see multiple buffers on one screen. To move between these buffers, use: C-x o

### Set a single buffer as the current screen

```
C-x 1
```

If you have ever used a terminal multiplexer like `screen` or `tmux`, the buffer commands will feel very familiar.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of navigating and manipulating text files and buffers:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating, editing, saving, and navigating text within the Vim and Nano editors, which are crucial for working with buffers.
2. **[Linux cat Command: File Concatenating](https://labex.io/labs/linux-linux-cat-command-file-concatenating-210986)** - Learn to view, concatenate, and manipulate text files, directly applying to how you might interact with buffer content.
3. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using commands like `cat`, `more`, and `less` to efficiently view and navigate text files, simulating real-world scenarios of examining buffer-like content.

These labs will help you apply the concepts in real scenarios and build confidence with text file and buffer manipulation in Linux.

## Quiz Question

How do you kill a buffer?

## Quiz Answer

C-x k
