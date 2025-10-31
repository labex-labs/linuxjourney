---
index: 4
lang: "de"
title: "Festplattenpartitionierung"
meta_title: "Festplattenpartitionierung - Das Dateisystem"
meta_description: "Erfahren Sie mehr über die Linux-Festplattenpartitionierung mit dem parted-Befehl. Diese Anleitung behandelt, wie Sie Partitionen mit `sudo parted -l` anzeigen, erstellen und deren Größe ändern. Stellt auch gparted vor, eine beliebte grafische Alternative."
meta_keywords: "Linux Festplattenpartitionierung, parted Befehl, sudo parted -l, gparted, gparted Windows Alternative, fdisk, Festplattenverwaltung, Partition erstellen, Partition Größe ändern, Linux Anleitung"
---

## Lesson Content

Diese Lektion bietet eine praktische Anleitung zur Verwaltung von Dateisystemen durch Partitionierung einer Festplatte, z. B. eines USB-Sticks. Wenn Sie keine zusätzliche Festplatte haben, können Sie die Schritte trotzdem nachvollziehen, um die Konzepte zu verstehen.

Zuerst müssen wir unsere Festplatte partitionieren. Für diese Aufgabe stehen viele Werkzeuge zur Verfügung:

- **fdisk**: Ein grundlegendes Befehlszeilen-Partitionierungswerkzeug; es unterstützt kein GPT.
- **parted**: Ein leistungsstarkes Befehlszeilenwerkzeug, das sowohl MBR- als auch GPT-Partitionierung unterstützt.
- **gparted**: Die grafische Version von `parted`. Für Benutzer, die eine visuelle Oberfläche bevorzugen, ist `gparted` ein intuitives Werkzeug und wird oft als großartige `gparted windows alternative` angesehen.
- **gdisk**: Ähnlich wie `fdisk`, unterstützt es jedoch nur GPT.

Wir werden `parted` für unsere Beispiele verwenden.

### Auflisten vorhandener Partitionen

Bevor Sie Änderungen vornehmen, ist es entscheidend, Ihre Festplatte und deren aktuellen Aufbau zu identifizieren. Eine schnelle Methode hierfür ist der Befehl `sudo parted -l`, der die Partitionstabellen aller angeschlossenen Blockgeräte auflistet.

```bash
sudo parted -l
```

Dieser Befehl hilft Ihnen, den korrekten Gerätenamen, wie z. B. `/dev/sdb`, zu finden, bevor Sie mit der Änderung beginnen.

### Starten des interaktiven Modus

Um Änderungen vorzunehmen, starten Sie `parted` im interaktiven Modus. Nehmen wir an, Ihr Zielgerät ist `/dev/sdb`.

```bash
sudo parted
```

Sie gelangen in die Shell des `parted`-Tools, wo Sie Befehle zur Verwaltung der Partitionen Ihres Geräts ausführen können.

### Auswahl eines Geräts

Sobald Sie sich in der `parted`-Shell befinden, müssen Sie die zu ändernde Festplatte auswählen. Seien Sie sehr vorsichtig bei der Auswahl, um Datenverlust zu vermeiden.

```bash
select /dev/sdb
```

### Anzeigen der Partitionstabelle

Verwenden Sie den Befehl `print`, um die Partitionstabelle der ausgewählten Festplatte anzuzeigen.

```plaintext
(parted) print
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 10.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type      File system  Flags
 1      1049kB  10.7GB  10.7GB  primary   ext4         boot
```

Diese Ausgabe zeigt die verfügbaren Partitionen auf dem Gerät. Die Spalten **Start** und **End** geben an, wo sich jede Partition auf der Festplatte befindet.

### Erstellen einer Partition

Der Befehl `mkpart` erstellt eine neue Partition. Sie müssen den Partitionstyp (z. B. `primary`), einen optionalen Dateisystemtyp sowie die Start- und Endpunkte angeben.

```bash
mkpart primary ext4 1MB 5000MB
```

Dieser Befehl erstellt eine primäre Partition, formatiert mit ext4, die bei 1MB beginnt und bei 5000MB endet.

### Ändern der Größe einer Partition

Sie können auch die Größe einer vorhandenen Partition mit dem Befehl `resize` ändern. Sie benötigen die Partitionsnummer sowie die neuen Start- und Endpunkte.

```bash
resize 1 1MB 8000MB
```

Dieser Befehl ändert die Größe der Partition Nummer 1, sodass sie bei der 8000MB-Marke endet.

`parted` ist ein sehr mächtiges Werkzeug. Überprüfen Sie Ihre Befehle immer zweimal, bevor Sie sie ausführen, um versehentlichen Datenverlust zu vermeiden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Festplattenpartitionierung und Dateisystemverwaltung zu festigen:

1. [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845) - In diesem Lab lernen Sie, Festplattenpartitionen und Dateisysteme unter Linux zu verwalten. Sie verwenden fdisk, um eine neue Partition zu erstellen, diese mit ext4 zu formatieren, sie einzubinden, die dauerhafte Einhängung in /etc/fstab zu konfigurieren und eine Swap-Partition zu erstellen – alles auf einer sicheren sekundären virtuellen Festplatte.

Dieses Lab hilft Ihnen, die Konzepte der Festplattenpartitionierung und Dateisystemverwaltung in einem realen Szenario anzuwenden und Vertrauen in diese wesentlichen Linux-Administrationsfähigkeiten aufzubauen.

## Quiz Question

Was ist der `parted`-Befehl, um eine Partition zu erstellen? (Bitte antworten Sie auf Englisch und achten Sie auf die Groß- und Kleinschreibung).

## Quiz Answer

mkpart
