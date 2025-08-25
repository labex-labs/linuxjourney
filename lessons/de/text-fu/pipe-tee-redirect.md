---
index: 4
lang: "de"
title: "pipe und tee"
meta_title: "pipe und tee - Text-Fu"
meta_description: "Lernen Sie Linux-Pipes und den tee-Befehl für einen effizienten Datenfluss in der Befehlszeile. Verstehen Sie stdout, stdin und Dateiausgabe. Verbessern Sie Ihre Linux-Kenntnisse!"
meta_keywords: "Linux pipe, tee command, Linux tutorial, stdout, stdin, beginner Linux, command line, Linux guide"
---

## Lesson Content

Lassen Sie uns jetzt etwas "installieren", nicht wirklich, aber irgendwie. Versuchen wir einen Befehl:

```bash
ls -la /etc
```

Sie sollten eine sehr lange Liste von Elementen sehen; es ist tatsächlich etwas schwer zu lesen. Anstatt diese Ausgabe in eine Datei umzuleiten, wäre es nicht schön, wenn wir die Ausgabe einfach in einem anderen Befehl wie `less` sehen könnten? Nun, das können wir!

```bash
ls -la /etc | less
```

Der Pipe-Operator `|`, dargestellt durch einen vertikalen Balken, ermöglicht es uns, die `stdout` eines Befehls zu erhalten und diese zur `stdin` eines anderen Prozesses zu machen. In diesem Fall haben wir die `stdout` von `ls -la /etc` genommen und sie dann an den Befehl `less` _weitergeleitet_. Der Pipe-Befehl ist äußerst nützlich, und wir werden ihn für alle Ewigkeit weiter verwenden.

Was aber, wenn ich die Ausgabe meines Befehls in zwei verschiedene Streams schreiben wollte? Das ist mit dem Befehl `tee` möglich:

```bash
ls | tee peanuts.txt
```

Sie sollten die Ausgabe von `ls` auf Ihrem Bildschirm sehen, und wenn Sie die Datei `peanuts.txt` öffnen, sollten Sie die gleichen Informationen sehen!

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Ein-/Ausgabeumleitung und Pipelines zu vertiefen:

1. **[Eingabe und Ausgabe in Linux umleiten](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** – Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie die Standardausgabe (stdout), Standardfehler (stderr) und Standardeingabe (stdin) mithilfe von Operatoren wie `>`, `>>`, `2>` und dem Befehl `tee` manipulieren.
2. **[Sequenzsteuerung und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** – Lernen Sie, die Ausführungssequenzen von Befehlen zu steuern, Pipelines zu nutzen und leistungsstarke Textverarbeitungswerkzeuge wie `cut`, `grep`, `wc`, `sort` und `uniq` einzusetzen.
3. **[Datenstromumleitung](https://labex.io/de/labs/linux-data-stream-redirection-17995)** – Lernen Sie die Kunst der Linux-Stream-Umleitung, einschließlich der Manipulation von Standardeingabe-, -ausgabe- und -fehlerströmen, der Kombination von Ausgaben und der Verwendung von `/dev/null`.

Diese Übungen helfen Ihnen, die Konzepte des Piping und der Umleitung in realen Szenarien anzuwenden und Vertrauen in die Datenmanipulation über die Befehlszeile aufzubauen.

## Quiz Question

Welche Taste stellt den Pipe-Operator dar?

## Quiz Answer

|
