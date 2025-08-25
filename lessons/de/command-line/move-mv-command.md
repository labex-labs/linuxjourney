---
index: 11
lang: "de"
title: "mv (Verschieben)"
meta_title: "mv (Verschieben) - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl mv verwenden, um Dateien/Verzeichnisse zu verschieben und umzubenennen. Verstehen Sie seine Optionen und verhindern Sie Überschreibungen. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "mv Befehl, Linux mv, Dateien verschieben Linux, Dateien umbenennen Linux, Linux Tutorial, Anfänger, Linux Guide"
---

## Lesson Content

Wird zum Verschieben von Dateien und auch zum Umbenennen verwendet. Ziemlich ähnlich dem `cp`-Befehl in Bezug auf Flags und Funktionalität.

Sie können Dateien wie folgt umbenennen:

```bash
mv oldfile newfile
```

Oder Sie können eine Datei tatsächlich in ein anderes Verzeichnis verschieben:

```bash
mv file2 /home/pete/Documents
```

Und mehr als eine Datei verschieben:

```bash
mv file_1 file_2 /somedirectory
```

Sie können auch Verzeichnisse umbenennen:

```bash
mv directory1 directory2
```

Wie `cp` überschreibt `mv` eine Datei oder ein Verzeichnis, wenn es etwas im selben Verzeichnis gibt. Sie können also das Flag `-i` verwenden, um vor dem Überschreiben eine Bestätigung zu erhalten.

```bash
mv -i directory1 directory2
```

Angenommen, Sie wollten eine Datei mit `mv` überschreiben. Sie können auch ein Backup dieser Datei erstellen, und die alte Version wird einfach mit einem `~` umbenannt.

```bash
mv -b directory1 directory2
```

## Exercise

Übung macht den Meister! Praktische Erfahrung ist entscheidend, um Linux-Befehle wie `mv` zu beherrschen. Diese Labs helfen Ihnen, Ihr Verständnis für das Verschieben und Umbenennen von Dateien und Verzeichnissen in einer realen Umgebung zu festigen:

1. **[Linux mv Befehl: Dateien verschieben und umbenennen](https://labex.io/de/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** – Üben Sie die Verwendung des `mv`-Befehls zum Verschieben und Umbenennen von Dateien und Verzeichnissen, einschließlich des Verständnisses seiner verschiedenen Optionen und Verhaltensweisen.
2. **[Dateien und Verzeichnisse organisieren](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Wenden Sie Ihr Wissen über `mv` (zusammen mit `cp` und `rm`) in einer praktischen Herausforderung an, um eine Projektstruktur zu organisieren, Dateien zu verschieben und Verzeichnisse zu bereinigen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Datei- und Verzeichnisverwaltung mit dem `mv`-Befehl aufzubauen.

## Quiz Question

Wie benennt man eine Datei namens `cat` in `dog` um?

## Quiz Answer

mv cat dog