---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "de"
order_index: 16
title: "grep"
description: "Lerne, Zeilen mit festen Zeichenfolgen oder regulären Ausdrücken auszuwählen und grep-Ergebnisse zu deuten."
meta_title: "grep - Text-Fu"
meta_description: "Lernen Sie, den mächtigen grep-Befehl in Linux zu verwenden, um nach Textmustern zu suchen. Diese Anleitung behandelt die grundlegende Verwendung, den grep -e Befehl, grep -c zum Zählen und andere wesentliche Optionen für die effektive Textverarbeitung."
meta_keywords: "grep Befehl, grep -e Befehl, grep -c, grep -f, grep -o, grep -e Beispiel, linux grep, Text suchen, Mustererkennung, Textverarbeitung, linux Tutorial"
---

Der Befehl `grep` wählt Eingabezeilen aus, die zu einem Muster passen. Er kann benannte Dateien oder stdin durchsuchen, Kontext zu Treffern ausgeben, ausgewählte Zeilen zählen und über seinen Beendigungsstatus mitteilen, ob ein Treffer gefunden wurde.

## Passende Zeilen in einer Datei finden

Übergib ein Muster, gefolgt von einer oder mehreren Eingabedateien:

```bash
$ grep 'fox' sample.txt
```

GNU `grep` interpretiert das Muster standardmäßig als einfachen regulären Ausdruck und gibt jede ausgewählte Zeile aus. Setze Muster in Anführungszeichen, damit Leerzeichen und Shell-Metazeichen nicht zuerst von der Shell interpretiert werden.

Verwende `-F`, wenn das Muster als feste Zeichenfolge statt als regulärer Ausdruck behandelt werden soll:

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string}
Welcher Befehl durchsucht `products.txt` nach dem wörtlichen Text `price: $5.00`, ohne Musterzeichen als Syntax eines regulären Ausdrucks zu behandeln?

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F` wählt die Suche nach festen Zeichenfolgen; einfache Anführungszeichen schützen das Dollarzeichen vor der Shell-Erweiterung."}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E` aktiviert erweiterte reguläre Ausdrücke, in denen `$` und `.` eine besondere statt einer wörtlichen Bedeutung besitzen."}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v` wählt nicht passende Zeilen aus und verwendet standardmäßig weiterhin die Interpretation als regulären Ausdruck."}
:::

## Die Mustersyntax auswählen

GNU `grep` bietet drei häufig verwendete Mustermodi:

- Standard: einfache reguläre Ausdrücke.
- `-E`: erweiterte reguläre Ausdrücke mit Operatoren wie `|`, `+` und `?` ohne Backslashes.
- `-F`: feste Zeichenfolgen ohne Operatoren regulärer Ausdrücke.

Anker wie `^` und `$` passen auf Anfang und Ende einer Zeile. So findest du in einer Textliste Dateinamen, die mit der wörtlichen Endung `.txt` enden:

```bash
$ grep -E '\.txt$' filenames.txt
```

Der Backslash macht den Punkt wörtlich; ein ungeschütztes `.` steht in einem regulären Ausdruck für ein beliebiges einzelnes Zeichen.

:::single-choice{#grep-literal-txt-suffix}
Welcher erweiterte reguläre Ausdruck passt auf Zeilen, die mit der wörtlichen Endung `.txt` enden?

::option[`'.txt$'`]{#grep-anychar-txt explanation="Der Punkt ist nicht geschützt und steht daher für ein beliebiges Zeichen vor `txt`, nicht speziell für einen wörtlichen Punkt."}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.` passt auf einen wörtlichen Punkt; `$` verankert den Treffer am Zeilenende."}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="Dieser Ausdruck ist am Zeilenanfang verankert und verwendet weiterhin einen ungeschützten Punkt. Er beschreibt einen anderen Treffer."}
:::

## Muster sicher angeben

Mit `-e PATTERN` gibst du ein Muster ausdrücklich an. Das ist besonders hilfreich, wenn es mit `-` beginnt, denn Anführungszeichen verhindern nicht die Optionsauswertung:

```bash
$ grep -e '-v' settings.conf
```

Du kannst `-e` mehrfach verwenden, um Zeilen auszuwählen, die zu einem der angegebenen Muster passen. Mit `-f patterns.txt` liest du ein Muster pro Zeile aus einer Datei.

:::single-choice{#grep-hyphen-pattern}
Welcher Befehl durchsucht `settings.conf` nach dem Muster `-v`, statt es als Option zu interpretieren?

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="Anführungszeichen schützen vor Shell-Erweiterungen, doch `grep` kann das entstandene Argument `-v` weiterhin als Option zur Umkehrung der Auswahl interpretieren."}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="Dieser Befehl aktiviert die umgekehrte Auswahl und stellt `settings.conf` nicht auf die verlangte Weise zugleich als Muster und Eingabe bereit."}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="Die Option `-e` erklärt das nachfolgende Argument ausdrücklich zum Muster, obwohl es mit einem Bindestrich beginnt."}
:::

## Die ausgewählte Ausgabe steuern

- `-i`: Ignoriert Unterschiede zwischen Groß- und Kleinschreibung.
- `-n`: Stellt ausgewählten Zeilen ihre Zeilennummer voran.
- `-v`: Wählt Zeilen aus, die nicht passen.
- `-c`: Gibt für jede Eingabedatei die Anzahl ausgewählter Zeilen aus.
- `-o`: Gibt statt der vollständigen ausgewählten Zeile nur jeden nicht leeren passenden Teil aus.

