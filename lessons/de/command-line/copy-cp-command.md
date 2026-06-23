---
index: 10
lang: "de"
title: "cp (Kopieren)"
meta_title: "cp (Kopieren) - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl cp mit Beispielen zum Kopieren von Dateien, Verzeichnissen, mehreren Dateien, Wildcards, Backups und Optionen wie cp -r, cp -i und cp -p."
meta_keywords: "linux cp befehl, cp befehl, dateien kopieren linux, cp -r, cp -i, cp -p, cp -a, cp -u, rekursives kopieren, linux wildcards"
---

## Lesson Content

Der Befehl `cp` ist das Standardwerkzeug zum Kopieren von Dateien und Verzeichnissen unter Linux. Er erstellt eine neue Kopie und lässt die Originaldatei unverändert. Die Grundsyntax lautet:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Sie können eine Datei in eine andere Datei kopieren, eine oder mehrere Dateien in ein Verzeichnis oder mit der richtigen Option einen gesamten Verzeichnisbaum.

### Grundlegendes Kopieren von Dateien

Um eine Datei zu kopieren, geben Sie die Quelldatei und das Zielverzeichnis oder den Zielpfad an.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

In diesem Beispiel ist `mycoolfile` die Quelldatei und `/home/pete/Documents/cooldocs` das Zielverzeichnis. Sie können auch eine Datei kopieren und ihr im Ziel einen neuen Namen geben.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

Wenn das Ziel ein vorhandenes Verzeichnis ist, behält die kopierte Datei ihren ursprünglichen Namen. Wenn das Ziel ein Dateiname ist, erstellt `cp` eine Kopie mit diesem neuen Namen.

### Mehrere Dateien in ein Verzeichnis kopieren

Um mehrere Dateien in dasselbe Verzeichnis zu kopieren, listen Sie zuerst alle Quellen auf und setzen das Zielverzeichnis an das Ende.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

Das letzte Argument muss ein Verzeichnis sein, wenn Sie mehr als eine Quelle angeben.

### Verwendung von Wildcards für Massenkopien

Wildcards sind spezielle Zeichen, die Ihnen helfen, mehrere Dateien anhand von Mustern auszuwählen und bieten große Flexibilität.

- `*`: Passt auf eine beliebige Zeichenfolge.
- `?`: Passt auf genau ein einzelnes Zeichen.
- `[]`: Passt auf eines der in den Klammern eingeschlossenen Zeichen.

Zum Beispiel, um alle JPEG-Bilder von Ihrem aktuellen Ort in das Verzeichnis `Pictures` zu kopieren:

```bash
$ cp *.jpg /home/pete/Pictures
```

Sie können die passenden Dateien vor dem Kopieren anzeigen lassen:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

### Verzeichnisse rekursiv kopieren

Wenn Sie versuchen, ein Verzeichnis mit `cp` ohne Optionen zu kopieren, erhalten Sie einen Fehler. Um ein Verzeichnis und seinen gesamten Inhalt, einschließlich Unterverzeichnissen, zu kopieren, müssen Sie die Option `-r` (rekursiv) verwenden.

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Dieser Befehl kopiert das Verzeichnis `Pumpkin` und alles darin in Ihr Verzeichnis `Documents`.

Sie können auch `-R` sehen, was auf typischen Linux-Systemen denselben rekursiven Zweck erfüllt:

```bash
$ cp -R website /home/pete/backups/
```

### Umgang mit Dateiüberschreibungen

Standardmäßig überschreibt `cp` eine Datei im Ziel, wenn sie denselben Namen hat. Um versehentlichen Datenverlust zu vermeiden, verwenden Sie die Option `-i` (interaktiv), die vor dem Überschreiben um Bestätigung bittet.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Umgekehrt, wenn Sie eine Überschreibung ohne Nachfrage erzwingen möchten, verwenden Sie die Option `-f`. Dies ist nützlich in Skripten, in denen keine Benutzerinteraktion möglich ist.

```bash
$ cp -f mycoolfile /home/pete/Pictures
```

