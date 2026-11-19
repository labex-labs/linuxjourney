---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "zh"
order_index: 3
title: "文件完整性"
description: "学习用哈希和元数据比较文件的内容与访问权限。"
meta_title: "文件完整性 - 系统审计"
meta_description: "用 SHA-256 记录文件内容的哈希，用 stat 检查权限，并分别验证两项属性的变化。"
meta_keywords: "文件完整性, SHA-256, stat, 文件哈希, 权限模式, 系统审计, Linux Journey"
---

完整性检查要回答的是文件是否仍符合参考状态。内容和元数据应该分开检查。内容是文件内部的字节。**元数据**则包括访问权限等详细信息。

## 记录内容哈希

在空的练习目录下创建一个小型配置文件。重定向会覆盖同名文件，所以请使用新的目录。

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

第一个字段是**哈希**，即用文件字节计算出的固定长度的值。之后用同样的方法检查同一个文件。哈希变了，就说明参与计算的字节不同。

:::single-choice{#host-file-integrity-changed-hash} 文件编辑后，SHA-256 值发生了变化。这说明什么？

::option[文件内容与之前测量的字节不同。]{#host-file-integrity-changed-hash-a .correct explanation="输入不同的内容，会改变算出的哈希。"}
::option[这次编辑一定未经授权。]{#host-file-integrity-changed-hash-b explanation="是否获得批准是另一个问题。"}
::option[某个账户的访问权限一定发生了变化。]{#host-file-integrity-changed-hash-c explanation="内容哈希不会记录权限。"}
:::

## 记录文件权限

在 Linux 上，`stat -c` 可以打印指定的元数据。`%a` 输出数字形式的权限，`%n` 输出文件名。

```bash
$ stat -c '%a %n' site.conf
```

初始权限取决于文件的创建方式。把权限和内容哈希一起记下来，之后就能比较这两项属性。

:::single-choice{#host-file-integrity-mode-vs-content} 哈希与参考值相同，但 stat 报告的权限模式不同。根据这些检查，哪项属性发生了变化？

::option[文件字节变了，权限模式相同。]{#host-file-integrity-mode-vs-content-a explanation="哈希相同，权限模式不同。"}
::option[文件一定被删除了。]{#host-file-integrity-mode-vs-content-c explanation="这两项检查都返回了文件的信息。"}
::option[权限变了，观察到的内容哈希仍然相同。]{#host-file-integrity-mode-vs-content-b .correct explanation="这两种工具检查的是不同的属性。"}
:::

## 测试权限变化

下一条命令会把这个练习文件的权限改成 `640`，允许所有者读写、所属组读取。再次运行前面两项检查，然后比较结果。

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

权限应显示为 640，内容哈希应与首次测量一致。

:::single-choice{#host-file-integrity-repeat-check} 如果以后修改了文件内的 mode=preview，哪项检查能发现它？

::option[只查看 stat 给出的文件名。]{#host-file-integrity-repeat-check-a explanation="编辑内容后，名称可以保持不变。"}
::option[重新计算 SHA-256，与原始哈希比较。]{#host-file-integrity-repeat-check-c .correct explanation="内容发生变化时，会得到不同的哈希。"}
::option[只看所有者对应的权限数字。]{#host-file-integrity-repeat-check-b explanation="权限与大多数内容修改是两回事。"}
:::

![LabEx 记录的输出显示权限改为 640，内容哈希保持不变](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## 总结

现在，你可以分别比较文件内容和访问权限。

1. 记录 SHA-256 内容哈希。
2. 用 stat 读取权限模式。
3. 检查一次权限改动的结果。
