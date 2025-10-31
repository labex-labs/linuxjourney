---
index: 6
lang: "de"
title: "cut"
meta_title: "cut - Text-Tools"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl `cut` verwenden, um bestimmte Textabschnitte aus Dateien zu extrahieren. Diese Anleitung behandelt das Schneiden nach Zeichen und Feld (`cut f`), einschließlich der Verwendung von `cut f` mit benutzerdefinierten Trennzeichen. Perfekt für die Beherrschung der Linux-Textverarbeitung."
meta_keywords: "cut Befehl, Linux Textverarbeitung, Text extrahieren, cut f, cut f verwenden, Linux Tutorial, cut Beispiele, Linux Anleitung, Feldtrennung"
---

## Lesson Content

Wir werden ein paar nützliche Befehle zur Textverarbeitung kennenlernen. Bevor wir beginnen, erstellen wir eine Datei, mit der wir arbeiten können. Kopieren Sie den folgenden Befehl und fügen Sie ihn ein. Nach dem Einfügen müssen Sie ein tatsächliches TAB-Zeichen zwischen "lazy" und "dog" einfügen (dies gelingt oft durch Drücken von Strg-V und dann TAB).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

Der erste Befehl, den wir untersuchen werden, ist `cut`, der Textabschnitte aus einer Datei extrahiert.

### Schneiden nach Zeichen

Sie können Inhalte basierend auf der Zeichenposition mithilfe des Flags `-c` extrahieren.

```bash
cut -c 5 sample.txt
```

Dieser Befehl gibt das 5. Zeichen aus jeder Zeile der Datei aus. In unserem Fall ist die Ausgabe "q". Beachten Sie, dass Leerzeichen auch als Zeichen zählen.

### Schneiden nach Feld mit cut f

Aussagekräftiger ist das Schneiden nach Feldern. Die Syntax `cut f`, die das Flag `-f` verwendet, ermöglicht es Ihnen, Text basierend auf der Feldposition zu extrahieren. Standardmäßig verwendet `cut` das TAB-Zeichen als Trennzeichen, was bedeutet, dass alles, was durch ein TAB getrennt ist, als eigenständiges Feld betrachtet wird.

Sehen wir uns an, wie man f basierend auf Feldern schneidet:

```bash
cut -f 2 sample.txt
```

Da wir ein TAB zwischen "lazy" und "dog" eingefügt haben, behandelt dieser Befehl "dog" als das zweite Feld. Ihre Ausgabe sollte "dog" sein.

### Verwendung benutzerdefinierter Trennzeichen

Sie können das Feld-Flag auch mit dem Trennzeichen-Flag (`-d`) kombinieren, um ein benutzerdefiniertes Trennzeichen anzugeben. Dies ist nützlich, wenn Sie mit Dateien arbeiten, die Zeichen wie Kommas oder Semikolons zur Trennung von Daten verwenden.

```bash
cut -f 1 -d ";" sample.txt
```

Dieser Befehl ändert das Trennzeichen von einem TAB in ein Semikolon (`;`). Da wir das erste Feld (`-f 1`) schneiden, ist das Ergebnis "The quick brown".

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Textverarbeitung mit `cut` und anderen verwandten Befehlen zu festigen:

1. **[Linux cut Befehl: Textausschnitt](https://labex.io/de/labs/linux-linux-cut-command-text-cutting-219187)** - Dieses Labor bietet eine direkte, praktische Einführung in den `cut`-Befehl, mit dem Sie das Extrahieren bestimmter Spalten oder Felder aus Textdateien üben können, genau wie in der Lektion besprochen.
2. **[Einfache Textverarbeitung](https://labex.io/de/labs/linux-simple-text-processing-18004)** - Erweitern Sie Ihre Fähigkeiten zur Textmanipulation, indem Sie leistungsstarke Befehle wie `tr`, `col`, `join` und `paste` verwenden, um Textdaten effizient zu verarbeiten und zu analysieren.
3. **[Sequenzsteuerung und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** - Verbessern Sie Ihre Kommandozeilen-Effizienz, indem Sie lernen, Befehlssequenzen zu steuern, Pipelines zu nutzen und leistungsstarke Textverarbeitungswerkzeuge wie `cut`, `grep`, `wc`, `sort` und `uniq` einzusetzen.

Diese Labore helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textverarbeitung unter Linux aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um das erste Zeichen jeder Zeile in einer Datei abzurufen?

## Quiz Answer

cut -c 1
