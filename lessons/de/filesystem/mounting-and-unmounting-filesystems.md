---
index: 6
lang: "de"
title: "mount und umount"
meta_title: "mount und umount - Das Dateisystem"
meta_description: "Erfahren Sie, wie Sie die Befehle mount und umount unter Linux verwenden, um Dateisysteme anzuhängen und zu trennen. Diese Anleitung behandelt das Einhängen von Geräten, den sudo umount-Prozess für ein sicheres Linux-Aushängen und die Verwendung von UUIDs."
meta_keywords: "mount, umount, sudo umount, umount linux, linux aushängen, debian umount, dateisystem mounten, gerät aushängen, Linux UUID, mount point"
---

## Lesson Content

Bevor Sie auf die Dateien auf einem Speichergerät zugreifen können, müssen Sie dessen Dateisystem zuerst auf ein Verzeichnis Ihres Systems einbinden (mounten). Dieser Vorgang beinhaltet den Speicherort des Geräts, den Dateisystemtyp und einen Einhängepunkt (Mount Point). Der Einhängepunkt ist einfach ein vorhandenes Verzeichnis, an das das Dateisystem angehängt wird.

### Ein Dateisystem einbinden (mounten)

Zuerst müssen Sie einen Einhängepunkt erstellen. Erstellen wir ein Verzeichnis für diesen Zweck:

```bash
sudo mkdir /mydrive
```

Sobald der Einhängepunkt bereit ist, können Sie den Befehl `mount` verwenden, um Ihr Gerät anzuhängen. Die Option `-t` gibt den Dateisystemtyp an.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

So einfach ist das! Wenn Sie nun in das Verzeichnis `/mydrive` navigieren, sehen Sie den Inhalt des Dateisystems Ihres Geräts.

### Ein Dateisystem unter Linux aushängen (unmounten)

Wenn Sie mit einem Gerät fertig sind, sollten Sie es aushängen (unmounten), um sicherzustellen, dass alle Daten sicher geschrieben und das Dateisystem sauber getrennt wird. Der Standardbefehl für diesen Vorgang unter Linux ist `umount`. Um ein `linux unmount` durchzuführen, können Sie entweder den Einhängepunkt oder den Gerätenamen angeben.

Verwendung des Einhängepunkts:

```bash
sudo umount /mydrive
```

Alternativ die Verwendung des Gerätenamens:

```bash
sudo umount /dev/sdb2
```

Es ist bewährte Praxis, `sudo umount` zu verwenden, um sicherzustellen, dass Sie die erforderlichen Berechtigungen zum Trennen des Dateisystems haben. Dieser Befehl ist distributionsübergreifend unter Linux universell, sodass dieselbe Syntax gilt, egal ob Sie Ubuntu, Fedora oder ein `debian umount` durchführen. Beachten Sie, dass Sie ein Gerät nicht aushängen können (`umount`), wenn es gerade verwendet wird (z. B. wenn eine Datei geöffnet ist oder Ihr aktuelles Arbeitsverzeichnis auf dem Gerät liegt).

### Verwendung von UUIDs für stabiles Mounten

Der Kernel benennt Geräte in der Reihenfolge, in der er sie entdeckt, was bedeutet, dass ein Gerätename wie `/dev/sdb2` sich zwischen Neustarts ändern kann. Um Probleme zu vermeiden, können Sie die universell eindeutige ID (UUID) eines Geräts verwenden, die konstant bleibt.

Um die UUIDs für Ihre Blockgeräte anzuzeigen, verwenden Sie den Befehl `blkid`:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Diese Ausgabe zeigt Gerätenamen, deren Dateisystemtypen und die entsprechenden UUIDs. Sie können dann ein Gerät mithilfe seiner UUID einbinden:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Obwohl Sie Geräte nicht immer über ihre UUIDs mounten müssen, ist dies die empfohlene Methode für das automatische Einhängen von Dateisystemen beim Start, wie z. B. einer sekundären Festplatte. Diesen Vorgang behandeln wir in der nächsten Lektion.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis für die Verwaltung von Linux-Dateisystemen zu festigen:

- **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - In diesem Labor lernen Sie, Festplattenpartitionen und Dateisysteme unter Linux zu verwalten. Sie verwenden fdisk, um eine neue Partition zu erstellen, sie mit ext4 zu formatieren, sie einzubinden, das persistente Einhängen in /etc/fstab zu konfigurieren und eine Swap-Partition zu erstellen, alles auf einer sicheren sekundären virtuellen Festplatte.

Dieses Labor hilft Ihnen, die Konzepte des Einhängens und Aushängens in realen Szenarien anzuwenden und Vertrauen in die Dateisystemverwaltung aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um ein Dateisystem anzuhängen? (Bitte verwenden Sie ein einzelnes, kleingeschriebenes englisches Wort als Antwort.)

## Quiz Answer

mount
