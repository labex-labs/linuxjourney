---
index: 6
lang: "de"
title: "mount und umount"
meta_title: "mount und umount - Das Dateisystem"
meta_description: "Erfahren Sie, wie Sie die Linux-Befehle mount und umount verwenden, um Dateisysteme zu verwalten. Verstehen Sie das Mounten und Unmounten von Geräten sowie UUIDs für Anfänger."
meta_keywords: "Linux mount, umount Befehl, Dateisystem mounten, Linux UUID, Linux für Anfänger, Linux Tutorial, Mountpoint, Linux Anleitung"
---

## Lesson Content

Bevor Sie den Inhalt Ihres Dateisystems anzeigen können, müssen Sie es mounten. Dazu benötige ich den Gerätestandort, den Dateisystemtyp und einen Mountpoint. Der Mountpoint ist ein Verzeichnis auf dem System, an das das Dateisystem angehängt wird. Wir möchten also unser Gerät im Grunde an einen Mountpoint mounten.

Erstellen Sie zuerst den Mountpoint; in unserem Fall **mkdir /mydrive**.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

So einfach ist das! Wenn wir jetzt zu /mydrive gehen, können wir den Inhalt unseres Dateisystems sehen. Das **-t** gibt den Typ des Dateisystems an, dann haben wir den Gerätestandort und dann den Mountpoint.

Um ein Gerät von einem Mountpoint zu unmounten:

```bash
sudo umount /mydrive
```

oder

```bash
sudo umount /dev/sdb2
```

Denken Sie daran, dass der Kernel Geräte in der Reihenfolge benennt, in der er sie findet. Was, wenn sich unser Gerätename aus irgendeinem Grund ändert, nachdem wir ihn gemountet haben? Nun, glücklicherweise können Sie stattdessen die universell eindeutige ID (UUID) eines Geräts verwenden.

Um die UUIDs auf Ihrem System für Blockgeräte anzuzeigen:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Wir können unsere Gerätenamen, ihre entsprechenden Dateisystemtypen und ihre UUIDs sehen. Wenn wir nun etwas mounten möchten, können wir Folgendes verwenden:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Meistens müssen Sie Geräte nicht über ihre UUIDs mounten; es ist viel einfacher, den Gerätenamen zu verwenden, und oft weiß das Betriebssystem, wie gängige Geräte wie USB-Laufwerke gemountet werden. Wenn Sie jedoch ein Dateisystem beim Start automatisch mounten müssen, z. B. wenn Sie eine sekundäre Festplatte hinzugefügt haben, sollten Sie die UUID verwenden, und das werden wir in der nächsten Lektion behandeln.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis der Verwaltung von Linux-Dateisystemen zu vertiefen:

- **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – In diesem Labor lernen Sie, Festplattenpartitionen und Dateisysteme in Linux zu verwalten. Sie verwenden fdisk, um eine neue Partition zu erstellen, sie mit ext4 zu formatieren, sie zu mounten, die persistente Einbindung in /etc/fstab zu konfigurieren und eine Swap-Partition zu erstellen, alles auf einer sicheren sekundären virtuellen Festplatte.

Dieses Labor wird Ihnen helfen, die Konzepte des Mountens und Unmountens in realen Szenarien anzuwenden und Vertrauen in die Dateisystemverwaltung aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um ein Dateisystem anzuhängen?

## Quiz Answer

mount
