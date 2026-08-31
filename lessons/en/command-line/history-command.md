---
lesson_id: "history-command"
course_id: "command-line"
lang: "en"
order_index: 9
title: "history"
description: "Learn how to inspect, search, reuse, and manage command history in Bash."
meta_title: "history - Command Line"
meta_description: "Learn the Linux history command with examples for viewing command history, rerunning commands, reverse search, deleting entries, and clearing the terminal."
meta_keywords: "linux history command, bash history, history -c, history -d, history -w, Ctrl-R, command history, clear command"
---

Interactive shells can keep a record of commands you enter. This lesson focuses on Bash, where the `history` builtin displays and manages that record. Other shells may use different shortcuts, files, or settings.

## Viewing Bash History

Run `history` to display the current history list:

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Each line has a history number followed by the command.

:::single-choice{#show-command-history}
Which Bash command displays the current numbered history list?

::option[`clear`]{#clear-display explanation="`clear` refreshes the visible terminal area. It does not display previous commands."}
::option[`history -w`]{#write-history explanation="`history -w` writes the current list to the history file. Its purpose is saving rather than displaying the list."}
::option[`history`]{#show-history .correct explanation="The `history` builtin prints commands in the current history list, normally with their history numbers."}
:::

## Reusing Previous Commands

Bash provides several shortcuts for recalling or immediately executing commands:

- **Up Arrow**: Recall earlier commands for review or editing.
- **`!!`**: Expand to and execute the most recent command.
- **Run by number**: Use `!102` to run command number 102 from your history.
- **Run by prefix**: Use `!cat` to run the most recent command that started with `cat`.

History expansion forms that begin with `!` can run a command as soon as you press Enter. Inspect the match first when there is any doubt, especially before adding elevated privileges or operating on important files.

:::single-choice{#repeat-most-recent-command}
Which Bash history expansion repeats the most recently executed command?

::option[`!102`]{#event-number explanation="This expansion selects the command with history number 102. That entry is not necessarily the most recent command."}
::option[`!cat`]{#event-prefix explanation="This selects the most recent command whose text begins with `cat`. It does not mean the most recent command of any kind."}
::option[`!!`]{#previous-event .correct explanation="In Bash, `!!` expands to the previous command and executes it after you submit the line."}
:::

## Searching History Interactively

Press `Ctrl+R` to start a reverse incremental search, then type part of the command you want. Press `Ctrl+R` again to move to an older match.

Press Enter to execute the displayed match. If you want to review or edit it first, use an arrow key to place the command on the editing line instead.

:::single-choice{#search-before-executing}
You remember part of an earlier Bash command and want to find it interactively. What should you press first?

::option[`Ctrl+D`]{#end-input explanation="`Ctrl+D` signals end of input in many terminal contexts and may exit an idle shell. It does not begin a history search."}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C` normally interrupts or cancels the current operation. It does not search command history."}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R` begins a reverse incremental search through command history. Typing more characters narrows the match."}
:::

## Managing the History List

The `history` builtin can modify or save the current list:

- `history -c`: Clear the current in-memory history list.
- `history -w`: Write the current list to the configured history file, commonly `~/.bash_history`.
- `history -d <offset>`: Delete the entry at the given history position.

Examples:

```bash
$ history -d 101
$ history -w
```

Clearing the in-memory list does not by itself guarantee that older commands have disappeared from every file, backup, or other active shell. History behavior also depends on Bash settings and when sessions read or write their files.

:::single-choice{#save-current-history-list}
Which command writes the current Bash history list to its configured history file?

::option[`history -c`]{#clear-current-list explanation="The `-c` option clears the in-memory list. It does not request that the current list be saved."}
::option[`history -d 101`]{#delete-one-entry explanation="The `-d` option removes one selected history entry. It is not the operation for saving the complete list."}
::option[`history -w`]{#write-current-list .correct explanation="The `-w` option writes the current history list to the configured history file."}
:::

## Clearing the Display and Completing Names

Use `clear` when you want a fresh visible terminal area:

```bash
$ clear
```

This does not erase the Bash history list. Depending on the terminal, older display content may also remain available in scrollback.

Tab completion is another way to avoid retyping. Start a command, filename, or directory name and press Tab. Bash may complete an unambiguous match or show possible completions when more than one exists.

Command lines can be stored in history, so do not place passwords, tokens, or other secrets directly in commands when a safer input method is available.

:::single-choice{#distinguish-clear-from-history-clear}
You want to refresh the visible terminal without deleting the in-memory command history. Which command should you run?

::option[`clear`]{#clear-visible-area .correct explanation="`clear` refreshes the visible terminal area while leaving Bash's in-memory history list intact."}
::option[`history -c`]{#clear-memory explanation="This removes entries from the current in-memory history list. It changes history rather than only refreshing the display."}
::option[`history -d 1`]{#delete-first-entry explanation="This asks Bash to delete a selected history entry. It does not clear the visible terminal area."}
:::

## Summary

You can now find and reuse Bash commands while managing history deliberately.

1. Display the current numbered history list.
2. Recall or expand a previous command carefully.
3. Search history interactively with `Ctrl+R`.
4. Delete, clear, or write history entries.
5. Distinguish command history from the terminal display.
