---
lesson_id: "filesystem-hierarchy"
course_id: "filesystem"
lang: "zh"
order_index: 1
title: "文件系统层次结构"
description: "了解 Linux 主要目录的预期用途，以及现代合并式目录布局可能存在的差异。"
meta_title: "文件系统层次结构 - 文件系统"
meta_description: "探索标准的 Linux 文件系统层次结构（FSH）。本指南解释了 /bin、/etc、/home 和 /var 等关键目录的用途，清晰概述了 Linux 中的文件系统层次结构。"
meta_keywords: "linux 文件系统层次结构，linux 中的文件系统层次结构，linux 文件层次结构，linux 文件层次，FSH, linux 目录结构"
---

Linux 把已挂载的文件系统呈现为一棵以 `/` 为根的目录树。文件系统层次结构标准（Filesystem Hierarchy Standard，FHS）规定了许多目录的传统用途，但不同发行版、容器、不可变系统和本地策略可能有所差异。依赖某个路径前，应检查实际主机。

```bash
$ ls -ld /*
```

## 根目录与基本系统路径

- `/` 是可见文件系统树的根。
- `/etc` 保存主机特有的系统配置。它可能包含可执行的辅助脚本或启动脚本，因此说它绝不包含可执行内容并不准确。
- `/boot` 保存与启动有关的文件，例如引导加载程序数据；在许多系统上还包含内核和初始 RAM 文件系统映像。
- `/bin` 和 `/sbin` 传统上分别保存基本的用户命令和系统管理命令。
- `/lib` 及其架构特定变体传统上保存基本共享库和加载器组件。

许多现代发行版使用合并式 `/usr` 布局，其中 `/bin`、`/sbin` 和 `/lib` 都是指向 `/usr` 下对应目录的符号链接。应通过命令查找机制和软件包记录确认实际位置，不要假定某个路径一定是实体目录或链接。

