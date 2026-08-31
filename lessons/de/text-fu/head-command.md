---
lesson_id: "head-command"
course_id: "text-fu"
lang: "de"
order_index: 8
title: "Kopf"
description: "Lerne, eine festgelegte Anzahl von Zeilen oder Bytes am Anfang einer Eingabe anzuzeigen."
meta_title: "head - Text-Fu"
meta_description: "Ein Linux-Leitfaden für Anfänger zur Verwendung des head-Befehls, um den Anfang einer Datei anzuzeigen. Erfahren Sie, wie Sie die Option head -n verwenden, um die Zeilenanzahl zu steuern – eine wesentliche Fähigkeit für jedes Linux-Tutorial."
meta_keywords: "head-Befehl, Linux head, Dateianfang anzeigen, Linux-Tutorial, Linux-Befehle, Linux für Anfänger, head -n, Linux-Leitfaden, Textdateien, Kommandozeile"
---

Der Befehl `head` zeigt den Anfang einer Datei oder eines Eingabestroms an. Er eignet sich zum Prüfen von Kopfzeilen, als Vorschau strukturierter Daten oder zum Entnehmen einer Stichprobe, ohne alles auszugeben.

## Die ersten zehn Zeilen anzeigen

Ohne Zähloption gibt `head` die ersten 10 Zeilen jeder benannten Datei aus:

```bash
$ head events.log
```

Die Datei wird dabei nicht verändert. Enthält sie weniger als 10 Zeilen, werden alle vorhandenen Zeilen ausgegeben.

