---
lesson_id: "kernel-privilege-levels"
course_id: "kernel"
lang: "zh"
order_index: 2
title: "特权级别"
description: "学习处理器特权机制如何将用户执行与可信的内核执行分隔开。"
meta_title: "特权级别 - 内核"
meta_description: "探索 Linux 特权级别的核心概念。本课介绍内核模式与用户模式的区别、保护环的作用，以及系统调用如何提供对硬件的特权访问，帮助你理解内核如何管理安全和内核特权。"
meta_keywords: "Linux 特权级别, 内核模式, 用户模式, 保护环, 系统调用, 特权访问, 内核特权, 内核模式与用户模式的区别, Linux 安全"
---

处理器提供特权模式，用来限制敏感指令和内存访问。Linux 利用这一硬件边界，使普通应用程序的故障无法直接覆盖内核内存或重新配置设备。进入特权执行的转换由内核控制。

## 用户模式

普通进程在自己的虚拟地址空间内以用户模式执行。它可以自由计算，并访问内核授予的内存映射，而这些映射可能很大；用户模式并不意味着“只能使用少量内存”。它不能直接访问任意物理内存、其他进程的私有映射或处理器的特权控制功能。

页表和保护位负责实施内存访问控制。如果线程引用无效或不允许访问的地址，处理器会陷入内核；内核可以解决有效的缺页异常，也可以发送 `SIGSEGV` 等信号。

:::single-choice{#kernel-privilege-user-mode-memory}
用户模式进程通常可以直接访问哪些内存？

::option[每个物理 RAM 地址和全部内核内存。]{#kernel-privilege-all-physical explanation="特权机制和虚拟内存保护会阻止这些访问。"}
::option[只能访问进程启动时选定的一个固定字节。]{#kernel-privilege-one-byte explanation="非特权进程仍然可以拥有许多映射区域。"}
::option[它自己的虚拟地址空间中允许访问的映射。]{#kernel-privilege-own-mappings .correct explanation="硬件页保护会将进程限制在以适当权限建立的映射内。"}
:::

## 内核模式

内核模式允许执行特权指令，并访问内存管理、调度、中断处理和驱动程序所需的受保护内核映射。在 x86 上，Linux 的这种划分通常表述为内核使用 ring 0，用户进程使用 ring 3。Linux 通常不使用 ring 1 和 ring 2 来隔离普通进程。

其他架构使用不同的名称和机制，例如异常级别。虚拟化还会引入无法用简单双环图表示的虚拟机监控程序与客户机关系。核心思想是受控特权，而不是 x86 环编号本身。

:::single-choice{#kernel-privilege-x86-kernel-ring}
Linux 内核通常在哪个 x86 保护环中执行？

::option[Ring 3。]{#kernel-privilege-ring-three explanation="Ring 3 是传统的用户模式特权级别。"}
::option[Ring 0。]{#kernel-privilege-ring-zero .correct explanation="内核使用传统 x86 中特权最高的保护环。"}
::option[Ring 7。]{#kernel-privilege-ring-seven explanation="传统 x86 保护环的编号为 0 到 3。"}
:::

## 受控转换

以下几种事件会把控制权转移到内核入口点：

- 系统调用指令请求内核服务
- 异常报告缺页或无效指令等状况
- 硬件中断报告外部事件

处理器保存执行上下文，通过已配置的入口机制改变特权级别，然后开始执行可信内核代码。内核验证请求和状态，执行或拒绝相应工作，并在适当时返回用户模式。

应用程序并不会暂时变成内核代码。CPU 只是代表该线程执行内核处理程序，并使用由内核控制的栈和映射。

:::single-choice{#kernel-privilege-system-call-transition}
系统调用转换期间会发生什么？

::option[应用程序的用户代码获得不受限制的 ring 0 执行权限。]{#kernel-privilege-user-ring-zero explanation="通过受控入口后，只有可信内核代码会执行。"}
::option[进程永久将自己的 UID 改为零。]{#kernel-privilege-uid-zero explanation="处理器模式转换不会改写用户凭据。"}
::option[控制权进入一个验证请求的规定内核处理程序。]{#kernel-privilege-kernel-handler .correct explanation="处理器通过配置好的入口路径改变模式，同时保留用户上下文以便返回。"}
:::

## CPU 特权不同于用户身份

以 Linux `root` 用户身份运行的应用程序通常仍在用户模式下执行。UID 0 会影响内核授权检查，但不会允许应用程序指令直接访问内核内存。反过来，无论哪个用户发起系统调用，内核代码都会在特权模式下执行。

能力、命名空间、seccomp、安全模块和 cgroup 会进一步约束进程可以发出哪些请求。这些分层策略与硬件层面的用户/内核模式边界相互独立。

:::single-choice{#kernel-privilege-root-distinction}
哪项说法正确比较了 root 身份与内核模式？

::option[Root 是用户空间凭据；内核模式是处理器执行特权。]{#kernel-privilege-credential-versus-mode .correct explanation="root 进程从用户模式发出经过授权的请求，而可信内核代码负责特权执行。"}
::option[root 拥有的每条指令都作为可加载内核代码运行。]{#kernel-privilege-root-kernel-code explanation="UID 所有权不会把可执行文件转变成内核模块。"}
::option[内核模式是存储在 `/etc/passwd` 中的另一个用户名。]{#kernel-privilege-kernel-username explanation="处理器模式是硬件状态，不是登录账户。"}
:::

## 边界为何重要

这条边界可以限制普通缺陷造成的破坏，并提供执行访问检查的位置，但内核漏洞和恶意模块仍可能突破它。应通过可信渠道更新内核和固件，尽量减少特权代码，并避免加载不可信模块。

推测执行问题和侧信道也说明，硬件隔离需要持续缓解措施；“位于不同保护环”只是基础，并非完整的安全证明。

:::single-choice{#kernel-privilege-boundary-limit}
用户/内核模式隔离是否能保证系统绝对安全？

::option[能；内核漏洞无法影响用户进程。]{#kernel-privilege-no-kernel-vulns explanation="内核漏洞可能危及整个系统。"}
::option[不能；特权代码缺陷和侧信道仍可能跨越预期边界。]{#kernel-privilege-not-complete .correct explanation="模式划分能缩小攻击面，但还必须结合正确的内核代码和其他缓解措施。"}
::option[能；硬件模式消除了访问控制策略的必要性。]{#kernel-privilege-no-policy explanation="凭据和安全策略对于授权资源共享仍然不可或缺。"}
:::

## 总结

现在，你可以区分硬件执行特权与 Linux 账户权限。

1. 理解用户模式与受保护虚拟地址空间的关系。
2. 理解内核模式与特权指令、特权映射的关系。
3. 将系统调用、异常和中断视为受控入口。
4. 区分 UID 0 授权与 ring 0 执行。
5. 将特权模式视为整体安全设计中的一层。
