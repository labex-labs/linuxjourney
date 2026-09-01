---
lesson_id: "nl-wc-command"
course_id: "text-fu"
lang: "de"
order_index: 15
title: "wc und nl"
description: "Lerne, Zeilen, Wörter, Bytes oder Zeichen mit wc zu zählen und Zeilen mit nl zu nummerieren."
meta_title: "wc und nl - Text-Fu"
meta_description: "Meistern Sie die Befehle wc und nl in diesem Linux-Tutorial. Erfahren Sie, wie Sie eine Linux-Wortzählung durchführen, Zeilennummern zu Dateien hinzufügen und grundlegende Datei-Analysen durchführen. Ein perfekter Leitfaden für Anfänger zur Verbesserung ihrer Kommandozeilen-Fähigkeiten."
meta_keywords: "wc Befehl, nl Befehl, Linux Wortzählung, Wörter in Datei zählen Linux, Linux Zeilennummern, nl Befehl Linux, Datei-Analyse, Textverarbeitung Linux, Linux Kommandozeile, Linux Tutorial für Anfänger"
---

Der Befehl `wc` zählt Eigenschaften von Textströmen, während `nl` die Eingabe mit erzeugten Zeilennummern ausgibt. Beide lesen Dateien oder stdin und schreiben ihre Ergebnisse nach stdout.

## Die Standardausgabe von wc lesen

Ohne Zähloption gibt `wc` die Anzahl der Zeilenumbrüche, Wörter und Bytes aus; wurde eine Datei angegeben, folgt deren Name:

```bash
$ printf 'red blue\ngreen\n' > colors.txt
$ wc colors.txt
 2  3 15 colors.txt
```

Von links nach rechts:

1. `2` Zeilenumbruchzeichen, als Zeilen gemeldet.
2. `3` durch Leerraum getrennte Wörter.
3. `15` Bytes in diesem ASCII-Beispiel.

Eine letzte Textzeile ohne abschließenden Zeilenumbruch wird von `wc -l` nicht gezählt, da diese Option Zeilenumbruchzeichen und nicht optisch wahrgenommene Zeilen zählt.

