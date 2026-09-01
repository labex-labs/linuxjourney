---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "zh"
order_index: 4
title: "安装内核"
description: "学习如何安装、启动和验证发行版内核，并保留经过测试的备用内核。"
meta_title: "安装内核 - 内核"
meta_description: "学习如何安装和管理 Linux 内核，了解内核版本、uname -r 和 apt 命令，开启你的 Linux 内核学习之旅。"
meta_keywords: "Linux 内核, 安装内核, uname -r, apt dist-upgrade, 内核管理, Linux 教程, Linux 入门, Linux 指南"
---

发行版会将内核与模块、initramfs 集成、引导加载程序更新、签名和支持策略一起打包。除非你有意开发或测试自定义内核，并具备恢复计算机的能力，否则应使用这种受管理的工作流程。

## 正在运行和已安装的内核

显示当前运行内核的版本：

```bash
$ uname -r
6.8.0-00-generic
```

该命令不会列出所有已安装的内核，而且安装较新的软件包后，其输出也不会立即改变。系统必须启动新映像，`uname -r` 才会报告新版本。应使用发行版自己的工具查询已安装软件包和启动项。

:::single-choice{#kernel-installation-uname-release} `uname -r` 显示什么？

::option[当前运行内核的版本字符串。]{#kernel-installation-running-release .correct explanation="它报告实时内核状态，而不只是磁盘上存储的最新映像。"}
::option[所有仓库中可用的每个内核软件包。]{#kernel-installation-all-packages explanation="仓库清单应由软件包管理器查询。"}
::option[每个已连接设备的固件版本。]{#kernel-installation-device-firmware explanation="内核版本和设备固件清单是不同的数据。"}
:::

## 优先使用发行版跟踪软件包

安装或保留发行版支持的内核跟踪包或元软件包，以便继续接收未来的安全更新。软件包名称取决于发行版版本、架构、硬件类别和内核变体。例如，Ubuntu 通常提供 `linux-generic`，但云、低延迟、HWE、OEM、实时和特定架构系统会使用其他软件包。

不要直接把 `uname -r` 的版本字符串用作 `apt install` 的操作数，并想当然地认为它有效。安装前应查阅当前发行版文档，并使用软件包管理器检查候选版本。

:::single-choice{#kernel-installation-meta-package} 受支持的内核元软件包为什么有用？

::option[它保证永远不需要重启。]{#kernel-installation-no-reboot explanation="除专门的实时补丁适用范围外，新安装的内核只有在系统启动进入它后才会生效。"}
::option[它会把所有树外驱动程序转换成内置代码。]{#kernel-installation-convert-drivers explanation="外部模块仍然需要兼容的构建和签名。"}
::option[它会跟踪发行版预期的内核更新序列。]{#kernel-installation-update-tracking .correct explanation="随着更新发布，依赖关系会让系统转向较新的受支持映像和模块软件包。"}
:::

## 变更前检查

执行内核事务前：

1. 确认受支持的仓库、软件包签名、版本生命周期和预期内核变体。
2. 确保 `/boot` 或 EFI 系统分区具有足够空间。
3. 至少保留一个确认可用的已安装内核，以及可选择的启动项。
4. 验证控制台、远程管理、救援介质、加密恢复和回滚通道。
5. 检查树外模块、存储和网络驱动程序、安全启动签名、休眠以及虚拟化兼容性。

软件包事务应通过发行版钩子生成匹配的 initramfs 并更新启动项。必须阅读每条错误；如果 initramfs 或加载程序生成失败，仅仅显示软件包已安装并不足以证明成功。

:::single-choice{#kernel-installation-initramfs-error} 为什么出现 initramfs 生成错误时不能认定安装成功？

::option[生成 initramfs 会更改用户的 shell 密码。]{#kernel-installation-initramfs-password explanation="启动归档工作流程与账户身份验证密码无关。"}
::option[新内核可能缺少访问根存储所需的早期模块或工具。]{#kernel-installation-missing-early-tools .correct explanation="映像可能已经安装，但它所需的早期用户空间构件可能缺失或过期。"}
::option[该错误证明当前运行的内核已经停止。]{#kernel-installation-current-stopped explanation="软件包钩子运行时，旧内核仍可以保持活动。"}
:::

## 启动并验证

安排一次受控重启，同时考虑相关人员和活动工作负载。确保默认项失败时可以通过控制台选择旧启动项。启动后执行：

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

在非 systemd 系统上使用等效工具。验证存储、文件系统、网络、图形、输入、安全模块、外部模块、容器、虚拟机和应用程序健康状况。只看到登录提示符并不等于完成验证。

:::single-choice{#kernel-installation-activation} 新安装的普通内核软件包何时会成为正在运行的内核？

::option[输入 `uname -r` 后立即生效。]{#kernel-installation-uname-activates explanation="uname 是只读命令，不能切换内核。"}
::option[计算机启动该内核映像之后。]{#kernel-installation-after-boot .correct explanation="安装文件不会替换内存中已经执行的内核。"}
::option[软件包归档下载完成但尚未安装时。]{#kernel-installation-download-activates explanation="下载的归档不会影响实时执行。"}
:::

## 移除旧内核

只有新内核通过验证后，才能使用软件包管理器支持的清理流程。绝不能移除当前运行的内核、唯一确认可用的备用内核，或活动跟踪软件包所需的软件包。应检查确切的拟移除内容和最终启动项。

手动删除 `/boot` 中的文件会使软件包状态与加载程序状态不一致。如果空间已经耗尽，应先制定恢复方案再更改文件，而不是随意删除映像。

:::single-choice{#kernel-installation-old-kernel-removal} 初步验证新内核期间，应保留哪个内核？

::option[只保留未经测试的新内核。]{#kernel-installation-only-new explanation="测试前移除所有备用项，会把兼容性问题变成恢复事故。"}
::option[启动路径下不保留任何内核文件。]{#kernel-installation-no-kernels explanation="计算机需要可加载的内核构件才能启动 Linux。"}
::option[保留一个可由引导加载程序选择的已知可用备用内核。]{#kernel-installation-known-good-fallback .correct explanation="当新内核无法兼容硬件或工作负载时，备用内核能提供恢复通道。"}
:::

[自定义 GRUB2 启动菜单](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)实验提供了一个可安全恢复的环境，帮助你理解多个启动项。

## 总结

现在，你可以把内核更新视为启动链与兼容性变更。

1. 区分正在运行的版本与已安装映像。
2. 通过正确的发行版软件包跟踪受支持更新。
3. 预先检查存储空间、initramfs、签名、模块和恢复通道。
4. 启动后验证硬件与应用程序行为。
5. 在证明新内核可用前，保留一个已知可用的备用内核。
