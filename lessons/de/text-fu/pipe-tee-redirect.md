---
title: "pipe und tee"
description: "Lernen Sie Linux-Pipes und den tee-Befehl für einen effizienten Datenfluss in der Befehlszeile. Verstehen Sie stdout, stdin und Dateiausgabe. Verbessern Sie Ihre Linux-Kenntnisse!"
keywords: "Linux Pipe, tee Befehl, Linux Tutorial, stdout, stdin, Linux für Anfänger, Befehlszeile, Linux Anleitung"
---

## Lesson Content

Lassen Sie uns jetzt etwas „Klempnerarbeit“ leisten, nicht wirklich, aber irgendwie. Probieren wir einen Befehl aus:

```bash
ls -la /etc
```

Sie sollten eine sehr lange Liste von Elementen sehen; sie ist tatsächlich etwas schwer zu lesen. Anstatt diese Ausgabe in eine Datei umzuleiten, wäre es nicht schön, wenn wir die Ausgabe einfach in einem anderen Befehl wie `less` sehen könnten? Nun, das können wir!

```bash
ls -la /etc | less
```

Der Pipe-Operator `|`, dargestellt durch einen vertikalen Balken, ermöglicht es uns, den `stdout` eines Befehls zu erhalten und diesen zum `stdin` eines anderen Prozesses zu machen. In diesem Fall haben wir den `stdout` von `ls -la /etc` genommen und ihn dann an den `less`-Befehl _weitergeleitet_. Der Pipe-Befehl ist äußerst nützlich, und wir werden ihn für alle Ewigkeit weiter verwenden.

Was aber, wenn ich die Ausgabe meines Befehls in zwei verschiedene Streams schreiben wollte? Das ist mit dem `tee`-Befehl möglich:

```bash
ls | tee peanuts.txt
```

Sie sollten die Ausgabe von `ls` auf Ihrem Bildschirm sehen, und wenn Sie die Datei `peanuts.txt` öffnen, sollten Sie die gleichen Informationen sehen!

## Exercise

Probieren Sie die folgenden Befehle aus:

```bash
ls | tee peanuts.txt banan.txt
```

## Quiz Question

Welche Taste repräsentiert den Pipe-Operator?

## Quiz Answer

|