:::single-choice{#wc-default-columns} Wofür stehen die ersten drei Zahlen der Standardausgabe von `wc file.txt`?

::option[Für Zeilen, Wörter und Bytes in dieser Reihenfolge.]{#wc-lines-words-bytes .correct explanation="Die Standardausgabe von `wc` meldet vor dem Dateinamen die Anzahl der Zeilenumbrüche, Wörter und Bytes."}
::option[Für Bytes, Wörter und Zeilen in dieser Reihenfolge.]{#wc-bytes-words-lines explanation="Das sind dieselben Messwerte in falscher Reihenfolge. Die Zeilenanzahl steht zuerst."}
::option[Für Dateien, Zeichen und Absätze in dieser Reihenfolge.]{#wc-files-characters-paragraphs explanation="Die Standardspalten zählen weder Dateien noch Absätze; der dritte Standardmesswert sind Bytes."}
:::

## Einen einzelnen Messwert anfordern

Wähle nur den benötigten Messwert:

- `-l`: Zählt Zeilenumbruchzeichen.
- `-w`: Zählt Wörter.
- `-c`: Zählt Bytes.
- `-m`: Zählt Zeichen gemäß der aktuellen Locale.

Zum Beispiel:

```bash
$ wc -w colors.txt
3 colors.txt
```

Bei ASCII-Text sind Byte- und Zeichenanzahl gleich, bei Mehrbyte-Kodierungen wie UTF-8 können sie sich unterscheiden. Wird stdin ohne Dateinamenoperand verwendet, lässt `wc` die Dateibezeichnung normalerweise weg:

```bash
$ printf 'one two\n' | wc -w
2
```

:::single-choice{#wc-word-count-only} Welcher Befehl meldet ausschließlich die Wortanzahl von `essay.txt`?

::option[`wc -l essay.txt`]{#wc-lines-essay explanation="Die Option `-l` meldet Zeilenumbruchzeichen und keine Wörter."}
::option[`wc -w essay.txt`]{#wc-words-essay .correct explanation="Die Option `-w` wählt die Wortanzahl aus."}
::option[`wc -c essay.txt`]{#wc-bytes-essay explanation="Die Option `-c` meldet Bytes statt durch Leerraum getrennter Wörter."}
:::

:::single-choice{#wc-characters-not-bytes} Welche Option weist `wc` an, in der aktuellen Locale Zeichen statt Bytes zu zählen?

::option[`-m`]{#wc-character-option .correct explanation="Die Option `-m` meldet Zeichen; bei Mehrbyte-Text kann sich diese Anzahl von der Bytezahl unterscheiden."}
::option[`-c`]{#wc-byte-option explanation="Die Option `-c` meldet Bytes. In Kodierungen wie UTF-8 kann ein Zeichen mehrere Bytes belegen."}
::option[`-w`]{#wc-word-option explanation="Die Option `-w` zählt Wörter statt Zeichen oder Bytes."}
:::

Bei mehreren benannten Dateien gibt `wc` ein Ergebnis pro Datei und eine Zeile `total` aus. GNU `wc -L` meldet die maximale Anzeigebreite einer Eingabezeile.

## Nicht leere Zeilen mit nl nummerieren

Standardmäßig nummeriert `nl` nicht leere Zeilen im logischen Textkörper seiner Eingabe. Angenommen, `notes.txt` enthält eine leere zweite Zeile:

```text
alpha

beta
```

Die Leerzeile bleibt erhalten, erhält aber keine Nummer:

```bash
$ nl notes.txt
	 1	alpha

	 2	beta
```

`nl` schreibt eine nummerierte Ausgabe; `notes.txt` wird nicht verändert.

:::single-choice{#nl-default-blank-lines} Wie behandelt `nl notes.txt` standardmäßig leere Zeilen im Textkörper?

::option[Der Befehl lässt jede Leerzeile vollständig aus der Ausgabe weg.]{#nl-omit-blank explanation="Die Leerzeile bleibt in der Ausgabe, erhält standardmäßig aber keine Nummer."}
::option[Der Befehl bewahrt sie ohne Zeilennummer.]{#nl-preserve-unnumbered .correct explanation="Der Standardstil für den Textkörper nummeriert nicht leere Zeilen und reicht Leerzeilen unnummeriert durch."}
::option[Der Befehl nummeriert sie in derselben Folge wie nicht leere Zeilen.]{#nl-number-blank-default explanation="Zum Nummerieren jeder Textkörperzeile ist ein anderer Stil wie `-ba` erforderlich."}
:::

## Jede Zeile nummerieren

Mit `-ba` wählst du für den Textkörper den Nummerierungsstil `a`, der alle Zeilen nummeriert:

```bash
$ nl -ba notes.txt
	 1	alpha
	 2
	 3	beta
```

Weitere Optionen steuern die Formatierung. Beispielsweise legt `-w 3` die Breite des Nummernfelds fest und `-s ': '` ändert das Trennzeichen hinter der Nummer.

:::single-choice{#nl-number-all-lines} Welcher Befehl nummeriert jede Textkörperzeile von `notes.txt`, einschließlich Leerzeilen?

::option[`nl -w 3 notes.txt`]{#nl-width-three explanation="Damit wird die Breite des Nummernfelds verändert; die standardmäßige Regel, nur nicht leere Zeilen zu nummerieren, bleibt bestehen."}
::option[`nl -ba notes.txt`]{#nl-body-all .correct explanation="Die Option `-b` wählt den Textkörperstil; Stil `a` nummeriert alle Zeilen."}
::option[`wc -l notes.txt`]{#wc-lines-notes explanation="Dieser Befehl gibt die Anzahl der Zeilenumbruchzeichen aus und reproduziert die Datei nicht mit Zeilennummern."}
:::

Mit diesen Übungen kannst du das Zählen und Nummerieren von Text praktisch trainieren:

1. **[Linux wc Befehl: Textzählung](https://labex.io/de/labs/linux-linux-wc-command-text-counting-219200)** – Zähle mit `wc` Wörter, Zeilen und Zeichen in Textdateien.
2. **[Linux nl Befehl: Zeilennummerierung](https://labex.io/de/labs/linux-linux-nl-command-line-numbering-210988)** – Nummeriere mit `nl` die Zeilen von Textdateien.
3. **[Wortanzahl und Sortierung](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** – Kombiniere `wc` mit Sortierung, um Zeilen, Wörter und Zeichen zu zählen und Text praktisch zu analysieren.

## Zusammenfassung

Du kannst nun Textströme messen und sichtbare Zeilennummern hinzufügen, ohne die Quelle zu verändern.

1. Deute die Standardspalten für Zeilen, Wörter und Bytes von `wc`.
2. Wähle mit `-l`, `-w`, `-c` oder `-m` einen Messwert.
3. Unterscheide Byte- und Zeichenanzahl.
4. Nummeriere nicht leere Zeilen mit dem Standardverhalten von `nl`.
5. Nummeriere mit `nl -ba` auch Leerzeilen.
