---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "de"
order_index: 11
title: "Verbinden und Aufteilen"
description: "Lerne, zwei sortierte Textdateien über einen Schlüssel zu verbinden und eine Datei in benannte Teile aufzuteilen."
meta_title: "Verbinden und Aufteilen - Text-Fu"
meta_description: "Meistern Sie die Verwendung der Linux-Befehle join und split. Lernen Sie, Dateien effizient anhand gemeinsamer Felder zu verbinden und große Dateien in kleinere Teile aufzuteilen. Diese Anleitung behandelt, welchen Befehl Sie verwenden würden, um Dateien wie katze, hund, kuh zu verbinden, und andere praktische Beispiele."
meta_keywords: "linux dateien verbinden, welchen befehl würden sie verwenden um dateien zu verbinden, linux join befehl, linux split befehl, dateimanipulation, kommandozeile, textverarbeitung"
---

Die Befehle `join` und `split` lösen unterschiedliche Aufgaben der Dateiverarbeitung. `join` kombiniert zusammengehörige Datensätze aus zwei sortierten Texteingaben, während `split` eine Eingabe in eine Folge kleinerer Dateien aufteilt.

## Zwei Dateien über ihr erstes Feld verbinden

Standardmäßig vergleicht `join` das erste durch Leerraum getrennte Feld in genau zwei Eingabedateien. Betrachte diese bereits sortierten Dateien.

`people.txt`:

```text
1 John
2 Jane
3 Mary
```

`surnames.txt`:

```text
1 Doe
2 Doe
3 Sue
```

Verbinde Datensätze mit gleichen Schlüsselfeldern:

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Die Ausgabe enthält den gemeinsamen Schlüssel einmal, gefolgt von den übrigen Feldern der ersten und zweiten Datei. `join` verarbeitet jeweils zwei Dateien; drei gewöhnliche Dateioperanden bilden keine relationale Drei-Wege-Verknüpfung.

