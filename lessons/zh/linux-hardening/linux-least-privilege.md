---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "zh"
order_index: 3
title: "最小权限"
description: "学习为服务所承担的具体任务选择文件权限和管理权限。"
meta_title: "最小权限 - Linux 安全加固"
meta_description: "根据任务选择刚好够用的访问权限，检查路径中的目录，并验证管理操作的边界。"
meta_keywords: "最小权限, 文件权限, 目录权限, sudo, Linux 安全加固, Linux Journey"
---

**最小权限**指的是只给账户完成工作需要的访问权限。先明确账户实际要做什么。一项任务可能需要读一个文件、写另一个文件，而完全不涉及管理操作。

## 让权限符合职责

Web 工作进程需要读取 `index.html`。更新这个文件的是部署账户。这两项工作可以使用不同的权限。工作进程可以读网页，部署账户可以写入网页。

:::single-choice{#linux-least-privilege-read-only-page} 在这个例子里，工作进程需要什么网页文件权限？

::option[读取权限。]{#linux-least-privilege-read-only-page-a .correct explanation="要提供网页，需要读取文件内容。"}
::option[写入权限。]{#linux-least-privilege-read-only-page-b explanation="修改网页是部署账户的工作。"}
::option[管理无关服务的权限。]{#linux-least-privilege-read-only-page-c explanation="这些工作不属于 Web 工作进程的任务。"}
:::

## 检查完整的访问路径

文件本身的权限只是检查的一部分。在 Linux 上，还需要有权限进入通往文件的每一级目录。对目录拥有执行权限时，只要知道所需文件或子目录的名称，程序就能沿这条路径访问。如果工作进程无法经过某一级目录，那么即使文件本身可以读取，它也无法访问。

:::single-choice{#linux-least-privilege-path-boundary} 按文件权限看，工作进程应该能读取 index.html，但它无法进入父目录。这时需要检查什么？

::option[页面文件是不是变大了。]{#linux-least-privilege-path-boundary-a explanation="文件大小不会授予目录访问权限。"}
::option[是否要让所有人都能写入网页。]{#linux-least-privilege-path-boundary-c explanation="写权限无法补上缺少的路径访问权限。"}
::option[工作进程是否有权穿过该目录。]{#linux-least-privilege-path-boundary-b .correct explanation="进程既要有权限访问文件，也要有权限经过通往文件的目录。"}
:::

## 限制特殊操作

`sudo` 这样的管理工具可以允许经过授权的用户执行特定维护操作。先明确允许哪项操作、谁可以执行，以及如何验证新的访问权限。确认获准的维护任务仍能完成，也要检查同一规则下的其他管理操作仍受限制。

:::single-choice{#linux-least-privilege-policy-test} 某个维护角色需要查看服务状态。哪个测试计划最能验证预期权限？

::option[检查所有管理命令现在是否都能成功。]{#linux-least-privilege-policy-test-a explanation="这些额外权限超出了任务范围。"}
::option[确认该角色能查看状态，同时仍无法执行无关的特权变更。]{#linux-least-privilege-policy-test-c .correct explanation="这样既能验证必要的访问，也能验证预期的限制。"}
::option[只检查用户名是否存在。]{#linux-least-privilege-policy-test-b explanation="账户存在并不代表它具备哪些权限。"}
:::

## 总结

现在，你可以判断一项任务所需的最小访问范围。

1. 区分读取、写入和管理操作。
2. 检查是否可以经过路径上的各级目录。
3. 分别验证角色获准的操作和受到限制的操作。
