---
title: "find"
description: "Erfahren Sie, wie Sie den Linux-Befehl 'find' verwenden, um Dateien und Verzeichnisse zu finden. Entdecken Sie grundlegende Suchoptionen und verbessern Sie Ihre Fähigkeiten im Linux-Dateimanagement."
keywords: "Linux find Befehl, Dateien finden Linux, Linux Verzeichnissuche, find Befehl Tutorial, Linux Dateimanagement, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Bei all diesen Dateien, die wir auf dem System haben, kann es ziemlich hektisch werden, eine bestimmte zu finden. Nun, dafür gibt es einen Befehl: `find`!

```bash
find /home -name puppies.jpg
```

Mit `find` müssen Sie das Verzeichnis angeben, in dem Sie suchen möchten, und wonach Sie suchen. In diesem Fall versuchen wir, eine Datei mit dem Namen `puppies.jpg` zu finden.

Sie können angeben, welchen Dateityp Sie finden möchten.

```bash
find /home -type d -name MyFolder
```

Sie sehen, dass ich den Dateityp, den ich finden möchte, als `d` für directory festgelegt habe, und ich suche immer noch nach dem Namen `MyFolder`.

Eine coole Sache ist, dass `find` nicht an dem Verzeichnis aufhört, in dem Sie suchen; es wird auch in allen Unterverzeichnissen suchen, die dieses Verzeichnis möglicherweise hat.

## Exercise

1. Finden Sie eine Datei aus dem Stammverzeichnis, die das Wort "net" enthält.

## Quiz Question

Welche Option sollte ich für `find` angeben, wenn ich nach Namen suchen möchte?

## Quiz Answer

-name
