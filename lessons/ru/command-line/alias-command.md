---
index: 18
lang: "ru"
title: "alias"
meta_title: "alias - Командная строка"
meta_description: "Узнайте, как создавать и управлять псевдонимами Linux для часто используемых команд. Откройте для себя временную и постоянную настройку псевдонимов в .bashrc. Повысьте эффективность работы с командной строкой!"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

Иногда ввод команд может быть очень монотонным, или если вам нужно много раз вводить длинную команду, лучше всего иметь для этого псевдоним (alias). Чтобы создать псевдоним для команды, вы просто указываете имя псевдонима и присваиваете ему команду.

```bash
alias foobar='ls -la'
```

Теперь, вместо того чтобы вводить `ls -la`, вы можете ввести `foobar`, и это выполнит команду — довольно удобно. Имейте в виду, что эта команда не сохранит ваш псевдоним после перезагрузки, поэтому вам нужно будет добавить постоянный псевдоним в:

```plaintext
~/.bashrc
```

или аналогичные файлы, если вы хотите, чтобы он сохранялся после перезагрузки.

Вы можете удалить псевдонимы с помощью команды `unalias`:

```bash
unalias foobar
```

## Exercise

Создайте пару псевдонимов, затем удалите их.

Для дополнительной практической отработки основ командной строки Linux изучите эти интерактивные лаборатории:

- [Linux Directory Navigation](https://labex.io/ru/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/ru/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

Какая команда используется для создания псевдонима?

## Quiz Answer

alias
