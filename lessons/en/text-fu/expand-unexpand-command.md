---
lang: "en"
title: "expand and unexpand"
meta_title: "expand and unexpand - Text-Fu"
meta_description: "Learn to convert tabs to spaces with the `expand` command and spaces to tabs with `unexpand`. Improve text file formatting with this Linux tutorial."
meta_keywords: "expand command, unexpand command, Linux tabs, Linux spaces, text formatting, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

In our lesson on the `cut` command, we had our `sample.txt` file that contained a tab. Normally, tabs would usually show a noticeable difference, but some text files don't show that well enough. Having tabs in a text file may not provide the desired spacing. To change your tabs to spaces, use the `expand` command.

```bash
expand sample.txt
```

The command above will print output with each tab converted into a group of spaces. To save this output in a file, use output redirection as shown below.

```bash
expand sample.txt > result.txt
```

Opposite to `expand`, we can convert back each group of spaces to a tab with the `unexpand` command:

```bash
unexpand -a result.txt
```

## Exercise

What happens if you just type `expand` with no file input?

## Quiz Question

What command is used to convert tabs to spaces?

## Quiz Answer

expand
