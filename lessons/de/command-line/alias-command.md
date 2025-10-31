---
index: 18
lang: "de"
title: "Alias"
meta_title: "Alias - Kommandozeile"
meta_description: "Erfahren Sie, wie Sie einen Kommando-Alias unter Linux erstellen und verwalten, um Ihren Workflow zu optimieren. Diese Anleitung behandelt das Erstellen temporärer und permanenter Aliase mit dem alias-Befehl und der .bashrc-Datei."
meta_keywords: "linux alias, alias befehl linux, kommando alias in linux, linux kommando alias, bash alias, unalias befehl, .bashrc, kommandozeile, Linux Tutorial"
---

## Lesson Content

Das Tippen langer oder sich wiederholender Befehle kann mühsam sein. Glücklicherweise können Sie eine Abkürzung, oder ein **Linux-Alias**, erstellen, um Ihre Befehlszeilenerfahrung effizienter zu gestalten. Der Befehl `alias` ermöglicht es Ihnen, einen benutzerdefinierten Namen für einen beliebigen Befehl oder eine Befehlssequenz zu definieren.

### Erstellen eines temporären Alias

Um einen temporären Alias zu erstellen, der für Ihre aktuelle Terminalsitzung gültig ist, geben Sie einfach einen Namen an und setzen ihn gleich der Befehlszeichenfolge.

Um beispielsweise einen Alias namens `ll` für den Befehl `ls -la` zu erstellen, würden Sie die Syntax `alias command linux` wie folgt verwenden:

```bash
alias ll='ls -la'
```

Anstatt nun `ls -la` einzugeben, können Sie einfach `ll` eingeben, und der gleiche Befehl wird ausgeführt. Dies ist eine einfache, aber leistungsstarke Methode, um Ihre Shell anzupassen.

### Einen Alias dauerhaft machen

Ein temporärer Alias verschwindet, sobald Sie Ihr Terminal schließen oder Ihr System neu starten. Um einen **command alias in linux** dauerhaft zu machen, müssen Sie ihn in die Konfigurationsdatei Ihrer Shell eintragen. Für die Bash-Shell ist diese Datei typischerweise `~/.bashrc`.

1. Öffnen Sie die Datei in einem Texteditor: `nano ~/.bashrc`
2. Fügen Sie Ihre Alias-Definition in die Datei ein, genau so, wie Sie sie in der Befehlszeile eingegeben haben:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Speichern Sie die Datei und beenden Sie den Editor.

Damit die Änderungen wirksam werden, müssen Sie entweder das Terminal schließen und neu öffnen oder die Shell anweisen, die Konfigurationsdatei mit dem Befehl `source` neu zu laden:

```bash
source ~/.bashrc
```

Ihr **Linux command alias** ist nun bei jedem Start einer neuen Terminalsitzung verfügbar.

### Entfernen eines Alias

Wenn Sie einen Alias nicht mehr benötigen, können Sie ihn mit dem Befehl `unalias` entfernen. Dadurch wird er aus Ihrer aktuellen Sitzung entfernt.

```bash
unalias ll
```

Um einen permanenten Alias zu entfernen, müssen Sie auch dessen Definition aus Ihrer `~/.bashrc`-Datei löschen.

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Welcher Befehl wird verwendet, um einen Alias zu erstellen? Bitte antworten Sie in englischen Kleinbuchstaben.

## Quiz Answer

alias
