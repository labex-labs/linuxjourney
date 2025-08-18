---
lang: "en"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Learn how to use the Linux paste command to merge file lines. Discover delimiters and combine files with this essential Linux command tutorial."
meta_keywords: "Linux paste command, paste command tutorial, merge file lines, Linux commands, beginner Linux, Linux guide"
---

## Lesson Content

The `paste` command is similar to the `cat` command; it merges lines together in a file. Let's create a new file with the following contents:

```
sample2.txt
The
quick
brown
fox
```

Let's combine all these lines into one line:

```bash
paste -s sample2.txt
```

The default delimiter for `paste` is TAB, so now there is one line with TABs separating each word.

Let's change this delimiter (`-d`) to something a little more readable:

```bash
paste -d ' ' -s sample2.txt
```

Now everything should be on one line delimited by spaces.

## Exercise

Try to paste multiple files together. What happens?

## Quiz Question

What flag do you use with `paste` to make everything go on one line?

## Quiz Answer

-s
