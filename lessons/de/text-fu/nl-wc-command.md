---
index: 15
lang: "de"
title: "wc und nl"
meta_title: "wc und nl - Text-Fu"
meta_description: "Lernen Sie die Linux-Befehle wc und nl. Verstehen Sie Wortzählung, Zeilennummerierung und Dateianalyse. Verbessern Sie noch heute Ihre Linux-Befehlszeilenkenntnisse!"
meta_keywords: "wc Befehl, nl Befehl, Linux Wortzählung, Linux Zeilennummern, Dateianalyse, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der Befehl `wc` (word count) zeigt die Gesamtzahl der Wörter in einer Datei an.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Er zeigt die Anzahl der Zeilen, die Anzahl der Wörter bzw. die Anzahl der Bytes an.

Um nur die Anzahl eines bestimmten Feldes anzuzeigen, verwenden Sie die Optionen `-l`, `-w` oder `-c`.

```bash
$ wc -l /etc/passwd
96
```

Ein weiterer Befehl, den Sie verwenden können, um die Anzahl der Zeilen in einer Datei zu überprüfen, ist der Befehl `nl` (number lines).

```plaintext
file1.txt
i
like
turtles
```

```bash
$ nl file1.txt
1. i
2. like
3. turtles
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Textzählung und Zeilennummerierung unter Linux zu vertiefen:

1. **[Linux wc Befehl: Textzählung](https://labex.io/de/labs/linux-linux-wc-command-text-counting-219200)** – Üben Sie das Zählen von Wörtern, Zeilen und Zeichen in Textdateien mit dem Befehl `wc`.
2. **[Linux nl Befehl: Zeilennummerierung](https://labex.io/de/labs/linux-linux-nl-command-line-numbering-210988)** – Lernen Sie, Zeilen in Textdateien mit dem Befehl `nl` zu nummerieren.
3. **[Wortzählung und Sortierung](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** – Wenden Sie Ihr Wissen über `wc` an, um Zeilen, Wörter und Zeichen zu zählen, und kombinieren Sie es mit der Sortierung für praktische Textanalyseaufgaben.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textverarbeitung unter Linux aufzubauen.

## Quiz Question

Welchen Befehl würden Sie verwenden, um die Gesamtzahl der Wörter in einer Datei und nur die Wörter zu erhalten?

## Quiz Answer

wc -w
