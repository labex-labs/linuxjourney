---
index: 2
lang: "de"
title: "Gerätetypen"
meta_title: "Gerätetypen - Geräte"
meta_description: "Erfahren Sie mehr über Linux-Gerätetypen (Character, Block, Pipe, Socket) und wie Sie diese mit `ls -l /dev` identifizieren können. Verstehen Sie Major/Minor Device Numbers. Linux-Tutorial für Anfänger."
meta_keywords: "Linux-Gerätetypen, ls -l /dev, Zeichenschnittstellengerät, Blockgerät, Major Minor Device Number, Linux-Tutorial, Linux-Anleitung, Anfänger"
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

- Berechtigungen
- Eigentümer
- Gruppe
- Major Device Number
- Minor Device Number
- Zeitstempel
- Gerätename

Denken Sie daran, dass Sie im `ls`-Befehl den Dateityp am ersten Bit jeder Zeile erkennen können. Gerätedateien werden wie folgt bezeichnet:

- c - character
- b - block
- p - pipe
- s - socket

### Zeichenschnittstellengerät (Character Device)

Diese Geräte übertragen Daten, aber Zeichen für Zeichen. Sie werden viele Pseudogeräte (`/dev/null`) als Zeichenschnittstellengeräte sehen. Diese Geräte sind nicht wirklich physisch mit der Maschine verbunden, aber sie ermöglichen dem Betriebssystem eine größere Funktionalität.

### Blockgerät (Block Device)

Diese Geräte übertragen Daten, aber in großen, festen Blöcken. Am häufigsten werden Sie Geräte, die Datenblöcke verwenden, als Blockgeräte sehen, wie z.B. Festplatten, Dateisysteme usw.

### Pipe-Gerät (Pipe Device)

Benannte Pipes ermöglichen es zwei oder mehr Prozessen, miteinander zu kommunizieren. Diese ähneln Zeichenschnittstellengeräten, aber anstatt die Ausgabe an ein Gerät zu senden, wird sie an einen anderen Prozess gesendet.

### Socket-Gerät (Socket Device)

Socket-Geräte erleichtern die Kommunikation zwischen Prozessen, ähnlich wie Pipe-Geräte, aber sie können mit vielen Prozessen gleichzeitig kommunizieren.

### Gerätecharakterisierung

Geräte werden anhand von zwei Zahlen charakterisiert: **Major Device Number** und **Minor Device Number**. Sie können diese Zahlen im obigen `ls`-Beispiel sehen; sie sind durch ein Komma getrennt. Nehmen wir zum Beispiel an, ein Gerät hätte die Gerätenummern: **8, 0**:

Die Major Device Number repräsentiert den verwendeten Gerätetreiber, in diesem Fall 8, was oft die Major Number für sd-Blockgeräte ist. Die Minor Number teilt dem Kernel mit, welches eindeutige Gerät es in dieser Treiberklasse ist; in diesem Fall wird 0 verwendet, um das erste Gerät (a) darzustellen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Gerätedateien und deren Verwaltung zu vertiefen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Üben Sie das Erstellen und Verwalten von Festplattenpartitionen und Dateisystemen, die grundlegende Blockgeräte in Linux sind.
2. **[Hardwaregeräte in Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** – Lernen Sie, verschiedene Hardwaregeräte zu identifizieren und zu inspizieren und zu verstehen, wie sie im Verzeichnis `/dev` dargestellt werden.
3. **[Eine Swap-Datei in Linux erstellen und aktivieren](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** – Sammeln Sie praktische Erfahrungen beim Erstellen und Aktivieren einer Swap-Datei, die als virtuelles Speichergerät fungiert.

Diese Labs helfen Ihnen, die Konzepte der Geräteinteraktion und -verwaltung in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Was ist das Symbol für Zeichenschnittstellengeräte im Befehl `ls -l`?

## Quiz Answer

c
