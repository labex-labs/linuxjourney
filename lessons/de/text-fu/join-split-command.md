---
index: 11
lang: "de"
title: "Verbinden und Aufteilen"
meta_title: "Verbinden und Aufteilen - Text-Fu"
meta_description: "Meistern Sie die Verwendung der Linux-Befehle join und split. Lernen Sie, Dateien effizient anhand gemeinsamer Felder zu verbinden und große Dateien in kleinere Teile aufzuteilen. Diese Anleitung behandelt, welchen Befehl Sie verwenden würden, um Dateien wie katze, hund, kuh zu verbinden, und andere praktische Beispiele."
meta_keywords: "linux dateien verbinden, welchen befehl würden sie verwenden um dateien zu verbinden, linux join befehl, linux split befehl, dateimanipulation, kommandozeile, textverarbeitung"
---

## Lesson Content

In Linux ist die Verwaltung und Bearbeitung von Textdateien eine häufige Aufgabe. Zwei leistungsstarke Dienstprogramme hierfür sind `join` und `split`. Der Befehl `join` führt Zeilen aus zwei Dateien basierend auf einem gemeinsamen Feld zusammen, während `split` eine große Datei in kleinere, besser handhabbare Teile zerlegt.

### Dateien nach einem gemeinsamen Feld zusammenfügen

Der Befehl `join` ist ein grundlegendes Werkzeug, wenn Sie **linux join files** (Linux-Dateien zusammenfügen) müssen. Standardmäßig kombiniert er Zeilen aus zwei sortierten Dateien basierend auf dem identischen ersten Feld.

Stellen Sie sich zum Beispiel vor, Sie haben zwei Dateien, die Sie zusammenführen möchten:

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

Mit dem Befehl `join` können Sie sie einfach kombinieren:

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Wie Sie sehen, wurden die Dateien mithilfe des gemeinsamen ersten Feldes (1, 2, 3) zusammengefügt. Damit `join` korrekt funktioniert, müssen die Verknüpfungsfelder in beiden Dateien sortiert sein.

### Angabe unterschiedlicher Verknüpfungsfelder

Was ist, wenn das gemeinsame Feld nicht die erste Spalte ist? Sie können `join` mitteilen, welche Felder verwendet werden sollen. Betrachten Sie diese Dateien:

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

Hier müssen wir das zweite Feld von `file1.txt` und das erste Feld von `file2.txt` verknüpfen. Der Befehl würde lauten:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Die Option `-1 2` gibt das Feld 2 der ersten Datei an, und `-2 1` gibt das Feld 1 der zweiten Datei an.

### Aufteilen großer Dateien

Der Befehl `split` macht das Gegenteil von `join`; er teilt eine große Datei in kleinere auf.

```bash
$ split somefile
```

Standardmäßig teilt dieser Befehl `somefile` in neue Dateien auf, sobald eine Grenze von 1000 Zeilen erreicht ist. Die Ausgabedateien werden als `xaa`, `xab` usw. benannt. Sie können dieses Verhalten anpassen, indem Sie beispielsweise mit der Option `-l` eine andere Zeilenanzahl angeben oder mit der Option `-b` nach Dateigröße aufteilen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis für das Zusammenfügen und Bearbeiten von Textdateien zu festigen:

1. **[Linux join Befehl: Dateizusammenführung](https://labex.io/de/labs/linux-linux-join-command-file-joining-219193)** - Dieses Labor bietet eine direkte, praktische Einführung in den Befehl `join`, mit dem Sie das Zusammenführen von Zeilen aus zwei sortierten Textdateien basierend auf einem gemeinsamen Feld üben können, genau wie in der Lektion besprochen.
2. **[Verarbeitung von Mitarbeiterdaten](https://labex.io/de/labs/linux-processing-employees-data-388132)** - Wenden Sie Ihr Wissen über `join` und andere leistungsstarke Linux-Kommandozeilen-Dienstprogramme wie `awk` an, um Daten aus mehreren Quellen zu kombinieren und zu verarbeiten und so ein reales Datenanalyseszenario zu simulieren.
3. **[Sequenzsteuerung und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** - Verbessern Sie Ihre Effizienz in der Kommandozeile und Ihre Fähigkeiten zur Datenmanipulation, indem Sie lernen, Befehlsausführungssequenzen zu steuern, Pipelines zu nutzen und leistungsstarke Textverarbeitungswerkzeuge einzusetzen, was die Datenkombinationsfähigkeiten von `join` ergänzt.

Diese Labs helfen Ihnen, die Konzepte der Textdateibearbeitung und Datenkombination in realen Szenarien anzuwenden und Vertrauen in Linux-Kommandozeilen-Tools aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um Dateien namens `cat`, `dog`, `cow` zusammenzufügen? Bitte geben Sie den vollständigen Befehl in englischer Sprache an. Der Befehl und die Dateinamen sollten in Kleinbuchstaben sein.

## Quiz Answer

join cat dog cow
