---
index: 2
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

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of input and output redirection in Linux:

1.  **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like >, >>, 2>, and the tee command.
2.  **[Data Stream Redirection](https://labex.io/labs/linux-data-stream-redirection-17995)** - Learn the art of Linux stream redirection. Manipulate standard input, output, and error streams, combine outputs, and utilize /dev/null for advanced file operations.
3.  **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Learn to control command execution sequences and utilize pipelines, which are fundamental to directing output from one command as input to another.

These labs will help you apply the concepts of input and output redirection in real scenarios and build confidence with shell scripting and data manipulation.

## Quiz Question

What redirector do you use to redirect stdin?

## Quiz Answer

<
