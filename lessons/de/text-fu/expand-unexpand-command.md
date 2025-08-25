---
index: 10
lang: "de"
title: "expand und unexpand"
meta_title: "expand und unexpand - Text-Fu"
meta_description: "Lernen Sie, Tabs mit dem Befehl `expand` in Leerzeichen und Leerzeichen mit `unexpand` in Tabs umzuwandeln. Verbessern Sie die Formatierung von Textdateien mit diesem Linux-Tutorial."
meta_keywords: "expand Befehl, unexpand Befehl, Linux Tabs, Linux Leerzeichen, Textformatierung, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

In unserer Lektion über den Befehl `cut` hatten wir unsere Datei `sample.txt`, die einen Tab enthielt. Normalerweise würden Tabs einen merklichen Unterschied zeigen, aber einige Textdateien zeigen das nicht gut genug. Tabs in einer Textdatei bieten möglicherweise nicht den gewünschten Abstand. Um Ihre Tabs in Leerzeichen umzuwandeln, verwenden Sie den Befehl `expand`.

```bash
expand sample.txt
```

Der obige Befehl gibt eine Ausgabe aus, bei der jeder Tab in eine Gruppe von Leerzeichen umgewandelt wurde. Um diese Ausgabe in einer Datei zu speichern, verwenden Sie die Ausgabenumleitung, wie unten gezeigt.

```bash
expand sample.txt > result.txt
```

Im Gegensatz zu `expand` können wir jede Gruppe von Leerzeichen mit dem Befehl `unexpand` wieder in einen Tab umwandeln:

```bash
unexpand -a result.txt
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Textmanipulation und Umleitung in Linux zu vertiefen:

1. **[Umleiten von Eingabe und Ausgabe in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** – Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie die Standardausgabe (stdout), den Standardfehler (stderr) und die Standardeingabe (stdin) mithilfe von Operatoren wie `>` und `>>` manipulieren.
2. **[Einfache Textverarbeitung](https://labex.io/de/labs/linux-simple-text-processing-18004)** – Lernen Sie, leistungsstarke Befehle wie `tr`, `col`, `join` und `paste` zu verwenden, um Textdaten effizient zu manipulieren und zu analysieren, und verbessern Sie so Ihre Befehlszeilenkenntnisse für die Datenverarbeitung.
3. **[Textverarbeitung und reguläre Ausdrücke](https://labex.io/de/labs/linux-text-processing-and-regular-expressions-18003)** – Lernen Sie die leistungsstarken Textverarbeitungswerkzeuge `grep`, `sed` und `awk` kennen und verwenden Sie reguläre Ausdrücke für eine effiziente Textmanipulation und Mustererkennung in Linux.

Diese Übungen helfen Ihnen, die Konzepte der Texttransformation und Dateimanipulation in realen Szenarien anzuwenden und Vertrauen im Umgang mit Linux-Befehlszeilentools aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um Tabs in Leerzeichen umzuwandeln?

## Quiz Answer

expand
