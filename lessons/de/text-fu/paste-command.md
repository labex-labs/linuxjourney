---
title: "paste"
description: "Lernen Sie, wie Sie den Linux-Befehl paste verwenden, um Dateizeilen zusammenzuführen. Entdecken Sie Trennzeichen und kombinieren Sie Dateien mit diesem grundlegenden Linux-Befehls-Tutorial."
keywords: "Linux paste Befehl, paste Befehl Tutorial, Dateizeilen zusammenführen, Linux Befehle, Linux für Anfänger, Linux Anleitung"
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

Jetzt sollte alles in einer Zeile stehen, getrennt durch Leerzeichen.

## Exercise

Versuchen Sie, mehrere Dateien zusammenzufügen. Was passiert?

## Quiz Question

Welches Flag verwenden Sie mit `paste`, um alles in eine Zeile zu bringen?

## Quiz Answer

-s
