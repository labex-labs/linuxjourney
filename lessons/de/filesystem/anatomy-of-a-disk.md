---
title: "Anatomie einer Festplatte"
description: "Erfahren Sie mehr über Linux-Festplattenpartitionierung, MBR vs. GPT und Dateisystemstruktur. Verstehen Sie Partitionen, Tabellen und wie Daten organisiert werden. Beginnen Sie mit diesem Leitfaden für Anfänger!"
keywords: "Linux-Festplattenpartitionierung, MBR, GPT, Dateisystemstruktur, Linux-Partitionen, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Festplatten können in Partitionen unterteilt werden, wodurch im Wesentlichen mehrere Blockgeräte entstehen. Erinnern Sie sich an Beispiele wie `/dev/sda1` und `/dev/sda2`. `/dev/sda` ist die gesamte Festplatte, aber `/dev/sda1` ist die erste Partition auf dieser Festplatte. Partitionen sind äußerst nützlich, um Daten zu trennen, und wenn Sie ein bestimmtes Dateisystem benötigen, können Sie einfach eine Partition erstellen, anstatt die gesamte Festplatte zu einem Dateisystemtyp zu machen.

### Partition Table

Jede Festplatte hat eine Partitionstabelle. Diese Tabelle teilt dem System mit, wie die Festplatte partitioniert ist. Diese Tabelle zeigt Ihnen, wo Partitionen beginnen und enden, welche Partitionen bootfähig sind, welche Sektoren der Festplatte welcher Partition zugewiesen sind usw. Es gibt zwei Hauptschemata für Partitionstabellen: Master Boot Record (MBR) und GUID Partition Table (GPT).

### Partition

Festplatten bestehen aus Partitionen, die uns helfen, unsere Daten zu organisieren. Sie können mehrere Partitionen auf einer Festplatte haben, und sie dürfen sich nicht überlappen. Wenn Speicherplatz nicht einer Partition zugewiesen ist, wird er als freier Speicherplatz bezeichnet. Die Arten von Partitionen hängen von Ihrer Partitionstabelle ab. Innerhalb einer Partition können Sie ein Dateisystem haben oder eine Partition für andere Dinge wie Swap widmen (dazu kommen wir bald).

_MBR_

- Traditionelle Partitionstabelle, wurde als Standard verwendet
- Kann primäre, erweiterte und logische Partitionen haben
- MBR hat eine Begrenzung von vier primären Partitionen
- Zusätzliche Partitionen können erstellt werden, indem eine primäre Partition in eine erweiterte Partition umgewandelt wird (es kann nur eine erweiterte Partition auf einer Festplatte geben). Dann fügen Sie innerhalb der erweiterten Partition logische Partitionen hinzu. Die logischen Partitionen werden genau wie jede andere Partition verwendet. Albern, ich weiß.
- Unterstützt Festplatten bis zu 2 Terabyte

_GPT_

- GUID Partition Table (GPT) wird zum neuen Standard für die Festplattenpartitionierung
- Hat nur einen Partitionstyp, und Sie können viele davon erstellen
- Jede Partition hat eine global eindeutige ID (GUID)
- Wird meist in Verbindung mit UEFI-basiertem Booten verwendet (Details dazu in einem anderen Kurs)

### Filesystem Structure

Wir wissen aus unserer vorherigen Lektion, dass ein Dateisystem eine organisierte Sammlung von Dateien und Verzeichnissen ist. In seiner einfachsten Form besteht es aus einer Datenbank zur Verwaltung von Dateien und den eigentlichen Dateien selbst; wir werden jedoch etwas detaillierter darauf eingehen.

- Boot block - Dieser befindet sich in den ersten Sektoren des Dateisystems und wird vom Dateisystem nicht wirklich verwendet. Vielmehr enthält er Informationen, die zum Booten des Betriebssystems verwendet werden. Das Betriebssystem benötigt nur einen Boot block. Wenn Sie mehrere Partitionen haben, werden diese Boot blocks haben, aber viele davon sind ungenutzt.
- Super block - Dies ist ein einzelner Block, der nach dem Boot block kommt, und er enthält Informationen über das Dateisystem, wie die Größe der Inode table, die Größe der logical blocks und die Größe des Dateisystems.
- Inode table - Stellen Sie sich dies als die Datenbank vor, die unsere Dateien verwaltet (wir haben eine ganze Lektion über Inodes, also keine Sorge). Jede Datei oder jedes Verzeichnis hat einen eindeutigen Eintrag in der Inode table, und es enthält verschiedene Informationen über die Datei.
- Data blocks - Dies sind die eigentlichen Daten für die Dateien und Verzeichnisse.

Werfen wir einen Blick auf die verschiedenen Partitionstabellen. Unten ist ein Beispiel einer Partition, die die MBR-Partitionstabelle (msdos) verwendet. Sie können die primären, erweiterten und logischen Partitionen auf der Maschine sehen.

```plaintext
pete@icebox:~$ sudo parted -l
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

Dieses Beispiel ist GPT, das nur eine eindeutige ID für die Partitionen verwendet.

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

Run **parted -l** on your machine and evaluate your results.

## Quiz Question

Welcher Partitionstyp wird verwendet, um mehr als 4 Partitionen im MBR-Partitionierungsschema zu erstellen?

## Quiz Answer

extended
