---
index: 3
lang: "de"
title: "tar und gzip"
meta_title: "tar und gzip - Pakete"
meta_description: "Ein umfassender Leitfaden zur Verwendung von tar und gzip unter Linux. Erfahren Sie mehr über tar-Kompression, wie man Archive erstellt und extrahiert, und den Unterschied zwischen gzip und tar. Meistern Sie Befehle zum Komprimieren von tar gz-Dateien und verwalten Sie Ihre Softwarepakete effektiv."
meta_keywords: "tar und gzip, tar Kompression, gzip tar, tar gz komprimieren, gzip und tar, Linux Archivierung, Dateikomprimierung, tar Befehl, gzip Befehl, Linux Tutorial"
---

## Lesson Content

Bevor wir uns mit Paketmanagern befassen, ist es wichtig, das Archivieren und Komprimieren von Dateien zu verstehen. Wenn Sie Software online herunterladen, werden Sie diese oft in archivierten und komprimierten Formaten finden. Diese Lektion konzentriert sich auf zwei grundlegende Dienstprogramme für diesen Zweck: `tar` und `gzip`.

### Archivierung vs. Komprimierung verstehen

Es ist wichtig, zwischen Archivierung und Komprimierung zu unterscheiden. **Archivierung** ist der Prozess, bei dem mehrere Dateien und Verzeichnisse zu einer einzigen Datei, einem sogenannten Archiv, zusammengefasst werden. Dies erleichtert die Verwaltung und Übertragung einer Gruppe von Dateien. **Komprimierung** hingegen ist der Prozess der Größenreduzierung einer Datei, um Speicherplatz zu sparen und Übertragungen zu beschleunigen. Das Dienstprogramm `tar` wird für die Archivierung verwendet, während `gzip` für die Komprimierung verwendet wird. Oft werden `gzip und tar` zusammen verwendet.

### Einzelne Dateien mit gzip komprimieren

Das Programm `gzip` wird verwendet, um einzelne Dateien in Linux zu komprimieren. Wenn Sie eine Datei mit `gzip` komprimieren, wird sie durch eine Datei mit der Erweiterung `.gz` ersetzt.

Um eine Datei zu komprimieren:

```bash
gzip meinecooleDatei
```

Dies erstellt `meinecooleDatei.gz` und entfernt das Original. Um die Datei zu dekomprimieren, können Sie `gunzip` verwenden:

```bash
gunzip meinecooleDatei.gz
```

### Archive mit tar erstellen

Obwohl `gzip` hervorragend zur Komprimierung geeignet ist, kann es mehrere Dateien nicht zu einem einzigen Archiv bündeln. Dafür verwenden wir das Dienstprogramm `tar` (Tape Archive). Eine mit `tar` erstellte Datei wird oft als „Tarball“ bezeichnet und hat die Erweiterung `.tar`.

Um ein neues Archiv mit mehreren Dateien zu erstellen:

```bash
tar cvf meinarchiv.tar datei1 datei2 verzeichnis1
```

Schlüsseln wir die Optionen auf:

- `c`: **c**reate (erstellen) eines neuen Archivs.
- `v`: **v**erbose-Modus, der die Dateien auflistet, während sie verarbeitet werden.
- `f`: **f**ile (Datei), die angibt, dass das nächste Argument der Name der Archivdatei ist.

### Die Stärke von tar und gzip kombiniert

Die wahre Stärke liegt in der gemeinsamen Verwendung von `tar und gzip`. Sie können zuerst ein `.tar`-Archiv erstellen und es dann mit `gzip` komprimieren, was zu einer `.tar.gz`-Datei führt. `tar` bietet jedoch eine bequeme Möglichkeit, die `tar compression` (tar-Komprimierung) in einem einzigen Schritt mithilfe der Option `z` zu handhaben. Dieser Prozess wird manchmal als Erstellung eines `gzip tar`-Archivs bezeichnet.

Um ein komprimiertes Archiv zu erstellen, was eine übliche Methode ist, um `compress tar gz` Dateien zu erstellen:

```bash
tar czvf meinarchiv.tar.gz datei1 datei2 verzeichnis1
```

Hier weist die Option `z` `tar` an, `gzip` für die Komprimierung zu verwenden.

### tar und gzip Archive extrahieren

Um Dateien aus einem Archiv zu extrahieren, verwenden Sie die Option `x`.

Um ein einfaches `.tar`-Archiv zu extrahieren:

```bash
tar xvf meinarchiv.tar
```

Um ein `.tar.gz`-Archiv mit einem einzigen Befehl zu dekomprimieren und zu extrahieren, fügen Sie einfach erneut die Option `z` hinzu:

```bash
tar xzvf meinarchiv.tar.gz
```

Lassen Sie uns die Extraktionsoptionen überprüfen:

- `x`: **e**xtract (extrahieren) von Dateien aus einem Archiv.
- `z`: Dekomprimiert das Archiv mit `g**z**ip`.
- `v`: **v**erbose-Modus, der die Dateien auflistet, während sie extrahiert werden.
- `f`: **f**ile (Datei), die die zu extrahierende Archivdatei angibt.

Achtung: Eine hilfreiche Eselsbrücke hierfür ist: e**X**tract **Z**ee **V**ery **F**ast! (Extrahieren Sie sehr schnell!)

`tar` ist ein Befehl, der so wesentlich und doch oft vergessen wird. Relevanter xkcd: `https://xkcd.com/1168`

### Andere Dienstprogramme

Obwohl `tar` und `gzip` extrem verbreitet sind, werden Sie auf Ihrer Linux-Reise auf andere Archivierungs- und Komprimierungsformate stoßen. Dazu gehören `bzip2` (das `.bz2`-Dateien erstellt und das Flag `j` in `tar` verwendet), `xz` (das `.xz`-Dateien mit dem Flag `J` erstellt) und die bekannten Dienstprogramme `zip`/`unzip`. Jedes hat seine eigenen Befehle und Komprimierungsraten, aber die zugrunde liegenden Konzepte bleiben dieselben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Dateiarchivierung und -komprimierung zu festigen:

1. **[Datei-Packaging und Komprimierung](https://labex.io/de/labs/linux-file-packaging-and-compression-385413)** - Lernen Sie wesentliche Linux-Techniken zur Datei-Komprimierung und zum Packaging mit Tools wie tar, gzip und zip.
2. **[Erstellen und Wiederherstellen eines Backups mit tar unter Linux](https://labex.io/de/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Sammeln Sie praktische Erfahrungen beim Erstellen und Wiederherstellen von Dateisystem-Backups mit dem tar-Befehl.
3. **[Systemprotokoll sichern](https://labex.io/de/labs/linux-backup-system-log-17989)** - Lernen Sie die wesentliche Fähigkeit, Systemprotokolldateien mithilfe des tar-Befehls und der Datumsformatierung zu sichern.

Diese Labs helfen Ihnen, die Konzepte der Archivierung und Komprimierung in realen Szenarien anzuwenden und Vertrauen beim Verwalten von Dateien in Linux aufzubauen.

## Quiz Question

Welches tar-Flag wird zum Erstellen von Archiven verwendet? Bitte antworten Sie mit einem einzigen Kleinbuchstaben in englischer Sprache.

## Quiz Answer

c
