---
index: 3
lang: "de"
title: "stderr (Standardfehler)"
meta_title: "stderr (Standardfehler) - Text-Fu"
meta_description: "Erfahren Sie mehr über Linux stderr (Standardfehler) Umleitung. Verstehen Sie 2>, 2>&1, &> und /dev/null für die Fehlerbehandlung in Bash. Verbessern Sie Ihre Linux-Befehlszeilenkenntnisse!"
meta_keywords: "Linux stderr, Standardfehler, 2> Umleitung, 2>&1, &> Umleitung, /dev/null, Bash Fehlerbehandlung, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Versuchen wir nun etwas anderes. Versuchen wir, den Inhalt eines Verzeichnisses aufzulisten, das auf Ihrem System nicht existiert, und leiten die Ausgabe wieder in die Datei `peanuts.txt` um.

```bash
ls /fake/directory > peanuts.txt
```

Was Sie sehen sollten, ist:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Jetzt denken Sie wahrscheinlich, sollte diese Nachricht nicht an die Datei gesendet worden sein? Hier ist tatsächlich ein weiterer E/A-Stream im Spiel, der Standardfehler (stderr) genannt wird. Standardmäßig sendet stderr seine Ausgabe ebenfalls an den Bildschirm; es ist ein völlig anderer Stream als stdout. Sie müssen seine Ausgabe also auf eine andere Weise umleiten.

Leider ist der Redirector nicht so schön wie die Verwendung von `<` oder `>`, aber er ist ziemlich nah dran. Wir müssen Dateideskriptoren verwenden. Ein Dateideskriptor ist eine nicht-negative Zahl, die verwendet wird, um auf eine Datei oder einen Stream zuzugreifen. Wir werden dies später ausführlich behandeln, aber vorerst sollten Sie wissen, dass der Dateideskriptor für stdin, stdout und stderr 0, 1 bzw. 2 ist.

Wenn wir nun unseren stderr in die Datei umleiten möchten, können wir dies tun:

```bash
ls /fake/directory 2> peanuts.txt
```

Sie sollten nur die stderr-Nachrichten in `peanuts.txt` sehen.

Was ist, wenn ich sowohl stderr als auch stdout in der Datei `peanuts.txt` sehen möchte? Dies ist auch mit Dateideskriptoren möglich:

```bash
ls /fake/directory > peanuts.txt 2>&1
```

Dies sendet die Ergebnisse von `ls /fake/directory` an die Datei `peanuts.txt` und leitet dann stderr über `2>&1` an stdout um. Die Reihenfolge der Operationen ist hier wichtig; `2>&1` sendet stderr an das, worauf stdout zeigt. In diesem Fall zeigt stdout auf eine Datei, daher sendet `2>&1` stderr ebenfalls an eine Datei. Wenn Sie also die Datei `peanuts.txt` öffnen, sollten Sie sowohl stderr als auch stdout sehen. In unserem Fall gibt der obige Befehl nur stderr aus.

Es gibt eine kürzere Möglichkeit, sowohl stdout als auch stderr in eine Datei umzuleiten:

```bash
ls /fake/directory &> peanuts.txt
```

Was ist, wenn ich all diesen Müll nicht will und stderr-Nachrichten komplett loswerden möchte? Nun, Sie können die Ausgabe auch in eine spezielle Datei namens `/dev/null` umleiten, und sie wird jede Eingabe verwerfen.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Ein-/Ausgabeumleitung zu vertiefen:

1. **[Ein- und Ausgabe in Linux umleiten](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** – In diesem Lab lernen Sie, Ein- und Ausgabe in der Linux-Shell umzuleiten. Sie üben die Steuerung des Datenflusses von Befehlen, indem Sie die Standardausgabe (stdout), den Standardfehler (stderr) und die Standardeingabe (stdin) mit Operatoren wie >, >>, 2> und dem Befehl tee manipulieren.

Dieses Lab hilft Ihnen, die Konzepte der E/A-Umleitung in realen Szenarien anzuwenden und Vertrauen im Umgang mit Datenströmen in Linux aufzubauen.

## Quiz Question

Was ist der Redirector für stderr?

## Quiz Answer

2>
