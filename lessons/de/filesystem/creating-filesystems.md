---
index: 5
lang: "de"
title: "Dateisysteme erstellen"
meta_title: "Dateisysteme erstellen - Das Dateisystem"
meta_description: "Erfahren Sie, wie Sie Dateisysteme unter Linux mit mkfs erstellen. Dieser anfängerfreundliche Leitfaden behandelt ext4 und die Festplattenpartitionierung. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "mkfs, Dateisystem erstellen, ext4, Linux-Partitionierung, Linux-Tutorial, Linux für Anfänger, Festplattenverwaltung, Linux-Anleitung"
---

## Lesson Content

Nachdem Sie nun eine Festplatte partitioniert haben, erstellen wir ein Dateisystem!

```bash
sudo mkfs -t ext4 /dev/sdb2
```

So einfach ist das! Das Tool **mkfs** (make filesystem) ermöglicht es uns, den gewünschten Dateisystemtyp und den Speicherort anzugeben. Sie sollten ein Dateisystem nur auf einer neu partitionierten Festplatte erstellen oder wenn Sie eine alte neu partitionieren. Wenn Sie versuchen, ein Dateisystem über ein bestehendes zu erstellen, wird Ihr Dateisystem höchstwahrscheinlich in einem beschädigten Zustand zurückbleiben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Verwaltung von Linux-Dateisystemen zu vertiefen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – In diesem Lab lernen Sie, Festplattenpartitionen und Dateisysteme in Linux zu verwalten. Sie verwenden fdisk, um eine neue Partition zu erstellen, formatieren diese mit ext4 (mithilfe von `mkfs`), mounten sie, konfigurieren das persistente Mounten in /etc/fstab und erstellen eine Swap-Partition, alles auf einer sicheren sekundären virtuellen Festplatte.

Dieses Lab hilft Ihnen, die Konzepte der Erstellung und Verwaltung von Dateisystemen in realen Szenarien anzuwenden und Vertrauen in die Festplattenverwaltung unter Linux aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um ein Dateisystem zu erstellen?

## Quiz Answer

mkfs
