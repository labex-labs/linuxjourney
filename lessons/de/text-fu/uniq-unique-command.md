---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "de"
order_index: 14
title: "uniq (Eindeutig)"
description: "Lerne, benachbarte Gruppen gleicher Zeilen mit uniq zusammenzufassen, zu zählen oder zu filtern."
meta_title: "uniq (Eindeutig) - Text-Fu"
meta_description: "Erkunden Sie den uniq-Befehl in Linux, um doppelte benachbarte Zeilen aus Text zu filtern und zu entfernen. Erfahren Sie, wie Sie das uniq Linux-Tool mit Optionen wie -c, -u, -d verwenden und es mit sort für leistungsstarke Textverarbeitung kombinieren."
meta_keywords: "uniq Befehl, Linux uniq, uniq linux, Duplikate entfernen, sort uniq, Textverarbeitung, Datenbereinigung, Linux Tutorial"
---

Der Befehl `uniq` vergleicht jede Eingabezeile mit ihrer Vorgängerzeile. Er kann benachbarte Gruppen gleicher Zeilen zusammenfassen, zählen oder auswählen, sucht jedoch nicht in der gesamten Datei nach getrennten Duplikaten.

## Benachbarte doppelte Zeilen zusammenfassen

Angenommen, `reading.txt` enthält gruppierte Werte:

```plaintext
book
book
paper
paper
article
article
magazine
```

Führe `uniq` ohne Filteroption aus, um eine repräsentative Zeile aus jeder benachbarten Gruppe auszugeben:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Die Eingabedatei bleibt unverändert, weil das Ergebnis nach stdout geschrieben wird.

