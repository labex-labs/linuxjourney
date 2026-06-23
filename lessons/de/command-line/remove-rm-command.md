---
index: 13
lang: "de"
title: "rm (Entfernen)"
meta_title: "rm (Entfernen) - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl rm mit sicheren Beispielen zum Löschen von Dateien, Entfernen von Verzeichnissen, Verwendung von rm -r, rm -i und Vermeidung von rm -rf Fehlern."
meta_keywords: "linux rm befehl, rm befehl, rm -r, rm -i, rm -f, rm -rf, dateien löschen linux, verzeichnis entfernen linux, rmdir"
---

## Lesson Content

In Linux sammelt man häufig Dateien an, die nicht mehr benötigt werden. Um sie zu löschen, verwendet man den Befehl `rm` (remove), ein grundlegendes Werkzeug zur Verwaltung des Dateisystems. Die Grundsyntax lautet:

```bash
rm [OPTIONS] FILE...
```

Der Befehl `rm` entfernt Verzeichniseinträge aus dem Dateisystem. Einfach gesagt, löscht er Dateien. Im Gegensatz zu vielen Desktop-Umgebungen verschiebt das Löschen über die Kommandozeile Dateien normalerweise nicht in einen Papierkorb, daher sollten Sie Ihren Befehl vor dem Drücken der Eingabetaste überprüfen.

### Eine einzelne Datei entfernen

Um eine einzelne Datei zu löschen, übergeben Sie den Dateinamen an `rm`.

```bash
$ rm file1
```

Sie können mehrere Dateien gleichzeitig löschen, indem Sie sie nacheinander auflisten.

```bash
$ rm notes.txt old-report.txt draft.md
```

Das ist praktisch für eine schnelle Bereinigung, bedeutet aber auch, dass ein Tippfehler mehr löschen kann als beabsichtigt.

### Dateien mit Wildcards entfernen

Shell-Wildcards erlauben es, mehrere Dateien zu treffen. Zum Beispiel entfernt dieser Befehl jede `.tmp`-Datei im aktuellen Verzeichnis:

```bash
$ rm *.tmp
```

Vor der Verwendung von `rm` mit einem Wildcard ist es sicherer, die Übereinstimmung mit `ls` zu überprüfen.

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

Denken Sie daran, dass die Shell `*.tmp` vor Ausführung von `rm` erweitert. Wenn das Muster mehr Dateien trifft als erwartet, erhält `rm` trotzdem alle.

### Interaktives Löschen mit -i

Für eine sicherere Vorgehensweise verwenden Sie die Option `-i`. Sie fragt vor dem Löschen jeder Datei nach einer Bestätigung.

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

Verwenden Sie `rm -i`, wenn Sie Dateien aus einem gemeinsamen Verzeichnis löschen, viele Dateien aufräumen oder den Befehl zum ersten Mal lernen.

### Erzwingendes Löschen mit -f

Die Option `-f` bedeutet „force“ (erzwingen). Sie ignoriert nicht vorhandene Dateien und fragt nicht nach einer Bestätigung.

```bash
$ rm -f old-cache.txt
```

Das ist nützlich in Skripten, wo die Bereinigung fortgesetzt werden soll, auch wenn eine Datei bereits weg ist.

```bash
$ rm -f build.log
```

Seien Sie vorsichtig: `-f` unterdrückt auch einige Sicherheitsabfragen, daher können Fehler verborgen bleiben.

### Verzeichnisse mit -r entfernen

Standardmäßig kann `rm` kein Verzeichnis löschen.

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

Um ein Verzeichnis und alles darin zu entfernen, verwenden Sie `-r` oder `-R` für rekursives Löschen.

```bash
$ rm -r old-project
```

Rekursives Löschen durchläuft den Verzeichnisbaum und entfernt Dateien, Unterverzeichnisse und deren Inhalte.

### Die Gefahren von rm -rf

Der Befehl `rm -rf` kombiniert rekursives Löschen mit erzwingendem Löschen.

```bash
$ rm -rf old-project
```

