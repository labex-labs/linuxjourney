---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "zh"
order_index: 4
title: "NFS"
description: "学习如何发现、挂载、验证并安全自动化 NFS 客户端挂载。"
meta_title: "NFS - 网络共享"
meta_description: "了解如何在 Linux 中使用网络文件系统（NFS）。本课介绍设置 NFS 客户端、使用 mount 命令，以及配置自动挂载以便访问网络共享。"
meta_keywords: "NFS, NFS 客户端, 自动挂载, 网络文件系统, Linux 网络, mount 命令, Linux 教程, 初学者"
---

网络文件系统让客户端通过本地文件系统命名空间访问服务器导出。服务器控制导出和大部分访问策略；客户端控制在何处以及何时挂载获得授权的导出。

## 准备客户端

安装发行版的 NFS 客户端工具，在 Debian 系统上通常打包为 `nfs-common`，在 Red Hat 系统上通常为 `nfs-utils`。与服务器管理员确认 DNS 或地址可达性、允许的 NFS 版本、防火墙策略和确切导出路径。

`showmount -e SERVER` 可以列出通过旧式挂载协议提供的导出，但对只使用 NFSv4 的服务器并非始终权威。列出失败不能证明不存在已授权的 NFSv4 导出。

:::single-choice{#nfs-showmount-limit} 为什么 `showmount -e` 对 NFSv4 服务器可能不完整？

::option[它查询的旧式导出列表协议可能没有对外提供。]{#nfs-showmount-protocol .correct explanation="NFSv4 可以在不提供该独立列表服务的情况下运行。"}
::option[它只显示本地 CPU 温度。]{#nfs-showmount-temperature explanation="该命令用于查询 NFS 服务器导出信息。"}
::option[它会永久禁用每个列出的导出。]{#nfs-showmount-disables explanation="列出属于只读发现请求。"}
:::

## 挂载导出

创建空的专用挂载点，并挂载获准的导出：

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

只有策略或兼容性要求时才指定版本，例如 `-o vers=4.2`。不要猜测性能或安全选项。确认最终来源、类型和选项：

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands} 挂载命令中的 `server.example.net:/srv/team` 是什么？

::option[隐藏远程导出的本地目录。]{#nfs-local-mountpoint explanation="示例中的本地挂载点是 /mnt/team。"}
::option[要安装的客户端软件包名称。]{#nfs-package-name explanation="软件包名称因发行版而异，不是挂载源操作数。"}
::option[服务器和导出的远程路径。]{#nfs-remote-export .correct explanation="主机与冒号后的路径共同标识 NFS 来源。"}
:::

## 理解身份与权限

NFS 访问结合了服务器导出规则、协议安全、数字身份或目录服务，以及文件系统权限。两台主机显示相同用户名，并不保证数字 ID 相同。传统 `AUTH_SYS` 发送客户端提供的数字身份，高度依赖可信客户端和网络控制；安全要求较高的环境可以在端到端配置后使用 Kerberos 安全模式。

服务器通常通过 root squash 将远程 root 映射为非特权身份。不要仅仅为解决权限错误就禁用该保护；应检查 ID、目录所有权、导出策略和预期安全模型。

:::single-choice{#nfs-name-versus-id} 为什么显示名称相同的两个用户可能获得不同的 NFS 权限？

::option[NFS 权限可能取决于数字身份映射。]{#nfs-numeric-mapping .correct explanation="仅名称一致不能证明客户端与服务器解析出相同 UID 和组。"}
::option[NFS 会忽略所有文件系统权限。]{#nfs-ignores-permissions explanation="文件系统和导出权限仍是授权的一部分。"}
::option[每次挂载都会自动更改服务器账户数据库。]{#nfs-changes-accounts explanation="客户端挂载不会重写服务器身份。"}
:::

## 自动化网络挂载

当网络或服务器不可用时，普通的启动时 `/etc/fstab` 挂载可能延迟启动。根据主机情况，可使用 `autofs` 进行按需映射，或在测试确切语义后使用 `_netdev,nofail,x-systemd.automount` 等 systemd 挂载选项：

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

编辑 fstab 前，应保留恢复访问，并使用非破坏性解析器或受控挂载测试进行验证。自动挂载可以改善可用性行为，但不能修复授权、DNS 或服务器中断。

:::single-choice{#nfs-automount-benefit} 按需自动挂载 NFS 共享的主要好处是什么？

::option[它授予每个客户端对导出的 root 访问。]{#nfs-automount-root explanation="挂载时机不会覆盖服务器授权。"}
::option[它可以避免要求服务器在初始启动期间可用。]{#nfs-automount-boot .correct explanation="连接会在访问时触发，而不必阻塞早期启动。"}
::option[它将完整服务器文件系统复制到本地磁盘。]{#nfs-automount-copy explanation="挂载呈现远程访问，不是完整本地副本。"}
:::

## 卸载与验证

卸载前，应停止或协调使用共享的进程，并刷新应用程序工作。然后卸载挂载点，并确认它已消失：

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

强制或懒卸载可能隐藏活动引用并造成应用程序错误；只应在已诊断故障且有明确恢复计划时使用这些选项。

:::single-choice{#nfs-safe-unmount} 正常卸载 NFS 前应该做什么？

::option[协调使用共享的进程，并完成重要写入。]{#nfs-coordinate-writers .correct explanation="从应用程序中移除活动文件系统可能中断 I/O 或留下未完成工作。"}
::option[删除服务器上的导出目录。]{#nfs-delete-export explanation="客户端卸载不需要破坏服务器数据。"}
::option[禁用所有客户端网络接口。]{#nfs-disable-network explanation="这会让有序完成更困难，并非正常顺序。"}
:::

## 总结

现在，你可以在明确身份和可用性假设的情况下操作 NFS 客户端挂载。

1. 确认客户端工具、导出路径、协议和网络策略。
2. 挂载到专用路径，并验证实际来源和选项。
3. 通过身份和导出策略诊断权限。
4. 启动可用性重要时使用经过测试的按需挂载。
5. 协调用户、正常卸载并验证移除。
