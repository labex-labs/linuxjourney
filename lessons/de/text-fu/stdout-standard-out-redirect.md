---
index: 1
lang: "de"
title: "stdout (Standardausgabe)"
meta_title: "stdout (Standardausgabe) - Text-Fu"
meta_description: "Beginnen Sie Ihre Reise zum Erlernen von Linux, indem Sie die Standardausgabe (stdout) und I/O-Umleitung meistern. Diese Lektion behandelt, wie man die Ausgabe von Befehlen mithilfe der Operatoren > und >> in Dateien umleitet – eine grundlegende Fähigkeit für jeden Linux-Benutzer."
meta_keywords: "Linux, Linux lernen, stdout, I/O-Umleitung, Standardausgabe, Ausgabe umleiten, bash, Shell-Skripting, Linux-Befehle, Linux-Tutorial"
---

## Lesson Content

Während Sie weiterhin Linux lernen, haben Sie gesehen, wie Befehle Ausgaben erzeugen. Dies führt uns zum wichtigen Thema der I/O-Streams (Input/Output), insbesondere der Standardausgabe oder **stdout**. Lassen Sie uns dieses Konzept untersuchen, indem wir den folgenden Befehl ausführen:

```bash
echo Hello World > peanuts.txt
```

Nach der Ausführung finden Sie eine neue Datei namens `peanuts.txt` in Ihrem aktuellen Verzeichnis. Wenn Sie ihren Inhalt anzeigen, sehen Sie den Text "Hello World". Lassen Sie uns analysieren, was passiert ist.

### Standardausgabe (stdout) verstehen

Betrachten Sie zunächst den Befehl ohne das Sonderzeichen:

```bash
echo Hello World
```

Standardmäßig senden viele Befehle ihre Ergebnisse an **stdout**, was Ihr Terminalbildschirm ist. Deshalb zeigt `echo Hello World` den Text direkt in Ihrer Shell an. Prozesse verwenden I/O-Streams, um Eingaben (Standardeingabe oder stdin) zu empfangen und Ausgaben zu senden. Die I/O-Umleitung ermöglicht es uns, dieses Standardverhalten zu ändern und uns mehr Kontrolle über unsere Daten zu geben.

### stdout mit > umleiten

Das Zeichen `>` ist ein Umleitungsoperator. Es fängt die Daten ab, die an **stdout** gehen, und sendet sie an ein neues Ziel.

```bash
>
```

In unserem Beispiel sendet es die Ausgabe von `echo Hello World` an eine Datei anstatt an den Bildschirm. Wenn die Datei nicht existiert, wird sie erstellt. **Seien Sie vorsichtig**, denn wenn die Datei bereits existiert, überschreibt dieser Operator ihren Inhalt vollständig.

### stdout mit >> anhängen

Was ist, wenn Sie einer Datei etwas hinzufügen möchten, ohne ihren Inhalt zu löschen? Dafür verwenden wir den Operator `>>`.

```bash
echo Hello World >> peanuts.txt
```

Dieser Operator hängt die Ausgabe an das Ende der angegebenen Datei an. Wenn die Datei noch nicht existiert, wird sie erstellt, genau wie beim `>`-Operator. Die Beherrschung der **stdout**-Umleitung ist ein grundlegender Schritt auf Ihrem Linux-Weg.

## Exercise

Um Ihr Verständnis der I/O-Umleitung zu festigen, versuchen Sie dieses praktische Labor:

1. **[Eingabe und Ausgabe in Linux umleiten](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie die Standardausgabe (stdout), die Standardfehlerausgabe (stderr) und die Standardeingabe (stdin) mithilfe von Operatoren wie `>`, `>>`, `2>` und dem `tee`-Befehl manipulieren.

Dieses Labor hilft Ihnen, diese Konzepte in realen Szenarien anzuwenden und Selbstvertrauen bei der I/O-Umleitung aufzubauen.

## Quiz Question

Welchen Umleiter verwenden Sie, um Ausgabe an eine Datei anzuhängen?

## Quiz Answer

`>>`
