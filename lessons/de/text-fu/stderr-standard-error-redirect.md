---
index: 3
lang: "de"
title: "stderr (Standardfehler)"
meta_title: "stderr (Standardfehler) - Text-Fu"
meta_description: "Erfahren Sie, wie Sie Standardfehler (stderr) unter Linux verwalten. Dieser Leitfaden behandelt stderr-Umleitung, den stderr-Dateideskriptor (2) und wie man stderr mithilfe von 2>, 2>&1 und &> in eine Datei oder nach /dev/null umleitet."
meta_keywords: "stderr, Standardfehler Linux, stderr Dateideskriptor, stderr Datei, Linux Standardfehler, stderr umleiten, 2>, 2>&1, &>, /dev/null, Bash Fehlerbehandlung"
---

## Lesson Content

Erkunden wir, was passiert, wenn ein Befehl einen Fehler erzeugt. Versuchen Sie, den Inhalt eines nicht existierenden Verzeichnisses aufzulisten und die Ausgabe in eine Datei namens `peanuts.txt` umzuleiten.

```bash
ls /fake/directory > peanuts.txt
```

Anstelle eines sauberen Prompts sehen Sie eine Fehlermeldung auf Ihrem Bildschirm:

```plaintext
ls: cannot access /fake/directory: No such file or directory
```

Sie fragen sich vielleicht, warum diese Meldung nicht an die Datei gesendet wurde. Das liegt daran, dass ein anderer I/O-Stream beteiligt ist: **Standardfehler** oder **stderr**.

### Was ist Standardfehler (Standard Error) in Linux?

In Linux ist `stderr` ein Standard-Ausgabestrom, den Programme verwenden, um Fehlermeldungen und Diagnosen zu senden. Er ist vollständig getrennt vom Standardausgabe (`stdout`) -Stream, der für normale Programmausgaben verwendet wird. Standardmäßig senden sowohl `stdout` als auch `stderr` ihre Ausgaben an Ihren Terminalbildschirm, weshalb Sie die Fehlermeldung direkt sehen.

Um `stderr` zu steuern, benötigen Sie eine andere Umleitungsmethode.

### Verständnis von Dateideskriptoren

Um I/O-Streams wie `stdin`, `stdout` und `stderr` zu verwalten, verwendet das System Dateideskriptoren. Ein **Dateideskriptor** ist eine nicht-negative Zahl, die der Kernel verwendet, um eine geöffnete Datei oder einen Stream zu identifizieren. Die Standard-Dateideskriptoren sind:

- `0`: stdin (Standardeingabe)
- `1`: stdout (Standardausgabe)
- `2`: stderr (Standardfehler)

Die Zahl `2` ist der dedizierte **stderr-Dateideskriptor**, und wir können sie verwenden, um zu steuern, wohin Fehlermeldungen gesendet werden.

### Umleitung von stderr in eine Datei

Um `stderr` in eine Datei umzuleiten, verwenden Sie den Dateideskriptor `2` gefolgt vom `>` -Operator. Dieser Befehl sendet alle Fehlermeldungen in die angegebene **stderr-Datei**.

```bash
ls /fake/directory 2> peanuts.txt
```

Jetzt bleibt Ihr Terminal stumm, und die Fehlermeldung befindet sich in `peanuts.txt`.

### Kombination von stdout und stderr

Was ist, wenn Sie sowohl normale Ausgabe als auch Fehlermeldungen in derselben Datei erfassen möchten? Dies können Sie erreichen, indem Sie beide Streams umleiten.

```bash
ls /fake/directory /etc/passwd > peanuts.txt 2>&1
```

Lassen Sie uns das aufschlüsseln:

1. `> peanuts.txt` leitet `stdout` (Dateideskriptor 1) in die Datei `peanuts.txt` um.
2. `2>&1` leitet `stderr` (Dateideskriptor 2) an denselben Ort um, auf den `stdout` (Dateideskriptor 1) gerade zeigt.

Die Reihenfolge ist wichtig. `2>&1` sendet `stderr` an das aktuelle Ziel von `stdout`. In diesem Fall zeigt `stdout` auf eine Datei, daher wird auch `stderr` an diese Datei gesendet.

Eine modernere und kürzere Methode, sowohl `stdout` als auch `stderr` umzuleiten, ist die Verwendung von `&>`.

```bash
ls /fake/directory /etc/passwd &> peanuts.txt
```

### Verwerfen von Fehlermeldungen

Manchmal möchten Sie einen Befehl ausführen und alle potenziellen Fehlermeldungen komplett ignorieren. Dazu können Sie `stderr` in eine spezielle Datei namens `/dev/null` umleiten, die alle Daten, die in sie geschrieben werden, verwirft.

```bash
ls /fake/directory 2> /dev/null
```

Dieser Befehl wird ausgeführt, und jede Fehlerausgabe von `stderr` wird an `/dev/null` gesendet und verworfen, wodurch Ihr Bildschirm sauber bleibt.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Ein-/Ausgabeumleitung zu festigen:

1. **[Umleitung von Eingabe und Ausgabe in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** - In diesem Lab lernen Sie, Eingabe und Ausgabe in der Linux-Shell umzuleiten. Sie üben die Steuerung des Datenflusses von Befehlen, indem Sie Standardausgabe (stdout), Standardfehler (stderr) und Standardeingabe (stdin) mithilfe von Operatoren wie >, >>, 2> und dem tee-Befehl manipulieren.

Dieses Lab hilft Ihnen, die Konzepte der I/O-Umleitung in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Datenströmen in Linux aufzubauen.

## Quiz Question

Welcher Operator wird verwendet, um den `stderr`-Stream umzuleiten? Bitte geben Sie den genauen Operator in Ihrer Antwort an.

## Quiz Answer

2>
