---
lesson_id: "vim-editing"
course_id: "advanced-text-fu"
lang: "en"
order_index: 7
title: "Vim Editing"
description: "Learn how Vim combines operators, motions, registers, puts, and undo commands for text editing."
meta_title: "Vim Editing - Advanced Text-Fu"
meta_description: "A beginner Vim tutorial on essential editing commands. Learn how to delete, change, copy (yank), and paste text in the Vim text editor to improve your Linux workflow."
meta_keywords: "Vim editing, Vim commands, Linux text editor, Vim tutorial, Vim guide, beginner Vim, dd command, Vim delete"
---

Vim editing commands often combine an operator with a motion or text object. This grammar lets the same actions work at character, word, line, and larger scopes. Press `Esc` before practicing to return to Normal mode.

## Combining an Operator with a Motion

The general form is:

```text
[count] operator [count] motion
```

Common operators include:

- `d`: Delete text.
- `c`: Change text, then enter Insert mode.
- `y`: Yank, or copy, text.

For example, `dw` deletes through the `w` motion, while `d$` deletes from the cursor through the end of the line. `2dw` applies the delete across two word motions.

:::single-choice{#vim-edit-operator-motion}
In Normal mode, what does `d$` do?

::option[Deletes the complete file from the cursor onward.]{#vim-edit-delete-file-end explanation="The dollar motion targets the current line's end, not the end of the entire buffer."}
::option[Deletes from the cursor through the end of the line.]{#vim-edit-delete-line-end .correct explanation="The `d` operator applies to the `$` end-of-line motion."}
::option[Moves to the end of the line without changing text.]{#vim-edit-move-line-end explanation="`$` alone moves, but the preceding `d` turns the covered range into a deletion."}
:::

## Editing Characters and Lines

Some commands are convenient shortcuts:

- `x`: Delete the character under the cursor.
- `dd`: Delete the current line linewise.
- `3dd`: Delete three lines starting with the current line.
- `cc`: Change the current line and enter Insert mode.
- `r{char}`: Replace the character under the cursor with `{char}`.
- `R`: Enter Replace mode until `Esc` is pressed.

Repeating an operator, as in `dd`, makes it linewise. A count expands the number of lines.

:::single-choice{#vim-edit-delete-three-lines}
Which Normal-mode command deletes the current line and the next two lines?

::option[`dd3`]{#vim-edit-dd-three explanation="The count belongs before the doubled operator in this command form."}
::option[`3x`]{#vim-edit-three-x explanation="This deletes three characters under and after the cursor, not three complete lines."}
::option[`3dd`]{#vim-edit-three-dd .correct explanation="The count applies to the linewise `dd` command, deleting three lines beginning at the current one."}
:::

## Changing Text and Entering Insert Mode

The `c` operator removes the selected text and enters Insert mode so you can type a replacement:

- `ce`: Change through the end of the word.
- `c$`: Change through the end of the line.
- `cc`: Change the complete current line.
- `ciw`: Change the inner word under the cursor.
- `caw`: Change a word text object, including surrounding spacing as Vim defines it.

The behavior of `cw` has a historical special case and often acts like `ce`. Text objects such as `iw` can make the intended boundary clearer.

:::single-choice{#vim-edit-change-inner-word}
Which Normal-mode command replaces the inner word under the cursor by deleting it and entering Insert mode?

::option[`diw`]{#vim-edit-delete-inner-word explanation="This deletes the inner word but remains in Normal mode instead of starting replacement text."}
::option[`yiw`]{#vim-edit-yank-inner-word explanation="This yanks the inner word without changing the buffer or entering Insert mode."}
::option[`ciw`]{#vim-edit-change-inner-word-answer .correct explanation="The `c` operator changes the `iw` text object and then enters Insert mode."}
:::

## Yanking and Putting Text

Vim calls copying **yanking** and pasting **putting**:

- `yw`: Yank through a word motion.
- `yy`: Yank the current line.
- `p`: Put after the cursor for characterwise text or below the current line for linewise text.
- `P`: Put before the cursor or above the current line.

Deletes and changes also store text in registers, so a later `p` may put the most recently deleted text rather than an earlier yank. Named registers let you preserve specific text, but begin by watching what the latest operation stored.

:::single-choice{#vim-edit-yank-put-line}
After `yy` yanks the current line, which command puts that line below the current line?

::option[`p`]{#vim-edit-put-below .correct explanation="For linewise yanked text, lowercase `p` puts the stored line below the current line."}
::option[`P`]{#vim-edit-put-above explanation="Uppercase `P` puts linewise text above the current line."}
::option[`u`]{#vim-edit-undo-not-put explanation="Lowercase `u` undoes a change; it does not put the yanked line."}
:::

## Undoing, Redoing, and Repeating

In Normal mode:

- `u`: Undo the most recent change.
- `Ctrl+R`: Redo an undone change.
- `.`: Repeat the most recent change at the current location when applicable.
- `J`: Join the current line with the next line.

Undo history applies to buffer changes, not merely cursor motions. Save checkpoints and review edits rather than depending on an unlimited or permanent undo history.

:::single-choice{#vim-edit-redo-change}
Which Normal-mode command redoes a change that was just undone?

::option[`Ctrl+U`]{#vim-edit-control-u explanation="In Normal mode, `Ctrl+U` scrolls upward by about half a screen; it is not redo."}
::option[`.`]{#vim-edit-dot-repeat explanation="The dot repeats the latest change as a new action rather than traversing forward through undo history."}
::option[`Ctrl+R`]{#vim-edit-control-r .correct explanation="Vim uses `Ctrl+R` in Normal mode to move forward through undo history."}
:::

To practice operators, motions, and recovery on disposable text, try this hands-on lab:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating files, editing text, saving files, and navigating with both vi/vim and nano. This lab will help you apply concepts like deleting, changing, yanking, and putting text in real scenarios.

## Summary

You can now compose Vim edits and recover from mistakes in Normal mode.

1. Combine operators with motions, text objects, and counts.
2. Delete characters or complete lines at a chosen scope.
3. Change text and enter Insert mode for replacement.
4. Yank and put characterwise or linewise text.
5. Undo, redo, or repeat changes deliberately.
