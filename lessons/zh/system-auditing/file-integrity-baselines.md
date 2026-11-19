---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "zh"
order_index: 4
title: "完整性基线"
description: "学习解读完整性报告，并判断何时可以批准更新基线。"
meta_title: "完整性基线 - 系统审计"
meta_description: "区分内容、权限和路径是否存在，核实参考状态，再处理报告中的意外差异。"
meta_keywords: "完整性基线, 文件完整性, 差异报告, 系统审计, 网络安全, Linux Journey"
---

**基线**是一份可信记录，描述某个已知时间点文件应有的属性。之后进行完整性检查时，可以把当前文件与基线比较，再报告差异。

## 读懂差异报告

下面的模拟片段将主机当前状态与上一次获准的状态进行比较。

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

第一行显示文件字节变了。第二行显示权限变了。第三行表示检查时找不到之前跟踪的文件。

:::single-choice{#file-integrity-baselines-report-mode} 哪一行显示访问权限发生了变化？

::option[site.conf 那一行。]{#file-integrity-baselines-report-mode-a explanation="这一行报告的是内容哈希的变化。"}
::option[banner.txt 那一行。]{#file-integrity-baselines-report-mode-b .correct explanation="权限模式从 644 变成了 640。"}
::option[site.prev 那一行。]{#file-integrity-baselines-report-mode-c explanation="这一行记录的是路径是否存在。"}
:::

![模拟完整性报告对比文件内容、访问权限以及路径是否存在](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## 核查参考状态

报告要有价值，作为参照的早期状态就必须可信。保留基线的标识和创建日期。如果用于比较的旧文件在保存时就有问题，结果可能误导你。核实这份基线代表的是哪个获准状态。

:::single-choice{#file-integrity-baselines-reference-source} 哪份基线最适合核查今天的配置？

::option[变更前已记录且获得批准的副本。]{#file-integrity-baselines-reference-source-a .correct explanation="它提供了已知的参考，核查者可以验证。"}
::option[用今天来源尚未查明的文件生成的基线。]{#file-integrity-baselines-reference-source-b explanation="这样会在调查之前就把差异当成正常状态接受。"}
::option[另一台无关主机的设置，且没有可比的上下文。]{#file-integrity-baselines-reference-source-c explanation="不同主机可能承担不同角色，预期的文件和权限也不同。"}
:::

## 更新之前先核查差异

把每项差异与获准的变更对照，并验证服务结果。如果计划修改横幅文件的权限，却没有计划修改配置文件，就应分别核查。等差异核实并获授权后，再更新参考状态。同时保留旧基线的记录。

:::single-choice{#file-integrity-baselines-update-timing} 横幅权限变化已经批准，site.conf 的变化还无法解释。接受新基线前，应该做什么？

::option[既然其中一行符合预期，就批准全部变化。]{#file-integrity-baselines-update-timing-a explanation="这些文件差异分别对应不同的变更。"}
::option[丢弃差异报告。]{#file-integrity-baselines-update-timing-b explanation="报告记录了还需要核实的项目。"}
::option[调查 site.conf 中原因不明的改动。]{#file-integrity-baselines-update-timing-c .correct explanation="确认当前状态之后，才能接受新的基线。"}
:::

想在练习环境中创建并比较完整性基线，可以试试 [文件完整性监测](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122)。

## 总结

现在，你可以把基线用于一次具体的比较。

1. 区分报告中的内容、权限模式及路径是否存在。
2. 确认参考数据代表可信状态。
3. 接受新的参考状态前，先核查意外差异。
