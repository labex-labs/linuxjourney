---
index: 2
lang: "de"
title: "stdin (Standard In)"
meta_title: "stdin (Standard In) - Text-Fu"
meta_description: "Erfahren Sie mehr über stdin (Standardeingabe) Umleitung in Linux. Verstehen Sie, wie der '<'-Operator mit Dateien und Befehlen verwendet wird. Entdecken Sie praktische Beispiele und verbessern Sie Ihre Linux-Befehlszeilenkenntnisse."
meta_keywords: "stdin, Standardeingabe, Linux-Umleitung, < Operator, Linux-Tutorial, Befehlszeile, Anfänger, Anleitung"
---

## Lesson Content

In unserer vorherigen Lektion haben wir gelernt, dass wir verschiedene stdout-Streams verwenden können, wie z.B. eine Datei oder den Bildschirm. Nun, es gibt auch verschiedene Standard-Input-Streams (stdin), die wir ebenfalls verwenden können. Wir wissen, dass wir stdin von Geräten wie der Tastatur haben, aber wir können auch Dateien, die Ausgabe anderer Prozesse und das Terminal verwenden. Sehen wir uns ein Beispiel an.

Verwenden wir für dieses Beispiel die Datei `peanuts.txt` aus der vorherigen Lektion. Erinnern Sie sich, sie enthielt den Text "Hello World".

```bash
cat < peanuts.txt > banana.txt
```

So wie wir `>` für die stdout-Umleitung hatten, können wir `<` für die stdin-Umleitung verwenden.

Normalerweise sendet man beim `cat`-Befehl eine Datei an ihn, und diese Datei wird zum stdin. In diesem Fall haben wir `peanuts.txt` als unseren stdin umgeleitet. Dann wird die Ausgabe von `cat peanuts.txt`, die "Hello World" wäre, in eine andere Datei namens `banana.txt` umgeleitet.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Eingabe- und Ausgabeumleitung in Linux zu vertiefen:

1. **[Eingabe und Ausgabe in Linux umleiten](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie die Standardausgabe (stdout), die Standardfehlerausgabe (stderr) und die Standardeingabe (stdin) mit Operatoren wie >, >>, 2> und dem Befehl tee manipulieren.
2. **[Datenstrom-Umleitung](https://labex.io/de/labs/linux-data-stream-redirection-17995)** - Lernen Sie die Kunst der Linux-Stream-Umleitung. Manipulieren Sie Standardeingabe-, -ausgabe- und -fehlerströme, kombinieren Sie Ausgaben und nutzen Sie /dev/null für fortgeschrittene Dateivorgänge.
3. **[Sequenzsteuerung und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** - Lernen Sie, Befehlsausführungssequenzen zu steuern und Pipelines zu nutzen, die grundlegend sind, um die Ausgabe eines Befehls als Eingabe für einen anderen zu leiten.

Diese Labs helfen Ihnen, die Konzepte der Eingabe- und Ausgabeumleitung in realen Szenarien anzuwenden und Vertrauen in die Shell-Skripterstellung und Datenmanipulation aufzubauen.

## Quiz Question

Welchen Umleitungsoperator verwenden Sie, um stdin umzuleiten?

## Quiz Answer

<
