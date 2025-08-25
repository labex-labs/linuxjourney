---
index: 4
lang: "de"
title: "Festplattenpartitionierung"
meta_title: "Festplattenpartitionierung - Das Dateisystem"
meta_description: "Lernen Sie die Festplattenpartitionierung in Linux mit parted. Verstehen Sie, wie man Festplatten partitioniert, auswählt, anzeigt und in der Größe ändert. Beginnen Sie mit diesem anfängerfreundlichen Leitfaden!"
meta_keywords: "Linux Festplattenpartitionierung, parted Befehl, fdisk, gparted, Linux Tutorial, Linux für Anfänger, Festplattenverwaltung, Linux Leitfaden"
---

## Lesson Content

Lassen Sie uns etwas Praktisches mit Dateisystemen tun, indem wir den Prozess auf einem USB-Laufwerk durcharbeiten. Wenn Sie keines haben, keine Sorge, Sie können die nächsten paar Lektionen trotzdem verfolgen.

Zuerst müssen wir unsere Festplatte partitionieren. Es gibt viele Tools, um dies zu tun:

- fdisk - grundlegendes Befehlszeilen-Partitionierungstool; es unterstützt kein GPT
- parted - dies ist ein Befehlszeilen-Tool, das sowohl MBR- als auch GPT-Partitionierung unterstützt
- gparted - dies ist die GUI-Version von parted
- gdisk - fdisk, aber es unterstützt kein MBR, nur GPT

Verwenden wir parted für unsere Partitionierung. Nehmen wir an, ich schließe das USB-Gerät an und wir sehen, dass der Gerätename /dev/sdb2 ist.

### parted starten

```bash
sudo parted
```

Sie werden in das parted-Tool gelangen; hier können Sie Befehle ausführen, um Ihr Gerät zu partitionieren.

### Gerät auswählen

```bash
select /dev/sdb2
```

Um das Gerät auszuwählen, mit dem Sie arbeiten möchten, wählen Sie es anhand seines Gerätenamens aus.

### Aktuelle Partitionstabelle anzeigen

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

Hier sehen Sie die verfügbaren Partitionen auf dem Gerät. Die **Start-** und **Endpunkte** sind die Stellen, an denen die Partitionen Speicherplatz auf der Festplatte belegen; Sie sollten einen guten Start- und Endpunkt für Ihre Partitionen finden.

### Gerät partitionieren

```bash
mkpart primary 123 4567
```

Wählen Sie nun einfach einen Start- und Endpunkt und erstellen Sie die Partition; Sie müssen den Partitionstyp angeben, je nachdem, welche Tabelle Sie verwendet haben.

### Eine Partition in der Größe ändern

Sie können eine Partition auch in der Größe ändern, wenn Sie keinen Platz haben.

```bash
resize 2 1245 3456
```

Wählen Sie die Partitionsnummer und dann die Start- und Endpunkte, auf die Sie sie in der Größe ändern möchten.

Parted ist ein sehr mächtiges Tool, und Sie sollten vorsichtig sein, wenn Sie Ihre Festplatten partitionieren.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Festplattenpartitionierung und Dateisystemverwaltung zu vertiefen:

1. [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845) – In diesem Lab lernen Sie, Festplattenpartitionen und Dateisysteme in Linux zu verwalten. Sie verwenden fdisk, um eine neue Partition zu erstellen, sie mit ext4 zu formatieren, sie zu mounten, die persistente Einhängung in /etc/fstab zu konfigurieren und eine Swap-Partition zu erstellen, alles auf einer sicheren sekundären virtuellen Festplatte.

Dieses Lab hilft Ihnen, die Konzepte der Festplattenpartitionierung und Dateisystemverwaltung in einem realen Szenario anzuwenden und Vertrauen in diese wesentlichen Linux-Administrationsfähigkeiten aufzubauen.

## Quiz Question

Was ist der parted-Befehl, um eine Partition zu erstellen?

## Quiz Answer

mkpart
