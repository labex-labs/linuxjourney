---
lesson_id: "history-command"
course_id: "command-line"
lang: "zh"
order_index: 9
title: "history 命令"
description: "学习在 Bash 中查看、搜索、重用和管理命令历史。"
meta_title: "history - 命令行"
meta_description: "通过示例学习 Linux history 命令，包括查看命令历史、重运行命令、反向搜索、删除条目和清屏操作。"
meta_keywords: "linux history 命令, bash history, history -c, history -d, history -w, Ctrl-R, 命令历史, clear 命令"
---

交互式 shell 可以保存你输入过的命令。本课重点介绍 Bash，其中的 `history` 内建命令用于显示和管理这份记录；其他 shell 可能采用不同的快捷键、文件或设置。

## 查看 Bash 历史

要查看你使用过的命令列表，输入 `history`。

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

每一行都有一个历史编号，后面跟着命令。

:::single-choice{#show-command-history}
哪个 Bash 命令会显示当前带编号的历史列表？

::option[`clear`]{#clear-display explanation="`clear` 刷新可见的终端区域，不会显示以前的命令。"}
::option[`history -w`]{#write-history explanation="`history -w` 把当前列表写入历史文件，用途是保存，而不是显示列表。"}
::option[`history`]{#show-history .correct explanation="`history` 内建命令会打印当前历史列表中的命令，通常还会带上历史编号。"}
:::

## 重用以前的命令

shell 提供了几种快捷方式来方便地重运行命令。

- **向上箭头**：想运行刚才执行过的命令？只需按向上箭头键即可向后循环浏览历史命令。
- **`!!` 快捷方式**：要再次执行最近的命令，可以使用 `!!`。例如，如果你刚运行了 `cat file1`，输入 `!!` 并按回车将再次执行 `cat file1`。
- **按编号运行**：使用 `!102` 来运行历史中编号为 102 的命令。
- **按前缀运行**：使用 `!cat` 来运行最近以 `cat` 开头的命令。

以 `!` 开头的历史扩展形式可能会在按 Enter 后立即运行命令。只要有疑问，就先检查匹配内容，尤其是在添加提升权限的命令或操作重要文件之前。

:::single-choice{#repeat-most-recent-command}
哪个 Bash 历史扩展会重复最近执行的命令？

::option[`!102`]{#event-number explanation="这个扩展会选择历史编号 102 的命令，而该条目不一定是最近的命令。"}
::option[`!cat`]{#event-prefix explanation="它选择最近一条以 `cat` 开头的命令，并不表示任意类型的最近命令。"}
::option[`!!`]{#previous-event .correct explanation="在 Bash 中，`!!` 会展开为上一条命令，并在提交该行后执行它。"}
:::

## 交互式搜索历史

最强大的历史快捷键之一是 `Ctrl-R`。这会启动反向搜索。按下 `Ctrl-R` 后，开始输入你想查找的命令的任意部分，shell 会显示最近匹配的命令。你可以反复按 `Ctrl-R` 来循环浏览更早的匹配项。找到想要的命令后，按回车即可执行。

按 Enter 会执行显示的匹配项。如果想先查看或编辑，请用方向键把该命令放到编辑行上。

:::single-choice{#search-before-executing}
你记得以前某条 Bash 命令的一部分，并想交互式查找它。首先应按什么？

::option[`Ctrl+D`]{#end-input explanation="`Ctrl+D` 在许多终端场景中表示输入结束，在空闲 shell 中甚至可能退出；它不会开始历史搜索。"}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C` 通常会中断或取消当前操作，并不搜索命令历史。"}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R` 会开始对命令历史进行反向增量搜索，继续输入字符可缩小匹配范围。"}
:::

## 管理历史列表

除了查看历史，你还可以直接管理它。

- **清除当前历史列表**：`history -c` 会移除内存中的所有历史条目。
- **将历史写入文件**：`history -w` 会将当前会话的历史保存到你的历史文件，通常是 `~/.bash_history`。
- **删除特定条目**：`history -d <offset>` 按历史编号删除一条命令。

示例：

```bash
$ history -d 101
$ history -w
```

清空内存列表本身并不能保证旧命令已从所有文件、备份或其他活动 shell 中消失。历史行为还取决于 Bash 设置，以及会话读取或写入文件的时机。

:::single-choice{#save-current-history-list}
哪个命令会把当前 Bash 历史列表写入配置的历史文件？

::option[`history -c`]{#clear-current-list explanation="`-c` 会清空内存列表，并不要求保存当前列表。"}
::option[`history -d 101`]{#delete-one-entry explanation="`-d` 会删除选定的一条历史记录，不是保存完整列表的操作。"}
::option[`history -w`]{#write-current-list .correct explanation="`-w` 会把当前历史列表写入配置的历史文件。"}
:::

## 清理显示和补全名称

需要新的可见终端区域时，可以使用 `clear`：

```bash
$ clear
```

这不会删除 Bash 历史列表。根据终端的不同，滚动回看中也可能仍保留旧的显示内容。

Tab 补全也是避免重复输入的方法。先输入命令、文件名或目录名的开头，再按 Tab。若匹配唯一，Bash 可能直接补全；若有多个匹配，则可能显示候选项。

命令行可能被存进历史记录，因此如果存在更安全的输入方法，不要直接把密码、令牌或其他秘密写进命令。

:::single-choice{#distinguish-clear-from-history-clear}
你想刷新可见终端，但不删除内存中的命令历史。应运行哪个命令？

::option[`clear`]{#clear-visible-area .correct explanation="`clear` 会刷新可见终端区域，同时保留 Bash 的内存历史列表。"}
::option[`history -c`]{#clear-memory explanation="它会删除当前内存历史列表中的条目，改变的是历史，而不只是刷新显示。"}
::option[`history -d 1`]{#delete-first-entry explanation="它要求 Bash 删除选定的历史条目，并不会清理可见终端区域。"}
:::

## 总结

现在，你可以查找并重用 Bash 命令，同时有意识地管理历史记录。

1. 显示当前带编号的历史列表。
2. 谨慎地调出或展开以前的命令。
3. 使用 `Ctrl+R` 交互式搜索历史。
4. 删除、清空或写入历史条目。
5. 区分命令历史与终端显示内容。
