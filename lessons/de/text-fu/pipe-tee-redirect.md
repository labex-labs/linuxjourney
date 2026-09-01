---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "de"
order_index: 4
title: "Pipe und Tee"
description: "Lerne, Befehle mit Pipelines zu verbinden und einen Strom mit tee zu speichern und zugleich weiterzugeben."
meta_title: "Pipe und Tee - Text-Fu"
meta_description: "Entdecken Sie den leistungsstarken Pipe- und Tee-Befehl in Linux. Erfahren Sie, wie Sie Befehle mit der Linux Pipe-Tee-Kombination verketten und die Ausgabe sowohl auf dem Bildschirm als auch in einer Datei umleiten. Diese Anleitung behandelt das Piping zu tee für einen erweiterten Kommandozeilen-Datenfluss."
meta_keywords: "pipe und tee befehl in linux, linux pipe tee, pipe zu tee, linux pipe, tee befehl, stdout, stdin, kommandozeilenumleitung, linux tutorial"
---

Pipelines verbinden kleine Befehle, sodass Daten ohne Zwischendatei zwischen ihnen fließen können. Mit `tee` kannst du einen Teil dieses Stroms in eine Datei kopieren und zugleich weiterleiten.

## Befehle mit | verbinden

Angenommen, eine Verzeichnisauflistung ist zu lang, um sie auf einmal zu lesen:

```bash
$ ls -la /etc
```

Setze den Pipe-Operator `|` zwischen zwei Befehle, um stdout des linken Befehls mit stdin des rechten zu verbinden:

```bash
$ ls -la /etc | less
```

Die Shell startet die Pipeline-Befehle und richtet die Stromverbindung ein. Die Befehle können gleichzeitig arbeiten: `less` kann bereits lesen, bevor `ls` seine gesamte Auflistung erzeugt hat.

