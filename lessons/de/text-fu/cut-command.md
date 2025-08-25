---
index: 6
lang: "de"
title: "cut"
meta_title: "cut - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl `cut` verwenden, um Text aus Dateien zu extrahieren. Dieses anfängerfreundliche Tutorial behandelt das Schneiden von Zeichen und Feldern. Verbessern Sie Ihre Linux-Textverarbeitungsfähigkeiten!"
meta_keywords: "cut Befehl, Linux Textverarbeitung, Text extrahieren, Linux Tutorial, Linux für Anfänger, cut Beispiele, Linux Anleitung"
---

## Lesson Content

Wir werden ein paar nützliche Befehle lernen, die Sie zur Textverarbeitung verwenden können. Bevor wir anfangen, erstellen wir eine Datei, mit der wir arbeiten werden. Kopieren Sie den folgenden Befehl und fügen Sie ihn ein; sobald Sie das getan haben, fügen Sie ein TAB zwischen "lazy" und "dog" ein (halten Sie Strg-v + TAB gedrückt).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

Der erste Befehl, den wir lernen werden, ist der Befehl `cut`. Er extrahiert Textteile aus einer Datei.

Um Inhalte nach einer Zeichenliste zu extrahieren:

```bash
cut -c 5 sample.txt
```

Dies gibt das 5. Zeichen in jeder Zeile der Datei aus. In diesem Fall ist es "q"; beachten Sie, dass das Leerzeichen auch als Zeichen zählt.

Um die Inhalte nach einem Feld zu extrahieren, müssen wir eine kleine Änderung vornehmen:

```bash
cut -f 2 sample.txt
```

Das Flag `-f` oder Feld schneidet Text basierend auf Feldern. Standardmäßig verwendet es TABs als Trennzeichen, sodass alles, was durch ein TAB getrennt ist, als Feld betrachtet wird. Sie sollten "dog" als Ausgabe sehen.

Sie können das Feld-Flag mit dem Trennzeichen-Flag kombinieren, um die Inhalte mit einem benutzerdefinierten Trennzeichen zu extrahieren:

```bash
cut -f 1 -d ";" sample.txt
```

Dies ändert das TAB-Trennzeichen in ein ";"-Trennzeichen, und da wir das erste Feld schneiden, sollte das Ergebnis "The quick brown" sein.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Textverarbeitung mit `cut` und anderen verwandten Befehlen zu festigen:

1. **[Linux cut Befehl: Text schneiden](https://labex.io/de/labs/linux-linux-cut-command-text-cutting-219187)** - Dieses Lab bietet eine direkte, praktische Einführung in den `cut`-Befehl, mit dem Sie das Extrahieren spezifischer Spalten oder Felder aus Textdateien üben können, genau wie in der Lektion besprochen.
2. **[Einfache Textverarbeitung](https://labex.io/de/labs/linux-simple-text-processing-18004)** - Erweitern Sie Ihre Textmanipulationsfähigkeiten, indem Sie leistungsstarke Befehle wie `tr`, `col`, `join` und `paste` verwenden, um Textdaten effizient zu verarbeiten und zu analysieren.
3. **[Sequenzkontrolle und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** - Verbessern Sie Ihre Effizienz in der Befehlszeile, indem Sie lernen, Befehlsausführungssequenzen zu steuern, Pipelines zu nutzen und leistungsstarke Textverarbeitungswerkzeuge wie `cut`, `grep`, `wc`, `sort` und `uniq` einzusetzen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textverarbeitung unter Linux aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um das erste Zeichen jeder Zeile in einer Datei zu erhalten?

## Quiz Answer

cut -c 1
