---
lesson_id: "vim-search-patterns"
course_id: "advanced-text-fu"
lang: "en"
order_index: 4
title: "Vim Search Patterns"
description: "Learn how to search forward or backward in Vim and repeat, refine, or clear pattern matches."
meta_title: "Vim Search Patterns - Advanced Text-Fu"
meta_description: "Learn how to perform a forward and backward Vim search using patterns. Master Vim lookup techniques to quickly find text, and navigate results with 'n' and 'N'."
meta_keywords: "Vim search, vim lookup, Vim commands, Linux text editor, Vim tutorial, Vim guide, search patterns"
---

Vim searches from the current cursor position using patterns. Begin in Normal mode, enter a forward or backward search, and then repeat matches without retyping the pattern.

## Searching Forward

In Normal mode, type `/`, enter a pattern, and press Enter. Vim moves to the next match after the cursor:

```vim
/pretty
```

Searches use Vim's regular-expression syntax, so characters such as `.`, `*`, `[`, and `\` can have special meaning. Use `\V` at the start when the rest of a pattern should be treated as very nomagic, or escape special characters deliberately.

:::single-choice{#vim-search-forward-key}
From Normal mode, which command starts a forward search for `pretty`?

::option[`?pretty` followed by Enter]{#vim-backward-pretty explanation="A question mark begins a backward search from the current cursor position."}
::option[`/pretty` followed by Enter]{#vim-forward-pretty .correct explanation="A slash begins a forward search, and Enter submits the pattern."}
::option[`:pretty` followed by Enter]{#vim-command-pretty explanation="A colon enters Command-line mode for an Ex command; `pretty` is not introduced as a search this way."}
:::

## Searching Backward

Type `?`, enter a pattern, and press Enter to move to the preceding match before the cursor:

```vim
?pretty
```

This does not inherently mean “the final match in the file.” The result depends on the current cursor position. With Vim's default `wrapscan` setting, a search can wrap at the beginning or end; `:set nowrapscan` disables that wrapping.

:::single-choice{#vim-search-backward-key}
Which Normal-mode search prefix looks toward earlier text from the cursor?

::option[`/`]{#vim-slash-forward explanation="A slash searches forward from the cursor rather than toward preceding text."}
::option[`?`]{#vim-question-backward .correct explanation="A question mark starts a backward pattern search from the current cursor position."}
::option[`:`]{#vim-colon-command explanation="A colon starts an Ex command line. It is not the backward-search prefix."}
:::

## Repeating a Search

After either kind of search:

- Press `n` to repeat in the original search direction.
- Press `N` to repeat in the opposite direction.

Therefore, after `/pretty`, `n` moves forward and `N` backward. After `?pretty`, `n` moves backward and `N` forward.

:::single-choice{#vim-repeat-backward-search}
After running `?error`, which key repeats the search in the same backward direction?

::option[`n`]{#vim-same-question-search .correct explanation="Lowercase `n` repeats the most recent search in its original direction, which is backward here."}
::option[`N`]{#vim-opposite-question-search explanation="Uppercase `N` reverses the original search direction, so it would move forward after a `?` search."}
::option[`/`]{#vim-new-forward-search explanation="A slash starts a new forward search and waits for a pattern rather than repeating the previous one."}
:::

## Searching for the Word under the Cursor

In Normal mode, place the cursor on a word and use:

- `*` to search forward for that whole word.
- `#` to search backward for that whole word.

These commands set the latest search pattern, so `n` and `N` can continue from it.

:::single-choice{#vim-current-word-forward}
Which Normal-mode key searches forward for the whole word under the cursor?

::option[`#`]{#vim-hash-current-word explanation="The hash key searches backward for the word under the cursor."}
::option[`*`]{#vim-star-current-word .correct explanation="The star command builds a whole-word pattern from the word under the cursor and searches forward."}
::option[`n`]{#vim-repeat-current-pattern explanation="The `n` key repeats an existing search; it does not first create a pattern from the current word."}
:::

## Controlling Case and Highlighting

Vim options can change case behavior:

- `:set ignorecase` makes searches ignore case.
- `:set smartcase` makes an uppercase character restore case sensitivity when `ignorecase` is also set.
- `\c` inside a pattern forces that search to ignore case.
- `\C` forces that search to respect case.

For example, `/\cerror` matches `error`, `Error`, and `ERROR` regardless of the current case options.

When search highlighting is enabled, `:nohlsearch` clears the current visual highlights without deleting the search pattern. The next search or repeat can highlight matches again.

:::single-choice{#vim-force-case-insensitive}
Which pattern forces one Vim search for `error` to ignore case regardless of the current case options?

::option[`/\Cerror`]{#vim-pattern-match-case explanation="Uppercase `\C` forces case-sensitive matching, the opposite behavior."}
::option[`/:error`]{#vim-pattern-colon-error explanation="A colon inside this pattern is a literal character here and does not select case handling."}
::option[`/\cerror`]{#vim-pattern-ignore-case .correct explanation="The `\c` atom makes that search case-insensitive, so capitalization variants can match."}
:::

To practice Vim navigation and search in a controlled file, try this hands-on lab:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating, editing, saving, and navigating text files with Vim and Nano.

## Summary

You can now search a Vim buffer and move between matches predictably.

1. Start forward searches with `/` and backward searches with `?`.
2. Repeat in the same direction with `n` or the opposite direction with `N`.
3. Search for the whole word under the cursor with `*` or `#`.
4. Control case behavior for one pattern or through options.
5. Clear highlights without losing the current search pattern.
