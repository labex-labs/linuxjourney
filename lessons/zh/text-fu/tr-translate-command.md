---
lang: "zh"
title: "tr (转换)"
description: "学习如何使用 Linux 'tr' 命令来转换和删除字符。通过示例和练习理解字符转换。开始您的 Linux 之旅！"
keywords: "tr 命令，Linux tr, 转换字符，删除字符，Linux 教程，Linux 初学者，Linux 指南"
---

## Lesson Content

`tr` (translate) 命令允许您将一组字符转换为另一组字符。让我们尝试一个将所有小写字符转换为大写字符的示例。

```bash
$ tr a-z A-Z
hello
HELLO
```

如您所见，我们将 `a-z` 的范围转换为 `A-Z`，所有我们输入的小写文本都变成了大写。

## Exercise

尝试以下命令。会发生什么？

```bash
$ tr -d ello
hello
```

## Quiz Question

用于字符转换的命令是什么？

## Quiz Answer

tr
