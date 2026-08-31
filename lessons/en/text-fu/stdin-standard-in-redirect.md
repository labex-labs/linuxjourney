---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "en"
order_index: 2
title: "stdin (Standard In)"
description: "Learn how programs read standard input and how Bash connects that stream to a file."
meta_title: "stdin (Standard In) - Text-Fu"
meta_description: "Master Linux command-line operations by learning how to redirect stdin (standard input). This guide covers the relationship between stdin and stdout, using the '<' operator, and practical examples like 'cat stdin' to manage data streams effectively."
meta_keywords: "stdin, standardin, redirect stdin, cat stdin, stdin and stdout, standard input, Linux redirection, command line, input stream"
---

Standard input, abbreviated **stdin**, is the stream a program normally reads for incoming data. In an interactive terminal, the shell usually connects stdin to your terminal input, so a program can read what you type.

## Standard Input and File Descriptor 0

By convention, the three standard streams use these file descriptor numbers:

- `0`: standard input (`stdin`)
- `1`: standard output (`stdout`)
- `2`: standard error (`stderr`)

A program can choose whether and how to use these streams. A command designed to read stdin often waits for terminal input when no file operand or other input source is supplied.

:::single-choice{#stdin-descriptor-number}
Which file descriptor conventionally represents standard input?

::option[`0`]{#stdin-fd-zero .correct explanation="Standard input is conventionally file descriptor 0."}
::option[`1`]{#stdin-fd-one explanation="File descriptor 1 conventionally represents standard output, the stream for regular results."}
::option[`2`]{#stdin-fd-two explanation="File descriptor 2 conventionally represents standard error, not standard input."}
:::

## Redirecting a File into stdin

The `<` operator tells Bash to open a file for reading and connect it to the command's stdin:

```bash
$ cat < peanuts.txt
Hello World
```

The shell handles `< peanuts.txt`; `cat` simply reads file descriptor 0. The pathname is not passed to `cat` as a normal file operand.

If the input file does not exist or cannot be opened, the shell reports the redirection error and does not start the command with that input.

:::single-choice{#stdin-from-file}
Which command makes `sort` read its standard input from `names.txt`?

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="Bash opens `names.txt` for reading and connects it to `sort` on file descriptor 0."}
::option[`sort > names.txt`]{#stdout-to-names explanation="A greater-than operator redirects stdout to the file and can truncate it. It does not supply the file as input."}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="This includes an incomplete output redirection. It does not express the requested stdin connection."}
:::

## File Operand versus Input Redirection

Some commands accept either a filename operand or stdin, but the results can differ slightly. For example:

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

Both forms count lines in the same data. In the first form, `wc` knows the filename because it received it as an argument. In the second, it only receives a stream on stdin, so it has no filename to print.

:::single-choice{#stdin-not-command-argument}
Why does `wc -l < peanuts.txt` normally omit `peanuts.txt` from its output?

::option[`wc` deletes the filename after it finishes counting lines.]{#stdin-delete-name explanation="The command does not rename or delete the source file. Only its input connection differs."}
::option[The `<` operator hides every word printed by the command.]{#stdin-hide-words explanation="Input redirection does not filter stdout. The filename is absent because `wc` never received it as an argument."}
::option[Bash provides the file as stdin rather than as a filename argument.]{#stdin-no-filename .correct explanation="The shell consumes the redirection and connects the file to descriptor 0, so `wc` is not given the pathname as an operand."}
:::

## Combining Input and Output Redirection

One command line can redirect more than one stream:

```bash
$ cat < peanuts.txt > banana.txt
```

The shell performs two independent connections:

1. `< peanuts.txt` opens `peanuts.txt` as `cat`'s stdin.
2. `> banana.txt` creates or truncates `banana.txt` and connects it to `cat`'s stdout.

`cat` reads bytes from stdin and writes them to stdout, so `banana.txt` receives the source content. For ordinary file copying, `cp peanuts.txt banana.txt` communicates the intent more directly; this example is about stream connections.

:::single-choice{#stdin-and-stdout-files}
In `cat < input.txt > output.txt`, which file supplies stdin and which receives stdout?

::option[`output.txt` supplies stdin; `input.txt` receives stdout.]{#stdin-output-stdout-input explanation="This reverses the meanings of the redirection operators. The arrows point toward the command for input and toward the file for output."}
::option[`input.txt` supplies stdin; `output.txt` receives stdout.]{#stdin-input-stdout-output .correct explanation="The `<` redirection opens `input.txt` for descriptor 0, and `>` opens `output.txt` for descriptor 1."}
::option[Both files supply stdin, and stdout stays on the terminal.]{#both-stdin explanation="The two operators affect different standard streams. `>` redirects stdout away from the terminal."}
:::

To practice input and output redirection, try these hands-on labs:

1. **[Redirecting Input and Output in Linux](https://labex.io/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practice controlling data flow from commands by manipulating standard output (stdout), standard error (stderr), and standard input (stdin) using operators like >, >>, 2>, and the tee command.
2. **[Data Stream Redirection](https://labex.io/labs/linux-data-stream-redirection-17995)** - Learn the art of Linux stream redirection. Manipulate standard input, output, and error streams, combine outputs, and utilize /dev/null for advanced file operations.
## Summary

You can now connect a command's standard input to a file through the shell.

1. Recognize stdin as file descriptor 0.
2. Redirect a readable file with `<`.
3. Distinguish a filename operand from redirected input.
4. Combine stdin and stdout redirections deliberately.
