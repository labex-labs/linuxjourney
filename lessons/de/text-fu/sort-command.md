---
index: 12
lang: "de"
title: "sort"
meta_title: "sort - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl sort zum Sortieren von Textdateien verwenden. Entdecken Sie Optionen wie umgekehrte und numerische Sortierung. Verbessern Sie Ihre Linux-Befehlszeilenkenntnisse!"
meta_keywords: "Linux sort Befehl, sort -r, sort -n, Linux Tutorial, Befehlszeile, Linux für Anfänger, sort Anleitung"
---

## Lesson Content

Der Befehl `sort` ist nützlich zum Sortieren von Zeilen.

```plaintext
file1.txt
dog
cow
cat
elephant
bird

$ sort file1.txt
bird
cat
cow
dog
elephant
```

Sie können auch eine umgekehrte Sortierung vornehmen:

```bash
$ sort -r file1.txt
elephant
dog
cow
cat
bird
```

Und auch nach numerischem Wert sortieren:

```bash
$ sort -n file1.txt
bird
cat
cow
elephant
dog
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des `sort`-Befehls und der Textverarbeitung zu vertiefen:

1. **[Linux sort Befehl: Textsortierung](https://labex.io/de/labs/linux-linux-sort-command-text-sorting-219196)** - Dieses Lab bietet eine direkte Einführung in den `sort`-Befehl, sodass Sie das Sortieren von Textdateizeilen auf verschiedene Weisen üben können, einschließlich aufsteigender und absteigender Reihenfolge.
2. **[Wortzählung und Sortierung](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** - In dieser Herausforderung wenden Sie Ihr Wissen über Sortierung zusammen mit der Wortzählung an, um Textdaten zu analysieren, was Ihnen hilft, häufige Muster zu finden und Daten effizient zu sortieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textmanipulation und Sortierung unter Linux aufzubauen.

## Quiz Question

Welches Flag verwenden Sie, um eine umgekehrte Sortierung durchzuführen?

## Quiz Answer

-r
