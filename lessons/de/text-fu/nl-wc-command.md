---
index: 15
lang: "de"
title: "wc und nl"
meta_title: "wc und nl - Text-Fu"
meta_description: "Meistern Sie die Befehle wc und nl in diesem Linux-Tutorial. Erfahren Sie, wie Sie eine Linux-Wortzählung durchführen, Zeilennummern zu Dateien hinzufügen und grundlegende Datei-Analysen durchführen. Ein perfekter Leitfaden für Anfänger zur Verbesserung ihrer Kommandozeilen-Fähigkeiten."
meta_keywords: "wc Befehl, nl Befehl, Linux Wortzählung, Wörter in Datei zählen Linux, Linux Zeilennummern, nl Befehl Linux, Datei-Analyse, Textverarbeitung Linux, Linux Kommandozeile, Linux Tutorial für Anfänger"
---

## Lesson Content

In Linux ist die Analyse von Textdateien eine häufige Aufgabe. Zwei grundlegende Dienstprogramme hierfür sind `wc` und `nl`, die Ihnen helfen, Inhalte zu zählen bzw. Zeilen zu nummerieren.

### Zählen mit dem wc-Befehl

Der Befehl `wc` (word count) ist ein leistungsstarkes Werkzeug für die grundlegende Dateianalyse. Wenn er auf einer Datei ausgeführt wird, liefert er eine Zusammenfassung ihres Inhalts.

```bash
$ wc /etc/passwd
 96     265    5925 /etc/passwd
```

Die Ausgabe zeigt drei Zahlen, gefolgt vom Dateinamen. Von links nach rechts stellen diese Zahlen dar:

1. Die Anzahl der Zeilen.
2. Die Anzahl der Wörter (der Linux-Wortzähler).
3. Die Anzahl der Bytes.

### Spezifische Zählungen erhalten

Oft benötigen Sie nur eine Information. Sie können Optionen verwenden, um anstelle aller drei eine spezifische Zählung anzuzeigen.

- `-l`: Zeigt nur die Zeilenanzahl an.
- `-w`: Zeigt nur die Wortanzahl an.
- `-c`: Zeigt nur die Byteanzahl an.

Um beispielsweise nur die Anzahl der Zeilen in der Datei `/etc/passwd` anzuzeigen, würden Sie Folgendes verwenden:

```bash
$ wc -l /etc/passwd
96
```

### Zeilen mit dem nl-Befehl nummerieren

Ein weiteres nützliches Werkzeug zur Überprüfung von Dateien ist `nl` (number lines). Wie der Name schon sagt, liest es eine Datei und gibt deren Inhalt aus, wobei am Anfang jeder Zeile Zeilennummern hinzugefügt werden. Dies ist besonders hilfreich beim Überprüfen von Skripten oder Konfigurationsdateien.

Betrachten Sie eine Datei namens `file1.txt` mit folgendem Inhalt:

```plaintext
i
like
turtles
```

Mit dem Befehl `nl` können Sie einfach Linux-Zeilennummern hinzufügen:

```bash
$ nl file1.txt
     1 i
     2 like
     3 turtles
```

Sowohl `wc` als auch `nl` sind wesentliche Befehle für die tägliche Textverarbeitung auf der Linux-Kommandozeile.

## Exercise

Um diese Befehle zu beherrschen, ist praktische Übung der Schlüssel. Versuchen Sie diese Übungen, um Ihre Fähigkeiten im Zählen von Text und Nummerieren von Zeilen unter Linux zu festigen:

1. **[Linux wc Befehl: Textzählung](https://labex.io/de/labs/linux-linux-wc-command-text-counting-219200)** - Üben Sie das Zählen von Wörtern, Zeilen und Zeichen in Textdateien mit dem `wc`-Befehl.
2. **[Linux nl Befehl: Zeilennummerierung](https://labex.io/de/labs/linux-linux-nl-command-line-numbering-210988)** - Lernen Sie, Zeilen in Textdateien mit dem `nl`-Befehl zu nummerieren.
3. **[Wortzählung und Sortierung](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** - Wenden Sie Ihr Wissen über `wc` an, um Zeilen, Wörter und Zeichen zu zählen, und kombinieren Sie es mit dem Sortieren für praktische Textanalysen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Textverarbeitung unter Linux aufzubauen.

## Quiz Question

Welchen Befehl und welche Option würden Sie verwenden, um nur die gesamte Wortanzahl einer Datei anzuzeigen? Bitte antworten Sie nur mit dem Befehl und seiner Option auf Englisch. Die Antwort ist groß- und kleingeschrieben.

## Quiz Answer

wc -w
