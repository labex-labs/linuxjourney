---
index: 11
lang: "de"
title: "mv (Verschieben)"
meta_title: "mv (Verschieben) - Kommandozeile"
meta_description: "Ein umfassender Leitfaden zum mv-Befehl in Linux. Erfahren Sie, wie Sie den bash mv-Befehl zum Verschieben und Umbenennen von Dateien und Verzeichnissen verwenden, Optionen wie linux mv -t nutzen und versehentliches Überschreiben verhindern."
meta_keywords: "mv Befehl, mv Befehl in linux, linux mv, bash mv, mv -r linux, linux mv -t, Dateien verschieben, Dateien umbenennen, linux Kommandozeile"
---

## Lesson Content

Der `mv`-Befehl, kurz für „move“ (verschieben), ist ein grundlegendes Dienstprogramm in jeder Linux-Umgebung. Er dient zwei Hauptzwecken: dem Umbenennen von Dateien oder Verzeichnissen und dem Verschieben dieser an einen anderen Ort. Seine Funktionalität ähnelt in vielerlei Hinsicht der des `cp`-Befehls.

### Dateien und Verzeichnisse umbenennen

Eine der häufigsten Anwendungen des `mv command in linux` ist das Umbenennen. Die Syntax ist unkompliziert: Sie geben den alten Namen und den neuen Namen an.

Um eine Datei umzubenennen:

```bash
mv alte_datei neue_datei
```

Dieselbe Logik gilt für das Umbenennen von Verzeichnissen:

```bash
mv alter_verzeichnisname neuer_verzeichnisname
```

### Dateien und Verzeichnisse verschieben

Die andere Kernfunktion des `mv`-Befehls besteht darin, Elemente von einem Ort zum anderen zu verschieben.

Um eine einzelne Datei in ein anderes Verzeichnis zu verschieben:

```bash
mv datei2 /home/pete/Dokumente
```

Sie können auch mehrere Dateien gleichzeitig verschieben. Listen Sie einfach alle Quelldateien gefolgt vom Zielverzeichnis auf:

```bash
mv datei_1 datei_2 /ein_verzeichnis
```

Eine nützliche Option hierfür ist `linux mv -t`, mit der Sie zuerst das Zielverzeichnis angeben können. Dies kann beim Verschieben vieler Dateien übersichtlicher sein.

```bash
mv -t /ein_verzeichnis datei_1 datei_2
```

Im Gegensatz zum `cp`-Befehl benötigen Sie kein `-r`-Flag, um ein Verzeichnis zu verschieben. Der `bash mv`-Befehl behandelt Verzeichnisse standardmäßig. Obwohl einige Benutzer nach `mv -r linux` suchen, ist diese Option nicht erforderlich, um Verzeichnisse mit `mv` zu verschieben.

### Wichtige Optionen für den mv-Befehl

Standardmäßig überschreibt `mv` eine Datei ohne Warnung, wenn Sie sie an ein Ziel verschieben, an dem bereits eine Datei mit demselben Namen existiert. Um versehentlichen Datenverlust zu vermeiden, können Sie die folgenden Optionen verwenden:

- **-i (interaktiv)**: Dies ist eine entscheidende Sicherheitsfunktion. Sie fordert Sie zur Bestätigung auf, bevor eine vorhandene Datei überschrieben wird.

  ```bash
  mv -i quell_datei ziel_verzeichnis
  ```

````

- **-b (backup)**: Wenn Sie beabsichtigen, eine Datei zu überschreiben, aber die alte Version behalten möchten, erstellt diese Option eine Sicherungskopie der Zieldatei. Die Sicherungskopie wird typischerweise mit einem Tilde (`~`) Suffix umbenannt.

  ```bash
mv -b datei1 verzeichnis_mit_datei1
````

- **-v (verbose)**: Diese Option bewirkt, dass der `mv`-Befehl ausgibt, was er tut, und jede verschobene oder umbenannte Datei anzeigt.

  ```bash
  mv -v datei1 datei2 /ein_verzeichnis
  ```

```

Die Beherrschung des `mv command` ist für eine effiziente Dateiverwaltung auf der Kommandozeile unerlässlich.

## Exercise
Übung macht den Meister! Praktische Erfahrung ist entscheidend, um Linux-Befehle wie `mv` zu beherrschen. Diese Labs helfen Ihnen, Ihr Verständnis für das Verschieben und Umbenennen von Dateien und Verzeichnissen in einer realen Umgebung zu festigen:

1.  **[Linux mv Befehl: Dateien verschieben und umbenennen](https://labex.io/de/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Üben Sie die Verwendung des `mv`-Befehls zum Verschieben und Umbenennen von Dateien und Verzeichnissen, einschließlich des Verständnisses seiner verschiedenen Optionen und Verhaltensweisen.
2.  **[Dateien und Verzeichnisse organisieren](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** - Wenden Sie Ihr Wissen über `mv` (zusammen mit `cp` und `rm`) in einer praktischen Herausforderung an, um eine Projektstruktur zu organisieren, Dateien zu verschieben und Verzeichnisse aufzuräumen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Datei- und Verzeichnisverwaltung mit dem `mv`-Befehl aufzubauen.

## Quiz Question
Wie würden Sie mit dem `mv`-Befehl eine Datei namens `cat` in `dog` umbenennen? Bitte geben Sie den vollständigen Befehl an. Hinweis: Die Antwort ist groß-/kleingeschrieben und sollte in Kleinbuchstaben auf Englisch eingegeben werden.

## Quiz Answer
mv cat dog
```