:::single-choice{#head-default-lines}
Was gibt `head events.log` standardmäßig aus?

::option[Die letzten 10 Zeilen oder bei einer kürzeren Datei alle Zeilen.]{#head-last-ten explanation="Das Ende einer Eingabe zeigt `tail` an. `head` wählt vom Anfang aus."}
::option[Die ersten 10 Zeilen oder bei einer kürzeren Datei alle Zeilen.]{#head-first-ten .correct explanation="Ohne Zähloption wählt `head` bis zu zehn Zeilen am Anfang der Eingabe aus."}
::option[Unabhängig von der Dateilänge nur die erste Zeile.]{#head-first-one explanation="Für eine Zeile ist eine ausdrückliche Anzahl wie `-n 1` erforderlich; der Standardwert ist zehn."}
:::

## Eine Zeilenanzahl wählen

Mit `-n NUMBER` bestimmst du, wie viele Zeilen ausgegeben werden:

```bash
$ head -n 15 events.log
```

GNU `head` akzeptiert auch die Kurzform `-15`; `-n 15` macht die Bedeutung der Option jedoch deutlicher.

:::single-choice{#head-five-lines}
Welcher Befehl zeigt die ersten fünf Zeilen von `report.txt` an?

::option[`head -c 5 report.txt`]{#head-five-bytes explanation="Die Option `-c` zählt Bytes statt Zeilen und kann daher mitten in der ersten Zeile enden."}
::option[`head -n 5 report.txt`]{#head-report-five .correct explanation="Die Option `-n` wählt eine Zeilenanzahl; `5` fordert die ersten fünf Zeilen an."}
::option[`tail -n 5 report.txt`]{#tail-five-lines explanation="Dieser Befehl zeigt die letzten fünf Zeilen der Datei und nicht ihren Anfang."}
:::

## Eine Byteanzahl wählen

Verwende `-c NUMBER`, wenn du Bytes statt vollständiger Zeilen benötigst:

```bash
$ head -c 20 archive.bin
```

Damit werden die ersten 20 Bytes ausgegeben. Die Ausgabe kann mitten in einer Textzeile oder bei Mehrbyte-Text mitten in einem kodierten Zeichen enden. Für gewöhnliche Textvorschauen eignet sich der Zeilenmodus besser.

:::single-choice{#head-first-bytes}
Welcher Befehl schreibt die ersten 100 Bytes von `payload.bin` nach stdout?

::option[`head -c 100 payload.bin`]{#head-hundred-bytes .correct explanation="Die Option `-c` wählt eine Byteanzahl, sodass die ersten 100 verfügbaren Bytes angefordert werden."}
::option[`head -n 100 payload.bin`]{#head-hundred-lines explanation="Die Option `-n` zählt Zeilen, nicht Bytes. Dadurch können wesentlich mehr oder weniger als 100 Bytes entstehen."}
::option[`cut -c 100 payload.bin`]{#cut-hundredth-character explanation="Dieser Befehl wählt aus jeder Zeile Position 100 statt der ersten 100 Bytes der gesamten Eingabe."}
:::

## Von stdin und aus mehreren Dateien lesen

Ohne Dateioperanden liest `head` von stdin:

```bash
$ generate-report | head -n 5
```

Bei mehreren benannten Dateien setzt `head` normalerweise eine Kopfzeile mit dem jeweiligen Dateinamen vor die Ausgabe:

```bash
$ head -n 2 january.txt february.txt
==> january.txt <==
...

==> february.txt <==
...
```

Mit `-q` unterdrückst du diese Kopfzeilen; `-v` zeigt sie auch bei nur einer Datei an.

:::single-choice{#head-pipeline-preview}
Was liest `head` in `generate-report | head -n 5`?

::option[Über stdin die Standardausgabe von `generate-report`.]{#head-pipe-input .correct explanation="Die Pipe verbindet stdout des Erzeugers mit stdin von `head`, das daraus die ersten fünf Zeilen auswählt."}
::option[Die ersten fünf Dateinamen des aktuellen Verzeichnisses.]{#head-directory-names explanation="An der Pipeline ist kein Befehl zur Verzeichnisauflistung beteiligt. `head` erhält einen Datenstrom."}
::option[Fünf Bytes aus einer Datei namens `generate-report`.]{#head-producer-file explanation="Die linke Seite wird als Befehl ausgeführt; außerdem zählt `-n` Zeilen und nicht Bytes."}
:::

:::single-choice{#head-suppress-filename-headers}
Welche Option unterdrückt Dateinamen-Kopfzeilen, wenn `head` mehrere Dateien liest?

::option[`-v`]{#head-verbose explanation="Die Option `-v` fordert Kopfzeilen selbst bei einer einzelnen Datei an und bewirkt damit das Gegenteil."}
::option[`-c`]{#head-byte-option explanation="Die Option `-c` ändert die Auswahleinheit in Bytes. Dateinamen-Kopfzeilen steuert sie nicht."}
::option[`-q`]{#head-quiet .correct explanation="Die Option `-q`, kurz für „quiet“, verhindert, dass `head` Kopfzeilen für einzelne Dateien ausgibt."}
:::

Mit diesen Übungen kannst du Dateianfänge praktisch untersuchen:

1. **[Linux head Befehl: Anzeige des Dateianfangs](https://labex.io/de/labs/linux-linux-head-command-file-beginning-display-214302)** – Zeige mit `head` die ersten Zeilen von Textdateien an und ändere die ausgegebene Zeilenanzahl.
2. **[Anzeigen von Protokoll- und Konfigurationsdateien in Linux](https://labex.io/de/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** – Übe mit Befehlen wie `head` das effiziente Anzeigen von Protokoll- und Konfigurationsdateien.
3. **[Schnelle Bedrohungserkennung](https://labex.io/de/labs/linux-rapid-threat-detection-387930)** – Wende `head` und `tail` an, um Protokolleinträge schnell zu extrahieren und zu analysieren.

## Zusammenfassung

Du kannst nun mit `head` den Anfang von Dateien und Befehlsausgaben betrachten.

1. Verwende die standardmäßige Ansicht der ersten zehn Zeilen.
2. Wähle mit `-n` eine Zeilenanzahl.
3. Wähle bei Bedarf mit `-c` eine Byteanzahl.
4. Lies in einer Pipeline von stdin.
5. Steuere Kopfzeilen bei mehreren Dateien.
