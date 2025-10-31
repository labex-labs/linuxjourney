---
index: 4
lang: "de"
title: "Pipe und Tee"
meta_title: "Pipe und Tee - Text-Fu"
meta_description: "Entdecken Sie den leistungsstarken Pipe- und Tee-Befehl in Linux. Erfahren Sie, wie Sie Befehle mit der Linux Pipe-Tee-Kombination verketten und die Ausgabe sowohl auf dem Bildschirm als auch in einer Datei umleiten. Diese Anleitung behandelt das Piping zu tee für einen erweiterten Kommandozeilen-Datenfluss."
meta_keywords: "pipe und tee befehl in linux, linux pipe tee, pipe zu tee, linux pipe, tee befehl, stdout, stdin, kommandozeilenumleitung, linux tutorial"
---

## Lesson Content

Unter Linux wird die Kommandozeile unglaublich leistungsstark, wenn Sie anfangen, Befehle zu verknüpfen. Anstatt einen Befehl auszuführen, seine Ausgabe zu speichern und dann einen anderen auszuführen, können Sie eine Pipeline erstellen, um Daten direkt zwischen ihnen zu übergeben.

### Den Pipe-Operator verstehen

Beginnen wir mit einem Befehl, der eine große Ausgabe erzeugt:

```bash
ls -la /etc
```

Die Liste der Elemente ist wahrscheinlich zu lang, um auf Ihren Bildschirm zu passen, was das Lesen erschwert. Sie könnten diese Ausgabe zwar in eine Datei umleiten, aber eine effizientere Methode besteht darin, sie direkt an einen anderen Befehl, wie `less`, zur einfachen Anzeige zu senden.

```bash
ls -la /etc | less
```

Der Pipe-Operator `|`, dargestellt durch einen senkrechten Strich, ist der Schlüssel zu diesem Prozess. Er nimmt die Standardausgabe (`stdout`) des Befehls links davon und verwendet sie als Standardeingabe (`stdin`) für den Befehl rechts davon. In diesem Fall haben wir die Ausgabe von `ls -la /etc` direkt in den `less`-Befehl _gepipet_. Die Pipe ist ein grundlegendes Werkzeug, das Sie ständig verwenden werden.

### Ausgabe mit dem Tee-Befehl aufteilen

Was ist, wenn Sie die Ausgabe gleichzeitig auf Ihrem Bildschirm sehen _und_ in einer Datei speichern möchten? Hier kommt der `tee`-Befehl ins Spiel. Der `pipe and tee command in linux` ist eine klassische Kombination zum Protokollieren und Überwachen.

```bash
ls | tee peanuts.txt
```

Nach der Ausführung sehen Sie die Ausgabe von `ls` auf Ihrem Terminal. Wenn Sie auch den Inhalt von `peanuts.txt` überprüfen, werden Sie exakt dieselben Informationen finden. Der `tee`-Befehl teilt den Ausgabestrom effektiv in zwei Richtungen auf: eine zur Standardausgabe und eine zu einer angegebenen Datei.

### Pipe und Tee kombinieren

Sie können noch fortschrittlichere Workflows erstellen, indem Sie diese Befehle verketten. Ein gängiges Muster ist, `pipe to tee` mitten in einer längeren Befehlskette zu verwenden. Dies ermöglicht es Ihnen, ein Zwischenergebnis zu speichern, während die Daten weiterverarbeitet werden.

Zum Beispiel können Sie die Kombination `linux pipe tee` verwenden, um die Ausgabe vor weiterer Filterung anzuzeigen und zu speichern:

```bash
ls -la /etc | tee etc_listing.txt | grep "conf"
```

Dieser Befehl bewirkt drei Dinge:

1. Er listet den Inhalt des Verzeichnisses `/etc` auf.
2. Er leitet diese Ausgabe an `tee` weiter, das eine Kopie in `etc_listing.txt` speichert und sie gleichzeitig weitergibt.
3. Die Ausgabe von `tee` wird dann an `grep` weitergeleitet, das nach Zeilen filtert, die "conf" enthalten.

Die Beherrschung dieser Befehle wird Ihre Effizienz auf der Kommandozeile erheblich steigern.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Ein-/Ausgabeumleitung und von Pipelines zu festigen:

1. **[Redirecting Input and Output in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie Standardausgabe (stdout), Standardfehlerausgabe (stderr) und Standardeingabe (stdin) mithilfe von Operatoren wie `>`, `>>`, `2>` und dem `tee`-Befehl manipulieren.
2. **[Sequence Control and Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** - Lernen Sie, Befehlsausführungssequenzen zu steuern, Pipelines zu nutzen und leistungsstarke Textverarbeitungswerkzeuge wie `cut`, `grep`, `wc`, `sort` und `uniq` einzusetzen.
3. **[Data Stream Redirection](https://labex.io/de/labs/linux-data-stream-redirection-17995)** - Lernen Sie die Kunst der Linux-Stream-Umleitung kennen, einschließlich der Manipulation von Standardeingabe, -ausgabe und -fehlerströmen, dem Kombinieren von Ausgaben und der Verwendung von `/dev/null`.

Diese Labs helfen Ihnen, die Konzepte von Piping und Umleitung in realen Szenarien anzuwenden und Selbstvertrauen bei der Datenmanipulation in der Kommandozeile aufzubauen.

## Quiz Question

Welches einzelne Zeichen repräsentiert den Pipe-Operator in einem Linux-Befehl? Bitte antworten Sie nur mit dem Symbol.

## Quiz Answer

|