:::single-choice{#uniq-collapse-adjacent} Was bewirkt `uniq reading.txt` standardmäßig?

::option[Der Befehl sortiert die vollständige Datei und entfernt anschließend jeden wiederholten Wert.]{#uniq-auto-sort explanation="`uniq` erhält die Eingabereihenfolge und sortiert nicht. Getrennte Vorkommen bleiben getrennte Gruppen."}
::option[Der Befehl gibt aus jeder benachbarten Gruppe gleicher Zeilen eine Zeile aus.]{#uniq-one-per-group .correct explanation="Standardmäßig fasst `uniq` aufeinanderfolgende gleiche Zeilen zu einer Ausgabezeile zusammen."}
::option[Der Befehl löscht doppelte Zeilen unmittelbar aus `reading.txt`.]{#uniq-edit-file explanation="Der gefilterte Text wird standardmäßig nach stdout geschrieben; die Eingabedatei wird nicht bearbeitet."}
:::

## Benachbarte Gruppen zählen

Mit `-c` stellst du jeder Ausgabegruppe die Anzahl ihrer aufeinanderfolgenden Eingabezeilen voran:

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Diese Werte sind Lauflängen und keine globalen Häufigkeiten, sofern nicht zuvor alle gleichen Zeilen nebeneinander angeordnet wurden.

:::single-choice{#uniq-count-groups} Was beschreibt die Zahl von `uniq -c`?

::option[Die Anzahl der Zeichen in jeder Eingabezeile.]{#uniq-character-count explanation="Zeichen zu zählen ist nicht Aufgabe von `uniq -c`; Werkzeuge wie `wc` ermitteln Zeichen- und Bytesummen."}
::option[Die Anzahl aufeinanderfolgender gleicher Zeilen in jeder Gruppe.]{#uniq-consecutive-count .correct explanation="`-c` stellt jeder zusammengefassten benachbarten Gruppe die Anzahl ihrer enthaltenen Zeilen voran."}
::option[Die Gesamtzahl passender Zeilen an beliebigen Stellen der Datei.]{#uniq-global-count explanation="Getrennte gleiche Zeilen bilden eigene Gruppen, sofern die Daten nicht zuvor sortiert oder anderweitig gruppiert wurden."}
:::

## Einmalige oder wiederholte Gruppen auswählen

Mit `-u` gibst du nur Gruppen aus, die genau eine Zeile enthalten:

```bash
$ uniq -u reading.txt
magazine
```

Mit `-d` gibst du eine repräsentative Zeile aus jeder benachbarten Gruppe mit mehr als einer Zeile aus:

```bash
$ uniq -d reading.txt
book
paper
article
```

GNU `uniq -D` gibt jede Zeile aus wiederholten Gruppen aus, während das kleine `-d` ihren Wert jeweils einmal ausgibt.

:::single-choice{#uniq-only-singletons} Welcher Befehl gibt nur benachbarte Gruppen aus, die genau einmal vorkommen?

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="Dieser Befehl gibt jede Gruppe mit einer Anzahl aus, sowohl wiederholte als auch einmalige Gruppen."}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="Das kleine `-d` gibt je eine Zeile für wiederholte Gruppen aus und wählt damit das Gegenteil."}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="Die Option `-u` wählt Gruppen aus, deren benachbarte Lauflänge genau eins beträgt."}
:::

:::single-choice{#uniq-one-per-duplicate-group} Welcher Befehl gibt für jede benachbarte Gruppe mit mehr als einem Vorkommen eine Zeile aus?

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="Die Option `-d` wählt wiederholte benachbarte Gruppen und gibt pro Gruppe eine repräsentative Zeile aus."}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="Das große GNU-`-D` gibt alle Zeilen wiederholter Gruppen aus und nicht nur eine repräsentative Zeile."}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="Die Option `-u` wählt einmalige statt wiederholte Gruppen aus."}
:::

## Getrennte Duplikate gruppieren

Sind gleiche Zeilen voneinander getrennt, bilden sie unterschiedliche Gruppen:

```plaintext
book
paper
book
paper
article
magazine
article
```

`uniq` erzeugt bei dieser Datei ein möglicherweise überraschendes Ergebnis:

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

Keine Zeile wird zusammengefasst, da sich benachbarte Werte unterscheiden. Sortiere zuerst, wenn eine veränderte Reihenfolge zulässig ist und gleiche vollständige Zeilen gruppiert werden sollen:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Verwende für beide Schritte eine einheitliche Locale und Vergleichsregel. `sort -u reading.txt` kann ebenfalls in einem Befehl sortieren und je gleichem Sortierschlüssel eine Zeile bewahren.

:::single-choice{#uniq-separated-duplicates} Gleiche Zeilen sind über `reading.txt` verteilt und die Ausgabereihenfolge darf sich ändern. Welche Pipeline erzeugt je vollständiger unterschiedlicher Zeile eine sortierte Kopie?

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="Die Sortierung gruppiert gleiche vollständige Zeilen; anschließend fasst `uniq` jede benachbarte Gruppe zu einer Zeile zusammen."}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="`uniq` läuft, bevor getrennte gleiche Zeilen benachbart werden. Nach der späteren Sortierung können daher weiterhin doppelte Ausgabezeilen vorhanden sein."}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="Dieser Befehl zählt vorhandene benachbarte Gruppen und begrenzt danach die Ausgabe. Getrennte Duplikate werden nicht global gruppiert."}
:::

Ohne benannte Eingabedatei liest `uniq` von stdin und passt daher gut hinter `sort`. GNU-Optionen wie `-i` können Groß- und Kleinschreibung ignorieren; `-f`, `-s` und `-w` können Vergleichsbereiche überspringen oder begrenzen. Verwende sie nur, wenn Gleichheit über einen Teil jeder Zeile definiert werden soll.

Mit diesen Übungen kannst du das Gruppieren, Zählen und Filtern von Duplikaten praktisch trainieren:

1. **[Linux uniq Befehl: Duplikate filtern](https://labex.io/de/labs/linux-linux-uniq-command-duplicate-filtering-219199)** – Kombiniere `uniq` mit `sort`, um doppelte Zeilen zu erkennen, zu filtern und zu analysieren.
2. **[Linux sort Befehl: Text sortieren](https://labex.io/de/labs/linux-linux-sort-command-text-sorting-219196)** – Ordne mit `sort` Textzeilen als Vorbereitung auf den wirksamen Einsatz von `uniq`.
3. **[Wortanzahl und Sortierung](https://labex.io/de/labs/linux-word-count-and-sorting-388125)** – Nutze `wc` und `sort`, um Zeilen, Wörter und Zeichen zu zählen, häufige Muster zu finden und Daten effizient zu sortieren.

## Zusammenfassung

Du kannst nun benachbarte Gruppen gleicher Zeilen mit `uniq` analysieren.

1. Fasse jede benachbarte Duplikatgruppe zu einer Zeile zusammen.
2. Zähle aufeinanderfolgende Vorkommen mit `-c`.
3. Wähle einmalige Gruppen mit `-u` aus.
4. Wähle wiederholte Gruppen mit `-d` oder GNU `-D` aus.
5. Sortiere zuerst, wenn getrennte Duplikate gruppiert werden müssen.
