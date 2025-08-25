---
index: 14
lang: "de"
title: "uniq (Unique)"
meta_title: "uniq (Unique) - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl `uniq` verwenden, um doppelte Zeilen aus Textdateien zu entfernen. Entdecken Sie Optionen wie -c, -u, -d und kombinieren Sie ihn mit `sort` für eine effektive Datenbereinigung."
meta_keywords: "uniq Befehl, Linux uniq, Duplikate entfernen, sort uniq, Linux Tutorial, Textverarbeitung, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der Befehl `uniq` (unique) ist ein weiteres nützliches Werkzeug zum Parsen von Text.

Nehmen wir an, Sie hätten eine Datei mit vielen Duplikaten:

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

Und Sie wollten die Duplikate entfernen; nun, Sie können den Befehl `uniq` verwenden:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Lassen Sie uns die Anzahl der Vorkommen einer Zeile ermitteln:

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Lassen Sie uns nur eindeutige Werte erhalten:

```bash
$ uniq -u reading.txt
magazine
```

Lassen Sie uns nur doppelte Werte erhalten:

```bash
$ uniq -d reading.txt
book
paper
article
```

**Hinweis**: `uniq` erkennt doppelte Zeilen nur, wenn sie nebeneinander liegen. Zum Beispiel:

Nehmen wir an, Sie hätten eine Datei mit Duplikaten, die nicht nebeneinander liegen:

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

Das von `uniq` zurückgegebene Ergebnis enthält alle Einträge, im Gegensatz zum allerersten Beispiel.

Um diese Einschränkung von `uniq` zu überwinden, können wir `sort` in Kombination mit `uniq` verwenden:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Textverarbeitung mit `uniq` und `sort` zu vertiefen:

1. **[Linux uniq Command: Duplicate Filtering](https://labex.io/de/labs/linux-linux-uniq-command-duplicate-filtering-219199)** – Erfahren Sie, wie Sie den Linux-Befehl `uniq` in Kombination mit `sort` verwenden, um doppelte Zeilen in Textdateien zu identifizieren, zu filtern und zu analysieren.
2. **[Linux sort Command: Text Sorting](https://labex.io/de/labs/linux-linux-sort-command-text-sorting-219196)** – Üben Sie die Verwendung des Befehls `sort`, um Zeilen von Textdateien zu organisieren, ein entscheidender Schritt, bevor Sie `uniq` effektiv einsetzen.
3. **[Word Count and Sorting](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** – Lernen Sie in dieser praktischen Herausforderung die wesentlichen Linux-Textverarbeitungstools `wc` (word count) und `sort` kennen. Lernen Sie, Zeilen, Wörter und Zeichen zu zählen, häufige Muster zu finden und Daten für verschiedene Textanalyseaufgaben effizient zu sortieren.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textverarbeitung und Datenmanipulation unter Linux aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um Duplikate in einer Datei zu entfernen?

## Quiz Answer

uniq
