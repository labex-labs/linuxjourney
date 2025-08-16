---
lang: "zh"
title: "env (环境)"
description: "通过 'env' 命令了解 Linux 环境变量。理解 PATH、HOME 和 USER 变量。获取 Linux 环境管理的初学者指南。"
keywords: "env 命令，Linux 环境变量，PATH 变量，Linux 教程，Linux 初学者，shell 变量，Linux 指南"
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

这会返回一个由冒号分隔的路径列表，您的系统在运行命令时会搜索这些路径。假设您手动从互联网下载并安装了一个软件包，并将其放入一个非标准目录，并且您想运行该命令。您输入 `$ coolcommand`，然后提示显示“command not found”。这很傻；您正在文件夹中查看二进制文件，并且知道它存在。发生的情况是 `$PATH` 变量没有检查该目录中的此二进制文件，因此它会抛出错误。

假设您想从该目录运行大量二进制文件；您可以修改 PATH 变量，将该目录包含在您的 PATH 环境变量中。

## Exercise

以下输出是什么？为什么？

```bash
echo $HOME
```

## Quiz Question

如何查看您的环境变量？

## Quiz Answer

env
