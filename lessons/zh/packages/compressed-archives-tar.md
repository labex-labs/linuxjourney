---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "zh"
order_index: 3
title: "tar 与 gzip"
description: "学习如何用 `tar` 归档文件、用 `gzip` 压缩数据流，并在安全提取前检查归档。"
meta_title: "tar 与 gzip - 软件包"
meta_description: "关于在 Linux 中使用 tar 和 gzip 的综合指南。了解 tar 压缩、如何创建和提取归档文件，以及 gzip 和 tar 之间的区别。掌握压缩 tar gz 文件的命令，并有效管理软件包。"
meta_keywords: "tar 和 gzip, tar 压缩，gzip tar, 压缩 tar gz, gzip 和 tar, Linux 归档，文件压缩，tar 命令，gzip 命令，Linux 教程"
---

归档与压缩解决的是不同问题。归档把目录树及其元数据组合成一个数据流；压缩则对数据流重新编码以减小体积。`.tar.gz` 文件通常是数据流经过 gzip 压缩的 tar 归档。

## 使用 `gzip` 压缩单个数据流

默认情况下，`gzip` 会压缩文件，并用一个 `.gz` 文件替换原来的名称：

```bash
$ gzip report.txt
```

成功创建 `report.txt.gz` 后，通常会移除 `report.txt`。使用以下命令解压：

```bash
$ gunzip report.txt.gz
```

在支持的系统上，可以用 `gzip -k report.txt` 保留输入文件；需要明确控制时，也可以使用标准流。文件扩展名只是一种约定，不能证明实际格式；`file` 等工具可以检查内容。

:::single-choice{#tar-gzip-gzip-role} 本课中 `gzip` 的主要作用是什么？

::option[把目录树及文件元数据组合成归档。]{#tar-gzip-directory-archive explanation="在应用 gzip 压缩前，由 Tar 承担这一归档任务。"}
::option[压缩单个输入数据流。]{#tar-gzip-compress-stream .correct explanation="Gzip 转换一个字节流，本身不会编码目录层次。"}
::option[把依赖元数据安装到软件包数据库。]{#tar-gzip-package-install explanation="压缩与原生软件包安装和依赖跟踪无关。"}
:::

## 创建 Tar 归档

使用以下命令创建未压缩归档：

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c` 创建新归档。
- `-v` 在处理时列出成员，可省略。
- `-f project.tar` 指定归档文件；由于 `-f` 会使用一个参数，应把文件名紧跟在它旁边。

路径会作为归档成员名称保存。应从有意识选择的工作目录创建归档，避免意外收录密钥、缓存、套接字或范围过大的绝对路径。

:::single-choice{#tar-gzip-create-option} 哪个 `tar` 选项用于创建新归档？

::option[`-x`]{#tar-gzip-option-extract explanation="`-x` 操作用于提取归档成员。"}
::option[`-c`]{#tar-gzip-option-create .correct explanation="创建操作会根据指定输入写入新归档。"}
::option[`-t`]{#tar-gzip-option-list explanation="`-t` 操作用于列出归档成员而不提取。"}
:::

## 创建 Gzip 压缩的 Tar 归档

GNU tar 和许多其他实现可以通过 `-z` 调用 gzip：

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

结果是一个经过 gzip 压缩的 tar 数据流。压缩不会加密归档，也无法向能够读取并解压它的人隐藏内容。如果需要保密性，应采用适当的认证加密流程，并单独管理密钥。

:::single-choice{#tar-gzip-z-option} 所示 `tar` 命令中的 `-z` 请求什么？

::option[使用零知识密钥加密归档。]{#tar-gzip-z-encrypt explanation="Tar 和 gzip 都不会通过此选项提供加密。"}
::option[丢弃每个长度为零的成员。]{#tar-gzip-z-zero explanation="该选项选择 gzip，不会按大小筛选归档成员。"}
::option[让归档数据流经过 gzip 处理。]{#tar-gzip-z-gzip .correct explanation="`z` 选项把 tar 的归档操作连接到 gzip 压缩或解压。"}
:::

## 提取前先列出内容

应把他人提供的归档视为不受信任输入。先列出成员名称：

```bash
$ tar -tzf download.tar.gz
```

检查意外的绝对路径、`..` 路径穿越组成部分、可疑的符号链接或硬链接、设备文件，以及会覆盖重要文件的名称。现代 tar 实现会提供一定保护，但行为和选项不尽相同，而且提取仍会创建攻击者选择的名称与内容。

应提取到新创建的非特权暂存目录：

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

不要以 root 身份提取未经审查的归档。把选定文件移到最终位置前，应先核实实际创建的内容。

:::single-choice{#tar-gzip-list-before-extract} 哪个操作只列出归档成员而不提取？

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="该命令根据当前目录创建或替换归档。"}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="`-x` 操作会把成员写入目标目录。"}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="`-t` 操作读取并显示成员表，`-z` 负责处理 gzip。"}
:::

## 其他压缩格式

Tar 实现还可以配合 bzip2 和 xz 等压缩程序；在 GNU tar 中通常分别用 `-j` 和 `-J` 选择。格式支持和自动检测会有差异，因此应查阅 `tar --help` 或本机手册。ZIP 是另一种归档格式，使用 `zip` 和 `unzip` 等工具操作。

:::single-choice{#tar-gzip-archive-confidentiality} Gzip 压缩会让 tar 归档具有保密性吗？

::option[不会；任何能读取它的人通常都能解压。]{#tar-gzip-not-encryption .correct explanation="压缩改变表示方式和大小，但不提供访问控制或加密保密性。"}
::option[会；gzip 会从文件名派生加密密钥。]{#tar-gzip-filename-key explanation="Gzip 没有实现这种加密机制。"}
::option[会；tar 会在 gzip 处理前加密每个成员。]{#tar-gzip-tar-encrypt explanation="Tar 会归档成员，但不会自动加密内容。"}
:::

可以先在[文件打包和压缩](https://labex.io/zh/labs/linux-file-packaging-and-compression-385413)实验中使用可丢弃文件练习，再在[使用 tar 创建和恢复备份](https://labex.io/zh/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)实验中应用检查和暂存流程。

## 总结

现在，你可以安全地把 tar 归档与 gzip 压缩结合使用。

1. 区分 tar 归档与 gzip 压缩。
2. 使用 `-c` 创建归档，使用 `-z` 处理 gzip 数据流。
3. 提取前先用 `-t` 列出成员，再用 `-x` 提取。
4. 把不受信任内容提取到非特权暂存目录。
5. 将压缩与加密视为不同概念。
