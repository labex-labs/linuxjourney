---
index: 1
lang: "de"
title: "regex (Reguläre Ausdrücke)"
meta_title: "regex (Reguläre Ausdrücke) - Fortgeschrittene Text-Fu"
meta_description: "Lernen Sie reguläre Ausdrücke (regex) für den Musterabgleich unter Linux. Verstehen Sie die Regex-Syntax wie ^, $, . und [] für die Textmanipulation. Verbessern Sie Ihre grep-Fähigkeiten!"
meta_keywords: "reguläre Ausdrücke, regex, Linux regex, grep regex, Musterabgleich, regex Tutorial, Linux Befehle, Anfänger"
---

## Lesson Content

Reguläre Ausdrücke sind ein mächtiges Werkzeug für die musterbasierte Auswahl. Sie verwenden spezielle Notationen, die denen ähneln, denen wir bereits begegnet sind, wie dem `*`-Platzhalter.

Wir werden einige der gebräuchlichsten regulären Ausdrücke durchgehen; diese sind in fast jeder Programmiersprache universell einsetzbar.

Wir werden diesen Satz als Teststring verwenden:

```plaintext
sally sells seashells
by the seashore
```

### 1. Zeilenanfang mit ^

```plaintext
^by
would match the line "by the seashore"
```

### 2. Zeilenende mit $

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. Beliebiges einzelnes Zeichen abgleichen mit

```plaintext
b.
would match by
```

### 4. Klammernotation mit [] und ()

Das kann etwas knifflig sein. Klammern ermöglichen es uns, Zeichen anzugeben, die innerhalb der Klammer gefunden werden.

```plaintext
d[iou]g
would match: dig, dog, dug
```

Der vorherige Anker-Tag `^` bedeutet, wenn er in einer Klammer verwendet wird, alles außer den Zeichen innerhalb der Klammer.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

Klammern können auch Bereiche verwenden, um die Anzahl der Zeichen zu erhöhen, die Sie verwenden möchten.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

Seien Sie jedoch vorsichtig, da Klammern Groß- und Kleinschreibung beachten:

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

Und das sind einige grundlegende reguläre Ausdrücke.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von regulären Ausdrücken und Musterabgleich zu vertiefen:

1. **[Text mit grep in Linux suchen](https://labex.io/de/labs/comptia-search-text-with-grep-in-linux-590841)** - In diesem Lab lernen Sie, Text in Dateien auf einem Linux-System mit dem Befehl `grep` zu suchen. Sie werden grundlegende Suchen durchführen, Zeilennummern anzeigen, Anker wie `^` und `$` verwenden, um Zeilenpositionen abzugleichen, und sowohl grundlegende als auch erweiterte reguläre Ausdrücke für komplexe Musterabgleiche nutzen.
2. **[Textverarbeitung und reguläre Ausdrücke](https://labex.io/de/labs/linux-text-processing-and-regular-expressions-18003)** - Lernen Sie die leistungsstarken Textverarbeitungswerkzeuge grep, sed und awk. Lernen Sie, reguläre Ausdrücke für effiziente Textmanipulation und Musterabgleich in Linux zu verwenden.
3. **[Extrahieren von E-Mails und Nummern](https://labex.io/de/labs/linux-extracting-mails-and-numbers-17991)** - In dieser Herausforderung lernen Sie, wie Sie grep und reguläre Ausdrücke verwenden, um E-Mail-Adressen und Nummern aus einer Datei zu extrahieren, und demonstrieren dabei grundlegende Linux-Textverarbeitungsfähigkeiten.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit regulären Ausdrücken und der Textverarbeitung aufzubauen.

## Quiz Question

Welchen regulären Ausdruck würden Sie verwenden, um ein einzelnes Zeichen abzugleichen?

## Quiz Answer

.
