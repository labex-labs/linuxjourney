---
lesson_id: "kernel-privilege-levels"
course_id: "kernel"
lang: "en"
order_index: 2
title: "Privilege Levels"
description: "Learn how processor privilege separates user execution from trusted kernel execution."
meta_title: "Privilege Levels - Kernel"
meta_description: "Explore the core concepts of Linux privilege levels. This lesson explains the difference between kernel mode and user mode, the role of protection rings, and how system calls provide privileged access to hardware. Understand how the kernel manages security and kernel privileges."
meta_keywords: "Linux privilege levels, kernel mode, user mode, protection rings, system calls, privileged access, kernel privileges, what is the difference between kernel mode and user mode, Linux security"
---

Processors provide privilege modes that restrict sensitive instructions and memory access. Linux uses this hardware boundary so ordinary application failures cannot directly overwrite kernel memory or reconfigure devices. The kernel controls transitions into privileged execution.

## User Mode

A normal process executes in user mode within its virtual address space. It can compute freely and access memory mappings the kernel has granted, which can be large; user mode does not mean “only a small amount of memory.” It cannot directly access arbitrary physical memory, another process's private mappings, or privileged processor controls.

Page tables and protection bits enforce memory access. If a thread references an invalid or disallowed address, the processor traps into the kernel, which can resolve a valid page fault or deliver a signal such as `SIGSEGV`.

:::single-choice{#kernel-privilege-user-mode-memory}
What memory can a user-mode process normally access directly?

::option[Every physical RAM address and all kernel memory.]{#kernel-privilege-all-physical explanation="Those accesses are prevented by privilege and virtual-memory protection."}
::option[Only one fixed byte selected when the process starts.]{#kernel-privilege-one-byte explanation="A process can have many mapped regions while remaining unprivileged."}
::option[Mappings permitted in its own virtual address space.]{#kernel-privilege-own-mappings .correct explanation="Hardware page protections restrict the process to mappings established with appropriate access."}
:::

## Kernel Mode

Kernel mode permits execution of privileged instructions and access to protected kernel mappings needed for memory management, scheduling, interrupt handling, and drivers. On x86 this Linux split is commonly described as ring 0 for the kernel and ring 3 for user processes. Linux normally does not use rings 1 and 2 for ordinary process isolation.

Other architectures use different names and mechanisms, such as exception levels. Virtualization adds hypervisor and guest relationships that do not fit a simple two-ring drawing. The essential idea is controlled privilege, not the x86 ring numbers themselves.

:::single-choice{#kernel-privilege-x86-kernel-ring}
Which x86 protection ring normally executes the Linux kernel?

::option[Ring 3.]{#kernel-privilege-ring-three explanation="Ring 3 is the conventional user-mode privilege level."}
::option[Ring 0.]{#kernel-privilege-ring-zero .correct explanation="The kernel uses the most privileged traditional x86 ring."}
::option[Ring 7.]{#kernel-privilege-ring-seven explanation="Traditional x86 protection rings are numbered 0 through 3."}
:::

## Controlled Transitions

Several events transfer control to a kernel entry point:

- a system-call instruction requests a kernel service
- an exception reports a condition such as a page fault or invalid instruction
- a hardware interrupt reports an external event

The processor saves execution context, changes privilege according to configured entry mechanisms, and begins trusted kernel code. The kernel validates the request and state, performs or rejects work, then returns to user mode when appropriate.

The application does not temporarily become kernel code. The CPU executes a kernel handler on behalf of the thread, with kernel-controlled stacks and mappings.

:::single-choice{#kernel-privilege-system-call-transition}
What happens during a system-call transition?

::option[The application's user code receives unrestricted ring 0 execution.]{#kernel-privilege-user-ring-zero explanation="Only trusted kernel code executes after the controlled entry."}
::option[The process permanently changes its UID to zero.]{#kernel-privilege-uid-zero explanation="Processor mode transition does not rewrite user credentials."}
::option[Control enters a defined kernel handler that validates the request.]{#kernel-privilege-kernel-handler .correct explanation="The processor changes mode through a configured entry path while preserving the user context for return."}
:::

## CPU Privilege Is Not User Identity

An application running as Linux user `root` still normally executes in user mode. UID 0 influences kernel authorization checks but does not let its instructions directly access kernel memory. Conversely, kernel code executes in privileged mode regardless of which user's system call caused it to run.

Capabilities, namespaces, seccomp, security modules, and cgroups further constrain what a process can request. This layered policy is separate from the hardware user/kernel mode boundary.

:::single-choice{#kernel-privilege-root-distinction}
Which statement correctly compares root identity and kernel mode?

::option[Root is a user-space credential; kernel mode is a processor execution privilege.]{#kernel-privilege-credential-versus-mode .correct explanation="A root process makes authorized requests from user mode, while trusted kernel code performs privileged execution."}
::option[Every root-owned instruction runs as loadable kernel code.]{#kernel-privilege-root-kernel-code explanation="UID ownership does not transform an executable into a kernel module."}
::option[Kernel mode is another username stored in `/etc/passwd`.]{#kernel-privilege-kernel-username explanation="Processor modes are hardware states, not login accounts."}
:::

## Why the Boundary Matters

The boundary limits damage from ordinary bugs and provides a point for access checks, but kernel vulnerabilities and malicious modules can defeat it. Keep kernels and firmware updated through trusted channels, minimize privileged code, and avoid loading untrusted modules.

Speculative-execution issues and side channels also show that hardware isolation requires ongoing mitigation; “different ring” is a foundation, not a complete security proof.

:::single-choice{#kernel-privilege-boundary-limit}
Does user/kernel mode separation guarantee complete system security?

::option[Yes; kernel vulnerabilities cannot affect user processes.]{#kernel-privilege-no-kernel-vulns explanation="A kernel vulnerability can compromise the whole system."}
::option[No; privileged-code flaws and side channels can still cross intended boundaries.]{#kernel-privilege-not-complete .correct explanation="The mode split reduces attack surface but must be combined with correct kernel code and additional mitigations."}
::option[Yes; hardware modes eliminate the need for access-control policy.]{#kernel-privilege-no-policy explanation="Credentials and security policy remain essential for authorized resource sharing."}
:::

## Summary

You can now distinguish hardware execution privilege from Linux account authority.

1. Relate user mode to protected virtual address spaces.
2. Relate kernel mode to privileged instructions and mappings.
3. Treat system calls, exceptions, and interrupts as controlled entries.
4. Separate UID 0 authorization from ring 0 execution.
5. View privilege modes as one layer of a broader security design.
