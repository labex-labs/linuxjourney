---
index: 8
lang: "en"
title: "Vim Saving and Exiting"
meta_title: "Vim Saving and Exiting - Advanced Text-Fu"
meta_description: "Learn how to save in Vim editor using commands like :w. Master how to save and quit with :wq or ZZ. This guide covers the essential linux wq and vi write and quit commands for efficient file management in Vim."
meta_keywords: "vim how to save, linux wq, vi write and quit, vim how to save and quit, how to save in vim editor, save file vim, exit vim, vim commands"
---

## Lesson Content

After you have finished editing a file, the next step is to save your changes and exit the editor. Vim provides several commands for this purpose, each with a specific function. All these commands are executed in Command-line mode, which you can enter by pressing `:`.

### How to Save in Vim Editor

To save the changes you've made to a file without exiting, you use the write command. This is the fundamental answer to the question "vim how to save".

- `:w` - Writes (saves) the current state of the file to disk.

### Exiting Vim

If you want to quit the editor, you have a couple of options depending on whether you want to save your changes.

- `:q` - Quits the editor. This command only works if you have no unsaved changes.
- `:q!` - Quits the editor and discards any unsaved changes. This is useful when you've made mistakes and want to revert to the last saved version of the file.

### Vim How to Save and Quit

Combining saving and quitting is a very common workflow. The `linux wq` command is a staple for many developers working on the command line.

- `:wq` - This command first writes (saves) the file and then quits. It's a two-in-one action for efficiency. Many users search for `vi write and quit`, and this command works for both Vi and Vim.
- `ZZ` - This is a shortcut equivalent to `:wq`. It saves the file if it has been modified and then quits. It's one character faster to type and a favorite among experienced Vim users.

### Undoing and Redoing Changes

While editing, you might need to reverse an action or bring it back. These commands are used in Normal mode (press `Esc` to enter).

- `u` - Undoes your last action.
- `Ctrl-r` - Redoes the last action that you undid.

Mastering these basic commands is the first step toward proficiency in Vim. As you become more comfortable, you'll find that these operations become second nature. For more advanced features, the official Vim documentation is an excellent resource.

## Exercise

To master these commands, hands-on practice is essential. The following lab provides a real-world scenario to help you reinforce your text editing skills in Vim.

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both Vim and Nano. This lab will solidify your understanding of basic Vim operations, including how to save and quit.

Completing this lab will help you apply these concepts and build confidence with text editing in a Linux environment.

## Quiz Question

How do you quit out of Vim without saving your changes? Please provide the exact command in English, paying attention to case and special characters.

## Quiz Answer

:q
