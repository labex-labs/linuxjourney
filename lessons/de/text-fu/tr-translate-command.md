---
index: 13
lang: "de"
title: "tr (Übersetzen)"
meta_title: "tr (Übersetzen) - Text-Fu"
meta_description: "Lerne den Linux-Befehl tr mit Beispielen zum Übersetzen von Zeichen, Löschen von Zeichen, Zusammenziehen von Wiederholungen, Verwendung von Zeichenklassen und Bereinigung von Text."
meta_keywords: "linux tr befehl, tr befehl, tr -d, tr -s, zeichen übersetzen, zeichen löschen, zeichenklassen, textverarbeitung linux"
---

## Lesson Content

Der Befehl `tr`, kurz für translate (übersetzen), ist ein Kommandozeilenwerkzeug, das Zeichen aus der Standardeingabe übersetzt, löscht oder zusammenzieht. Er ist nützlich für einfache Textmanipulationen und wird oft mit Pipes verwendet, um die Ausgabe anderer Befehle zu verarbeiten.

Die Grundsyntax lautet:

```bash
tr [OPTIONS] SET1 [SET2]
```

Im Gegensatz zu Werkzeugen wie `sed` oder `awk` arbeitet `tr` zeichenweise. Es versteht Wörter, Spalten oder reguläre Ausdrücke nicht auf dieselbe Weise. Das macht es schnell und einfach für Aufgaben wie Groß-/Kleinschreibung ändern, Ziffern entfernen und wiederholte Leerzeichen normalisieren.

### Grundlegende Zeichenübersetzung

Die häufigste Verwendung von `tr` ist das Ersetzen eines Zeichensatzes durch einen anderen. Zum Beispiel kann man alle Kleinbuchstaben einfach in Großbuchstaben übersetzen.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

In diesem Beispiel haben wir die Ausgabe von `echo` an den Befehl `tr` weitergeleitet. Der `tr`-Befehl hat dann den Zeichensatzbereich `a-z` in die entsprechenden Zeichen im Bereich `A-Z` übersetzt.

Man kann auch einzelne Zeichen in andere übersetzen:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

Jedes Zeichen in `SET1` wird auf das Zeichen an der gleichen Position in `SET2` abgebildet.

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Hier wird `a` zu `A`, `b` zu `B` und `c` zu `C`.

### Löschen von Zeichen mit -d

Eine weitere mächtige Funktion ist die Möglichkeit, bestimmte Zeichen mit der Option `-d` zu löschen. Das ist besonders nützlich, um Text zu bereinigen. Wenn man zum Beispiel alle Ziffern aus einem String entfernen möchte, kann man Folgendes verwenden:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Hier hat `tr -d` jedes Zeichen aus dem angegebenen Satz von `0` bis `9` gelöscht.

Man kann Satzzeichen aus einem String entfernen, indem man eine Zeichenklasse verwendet:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Man kann auch Zeilenumbrüche entfernen, um Zeilen zusammenzufügen:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

### Zusammenziehen von wiederholten Zeichen

Der Befehl `tr` kann auch wiederholte Zeichen mit der Option `-s` „zusammenziehen“. Das ist ideal, um Text mit überflüssigen Leerzeichen zu normalisieren.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

In diesem Fall hat `tr -s ' '` Folgen von mehreren Leerzeichen durch ein einzelnes Leerzeichen ersetzt, was die Ausgabe viel sauberer macht.

Man kann auch wiederholte Zeilenumbrüche zusammenziehen:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

### Verwendung von Zeichenklassen

Zeichenklassen machen `tr`-Befehle leichter lesbar und portabler. Häufige Klassen sind:

- `[:lower:]`: Kleinbuchstaben.
- `[:upper:]`: Großbuchstaben.
- `[:digit:]`: Ziffern.
- `[:alpha:]`: Buchstaben.
- `[:alnum:]`: Buchstaben und Ziffern.
- `[:space:]`: Leerraumzeichen.
- `[:punct:]`: Satzzeichen.

Zum Beispiel kann man mit Zeichenklassen Kleinbuchstaben in Großbuchstaben umwandeln:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

Lösche alles außer Buchstaben und Ziffern, indem du `-c` mit `-d` verwendest. Die Option `-c` bedeutet Komplement, also „alles, was nicht in diesem Satz ist“.

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

### Kombination von Löschen und Zusammenziehen

Man kann Optionen kombinieren, wenn man Text bereinigt. Dieses Beispiel löscht Satzzeichen und zieht dann wiederholte Leerzeichen zusammen:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Für tabulatorgetrennte Eingaben kann man Tabs in Kommas übersetzen:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

### Häufige tr-Optionen

Hier sind die Optionen, die du am häufigsten verwenden wirst:

- `-d`: Löscht Zeichen in `SET1`.
- `-s`: Zieht wiederholte Zeichen in `SET1` zusammen.
- `-c`: Verwendet das Komplement von `SET1`.
- `-t`: Kürzt `SET1` auf die Länge von `SET2` vor der Übersetzung.

### Häufige Fragen

**Warum liest tr von einer Pipe?** `tr` liest von der Standardeingabe, daher wird es häufig nach Befehlen wie `echo`, `cat`, `printf` oder anderen textproduzierenden Befehlen verwendet.

**Ersetzt tr Wörter?** Nein. `tr` übersetzt Zeichen, keine Wörter. Verwende `sed`, wenn du ganze Wörter oder Muster ersetzen möchtest.

**Warum hat mein tr-Befehl Zeichen einzeln geändert?** So funktioniert `tr`. Es ordnet jedes Zeichen in `SET1` dem entsprechenden Zeichen in `SET2` zu.

**Warum sollte ich Zeichensätze wie 'a-z' in Anführungszeichen setzen?** Das Setzen in Anführungszeichen verhindert, dass die Shell Sonderzeichen interpretiert, bevor `tr` sie erhält.

## Exercise

Um dein Wissen praktisch anzuwenden, probiere das folgende praktische Lab aus. Es hilft dir, dein Verständnis von Zeichenübersetzung und Textverarbeitung zu vertiefen.

1. **[Linux tr Command: Character Translating](https://labex.io/de/labs/linux-linux-tr-command-character-translating-219198)** – Lerne den Linux-Befehl `tr` für zeichenweise Transformationen in Textströmen. Du wirst das Übersetzen von Zeichen, Löschen bestimmter Zeichen, Arbeiten mit Zeichenklassen und Zusammenziehen wiederholter Zeichen üben.

Dieses Lab hilft dir, die Konzepte der Textmanipulation in realen Szenarien anzuwenden und Vertrauen im Umgang mit dem `tr`-Befehl zu gewinnen.

## Quiz Question

Welcher Befehl wird verwendet, um Zeichen zu übersetzen? (Bitte nur Kleinbuchstaben auf Englisch antworten)

## Quiz Answer

tr
