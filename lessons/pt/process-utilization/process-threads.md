---
index: 3
lang: "pt"
title: "Threads de Processo"
meta_title: "Threads de Processo - Utilização do Processo"
meta_description: "Um guia sobre threads de processos no Linux. Aprenda a diferença entre processos de thread único e multi-thread e como usar o comando ps para exibir threads."
meta_keywords: "threads Linux, threads de processo, ps mostrar threads, ps m, multi-thread, thread único, processo leve, gerenciamento de processos Linux"
---

## Lesson Content

### O Que São Threads de Processo?

You may have heard the terms single-threaded and multi-threaded. Threads are units of execution within a process and are often called "lightweight processes." While processes operate with their own isolated system resources, threads within the same process can share these resources, such as memory. This shared-resource model makes communication between threads much faster and more efficient than communication between separate processes.

### Single-Threaded vs. Multi-Threaded

Every process has at least one thread. A process with only one thread is called single-threaded, while a process with more than one is multi-threaded.

For example, when you use a modern text editor, it might run as a single process. However, within that process, one thread could be managing your keyboard input, while another thread runs in the background to perform spell-checking or auto-saving. This concurrent execution makes the application feel more responsive. Using multiple threads is often more efficient than launching multiple processes for related tasks.

### How to Show Threads with ps

To inspect running processes and their threads, you can use the `ps` command. While `ps` has many options, a common way to **show threads** is with the `m` flag.

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

### Interpreting the Output

In the output above, the lines with a `PID` (Process ID) represent the main process. The lines directly underneath, which have a dash (`-`) instead of a `PID`, represent the threads belonging to that process. In this example, both the `bash` and `ps m` processes are single-threaded, as each has only one main thread listed.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux processes and their management:

1. **[Gerenciar e Monitorar Processos Linux](https://labex.io/pt/labs/comptia-manage-and-monitor-linux-processes-590864)** - Neste laboratório, você aprenderá habilidades essenciais para gerenciar e monitorar processos em um sistema Linux. Você explorará como interagir com processos em primeiro plano e em segundo plano, inspecioná-los com `ps`, monitorar recursos com `top`, ajustar a prioridade com `renice` e terminá-los com `kill`.

This lab will help you apply the concepts of process management in real scenarios and build confidence with monitoring system activity.

## Quiz Question

Verdadeiro ou falso, todos os processos começam como single-threaded.

## Quiz Answer

True
