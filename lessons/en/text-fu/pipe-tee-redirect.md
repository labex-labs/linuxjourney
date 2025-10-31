---
index: 4
lang: "en"
title: "pipe and tee"
meta_title: "pipe and tee - Text-Fu"
meta_description: "Explore the powerful pipe and tee command in Linux. Learn how to chain commands with the Linux pipe tee combination and redirect output to both the screen and a file. This guide covers how to pipe to tee for advanced command-line data flow."
meta_keywords: "pipe and tee command in linux, linux pipe tee, pipe to tee, Linux pipe, tee command, stdout, stdin, command line redirection, Linux tutorial"
---

## Lesson Content

In Linux, the command line becomes incredibly powerful when you start connecting commands. Instead of running one command, saving its output, and then running another, you can create a pipeline to pass data directly between them.

### Understanding the Pipe Operator

Let's start with a command that produces a lot of output:

```bash
ls -la /etc
```

The list of items is likely too long to fit on your screen, making it difficult to read. While you could redirect this output to a file, a more efficient method is to send it directly to another command, like `less`, for easy viewing.

```bash
ls -la /etc | less
```

The pipe operator `|`, represented by a vertical bar, is the key to this process. It takes the standard output (`stdout`) of the command on its left and uses it as the standard input (`stdin`) for the command on its right. In this case, we _piped_ the output of `ls -la /etc` directly into the `less` command. The pipe is a fundamental tool you will use constantly.

### Splitting Output with the Tee Command

What if you want to see the output on your screen _and_ save it to a file simultaneously? This is where the `tee` command comes in. The `pipe and tee command in linux` is a classic combination for logging and monitoring.

```bash
ls | tee peanuts.txt
```

After running this, you will see the output of `ls` on your terminal. If you also check the contents of `peanuts.txt`, you will find the exact same information. The `tee` command effectively splits the output stream into two directions: one to standard output and another to a specified file.

### Combining Pipe and Tee

You can create even more advanced workflows by chaining these commands. A common pattern is to `pipe to tee` in the middle of a longer command chain. This allows you to save an intermediate result while continuing to process the data.

For example, you can use the `linux pipe tee` combination to view and save output before further filtering:

```bash
ls -la /etc | tee etc_listing.txt | grep "conf"
```

This command does three things:

1. It lists the contents of the `/etc` directory.
2. It pipes that output to `tee`, which saves a copy to `etc_listing.txt` and also passes it along.
3. The output from `tee` is then piped to `grep`, which filters for lines containing "conf".

Mastering these commands will significantly improve your efficiency on the command line.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of input/output redirection and pipelines:

1. **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like `>`, `>>`, `2>`, and the `tee` command.
2. **[Sequence Control and Pipeline](https://labex.io/labs/linux-sequence-control-and-pipeline-17994)** - Learn to control command execution sequences, utilize pipelines, and leverage powerful text processing tools like `cut`, `grep`, `wc`, `sort`, and `uniq`.
3. **[Data Stream Redirection](https://labex.io/labs/linux-data-stream-redirection-17995)** - Learn the art of Linux stream redirection, including manipulating standard input, output, and error streams, combining outputs, and utilizing `/dev/null`.

These labs will help you apply the concepts of piping and redirection in real scenarios and build confidence with command-line data manipulation.

## Quiz Question

What single character represents the pipe operator in a Linux command? Please answer with only the symbol.

## Quiz Answer

|
