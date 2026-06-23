---
index: 14
lang: "de"
title: "find"
meta_title: "find - Kommandozeile"
meta_description: "Lernen Sie den Linux-Befehl find mit Beispielen zum Suchen nach Name, Typ, Größe, Änderungszeit und zum Ausführen von Aktionen auf passenden Dateien."
meta_keywords: "linux find befehl, find befehl, dateien finden linux, nach name finden, nach typ finden, nach größe finden, find mtime, find exec"
---

## Lesson Content

Bei unzähligen Dateien auf einem System kann es schwierig sein, eine bestimmte zu finden. Der Befehl `find` durchsucht Verzeichnisbäume anhand von Kriterien wie Name, Typ, Größe und Änderungszeit.

### Verwendung des find-Befehls

Die Grundsyntax lautet:

```bash
find [PATH] [EXPRESSION]
```

Sie geben das Verzeichnis an, in dem gesucht werden soll, sowie die Kriterien für das Gesuchte.

Zum Beispiel, um nach einer Datei namens `puppies.jpg` im Verzeichnis `/home` und allen Unterverzeichnissen zu suchen, verwenden Sie:

```bash
$ find /home -name puppies.jpg
```

Suchvorgänge sind standardmäßig rekursiv, daher durchsucht `find /home` das Verzeichnis `/home` und seine Unterverzeichnisse.

### Suche nach Name und Typ

Eine der häufigsten Anwendungen von `find` ist die Suche nach Dateinamen. Die Option `-name` sucht nach exakten Namen oder nach Mustern im Shell-Stil.

```bash
$ find . -name "*.txt"
```

Sie können auch den Typ des gesuchten Elements angeben. Die Option `-type` wird dafür verwendet. Wenn Sie beispielsweise ein Verzeichnis statt einer Datei finden möchten, verwenden Sie `d`.

```bash
$ find /home -type d -name MyFolder
```

In diesem Befehl setzen wir den Typ auf `d` für Verzeichnis und suchen nach einem Element namens `MyFolder`. Um speziell nach regulären Dateien zu suchen, verwenden Sie `-type f`.

### Suche nach Größe und Zeit

Sie können nach Dateigröße suchen:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

Der erste Befehl findet Dateien, die größer als 10 Megabyte sind. Der zweite findet Dateien, die kleiner als 1 Kilobyte sind.

Sie können auch nach Änderungszeit suchen:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` bedeutet, innerhalb der letzten 7 Tage geändert. `-mtime +30` bedeutet, vor mehr als 30 Tagen geändert.

### Aktionen auf Ergebnissen ausführen

Standardmäßig gibt `find` die passenden Pfade aus. Sie können Aktionen wie `-print`, `-delete` oder `-exec` hinzufügen.

Treffer explizit ausgeben:

```bash
$ find . -name "*.log" -print
```

`ls -l` für jeden Treffer ausführen:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

Der Platzhalter `{}` wird durch jeden passenden Pfad ersetzt. Das maskierte Semikolon markiert das Ende des Befehls.

Seien Sie vorsichtig mit destruktiven Aktionen wie `-delete`. Führen Sie zuerst dieselbe Suche ohne `-delete` aus, um die Treffer zu überprüfen.

### Häufige find-Optionen

- `-name PATTERN`: Nach Dateinamen suchen.
- `-iname PATTERN`: Nach Dateinamen suchen, Groß-/Kleinschreibung ignorieren.
- `-type f`: Reguläre Dateien finden.
- `-type d`: Verzeichnisse finden.
- `-size +10M`: Dateien größer als 10 Megabyte finden.
- `-mtime -7`: Dateien finden, die innerhalb der letzten 7 Tage geändert wurden.
- `-maxdepth N`: Begrenzung der Suchtiefe von `find`.

### Häufige Fragen

**Warum zeigt find „Permission denied“ an?** Ihr Benutzer kann einige Verzeichnisse nicht lesen. Suchen Sie in einem engeren Pfad oder verwenden Sie entsprechende Berechtigungen.

**Warum sollte ich Muster wie "*.txt" in Anführungszeichen setzen?** Das Anführungszeichen verhindert, dass die Shell das Wildcard vor der Übergabe an `find` erweitert.

**Ist find rekursiv?** Ja. Es durchsucht standardmäßig Unterverzeichnisse.

## Exercise

Übung ist der Schlüssel, um den `find`-Befehl in Linux zu meistern. Diese praktischen Labs helfen Ihnen, Ihr Verständnis für das Finden von Dateien und Verzeichnissen zu vertiefen:

1. **[Linux find Command: File Searching](https://labex.io/de/labs/linux-linux-find-command-file-searching-219191)** – Dieses Lab bietet eine Einführung in den `find`-Befehl, ein vielseitiges Werkzeug zum Suchen und Auffinden von Dateien und Verzeichnissen basierend auf verschiedenen Kriterien. Sie üben, mit `find` bestimmte Dateien zu finden.
2. **[Discover Critical System Resources](https://labex.io/de/labs/linux-discover-critical-system-resources-388032)** – Lernen Sie wichtige Linux-Befehle zum Auffinden von Dateien und ausführbaren Dateien kennen, einschließlich `find`. Sie üben, das Dateisystem effizient zu navigieren und kritische Systemressourcen zu entdecken.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit dem `find`-Befehl zu gewinnen.

## Quiz Question

Welche Option sollten Sie für den `find`-Befehl angeben, um nach Namen zu suchen? Bitte antworten Sie nur mit der englischen Option und beachten Sie das erforderliche Format (z. B. -option).

## Quiz Answer

-name
