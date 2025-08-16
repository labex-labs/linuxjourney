---
lang: "de"
title: "Disk-Partitionierung"
description: "Lernen Sie die Disk-Partitionierung in Linux mit parted. Verstehen Sie, wie man Disks partitioniert, auswählt, anzeigt und in der Größe ändert. Beginnen Sie mit diesem anfängerfreundlichen Leitfaden!"
keywords: "Linux Disk-Partitionierung, parted Befehl, fdisk, gparted, Linux Tutorial, Linux für Anfänger, Disk-Management, Linux Leitfaden"
---

## Lesson Content

Lassen Sie uns praktische Dinge mit Dateisystemen tun, indem wir den Prozess auf einem USB-Laufwerk durcharbeiten. Wenn Sie keines haben, keine Sorge, Sie können trotzdem die nächsten paar Lektionen verfolgen.

Zuerst müssen wir unsere Disk partitionieren. Es gibt viele Tools, um dies zu tun:

- fdisk – grundlegendes Befehlszeilen-Partitionierungstool; es unterstützt kein GPT
- parted – dies ist ein Befehlszeilen-Tool, das sowohl MBR- als auch GPT-Partitionierung unterstützt
- gparted – dies ist die GUI-Version von parted
- gdisk – fdisk, aber es unterstützt kein MBR, nur GPT

Lassen Sie uns parted für unsere Partitionierung verwenden. Nehmen wir an, ich schließe das USB-Gerät an und wir sehen, dass der Gerätename /dev/sdb2 ist.

### Launch parted

```bash
sudo parted
```

Sie werden in das parted-Tool gelangen; hier können Sie Befehle ausführen, um Ihr Gerät zu partitionieren.

### Select the device

```bash
select /dev/sdb2
```

Um das Gerät auszuwählen, mit dem Sie arbeiten möchten, wählen Sie es anhand seines Gerätenamens aus.

### View current partition table

```plaintext
(parted) print
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

Hier sehen Sie die verfügbaren Partitionen auf dem Gerät. Die **start**- und **end**-Punkte sind die Stellen, an denen die Partitionen Speicherplatz auf der Festplatte belegen; Sie sollten eine gute Start- und Endposition für Ihre Partitionen finden.

### Partition the device

```bash
mkpart primary 123 4567
```

Wählen Sie nun einfach einen Start- und Endpunkt und erstellen Sie die Partition; Sie müssen den Partitionstyp angeben, abhängig von der verwendeten Tabelle.

### Resize a partition

Sie können eine Partition auch in der Größe ändern, wenn Sie keinen Platz haben.

```bash
resize 2 1245 3456
```

Wählen Sie die Partitionsnummer und dann die Start- und Endpunkte, auf die Sie sie ändern möchten.

Parted ist ein sehr mächtiges Tool, und Sie sollten vorsichtig sein, wenn Sie Ihre Disks partitionieren.

## Exercise

Partitionieren Sie ein USB-Laufwerk, wobei die Hälfte des Laufwerks als ext4 und die andere Hälfte als freier Speicherplatz dient.

## Quiz Question

Was ist der parted-Befehl, um eine Partition zu erstellen?

## Quiz Answer

mkpart
