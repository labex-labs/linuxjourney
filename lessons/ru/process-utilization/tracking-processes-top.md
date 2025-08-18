---
lang: "ru"
title: "Отслеживание процессов: top"
meta_title: "Отслеживание процессов: top - Использование процессов"
meta_description: "Узнайте, как использовать команду Linux `top` для мониторинга системных ресурсов и отслеживания процессов. Разберитесь с деталями CPU, памяти и процессов для анализа производительности."
meta_keywords: "Команда Linux top, мониторинг процессов, использование системы, производительность Linux, для начинающих, учебник, руководство"
---

## Lesson Content

В этом курсе мы рассмотрим, как читать и анализировать использование ресурсов в вашей системе. Этот урок покажет несколько отличных инструментов, которые можно использовать, когда вам нужно отслеживать, что делает процесс.

### top

Мы уже обсуждали `top` раньше, но сейчас мы углубимся в детали того, что он на самом деле отображает. Помните, `top` — это инструмент, который мы использовали для получения представления об использовании системы нашими процессами в реальном времени:

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

Давайте разберем, что означает этот вывод. Вам не нужно это запоминать, но возвращайтесь к этому, когда вам понадобится справка.

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

Поля слева направо:

1. Current time
2. How long the system has been running
3. How many users are currently logged on
4. System load average (more to come)

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - Percentage of CPU time spent running users’ processes that aren’t niced.
2. `sy`: system CPU time - Percentage of CPU time spent running the kernel and kernel processes.
3. `ni`: nice CPU time - Percentage of CPU time spent running niced processes.
4. `id`: CPU idle time - Percentage of CPU time that is spent idle.
5. `wa`: I/O wait - Percentage of CPU time that is spent waiting for I/O. If this value is low, the problem probably isn’t disk or network I/O.
6. `hi`: hardware interrupts - Percentage of CPU time spent serving hardware interrupts.
7. `si`: software interrupts - Percentage of CPU time spent serving software interrupts.
8. `st`: steal time - If you are running virtual machines, this is the percentage of CPU time that was stolen from you for other tasks.

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

1. `PID`: ID of the process
2. `USER`: user that is the owner of the process
3. `PR`: Priority of process
4. `NI`: The nice value
5. `VIRT`: Virtual memory used by the process
6. `RES`: Physical memory used by the process
7. `SHR`: Shared memory of the process
8. `S`: Indicates the status of the process: `S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible, `T`=stopped
9. `%CPU`: this is the percent of CPU used by this process
10. `%MEM`: percentage of RAM used by this process
11. `TIME+`: total time of activity of this process
12. `COMMAND`: name of the process

Вы также можете указать ID процесса, если хотите отслеживать только определенные процессы:

```bash
top -p 1
```

## Exercise

Поэкспериментируйте с командой `top` и посмотрите, какие процессы используют больше всего ресурсов.

## Quiz Question

Какая команда отображает тот же вывод, что и первая строка в `top`?

## Quiz Answer

uptime
