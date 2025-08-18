---
index: 14
lang: "en"
title: "find"
meta_title: "find - Command Line"
meta_description: "Learn how to use the Linux 'find' command to locate files and directories. Discover basic search options and improve your Linux file management skills."
meta_keywords: "Linux find command, find files Linux, Linux directory search, find command tutorial, Linux file management, beginner Linux, Linux guide"
---

## Lesson Content

With all these files we have on the system, it can get a little hectic trying to find a specific one. Well, there's a command we can use for that: `find`!

```bash
find /home -name puppies.jpg
```

With `find`, you'll have to specify the directory you'll be searching in and what you're searching for. In this case, we are trying to find a file by the name of `puppies.jpg`.

You can specify what type of file you are trying to find.

```bash
find /home -type d -name MyFolder
```

You can see that I set the type of file I'm trying to find as `d` for directory, and I'm still searching by the name of `MyFolder`.

One cool thing to note is that `find` doesn't stop at the directory you are searching; it will look inside any subdirectories that directory may have as well.

## Exercise

1. Find a file from the root directory that has the word "net" in it.

## Quiz Question

What option should I specify for `find` if I want to search by name?

## Quiz Answer

-name
