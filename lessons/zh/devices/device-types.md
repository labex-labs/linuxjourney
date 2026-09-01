---
lesson_id: "device-types"
course_id: "devices"
lang: "zh"
order_index: 2
title: "设备类型"
description: "学习区分字符和块设备节点与管道、套接字及普通文件系统对象。"
meta_title: "设备类型 - 设备"
meta_description: "探索 Linux 中不同的设备类型，包括字符、块、管道和套接字设备。学习 Linux 如何管理设备、如何使用 ls -l /dev 识别设备文件，并理解主设备号和次设备号的作用。"
meta_keywords: "Linux 设备, Linux 设备类型, 设备文件, 字符设备, 块设备, 主次设备号, Linux 设备指南, /dev 目录"
---

`ls -l` 模式中的第一个字符标识对象的文件系统类型。在 `/dev` 下，字符特殊文件和块特殊文件属于设备节点。管道和 Unix 域套接字节点也可能出现在这里，但它们是进程间通信对象，并非硬件设备节点。

```text
$ ls -l /dev/null /dev/sda /run/systemd/journal/dev-log /tmp/example-fifo
crw-rw-rw- 1 root root 1, 3 ... /dev/null
brw-rw---- 1 root disk 8, 0 ... /dev/sda
srw-rw-rw- 1 root root      ... /run/systemd/journal/dev-log
prw------- 1 user user      ... /tmp/example-fifo
```

不同系统上的条目和权限并不相同；该示例只用于说明类型字符。

## 字符设备节点

`c` 表示字符设备。它通常公开面向流或设备特有的接口，而不是可寻址的固定大小存储块。例如终端和 `/dev/null` 等伪设备。

“字符”并不要求每次系统调用恰好传输一个字符。应用程序可以读写缓冲区，而阻塞、成帧和控制行为由驱动程序定义。

:::single-choice{#device-types-character-marker} 模式中的哪个首字符表示字符设备节点？

::option[`b`]{#device-types-marker-block explanation="b 标记表示块设备节点。"}
::option[`p`]{#device-types-marker-pipe explanation="p 标记表示 FIFO，也就是命名管道。"}
::option[`c`]{#device-types-marker-character .correct explanation="字符特殊文件在长列表模式的开头显示 c。"}
:::

## 块设备节点

`b` 表示块设备。块设备通过内核块层提供按块寻址的存储，并可支持缓冲 I/O、分区和文件系统等操作。磁盘、分区和逻辑卷通常都有块设备节点。

块设备节点不是已挂载的文件系统。它表示一个存储设备或逻辑区域；可以在其上创建文件系统，再单独挂载。向错误的块设备节点写入原始数据可能破坏分区表、文件系统或用户数据。

:::single-choice{#device-types-block-marker} 模式的第一个字符 `b` 表示什么？

::option[后台 shell 作业。]{#device-types-background-job explanation="shell 作业状态不会编码成文件系统类型字符。"}
::option[块设备接口。]{#device-types-block-device .correct explanation="块特殊文件通过内核块子系统公开可寻址存储。"}
::option[损坏的符号链接。]{#device-types-broken-link explanation="无论目标当前是否存在，符号链接都使用 l。"}
:::

## FIFO 与套接字节点

`p` 表示 FIFO，也称命名管道。它提供一个具名字节流，进程可以通过它通信。数据被读取后，不会持久保存在 FIFO 节点中。

`s` 表示 Unix 域套接字节点。它为本地套接字端点命名，并可以支持面向连接或数据报通信、描述符传递和对端凭据等功能。使用互联网地址的网络套接字不一定有文件系统节点。

FIFO 和 Unix 套接字节点都不会通过主设备号和次设备号选择硬件驱动程序。

:::single-choice{#device-types-pipe-socket-distinction} 哪项说法正确区分了这两种 IPC 对象类型？

::option[`p` 表示磁盘分区，`s` 表示固态存储。]{#device-types-storage-letters explanation="分区通常属于块设备，而且这些字母不编码存储技术。"}
::option[`p` 表示 FIFO，`s` 表示 Unix 域套接字节点。]{#device-types-p-and-s .correct explanation="这是用于本地进程间通信的两种不同文件系统对象类型。"}
::option[两种类型都通过主设备号标识内核块驱动程序。]{#device-types-ipc-major explanation="FIFO 和套接字节点都不是字符或块设备节点。"}
:::

## 主设备号与次设备号

字符和块设备节点存储一个拆分为主、次两部分的设备号。在长列表中，它们会取代普通文件大小列：

```text
brw-rw---- 1 root disk 8, 0 ... /dev/sda
```

这对数字告诉内核该节点指向哪个已注册设备接口及其实例。主设备号与驱动程序或设备类别相关联，次设备号则由驱动程序解释。不要硬编码“次设备号零始终表示第一个驱动器”之类的假设；映射取决于子系统和内核接口。

使用以下命令明确显示类型和设备号：

```bash
$ stat -c 'type=%F major=%t minor=%T path=%n' /dev/null
```

GNU `stat` 会以十六进制显示 `%t` 和 `%T` 的值。

:::single-choice{#device-types-major-minor-scope} 哪些对象使用主设备号和次设备号标识内核设备接口？

::option[每个普通文件和目录。]{#device-types-all-files explanation="普通文件使用大小和文件系统元数据，而不是设备节点的主次设备号。"}
::option[只有目标缺失的符号链接。]{#device-types-broken-symlinks explanation="符号链接存储路径文本，不会因为目标缺失而变成设备节点。"}
::option[字符设备节点和块设备节点。]{#device-types-device-number-nodes .correct explanation="它们的特殊 inode 元数据包含路由到驱动程序接口的设备号。"}
:::

## 总结

现在，你可以解读特殊文件系统类型，而不会把它们全部当作硬件设备。

1. 将 `c` 识别为字符设备节点，将 `b` 识别为块设备节点。
2. 将 `p` 识别为 FIFO，将 `s` 识别为 Unix 域套接字节点。
3. 只把主设备号和次设备号与设备节点相关联。
4. 将原始块设备访问视为可能具有破坏性的操作。
