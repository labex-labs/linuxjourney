---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "zh"
order_index: 5
title: "工作流日志"
description: "找到工作流中失败的步骤，读出第一条能指导排查的日志消息。"
meta_title: "工作流日志 - 持续集成"
meta_description: "按顺序查看步骤状态，根据首个错误定位问题，并在修复后核对新结果。"
meta_keywords: "工作流日志, GitHub Actions, CI 排查, 持续集成, DevOps, Linux Journey"
---

工作流结果会给出总体状态。要弄清失败原因，先展开失败的作业，再按顺序看各个步骤。如果前面的步骤没有成功完成，后面的步骤可能被跳过。

## 找到最早的失败

下面是一次模拟的运行，列出了网页检查作业中每个步骤的状态。

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

先看 `Build page`。跳过的检查没有给出网页结果。修复失败原因后，重新运行工作流，再核对后续步骤。

:::single-choice{#ci-workflow-logs-first-failure} 应该先查看哪个步骤的输出？

::option[Package site，因为它排在最后。]{#ci-workflow-logs-first-failure-a explanation="这次运行跳过了打包命令。"}
::option[Check heading，因为这是检查网页的工作流。]{#ci-workflow-logs-first-failure-c explanation="状态表明标题检查没有执行。"}
::option[Build page，因为它先失败，后面的步骤都没有运行。]{#ci-workflow-logs-first-failure-b .correct explanation="这个步骤的日志能解释之后的步骤为什么被跳过。"}
:::

![模拟的 CI 运行显示构建失败，后续步骤被跳过](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## 根据错误消息排查

失败步骤显示了下面几行。

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

错误消息写出了目标路径。如果父目录 `dist` 不存在，复制命令就无法在里面创建文件。查看复制之前是否有命令创建了该目录。退出码 1 表示命令失败，具体该查哪里则要看错误消息。

:::single-choice{#ci-workflow-logs-actionable-log} 已知 dist 不存在，哪项改动能解决报告的问题？

::option[修改 grep 要检查的标题。]{#ci-workflow-logs-actionable-log-b explanation="标题检查还没运行，无法说明文本是否写错。"}
::option[先创建 dist，再复制文件。]{#ci-workflow-logs-actionable-log-a .correct explanation="目标文件需要先有父目录。"}
::option[从被跳过的步骤下载产物。]{#ci-workflow-logs-actionable-log-c explanation="这里的打包步骤没有生成产物。"}
:::

## 检查重新运行的结果

修复构建问题后，检查新一次运行对应的修订版本及各步骤状态。复制成功说明输出文件已经生成。要确认整个流程通过，还要看测试和打包的结果。报告问题时，把第一条有助于排查的错误与对应的步骤名一起记录下来。

:::single-choice{#ci-workflow-logs-rerun-evidence} 新的运行结果显示 Build page 通过，Check heading 失败。现在有什么变化？

::option[构建成功，标题检查也有了可供排查的结果。]{#ci-workflow-logs-rerun-evidence-c .correct explanation="当前最早需要处理的失败已经移到了测试步骤。"}
::option[旧构建失败过，所以新的运行结果没用。]{#ci-workflow-logs-rerun-evidence-a explanation="每次运行的结果都针对它所用的修订版本。"}
::option[既然构建通过，打包也一定通过。]{#ci-workflow-logs-rerun-evidence-b explanation="后面的步骤仍可能失败或被跳过。"}
:::

## 总结

现在，你可以结合步骤顺序解读工作流失败。

1. 找出最早实际运行但没有成功的步骤。
2. 用日志内容确定要检查的地方。
3. 修复后检查新版本及后续步骤的结果。
