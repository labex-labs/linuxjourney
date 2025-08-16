---
lang: "de"
title: "cp (Kopieren)"
description: "Erfahren Sie, wie Sie den Linux-Befehl cp zum Kopieren von Dateien und Verzeichnissen verwenden. Verstehen Sie Optionen wie -r und Wildcards. Beginnen Sie noch heute Ihre Linux-Reise!"
keywords: "cp Befehl, Dateien kopieren Linux, Linux Tutorial, Linux für Anfänger, cp -r, Linux Wildcards, Linux Anleitung"
---

## Lesson Content

Fangen wir an, Kopien dieser Dateien zu erstellen. Ähnlich wie beim Kopieren und Einfügen von Dateien in anderen Betriebssystemen bietet uns die Shell eine noch einfachere Möglichkeit dazu.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` ist die Datei, die Sie kopieren möchten, und `/home/pete/Documents/cooldocs` ist der Ort, an den Sie die Datei kopieren.

Sie können mehrere Dateien und Verzeichnisse kopieren sowie Wildcards verwenden. Eine Wildcard ist ein Zeichen, das für eine musterbasierte Auswahl eingesetzt werden kann, was Ihnen mehr Flexibilität bei Suchen bietet. Sie können Wildcards in jedem Befehl für mehr Flexibilität verwenden.

- `*` die Wildcard der Wildcards, sie wird verwendet, um alle einzelnen Zeichen oder beliebige Zeichenketten darzustellen.
- `?` wird verwendet, um ein Zeichen darzustellen
- `[]` wird verwendet, um jedes Zeichen innerhalb der Klammern darzustellen

```bash
cp *.jpg /home/pete/Pictures
```

Dies kopiert alle Dateien mit der Erweiterung `.jpg` in Ihrem aktuellen Verzeichnis in das Verzeichnis `Pictures`.

Ein nützlicher Befehl ist die Verwendung des Flags `-r`; dies kopiert die Dateien und Verzeichnisse innerhalb eines Verzeichnisses rekursiv.

Versuchen Sie, ein `cp` für ein Verzeichnis, das ein paar Dateien enthält, in Ihr Verzeichnis `Documents` durchzuführen. Hat nicht funktioniert, oder? Nun, das liegt daran, dass Sie die Dateien und Verzeichnisse darin auch mit dem Befehl `-r` kopieren müssen.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Eines ist zu beachten: Wenn Sie eine Datei in ein Verzeichnis kopieren, das denselben Dateinamen hat, wird die Datei mit dem überschrieben, was Sie kopieren. Das ist nicht gut, wenn Sie eine Datei haben, die Sie nicht versehentlich überschreiben möchten. Sie können das Flag `-i` (interaktiv) verwenden, um vor dem Überschreiben einer Datei eine Bestätigung anzufordern.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

Kopieren Sie ein paar Dateien; achten Sie darauf, nichts Wichtiges zu überschreiben.

## Quiz Question

Welches Flag müssen Sie angeben, um ein Verzeichnis zu kopieren?

## Quiz Answer

-r
