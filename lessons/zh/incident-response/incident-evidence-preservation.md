---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "zh"
order_index: 2
title: "证据保全"
description: "学习怎样保存练习记录、副本和校验值，供之后核查。"
meta_title: "证据保全 - 事件响应"
meta_description: "记录证据来源和采集范围，核验副本是否一致，并为审查准备脱敏片段。"
meta_keywords: "证据保全, 日志证据, SHA-256, 校验值, 事件响应, Linux Journey"
---

响应事件时，一段日志有助于解释发生了什么。应当保留原始资料或经批准的导出文件，同时记下另一位审查者理解这些资料所需的信息。

## 记录采集上下文

记下主机、数据来源、时区和时间范围。注明由谁采集记录，以及用了什么筛选条件。一行脱离上下文的副本，可能和另一台机器上的一行记录完全相同。

:::single-choice{#incident-evidence-preservation-context-fields} 同事收到一行只带 09:22 时间的记录，缺少其他背景。你应该补充什么？

::option[副本在本地保存的路径。]{#incident-evidence-preservation-context-fields-b explanation="这个路径可以帮助找到副本，却无法说明它原先来自哪里，或者时间该怎样理解。"}
::option[猜测一个可能的原因。]{#incident-evidence-preservation-context-fields-c explanation="采集信息和对事件的解释应该分别记录。"}
::option[来源主机、时区和采集时段。]{#incident-evidence-preservation-context-fields-a .correct explanation="这些信息能帮助审查者把该记录放到正确的时间线上。"}
:::

## 核对副本

在新的练习目录里，保存一条无害的示例记录、复制它，再分别计算两个文件的 SHA-256 值。只使用示例文件。写入操作会覆盖该目录中的同名文件。

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

第一列显示内容哈希。两个值应当相同。这可以核对检查时副本的字节是否与原文件一致，但无法证明原始事件所记录的信息准确。

:::single-choice{#incident-evidence-preservation-copy-meaning} 哈希相同支持什么结论？

::option[源记录中的时间戳一定真实。]{#incident-evidence-preservation-copy-meaning-a explanation="哈希校验的是文件内容，无法验证时钟。"}
::option[审查副本与示例文件在检查时的字节一致。]{#incident-evidence-preservation-copy-meaning-b .correct explanation="两个哈希使用同一种算法计算得出。"}
::option[副本已获准公开分享。]{#incident-evidence-preservation-copy-meaning-c explanation="是否获准取决于谁可以查看文件，与哈希无关。"}
:::

![LabEx 记录的校验输出显示练习文件与审查副本的哈希相同](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## 准备可以安全查看的副本

保持原始记录完整并限制访问。如果另一团队只需要几个字段，就另做一个片段，再从这一片段移除敏感信息。记录这是范围已缩减的副本，并保留指向受保护原件的引用。

:::single-choice{#incident-evidence-preservation-redact-copy} 分享之前，应该对哪份材料脱敏？

::option[单独准备的审查片段。]{#incident-evidence-preservation-redact-copy-c .correct explanation="这样既能保留原件，也能缩小共享范围。"}
::option[受保护的原件，这样所有副本也一起变化。]{#incident-evidence-preservation-redact-copy-a explanation="这样会改动你想保留的证据。"}
::option[哈希校验文字，让变更后的文件看起来没有变化。]{#incident-evidence-preservation-redact-copy-b explanation="应保留实际测得的值及其对应的文件。"}
:::

## 总结

现在，你可以准备其他审查者能够理解的证据。

1. 记录资料从哪里、在什么时候采集。
2. 检查副本的字节是否与来源一致。
3. 分享时单独准备脱敏片段。
