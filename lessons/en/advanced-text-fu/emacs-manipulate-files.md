---
lesson_id: "emacs-manipulate-files"
course_id: "advanced-text-fu"
lang: "en"
order_index: 10
title: "Emacs Manipulate Files"
description: "Learn how to visit, save, rename, revisit, and review file-backed buffers in Emacs."
meta_title: "Emacs Manipulate Files - Advanced Text-Fu"
meta_description: "Learn Emacs file manipulation: save, save as, and open files using C-x C-s, C-x C-w, and C-x C-f commands. Master essential Emacs file operations!"
meta_keywords: "Emacs, Emacs save file, Emacs open file, Emacs tutorial, Linux commands, beginner Emacs, Emacs guide"
---

Emacs visits files in buffers. Editing changes the buffer first; saving writes its current contents to the associated pathname. Read minibuffer messages because permissions, conflicting disk changes, or other errors can prevent a write.

## Visiting a File

Use `C-x C-f`, which runs `find-file`, then enter a pathname in the minibuffer and press Enter:

```text
C-x C-f
```

Emacs opens an existing readable file in a buffer or prepares a new file-visiting buffer when the pathname is missing. In the second case, no disk file exists until a save succeeds.

You can use Tab completion while entering a pathname. Visiting a directory normally opens Dired, Emacs's directory editor, rather than treating the directory as a text file.

:::single-choice{#emacs-find-file-key}
Which Emacs key sequence prompts for a pathname and visits it?

::option[`C-x C-s`]{#emacs-file-save explanation="This saves the current file-visiting buffer and does not prompt to visit another pathname."}
::option[`C-x C-c`]{#emacs-file-exit explanation="This begins exiting Emacs rather than opening a file."}
::option[`C-x C-f`]{#emacs-find-file .correct explanation="This runs `find-file`, prompting in the minibuffer for the pathname to visit."}
:::

:::single-choice{#emacs-find-missing-file}
When `C-x C-f` visits a pathname that does not exist, when is the disk file normally created?

::option[Only after the new buffer is successfully saved.]{#emacs-file-created-on-save .correct explanation="The buffer can hold edits before any file exists, and saving performs the creation."}
::option[Immediately when the pathname is entered.]{#emacs-file-created-immediately explanation="Emacs first creates a buffer associated with the new pathname; disk creation is deferred."}
::option[Only after Emacs itself is closed.]{#emacs-file-created-on-exit explanation="Exiting can prompt to save, but file creation is tied to a successful save rather than necessarily to closing Emacs."}
:::

## Saving the Current Buffer

Use `C-x C-s`, which runs `save-buffer`, to save the current file-visiting buffer:

```text
C-x C-s
```

If the buffer has no associated filename, Emacs prompts for one. A successful write clears the buffer's modified indicator; a failure leaves the unsaved data in the buffer and reports an error.

:::single-choice{#emacs-save-current-buffer}
Which key sequence saves the current file-visiting buffer?

::option[`C-x C-s`]{#emacs-save-buffer-key .correct explanation="`C-x C-s` runs `save-buffer` for the current buffer."}
::option[`C-x C-w`]{#emacs-write-file-key explanation="This prompts for another filename and changes which file the buffer visits."}
::option[`C-x s`]{#emacs-save-some-key explanation="This checks multiple file-visiting buffers and prompts about saving them rather than targeting only the current one."}
:::

## Writing under Another Name

Use `C-x C-w`, which runs `write-file`, to prompt for a pathname, write the buffer there, and make the buffer visit that new file:

```text
C-x C-w
```

This is the Emacs “Save As” behavior. It differs from merely writing a separate copy while continuing to visit the original pathname.

:::single-choice{#emacs-write-file-as}
Which key sequence performs the usual Save As operation for the current buffer?

::option[`C-x C-f`]{#emacs-find-file-other explanation="This visits a file, potentially switching to another buffer; it is not Save As for the current buffer."}
::option[`C-x k`]{#emacs-write-as-kill-buffer explanation="This asks to kill a buffer and can prompt about unsaved changes; it does not save under a new name."}
::option[`C-x C-w`]{#emacs-write-file-answer .correct explanation="`write-file` writes to the chosen pathname and makes the buffer visit that file."}
:::

## Reviewing Several Modified Buffers

Use `C-x s`, which runs `save-some-buffers`, to examine modified file-visiting buffers:

```text
C-x s
```

Emacs normally asks whether to save each eligible modified buffer. Read the buffer name and answer deliberately; this is not an unconditional save-all shortcut.

:::single-choice{#emacs-save-some-buffers}
What does `C-x s` normally do?

::option[Prompts about saving modified file-visiting buffers.]{#emacs-prompt-save-some .correct explanation="`save-some-buffers` reviews eligible modified buffers and asks which should be written."}
::option[Silently saves every buffer without showing names.]{#emacs-silent-save-all explanation="The normal interactive command prompts rather than unconditionally writing every buffer."}
::option[Closes every buffer after saving the current one.]{#emacs-close-all-buffers explanation="The command concerns saving multiple buffers and does not normally close them."}
:::

## Reverting from Disk

If a file changed on disk and you intentionally want to discard the buffer's current contents, run `M-x revert-buffer` and review the confirmation prompt. Reverting can destroy unsaved buffer edits, so use it only after confirming which source should win.

To compare before deciding, save a separate copy or use version-control and diff tools. Avoid treating reload operations as harmless when the buffer is modified.

## Summary

You can now manage file-backed buffers without confusing visits and writes.

1. Visit a pathname with `C-x C-f`.
2. Create a missing file only when its buffer is saved.
3. Save the current buffer with `C-x C-s`.
4. Save under a new visited name with `C-x C-w`.
5. Review several modified buffers with `C-x s`.