:::single-choice{#pipe-stream-connection} Welche Ströme verbindet `|` in `ls -la /etc | less` standardmäßig?

::option[stdin von `ls` mit stdout von `less`.]{#pipe-reversed-streams explanation="Damit wären Erzeuger, Verbraucher und beide Ströme vertauscht. Die Daten fließen von der Ausgabe des linken Befehls zur Eingabe des rechten."}
::option[stderr von `ls` mit beiden Strömen von `less`.]{#pipe-stderr-both explanation="Eine gewöhnliche Pipe verbindet stderr des linken Befehls nicht und zielt auch nicht auf beide Ströme des rechten."}
::option[stdout von `ls` mit stdin von `less`.]{#pipe-stdout-stdin .correct explanation="Eine Standardpipeline verbindet Dateideskriptor 1 des linken Befehls mit Dateideskriptor 0 des rechten."}
:::

## stderr getrennt halten

Ein einfaches `|` überträgt nur stdout. Stderr des linken Befehls behält sein bisheriges Ziel, häufig also das Terminal:

```bash
$ find /etc -name "*.conf" | less
```

Passende Pfade fließen durch die Pipe, während Berechtigungsdiagnosen weiterhin unmittelbar im Terminal erscheinen können. Leite stderr getrennt um, wenn du ein anderes Verhalten benötigst:

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr} Wohin fließt stderr von `find` in `find /etc -name "*.conf" | less` normalerweise, wenn keine weitere Umleitung vorhanden ist?

::option[Durch dieselbe Pipe wie stdout nach `less`.]{#pipe-errors-to-less explanation="Die gewöhnliche Pipe verbindet nur stdout. Stderr wird nicht automatisch damit zusammengeführt."}
::option[In eine Datei namens `stderr` im aktuellen Verzeichnis.]{#pipe-errors-to-file explanation="Es ist keine Umleitung in eine Fehlerdatei angegeben, daher erstellt die Shell keine solche Datei."}
::option[An sein bisheriges Ziel, normalerweise das Terminal.]{#pipe-errors-terminal .correct explanation="Da Deskriptor 2 unverändert bleibt, sind Diagnosen üblicherweise weiterhin mit dem Terminal verbunden."}
:::

## Einen Strom mit tee kopieren

`tee` liest stdin, schreibt eine Kopie in jede benannte Datei und gibt dieselben Daten außerdem nach stdout aus:

```bash
$ ls | tee listing.txt
```

Hier erhält `listing.txt` die Auflistung, während stdout von `tee` mit dem Terminal verbunden bleibt. Standardmäßig erstellt oder leert `tee` die benannte Datei wie `>`.

:::single-choice{#tee-display-and-save} Welcher Befehl zeigt die Ausgabe von `generate-report` an und ersetzt zugleich `report.txt` durch dieselbe Ausgabe?

::option[`generate-report > report.txt`]{#redirect-report-only explanation="Eine einfache Ausgabeumleitung schreibt zwar die Datei, lässt aber keine Kopie zum Terminal weiterfließen."}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee` kopiert stdin nach `report.txt` und in seine Standardausgabe, die in dieser Pipeline mit dem Terminal verbunden bleibt."}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="Damit wird `generate-report` als Zieldatei behandelt und versucht, `report.txt` als Befehl auszuführen. Der Erzeuger gehört nach links."}
:::

Verwende `-a`, wenn die Datei ergänzt statt ersetzt werden soll:

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log} Welcher Befehl zeigt das aktuelle Datum an und hängt es an `activity.log` an?

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="Mit der Option `-a` hängt `tee` an die Datei an und kopiert die Eingabe weiterhin nach stdout."}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="Ohne `-a` ersetzt `tee` die vorhandene Datei, statt frühere Einträge zu erhalten."}
::option[`date > activity.log`]{#redirect-replace-activity explanation="Damit wird die Datei ersetzt und keine Kopie zum Terminal gesendet. Weder Anhängen noch Anzeigen ist erfüllt."}
:::

## Ein Zwischenergebnis speichern

Setze `tee` in die Mitte einer Pipeline, um einen Zwischenstrom zu speichern und zugleich weiterzuverarbeiten:

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

Diese Pipeline:

1. erzeugt die vollständige lange Auflistung,
2. speichert den vollständigen Strom in `etc-listing.txt` und
3. sendet denselben Strom an `grep`, das nur Zeilen mit `conf` ausgibt.

Die Datei enthält die Daten vor der Filterung durch `grep`. Soll sie nur die gefilterten Zeilen enthalten, setze `tee` hinter `grep`.

:::single-choice{#tee-before-filter-result} Was enthält `all.txt`, nachdem `produce | tee all.txt | grep error` erfolgreich beendet wurde?

::option[Nur die von `grep` gefundenen Zeilen.]{#tee-filtered-only explanation="`tee` läuft vor `grep` und schreibt deshalb die ungefilterte Eingabe statt der nachfolgenden Treffermenge."}
::option[Nur stderr von `produce`.]{#tee-producer-stderr explanation="Eine gewöhnliche Pipe überträgt stdout von `produce`. Dessen stderr ist nicht die Eingabe von `tee`."}
::option[Die gesamte vor der Filterung erzeugte Standardausgabe.]{#tee-complete-intermediate .correct explanation="`tee` speichert jedes empfangene Byte und reicht denselben Strom anschließend zur Filterung an `grep` weiter."}
:::

Mit diesen Labs kannst du Pipelines und das Kopieren von Strömen praktisch trainieren:

1. **[Redirecting Input and Output in Linux](https://labex.io/de/labs/comptia-redirecting-input-and-output-in-linux-590840)** – Steuere Standardausgabe, Standardfehler und Standardeingabe mit Operatoren wie `>`, `>>` und `2>` sowie mit `tee`.
2. **[Sequence Control and Pipeline](https://labex.io/de/labs/linux-sequence-control-and-pipeline-17994)** – Steuere Befehlsfolgen, verwende Pipelines und kombiniere Werkzeuge wie `cut`, `grep`, `wc`, `sort` und `uniq`.
3. **[Data Stream Redirection](https://labex.io/de/labs/linux-data-stream-redirection-17995)** – Leite Eingabe-, Ausgabe- und Fehlerströme um, kombiniere Ausgaben und nutze `/dev/null`.

## Zusammenfassung

Du kannst nun Befehle verbinden und ausgewählte Stellen in einem Datenstrom bewahren.

1. Leite stdout eines Befehls in stdin eines anderen.
2. Leite stderr bei Bedarf getrennt um.
3. Kopiere Eingaben mit `tee` zugleich in eine Datei und nach stdout.
4. Hänge mit `tee -a` an, statt eine Datei zu ersetzen.
5. Setze `tee` bewusst vor oder hinter einen Filter.