:::single-choice{#filesystem-hierarchy-configuration-directory}
哪个目录传统上保存主机特有的系统配置？

::option[`/proc`]{#filesystem-hierarchy-proc-config explanation="Procfs 提供实时进程和内核接口，而不是持久的主机配置文件。"}
::option[`/etc`]{#filesystem-hierarchy-etc .correct explanation="系统和服务配置传统上组织在 `/etc` 下。"}
::option[`/dev`]{#filesystem-hierarchy-dev-config explanation="`/dev` 包含运行时的设备相关对象，而不是通用配置层次。"}
:::

## 发行版软件与本地软件

- `/usr` 包含主要的、可共享且大体只读的操作系统与应用程序层次，其中包括命令、库和与架构无关的数据。
- `/usr/local` 保留给本地管理员在发行版常规 `/usr` 管理范围之外安装的软件和数据。
- `/opt` 可以用独立子树保存附加应用程序软件包。

尽管名称容易误导，`/usr` 通常并不是存放各用户个人文件的位置。发行版的软件包管理器通常管理其中的大部分内容，因此把本地编译的文件复制到 `/usr/bin` 可能会与受管理的软件包冲突。

:::single-choice{#filesystem-hierarchy-local-software}
哪个前缀传统上保留给安装在发行版所管理 `/usr` 内容之外的本地软件？

::option[`/usr/local`]{#filesystem-hierarchy-usr-local .correct explanation="本地层次把管理员安装的软件与发行版的主要 `/usr` 树分开。"}
::option[`/proc/local`]{#filesystem-hierarchy-proc-local explanation="Procfs 是虚拟内核接口，并不是持久的软件前缀。"}
::option[`/dev/local`]{#filesystem-hierarchy-dev-local explanation="设备节点的存放位置不是本地应用程序的传统安装路径。"}
:::

## 用户数据与服务数据

- `/home` 传统上保存非 root 用户的家目录，但目录服务和本地策略可能把它们放到其他位置。
- `/root` 是 root 账户传统的家目录。
- `/srv` 用于保存本系统对外提供的站点特有数据。

家目录路径来自账户信息，而不是简单地把用户名拼接到 `/home` 后面。应使用 `getent passwd USER` 或 shell 解析得到的家目录，不要硬编码假设。

:::single-choice{#filesystem-hierarchy-root-home}
root 账户传统的家目录是什么？

::option[`/home/root`]{#filesystem-hierarchy-home-root explanation="普通家目录通常位于 `/home` 下，但 root 使用独立的传统路径。"}
::option[`/root`]{#filesystem-hierarchy-root .correct explanation="特权账户的家目录传统上直接位于文件系统根目录下。"}
::option[`/usr/root`]{#filesystem-hierarchy-usr-root explanation="`/usr` 是软件和共享数据层次，而不是 root 的家目录。"}
:::

## 可变数据、运行时数据与临时数据

- `/var` 保存日志、缓存、假脱机数据和应用状态等可变数据。系统日志通常位于 `/var/log` 下，但某些系统主要使用日志接口。
- `/run` 保存当前这次启动的易失性运行状态，例如套接字、服务状态和 PID 文件。它通常会在启动时重新创建。
- `/tmp` 用于临时文件，通常允许所有用户写入，并由粘滞位提供保护。
- `/var/tmp` 用于保存应比 `/tmp` 中内容存续更久的临时文件。

`/tmp` 的清理策略因系统而异；不要假定文件一定能保留到重启，也不要假定重启时一定会删除。应用程序应安全地创建临时文件，而不是使用可预测的名称。

:::single-choice{#filesystem-hierarchy-log-path}
哪个路径传统上保存系统日志文件？

::option[`/etc/log`]{#filesystem-hierarchy-etc-log explanation="`/etc` 用于配置，而不是普通的持续累积日志数据。"}
::option[`/var/log`]{#filesystem-hierarchy-var-log .correct explanation="日志属于不断变化的系统数据，组织在可变数据层次下。"}
::option[`/boot/log`]{#filesystem-hierarchy-boot-log explanation="`/boot` 保留给启动相关内容，不用于普通服务日志。"}
:::

## 设备、内核接口与挂载点

- `/dev` 包含设备节点和相关的运行时链接。
- `/proc` 通过 procfs 公开进程和内核接口。
- `/sys` 通过 sysfs 公开内核对象、设备、驱动程序和属性。
- `/media` 常用于自动挂载的可移动介质。
- `/mnt` 是管理员临时挂载文件系统的传统位置。

这些只是目录用途约定，并不等同于权限授予。在非空目录上挂载另一个文件系统，会暂时隐藏该目录原有的内容，直到文件系统被卸载。

:::single-choice{#filesystem-hierarchy-sysfs-path}
哪个路径通常通过 sysfs 公开内核设备模型？

::option[`/srv`]{#filesystem-hierarchy-srv explanation="`/srv` 用于系统对外提供的数据。"}
::option[`/sys`]{#filesystem-hierarchy-sys .correct explanation="Sysfs 传统上挂载到 `/sys`，用于呈现设备、驱动程序、总线和属性。"}
::option[`/opt`]{#filesystem-hierarchy-opt explanation="`/opt` 保存可选附加应用程序的目录树。"}
:::

可以在[在 Linux 中导航文件系统](https://labex.io/zh/labs/comptia-navigate-the-filesystem-in-linux-590971)实验中检查这些路径，并通过[在 Linux 中查找文件和命令](https://labex.io/zh/labs/comptia-find-files-and-commands-in-linux-590834)避免依赖猜测的位置。

## 总结

现在，你可以把 Linux 主要路径与其预期用途联系起来，同时容纳真实系统中的差异。

1. 从以 `/` 为根的统一目录树出发。
2. 区分配置、发行版管理的软件、本地软件和可变数据。
3. 区分家目录与服务数据、运行时状态。
4. 认识到 `/dev`、`/proc` 和 `/sys` 是特殊的运行时接口。
5. 假定布局前，检查符号链接、挂载、账户数据和发行版策略。
