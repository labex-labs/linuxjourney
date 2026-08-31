---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "de"
order_index: 7
title: "paste"
description: "Lerne, entsprechende Zeilen zusammenzuführen oder Zeilen mit einstellbaren Trennzeichen zu serialisieren."
meta_title: "paste - Text-Fu"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl paste verwenden, um Dateizeilen zusammenzuführen. Entdecken Sie Trennzeichen und kombinieren Sie Dateien mit diesem grundlegenden Linux-Befehls-Tutorial."
meta_keywords: "Linux paste Befehl, paste Befehl Tutorial, Dateizeilen zusammenführen, Linux Befehle, Linux für Anfänger, Linux Anleitung"
---

Der Befehl `paste` kombiniert Zeilen zu Spalten. Standardmäßig nimmt er aus jeder Eingabedatei eine Zeile, verbindet diese Zeilen mit einem Tabulator und wiederholt den Vorgang, bis alle Eingaben ihr Dateiende erreicht haben.

## Dateien nebeneinander zusammenführen

Erstelle zwei kleine Dateien:

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

Übergib beide Dateien an `paste`:

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

Der sichtbare Abstand zwischen den Spalten ist ein Tabulator. Anders als `cat`, das vollständige Dateien nacheinander ausgibt, verbindet `paste` die jeweils entsprechenden Eingabezeilen.

:::single-choice{#paste-corresponding-lines}
`first.txt` enthält nacheinander `A` und `B`, `second.txt` enthält `1` und `2`. Was erzeugt `paste first.txt second.txt` standardmäßig?

::option[`A`, `B`, `1` und `2` auf vier aufeinanderfolgenden Zeilen.]{#paste-concatenated-files explanation="Das entspräche eher einer Ausgabe der Dateien nacheinander. `paste` verbindet stattdessen jeweils zusammengehörige Zeilen."}
::option[`A`, `B`, `1` und `2` ohne Trennzeichen auf einer Zeile.]{#paste-one-line-no-separator explanation="Eine Serialisierung in eine Zeile erfordert `-s`; das Standardtrennzeichen ist außerdem ein Tabulator und nicht die leere Zeichenfolge."}
::option[Zuerst `A` mit `1`, dann `B` mit `2`, jeweils durch einen Tabulator getrennt.]{#paste-parallel-result .correct explanation="Der parallele Standardmodus nimmt für jede Ausgabezeile eine Zeile aus jeder Datei und trennt die Felder durch einen Tabulator."}
:::

## Ein Trennzeichen wählen

Mit `-d LIST` ersetzt du den standardmäßigen Tabulator. Für einen Doppelpunkt:

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

Schütze Trennzeichen mit Shell-Bedeutung durch Anführungszeichen. Enthält die Liste mehrere Zeichen, kann `paste` sie abwechselnd verwenden; für zwei Spalten ist ein einzelnes Zeichen am einfachsten.

:::single-choice{#paste-colon-delimiter}
Welcher Befehl verbindet entsprechende Zeilen aus `names.txt` und `roles.txt` mit einem Doppelpunkt?

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="Die Option `-d` ersetzt den standardmäßigen Tabulator für jedes Feldpaar durch den angegebenen Doppelpunkt."}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="Die Option `-s` wählt den seriellen Modus; `:` würde als weiterer Eingabepfad statt als Trennzeichen behandelt."}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="Ohne `-d` wird jeder Operand als Eingabedatei behandelt. Der Befehl würde versuchen, eine Datei namens `:` zu öffnen."}
:::

## Zeilen einer Datei serialisieren

Die Option `-s` verarbeitet jede Eingabedatei seriell und verbindet ihre Zeilen zu einer Ausgabezeile. Erstelle eine Datei mit einem Wort pro Zeile:

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

Kombiniere `-s` mit `-d`, um das Trennzeichen festzulegen:

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

Werden mit `-s` mehrere Dateien angegeben, wird jede Datei zu einer eigenen Ausgabezeile.

:::single-choice{#paste-serialize-with-spaces}
Welcher Befehl verbindet alle Zeilen von `words.txt` zu einer einzigen, durch Leerzeichen getrennten Ausgabezeile?

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="Im parallelen Standardmodus erzeugt auch eine einzelne Eingabedatei weiterhin eine Ausgabezeile pro Eingabezeile. Das Trennzeichen hat zwischen Dateien nichts zu verbinden."}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="Dieser Befehl serialisiert zwei Dateien getrennt mit dem standardmäßigen Tabulator und erzeugt zwei Ausgabezeilen statt des verlangten Ergebnisses."}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s` serialisiert die Dateizeilen; `-d ' '` setzt ein Leerzeichen zwischen sie."}
:::

## Eingaben unterschiedlicher Länge behandeln

Besitzen parallele Eingabedateien unterschiedlich viele Zeilen, arbeitet `paste` bis zum Ende der längsten Datei weiter. Fehlende Werte einer kürzeren Datei werden zu leeren Feldern:

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files}
Was geschieht, wenn eine an paralleles `paste` übergebene Datei vor einer anderen endet?

::option[`paste` verwendet für diese Datei leere Felder, bis die längste Eingabe endet.]{#paste-empty-fields .correct explanation="Der parallele Modus arbeitet weiter, bis alle Dateien erschöpft sind, und stellt fehlende Zeilen kürzerer Eingaben als leere Felder dar."}
::option[`paste` beendet sich sofort und verwirft verbleibende Zeilen.]{#paste-stop-shortest explanation="`paste` arbeitet bis zum Ende der längsten Eingabe; verbleibende Zeilen gehen nicht allein deshalb verloren, weil eine andere Datei endete."}
::option[`paste` beginnt mit der kürzeren Datei wieder von vorn.]{#paste-repeat-shorter explanation="Der Befehl wiederholt keine Eingabedatensätze. Eine erschöpfte Eingabe liefert leere Felder."}
:::

## Eine Eingabe von stdin lesen

Verwende `-` als Dateioperanden, um an dieser Position von stdin zu lesen:

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand}
Was bedeutet der Operand `-` in `producer | paste names.txt -`?

::option[Das zusammengeführte Ergebnis nach stderr schreiben.]{#paste-write-stderr explanation="Der Bindestrich bezeichnet hier eine Eingabequelle. Einen Ausgabestrom leitet er nicht um."}
::option[Die Trennzeichen zwischen den beiden Spalten entfernen.]{#paste-remove-delimiter explanation="Das Trennzeichen wird mit `-d` ausgewählt. Der Bindestrich verändert es nicht."}
::option[Diese Eingabespalte von stdin lesen.]{#paste-read-stdin .correct explanation="Der Bindestrich weist `paste` an, an dieser Operandenposition die Standardeingabe zu verwenden."}
:::

Mit dieser Übung kannst du das Zusammenführen zeilenorientierter Daten praktisch trainieren:

1. **[Einfache Textverarbeitung](https://labex.io/de/labs/linux-simple-text-processing-18004)** – Verarbeite und analysiere Textdaten effizient mit Werkzeugen wie `tr`, `col`, `join` und `paste`.

## Zusammenfassung

Du kannst nun zeilenorientierte Eingaben mit vorhersehbarer Ausrichtung und gewählten Trennzeichen kombinieren.

1. Führe entsprechende Zeilen aus mehreren Dateien zusammen.
2. Ersetze den standardmäßigen Tabulator mit `-d`.
3. Serialisiere die Zeilen einer Datei mit `-s`.
4. Deute leere Felder aus kürzeren Eingaben.
5. Verwende `-`, wenn eine Eingabe von stdin stammt.
