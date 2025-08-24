---
index: 18
lang: "de"
title: "alias"
meta_title: "alias - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie Linux-Aliase für gängige Befehle erstellen und verwalten. Entdecken Sie die temporäre und permanente Alias-Einrichtung in .bashrc. Verbessern Sie Ihre Effizienz in der Befehlszeile!"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

Manchmal kann das Tippen von Befehlen sehr repetitiv werden, oder wenn Sie einen langen Befehl viele Male eingeben müssen, ist es am besten, einen Alias dafür zu verwenden. Um einen Alias für einen Befehl zu erstellen, geben Sie einfach einen Aliasnamen an und weisen ihn dem Befehl zu.

```bash
alias foobar='ls -la'
```

Anstatt `ls -la` einzugeben, können Sie nun `foobar` eingeben, und es wird dieser Befehl ausgeführt – ziemlich clever. Beachten Sie, dass dieser Befehl Ihren Alias nach einem Neustart nicht speichert. Sie müssen also einen permanenten Alias hinzufügen in:

```plaintext
~/.bashrc
```

oder ähnlichen Dateien, wenn Sie möchten, dass er nach einem Neustart bestehen bleibt.

Sie können Aliase mit dem Befehl `unalias` entfernen:

```bash
unalias foobar
```

## Exercise

Erstellen Sie ein paar Aliase und entfernen Sie sie dann wieder.

Für zusätzliche praktische Übungen zu den Grundlagen der Linux-Befehlszeile erkunden Sie diese interaktiven Labs:

- [Linux Directory Navigation](https://labex.io/de/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/de/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

Welcher Befehl wird verwendet, um einen Alias zu erstellen?

## Quiz Answer

alias
