---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "zh"
order_index: 4
title: "构建与测试"
description: "在本地练习检查一个小网页，区分准备、构建和测试三个环节。"
meta_title: "构建与测试 - 持续集成"
meta_description: "准备网页文件，生成构建输出，再从检查命令的退出码判断结果。"
meta_keywords: "CI 构建, 测试, grep, 退出码, 持续集成, DevOps, Linux Journey"
---

一次检查失败时，如果每个环节只负责一件事，就更容易查出问题。**准备**提供输入和工具，**构建**生成输出，**测试**则核对源文件或输出是否符合预期。

## 准备输入文件

在空的练习目录中写一个示例网页。重定向会覆盖已有的 `index.html`，因此请使用新的练习目录。

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

在 CI 作业中，checkout 步骤会提供这个网页。有些项目还需要安装依赖，也就是构建或测试所需的库和工具。

:::single-choice{#ci-builds-and-tests-prepare-input} 复制命令尚未执行，网页文件就已经找不到了。应该先检查哪个环节？

::option[后续作业中下载产物的环节。]{#ci-builds-and-tests-prepare-input-a explanation="构建输出之前就要有这个输入文件。"}
::option[准备环节。]{#ci-builds-and-tests-prepare-input-b .correct explanation="要先把输入文件准备到当前作业可访问的位置。"}
::option[生产环境的响应时间。]{#ci-builds-and-tests-prepare-input-c explanation="这个问题涉及运行器里的文件。"}
:::

## 构建输出

把网页复制到存放成品网站的目录中。

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

即使目录已经存在，`-p` 也能让 `mkdir` 成功。复制会在输出目录中生成一个独立文件，后续测试可以检查它。

:::single-choice{#ci-builds-and-tests-build-product} 复制成功后，哪个文件已经可以打包？

::option[dist/index.html。]{#ci-builds-and-tests-build-product-a .correct explanation="构建把网页的副本放入了输出目录。"}
::option[公开网站上已部署的网页。]{#ci-builds-and-tests-build-product-b explanation="在本地复制文件不会启动服务。"}
::option[工作流状态记录。]{#ci-builds-and-tests-build-product-c explanation="这里的构建产物是网页。检查状态由运行器另行记录。"}
:::

## 测试网页

构建后立即执行下面的检查。`-F` 按字面文本匹配，`-q` 不打印匹配结果。shell 将上一条命令的退出码保存在 `$?` 中。0 表示找到了文本，1 表示没有匹配的行。

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

预期结果是 `0`。这个测试只检查构建后的文件是否包含指定的文字，不涉及颜色、浏览器渲染或响应时间。

:::single-choice{#ci-builds-and-tests-test-scope} 测试通过，可以得出什么结论？

::option[可以从互联网访问网页。]{#ci-builds-and-tests-test-scope-a explanation="检查只读取了本地输出文件。"}
::option[网页能在每个受支持的浏览器中正确呈现。]{#ci-builds-and-tests-test-scope-b explanation="这次测试没有用到浏览器。"}
::option[构建后的文件中包含预期的标题文本。]{#ci-builds-and-tests-test-scope-c .correct explanation="这正是 grep 命令检查的条件。"}
:::

![LabEx 中的本地标题检查成功，shell 退出码为 0](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## 总结

现在，你可以判断小型 CI 检查中每个环节说明了什么。

1. 在构建前准备好输入。
2. 找出构建生成的文件。
3. 读懂退出码，并说清测试验证了哪些内容。
