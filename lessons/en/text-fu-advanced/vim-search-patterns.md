---
index: 4
lang: "en"
title: "Vim Search Patterns"
meta_title: "Vim Search Patterns - Advanced Text-Fu"
meta_description: "Learn Vim search patterns: forward (/) and backward (?) search. Navigate results with 'n' and 'N'. Improve your Vim skills today!"
meta_keywords: "Vim search, Vim commands, Linux text editor, Vim tutorial, Vim guide, beginner Vim"
---

## Lesson Content

To search for an expression, just type the `/` key and then your search term while you are in a Vim session. Once you hit Enter, you can press `n` to go forward or `N` to go backward in your search results.

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

The `?` search command will search the text file backward. So, in the previous example, the last "pretty" would come up first.

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of text editing and searching in Linux:

1. **[Edit Text Files in Linux with Vim and Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practice creating, editing, saving, and navigating text files with Vim and Nano. This lab will help you become proficient with essential text editing tools, including search functionalities.

This lab will help you apply the concepts in real scenarios and build confidence with text file manipulation in Linux.

## Quiz Question

What key is used to search in Vim?

## Quiz Answer

/
