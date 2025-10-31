---
index: 5
lang: "zh"
title: "env (环境变量)"
meta_title: "env (环境变量) - Text-Fu"
meta_description: "了解 Linux 中的 env 命令的作用。本指南解释了如何使用 env linux 命令查看和使用 PATH、HOME 和 USER 等 Linux 环境变量。"
meta_keywords: "env, linux env, env linux, env 命令 linux, linux env 命令，env 在 linux 中做什么，环境变量，PATH 变量，shell 变量"
---

## Lesson Content

您的 Linux 系统使用环境变量来存储 shell 和其他进程可以访问的信息。这些变量包含有关您的用户会话和系统配置的有用数据。

### 探索基本环境变量

您可以通过在变量名称前加上 `$` 符号来查看特定变量的值。例如，运行以下命令：

```bash
echo $HOME
```

此命令将显示您的主目录的路径，它可能看起来像 `/home/pete`。

现在，尝试另一个：

```bash
echo $USER
```

这将输出您当前的用户名。但这些信息是从哪里来的呢？它存储在您的 shell 环境中。

### Linux 中的 env 命令的作用

要查看当前为您的会话设置的所有环境变量，您可以使用 `env` 命令。`linux env command` 是检查 shell 配置的基本工具。

```bash
env
```

运行 `env` 命令将输出键值对的列表。以下是您可能会看到的内容的简短示例：

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

理解 `linux env` 对于有效管理您的系统至关重要。

### PATH 变量的重要性

在您的 `env linux` 输出中最重要的变量之一是 `PATH`。您可以使用以下命令专门查看其内容：

```bash
echo $PATH
```

此命令返回一个以冒号分隔的目录列表。当您键入命令时，系统会搜索这些目录以查找相应的可执行文件。

想象一下，您在非标准目录（如 `/opt/coolapp/bin`）中手动安装了一个程序。如果您尝试通过键入 `coolcommand` 来运行它，您可能会收到“command not found”错误。发生这种情况是因为包含您程序的目录未列在 `PATH` 变量中，因此 shell 不知道在哪里查找它。

要解决此问题，您可以修改 `PATH` 变量以包含新目录。通过将自定义目录添加到 `PATH`，您可以使 shell 能够在终端中的任何位置找到并执行您的程序。

## Exercise

熟能生巧！以下是一些实践操作实验，以加强您对 Linux 环境变量的理解：

1.  **[在 Linux 中管理 Shell 环境和配置](https://labex.io/zh/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - 练习创建和管理本地变量和环境变量，理解继承，并通过修改 `.bashrc` 文件使配置持久化。
2.  **[Linux 中的环境变量](https://labex.io/zh/labs/linux-environment-variables-in-linux-385274)** - 学习环境变量的概念和用法，如何创建、修改和管理它们，以及它们在系统配置中的作用。
3.  **[配置 Linux 环境变量](https://labex.io/zh/labs/linux-configure-linux-environment-variables-437861)** - 在 Linux 系统中亲手实践创建、设置和管理环境变量。

这些实验将帮助您在实际场景中应用这些概念，并建立管理 Linux shell 环境的信心。

## Quiz Question

哪个命令会显示您当前所有的环境变量？（请用英文回答，只使用小写命令名）。

## Quiz Answer

env
