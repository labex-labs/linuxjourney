---
lesson_id: "network-file-sharing"
course_id: "network-sharing"
lang: "zh"
order_index: 1
title: "文件共享概述"
description: "学习如何选择并安全执行基于 SSH 的 scp 文件传输。"
meta_title: "文件共享概述 - 网络共享"
meta_description: "通过免费在线课程探索 Linux 文件共享。学习 scp 等 Linux 命令，安全地通过网络传输文件，是 Linux 编程的重要资源。"
meta_keywords: "Linux 文件共享, scp 命令, 安全复制, 学习 Linux 命令, 免费 Linux 在线课程, Linux 编程, 网络文件传输, Linux 学习资源"
---

网络文件移动涵盖一次性复制、持续挂载的共享和同步目录树。选择方法时，应考虑方向、数据大小、更新频率、身份模型、网络信任、元数据要求，以及客户端是否需要实时共享访问。

## 选择传输方法

- `scp` 或 SFTP 提供经过 SSH 身份验证的复制或交互式传输。
- `rsync` 可以在本地或通过 SSH 等传输高效协调目录树。
- NFS 将服务器导出呈现为挂载文件系统，常用于类 Unix 主机之间。
- Linux 上由 Samba 实现的 SMB 支持多个操作系统共享访问。
- HTTP 可以提供简单下载，但不是通用的挂载文件系统。

复制并不自动等于备份。备份设计还需要独立保留、恢复测试、完整性检查，以及防止受到相同删除或入侵的保护。

:::single-choice{#file-sharing-one-time-ssh-copy}
哪个工具适合通过 SSH 一次性复制文件？

::option[`scp`]{#file-sharing-scp .correct explanation="SCP 使用 SSH 身份验证和传输来复制文件。"}
::option[`uptime`]{#file-sharing-uptime explanation="uptime 报告主机运行时间和负载，而不传输文件。"}
::option[`logrotate`]{#file-sharing-logrotate explanation="logrotate 管理主机上的文件日志版本。"}
:::

## 理解 scp 路径

一般形式为 `scp SOURCE DESTINATION`。远程操作数通常使用 `user@host:path`：

```bash
$ scp -- report.txt alice@example.net:/srv/incoming/
$ scp -- alice@example.net:/srv/outgoing/result.txt ./result.txt
```

第一条命令推送本地文件，第二条拉取远程文件。冒号用于分隔远程主机和路径。包含 shell 敏感字符的路径应加引号，并避免使用有歧义的不可信文件名。

:::single-choice{#file-sharing-scp-pull-source}
在 `scp` 拉取操作中，远程说明位于哪里？

::option[作为本地目标之前的源。]{#file-sharing-pull-source .correct explanation="复制方向遵循从源到目标的操作数顺序。"}
::option[作为所有选项之后的本地目标。]{#file-sharing-pull-destination explanation="要取回的远程对象是源操作数。"}
::option[只出现在用户的 SSH 配置文件中。]{#file-sharing-pull-config explanation="SSH 配置可以提供默认值，但要复制的远程路径仍是操作数。"}
:::

## 复制目录

对目录树使用递归模式：

```bash
$ scp -r -- project/ alice@example.net:/srv/incoming/
```

复制前，应检查数据大小、符号链接、权限、所有权要求、可用空间和目标命名。SCP 不是同步策略；反复复制目录可能在目标处留下源中已经不存在的文件。

:::single-choice{#file-sharing-scp-recursive}
`scp -r` 请求什么？

::option[复制前移除远程目标。]{#file-sharing-scp-remove explanation="递归模式遍历目录，不定义清理策略。"}
::option[递归复制目录树。]{#file-sharing-scp-tree .correct explanation="所选源是目录时需要该标志。"}
::option[以只读方式访问 SSH 配置。]{#file-sharing-scp-readonly explanation="该选项涉及目录遍历，而不是配置访问。"}
:::

## 验证身份与结果

SSH 主机密钥验证可以防止连接到错误服务器。主机密钥改变时，应通过可信渠道验证该事件，而不是绕过警告。应使用最小权限账户，并采用适合环境的密钥处理方式。

传输后，应验证退出状态、预期文件、大小和元数据；完整性要求较高时，还应在两端独立计算哈希。确认目标应用程序确实能够读取数据。

:::single-choice{#file-sharing-host-key-change}
SSH 报告主机密钥意外改变时应该怎么做？

::option[为以后每次传输禁用主机密钥检查。]{#file-sharing-disable-checking explanation="这会移除一项重要的服务器身份控制。"}
::option[继续前通过可信来源验证新密钥。]{#file-sharing-verify-key .correct explanation="该警告可能表示主机重建、目标错误或遭到拦截，应进行调查。"}
::option[在命令输出中发布私有身份验证密钥。]{#file-sharing-publish-key explanation="私有凭据绝不能暴露。"}
:::

## 总结

现在，你可以选择并验证安全的一次性网络文件复制。

1. 根据访问和保留需求匹配共享方法。
2. 按源和目标理解本地与远程 `scp` 操作数。
3. 有意使用递归模式复制目录树。
4. 验证服务器身份、传输结果和目标可用性。
