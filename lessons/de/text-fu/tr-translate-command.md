---
index: 13
lang: "de"
title: "tr (Übersetzen)"
meta_title: "tr (Übersetzen) - Text-Fu"
meta_description: "Meistern Sie den Linux-tr-Befehl zur Zeichenübersetzung und -löschung. Diese Anleitung behandelt, wie man Zeichen mit tr übersetzt, Optionen wie linux tr -d zum Entfernen von Zeichen verwendet und bietet praktische Beispiele für die Textmanipulation."
meta_keywords: "tr, tr Befehl, trübersetzen, linux tr -d, tr -d linux, Zeichen übersetzen, Zeichen löschen, Textverarbeitung, Linux Befehl"
---

## Lesson Content

Der `tr`-Befehl, kurz für translate (übersetzen), ist ein Befehlszeilenprogramm unter Linux, das Zeichen aus der Standardeingabe übersetzt oder löscht. Es ist ein nützliches Werkzeug für einfache Textmanipulationen und wird oft mit Pipes verwendet, um die Ausgabe anderer Befehle zu verarbeiten. Die `trtranslate`-Funktionalität ist ein Kernbestandteil der Textverarbeitung.

### Grundlegende Zeichenübersetzung

Die häufigste Verwendung von `tr` ist der Austausch einer Zeichensatzgruppe gegen eine andere. Sie können beispielsweise ganz einfach alle Kleinbuchstaben in Großbuchstaben umwandeln.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

In diesem Beispiel haben wir die Ausgabe von `echo` an den `tr`-Befehl weitergeleitet (gepipet). Der `tr`-Befehl übersetzte dann den Zeichenbereich `a-z` in die entsprechenden Zeichen im Bereich `A-Z`.

### Zeichen mit -d löschen

Eine weitere leistungsstarke Funktion ist die Möglichkeit, bestimmte Zeichen mithilfe der Option `-d` (delete/löschen) zu entfernen. Dies ist besonders nützlich, um Text zu bereinigen. Wenn Sie beispielsweise alle Ziffern aus einer Zeichenkette entfernen möchten, können Sie `linux tr -d` verwenden.

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Hier löschte der `tr -d`-Befehl jedes Zeichen im angegebenen Satz ('0' bis '9') aus dem Eingabestrom. Dies ist ein gängiges Muster für Benutzer von `tr -d linux`.

### Wiederholte Zeichen quetschen (Squeezing)

Der `tr`-Befehl kann auch wiederholte Zeichen mithilfe der Option `-s` (squeeze/quetschen) zu einer einzigen Instanz zusammenfassen. Dies ist ideal, um Text mit übermäßig vielen Leerzeichen zu normalisieren.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

In diesem Fall ersetzte `tr -s ' '` Sequenzen von mehreren Leerzeichen durch ein einzelnes Leerzeichen, was die Ausgabe wesentlich sauberer machte.

## Exercise

Um Ihr Wissen in die Praxis umzusetzen, versuchen Sie das folgende praktische Labor. Es wird Ihnen helfen, Ihr Verständnis der Zeichenübersetzung und Textverarbeitung zu festigen.

1. **[Linux tr Befehl: Zeichenübersetzung](https://labex.io/de/labs/linux-linux-tr-command-character-translating-219198)** - Lernen Sie den Linux `tr`-Befehl für zeichenweise Transformationen in Textströmen kennen. Sie üben das Übersetzen von Zeichen, das Löschen bestimmter Zeichen, die Arbeit mit Zeichenklassen und das Quetschen wiederholter Zeichen.

Dieses Labor hilft Ihnen, die Konzepte der Textmanipulation in realen Szenarien anzuwenden und Vertrauen in den `tr`-Befehl aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um Zeichen zu übersetzen? (Bitte antworten Sie nur in englischen Kleinbuchstaben)

## Quiz Answer

tr
