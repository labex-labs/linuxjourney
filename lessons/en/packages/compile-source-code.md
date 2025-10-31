---
index: 7
lang: "en"
title: "Compile Source Code"
meta_title: "Compile Source Code - Packages"
meta_description: "Learn how to compile from source code in Linux. This guide covers the essential steps on how to build source code using configure, make, and the recommended checkinstall command for clean package management."
meta_keywords: "how to compile from source code, how to build source code, compile source code, make install, checkinstall, Linux compile, build-essential, configure script, makefile, Linux tutorial"
---

## Lesson Content

Occasionally, you may find a package that is only available as source code. To use it, you'll need to compile and install it on your system. This lesson will guide you through the common process of how to compile from source code.

### Preparing Your System

Before you can compile anything, you need the necessary tools. On Debian-based systems like Ubuntu, you can install them with a single command.

```bash
sudo apt install build-essential
```

The `build-essential` package installs a suite of software development tools, including the GCC compiler and the `make` utility, which are essential for compilation.

After installing the tools, extract the contents of the source code package, which is typically a `.tar.gz` file.

```bash
tar -xzvf package.tar.gz
```

Before proceeding, always check for a `README` or `INSTALL` file inside the extracted directory. These files often contain specific instructions or dependencies required for that particular package.

### The Standard Build Process

While different developers might use various build systems like `cmake`, the most traditional method involves a three-step process. Understanding this is fundamental to learning how to build source code.

First, run the `configure` script. This script checks your system for all the necessary dependencies and libraries the software needs to build and run correctly.

```bash
./configure
```

The `./` prefix tells the shell to execute the script from the current directory. If the script reports any missing dependencies, you must install them before continuing.

Next, run the `make` command. This command reads a file named `Makefile` in the directory, which contains a set of rules on how to compile the source code into executable programs.

```bash
make
```

Finally, to install the software onto your system, you would typically run:

```bash
sudo make install
```

This command copies the compiled files to the appropriate system directories, making the software available for use.

### A Better Way to Install

While `sudo make install` works, it has a significant drawback: it doesn't register the software with your system's package manager. This makes it difficult to track, update, or cleanly uninstall the package later.

A much better approach is to use `checkinstall`. This tool runs the installation process but, instead of copying files directly, it creates a native system package (like a `.deb` file on Debian/Ubuntu) and installs that.

```bash
sudo checkinstall
```

Using `checkinstall` integrates the compiled software into your package management system. This means you can easily remove it later using `apt` or `dpkg`, just like any other package you installed from the official repositories. For this reason, you should always prefer `checkinstall` over `make install`.

To uninstall a package installed with `make install`, you would navigate back to the source directory and run `sudo make uninstall`, but this is not always reliable.

## Exercise

Practice makes perfect! Here's a hands-on lab to reinforce your understanding of building software from source:

1. **[Build Software from Source Code in Linux](https://labex.io/labs/comptia-build-software-from-source-code-in-linux-590853)** - Practice the fundamental process of building and installing software from its source code, including using `configure`, `make`, and `make install`.

This lab will help you apply the concepts in a real scenario and build confidence with compiling software.

## Quiz Question

What should you use instead of `make install` ALWAYS? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

checkinstall
