---
lesson_id: "emacs-exiting-and-help"
course_id: "advanced-text-fu"
lang: "en"
order_index: 13
title: "Emacs Exiting and Help"
description: "Learn how to exit Emacs safely, cancel pending commands, inspect help topics, and undo changes."
meta_title: "Emacs Exiting and Help - Advanced Text-Fu"
meta_description: "Learn Emacs exiting commands and how to access help. Understand basic Emacs navigation and undo functions in this beginner-friendly tutorial."
meta_keywords: "Emacs exit, Emacs help, Emacs undo, Emacs tutorial, Linux text editor, beginner guide"
---

Emacs provides contextual help for keys, functions, variables, and active modes. It also protects modified file-visiting buffers during exit, giving you a chance to save or decline each write.

## Exiting Emacs

Use `C-x C-c`, which runs `save-buffers-kill-terminal`, to request that the Emacs session or terminal connection close:

```text
C-x C-c
```

Emacs checks relevant modified file-visiting buffers and asks whether to save them. Read each buffer name and answer deliberately. It may also ask about active processes. Cancel the exit if you need to inspect work before deciding.

In an `emacsclient` workflow or an Emacs server, the exact frame and server behavior can differ, but modified-buffer prompts still deserve careful attention.

:::single-choice{#emacs-exit-key}
Which key sequence requests a normal Emacs exit and checks modified buffers?

::option[`C-x k`]{#emacs-exit-kill-buffer explanation="This kills one selected buffer and does not request that the Emacs session exit."}
::option[`C-g`]{#emacs-exit-keyboard-quit explanation="This cancels a pending command or prompt rather than closing Emacs."}
::option[`C-x C-c`]{#emacs-exit-save-buffers .correct explanation="This runs the normal save-buffers-and-exit workflow, including prompts for relevant unsaved work."}
:::

## Opening the Help Dispatcher

The standard help prefix is `C-h`. Use `C-h C-h`, which runs help for help, to display guidance on available help commands:

```text
C-h C-h
```

The second key chooses the type of help you need.

:::single-choice{#emacs-help-for-help}
Which key sequence explains how to use the Emacs help system?

::option[`C-h C-h`]{#emacs-help-help .correct explanation="The help prefix followed by another `C-h` opens help about the help dispatcher itself."}
::option[`C-x C-h`]{#emacs-help-prefix-list explanation="This is not the help-for-help sequence introduced here."}
::option[`C-h t`]{#emacs-help-tutorial-other explanation="This opens the tutorial directly rather than explaining the broader help menu."}
:::

## Describing Keys and Editor State

Useful help commands include:

- `C-h k KEY`: Describe what a key sequence runs.
- `C-h f FUNCTION`: Describe an Emacs Lisp function.
- `C-h v VARIABLE`: Describe an Emacs Lisp variable.
- `C-h m`: Describe the current major and minor modes.
- `C-h t`: Open the interactive tutorial.

For example, type `C-h k C-x C-s` to see documentation for the save-buffer binding.

:::single-choice{#emacs-describe-key}
You want to learn what `C-x C-s` does. Which help prefix should you enter before that key sequence?

::option[`C-h k`]{#emacs-describe-key-answer .correct explanation="`describe-key` waits for a key sequence and explains the command bound to it."}
::option[`C-h f`]{#emacs-describe-function explanation="This prompts for a function name rather than reading a key sequence to identify its binding."}
::option[`C-h v`]{#emacs-describe-variable explanation="This prompts for a variable name and does not inspect a key binding."}
:::

## Cancelling a Pending Command

Use `C-g`, bound to `keyboard-quit`, when you are stuck in a prompt, partially entered key sequence, incremental search, or other command you want to cancel:

```text
C-g
```

It does not undo buffer changes that have already happened and does not exit Emacs. It stops the current interaction and returns control to ordinary editing when possible.

:::single-choice{#emacs-cancel-pending-command}
Which key normally cancels the current Emacs prompt or pending command?

::option[`C-x C-c`]{#emacs-cancel-exit explanation="This initiates the Emacs exit workflow rather than merely cancelling the current prompt."}
::option[`C-y`]{#emacs-cancel-yank explanation="This yanks text from the kill ring and does not cancel a command."}
::option[`C-g`]{#emacs-keyboard-quit-answer .correct explanation="`keyboard-quit` aborts the current command interaction and returns control to Emacs."}
:::

## Undoing Buffer Changes

Use `C-/`, `C-_`, or `C-x u` to invoke undo in common Emacs configurations:

```text
C-/
```

Repeated undo commands walk backward through recent buffer changes. Cursor movement alone is not normally a buffer change. Emacs versions and configurations can offer `undo-redo` and more advanced history tools; use `C-h k` on your actual undo and redo bindings to verify local behavior.

:::single-choice{#emacs-undo-change}
Which key sequence is a standard binding for undoing a recent Emacs buffer change?

::option[`C-/`]{#emacs-undo-control-slash .correct explanation="`C-/` is a standard undo binding, alongside `C-_` and `C-x u` in common configurations."}
::option[`C-x C-s`]{#emacs-undo-save explanation="This saves the current buffer rather than traversing its undo history."}
::option[`C-w`]{#emacs-undo-kill explanation="This kills the active region and creates another change instead of undoing one."}
:::

Practice by opening `*scratch*`, making a disposable change, using undo, asking `C-h k` about an unfamiliar key, and cancelling a minibuffer prompt with `C-g` before exiting normally.

## Summary

You can now recover help and leave Emacs without ignoring unsaved work.

1. Exit through the modified-buffer checks with `C-x C-c`.
2. Open help for help with `C-h C-h`.
3. Describe keys, functions, variables, or active modes.
4. Cancel a pending command with `C-g`.
5. Undo recent buffer changes with a verified local binding.
