---
lang: "en"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "Learn how to use the Linux sort command for sorting text files. Discover options like reverse and numerical sorting. Improve your Linux command line skills!"
meta_keywords: "Linux sort command, sort -r, sort -n, Linux tutorial, command line, beginner Linux, sort guide"
---

## Lesson Content

The `sort` command is useful for sorting lines.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

You can also do a reverse sort:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

And also sort by numerical value:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

The real power of `sort` comes with its ability to be combined with other commands. Try the following command and see what happens:

```bash
ls /etc | sort -rn
```

## Quiz Question

What flag do you use to perform a reverse sort?

## Quiz Answer

-r
