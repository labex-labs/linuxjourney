---
index: 19
lang: "zh"
title: "exit 命令"
meta_title: "exit 命令 - 命令行"
meta_description: "学习 Linux exit 命令，如何关闭 shell 会话，logout 与 exit 的区别，以及退出状态值的工作原理。"
meta_keywords: "exit 命令, linux exit, logout 命令, shell 会话, 终端退出, 退出状态, bash exit"
---

## Lesson Content

恭喜你完成了 Linux 之旅的基础课程！你已经掌握了 Linux 的基本知识，现在是时候学习如何正确结束你的会话了。退出 Linux shell 是一个简单但重要的最后步骤。

### 退出命令

结束 shell 会话最常用的方法是使用 `exit` 命令。当你输入 `exit` 并按回车时，当前的 shell 进程将终止。这个命令几乎适用于任何 shell 环境。

```bash
$ exit
```

如果你打开了一个终端窗口，`exit` 通常会关闭其中运行的 shell。如果你通过 SSH 连接，`exit` 会结束远程 shell 会话并返回到本地提示符。

### 退出状态值

`exit` 命令还可以返回一个状态码。状态码为 `0` 通常表示成功，非零状态码通常表示错误或特殊情况。

```bash
$ exit 0
```

你在编写 shell 脚本时会更常见退出状态。在交互式使用中，简单输入 `exit` 就足够了。

### logout 命令

另一个可以用来退出终端的命令是 `logout`。该命令专门用于终止登录 shell。虽然在许多现代系统中它的行为与 `exit` 类似，但了解这两个命令都是良好的习惯。

```bash
$ logout
```

### 关闭终端窗口

如果你在图形用户界面中工作，也可以选择直接关闭终端窗口。此操作通常会发送信号，终止其中运行的 shell 会话。

### 离开 shell 的常见方式

- 输入 `exit` 结束当前 shell。
- 在空提示符下按 `Ctrl-D` 发送文件结束符，通常会退出 shell。
- 在登录 shell 中输入 `logout`。
- 在使用图形终端时关闭终端窗口。

### 常见问题

**exit 和关闭终端窗口一样吗？** 结果通常相似，但 `exit` 是干净地告诉 shell 终止。

**什么是 Ctrl-D？** 它向 shell 发送文件结束符信号。在空提示符时，这通常会退出。

**exit 1 是什么意思？** 它以状态码 `1` 退出，通常用于脚本中表示失败。

你已经成功学会了如何导航、操作文件、获取帮助以及退出 shell。

## Exercise

虽然本主题没有特定的实验，但我们推荐你探索全面的 [Linux 学习路径](https://labex.io/zh/learn/linux) 来练习相关的 Linux 技能和概念。

## Quiz Question

退出 Linux shell 最常用的命令是什么？请仅用一个小写英文单词回答。

## Quiz Answer

exit
