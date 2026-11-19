---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "zh"
order_index: 2
title: "服务账户"
description: "学习查出 Linux 进程以哪个账户运行，并判断它需要哪些访问权限。"
meta_title: "服务账户 - Linux 安全加固"
meta_description: "从 ps 输出识别进程的运行身份，并为服务账户选择符合职责的权限。"
meta_keywords: "服务账户, Linux 进程, ps, 最小权限, Linux 安全加固, Linux Journey"
---

Web 服务器启动后会成为一个进程。Linux 为每个进程关联一个身份，以此判断程序可以读取或修改什么。**服务账户**是为程序单独设立的运行身份。

## 查看进程身份

在普通终端中，`$$` 表示当前 shell 的进程 ID。利用它，可以查看当前 shell 的运行身份。`-p` 选中这个进程，`-o` 指定要显示的列。字段后的等号表示不显示列标题。

```bash
$ ps -p "$$" -o user=,comm=
```

LabEx 终端里的账户可能是 `labex`。命令列会显示 shell 程序名。查看服务进程时，相应字段会显示该服务实际使用的账户，与是谁启动它无关。

:::single-choice{#linux-service-accounts-process-user} 哪个字段告诉你选中的进程与哪个账户关联？

::option[通过 -p 传入的进程 ID。]{#linux-service-accounts-process-user-a explanation="进程 ID 用来选中一个正在运行的进程。"}
::option[最后一列的命令名。]{#linux-service-accounts-process-user-c explanation="这一列给出正在运行的程序名。"}
::option[ps 输出的 user 字段。]{#linux-service-accounts-process-user-b .correct explanation="user 字段显示进程的运行身份。"}
:::

![ps 输出显示 LabEx 的 shell 进程和 labex 账户](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## 选择专用的运行身份

假设某个 Web 服务只需要读取网页和写入自己的日志。可以把这些权限授予专用账户 `site-web`。如果改用管理员的宽泛权限运行，程序就可以修改主机上许多它根本不需要动的内容。

:::single-choice{#linux-service-accounts-isolate-service} 哪套权限符合这个服务的职责？

::option[允许 site-web 编辑所有用户的文件。]{#linux-service-accounts-isolate-service-b explanation="该服务没有需要这种访问范围的任务。"}
::option[允许 site-web 读取网页并写入自己的日志。]{#linux-service-accounts-isolate-service-a .correct explanation="这两项权限正好对应服务的两项工作。"}
::option[允许 site-web 对每个请求都以管理员身份运行。]{#linux-service-accounts-isolate-service-c explanation="大部分请求只需要服务本身的有限权限。"}
:::

## 检查使用多个进程的服务

有些服务用不同进程承担不同职责。要判断处理请求时使用哪些权限，先检查真正处理请求的进程。如果要更改运行身份，请确认服务仍能读取所需的输入，并且只向必要的地方写入数据。

:::single-choice{#linux-service-accounts-verify-identity} 维护工具显示监督进程使用 root。怎样才能确定哪个账户负责处理 Web 请求？

::option[查看负责处理请求的工作进程的身份。]{#linux-service-accounts-verify-identity-c .correct explanation="检查真正执行这项工作的进程，才能把账户和实际操作对应起来。"}
::option[只看服务配置文件的文件名。]{#linux-service-accounts-verify-identity-a explanation="文件名无法说明工作进程以哪个身份运行。"}
::option[查看打开终端的人是谁。]{#linux-service-accounts-verify-identity-b explanation="终端用户和正在运行的服务可能使用不同的账户。"}
:::

## 总结

现在，你可以查到 Linux 进程实际使用的运行身份。

1. 从 ps 的输出中找出进程用户。
2. 根据服务职责选择合适的权限。
3. 在多进程服务中检查实际执行任务的进程。
