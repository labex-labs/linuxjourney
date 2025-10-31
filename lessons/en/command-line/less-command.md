---
index: 8
lang: "en"
title: "less"
meta_title: "less - Command Line"
meta_description: "Master the Linux less command for efficient text file viewing. This guide covers how to use the command less, navigate, perform a unix less search, and how to exit less."
meta_keywords: "less command, command less, exit less, unix less search, linux less, view text files, navigate files, linux command line"
---

## Lesson Content

When viewing text files that are too large to fit on a single screen, the `less command` is an invaluable tool. As the old Unix saying goes, "less is more." (This is a play on the fact that there is also a `more` command with similar functionality). The `less` utility displays text in a paged format, allowing you to navigate through a file page by page without loading the entire file into memory.

### Getting Started with the Less Command

To start viewing a file, simply use the `command less` followed by the filename. This will open the file in the `less` interface.

```bash
less /home/pete/Documents/text1
```

Once you are inside the `less` viewer, your standard shell commands won't work. Instead, you use a specific set of keys to navigate and interact with the text.

### Navigation and Controls

You can use several keys to move through the document:

- **Arrow Keys and Page Keys**: Use `Page Up`, `Page Down`, `Up`, and `Down` to navigate line by line or page by page.
- **Go to Start**: Press `g` to move directly to the beginning of the text file.
- **Go to End**: Press `G` (Shift + g) to jump to the end of the text file.
- **Help Menu**: If you forget the commands while inside `less`, just press `h` to display a helpful summary.

### Unix Less Search

A powerful feature of `less` is its ability to search for text. To perform a `unix less search`, type `/` followed by the text you want to find, and then press Enter. This will highlight all occurrences of your search term.

- `/search_term`: Searches forward for "search_term".
- `?search_term`: Searches backward for "search_term".
- `n`: Jumps to the next occurrence of the search term.
- `N`: Jumps to the previous occurrence.

### How to Exit Less

When you are finished viewing the file, you need to know how to `exit less` and return to your command prompt.

- **Quit**: Simply press `q` to quit the `less` viewer and go back to your shell.

Mastering the `less command` is a fundamental skill for anyone working on the Linux command line, making file inspection much more efficient.

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
