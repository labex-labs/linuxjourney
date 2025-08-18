---
lang: "zh"
title: "/etc/group"
meta_description: "了解 Linux 中的 /etc/group 文件，理解组管理、GID 和用户权限。面向初学者的重要 Linux 组文件教程。"
meta_keywords: "/etc/group, Linux 组，组管理，GID, Linux 权限，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

另一个用于用户管理的文件是 `/etc/group` 文件。该文件允许不同的组拥有不同的权限。

```bash
$ cat /etc/group

root:*:0:pete
```

与 `/etc/passwd` 文件非常相似，`/etc/group` 文件的字段如下：

1. 组名
2. 组密码 - 不需要设置组密码；使用 `sudo` 等提升权限是标准做法。默认值将显示为星号 (`*`)。
3. 组 ID (GID)
4. 用户列表 - 您可以手动指定要添加到特定组的用户

## Exercise

运行命令 `groups`。你看到了什么？

## Quiz Question

root 的 GID 是多少？

## Quiz Answer

0
