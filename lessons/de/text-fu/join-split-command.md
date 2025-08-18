---
lang: "de"
title: "join und split"
meta_title: "join und split - Text-Fu"
meta_description: "Lernen Sie, die Linux-Befehle 'join' und 'split' für die Dateimanipulation zu verwenden. Verstehen Sie, wie Dateien nach gemeinsamen Feldern kombiniert und große Dateien effizient aufgeteilt werden. Erhalten Sie praktische Beispiele und Tipps."
meta_keywords: "Linux join Befehl, Linux split Befehl, Dateimanipulation, Linux Tutorial, Kommandozeile, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Der Befehl `join` ermöglicht es Ihnen, mehrere Dateien anhand eines gemeinsamen Feldes zusammenzuführen:

Nehmen wir an, ich hätte zwei Dateien, die ich zusammenführen wollte:

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

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Sehen Sie, wie es meine Dateien zusammengeführt hat? Sie werden standardmäßig nach dem ersten Feld zusammengeführt, und die Felder müssen identisch sein. Wenn sie es nicht sind, können Sie sie sortieren. In diesem Fall werden die Dateien über 1, 2, 3 zusammengeführt.

Wie würden wir die folgenden Dateien zusammenführen?

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

Um diese Datei zusammenzuführen, müssen Sie angeben, welche Felder Sie zusammenführen. In diesem Fall möchten wir Feld 2 in `file1.txt` und Feld 1 in `file2.txt` zusammenführen, daher würde der Befehl so aussehen:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1` bezieht sich auf `file1.txt` und `-2` bezieht sich auf `file2.txt`. Ziemlich clever. Sie können eine Datei auch mit dem Befehl `split` in verschiedene Dateien aufteilen:

```bash
split somefile
```

Dies wird sie in verschiedene Dateien aufteilen. Standardmäßig werden sie aufgeteilt, sobald sie eine Grenze von 1000 Zeilen erreichen. Die Dateien werden standardmäßig `x**` genannt.

## Exercise

Führen Sie zwei Dateien mit einer unterschiedlichen Zeilenanzahl in jeder Datei zusammen. Was passiert?

## Quiz Question

Welchen Befehl würden Sie verwenden, um Dateien namens `cat`, `dog`, `cow` zusammenzuführen?

## Quiz Answer

join cat dog cow
