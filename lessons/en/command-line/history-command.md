---
index: 9
lang: "en"
title: "history"
meta_title: "history - Command Line"
meta_description: "Learn the Linux history command with examples for viewing command history, rerunning commands, reverse search, deleting entries, and clearing the terminal."
meta_keywords: "linux history command, bash history, history -c, history -d, history -w, Ctrl-R, command history, clear command"
---

## Lesson Content

Your shell keeps a record of the commands you have previously entered. You can access this list when you want to find and reuse a command without retyping it. The `history` command is a fundamental tool in Bash and many Unix-like shell environments.

### Viewing Your Command History

To see the list of commands you have used, type `history`.

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Each line has a history number followed by the command.

### Re-running Previous Commands

The shell provides several shortcuts to make re-running commands easier.

- **Up Arrow**: Want to run the same command you just did? Just press the up arrow key to cycle backward through your history.
- **The `!!` Shortcut**: To execute the most recent command again, you can use `!!`. For example, if you just ran `cat file1`, typing `!!` and pressing Enter will run `cat file1` again.
- **Run by number**: Use `!102` to run command number 102 from your history.
- **Run by prefix**: Use `!cat` to run the most recent command that started with `cat`.

### Searching Your History

One of the most powerful history shortcuts is `Ctrl-R`. This initiates a reverse search. After pressing `Ctrl-R`, start typing any part of the command you're looking for, and the shell will display the most recent match. You can press `Ctrl-R` repeatedly to cycle through older matches. Once you find the command you want, just press Enter to execute it.

If you want to edit the matched command before running it, press the right arrow key or left arrow key instead of Enter.

### Managing the History List

Beyond just viewing your history, you can also manage it directly.

- **Clear current history list**: `history -c` removes all entries from the history list in memory.
- **Write history to file**: `history -w` saves the current session's history to your history file, usually `~/.bash_history`.
- **Delete a specific entry**: `history -d <offset>` removes one command by its history number.

Examples:

```bash
$ history -d 101
$ history -w
```

Be careful with history expansion commands such as `!!` and `!102`. Use `history` first to confirm what will run.

### Other Useful Terminal Tools

As your terminal window fills up, you might want to clean it. Use the `clear` command to wipe your display and start with a fresh screen.

```bash
$ clear
```

Another indispensable feature is tab completion. If you start typing the beginning of a command, filename, or directory and press the Tab key, the shell will attempt to autocomplete it. If there are multiple possibilities, it may show you the options or do nothing. Pressing Tab a second time will often list all possible completions.

### Common Questions

**Where is Bash history stored?** Usually in `~/.bash_history`, though the exact behavior depends on shell settings.

**Does history include every command immediately?** Not always. Some shells write history when a session exits unless configured otherwise.

**Can history contain sensitive data?** Yes. Avoid typing passwords, tokens, or secrets directly into commands.

**What is the difference between history -c and clear?** `history -c` clears command history in memory. `clear` only clears the terminal screen.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What is the command to clear the terminal? (Please answer in lowercase English letters only)

## Quiz Answer

clear