Dieser Befehl kann geeignet sein, um generierte Ordner wie Build-Ausgaben zu entfernen, ist aber gefährlich, weil er einen ganzen Baum ohne Rückfrage löscht. Prüfen Sie immer:

- Befinden Sie sich im Verzeichnis, von dem Sie denken, dass Sie dort sind? Verwenden Sie `pwd`.
- Hat Ihr Wildcard richtig erweitert? Vorschau mit `ls`.
- Ist der Pfad absolut oder relativ? `/tmp/cache` und `tmp/cache` sind sehr unterschiedlich.
- Gibt es versehentlich ein Leerzeichen? `rm -rf old-project` und `rm -rf old project` zielen auf unterschiedliche Pfade.

### Verwendung von rmdir für leere Verzeichnisse

Als sicherere Alternative entfernen Sie ein leeres Verzeichnis mit `rmdir`.

```bash
$ rmdir empty-directory
```

Der Befehl `rmdir` gelingt nur, wenn das Verzeichnis komplett leer ist, was ihn zu einer sichereren Wahl als `rm -r` für Aufräumarbeiten macht.

### Häufige rm-Optionen

Hier sind die Optionen, die Sie am häufigsten sehen werden:

- `-i`: Vor jeder Entfernung nachfragen.
- `-I`: Einmal nachfragen, bevor mehr als drei Dateien oder rekursiv gelöscht wird.
- `-f`: Erzwingt das Löschen und ignoriert nicht vorhandene Dateien.
- `-r` oder `-R`: Verzeichnisse und deren Inhalte rekursiv entfernen.
- `-v`: Zeigt an, was entfernt wurde.

Zum Beispiel können Sie Optionen kombinieren:

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

### Häufige Fragen

**Kann ich rm rückgängig machen?** Normalerweise nein. Sobald eine Datei mit `rm` gelöscht wurde, gibt es keinen eingebauten Rückgängig-Befehl. Backups, Versionskontrolle und Tools zur Dateisystemwiederherstellung sind die wirklichen Sicherheitsnetze.

**Warum sagt rm „Permission denied“?** Sie haben keine Berechtigung, diese Datei zu löschen oder das Verzeichnis zu ändern, das sie enthält. Prüfen Sie Besitz und Berechtigungen mit `ls -l`.

**Warum sagt rm „No such file or directory“?** Die Datei existiert an diesem Pfad nicht, oder Sie befinden sich in einem anderen Verzeichnis als erwartet. Verwenden Sie `pwd` und `ls` zur Überprüfung.

**Sollte ich sudo mit rm verwenden?** Nur wenn Sie den Pfad, den Sie löschen, vollständig verstehen. `sudo rm -r` kann Systemdateien entfernen, die Ihr normaler Benutzer nicht anfassen darf.

## Exercise

Übung macht den Meister. Hier sind einige praktische Übungen, um Ihr Verständnis für das Entfernen von Dateien und Verzeichnissen in Linux zu festigen:

1. **[Linux rm Command: File Removing](https://labex.io/de/labs/linux-linux-rm-command-file-removing-209741)** – Lernen Sie, wie Sie den Befehl `rm` zum Entfernen von Dateien und Verzeichnissen verwenden, einschließlich verschiedener Optionen wie `-r` und `-i`, und üben Sie sicheres und effektives Löschen.
2. **[Organizing Files and Directories](https://labex.io/de/labs/linux-organizing-files-and-directories-387877)** – Üben Sie wichtige Linux-Dateimanagement-Fähigkeiten, einschließlich der Verwendung von `rm` zum Aufräumen unnötiger Verzeichnisse, in einer praktischen Herausforderung.

Diese Labs helfen Ihnen, diese Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit dem `linux rm command` zu gewinnen.

## Quiz Question

Wie entfernen Sie eine Datei namens `myfile`? Ihre Antwort muss auf Englisch sein und den genauen, groß- und kleinschreibungssensitiven Befehl verwenden.

## Quiz Answer

rm myfile
