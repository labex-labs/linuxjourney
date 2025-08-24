---
index: 14
lang: "de"
title: "find"
meta_title: "find - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'find' verwenden, um Dateien und Verzeichnisse zu finden. Entdecken Sie grundlegende Suchoptionen und verbessern Sie Ihre Linux-Dateiverwaltungsfähigkeiten."
meta_keywords: "Linux find Befehl, Dateien finden Linux, Linux Verzeichnissuche, find Befehl Tutorial, Linux Dateiverwaltung, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Bei all den Dateien, die wir auf dem System haben, kann es etwas chaotisch werden, eine bestimmte zu finden. Nun, dafür gibt es einen Befehl, den wir verwenden können: `find`!

```bash
find /home -name puppies.jpg
```

Mit `find` müssen Sie das Verzeichnis angeben, in dem Sie suchen möchten, und wonach Sie suchen. In diesem Fall versuchen wir, eine Datei mit dem Namen `puppies.jpg` zu finden.

Sie können angeben, welchen Dateityp Sie suchen.

```bash
find /home -type d -name MyFolder
```

Sie sehen, dass ich den Dateityp, den ich suche, als `d` für Verzeichnis festgelegt habe, und ich suche immer noch nach dem Namen `MyFolder`.

Eine coole Sache ist, dass `find` nicht bei dem Verzeichnis aufhört, in dem Sie suchen; es wird auch in allen Unterverzeichnissen suchen, die dieses Verzeichnis möglicherweise hat.

## Exercise

1. Finden Sie eine Datei aus dem Stammverzeichnis, die das Wort "net" enthält.

Für praktische Übungen mit dem `find`-Befehl probieren Sie dieses interaktive Labor aus:

- [Linux find Command: File Searching](https://labex.io/de/labs/linux-linux-find-command-file-searching-219191)

## Quiz Question

Welche Option sollte ich für `find` angeben, wenn ich nach Namen suchen möchte?

## Quiz Answer

-name
