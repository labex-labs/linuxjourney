---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "de"
order_index: 6
title: "cut"
description: "Lerne, mit cut Zeichenpositionen oder getrennte Felder aus jeder Zeile auszuwählen."
meta_title: "cut - Text-Tools"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl `cut` verwenden, um bestimmte Textabschnitte aus Dateien zu extrahieren. Diese Anleitung behandelt das Schneiden nach Zeichen und Feld (`cut f`), einschließlich der Verwendung von `cut f` mit benutzerdefinierten Trennzeichen. Perfekt für die Beherrschung der Linux-Textverarbeitung."
meta_keywords: "cut Befehl, Linux Textverarbeitung, Text extrahieren, cut f, cut f verwenden, Linux Tutorial, cut Beispiele, Linux Anleitung, Feldtrennung"
---

Der Befehl `cut` wählt bestimmte Zeichenpositionen oder Felder aus jeder Eingabezeile aus. Er eignet sich am besten für einheitlich strukturierte Texte, deren Trennzeichen und Feldpositionen bekannt sind.

Erstelle für die Beispiele eine kleine tabulatorgetrennte Datei. `printf` interpretiert `\t` als Tabulator und `\n` als Zeilenumbruch:

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

## Zeichenpositionen auswählen

Mit `-c LIST` wählst du Positionen aus jeder Zeile aus. Die Zählung beginnt bei 1:

```bash
$ cut -c 1 team.tsv
n
a
b
```

Die Liste kann einzelne Positionen und Bereiche enthalten:

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

Leerzeichen, Tabulatoren und Satzzeichen belegen ebenfalls Positionen. `cut` verarbeitet jede Zeile unabhängig.

:::single-choice{#cut-first-character} Welcher Befehl gibt das erste Zeichen jeder Zeile von `names.txt` aus?

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="Die Option `-c` wählt Zeichenpositionen aus; Position 1 ist das erste Zeichen jeder Zeile."}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="Die Option `-f` wählt das erste tabulatorgetrennte Feld aus, das mehr als ein Zeichen enthalten kann."}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="Die Option `-d` legt ein Feldtrennzeichen fest und muss mit einer Feldauswahl kombiniert werden. Eine Zeichenposition wählt sie nicht aus."}
:::

## Tabulatorgetrennte Felder auswählen

Mit `-f LIST` wählst du Felder aus. Das standardmäßige Trennzeichen ist ein Tabulator:

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

Wie bei der Zeichenauswahl kann eine Liste Werte wie `1`, `1,3`, `2-4`, `-3` oder `2-` enthalten.

:::single-choice{#cut-second-tab-field} Welcher Befehl gibt das zweite tabulatorgetrennte Feld jeder Zeile von `team.tsv` aus?

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="Damit wird aus jeder Zeile die zweite Zeichenposition ausgewählt, nicht das zweite tabulatorgetrennte Feld."}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="Ohne `-d` verwendet der Feldmodus einen Tabulator als Trennzeichen; `-f 2` wählt das zweite Feld."}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="Dieser Befehl versucht, `2` als Trennzeichen zu verwenden, enthält aber keine Feldliste. Feld 2 wird nicht ausgewählt."}
:::

## Ein eigenes Trennzeichen wählen

Verwende `-d CHARACTER` zusammen mit `-f`, wenn die Felder nicht durch Tabulatoren getrennt sind. Dieses Beispiel erzeugt semikolongetrennte Daten:

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

Das Trennzeichen dieser Form besteht aus einem Zeichen. Setze `;` in Anführungszeichen, weil ein ungeschütztes Semikolon in der Shell eine Steuerbedeutung besitzt.

:::single-choice{#cut-semicolon-role-field} Welcher Befehl gibt das zweite semikolongetrennte Feld von `team.txt` aus?

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="Dieser Befehl wählt durch Doppelpunkte getrennte Felder aus; die Datei verwendet jedoch Semikolons."}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="Das geschützte Semikolon legt das Trennzeichen fest; `-f 2` wählt das zweite Feld jeder Zeile aus."}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="Hier wird die Zeichenauswahl mit einem ungültigen Feldargument vermischt. Das Trennzeichen gehört hinter `-d`, die Feldnummer hinter `-f`."}
:::

## Zeilen ohne Trennzeichen behandeln

Im Feldmodus gibt `cut` eine Zeile normalerweise unverändert aus, wenn sie kein Trennzeichen enthält. Mit `-s` unterdrückst du solche Zeilen:

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

Damit wird keine allgemeine CSV-Datei ausgewertet. CSV kann geschützte Trennzeichen, eingebettete Zeilenumbrüche und Maskierungsregeln enthalten, die eine Aufteilung an einem einzelnen Zeichen nicht versteht. Verwende für solche Daten ein CSV-fähiges Werkzeug.

:::single-choice{#cut-suppress-undelimited} Was bewirkt `-s` bei `cut -d ':' -f 1`?

::option[Die ausgewählten Felder werden vor der Ausgabe sortiert.]{#cut-s-sort explanation="`cut` sortiert seine Eingabe nicht; `-s` hat nichts mit der Reihenfolge zu tun."}
::option[Aufeinanderfolgende Trennzeichen werden als ein Trennzeichen behandelt.]{#cut-s-squeeze explanation="`cut` verwendet `-s` nicht zum Zusammenfassen von Trennzeichen. Leere Felder bleiben eigenständige Positionen."}
::option[Zeilen ohne das gewählte Trennzeichen werden unterdrückt.]{#cut-s-suppress .correct explanation="Im Feldmodus verhindert `-s`, dass Zeilen ohne Trennzeichen unverändert durchgereicht werden."}
:::

## Von stdin lesen

Ohne benannte Datei oder mit `-` als Eingabeoperand liest `cut` von stdin. Dadurch eignet es sich gut als Pipeline-Stufe:

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input} Woher liest `cut` in `generate-data | cut -d ':' -f 1` seine Eingabe?

::option[Über die Pipe aus stdout von `generate-data`.]{#cut-pipe-stdin .correct explanation="Die Pipe verbindet stdout des Erzeugers mit stdin von `cut`; eine separate Eingabedatei ist nicht benannt."}
::option[Aus einer Datei mit dem wörtlichen Namen `generate-data`.]{#cut-pipe-file explanation="`generate-data` wird als linker Pipeline-Befehl ausgeführt und nicht als Dateiname an `cut` übergeben."}
::option[Aus der Standardfehlerausgabe von `cut`.]{#cut-pipe-stderr explanation="Eine normale Pipe speist die Standardeingabe aus stdout des vorherigen Befehls, nicht aus stderr von `cut`."}
:::

Mit diesen Übungen kannst du die Positions- und Feldauswahl praktisch trainieren:

1. **[Linux cut Befehl: Textausschnitt](https://labex.io/de/labs/linux-linux-cut-command-text-cutting-219187)** – Extrahiere mit `cut` bestimmte Spalten oder Felder aus Textdateien.
2. **[Sequenzsteuerung und Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** – Steuere Befehlsfolgen, verwende Pipelines und kombiniere Textwerkzeuge wie `cut`, `grep`, `wc`, `sort` und `uniq`.

## Zusammenfassung

Du kannst nun mit `cut` vorhersehbare Positionen aus zeilenorientiertem Text auswählen.

1. Wähle einzelne Zeichenpositionen oder Bereiche aus.
2. Extrahiere tabulatorgetrennte Felder mit `-f`.
3. Gib mit `-d` ein einzeichenlanges Trennzeichen an.
4. Unterdrücke bei Bedarf Zeilen ohne Trennzeichen.
5. Lies strukturierte Texte aus Dateien oder stdin.
