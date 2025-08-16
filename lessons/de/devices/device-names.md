---
lang: "de"
title: "Gerätenamen"
description: "Lernen Sie Linux-Gerätenamen wie SCSI- (sd), Pseudo- und PATA-Geräte (hd) kennen. Verstehen Sie /dev/sda, /dev/null und mehr in diesem anfängerfreundlichen Leitfaden."
keywords: "Linux-Gerätenamen, /dev, SCSI-Geräte, Pseudo-Geräte, PATA-Geräte, Linux-Tutorial, Linux für Anfänger, Gerätedateien"
---

## Lesson Content

Hier sind die gängigsten Gerätenamen, denen Sie begegnen werden:

### SCSI Devices

Wenn Sie Massenspeicher auf Ihrem Computer haben, ist die Wahrscheinlichkeit groß, dass dieser das SCSI-Protokoll (ausgesprochen „scuzzy“) verwendet. SCSI steht für Small Computer System Interface; es ist ein Protokoll, das die Kommunikation zwischen Festplatten, Druckern, Scannern und anderen Peripheriegeräten und Ihrem System ermöglicht. Sie haben vielleicht von SCSI-Geräten gehört, die in modernen Systemen eigentlich nicht mehr verwendet werden; unsere Linux-Systeme ordnen SCSI-Festplatten jedoch den Festplattenlaufwerken in `/dev` zu. Sie werden durch ein Präfix von `sd` (SCSI disk) dargestellt:

Gängige SCSI-Gerätedateien:

- `/dev/sda` - Erste Festplatte
- `/dev/sdb` - Zweite Festplatte
- `/dev/sda3` - Dritte Partition auf der ersten Festplatte

### Pseudo Devices

Wie bereits erwähnt, sind Pseudo-Geräte nicht wirklich physisch mit Ihrem System verbunden. Die meisten gängigen Pseudo-Geräte sind Zeichengeräte:

- `/dev/zero` - akzeptiert und verwirft alle Eingaben, erzeugt einen kontinuierlichen Strom von NULL (Nullwert) Bytes
- `/dev/null` - akzeptiert und verwirft alle Eingaben, erzeugt keine Ausgabe
- `/dev/random` - erzeugt Zufallszahlen

### PATA Devices

Manchmal, in älteren Systemen, können Sie Festplatten mit einem `hd`-Präfix sehen:

- `/dev/hda` - Erste Festplatte
- `/dev/hdd2` - Zweite Partition auf der 4. Festplatte

## Exercise

Schreiben Sie auf die Pseudo-Geräte und sehen Sie, was passiert. Seien Sie vorsichtig, Ihre Festplatten nicht auf diese Geräte zu schreiben!

## Quiz Question

Wie würde der Gerätename für die erste Partition auf der zweiten SCSI-Festplatte üblicherweise lauten?

## Quiz Answer

sdb1
