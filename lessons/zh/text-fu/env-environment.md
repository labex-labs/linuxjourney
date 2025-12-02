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

此命令将显示您的主目录路径，它可能看起来像 `/home/pete`。

现在，再试一个：

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

理解 `linux env` 对于有效管理系统至关重要。

### PATH 变量的重要性

在您的 `env linux` 输出中最重要的变量之一是 `PATH`。您可以使用以下命令专门查看其内容：

```bash
echo $PATH
```

此命令返回一个由冒号分隔的目录列表。当您输入一个命令时，系统会搜索这些目录以查找相应的可执行文件。

想象一下，您手动将一个程序安装在非标准目录，如 `/opt/coolapp/bin`。如果您尝试通过键入 `coolcommand` 来运行它，您可能会收到“command not found”错误。发生这种情况是因为包含您程序的目录未列在 `PATH` 变量中，因此 shell 不知道在哪里查找它。

要解决此问题，您可以修改 `PATH` 变量以包含新目录。通过将自定义目录添加到 `PATH`，您可以使 shell 能够在终端中的任何位置找到并执行您的程序。

### 为当前会话设置环境变量

在终端中运行以下命令会将环境变量 `TEST` 设置为仅当前会话有效：

```bash
export TEST=test
```

之后，如果您运行：

```bash
echo $TEST
```

输出将是：

```
test
```

只要终端会话保持打开状态，此变量就可用。一旦您关闭并重新打开终端，该变量将不再存在。

### 使环境变量在会话间持久化

如果您希望环境变量在每次终端会话中都可用（即使在关闭和重新打开终端后），您需要将其添加到 shell 的启动文件中。对于 Bash（许多 Linux 发行版和 macOS 的默认 shell），该文件通常是主目录中的 `.bashrc`。

操作方法如下：

1.  在您喜欢的文本编辑器中打开 `.bashrc`。例如：

        ```bash

    nano ~/.bashrc
    ```

2.  将 `export` 行添加到文件末尾：

        ```bash

    export TEST=test
    ```

3.  保存并退出编辑器（在 Nano 中，这将是 `Ctrl+X`，然后按 `Y` 确认，再按 `Enter`）。

4.  要立即应用更改而无需重新打开终端，请运行：

        ```bash

    source ~/.bashrc
    ```

此后，`TEST` 变量将在所有将来的终端会话中可用，并且即使在关闭和重新打开终端后，运行 `echo $TEST` 也会打印 `test`。

### 关于 Shell 配置文件的一点说明

- 对于 **Bash**（许多系统的默认设置），相关文件是用于非登录交互式 shell 的 `~/.bashrc`。
- 对于 **Zsh**，等效文件通常是 `~/.zshrc`。
- 对于 **Fish**，您通常会使用 `~/.config/fish/config.fish`。

## Exercise

实践造就完美！以下是一些实践实验，以加强您对 Linux 环境变量的理解：

1. **[在 Linux 中管理 Shell 环境和配置](https://labex.io/zh/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - 练习创建和管理本地变量和环境变量，理解继承，并通过修改 `.bashrc` 文件使配置持久化。
2. **[Linux 中的环境变量](https://labex.io/zh/labs/linux-environment-variables-in-linux-385274)** - 学习环境变量的概念和用法，如何创建、修改和管理它们，以及它们在系统配置中的作用。
3. **[配置 Linux 环境变量](https://labex.io/zh/labs/linux-configure-linux-environment-variables-437861)** - 在 Linux 系统中获得创建、设置和管理环境变量的实践经验。

这些实验将帮助您在真实场景中应用这些概念，并增强您管理 Linux shell 环境的信心。

## Quiz Question

哪个命令会显示您当前所有的环境变量？ (请用英文回答，只使用小写的命令名称)

## Quiz Answer

env
