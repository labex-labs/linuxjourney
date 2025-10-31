---
index: 3
lang: "en"
title: "stderr (Standard Error)"
meta_title: "stderr (Standard Error) - Text-Fu"
meta_description: "Learn how to manage standard error in Linux. This guide covers stderr redirection, the stderr file descriptor (2), and how to redirect stderr to a file or /dev/null using 2>, 2>&1, and &>."
meta_keywords: "stderr, standard error linux, stderr file descriptor, stderr file, linux standard error, redirect stderr, 2>, 2>&1, &>, /dev/null, bash error handling"
---

## Lesson Content

Let's explore what happens when a command produces an error. Try to list the contents of a directory that doesn't exist and redirect the output to a file named `peanuts.txt`.

```bash
ls /fake/directory > peanuts.txt
```

Instead of a clean prompt, you will see an error message on your screen:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

You might be wondering why this message wasn't sent to the file. This is because another I/O stream is at play: **standard error**, or **stderr**.

### What is Standard Error in Linux?

In Linux, `stderr` is a default output stream used by programs to send error messages and diagnostics. It is completely separate from the standard output (`stdout`) stream, which is used for normal program output. By default, both `stdout` and `stderr` send their output to your terminal screen, which is why you see the error message directly.

To control `stderr`, you need a different redirection method.

### Understanding File Descriptors

To manage I/O streams like `stdin`, `stdout`, and `stderr`, the system uses file descriptors. A **file descriptor** is a non-negative number that the kernel uses to identify an open file or stream. The default file descriptors are:

- `0`: stdin (standard input)
- `1`: stdout (standard output)
- `2`: stderr (standard error)

The number `2` is the dedicated **stderr file descriptor**, and we can use it to control where error messages go.

### Redirecting stderr to a File

To redirect `stderr` to a file, you use the file descriptor `2` followed by the `>` operator. This command will send any error messages into the specified `stderr file`.

```bash
ls /fake/directory 2> peanuts.txt
```

Now, your terminal will be quiet, and the error message will be inside `peanuts.txt`.

### Combining stdout and stderr

What if you want to capture both normal output and error messages in the same file? You can achieve this by redirecting both streams.

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

Let's break this down:

1.  `> peanuts.txt` redirects `stdout` (file descriptor 1) to the `peanuts.txt` file.
2.  `2>&1` redirects `stderr` (file descriptor 2) to the same location that `stdout` (file descriptor 1) is currently pointing to.

The order is important. `2>&1` sends `stderr` to the current destination of `stdout`. In this case, `stdout` is pointing to a file, so `stderr` is also sent to that file.

A more modern and shorter way to redirect both `stdout` and `stderr` is by using `&>`.

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### Discarding Error Messages

Sometimes, you might want to run a command and completely ignore any potential error messages. To do this, you can redirect `stderr` to a special file called `/dev/null`, which discards any data written to it.

```bash
ls /fake/directory 2> /dev/null
```

This command will execute, and any error output from `stderr` will be sent to `/dev/null` and discarded, leaving your screen clean.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of input/output redirection:

1. **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - In this lab, you will learn to redirect input and output in the Linux shell. You will practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like >, >>, 2>, and the tee command.

This lab will help you apply the concepts of I/O redirection in real scenarios and build confidence with managing data streams in Linux.

## Quiz Question

What is the operator used to redirect the `stderr` stream? Please provide the exact operator in your answer.

## Quiz Answer

2>
