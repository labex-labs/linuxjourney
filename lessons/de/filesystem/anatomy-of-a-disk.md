---
index: 3
lang: "de"
title: "Anatomie einer Festplatte"
meta_title: "Anatomie einer Festplatte - Das Dateisystem"
meta_description: "Erkunden Sie die Anatomie einer Festplatte unter Linux. Dieser Leitfaden erklärt, welche Komponente einer Festplatte dem Betriebssystem mitteilt, wie die Festplatte partitioniert ist, und behandelt MBR- und GPT-Partitionstabellen, verschiedene Arten von Linux-Partitionen und deren Organisation."
meta_keywords: "Festplatte in Linux, Linux-Partitionen, Arten von Linux-Partitionen, was teilt dem Betriebssystem mit, wie die Festplatte partitioniert ist, was enthält Informationen zur Organisation von Festplattenpartitionen, MBR, GPT, Partitionstabelle, Dateisystem"
---

## Lesson Content

Eine Festplatte in Linux kann in Partitionen unterteilt werden, die als einzelne Blockgeräte fungieren. Sie erinnern sich vielleicht an Beispiele wie /dev/sda1 und /dev/sda2. Hierbei steht /dev/sda für die gesamte Festplatte, während /dev/sda1 die erste Partition auf dieser Festplatte ist. Partitionen sind unglaublich nützlich, um Daten zu trennen. Wenn Sie für einen Teil Ihres Speichers ein bestimmtes Dateisystem benötigen, können Sie eine neue Partition dafür erstellen, anstatt die gesamte Festplatte zu formatieren.

### Die Partitionstabelle

Welcher Bestandteil einer Festplatte teilt dem Betriebssystem mit, wie die Festplatte partitioniert ist? Die Antwort ist die **Partitionstabelle**. Diese entscheidende Komponente enthält Informationen darüber, wie Festplattenpartitionen organisiert sind. Die Partitionstabelle legt fest, wo jede Partition beginnt und endet, welche Partitionen bootfähig sind und welche Sektoren der Festplatte jeder Partition zugewiesen sind. Es gibt zwei primäre Partitionstabellenschemata: Master Boot Record (MBR) und GUID Partition Table (GPT).

### Linux-Partitionen verstehen

Festplatten bestehen aus Partitionen, die uns helfen, unsere Daten zu organisieren. Sie können mehrere Partitionen auf einer einzigen Festplatte haben, aber sie dürfen sich nicht überlappen. Jeder Speicherplatz auf der Festplatte, der keiner Partition zugewiesen ist, wird als freier Speicherplatz bezeichnet. Die verfügbaren Arten von Linux-Partitionen hängen vom verwendeten Partitionstabellenschema ab. Innerhalb einer Partition können Sie ein Dateisystem erstellen oder sie für andere Zwecke widmen, wie z. B. Swap-Speicher.

### MBR-Partitionen

Der Master Boot Record (MBR) ist der traditionelle Standard für Partitionstabellen.

- Er unterstützt primäre, erweiterte und logische Partitionen.
- MBR hat eine Begrenzung auf vier primäre Partitionen.
- Um mehr Partitionen zu erstellen, muss eine primäre Partition als erweiterte Partition ausgewiesen werden (pro Festplatte ist nur eine erlaubt). Innerhalb dieser erweiterten Partition können Sie mehrere logische Partitionen erstellen, die wie jede andere Partition funktionieren.
- Er unterstützt Festplatten bis zu einer Größe von 2 Terabyte.

### GPT-Partitionen

Die GUID Partition Table (GPT) ist der moderne Standard für die Festplattenpartitionierung.

- Sie hat nur einen Partitionstyp, und Sie können eine große Anzahl davon erstellen.
- Jede Partition erhält eine Globally Unique Identifier (GUID).
- GPT wird häufig mit UEFI-basierten Boot-Systemen verwendet.

### Dateisystemstruktur

Wie wir bereits gelernt haben, ist ein Dateisystem eine organisierte Sammlung von Dateien und Verzeichnissen. Im Kern besteht es aus einer Datenbank zur Verwaltung von Dateien und den Dateien selbst. Lassen Sie uns seine Struktur genauer untersuchen.

- **Boot-Block**: Dieser Block befindet sich in den ersten Sektoren eines Dateisystems und wird vom Dateisystem selbst nicht verwendet. Stattdessen enthält er Informationen, die zum Booten des Betriebssystems verwendet werden. Es wird nur ein Boot-Block pro Betriebssystem benötigt. Obwohl andere Partitionen Boot-Blöcke haben können, bleiben diese oft ungenutzt.
- **Superblock**: Dies ist ein einzelner Block nach dem Boot-Block, der Metadaten über das Dateisystem enthält, wie z. B. die Größe der Inode-Tabelle, die Größe der logischen Blöcke und die Gesamtgröße des Dateisystems.
- **Inode-Tabelle**: Dies ist die Datenbank, die Dateien und Verzeichnisse verwaltet. Jede Datei oder jedes Verzeichnis hat einen eindeutigen Eintrag in der Inode-Tabelle, der verschiedene Attribute darüber speichert. Wir werden Inodes in einer speziellen Lektion behandeln.
- **Datenblöcke**: Hier wird der eigentliche Inhalt Ihrer Dateien und Verzeichnisse gespeichert.

Unten sehen Sie ein Beispiel für eine Festplatte, die die MBR-Partitionstabelle verwendet (als `msdos` bezeichnet). Sie können die primären, erweiterten und logischen Partitionen sehen.

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

Dieses zweite Beispiel zeigt eine GPT-Partitionstabelle, die eindeutige IDs für ihre Partitionen verwendet.

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

Um Ihr Verständnis von Festplattenpartitionierung und Dateisystemen zu festigen, empfehlen wir dieses praktische Labor:

1.  **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Üben Sie das Erstellen neuer Partitionen, deren Formatierung mit Dateisystemen wie ext4, deren Einhängen und die Konfiguration des persistenten Einhängens in `/etc/fstab`.

Dieses Labor hilft Ihnen, Konzepte des Speichermanagements in realen Szenarien anzuwenden und Selbstvertrauen im Umgang mit Linux-Speicher aufzubauen.

## Quiz Question

Welcher Partitionstyp wird verwendet, um mehr als 4 Partitionen im MBR-Partitionierungsschema zu erstellen? (Bitte antworten Sie in einem einzigen kleingeschriebenen englischen Wort.)

## Quiz Answer

extended
