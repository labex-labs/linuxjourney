---
lesson_id: "man-command"
course_id: "command-line"
lang: "en"
order_index: 16
title: "man"
description: "Learn how to open, navigate, search, and select sections of installed manual pages."
meta_title: "man - Command Line"
meta_description: "Learn the Linux man command with examples for reading manual pages, searching inside man pages, understanding sections, and finding command options."
meta_keywords: "man command, linux man pages, command manual, man ls, man sections, search man page, command line help"
---

Many Linux commands, interfaces, configuration files, and administrative tools have installed reference documentation called manual pages, or man pages. The `man` command finds and displays those pages.

## Opening a Manual Page

Pass a topic name to `man`. For example, open the page for `ls` with:

```bash
$ man ls
```

Manual pages commonly include a synopsis, description, options, related files, and cross-references, although the exact sections vary.

:::single-choice{#open-ls-manual}
Which command opens the installed manual page for `ls`?

::option[`help ls`]{#help-ls explanation="Bash `help` documents shell builtins and normally does not open the external `ls` manual page."}
::option[`man ls`]{#manual-ls-page .correct explanation="`man` looks up the topic `ls` in the manual database and displays the matching page."}
::option[`ls --help`]{#ls-usage explanation="This asks `ls` for its own usage summary. It does not open the installed manual page."}
:::

## Navigating and Searching a Page

On many systems, `man` displays pages through a pager such as `less`. While a page is open, you can scroll with arrow or page keys and use these controls:

Inside a man page:

- Type `/pattern` and press Enter to search forward.
- Press `n` to repeat the search in the same direction.
- Press `N` to repeat it in the opposite direction.
- Press `q` to quit.

The pager can differ by system or environment, so its exact keys are not guaranteed everywhere. The controls above apply to the common `less` setup.

:::single-choice{#search-man-page}
With a man page open in `less`, what starts a forward search for `--recursive`?

::option[Type `?--recursive` and press Enter.]{#backward-man-search explanation="A question mark begins a backward search. It looks in the opposite direction from the one requested."}
::option[Type `/--recursive` and press Enter.]{#forward-man-search .correct explanation="A slash begins a forward search in `less`, and Enter submits the pattern."}
::option[Type `n--recursive` and press Enter.]{#repeat-man-search explanation="The `n` key repeats an existing search. It does not introduce a new search pattern this way."}
:::

:::single-choice{#leave-man-page}
With a man page open in the usual pager, which key returns to the shell?

::option[`G`]{#man-page-end explanation="Uppercase `G` moves to the end of the page in `less`. It does not close the pager."}
::option[`n`]{#next-man-match explanation="The `n` key repeats the most recent search. It keeps the manual page open."}
::option[`q`]{#quit-man .correct explanation="The `q` key quits the usual pager and returns control to the shell."}
:::

## Selecting a Manual Section

The manual is organized into numbered sections. Common sections include:

- `1`: User commands.
- `2`: System calls.
- `3`: Library functions.
- `5`: File formats.
- `8`: System administration commands.

The same topic can appear in more than one section. Put the section before the topic to select one explicitly:

```bash
$ man 5 passwd
$ man 1 passwd
```

The first command opens the `passwd` file-format page from section 5. The second opens the user command page from section 1. References such as `passwd(5)` use the same `topic(section)` notation.

:::single-choice{#open-passwd-file-format}
Which command opens the section 5 page that documents the `passwd` file format?

::option[`man passwd 5`]{#section-after-topic explanation="The section selector belongs before the topic in this command form. This operand order does not request `passwd(5)`."}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="Placing section `5` before `passwd` selects the file-format page specifically."}
::option[`man 1 passwd`]{#passwd-command-page explanation="Section 1 contains user commands, so this selects the `passwd` command page rather than the file-format page."}
:::

## When a Page Is Missing

Not every command name has a separately installed manual page. If `man` reports that no entry exists:

- Run `type NAME` to see how Bash resolves the name.
- Use `help NAME` when it is a Bash builtin.
- Try `NAME --help` when an external program supports that convention.
- Check whether your distribution offers a separate documentation package.

:::single-choice{#missing-builtin-manual}
`type cd` reports that `cd` is a Bash builtin, and no separate man page is available. Which command should you try next?

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis` summarizes entries from the manual database. It cannot supply a missing dedicated page for the builtin."}
::option[`file cd`]{#file-cd-name explanation="`file` classifies filesystem objects, but `cd` is being resolved as a shell builtin rather than a pathname here."}
::option[`help cd`]{#builtin-cd-help .correct explanation="Bash's `help` builtin provides the shell's own documentation for `cd`."}
:::

## Summary

You can now locate and navigate installed manual documentation.

1. Open a page by topic name.
2. Search and move through a page in the usual pager.
3. Quit the pager and return to the shell.
4. Select a numbered manual section.
5. Choose another help source when a page is unavailable.