So zählst du Zeilen mit `fox` unabhängig von Groß- und Kleinschreibung:

```bash
$ grep -ic 'fox' sample.txt
```

`-c` zählt ausgewählte Zeilen, nicht sämtliche Treffer innerhalb dieser Zeilen. Eine Zeile mit `fox fox` trägt eins zur Anzahl bei. Benötigst du mit GNU `grep` ausdrücklich nicht überlappende einzelne Treffer, ist `grep -o PATTERN | wc -l` eine mögliche Pipeline.

:::single-choice{#grep-count-lines}
`data.txt` enthält eine Zeile mit `error error` und zwei Zeilen ohne Treffer. Was meldet `grep -c 'error' data.txt`?

::option[`2`, weil das Wort zweimal in einer Zeile vorkommt.]{#grep-count-occurrences explanation="`-c` zählt ausgewählte Zeilen und nicht einzelne Treffer innerhalb einer Zeile."}
::option[`1`, weil genau eine Zeile passt.]{#grep-count-one-line .correct explanation="Die eine Zeile wird einmal ausgewählt, obwohl das Muster darin zweimal vorkommt."}
::option[`3`, weil die Datei insgesamt drei Zeilen enthält.]{#grep-count-total-lines explanation="Nur ausgewählte Zeilen tragen zu `grep -c` bei; nicht passende Zeilen werden nicht gezählt."}
:::

## stdin filtern und Verzeichnisse durchsuchen

Ohne benannte Eingabedatei liest `grep` von stdin und eignet sich natürlich für Pipelines:

```bash
$ env | grep '^USER='
```

Mit `-r` durchsuchst du lesbare Dateien unterhalb eines Verzeichnisses rekursiv:

```bash
$ grep -r 'listen_port' config/
```

Diagnosen wie Berechtigungsfehler fließen nach stderr und sind keine durchsuchte Eingabe. Grenze den Suchpfad ein und verstehe Berechtigungen, bevor du den Zugriff erhöhst.

:::single-choice{#grep-pipeline-input}
Welche Eingabe durchsucht `grep` in `generate-report | grep 'failed'`?

::option[Eine Datei namens `generate-report` im aktuellen Verzeichnis.]{#grep-report-file explanation="Das Wort links wird als Befehl ausgeführt und nicht als Dateioperand an `grep` übergeben."}
::option[Den von `generate-report` erzeugten stdout-Strom.]{#grep-report-stdout .correct explanation="Die Pipe verbindet stdout des Erzeugers mit stdin von `grep`."}
::option[Den von `generate-report` erzeugten stderr-Strom.]{#grep-report-stderr explanation="Eine gewöhnliche Pipe überträgt stdout. Stderr bleibt getrennt, sofern es nicht ausdrücklich umgeleitet wird."}
:::

## Den Beendigungsstatus deuten

Bei gewöhnlichen Suchen gibt GNU `grep` Status `0` zurück, wenn mindestens eine Zeile ausgewählt wurde, `1`, wenn keine Zeile ausgewählt wurde, und `2` bei einem Fehler. Skripte können dadurch „kein Treffer“ von einer unlesbaren Datei oder einem ungültigen Muster unterscheiden.

Optionen wie `-q` unterdrücken die normale Ausgabe und beenden die Suche nach dem ersten Treffer, was für Bedingungsprüfungen nützlich ist. Schließe nicht allein aus einer leeren Anzeige auf Erfolg: `-q`, eine Umleitung, kein Treffer und ein Fehler können wenig oder kein stdout erzeugen, besitzen aber unterschiedliche Statuswerte.

Mit diesen Übungen kannst du feste Zeichenfolgen und reguläre Ausdrücke praktisch durchsuchen:

1. **[Text mit grep in Linux suchen](https://labex.io/de/labs/comptia-search-text-with-grep-in-linux-590841)** – Übe grundlegende Suchen, Zeilennummern, Anker sowie einfache und erweiterte reguläre Ausdrücke mit `grep`.
2. **[Linux grep Befehl: Mustersuche](https://labex.io/de/labs/linux-linux-grep-command-pattern-searching-219192)** – Nutze `grep`, um in Textdateien nach Mustern zu suchen, und definiere komplexere Suchmuster mit regulären Ausdrücken.
3. **[Nadel im Heuhaufen](https://labex.io/de/labs/linux-needle-in-the-haystack-388109)** – Nutze `grep`, um in Protokolldateien nach Mustern zu suchen, Vorkommen zu zählen, eindeutige Werte zu extrahieren und Suchkriterien zu kombinieren.

## Zusammenfassung

Du kannst nun zeilenorientierten Text durchsuchen und Treffer von Fehlern unterscheiden.

1. Wähle einfache, erweiterte oder feste Zeichenfolgensuche.
2. Schütze Muster durch Anführungszeichen und verwende `-e` bei einem führenden Bindestrich.
3. Zähle ausgewählte Zeilen, ohne sie mit einzelnen Vorkommen zu verwechseln.
4. Filtere stdin oder durchsuche ein begrenztes Verzeichnis rekursiv.
5. Deute Beendigungsstatus für Treffer, keinen Treffer und Fehler.
