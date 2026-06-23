---
index: 8
lang: "en"
title: "less"
meta_title: "less - Command Line"
meta_description: "Learn the Linux less command with examples for viewing large files, scrolling, searching, jumping to lines, following logs, and quitting less."
meta_keywords: "less command, linux less, view large file linux, search in less, quit less, less -N, less +F, text viewer linux"
---

## Lesson Content

When viewing text files that are too large to fit on a single screen, the `less` command is an invaluable tool. As the old Unix saying goes, "less is more." This is a play on the fact that there is also a `more` command with similar functionality.

The `less` utility displays text in a paged format, allowing you to navigate through a file without flooding your terminal.

### Getting Started with the Less Command

To start viewing a file, use `less` followed by the filename.

```bash
$ less /home/pete/Documents/text1
```

Once you are inside the `less` viewer, your standard shell commands won't work. Instead, you use a specific set of keys to navigate and interact with the text.

### Navigation and Controls

You can use several keys to move through the document:

- **Arrow Keys and Page Keys**: Use `Page Up`, `Page Down`, `Up`, and `Down` to navigate line by line or page by page.
- **Go to Start**: Press `g` to move directly to the beginning of the text file.
- **Go to End**: Press `G` (Shift + g) to jump to the end of the text file.
- **Move half a page**: Press `u` to move up and `d` to move down.
- **Help Menu**: If you forget the commands while inside `less`, just press `h` to display a helpful summary.

### Searching in Less

A powerful feature of `less` is its ability to search for text. Type `/` followed by the text you want to find, and then press Enter.

- `/search_term`: Searches forward for "search_term".
- `?search_term`: Searches backward for "search_term".
- `n`: Jumps to the next occurrence of the search term.
- `N`: Jumps to the previous occurrence.

### How to Exit Less

When you are finished viewing the file, you need to know how to `exit less` and return to your command prompt.

- **Quit**: Simply press `q` to quit the `less` viewer and go back to your shell.

### Useful less Options

You can start `less` with options:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: Show line numbers.
- `+G`: Open at the end of the file.
- `+F`: Follow new content as it is added, similar to `tail -f`.

While following a file with `+F`, press `Ctrl-C` to stop following and return to normal navigation, then press `q` to quit.

### Common Questions

**Is less better than cat?** Use `cat` for short files and `less` for long files or files you need to search.

**How do I search case-insensitively?** Start `less` with `-i`, or type searches normally when the pattern has no uppercase letters on many systems.

**Can less open command output?** Yes. Pipe output into it, such as `dmesg | less`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing and navigating text files in Linux:

1. **[Linux less Command: File Paging](https://labex.io/labs/linux-linux-less-command-file-paging-214301)** - Learn the Linux 'less' command for efficient text file viewing and navigation, including search, line numbers, and pattern matching.
2. **[Linux more Command: File Scrolling](https://labex.io/labs/linux-linux-more-command-file-scrolling-214299)** - Learn the Linux 'more' command for efficient text file viewing, covering basic usage, starting from specific lines, and customizing display.
3. **[Viewing Log and Configuration Files in Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Learn essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files, using commands like `cat`, `more`, and `less`.

These labs will help you apply the concepts in real scenarios and build confidence with text file manipulation and navigation.

## Quiz Question

How do you quit out of the `less` command? Please provide the single character key as your answer. Note: the answer is a case-sensitive English letter.

## Quiz Answer

q
