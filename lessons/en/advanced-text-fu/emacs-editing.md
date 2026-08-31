---
lesson_id: "emacs-editing"
course_id: "advanced-text-fu"
lang: "en"
order_index: 12
title: "Emacs Editing"
description: "Learn how to move point, activate a region, and use Emacs kill-ring commands to edit text."
meta_title: "Emacs Editing - Advanced Text-Fu"
meta_description: "Master the fundamentals of Emacs editing with this beginner-friendly guide. Learn essential Emacs commands for text navigation, cutting, and pasting in this powerful Linux text editor."
meta_keywords: "Emacs, Emacs tutorial, Emacs commands, text editor, Linux editor, Emacs navigation, beginner Emacs, Emacs guide"
---

Emacs calls the current cursor position **point**. Movement commands reposition point; editing commands insert, delete, kill, copy, or yank text around it. In the key notation below, `C-` means Control and `M-` means Meta, commonly Alt.

## Moving by Characters and Lines

Arrow and other platform navigation keys may work, but Emacs's standard movement commands remain available across terminal and graphical sessions:

- `C-f`: Move forward one character.
- `C-b`: Move backward one character.
- `C-n`: Move to the next line.
- `C-p`: Move to the previous line.
- `C-a`: Move to the beginning of the line.
- `C-e`: Move to the end of the line.

:::single-choice{#emacs-edit-next-line}
Which Emacs key moves point to the next line?

::option[`C-p`]{#emacs-edit-previous-line explanation="`C-p` moves to the previous line, in the opposite direction."}
::option[`C-n`]{#emacs-edit-next-line-answer .correct explanation="`C-n`, for next-line, moves point downward to the next screen line position."}
::option[`C-f`]{#emacs-edit-forward-character explanation="`C-f` moves forward one character rather than to the next line."}
:::

## Moving by Words and Buffer Boundaries

Meta commands move across larger units:

- `M-f`: Move forward one word.
- `M-b`: Move backward one word.
- `M-<`: Move to the beginning of the buffer.
- `M->`: Move to the end of the buffer.

On many keyboards, Alt acts as Meta. When that chord is unavailable, pressing `Esc` and then the following key often sends the equivalent Meta command.

:::single-choice{#emacs-edit-buffer-end}
Which Emacs key moves point to the end of the buffer?

::option[`C-e`]{#emacs-edit-line-end explanation="`C-e` moves to the end of the current line rather than the entire buffer."}
::option[`M-<`]{#emacs-edit-buffer-start explanation="`M-<` moves to the beginning of the buffer."}
::option[`M->`]{#emacs-edit-buffer-end-answer .correct explanation="`M->` moves point to the end of the current buffer."}
:::

## Defining a Region

The **mark** is a saved buffer position. The text between point and mark is the **region**. Press `C-SPC`, written `C-space` in some documentation, to run `set-mark-command`, then move point to extend the active region.

In a terminal, `C-SPC` can be encoded as `C-@`. Highlighting depends on transient-mark settings, but point and mark still define a region.

:::single-choice{#emacs-edit-set-mark}
Which key begins defining a region by setting the mark at point?

::option[`C-w`]{#emacs-edit-kill-region-before-mark explanation="`C-w` kills an already defined region; it is not the initial mark-setting command."}
::option[`C-y`]{#emacs-edit-yank-before-mark explanation="`C-y` inserts text from the kill ring and does not begin a selection."}
::option[`C-SPC`]{#emacs-edit-control-space .correct explanation="`set-mark-command` places the mark, after which movement changes the region between mark and point."}
:::

## Killing or Copying a Region

Emacs stores killed and copied text in the **kill ring**:

- `C-w`: Kill the active region, removing it and adding it to the kill ring.
- `M-w`: Copy the active region to the kill ring without removing it.
- `C-k`: Kill from point to the end of the line; repeated use can include the newline.

Killing is more than ordinary deletion because the removed text is retained for later yanking.

:::single-choice{#emacs-edit-copy-region}
Which key copies the active region to the kill ring without removing it?

::option[`M-w`]{#emacs-edit-copy-active-region .correct explanation="`kill-ring-save`, bound to `M-w`, copies the region without deleting it."}
::option[`C-w`]{#emacs-edit-kill-active-region explanation="`C-w` removes the region while saving it to the kill ring."}
::option[`C-k`]{#emacs-edit-kill-line explanation="`C-k` kills text toward the end of the line rather than copying the selected region unchanged."}
:::

## Yanking from the Kill Ring

Use `C-y` to yank the most recent kill-ring entry at point. Immediately after a yank, `M-y` replaces that inserted text with an earlier kill-ring entry; repeating `M-y` cycles through entries.

```text
C-y
M-y
```

If another unrelated command occurs after `C-y`, `M-y` no longer has the same yank-pop context.

:::single-choice{#emacs-edit-yank-latest}
Which key inserts the most recent kill-ring entry at point?

::option[`C-y`]{#emacs-edit-yank-answer .correct explanation="`yank`, bound to `C-y`, inserts the latest kill-ring text into the current buffer."}
::option[`M-y`]{#emacs-edit-yank-pop explanation="`M-y` normally replaces a just-yanked entry with an earlier one; it depends on the preceding yank context."}
::option[`C-d`]{#emacs-edit-delete-character explanation="`C-d` deletes the character after point and does not retrieve kill-ring text."}
:::

Practice in `*scratch*` or a disposable file: move point, set the mark, copy one region, kill another, and yank both back. Save only when the resulting file is worth keeping.

## Summary

You can now navigate and rearrange Emacs text using point, mark, and the kill ring.

1. Move by characters or lines with Control commands.
2. Move by words or buffer boundaries with Meta commands.
3. Set the mark with `C-SPC` to define a region.
4. Kill with `C-w` or copy with `M-w`.
5. Yank with `C-y` and cycle with `M-y` immediately afterward.
