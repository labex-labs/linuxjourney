---
index: 1
lang: "ru"
title: "ps (Процессы)"
meta_title: "ps (Процессы) - Процессы"
meta_description: "Узнайте о команде Linux 'ps' для просмотра запущенных процессов и понимания идентификаторов процессов (PID). Получите руководство для начинающих по управлению процессами."
meta_keywords: "команда ps, процессы Linux, идентификатор процесса, PID, учебник Linux, для начинающих, руководство, команда top"
---

## Lesson Content

Процессы — это программы, которые запущены на вашей машине. Они управляются ядром, и каждому процессу присваивается идентификатор, называемый **идентификатором процесса (PID)**. Этот PID присваивается в порядке создания процессов.

Запустите команду `ps`, чтобы увидеть список запущенных процессов:

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Это показывает вам быстрый снимок текущих процессов:

- PID: Process ID
- TTY: Controlling terminal associated with the process (мы подробно рассмотрим это позже)
- STAT: Process status code
- TIME: Total CPU usage time
- CMD: Name of executable/command

Если вы посмотрите man page для `ps`, вы увидите, что существует множество опций команды, которые вы можете передать. Они будут различаться в зависимости от того, какие опции вы хотите использовать — BSD, GNU или Unix. По моему мнению, стиль BSD более популярен, поэтому мы будем использовать его. Если вам интересно, разница между стилями заключается в количестве используемых дефисов и флагов.

```bash
ps aux
```

**a** отображает все запущенные процессы, включая те, которые запущены другими пользователями. **u** показывает больше деталей о процессах. И, наконец, **x** перечисляет все процессы, которые не имеют связанного с ними TTY. Эти программы будут показывать `?` в поле TTY; они наиболее распространены в процессах-демонах, которые запускаются как часть системного стартапа.

Вы заметите, что теперь вы видите гораздо больше полей. Нет необходимости запоминать их все; в более позднем курсе по продвинутым процессам мы снова рассмотрим некоторые из них:

- USER: The effective user (тот, чей доступ мы используем)
- PID: Process ID
- %CPU: CPU time used divided by the time the process has been running
- %MEM: Ratio of the process's resident set size to the physical memory on the machine
- VSZ: Virtual memory usage of the entire process
- RSS: Resident set size, the non-swapped physical memory that a task has used
- TTY: Controlling terminal associated with the process
- STAT: Process status code
- START: Start time of the process
- TIME: Total CPU usage time
- COMMAND: Name of executable/command

Команда `ps` может быть немного запутанной для просмотра. Пока что поля, на которые мы будем смотреть чаще всего, это PID, STAT и COMMAND.

Еще одна очень полезная команда — это команда **top**. `top` дает вам информацию о процессах, запущенных в вашей системе, в реальном времени, а не в виде снимка. По умолчанию обновление происходит каждые 10 секунд. `top` — чрезвычайно полезный инструмент для определения того, какие процессы занимают много ваших ресурсов.

```bash
top
```

## Exercise

Use the `ps` command with different flags and see how the output changes.

## Quiz Question

Какой флаг `ps` используется для просмотра подробной информации о процессах?

## Quiz Answer

u
