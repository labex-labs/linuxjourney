---
index: 2
lang: "de"
title: "Dateisystemtypen"
meta_title: "Dateisystemtypen - Das Dateisystem"
meta_description: "Entdecken Sie die verschiedenen Linux-Dateisystemtypen, einschließlich ext4, Btrfs und XFS. Dieser Leitfaden erklärt Schlüsselkonzepte wie Journaling und das Virtual File System (VFS) und hilft Ihnen, die verschiedenen für Linux verfügbaren Dateisystemtypen zu verstehen."
meta_keywords: "linux dateisystemtypen, dateisystemtypen, ext4, Btrfs, XFS, journaling, VFS, linux tutorial"
---

## Lesson Content

Linux unterstützt eine Vielzahl von Dateisystemimplementierungen. Einige sind auf Geschwindigkeit optimiert, andere auf große Speicherkapazität, und einige sind für kleinere Geräte konzipiert. Jeder dieser verschiedenen Dateisystemtypen hat eine einzigartige Methode zur Organisation von Daten.

### Die Rolle des Virtuellen Dateisystems

Angesichts der vielen verfügbaren Implementierungen benötigen Anwendungen eine konsistente Möglichkeit, mit ihnen zu interagieren. Hier kommt das Virtuelle Dateisystem (VFS) ins Spiel. Das VFS ist eine Abstraktionsschicht im Linux-Kernel, die zwischen Anwendungen und den verschiedenen Dateisystemen sitzt. Es bietet eine einzige, einheitliche Schnittstelle und stellt sicher, dass Anwendungen nahtlos arbeiten können, unabhängig vom zugrunde liegenden Dateisystemtyp. Diese Flexibilität ermöglicht es Ihnen, mehrere Dateisysteme auf Ihren Festplatten zu haben, die oft durch Partitionen organisiert sind, was wir in einer zukünftigen Lektion behandeln werden.

### Journaling für Datenintegrität

Die meisten modernen Dateisystemtypen beinhalten standardmäßig eine Funktion namens Journaling (oder Protokollierung). Um seine Bedeutung zu verstehen, stellen Sie sich vor, Sie kopieren eine große Datei, während Ihr Computer plötzlich den Strom verliert. Bei einem nicht-journaled Dateisystem könnte diese Unterbrechung zu einer beschädigten Datei und einem inkonsistenten Dateisystemzustand führen. Nach dem Neustart müsste Ihr System eine vollständige Dateisystemprüfung (fsck) durchführen, was bei großen Festplatten zeitaufwendig sein kann.

A journaled Dateisystem verhindert dieses Problem. Bevor eine Schreiboperation durchgeführt wird, zeichnet es die beabsichtigten Änderungen zuerst in einer speziellen Protokolldatei, dem „Journal“, auf. Sobald die Operation erfolgreich abgeschlossen ist, wird das Journal aktualisiert, um die Aufgabe als beendet zu markieren. Wenn ein Absturz auftritt, kann das System beim Neustart einfach das Journal lesen, um zu sehen, welche Operationen gerade liefen, und das Dateisystem schnell wieder in einen konsistenten Zustand versetzen. Dies reduziert die Wiederherstellungszeit drastisch und schützt vor Datenkorruption.

### Gängige Linux-Dateisystemtypen

Hier sind einige der gängigsten **linux file system types** (Linux-Dateisystemtypen), denen Sie begegnen werden:

- **ext4** – Als neueste Version des nativen Linux Extended Filesystems ist ext4 der Standard für viele Distributionen. Es ist abwärtskompatibel mit seinen Vorgängern (ext2/ext3) und unterstützt sehr große Festplattenvolumen (bis zu 1 Exabyte) und Dateigrößen (bis zu 16 Terabyte). Es ist eine zuverlässige und Standardwahl für die meisten Anwendungsfälle.
- **Btrfs** – Oft als „B-tree FS“ bezeichnet, ist Btrfs ein modernes Dateisystem mit erweiterten Funktionen wie integrierten Snapshots, inkrementellen Backups und verbesserter Leistung. Obwohl es mittlerweile als stabil gilt und in einigen Distributionen Standard ist, befindet es sich noch in aktiver Entwicklung.
- **XFS** – Ein hochleistungsfähiges Journaling-Dateisystem, das sich durch die Handhabung großer Dateien und paralleler E/A-Operationen auszeichnet. Dies macht es zu einer ausgezeichneten Wahl für Systeme, die große Datenmengen verwalten, wie z. B. Medienserver.
- **NTFS und FAT** – Dies sind Standard-Windows-Dateisystemtypen. Linux bietet volle Unterstützung für das Lesen und Schreiben darauf, was für Dual-Boot-Systeme nützlich ist.
- **HFS+** – Das primäre Dateisystem, das von macOS verwendet wird. Linux hat standardmäßig nur Lesezugriff darauf, wobei Schreibzugriff über zusätzliche Tools möglich ist.

You can see which filesystems are in use on your machine with the `df` command:

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

The `df` command reports file system disk space usage. The `-T` flag specifically shows the filesystem type. We will explore this tool in more detail later.

## Exercise

Um Ihr Wissen in die Praxis umzusetzen, absolvieren Sie das folgende praktische Labor. Es wird Ihnen helfen, Ihr Verständnis von Linux-Dateisystemen und Partitionen zu festigen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – In diesem Labor üben Sie das Erstellen einer neuen Partition, das Formatieren mit einem bestimmten Dateisystemtyp, das Einhängen und die Konfiguration für das dauerhafte Einhängen. Dies sind grundlegende Fähigkeiten für die Verwaltung von Speicher unter Linux.

Dieses Labor ermöglicht es Ihnen, diese Konzepte in einem realen Szenario anzuwenden und Selbstvertrauen im Umgang mit der Festplattenverwaltung aufzubauen.

## Quiz Question

What is the most common and default filesystem type for many Linux distributions? (Please answer in English, paying attention to case sensitivity)

## Quiz Answer

ext4
