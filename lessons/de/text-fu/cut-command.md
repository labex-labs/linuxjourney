---
lang: "de"
title: "cut"
description: "Lernen Sie, wie Sie den Linux-Befehl `cut` verwenden, um Text aus Dateien zu extrahieren. Dieses anfängerfreundliche Tutorial behandelt das Schneiden von Zeichen und Feldern. Verbessern Sie Ihre Linux-Textverarbeitungsfähigkeiten!"
keywords: "cut command, Linux Textverarbeitung, Text extrahieren, Linux Tutorial, Linux für Anfänger, cut Beispiele, Linux Anleitung"
---

## Lesson Content

Wir werden ein paar nützliche Befehle lernen, die Sie zur Textverarbeitung verwenden können. Bevor wir anfangen, erstellen wir eine Datei, mit der wir arbeiten werden. Kopieren Sie den folgenden Befehl und fügen Sie ihn ein; sobald Sie das getan haben, fügen Sie einen TAB zwischen "lazy" und "dog" ein (halten Sie Strg-v + TAB gedrückt).

```bash
echo 'The quick brown; fox jumps over the lazy  dog' > sample.txt
```

Der erste Befehl, den wir lernen werden, ist der `cut`-Befehl. Er extrahiert Textteile aus einer Datei.

Um Inhalte nach einer Zeichenliste zu extrahieren:

```bash
cut -c 5 sample.txt
```

Dies gibt das 5. Zeichen in jeder Zeile der Datei aus. In diesem Fall ist es "q"; beachten Sie, dass das Leerzeichen auch als Zeichen zählt.

Um die Inhalte nach einem Feld zu extrahieren, müssen wir eine kleine Änderung vornehmen:

```bash
cut -f 2 sample.txt
```

Das `-f` oder field flag schneidet Text basierend auf Feldern. Standardmäßig werden TABs als Trennzeichen verwendet, sodass alles, was durch einen TAB getrennt ist, als Feld betrachtet wird. Sie sollten "dog" als Ausgabe sehen.

Sie können das field flag mit dem delimiter flag kombinieren, um die Inhalte mit einem benutzerdefinierten Trennzeichen zu extrahieren:

```bash
cut -f 1 -d ";" sample.txt
```

Dies ändert das TAB-Trennzeichen in ein ";"-Trennzeichen, und da wir das erste Feld schneiden, sollte das Ergebnis "The quick brown" sein.

## Exercise

Was bewirkt der folgende Befehl? Warum?

```bash
cut -c 5-10 sample.txt
cut -c 5- sample.txt
cut -c -5 sample.txt
```

## Quiz Question

Welchen Befehl würden Sie verwenden, um das erste Zeichen jeder Zeile in einer Datei zu erhalten?

## Quiz Answer

cut -c 1
