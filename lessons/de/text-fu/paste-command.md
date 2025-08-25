---
index: 7
lang: "de"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl paste verwenden, um Dateizeilen zusammenzuführen. Entdecken Sie Trennzeichen und kombinieren Sie Dateien mit diesem grundlegenden Linux-Befehls-Tutorial."
meta_keywords: "Linux paste Befehl, paste Befehl Tutorial, Dateizeilen zusammenführen, Linux Befehle, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der Befehl `paste` ähnelt dem Befehl `cat`; er führt Zeilen in einer Datei zusammen. Erstellen wir eine neue Datei mit folgendem Inhalt:

```
sample2.txt
The
quick
brown
fox
```

Führen wir alle diese Zeilen zu einer Zeile zusammen:

```bash
paste -s sample2.txt
```

Das Standardtrennzeichen für `paste` ist TAB, sodass nun eine Zeile mit TABs vorhanden ist, die jedes Wort trennen.

Ändern wir dieses Trennzeichen (`-d`) in etwas Lesbareres:

```bash
paste -d ' ' -s sample2.txt
```

Jetzt sollte alles in einer Zeile stehen, durch Leerzeichen getrennt.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Textverarbeitung und Datenmanipulation in Linux zu vertiefen:

1. **[Einfache Textverarbeitung](https://labex.io/de/labs/linux-simple-text-processing-18004)** – Lernen Sie, leistungsstarke Befehle wie `tr`, `col`, `join` und `paste` zu verwenden, um Textdaten effizient zu manipulieren und zu analysieren.
2. **[Datenstromumleitung](https://labex.io/de/labs/linux-data-stream-redirection-17995)** – Lernen Sie die Kunst der Linux-Stream-Umleitung und wie man Standardeingabe-, -ausgabe- und Fehlerströme manipuliert, was grundlegend für das Verständnis der Funktionsweise von Befehlen wie `paste` ist.
3. **[Ablaufsteuerung und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** – Lernen Sie, Befehlsausführungssequenzen zu steuern und Pipelines zu nutzen, wodurch Sie `paste` mit anderen Befehlen für komplexe Datenaufgaben kombinieren können.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textverarbeitung und Datenverarbeitung unter Linux aufzubauen.

## Quiz Question

Welches Flag verwenden Sie mit `paste`, um alles in eine Zeile zu bringen?

## Quiz Answer

-s
