---
title: "stdin (Standardeingabe)"
description: "Erfahren Sie mehr über die stdin (Standardeingabe)-Umleitung in Linux. Verstehen Sie, wie der Operator '<' mit Dateien und Befehlen verwendet wird. Entdecken Sie praktische Beispiele und verbessern Sie Ihre Linux-Kommandozeilenkenntnisse."
keywords: "stdin, Standardeingabe, Linux-Umleitung, < Operator, Linux-Tutorial, Kommandozeile, Anfänger, Anleitung"
---

## Lesson Content

In unserer vorherigen Lektion haben wir gelernt, dass wir verschiedene stdout-Streams verwenden können, wie z.B. eine Datei oder den Bildschirm. Nun, es gibt auch verschiedene Standard-Input (stdin)-Streams, die wir verwenden können. Wir wissen, dass wir stdin von Geräten wie der Tastatur haben, aber wir können auch Dateien, die Ausgabe anderer Prozesse und das Terminal verwenden. Sehen wir uns ein Beispiel an.

Verwenden wir für dieses Beispiel die Datei `peanuts.txt` aus der vorherigen Lektion. Erinnern Sie sich, sie enthielt den Text "Hello World".

```bash
cat < peanuts.txt > banana.txt
```

So wie wir `>` für die stdout-Umleitung hatten, können wir `<` für die stdin-Umleitung verwenden.

Normalerweise sendet man bei dem Befehl `cat` eine Datei an ihn, und diese Datei wird zum stdin. In diesem Fall haben wir `peanuts.txt` als unser stdin umgeleitet. Dann wird die Ausgabe von `cat peanuts.txt`, die "Hello World" wäre, in eine andere Datei namens `banana.txt` umgeleitet.

## Exercise

Probieren Sie ein paar Befehle aus:

```bash
echo < peanuts.txt > banana.txt
ls < peanuts.txt > banana.txt
pwd < peanuts.txt > banana.txt
```

## Quiz Question

Welchen Redirector verwenden Sie, um stdin umzuleiten?

## Quiz Answer

<
