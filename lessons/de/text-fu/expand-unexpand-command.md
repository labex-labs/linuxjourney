---
lang: "de"
title: "expand und unexpand"
description: "Lernen Sie, Tabulatoren mit dem Befehl `expand` in Leerzeichen und Leerzeichen mit `unexpand` in Tabulatoren umzuwandeln. Verbessern Sie die Formatierung von Textdateien mit diesem Linux-Tutorial."
keywords: "expand Befehl, unexpand Befehl, Linux Tabulatoren, Linux Leerzeichen, Textformatierung, Linux Tutorial, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

In unserer Lektion über den `cut`-Befehl hatten wir unsere Datei `sample.txt`, die einen Tabulator enthielt. Normalerweise würden Tabulatoren einen merklichen Unterschied zeigen, aber einige Textdateien zeigen das nicht gut genug. Tabulatoren in einer Textdatei bieten möglicherweise nicht den gewünschten Abstand. Um Ihre Tabulatoren in Leerzeichen umzuwandeln, verwenden Sie den Befehl `expand`.

```bash
expand sample.txt
```

Der obige Befehl gibt eine Ausgabe aus, bei der jeder Tabulator in eine Gruppe von Leerzeichen umgewandelt wurde. Um diese Ausgabe in einer Datei zu speichern, verwenden Sie die Ausgabenumleitung, wie unten gezeigt.

```bash
expand sample.txt > result.txt
```

Im Gegensatz zu `expand` können wir mit dem Befehl `unexpand` jede Gruppe von Leerzeichen wieder in einen Tabulator umwandeln:

```bash
unexpand -a result.txt
```

## Exercise

Was passiert, wenn Sie einfach `expand` ohne Dateieingabe eingeben?

## Quiz Question

Welcher Befehl wird verwendet, um Tabulatoren in Leerzeichen umzuwandeln?

## Quiz Answer

expand
