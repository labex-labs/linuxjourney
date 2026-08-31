---
lesson_id: "emacs-buffer-navigation"
course_id: "advanced-text-fu"
lang: "en"
order_index: 11
title: "Emacs Buffer Navigation"
description: "Learn how to switch and kill Emacs buffers while splitting, selecting, and closing display windows."
meta_title: "Emacs Buffer Navigation - Advanced Text-Fu"
meta_description: "A comprehensive guide to Emacs buffer navigation. Learn how to efficiently switch buffers, split windows, and manage your workflow with essential Emacs commands. Master the emacs switch buffer command and improve your text editing skills."
meta_keywords: "emacs navigation, emacs switch buffer, emacs buffer management, emacs commands, C-x b, C-x k, C-x 2, text editor, linux"
---

An Emacs buffer holds text or editor state, while a window displays a buffer. A buffer can exist without being visible, and several windows can display one buffer. Managing one object does not automatically manage the other.

## Switching Buffers

Use `C-x b`, which runs `switch-to-buffer`, to select a buffer by name in the current window:

```text
C-x b
```

The minibuffer offers completion for existing names. Entering a new name can create a non-file buffer with that name; it does not visit a file pathname.

By default, `C-x Right` runs `next-buffer` and `C-x Left` runs `previous-buffer`, cycling through buffers in the selected window.

:::single-choice{#emacs-switch-buffer-key}
Which key sequence prompts for a buffer name to display in the current window?

::option[`C-x C-f`]{#emacs-buffer-find-file explanation="This prompts for a file pathname and visits it, which is a different operation from choosing an existing buffer by name."}
::option[`C-x b`]{#emacs-switch-buffer .correct explanation="`switch-to-buffer` reads a buffer name and displays that buffer in the selected window."}
::option[`C-x k`]{#emacs-buffer-kill explanation="This prompts to kill a buffer rather than switch the selected window to one."}
:::

## Splitting the Selected Window

Use `C-x 2` to split the selected window into an upper and lower window:

```text
C-x 2
```

Use `C-x 3` to split it into left and right windows:

```text
C-x 3
```

The new window initially displays a buffer, often the same one. Switch buffers in either window independently.

:::single-choice{#emacs-split-side-by-side}
Which key sequence splits the selected Emacs window into left and right windows?

::option[`C-x 1`]{#emacs-window-one explanation="This deletes other windows and makes the selected window the only one in its frame."}
::option[`C-x 2`]{#emacs-window-below explanation="This creates upper and lower windows rather than a side-by-side split."}
::option[`C-x 3`]{#emacs-window-right .correct explanation="`split-window-right`, bound to `C-x 3`, creates left and right windows."}
:::

## Selecting and Closing Windows

Use `C-x o`, which runs `other-window`, to select the next window:

```text
C-x o
```

Use these commands to remove window displays:

- `C-x 0`: Delete the selected window.
- `C-x 1`: Delete the other windows in the current frame.

Deleting a window normally leaves its displayed buffer alive. You can show that buffer again in another window.

:::single-choice{#emacs-select-other-window}
Which key sequence moves point and keyboard focus to another Emacs window?

::option[`C-x 0`]{#emacs-delete-selected-window explanation="This deletes the selected window rather than moving focus to another one."}
::option[`C-x o`]{#emacs-other-window .correct explanation="`other-window` cycles selection to another window in the frame."}
::option[`C-x b`]{#emacs-switch-in-window explanation="This changes which buffer the current window displays, not which window is selected."}
:::

:::single-choice{#emacs-keep-one-window}
Which key sequence keeps the selected window and deletes the other windows in its frame?

::option[`C-x 1`]{#emacs-delete-other-windows .correct explanation="`delete-other-windows` makes the selected window the only window in the frame."}
::option[`C-x 0`]{#emacs-delete-current-window explanation="This deletes the selected window itself rather than preserving it."}
::option[`C-x 2`]{#emacs-add-lower-window explanation="This adds another window instead of reducing the frame to one."}
:::

## Killing a Buffer

Use `C-x k`, which runs `kill-buffer`, to prompt for a buffer to remove from Emacs:

```text
C-x k
```

The current buffer is the default choice. If a file-visiting buffer has unsaved changes, Emacs warns before killing it. Read the prompt; killing a modified buffer can discard edits.

Killing a buffer is different from deleting a window. Emacs replaces a killed buffer in any displaying window, while deleting a window can leave its buffer untouched.

:::single-choice{#emacs-kill-buffer-key}
Which key sequence prompts to kill an Emacs buffer?

::option[`C-x 0`]{#emacs-kill-window-only explanation="This deletes a window display but normally leaves the buffer alive."}
::option[`C-x k`]{#emacs-kill-buffer-answer .correct explanation="`kill-buffer` removes the selected buffer from Emacs after any required modified-buffer confirmation."}
::option[`C-x b`]{#emacs-kill-switch explanation="This switches the current window to a named buffer and does not kill it."}
:::

Practice these commands with `*scratch*` and disposable buffers. Before killing any file-visiting buffer, confirm whether its modified indicator shows unsaved work.

## Summary

You can now manage what Emacs stores and what each window displays.

1. Switch buffers in the selected window with `C-x b`.
2. Split below with `C-x 2` or to the right with `C-x 3`.
3. Select another window with `C-x o`.
4. Remove window displays with `C-x 0` or `C-x 1`.
5. Kill a buffer with `C-x k` only after reviewing unsaved changes.
