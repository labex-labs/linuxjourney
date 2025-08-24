---
index: 9
lang: "en"
title: "history"
meta_title: "history - Command Line"
meta_description: "Learn how to use Linux history command, !! shortcut, and Ctrl-R for efficient command recall. Improve your terminal productivity with these essential tips!"
meta_keywords: "Linux history, bash history, Ctrl-R, clear command, Linux tutorial, command line, beginner guide"
---

## Lesson Content

In your shell, there is a history of the commands that you previously entered. You can actually look through these commands. This is quite useful when you want to find and run a command you used previously without actually typing it again.

```bash
history
```

Want to run the same command you did before? Just hit the up arrow.

Want to run the previous command without typing it again? Use `!!`. If you typed `cat file1` and want to run it again, you can actually just type `!!` and it will run the last command you ran.

Another history shortcut is `Ctrl-R`. This is the reverse search command. If you hit `Ctrl-R` and start typing parts of the command you want, it will show you matches. You can navigate through them by hitting the `Ctrl-R` key again. Once you find the command you want to use again, just hit the Enter key.

Our terminal is getting a little cluttered, no? Let's do a little cleanup. Use the `clear` command to clear your display.

```bash
clear
```

There, that looks better, doesn't it?

While we are talking about useful things, one of the most useful features in any command-line environment is tab completion. If you start typing the beginning of a command, file, directory, etc., and hit the Tab key, it will autocomplete based on what it finds in the directory you are searching, as long as you don't have any other files that start with those letters. For example, if you were trying to run the command `chrome`, you can type `chr` and press Tab, and it will autocomplete to `chrome`.

## Exercise

Navigate through your previous command history with the Up and Down keys. Play around with `Ctrl-R` reverse search.

For additional hands-on practice with Linux command line navigation, explore these interactive labs:

- [Linux Directory Navigation](https://labex.io/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

What is the command to clear the terminal?

## Quiz Answer

clear
