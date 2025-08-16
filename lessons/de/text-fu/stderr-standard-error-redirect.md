---
lang: "de"
title: "stderr (Standardfehler)"
description: "Erfahren Sie mehr über die Umleitung von Linux stderr (Standardfehler). Verstehen Sie 2>, 2>&1, &> und /dev/null für die Fehlerbehandlung in Bash. Verbessern Sie Ihre Linux-Befehlszeilenkenntnisse!"
keywords: "Linux stderr, Standardfehler, 2> Umleitung, 2>&1, &> Umleitung, /dev/null, Bash Fehlerbehandlung, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Versuchen wir nun etwas anderes. Versuchen wir, den Inhalt eines Verzeichnisses aufzulisten, das auf Ihrem System nicht existiert, und leiten die Ausgabe erneut in die Datei `peanuts.txt` um.

```bash
ls /fake/directory > peanuts.txt
```

Was Sie sehen sollten, ist:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Jetzt denken Sie wahrscheinlich, sollte diese Nachricht nicht an die Datei gesendet worden sein? Hier ist tatsächlich ein weiterer E/A-Stream im Spiel, der als Standardfehler (stderr) bezeichnet wird. Standardmäßig sendet stderr seine Ausgabe ebenfalls an den Bildschirm; es ist ein völlig anderer Stream als stdout. Sie müssen seine Ausgabe also auf eine andere Weise umleiten.

Leider ist der Redirector nicht so angenehm wie die Verwendung von `<` oder `>`, aber er ist ziemlich nah dran. Wir müssen Dateideskriptoren verwenden. Ein Dateideskriptor ist eine nicht-negative Zahl, die verwendet wird, um auf eine Datei oder einen Stream zuzugreifen. Wir werden dies später ausführlich behandeln, aber vorerst sollten Sie wissen, dass der Dateideskriptor für stdin, stdout und stderr 0, 1 bzw. 2 ist.

Wenn wir nun unseren stderr in die Datei umleiten möchten, können wir dies tun:

```bash
ls /fake/directory 2> peanuts.txt
```

Sie sollten nur die stderr-Nachrichten in `peanuts.txt` sehen.

Was aber, wenn ich sowohl stderr als auch stdout in der Datei `peanuts.txt` sehen möchte? Dies ist auch mit Dateideskriptoren möglich:

```bash
ls /fake/directory > peanuts.txt 2>&1
```

Dies sendet die Ergebnisse von `ls /fake/directory` an die Datei `peanuts.txt` und leitet dann stderr über `2>&1` an stdout um. Die Reihenfolge der Operationen ist hier wichtig; `2>&1` sendet stderr an das, worauf stdout zeigt. In diesem Fall zeigt stdout auf eine Datei, daher sendet `2>&1` auch stderr an eine Datei. Wenn Sie also die Datei `peanuts.txt` öffnen, sollten Sie sowohl stderr als auch stdout sehen. In unserem Fall gibt der obige Befehl nur stderr aus.

Es gibt eine kürzere Möglichkeit, sowohl stdout als auch stderr in eine Datei umzuleiten:

```bash
ls /fake/directory &> peanuts.txt
```

Was aber, wenn ich all diesen Müll nicht will und stderr-Nachrichten komplett loswerden möchte? Nun, Sie können die Ausgabe auch in eine spezielle Datei namens `/dev/null` umleiten, und sie wird jede Eingabe verwerfen.

```bash
ls /fake/directory 2> /dev/null
```

## Exercise

Was bewirkt der folgende Befehl?

```bash
ls /fake/directory >> /dev/null 2>&1
```

## Quiz Question

Was ist der Redirector für stderr?

## Quiz Answer

2>
