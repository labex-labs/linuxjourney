---
index: 4
lang: "zh"
title: "/etc/shadow"
meta_title: "/etc/shadow - 用户管理"
meta_description: "了解 Linux 中的 /etc/shadow 文件、其字段以及它如何保护用户密码。帮助初学者理解 Linux 认证。"
meta_keywords: "/etc/shadow, Linux 安全，用户认证，密码管理，Linux 教程，初学者指南"
---

## Lesson Content

`/etc/shadow` 文件用于存储用户认证信息。它需要超级用户读取权限。

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

你会注意到它看起来与 `/etc/passwd` 的内容非常相似；然而，在密码字段中，你会看到一个加密的密码。字段之间用冒号分隔，如下所示：

1. 用户名
2. 加密密码
3. 上次密码更改日期 - 表示自 1970 年 1 月 1 日以来的天数。如果为 0，则表示用户下次登录时应更改密码。
4. 最小密码有效期 - 用户在再次更改密码之前必须等待的天数。
5. 最大密码有效期 - 用户必须更改密码前的最大天数。
6. 密码警告期 - 密码即将过期前的天数。
7. 密码不活动期 - 密码过期后允许使用其密码登录的天数。
8. 账户过期日期 - 用户将无法登录的日期。
9. 保留字段以备将来使用。

在今天的大多数发行版中，用户认证不仅仅依赖于 `/etc/shadow` 文件；还有其他机制，例如 PAM (Pluggable Authentication Modules)，它们取代了认证。

## Exercise

查看 `/etc/shadow` 文件。

## Quiz Question

No questions, move along!

## Quiz Answer
