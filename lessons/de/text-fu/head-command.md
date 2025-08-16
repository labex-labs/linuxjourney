---
title: "head"
description: "Erfahren Sie, wie Sie den Linux-Befehl 'head' verwenden, um den Anfang von Dateien anzuzeigen. Verstehen Sie Optionen wie -n für die Zeilenanzahl. Ein unverzichtbares Linux-Befehls-Tutorial."
keywords: "head Befehl, Linux head, Dateianfang anzeigen, Linux Tutorial, Linux Befehle, Linux für Anfänger, head -n, Linux Anleitung"
---

## Lesson Content

Nehmen wir an, wir haben eine sehr lange Datei; tatsächlich haben wir viele zur Auswahl. Führen Sie `cat /var/log/syslog` aus. Sie sollten seitenweise Text sehen. Was wäre, wenn ich nur die ersten paar Zeilen dieser Textdatei sehen wollte? Nun, das können wir mit dem `head`-Befehl tun. Standardmäßig zeigt Ihnen der `head`-Befehl die ersten 10 Zeilen einer Datei an.

```bash
head /var/log/syslog
```

Sie können die Zeilenanzahl auch nach Belieben ändern. Nehmen wir an, ich wollte stattdessen die ersten 15 Zeilen sehen.

```bash
head -n 15 /var/log/syslog
```

Das Flag `-n` steht für "number of lines" (Anzahl der Zeilen).

## Exercise

Was bewirkt der folgende Befehl und warum?

```bash
head -c 15 /var/log/syslog
```

## Quiz Question

Welches Flag würden Sie verwenden, um die Anzahl der Zeilen zu ändern, die Sie für den `head`-Befehl anzeigen möchten?

## Quiz Answer

-n
