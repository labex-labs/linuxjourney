---
lang: "de"
title: "Gerätetypen"
meta_description: "Erfahren Sie mehr über Linux-Gerätetypen (character, block, pipe, socket) und wie Sie diese mit `ls -l /dev` identifizieren können. Verstehen Sie Major/Minor Device Numbers. Linux-Tutorial für Anfänger."
meta_keywords: "Linux-Gerätetypen, ls -l /dev, character device, block device, major minor device number, Linux-Tutorial, Linux-Anleitung, Anfänger"
---

## Lesson Content

Bevor wir darüber sprechen, wie Geräte verwaltet werden, werfen wir einen Blick auf einige Geräte.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

Die Spalten sind von links nach rechts wie folgt:

- Permissions
- Owner
- Group
- Major Device Number
- Minor Device Number
- Timestamp
- Device Name

Denken Sie daran, dass Sie im `ls`-Befehl den Dateityp am ersten Bit jeder Zeile erkennen können. Gerätedateien werden wie folgt bezeichnet:

- c - character
- b - block
- p - pipe
- s - socket

### Character Device

Diese Geräte übertragen Daten, aber zeichenweise. Sie werden viele Pseudogeräte (`/dev/null`) als Character Devices sehen. Diese Geräte sind nicht wirklich physisch mit der Maschine verbunden, aber sie ermöglichen dem Betriebssystem eine größere Funktionalität.

### Block Device

Diese Geräte übertragen Daten, aber in großen, festen Blöcken. Am häufigsten sehen Sie Geräte, die Datenblöcke als Block Devices verwenden, wie Festplatten, Dateisysteme usw.

### Pipe Device

Benannte Pipes ermöglichen es zwei oder mehr Prozessen, miteinander zu kommunizieren. Diese ähneln Character Devices, aber anstatt dass die Ausgabe an ein Gerät gesendet wird, wird sie an einen anderen Prozess gesendet.

### Socket Device

Socket Devices erleichtern die Kommunikation zwischen Prozessen, ähnlich wie Pipe Devices, aber sie können mit vielen Prozessen gleichzeitig kommunizieren.

### Device Characterization

Geräte werden anhand von zwei Zahlen charakterisiert: **major device number** und **minor device number**. Sie können diese Zahlen im obigen `ls`-Beispiel sehen; sie sind durch ein Komma getrennt. Nehmen wir zum Beispiel an, ein Gerät hätte die Gerätenummern: **8, 0**:

Die Major Device Number repräsentiert den verwendeten Gerätetreiber, in diesem Fall 8, was oft die Major Number für sd block devices ist. Die Minor Number teilt dem Kernel mit, welches eindeutige Gerät es in dieser Treiberklasse ist; in diesem Fall wird 0 verwendet, um das erste Gerät (a) darzustellen.

## Exercise

Schauen Sie sich Ihr `/dev`-Verzeichnis an und finden Sie heraus, welche Arten von Geräten Sie sehen können.

## Quiz Question

Was ist das Symbol für Character Devices im Befehl `ls -l`?

## Quiz Answer

c
