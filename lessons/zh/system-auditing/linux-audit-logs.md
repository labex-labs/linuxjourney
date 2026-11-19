---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "zh"
order_index: 2
title: "Linux 审计日志"
description: "学习如何把描述同一次操作的多条 Linux 审计记录归在一起。"
meta_title: "Linux 审计日志 - 系统审计"
meta_description: "用主机和审计事件标识配对记录，区分登录身份和有效身份，再判断还需要查什么。"
meta_keywords: "Linux 审计日志, Linux Audit, 审计事件, auid, euid, 系统审计, Linux Journey"
---

Linux Audit 可能为同一个事件写入多条记录。一行可能描述操作，另一行则补充文件路径。先把相关记录归在一起，再判断它们能说明什么。

## 读取同一审计事件

下面是来自同一台主机、同一天的简化练习记录。审计事件标识中，冒号后的数字是事件编号。结合时间戳和事件编号，可以把相关记录归组。下面两行属于同一个事件。

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

第一行给出操作结果和账户字段。路径记录给出一个与该事件相关的文件。

:::single-choice{#linux-audit-logs-group-rows} 在这个例子中，哪些信息能把操作和路径关联起来？

::option[只看 SYSCALL 和 PATH 两种记录类型。]{#linux-audit-logs-group-rows-a explanation="类型说明各行的作用。多个不同事件可以包含同样的类型。"}
::option[两行都以 type 开头这一点。]{#linux-audit-logs-group-rows-c explanation="不同事件的记录也可以都有 type 字段。"}
::option[同一台主机上相同的审计事件标识。]{#linux-audit-logs-group-rows-b .correct explanation="这个标识把描述 42 号事件的记录归在一起。"}
:::

![模拟的 Linux Audit SYSCALL 和 PATH 记录有相同的审计事件标识](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## 区分两种身份

在本例中，`auid` 是审计登录用户 ID，`euid` 是执行操作时的有效用户 ID。程序使用的有效身份可以与登录身份不同。数字 ID 用于识别主机上的账户。要确定背后是哪一个人，可能还需要其他记录。

:::single-choice{#linux-audit-logs-identify-login} 哪个字段显示示例中的审计登录身份？

::option[euid 0。]{#linux-audit-logs-identify-login-b explanation="它显示程序在这个事件中使用的有效身份。"}
::option[auid 1001。]{#linux-audit-logs-identify-login-a .correct explanation="auid 是审计登录用户 ID，euid 则是有效身份。"}
::option[事件编号 42。]{#linux-audit-logs-identify-login-c explanation="该编号用来给记录归组，与账户身份无关。"}
:::

## 把结论限定在证据范围内

结果字段表示记录到的操作成功了。要确定是什么操作，请检查完整的事件。要确认文件内容有没有变，就把文件与已知的参考版本比较。

:::single-choice{#linux-audit-logs-useful-follow-up} 什么能帮助判断内容是否与获准的文件不同？

::option[与获准的参考副本或完整性记录进行比较。]{#linux-audit-logs-useful-follow-up-c .correct explanation="这类证据能说明文件本身发生了哪些变化。"}
::option[再找一条报告另一项操作成功的审计记录。]{#linux-audit-logs-useful-follow-up-a explanation="那可以确认另一次操作有记录，但无法比较当前文件与获准副本的字节。"}
::option[同一事件中的登录账户 ID。]{#linux-audit-logs-useful-follow-up-b explanation="登录 ID 能提供账户背景，无法描述文件字节的变化。"}
:::

## 总结

现在，你可以通过一组相关记录解读一次审计事件。

1. 结合主机和审计事件标识来匹配记录。
2. 分别读取登录身份和有效身份。
3. 操作结果留下疑问时，选择适当的后续检查。
