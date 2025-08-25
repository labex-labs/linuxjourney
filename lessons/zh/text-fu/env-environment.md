---
index: 5
lang: "zh"
title: "env (环境)"
meta_title: "env (环境) - Text-Fu"
meta_description: "通过 'env' 命令了解 Linux 环境变量。理解 PATH、HOME 和 USER 变量。获取管理 Linux 环境的初学者指南。"
meta_keywords: "env 命令，Linux 环境变量，PATH 变量，Linux 教程，Linux 初学者，shell 变量，Linux 指南"
---

## Lesson Content

运行以下命令：

```bash
echo $HOME
```

您应该会看到您的主目录路径；我的看起来像 /home/pete。

那这个命令呢？

```bash
echo $USER
```

您应该会看到您的用户名！

这些信息是从哪里来的？它来自您的环境变量。您可以通过输入以下命令来查看它们：

```bash
env
```

这会输出大量关于您当前设置的环境变量的信息。这些变量包含 shell 和其他进程可以使用的有用信息。

这是一个简短的例子：

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

一个特别重要的变量是 PATH 变量。您可以通过在变量名前面加上 `$` 来访问这些变量，如下所示：

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

这会返回一个由冒号分隔的路径列表，您的系统在运行命令时会搜索这些路径。假设您手动从互联网下载并安装了一个软件包，并将其放入一个非标准目录，并且您想运行该命令。您输入 `$ coolcommand`，提示符显示“command not found”。这很奇怪；您正在文件夹中查看二进制文件，并且知道它存在。发生的情况是 `$PATH` 变量没有在该目录中检查此二进制文件，因此它会抛出错误。

假设您想从该目录运行大量二进制文件；您可以修改 PATH 变量，将该目录包含在您的 PATH 环境变量中。

## Exercise

熟能生巧！以下是一些动手实验，以加深您对 Linux 环境变量的理解：

1. **[在 Linux 中管理 Shell 环境和配置](https://labex.io/zh/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - 练习创建和管理本地变量和环境变量，理解继承，并通过修改 `.bashrc` 文件使配置持久化。
2. **[Linux 中的环境变量](https://labex.io/zh/labs/linux-environment-variables-in-linux-385274)** - 学习环境变量的概念和用法，如何创建、修改和管理它们，以及它们在系统配置中的作用。
3. **[配置 Linux 环境变量](https://labex.io/zh/labs/linux-configure-linux-environment-variables-437861)** - 获得在 Linux 系统中创建、设置和管理环境变量的实践经验。

这些实验将帮助您在实际场景中应用这些概念，并增强您管理 Linux shell 环境的信心。

## Quiz Question

如何查看您的环境变量？

## Quiz Answer

env
