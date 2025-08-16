# stdout (Standard Out)

## Lesson Content

By now, we've become familiar with many commands and their output, and that brings us to our next subject: I/O (input/output) streams. Let's run the following command, and we'll discuss how this works.

```bash
echo Hello World > peanuts.txt
```

What just happened? Well, check the directory where you ran that command, and, lo and behold, you should see a file called `peanuts.txt`. Look inside that file, and you should see the text "Hello World". Lots of things just happened in one command, so let's break it down.

First, let's break down the first part:

```bash
echo Hello World
```

We know this prints "Hello World" to the screen, but how? Processes use I/O streams to receive input and return output. By default, the `echo` command takes input (standard input or stdin) from the keyboard and returns output (standard output or stdout) to the screen. So, that's why when you type `echo Hello World` in your shell, you get "Hello World" on the screen. However, I/O redirection allows us to change this default behavior, giving us greater file flexibility.

Let's proceed to the next part of the command:

```bash
>
```

The `>` is a redirection operator that allows us to change where standard output goes. It allows us to send the output of `echo Hello World` to a file instead of the screen. If the file does not already exist, it will create it for us. However, if it does exist, it will overwrite it (you can add a shell flag to prevent this, depending on what shell you are using).

And that's basically how stdout redirection works!

Well, let's say I didn't want to overwrite my `peanuts.txt`. Luckily, there is a redirection operator for that as well: `>>`.

```bash
echo Hello World >> peanuts.txt
```

This will append "Hello World" to the end of the `peanuts.txt` file. If the file doesn't already exist, it will create it for us, just like the `>` redirector!

## Exercise

Try a couple of commands:

```bash
ls -l /var/log > myoutput.txt
echo Hello World > rm
> somefile.txt
```

## Quiz Question

What redirector do you use to append output to a file?

## Quiz Answer

> >
