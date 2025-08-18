---
lang: "en"
title: "less"
meta_title: "less - Command Line"
meta_description: "Learn how to use the Linux 'less' command for efficient text file viewing and navigation. Master paging, searching, and quitting with this beginner-friendly guide."
meta_keywords: "less command, Linux less, view text files, navigate files, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

If you are viewing text files larger than a simple output, `less` is more. (There is actually a command called `more` that does something similar, so this is ironic.) The text is displayed in a paged manner, so you can navigate through a text file page by page.

Go ahead and look at the contents of a file with `less`. Once you’re in the `less` command, you can actually use other keyboard commands to navigate in the file.

```bash
less /home/pete/Documents/text1
```

Use the following commands to navigate through `less`:

- `q` - Used to quit out of `less` and go back to your shell.
- `Page up`, `Page down`, `Up` and `Down` - Navigate using the arrow keys and page keys.
- `g` - Moves to the beginning of the text file.
- `G` - Moves to the end of the text file.
- `/search` - You can search for specific text inside the text document. Preface the words you want to search with `/`.
- `h` - If you need a little help about how to use `less` while you’re in `less`, use help.

## Exercise

Run `less` on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file.

## Quiz Question

How do you quit out of a `less` command?

## Quiz Answer

q
