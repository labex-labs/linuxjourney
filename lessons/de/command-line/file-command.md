---
index: 6
lang: "de"
title: "file"
meta_title: "file - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl file mit Beispielen zur Identifikation von Textdateien, Bildern, Skripten, komprimierten Archiven, Binärdateien und MIME-Typen."
meta_keywords: "linux file befehl, file befehl, dateityp erkennen linux, mime typ linux, textdatei, binärdatei, archivdatei"
---

## Lesson Content

Im vorherigen Kapitel haben wir `touch` kennengelernt. Schauen wir uns das noch einmal an. Ist Ihnen aufgefallen, dass der Dateiname nicht den üblichen Namenskonventionen entspricht, wie Sie sie wahrscheinlich von anderen Betriebssystemen wie Windows kennen? Normalerweise würde man erwarten, dass eine Datei namens `banana.jpeg` eine JPEG-Bilddatei ist.

Unter Linux müssen Dateinamen nicht den Inhalt der Datei widerspiegeln. Sie können eine Datei namens `funny.gif` erstellen, die tatsächlich kein GIF ist.

Um herauszufinden, um welche Art von Datei es sich handelt, können Sie den Befehl `file` verwenden. Er zeigt Ihnen eine Beschreibung des Inhalts der Datei an.

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

### Warum Dateiendungen nicht ausreichen

Linux-Tools benötigen normalerweise keine Dateiendung, um zu entscheiden, was für eine Datei es ist. Ein Shell-Skript kann `backup` heißen, eine Textdatei `README` und ein Bild kann eine falsche Endung haben. Der Befehl `file` untersucht den Inhalt und die Metadaten der Datei, um eine bessere Einschätzung zu geben.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

### Mehrere Dateien prüfen

Sie können mehrere Dateien gleichzeitig prüfen:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Wildcards funktionieren ebenfalls:

```bash
$ file *
```

### MIME-Typen anzeigen

Die Option `-i` gibt Informationen im MIME-Format aus, was nützlich ist, wenn man mit Webdateien oder Skripten arbeitet.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

### Häufige Optionen von file

- `-i`: Zeigt MIME-Typ-Informationen an.
- `-b`: Kurze Ausgabe, ohne Dateinamen.
- `-L`: Symbolischen Links folgen.
- `-z`: Versucht, komprimierte Dateien zu untersuchen.

Zum Beispiel:

```bash
$ file -b notes.txt
ASCII text
```

### Häufige Fragen

**Verlässt sich file nur auf Dateiendungen?** Nein. Es untersucht hauptsächlich den Dateiinhalte und bekannte Signaturen.

**Kann file falsch liegen?** Ja. Es gibt eine fundierte Vermutung ab, besonders bei ungewöhnlichen oder beschädigten Dateien.

**Warum sagt file „data“?** Die Datei entspricht keinem spezifischeren bekannten Typ oder es handelt sich um Binärdaten ohne erkennbare Signatur.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis für die Inspektion von Dateiinhalten und -eigenschaften zu vertiefen:

1. **[Linux ls Command: Content Listing](https://labex.io/de/labs/linux-linux-ls-command-content-listing-219205)** – Lernen Sie den Linux-Befehl `ls` kennen, um Dateien und Verzeichnisse effizient aufzulisten und zu analysieren, was oft vor oder nach der Verwendung von `file` erfolgt, um den Inhalt Ihrer Verzeichnisse zu verstehen.
2. **[Linux cat Command: File Concatenating](https://labex.io/de/labs/linux-linux-cat-command-file-concatenating-210986)** – Üben Sie das Anzeigen und Bearbeiten von Textdateien, eine häufige Aufgabe nach der Identifikation des Dateityps.
3. **[Linux more Command: File Scrolling](https://labex.io/de/labs/linux-linux-more-command-file-scrolling-214299)** – Verbessern Sie Ihre Kommandozeilenfähigkeiten für das Navigieren und Erkunden großer Textdateien, basierend auf der Fähigkeit, Dateitypen zu erkennen und deren Inhalt zu prüfen.

Diese Labs helfen Ihnen, die Konzepte der Dateiinhaltsprüfung und -anzeige in realen Szenarien anzuwenden und stärken Ihr Selbstvertrauen im Umgang mit Dateien unter Linux.

## Quiz Question

Welchen Befehl können Sie verwenden, um den Dateityp einer Datei herauszufinden?

## Quiz Answer

file
