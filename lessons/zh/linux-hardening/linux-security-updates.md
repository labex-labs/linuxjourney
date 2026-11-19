---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "zh"
order_index: 7
title: "安全更新"
description: "学习查看可用的软件包更新，并在获准的维护之后验证服务。"
meta_title: "安全更新 - Linux 安全加固"
meta_description: "辨别可用更新、已安装版本和实际运行的版本，并验证用户能正常使用服务。"
meta_keywords: "安全更新, APT 更新, 版本核验, Linux 安全加固, Linux Journey"
---

安全更新可以修复已安装软件中的缺陷。先确认目前安装的是哪个版本，你的操作系统又提供了什么修复。安排变更时，要考虑人们正在使用的服务。

## 查看可用更新

下面这条只读命令会在 Ubuntu 练习主机上列出 APT 已知可升级的软件包。它使用的是主机上已经保存的软件包信息。

```bash
$ apt list --upgradable
```

软件包出现在列表里，表示现有信息中有更新的候选版本。查看发行版的安全公告，确认其中是否包含你需要的修复。列表为空也可能是因为本地软件包信息过期了。

:::single-choice{#linux-security-updates-candidate-is-listed} 某个软件包出现在列表中。你能得出什么结论？

::option[更新已经安装。]{#linux-security-updates-candidate-is-listed-a explanation="列表显示的是可用的升级候选版本。"}
::option[APT 知道已安装的软件包有更新的候选版本。]{#linux-security-updates-candidate-is-listed-b .correct explanation="这是本地软件包信息当前报告的内容。"}
::option[所有更新的候选版本都是安全更新。]{#linux-security-updates-candidate-is-listed-c explanation="需要查发行版公告，确认发布该更新的原因。"}
:::

## 规划维护

获准的变更应写明涉及的服务、目标版本和维护窗口。有些更新要重启服务或重启主机才会生效。更改主机之前，应先准备测试请求和恢复办法。

:::single-choice{#linux-security-updates-reboot-check} 软件包更新修复了一个长期运行的服务所用的代码。安装后应该检查什么？

::option[服务是否需要重启才能使用更新后的代码。]{#linux-security-updates-reboot-check-a .correct explanation="正在运行的进程可能仍加载着旧代码。"}
::option[安装之前，更新是否出现在可用软件包列表中。]{#linux-security-updates-reboot-check-b explanation="可用性信息有助于制定维护计划，但不能说明进程加载的是哪个版本。"}
::option[软件包列表里现在是否已没有其他升级项。]{#linux-security-updates-reboot-check-c explanation="即使软件包已经是最新版，进程也可能还没有重新加载更新后的代码。"}
:::

## 验证维护结果

确认已安装版本符合获准的目标。从用户实际使用的路径检查服务，并记录结果。如果修复涉及正在运行的组件，还要确认更新后的版本确实已经生效。

:::single-choice{#linux-security-updates-security-verification} 完成服务更新后，哪两项结果最能说明维护已经完成？

::option[列表命令运行了两次。]{#linux-security-updates-security-verification-a explanation="重复列出软件包无法说明服务是否正常。"}
::option[维护工单改了标题。]{#linux-security-updates-security-verification-b explanation="标题不会提供服务运行方面的证据。"}
::option[获准的版本正在使用，一次有代表性的请求也成功了。]{#linux-security-updates-security-verification-c .correct explanation="这样既验证了软件状态，也验证了用户依赖的服务。"}
:::

## 区分两个版本信号

已安装的软件包与实际处理请求的程序，可能暂时处于不同版本。例如，软件包清单显示已安装修复后的版本，而更新之前启动的进程仍在运行。还需要查看实际运行的进程，才能完成核验。

:::single-choice{#linux-security-updates-final-application} 已安装的版本包含修复，但旧进程仍在运行。还有什么需要确认？

::option[是否要替换机器上的其他所有进程。]{#linux-security-updates-final-application-c explanation="需要核查的是这项更新涉及的服务及获准的维护要求。"}
::option[是否已由更新后的程序接收请求。]{#linux-security-updates-final-application-a .correct explanation="清单只能核对磁盘上的已安装文件，进程检查才能验证实际运行的服务。"}
::option[是否曾有可用的更新包。]{#linux-security-updates-final-application-b explanation="已安装的软件包已经显示了修复后的版本。"}
:::

## 总结

现在，你可以从发现候选版本开始，一直跟进到更新结果的验证。

1. 区分可用更新与已安装的变更。
2. 制定计划时考虑重启和恢复。
3. 验证运行版本和预期的服务行为。
