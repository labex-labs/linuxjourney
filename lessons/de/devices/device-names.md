---
index: 3
lang: "de"
title: "Gerätenamen"
meta_title: "Gerätenamen - Geräte"
meta_description: "Lernen Sie Linux-Gerätenamen wie SCSI (sd), Pseudo- und PATA (hd)-Geräte kennen. Verstehen Sie /dev/sda, /dev/null und mehr in diesem anfängerfreundlichen Leitfaden."
meta_keywords: "Linux-Gerätenamen, /dev, SCSI-Geräte, Pseudo-Geräte, PATA-Geräte, Linux-Tutorial, Linux für Anfänger, Gerätedateien"
---

## Lesson Content

Hier sind die gängigsten Gerätenamen, denen Sie begegnen werden:

### SCSI-Geräte

Wenn Sie Massenspeicher auf Ihrem Computer haben, ist die Wahrscheinlichkeit groß, dass dieser das SCSI-Protokoll (ausgesprochen "scuzzy") verwendet. SCSI steht für Small Computer System Interface; es ist ein Protokoll, das die Kommunikation zwischen Festplatten, Druckern, Scannern und anderen Peripheriegeräten und Ihrem System ermöglicht. Sie haben vielleicht von SCSI-Geräten gehört, die in modernen Systemen eigentlich nicht mehr verwendet werden; unsere Linux-Systeme ordnen jedoch SCSI-Festplatten den Festplattenlaufwerken in `/dev` zu. Sie werden durch das Präfix `sd` (SCSI-Disk) dargestellt:

Gängige SCSI-Gerätedateien:

- `/dev/sda` – Erste Festplatte
- `/dev/sdb` – Zweite Festplatte
- `/dev/sda3` – Dritte Partition auf der ersten Festplatte

### Pseudo-Geräte

Wie bereits erwähnt, sind Pseudo-Geräte nicht wirklich physisch mit Ihrem System verbunden. Die gängigsten Pseudo-Geräte sind Zeichengeräte:

- `/dev/zero` – akzeptiert und verwirft alle Eingaben, erzeugt einen kontinuierlichen Strom von NULL (Nullwert) Bytes
- `/dev/null` – akzeptiert und verwirft alle Eingaben, erzeugt keine Ausgabe
- `/dev/random` – erzeugt Zufallszahlen

### PATA-Geräte

Manchmal, in älteren Systemen, können Festplatten mit einem `hd`-Präfix bezeichnet werden:

- `/dev/hda` – Erste Festplatte
- `/dev/hdd2` – Zweite Partition auf der 4. Festplatte

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Gerätenamen und Speicherverwaltung zu vertiefen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Üben Sie das Erstellen, Formatieren und Mounten von Partitionen, was direkt die Arbeit mit Gerätenamen beinhaltet.
2. **[Hardware-Geräte in Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** – Lernen Sie, verschiedene Hardware-Geräte und ihre zugehörigen Namen in einer Linux-Umgebung zu identifizieren und zu inspizieren.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Speicher und das Verständnis von Hardware in Linux aufzubauen.

## Quiz Question

Wie würde der Gerätename für die erste Partition auf der zweiten SCSI-Festplatte üblicherweise lauten?

## Quiz Answer

sdb1
