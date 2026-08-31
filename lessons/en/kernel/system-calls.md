---
lesson_id: "system-calls"
course_id: "kernel"
lang: "en"
order_index: 3
title: "System Calls"
description: "Learn how user-space code invokes Linux kernel services and how to inspect calls safely with `strace`."
meta_title: "System Calls - Kernel"
meta_description: "Explore the fundamentals of a system call in Linux. Learn how user-space processes use system calls (syscalls) to request services from the kernel, switch modes, and how the syscall table works. Use `strace` to see system calls in action."
meta_keywords: "system call linux, system calls, syscall table, kernel mode, user mode, strace, linux kernel, syscall API"
---

A system call is a defined entry into the kernel through which user-space code requests an operation such as opening a file, mapping memory, creating a process, or sending network data. The kernel validates arguments, credentials, object state, and security policy before performing the request.

## Libraries and the System-Call ABI

Applications commonly call C library functions rather than writing architecture-specific entry instructions. A library wrapper prepares registers and memory according to the system-call ABI, enters the kernel, and translates the result into its language-level convention.

The relationship is not always one function to one syscall:

- a library function can combine several system calls
- some functions operate entirely in user space
- an optimized vDSO function can obtain certain kernel-maintained data without a full mode transition
- one system call can support many higher-level APIs

:::single-choice{#system-calls-library-wrapper}
What does a typical libc system-call wrapper do?

::option[Prepare ABI arguments, enter the kernel, and translate the result.]{#system-calls-wrapper-role .correct explanation="The wrapper hides architecture-specific calling conventions behind a normal library interface."}
::option[Give the application unrestricted access to kernel memory.]{#system-calls-wrapper-unrestricted explanation="The kernel entry remains controlled and validates the request."}
::option[Recompile the kernel each time the function is called.]{#system-calls-wrapper-compile explanation="A runtime call uses the already running kernel."}
:::

## Entering and Returning from the Kernel

The wrapper places a system-call number and arguments in architecture-defined locations, then executes an entry instruction such as `syscall` on x86-64 or `svc` on AArch64. The processor switches to a configured privileged entry point and the kernel dispatches the request.

After completion, the kernel returns a value or an error indication. C library wrappers commonly return `-1` and set thread-local `errno` for errors. Other languages and runtimes expose different error types.

Calling every entry a “software interrupt” is imprecise on current architectures; traps, fast system-call instructions, and supervisor calls implement related controlled transitions differently.

:::single-choice{#system-calls-entry-result}
Who validates a system call's arguments and authorization?

::option[The shell prompt before the process starts.]{#system-calls-shell-validates explanation="A process can make syscalls independently of a shell, and kernel checks remain necessary."}
::option[The kernel implementation of the requested service.]{#system-calls-kernel-validates .correct explanation="The privileged handler checks pointers, object state, credentials, and policy before acting."}
::option[The disk partition table.]{#system-calls-partition-validates explanation="Storage layout metadata does not authorize arbitrary kernel services."}
:::

## Numbers and Compatibility

System-call numbers and calling conventions are architecture-specific. The same symbolic call can have a different number or structure layout on another ABI. Kernel releases can add system calls, while stable user-space ABIs aim to preserve existing behavior.

An unprivileged process cannot insert arbitrary new handlers into the running kernel's syscall table. Extending the interface requires kernel code and careful ABI design. Features such as seccomp can filter which calls a process is allowed to make, but do not create new kernel implementations.

:::single-choice{#system-calls-number-portability}
Why should an application avoid hard-coding syscall numbers from another architecture?

::option[Numbers and calling conventions are ABI-specific.]{#system-calls-abi-specific .correct explanation="A number meaningful on one architecture can identify another operation or be absent on another."}
::option[System calls are named from the current working directory.]{#system-calls-directory-names explanation="Pathnames do not define the syscall numbering ABI."}
::option[Every process receives a random syscall table at startup.]{#system-calls-random-table explanation="The running kernel ABI is stable for an architecture, not randomized per process."}
:::

## Tracing with `strace`

Trace a simple command and save output separately:

```bash
$ strace -o trace.log -- ls
```

Follow child processes where authorized with `-f`, or narrow output with an expression such as:

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace` can reveal paths, arguments, environment-derived data, network addresses, file content fragments, and credentials passed incorrectly through arguments. Store traces with restrictive permissions and remove them according to incident-data policy.

:::single-choice{#system-calls-strace-purpose}
What does `strace` primarily observe?

::option[Only source-code lines executed inside the application.]{#system-calls-strace-source-lines explanation="Source-level tracing requires debuggers or instrumentation with symbols."}
::option[System calls and signals at the user-kernel boundary.]{#system-calls-strace-boundary .correct explanation="It reports requests, arguments, results, and signal events for traced processes."}
::option[The physical voltage of each CPU core.]{#system-calls-strace-voltage explanation="Hardware telemetry is outside syscall tracing."}
:::

## Interpreting Traces Carefully

Tracing changes timing and can impose substantial overhead. A failed call may be an expected probe, and the final visible error can result from an earlier operation or application policy. Decode file descriptors, follow process relationships, and correlate with application logs.

Permissions and ptrace security policy restrict which processes can be traced. Do not attach to another user's or a production process without authorization; suspension and timing changes can affect service behavior.

:::single-choice{#system-calls-strace-failure}
Does one failed syscall in a trace necessarily mean the application is broken?

::option[Yes; every nonzero return immediately terminates Linux.]{#system-calls-nonzero-terminates explanation="Applications routinely handle syscall errors without system failure."}
::option[No; programs often probe alternatives and handle expected errors.]{#system-calls-expected-failure .correct explanation="Interpret the return in control-flow and application context rather than in isolation."}
::option[Yes; the kernel never returns expected errors.]{#system-calls-no-expected-errors explanation="Errors such as missing paths or unsupported operations are normal API outcomes."}
:::

## Summary

You can now trace a system call from library API to validated kernel work.

1. Separate high-level functions from the system-call ABI.
2. Relate architecture entry instructions to controlled kernel dispatch.
3. Treat syscall numbers and structures as architecture-specific.
4. Use filtered `strace` output while protecting sensitive data.
5. Interpret failures and tracing overhead in application context.