:::single-choice{#join-default-key} Welche Datensätze kombiniert `join first.txt second.txt` ohne Feldoptionen?

::option[Zeilen, deren erste durch Leerraum getrennte Felder gleich sind.]{#join-first-fields .correct explanation="Standardmäßig vergleicht `join` Feld 1 der beiden sortierten Eingaben."}
::option[Zeilen, die dieselbe physische Zeilennummer besitzen.]{#join-line-numbers explanation="Die Zuordnung richtet sich nach den Werten der Schlüsselfelder und nicht nur nach den Positionen der Datensätze."}
::option[Jede Zeile der ersten Datei mit jeder Zeile der zweiten.]{#join-all-pairs explanation="`join` gibt Datensätze für passende Schlüssel aus und bildet kein uneingeschränktes kartesisches Produkt aller Zeilen."}
:::

## Die Verknüpfungsschlüssel sortieren

Jede Eingabe muss nach ihrem Verknüpfungsfeld mit kompatiblen Vergleichsregeln geordnet sein. Bereite für das standardmäßige Feld 1 Kopien mit `sort -k 1,1` vor:

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

Wenn Sortierung und Verknüpfung dieselbe Locale verwenden, bleiben die Kollationsregeln konsistent. Leite eine Sortierung nicht zurück in ihren eigenen Eingabepfad, da die Shell die Datei zuvor leeren würde.

:::single-choice{#join-sort-requirement} Welche Vorbereitung benötigt `join` normalerweise für eine zuverlässige Zuordnung?

::option[Beide Dateien müssen genau gleich viele physische Zeilen enthalten.]{#join-equal-line-count explanation="Die Eingabelängen dürfen unterschiedlich sein. Passende Schlüssel und nicht gleiche Zeilenzahlen bestimmen die verknüpfte Ausgabe."}
::option[Die Dateinamen müssen in alphabetischer Sortierung nebeneinanderliegen.]{#join-filename-order explanation="Die Inhaltsschlüssel müssen sortiert sein; die lexikalische Beziehung der Dateinamen ist ohne Bedeutung."}
::option[Beide Dateien müssen nach ihren jeweiligen Verknüpfungsfeldern kompatibel sortiert sein.]{#join-sorted-keys .correct explanation="`join` durchläuft geordnete Schlüssel; deshalb muss jede Eingabe eine Reihenfolge verwenden, die zum durchgeführten Vergleich passt."}
:::

## Andere Verknüpfungsfelder auswählen

Mit `-1 FIELD` legst du den Schlüssel der ersten Datei fest, mit `-2 FIELD` den der zweiten. Angenommen, die erste Eingabe enthält:

```text
John 1
Jane 2
Mary 3
```

Die zweite enthält:

```text
1 Doe
2 Doe
3 Sue
```

Sortiere die erste Datei nach Feld 2 und die zweite nach Feld 1 und führe anschließend aus:

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Verwende `-t CHARACTER`, wenn ein einzelnes Nicht-Leerzeichen wie `:` die Felder trennt. Optionen wie `-a 1` oder `-a 2` können nicht zugeordnete Zeilen einer Eingabe aufnehmen; standardmäßig werden nur passende Schlüssel ausgegeben.

:::single-choice{#join-different-fields} Welche Optionen verbinden Feld 2 der ersten Datei mit Feld 1 der zweiten?

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="Damit wird Feld 1 der ersten und Feld 2 der zweiten Eingabe gewählt – die umgekehrte Zuordnung."}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2` wählt Feld 2 der ersten Datei; `-2 1` wählt Feld 1 der zweiten."}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="Diese Angaben ähneln Feld- und Trennzeichenoptionen anderer Textwerkzeuge. Für `join` sind sie keine Feldselektoren."}
:::

## Nach Zeilenanzahl aufteilen

`split` schreibt aufeinanderfolgende Abschnitte einer Eingabe in getrennte Ausgabedateien. Der Befehl ist nicht die Umkehrung einer schlüsselbasierten `join`-Verknüpfung.

```bash
$ split large.txt
```

GNU schreibt standardmäßig bis zu 1000 Zeilen pro Ausgabedatei und verwendet das Präfix `x`, sodass Namen wie `xaa`, `xab` und `xac` entstehen.

Mit `-l NUMBER` wählst du eine Zeilenzahl; ein letzter Operand legt das Ausgabepräfix fest:

```bash
$ split -l 500 large.txt part-
```

So entstehen `part-aa`, `part-ab` und weitere Dateien mit jeweils höchstens 500 Zeilen.

:::single-choice{#split-lines-with-prefix} Welcher Befehl teilt `large.txt` in Teile mit höchstens 500 Zeilen und dem Präfix `part-` auf?

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="Die Option `-b` wählt Bytes; bei gewöhnlichem Text wären die Teile damit deutlich kleiner als 500 Zeilen."}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500` setzt die maximale Zeilenanzahl; der letzte Operand liefert das Präfix für die Ausgabedateien."}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join` kombiniert schlüsselbasierte Datensätze aus zwei Dateien. Eine Eingabe teilt der Befehl nicht auf."}
:::

## Nach Größe aufteilen

Mit `-b SIZE` teilst du eine Eingabe nach Bytegröße. GNU-Suffixe wie `K`, `M` und `G` stehen hier für Zweierpotenzen auf Basis 1024:

```bash
$ split -b 10M archive.bin chunk-
```

Damit werden Teile von 10 Mebibyte angefordert; nur das letzte kann kleiner sein. `split` erstellt weder ein Archivmanifest noch Metadaten zur Wiederzusammensetzung. Bewahre die Reihenfolge der Suffixe und verkette die Teile gegebenenfalls in dieser Reihenfolge.

:::single-choice{#split-ten-mebibytes} Welcher Befehl teilt `archive.bin` mit dem Präfix `chunk-` in Teile von 10 MiB auf?

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="Die Option `-l` erwartet eine Zeilenanzahl und kein Größensuffix für binäre Teile."}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join` teilt keine Binäreingabe und unterstützt diesen Vorgang für Teilgrößen nicht."}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="Die Option `-b` wählt die Teilgröße; `10M` fordert 10×1024×1024 Bytes an und `chunk-` ist das Ausgabepräfix."}
:::

Mit diesen Übungen kannst du schlüsselbasierte Verknüpfungen und strukturierte Datenverarbeitung praktisch trainieren:

1. **[Linux join Befehl: Dateizusammenführung](https://labex.io/de/labs/linux-linux-join-command-file-joining-219193)** – Verbinde mit `join` Zeilen aus zwei sortierten Textdateien anhand eines gemeinsamen Feldes.
2. **[Verarbeitung von Mitarbeiterdaten](https://labex.io/de/labs/linux-processing-employees-data-388132)** – Kombiniere und verarbeite Daten aus mehreren Quellen mit `join` und weiteren Werkzeugen wie `awk`.

## Zusammenfassung

Du kannst nun sortierte Datensätze kombinieren oder eine Eingabe in geordnete Teile zerlegen.

1. Verbinde genau zwei Dateien über gleiche Schlüsselfelder.
2. Sortiere beide Eingaben konsistent nach ihren Verknüpfungsschlüsseln.
3. Wähle abweichende Schlüsselfelder mit `-1` und `-2`.
4. Teile mit `-l` nach Zeilenanzahl auf.
5. Teile mit `-b` und einem eindeutigen Präfix nach Bytegröße auf.
