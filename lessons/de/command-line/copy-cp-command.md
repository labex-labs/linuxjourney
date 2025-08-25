---
index: 10
lang: "de"
title: "cp (Kopieren)"
meta_title: "cp (Kopieren) - Befehlszeile"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl cp zum Kopieren von Dateien und Verzeichnissen verwenden. Verstehen Sie Optionen wie -r und Wildcards. Beginnen Sie noch heute Ihre Linux-Reise!"
meta_keywords: "cp Befehl, Dateien kopieren Linux, Linux Tutorial, Linux für Anfänger, cp -r, Linux Wildcards, Linux Anleitung"
---

## Lesson Content

Beginnen wir damit, Kopien dieser Dateien zu erstellen. Ähnlich wie das Kopieren und Einfügen von Dateien in anderen Betriebssystemen bietet uns die Shell eine noch einfachere Möglichkeit dazu.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` ist die Datei, die Sie kopieren möchten, und `/home/pete/Documents/cooldocs` ist der Ort, an den Sie die Datei kopieren.

Sie können mehrere Dateien und Verzeichnisse kopieren sowie Wildcards verwenden. Ein Wildcard ist ein Zeichen, das durch eine musterbasierte Auswahl ersetzt werden kann, was Ihnen mehr Flexibilität bei Suchen bietet. Sie können Wildcards in jedem Befehl für mehr Flexibilität verwenden.

- `*` der Wildcard der Wildcards, er wird verwendet, um alle einzelnen Zeichen oder beliebige Zeichenketten darzustellen.
- `?` wird verwendet, um ein Zeichen darzustellen
- `[]` wird verwendet, um jedes Zeichen innerhalb der Klammern darzustellen

```bash
cp *.jpg /home/pete/Pictures
```

Dies kopiert alle Dateien mit der Erweiterung `.jpg` in Ihrem aktuellen Verzeichnis in das Verzeichnis `Pictures`.

Ein nützlicher Befehl ist die Verwendung des Flags `-r`; dies kopiert die Dateien und Verzeichnisse innerhalb eines Verzeichnisses rekursiv.

Versuchen Sie, ein `cp` auf ein Verzeichnis, das ein paar Dateien enthält, in Ihr Verzeichnis `Documents` durchzuführen. Hat nicht funktioniert, oder? Nun, das liegt daran, dass Sie die Dateien und Verzeichnisse darin auch mit dem Befehl `-r` kopieren müssen.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Eine Sache ist zu beachten: Wenn Sie eine Datei in ein Verzeichnis kopieren, das denselben Dateinamen hat, wird die Datei mit dem überschrieben, was Sie kopieren. Das ist nicht gut, wenn Sie eine Datei haben, die Sie nicht versehentlich überschreiben möchten. Sie können das Flag `-i` (interaktiv) verwenden, um vor dem Überschreiben einer Datei eine Bestätigung anzufordern.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Kopierens von Dateien und Verzeichnissen in Linux zu vertiefen:

1. **[Linux cp Command: File Copying](https://labex.io/de/labs/linux-linux-cp-command-file-copying-209744)** – Üben Sie die grundlegende Verwendung, erweiterte Optionen wie rekursives Kopieren, Beibehalten von Attributen und die Verwendung von Wildcards, um Dateien und Verzeichnisse effizient zu kopieren.
2. **[Organizing Files and Directories](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Üben Sie grundlegende Linux-Dateiverwaltungsfähigkeiten, indem Sie die Befehle `cp`, `mv` und `rm` verwenden, um eine Projektstruktur zu organisieren, Dateien zu verschieben und unnötige Verzeichnisse zu bereinigen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Dateikopierung und -verwaltung unter Linux aufzubauen.

## Quiz Question

Welches Flag müssen Sie angeben, um ein Verzeichnis zu kopieren?

## Quiz Answer

-r
