---
index: 10
lang: "de"
title: "Erweitern und Zurücksetzen"
meta_title: "Erweitern und Zurücksetzen - Text-Fu"
meta_description: "Beherrschen Sie die Textformatierung unter Linux mit unserem Leitfaden zu den Befehlen expand und unexpand. Erfahren Sie, wie Sie Tabs in Leerzeichen und Leerzeichen wieder in Tabs umwandeln, um konsistente Dateilayouts zu erhalten."
meta_keywords: "expand Befehl, unexpand Befehl, Linux Tabs, Linux Leerzeichen, Textformatierung, Linux Tutorial, Anfänger Linux, Linux Anleitung"
---

## Lesson Content

Inkonsistente Leerzeichen können Textdateien schwer lesbar machen. Obwohl Tabs dazu dienen, eine einheitliche Einrückung zu erzeugen, kann ihre Anzeigebreite auf verschiedenen Editoren und Systemen variieren. Dies kann die Textformatierung und Ausrichtung stören. Glücklicherweise bietet Linux einfache Werkzeuge, um dies zu verwalten, indem zwischen Tabs und Leerzeichen konvertiert wird. Diese Linux-Anleitung für Anfänger führt Sie durch den Prozess.

### Tabs in Leerzeichen mit dem expand-Befehl umwandeln

Wenn Sie eine konsistente Leerzeichensetzung sicherstellen müssen, können Sie Tabs mithilfe des Befehls `expand` in eine Standardanzahl von Leerzeichen umwandeln. Dieser Befehl liest eine Datei und ersetzt jedes Tabulatorzeichen durch eine Reihe von Leerzeichen und gibt das Ergebnis auf der Standardausgabe aus.

```bash
expand sample.txt
```

Standardmäßig wandelt der `expand command` jeden Tab in 8 Leerzeichen um. Dieses einfache Dienstprogramm ist ein mächtiges Werkzeug zur Verbesserung der Textformatierung.

### Die umgewandelte Ausgabe speichern

Der Befehl `expand` gibt den umgewandelten Text nur auf Ihrem Terminal aus. Um die Änderungen zu speichern, müssen Sie die Ausgabe in eine neue Datei umleiten.

```bash
expand sample.txt > result.txt
```

Dieser Befehl nimmt die Ausgabe von `expand sample.txt` und schreibt sie in `result.txt`, wodurch Sie eine neue Datei mit Leerzeichen anstelle von Tabs erhalten.

### Leerzeichen mit dem unexpand-Befehl in Tabs umwandeln

Die umgekehrte Operation, das Zurückwandeln von Leerzeichen in Tabs, wird vom Befehl `unexpand` übernommen. Dies kann nützlich sein, um die Dateigröße zu reduzieren oder Codierungsstandards einzuhalten, die Tabs erfordern.

```bash
unexpand -a result.txt
```

Standardmäßig wandelt `unexpand` nur führende Leerzeichen in jeder Zeile um. Die Option `-a` weist den `unexpand command` an, alle Vorkommen von 8 Leerzeichen in einen Tab umzuwandeln, nicht nur diejenigen am Anfang einer Zeile, was eine umfassendere Kontrolle über Ihre Linux-Leerzeichen und Tabs ermöglicht.

## Exercise

Um die Textmanipulation und Umleitung in Linux zu meistern, ist Übung der Schlüssel. Die folgenden praktischen Übungen helfen, Ihr Verständnis zu festigen:

1. **[Eingabe- und Ausgabeumleitung in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Üben Sie die Steuerung des Datenflusses von Befehlen, indem Sie Standardausgabe (stdout), Standardfehler (stderr) und Standardeingabe (stdin) mithilfe von Operatoren wie `>` und `>>` manipulieren.
2. **[Einfache Textverarbeitung](https://labex.io/de/labs/linux-simple-text-processing-18004)** - Lernen Sie, leistungsstarke Befehle wie `tr`, `col`, `join` und `paste` zu verwenden, um Textdaten effizient zu manipulieren und zu analysieren, wodurch Ihre Kommandozeilenfähigkeiten für die Datenverarbeitung verbessert werden.
3. **[Textverarbeitung und reguläre Ausdrücke](https://labex.io/de/labs/linux-text-processing-and-regular-expressions-18003)** - Lernen Sie die leistungsstarken Textverarbeitungswerkzeuge `grep`, `sed` und `awk` kennen und verwenden Sie reguläre Ausdrücke für effiziente Textmanipulation und Mustererkennung in Linux.

Das Abschließen dieser Übungen hilft Ihnen, die Konzepte der Texttransformation und Dateimanipulation in realen Szenarien anzuwenden und Ihr Vertrauen in wesentliche Linux-Kommandozeilenwerkzeuge aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um Tabs in Leerzeichen umzuwandeln? (Bitte antworten Sie mit dem englischen Befehlsnamen in Kleinbuchstaben.)

## Quiz Answer

expand