Eine weitere nützliche Sicherheitsoption ist `-n`, was „no clobber“ bedeutet. Sie verhindert das Überschreiben einer bereits existierenden Zieldatei.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

### Dateiattribute mit -p erhalten

Beim Kopieren einer Datei werden deren Metadaten wie Änderungszeit und Eigentümer normalerweise aktualisiert. Um diese ursprünglichen Attribute zu erhalten, verwenden Sie die Option `-p`.

Die Option `cp -p` ist besonders nützlich für Backups oder beim Migrieren von Dateien, bei denen die Erhaltung der Zeitstempel wichtig ist.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Dies kopiert `mycoolfile` und erhält dabei Modus, Eigentümer (sofern erlaubt) und Zeitstempel.

### Archivkopien mit -a

Die Option `-a` steht für Archiv. Sie wird häufig für Backup-ähnliche Verzeichnis-Kopien verwendet, da sie viele Attribute erhält und rekursiv kopiert.

```bash
$ cp -a project/ project-backup/
```

Für viele alltägliche Backups ist `cp -a` bequemer als das manuelle Kombinieren mehrerer Optionen.

### Nur neuere Dateien mit -u kopieren

Die Option `-u` kopiert nur, wenn die Quelldatei neuer ist als die Zieldatei oder wenn die Zieldatei nicht existiert.

```bash
$ cp -u *.txt /home/pete/Documents/
```

Dies ist nützlich, wenn Sie einen Ordner aktualisieren möchten, ohne bereits aktuelle Dateien neu zu schreiben.

### Häufige cp-Optionen

Hier sind die Optionen, die Sie am häufigsten verwenden werden:

- `-r` oder `-R`: Verzeichnisse rekursiv kopieren.
- `-i`: Vor dem Überschreiben einer Datei nachfragen.
- `-f`: Überschreiben erzwingen, indem das Ziel bei Bedarf zuerst entfernt wird.
- `-n`: Keine vorhandenen Dateien überschreiben.
- `-p`: Modus, Eigentümer (wo möglich) und Zeitstempel erhalten.
- `-a`: Archivmodus, nützlich zum Erhalten von Verzeichnisbäumen.
- `-u`: Nur kopieren, wenn die Quelle neuer ist als das Ziel.
- `-v`: Zeigt jede Datei während des Kopiervorgangs an.

### Häufige Fragen

**Warum hat cp meine Datei überschrieben?** Standardmäßig ersetzt `cp` eine Zieldatei mit demselben Namen. Verwenden Sie `cp -i`, um zuerst zu fragen, oder `cp -n`, um Überschreiben zu vermeiden.

**Warum kann cp kein Verzeichnis kopieren?** Ein Verzeichnis erfordert rekursives Kopieren. Verwenden Sie `cp -r source-dir destination-dir`.

**Was ist der Unterschied zwischen cp und mv?** `cp` erstellt eine Kopie und behält das Original. `mv` verschiebt oder benennt das Original um.

**Sollte ich für Backups cp -r oder cp -a verwenden?** Verwenden Sie `cp -r` für eine einfache rekursive Kopie. Verwenden Sie `cp -a`, wenn Sie eine Backup-ähnliche Kopie möchten, die mehr Dateiattribute erhält.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis für das Kopieren von Dateien und Verzeichnissen unter Linux zu vertiefen:

1. **[Linux cp Command: File Copying](https://labex.io/de/labs/linux-linux-cp-command-file-copying-209744)** – Üben Sie die Grundnutzung, erweiterte Optionen wie rekursives Kopieren, Erhaltung von Attributen und die Verwendung von Wildcards, um Dateien und Verzeichnisse effizient zu kopieren.
2. **[Organizing Files and Directories](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Üben Sie wichtige Linux-Dateiverwaltungsfähigkeiten, indem Sie die Befehle `cp`, `mv` und `rm` verwenden, um eine Projektstruktur zu organisieren, Dateien zu verschieben und unnötige Verzeichnisse zu bereinigen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit Datei-Kopieren und -Verwaltung unter Linux zu gewinnen.

## Quiz Question

Welchen Parameter müssen Sie angeben, um ein Verzeichnis zu kopieren?

## Quiz Answer

-r
