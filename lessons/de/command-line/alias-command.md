---
index: 18
lang: "de"
title: "alias"
meta_title: "alias - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie Linux-Aliase für gängige Befehle erstellen und verwalten. Entdecken Sie die Einrichtung temporärer und permanenter Aliase in .bashrc. Verbessern Sie Ihre Effizienz in der Befehlszeile!"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, Befehlszeile, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Manchmal kann das Tippen von Befehlen sehr repetitiv werden, oder wenn Sie einen langen Befehl viele Male eingeben müssen, ist es am besten, einen Alias dafür zu verwenden. Um einen Alias für einen Befehl zu erstellen, geben Sie einfach einen Aliasnamen an und weisen ihn dem Befehl zu.

```bash
alias foobar='ls -la'
```

Anstatt `ls -la` einzugeben, können Sie jetzt `foobar` eingeben, und es wird dieser Befehl ausgeführt – ziemlich clever. Beachten Sie, dass dieser Befehl Ihren Alias nach einem Neustart nicht speichert. Wenn Sie ihn nach einem Neustart beibehalten möchten, müssen Sie einen permanenten Alias hinzufügen in:

```plaintext
~/.bashrc
```

oder ähnlichen Dateien.

Sie können Aliase mit dem Befehl `unalias` entfernen:

```bash
unalias foobar
```

## Exercise

Obwohl es keine spezifischen Labs für dieses Thema gibt, empfehlen wir Ihnen, den umfassenden [Linux-Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Welcher Befehl wird verwendet, um einen Alias zu erstellen?

## Quiz Answer

alias