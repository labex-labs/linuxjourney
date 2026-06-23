---
index: 5
lang: "de"
title: "touch"
meta_title: "touch - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl touch mit Beispielen zum Erstellen leerer Dateien, Aktualisieren von Zeitstempeln, Setzen von Daten, Verwenden von Referenzdateien und Vermeiden von Überschreibungen."
meta_keywords: "linux touch befehl, touch befehl, datei erstellen linux, zeitstempel aktualisieren linux, touch -d, touch -r, touch -c"
---

## Lesson Content

Der Befehl `touch` ist ein Standardwerkzeug auf Unix-ähnlichen Betriebssystemen. Während sein Hauptzweck darin besteht, Dateizeitstempel zu ändern, wird er auch häufig verwendet, um neue, leere Dateien zu erstellen.

Die grundlegende Syntax lautet:

```bash
touch [OPTIONS] FILE...
```

### Neue Dateien erstellen

Die einfachste Möglichkeit, eine leere Datei zu erstellen, ist die Verwendung von `touch` gefolgt von einem Dateinamen. Wenn die Datei nicht existiert, erstellt `touch` sie.

```bash
$ touch mysuperduperfile
```

Nach Ausführung dieses Befehls erscheint eine neue leere Datei namens `mysuperduperfile` in Ihrem aktuellen Verzeichnis. Sie können mehrere Dateien gleichzeitig erstellen, indem Sie ihre Namen auflisten.

```bash
$ touch file1.txt file2.txt file3.log
```

Dies ist nützlich, wenn Sie eine Projektstruktur einrichten oder Platzhalterdateien erstellen möchten, bevor Sie Inhalte hinzufügen.

### Aktualisieren von Dateizeitstempeln

Die ursprüngliche Funktion von `touch` ist das Aktualisieren der Zugriffs- und Änderungszeitstempel einer Datei oder eines Verzeichnisses. Wenn Sie `touch` auf eine vorhandene Datei anwenden, aktualisiert es deren Zeitstempel auf die aktuelle Zeit.

Sie können dies überprüfen, indem Sie `ls -l` verwenden, um den Zeitstempel einer Datei zu sehen, dann `touch` darauf ausführen und anschließend erneut prüfen.

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### Erweiterte Zeitstempelsteuerung

Der Befehl `touch` bietet auch Optionen für eine präzisere Zeitstempelmanipulation.

Verwenden Sie eine Referenzdatei mit `-r`, um Zeitstempel von einer Datei auf eine andere zu kopieren.

```bash
$ touch -r file1.txt file2.txt
```

Setzen Sie ein bestimmtes Datum und eine bestimmte Uhrzeit mit `-d`:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Verwenden Sie `-c`, wenn Sie eine Datei nur aktualisieren möchten, falls sie bereits existiert. Mit `-c` erstellt `touch` keine fehlende Datei.

```bash
$ touch -c existing-file.txt
```

### Häufige touch-Optionen

- `-a`: Nur die Zugriffszeit ändern.
- `-m`: Nur die Änderungszeit ändern.
- `-c`: Datei nicht erstellen, wenn sie nicht existiert.
- `-d "DATUM"`: Einen bestimmten Datumsstring verwenden.
- `-r DATEI`: Die Zeitstempel einer anderen Datei als Referenz verwenden.
- `-t ZEITSTEMPEL`: Einen Zeitstempel im kompakten numerischen Format verwenden.

Zum Beispiel ändert dies nur die Änderungszeit:

```bash
$ touch -m notes.txt
```

### Häufige Fragen

**Fügt touch Text zu einer Datei hinzu?** Nein. `touch` erstellt eine leere Datei oder aktualisiert Zeitstempel. Verwenden Sie einen Editor, `echo` oder `cat`, um Text hinzuzufügen.

**Überschreibt touch eine vorhandene Datei?** Nein. Es aktualisiert Zeitstempel, ersetzt aber nicht den Inhalt der Datei.

**Warum wird touch in Skripten verwendet?** Es ist eine schnelle Möglichkeit sicherzustellen, dass eine Datei existiert oder um zu markieren, dass eine Aufgabe zu einer bestimmten Zeit stattgefunden hat.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis für das Erstellen und Verwalten von Dateisystemobjekten zu vertiefen:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/de/labs/linux-linux-mkdir-command-directory-creating-209739)** – Lernen Sie, wie Sie den Befehl `mkdir` in Linux verwenden, um Verzeichnisse zu erstellen, Berechtigungen zu setzen und Ihr Dateisystem zu organisieren. Dies hilft Ihnen, das umfassendere Konzept der Erstellung neuer Elemente im Dateisystem zu verstehen.
2. **[Setting Up a New Project Structure](https://labex.io/de/labs/linux-setting-up-a-new-project-structure-387859)** – Üben Sie Ihre Fähigkeiten im Linux-Verzeichnismanagement, indem Sie eine spezifische Projektstruktur erstellen und mit wichtigen Befehlen wie `mkdir` und `cd` darin navigieren.

Diese Labs helfen Ihnen, die Konzepte der Dateisystemerstellung und -organisation in realen Szenarien anzuwenden und Vertrauen im Umgang mit Linux-Befehlen aufzubauen.

## Quiz Question

Wie erstellen Sie eine Datei namens `myfile`? Bitte antworten Sie nur mit dem englischen Befehl und achten Sie auf Groß- und Kleinschreibung.

## Quiz Answer

touch myfile
