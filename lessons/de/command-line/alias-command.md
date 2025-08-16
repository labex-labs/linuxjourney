---
title: "Alias"
description: "Erfahren Sie, wie Sie Linux-Aliase für gängige Befehle erstellen und verwalten. Entdecken Sie die temporäre und permanente Alias-Einrichtung in .bashrc. Verbessern Sie Ihre Effizienz in der Befehlszeile!"
keywords: "Linux-Alias, Bash-Alias, unalias-Befehl, .bashrc, Linux-Tutorial, Befehlszeile, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Manchmal kann das Tippen von Befehlen sehr repetitiv sein, oder wenn Sie einen langen Befehl viele Male eingeben müssen, ist es am besten, einen Alias dafür zu haben. Um einen Alias für einen Befehl zu erstellen, geben Sie einfach einen Alias-Namen an und weisen ihn dem Befehl zu.

```bash
alias foobar='ls -la'
```

Anstatt nun `ls -la` einzugeben, können Sie `foobar` eingeben, und dieser Befehl wird ausgeführt – ziemlich praktisch. Beachten Sie, dass dieser Befehl Ihren Alias nach einem Neustart nicht speichert. Sie müssen also einen permanenten Alias hinzufügen in:

```plaintext
~/.bashrc
```

oder ähnlichen Dateien, wenn Sie möchten, dass er nach einem Neustart bestehen bleibt.

Sie können Aliase mit dem Befehl `unalias` entfernen:

```bash
unalias foobar
```

## Exercise

Erstellen Sie ein paar Aliase und entfernen Sie sie dann.

## Quiz Question

Welcher Befehl wird verwendet, um einen Alias zu erstellen?

## Quiz Answer

alias
