---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "zh"
order_index: 6
title: "构建产物"
description: "把 CI 生成的文件与生成它的工作流运行记录和源代码版本关联起来。"
meta_title: "构建产物 - 持续集成"
meta_description: "打包网站文件，检查归档内容，并通过运行记录找到生成产物的源代码版本。"
meta_keywords: "构建产物, CI 产物, tar 归档, 持续集成, DevOps, Linux Journey"
---

**构建产物**是一次运行中保存下来供后续使用的一个或多个文件，例如测试报告或网站归档。把运行记录和修订版本与产物一并保存，审查者就能找出是哪个版本的源文件生成了它。

## 打包输出目录

继续使用练习目录，其中的 `dist` 应包含构建后的网页。这个示例会生成压缩归档，用一个文件保存目录中的内容。如果当前目录已有同名归档，会被覆盖。

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

第一条命令中，`-c` 创建归档，`-z` 启用压缩，`-f` 指定输出文件名。`-C dist .` 让 tar 先进入 `dist`，再打包当前目录。第二条命令用 `-t` 列出归档内容。提供这个归档之前，先确认列表中有 `./index.html`。

:::single-choice{#ci-build-artifacts-inspect-archive} 怎么检查归档里是否包含网页？

::option[用 tar -tzf site.tar.gz 列出归档内容。]{#ci-build-artifacts-inspect-archive-b .correct explanation="列表会显示归档中有没有 index.html。"}
::option[再创建一次归档。]{#ci-build-artifacts-inspect-archive-a explanation="重复构建不会列出归档中的项目。"}
::option[只看归档的名称。]{#ci-build-artifacts-inspect-archive-c explanation="归档名无法说明里面有什么。"}
:::

![tar 归档列表显示 site.tar.gz 中包含 index.html](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## 将产物关联到一次运行

工作流可以上传完成的归档。运行详情页会显示构建所用的修订版本。即使两个产物都叫 `site.tar.gz`，只要来自不同版本，内容就可能不同。选择下载哪个文件时，要同时核对运行记录和修订版本。

:::single-choice{#ci-build-artifacts-choose-run} 第 41 次和第 42 次运行都生成了 site.tar.gz。如何选出你审查过的那个版本的包？

::option[下载遇到的第一个 site.tar.gz。]{#ci-build-artifacts-choose-run-b explanation="名称无法说明文件来自哪个源代码版本。"}
::option[不管版本，选最近一次成功的运行。]{#ci-build-artifacts-choose-run-c explanation="之后的成功运行可能使用不同的源文件。要匹配你想用的修订版本。"}
::option[选择记录的修订版本与审查对象一致的那次运行。]{#ci-build-artifacts-choose-run-a .correct explanation="多次运行可以使用相同的文件名。"}
:::

## 区分归档和容器镜像

网站归档保存的是可以解包的文件。容器镜像则包含已经打包的文件系统，以及 Docker 用来启动容器的设置。工作流可以把镜像发布到镜像仓库。如果之后要运行的是这个镜像，就要同时记录镜像引用和源代码版本。

:::single-choice{#ci-build-artifacts-deployable-type} 下一个环节要从镜像仓库启动容器。它应该使用哪项输出？

::option[从运行结果中下载的测试报告。]{#ci-build-artifacts-deployable-type-a explanation="报告描述测试结果，不包含容器文件系统。"}
::option[发布到仓库的容器镜像引用。]{#ci-build-artifacts-deployable-type-c .correct explanation="Docker 能根据这个引用取得准备好的镜像。"}
::option[网站归档的文件名。]{#ci-build-artifacts-deployable-type-b explanation="里面保存的是网页文件，无法指向仓库中的镜像。"}
:::

## 总结

现在，你可以识别构建产物，并追溯它来自哪里。

1. 打包并检查构建生成的文件。
2. 核对生成产物的运行记录和修订版本。
3. 根据下一步的需求选择文件产物或容器镜像。
