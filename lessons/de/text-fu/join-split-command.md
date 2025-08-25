---
index: 11
lang: "de"
title: "join und split"
meta_title: "join und split - Text-Fu"
meta_description: "Lernen Sie, die Linux-Befehle 'join' und 'split' zur Dateimanipulation zu verwenden. Verstehen Sie, wie Dateien nach gemeinsamen Feldern zusammengeführt und große Dateien effizient aufgeteilt werden. Erhalten Sie praktische Beispiele und Tipps."
meta_keywords: "Linux join Befehl, Linux split Befehl, Dateimanipulation, Linux Tutorial, Befehlszeile, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der Befehl `join` ermöglicht es Ihnen, mehrere Dateien anhand eines gemeinsamen Feldes zusammenzuführen:

Nehmen wir an, ich hätte zwei Dateien, die ich zusammenführen wollte:

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Sehen Sie, wie meine Dateien zusammengeführt wurden? Sie werden standardmäßig nach dem ersten Feld zusammengeführt, und die Felder müssen identisch sein. Wenn nicht, können Sie sie sortieren. In diesem Fall werden die Dateien über 1, 2, 3 zusammengeführt.

Wie würden wir die folgenden Dateien zusammenführen?

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

Um diese Datei zusammenzuführen, müssen Sie angeben, welche Felder Sie zusammenführen. In diesem Fall möchten wir Feld 2 in `file1.txt` und Feld 1 in `file2.txt`, daher würde der Befehl so aussehen:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` bezieht sich auf `file1.txt` und `-2` auf `file2.txt`. Ziemlich clever. Sie können eine Datei auch mit dem Befehl `split` in verschiedene Dateien aufteilen:

```bash
split somefile
```

Dies wird sie in verschiedene Dateien aufteilen. Standardmäßig werden sie aufgeteilt, sobald sie eine Grenze von 1000 Zeilen erreichen. Die Dateien werden standardmäßig `x**` genannt.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Zusammenführens und Manipulierens von Textdateien zu vertiefen:

1. **[Linux join Command: File Joining](https://labex.io/de/labs/linux-linux-join-command-file-joining-219193)** – Dieses Lab bietet eine direkte, praktische Einführung in den Befehl `join`, die es Ihnen ermöglicht, das Zusammenführen von Zeilen aus zwei sortierten Textdateien basierend auf einem gemeinsamen Feld zu üben, genau wie in der Lektion besprochen.
2. **[Processing Employees Data](https://labex.io/de/labs/linux-processing-employees-data-388132)** – Wenden Sie Ihr Wissen über `join` und andere leistungsstarke Linux-Befehlszeilen-Dienstprogramme wie `awk` an, um Daten aus mehreren Quellen zu kombinieren und zu verarbeiten, wodurch ein reales Datenanalyseszenario simuliert wird.
3. **[Sequence Control and Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** – Verbessern Sie Ihre Befehlszeileneffizienz und Datenmanipulationsfähigkeiten, indem Sie lernen, Befehlsausführungssequenzen zu steuern, Pipelines zu nutzen und leistungsstarke Textverarbeitungswerkzeuge einzusetzen, was die Datenkombinationsfähigkeiten von `join` ergänzt.

Diese Labs helfen Ihnen, die Konzepte der Textdateimanipulation und Datenkombination in realen Szenarien anzuwenden und Vertrauen in Linux-Befehlszeilenwerkzeuge aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um Dateien namens `cat`, `dog`, `cow` zusammenzuführen?

## Quiz Answer

join cat dog cow
