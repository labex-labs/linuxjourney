---
index: 2
lang: "de"
title: "stdin (Standardeingabe)"
meta_title: "stdin (Standardeingabe) - Text-Fu"
meta_description: "Meistern Sie Linux-Befehlszeilenoperationen, indem Sie lernen, wie man stdin (Standardeingabe) umleitet. Dieser Leitfaden behandelt die Beziehung zwischen stdin und stdout, die Verwendung des '<'-Operators und praktische Beispiele wie 'cat stdin', um Datenströme effektiv zu verwalten."
meta_keywords: "stdin, standardeingabe, stdin umleiten, cat stdin, stdin und stdout, Standardeingabe, Linux-Umleitung, Befehlszeile, Eingabestrom"
---

## Lesson Content

In unserer vorherigen Lektion haben wir gelernt, wie man den Standardausgabe-Stream (stdout) umleitet. Ähnlich können wir auch den Standardeingabe-Stream (`stdin`) verwalten. Standardmäßig empfängt ein Programm seine `stdin` von der Tastatur, aber wir können auch Dateien oder die Ausgabe anderer Prozesse als Eingabequelle verwenden.

### Verständnis von stdin und stdout

Jeder Kommandozeilenprozess unter Linux arbeitet mit mindestens zwei grundlegenden Datenströmen: Standardeingabe (`stdin`) und Standardausgabe (`stdout`). Ein Programm liest Daten von `stdin` und schreibt seine Ergebnisse nach `stdout`. Das Verständnis, wie man sowohl `stdin als auch stdout` steuert, ist entscheidend für effektives Arbeiten in der Kommandozeile.

### Wie man stdin umleitet

So wie wir `>` für die stdout-Umleitung verwenden, nutzen wir den Operator `<` zur `Umleitung von stdin`. Diese leistungsstarke Funktion ermöglicht es Ihnen, einem Befehl mitzuteilen, seine Eingabe aus einer Datei zu lesen, anstatt darauf zu warten, dass Sie sie auf der Tastatur eingeben. Dies ist ein Kernkonzept der Eingabeumleitung.

### Praktisches Beispiel mit cat stdin

Betrachten wir erneut die Datei `peanuts.txt` aus der vorherigen Lektion, die den Text "Hello World" enthält. Betrachten Sie den folgenden Befehl:

```bash
cat < peanuts.txt > banana.txt
```

Hier ist eine Aufschlüsselung dessen, was passiert:

1.  Der Teil `< peanuts.txt` weist die Shell an, die `stdin` für den `cat`-Befehl umzuleiten, sodass dieser aus `peanuts.txt` liest anstatt von der Tastatur.
2.  Der `cat`-Befehl verarbeitet seine Eingabe. In diesem Fall bedeutet die Verwendung von `cat stdin`, dass der Inhalt von `peanuts.txt` gelesen wird.
3.  Der Teil `> banana.txt` leitet die Standardausgabe von `cat` in eine neue Datei namens `banana.txt` um.

Letztendlich wird der Inhalt von `peanuts.txt` nach `banana.txt` kopiert. Dieses Beispiel demonstriert effektiv, wie man sowohl `stdin als auch stdout` in einem einzigen, effizienten Befehl verwaltet.

## Exercise

Um Ihr Verständnis zu festigen, versuchen Sie diese praktischen Übungen, die sich auf die Eingabe- und Ausgabeumleitung in Linux konzentrieren:

1.  **[Eingabe- und Ausgabeumleitung in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie Standardausgabe (stdout), Standardfehler (stderr) und Standardeingabe (stdin) mithilfe von Operatoren wie >, >>, 2> und dem tee-Befehl manipulieren.
2.  **[Datenstromumleitung](https://labex.io/de/labs/linux-data-stream-redirection-17995)** - Lernen Sie die Kunst der Linux-Stream-Umleitung. Manipulieren Sie Standardeingabe-, Ausgabe- und Fehlerströme, kombinieren Sie Ausgaben und nutzen Sie /dev/null für erweiterte Dateioperationen.
3.  **[Sequenzsteuerung und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** - Lernen Sie, Befehlsausführungssequenzen zu steuern und Pipelines zu nutzen, die grundlegend dafür sind, die Ausgabe eines Befehls als Eingabe für einen anderen weiterzuleiten.

Diese Labs helfen Ihnen, die Konzepte der Eingabe- und Ausgabeumleitung in realen Szenarien anzuwenden und Vertrauen in Shell-Skripte und Datenmanipulation aufzubauen.

## Quiz Question

Welcher Operator wird verwendet, um stdin umzuleiten? Bitte antworten Sie nur mit dem erforderlichen Symbol.

## Quiz Answer

<
