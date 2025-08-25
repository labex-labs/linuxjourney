---
index: 14
lang: "de"
title: "find"
meta_title: "find - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl 'find' verwenden, um Dateien und Verzeichnisse zu finden. Entdecken Sie grundlegende Suchoptionen und verbessern Sie Ihre Linux-Dateiverwaltungsfähigkeiten."
meta_keywords: "Linux find Befehl, Dateien finden Linux, Linux Verzeichnissuche, find Befehl Tutorial, Linux Dateiverwaltung, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Bei all den Dateien, die wir auf dem System haben, kann es etwas hektisch werden, eine bestimmte zu finden. Nun, dafür gibt es einen Befehl: `find`!

```bash
find /home -name puppies.jpg
```

Mit `find` müssen Sie das Verzeichnis angeben, in dem Sie suchen möchten, und wonach Sie suchen. In diesem Fall versuchen wir, eine Datei mit dem Namen `puppies.jpg` zu finden.

Sie können angeben, welchen Dateityp Sie finden möchten.

```bash
find /home -type d -name MyFolder
```

Sie sehen, dass ich den Dateityp, den ich finden möchte, als `d` für Verzeichnis festgelegt habe, und ich suche immer noch nach dem Namen `MyFolder`.

Eine coole Sache ist, dass `find` nicht an dem Verzeichnis aufhört, in dem Sie suchen; es wird auch in allen Unterverzeichnissen suchen, die dieses Verzeichnis möglicherweise hat.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für das Auffinden von Dateien und Verzeichnissen unter Linux zu vertiefen:

1. **[Linux find Befehl: Dateisuche](https://labex.io/de/labs/linux-linux-find-command-file-searching-219191)** – Dieses Lab bietet eine Einführung in den Befehl `find`, ein vielseitiges Dienstprogramm zum Suchen und Auffinden von Dateien und Verzeichnissen basierend auf verschiedenen Kriterien. Sie üben die Verwendung von `find`, um bestimmte Dateien zu finden.
2. **[Kritische Systemressourcen entdecken](https://labex.io/de/labs/linux-discover-critical-system-resources-388032)** – Lernen Sie wichtige Linux-Befehle zum Auffinden von Dateien und ausführbaren Dateien, einschließlich `find`. Sie üben die effiziente Navigation im Dateisystem und das Auffinden kritischer Systemressourcen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die effektive Nutzung des `find`-Befehls aufzubauen.

## Quiz Question

Welche Option sollte ich für `find` angeben, wenn ich nach Namen suchen möchte?

## Quiz Answer

-name
