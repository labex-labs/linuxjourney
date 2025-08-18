---
lang: "en"
title: "stdin (Standard In)"
meta_title: "stdin (Standard In) - Text-Fu"
meta_description: "Learn about stdin (standard input) redirection in Linux. Understand how to use the '<' operator with files and commands. Explore practical examples and improve your Linux command-line skills."
meta_keywords: "stdin, standard input, Linux redirection, < operator, Linux tutorial, command line, beginner, guide"
---

## Lesson Content

In our previous lesson, we learned that we have different stdout streams we can use, such as a file or the screen. Well, there are also different standard input (stdin) streams we can use as well. We know that we have stdin from devices like the keyboard, but we can use files, output from other processes, and the terminal as well. Let's see an example.

Let's use the `peanuts.txt` file from the previous lesson for this example. Remember, it had the text "Hello World" in it.

```bash
cat < peanuts.txt > banana.txt
```

Just like we had `>` for stdout redirection, we can use `<` for stdin redirection.

Normally, in the `cat` command, you send a file to it and that file becomes the stdin. In this case, we redirected `peanuts.txt` to be our stdin. Then the output of `cat peanuts.txt`, which would be "Hello World", gets redirected to another file called `banana.txt`.

## Exercise

Try out a couple of commands:

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

What redirector do you use to redirect stdin?

## Quiz Answer

<
