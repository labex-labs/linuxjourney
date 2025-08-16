---
lang: "de"
title: "mount und umount"
description: "Erfahren Sie, wie Sie die Linux-Befehle mount und umount verwenden, um Dateisysteme zu verwalten. Verstehen Sie das Mounten, Unmounten von Geräten und UUIDs für Anfänger."
keywords: "Linux mount, umount Befehl, Dateisystem mounten, Linux UUID, Linux für Anfänger, Linux Tutorial, Mountpoint, Linux Anleitung"
---

## Lesson Content

Bevor Sie den Inhalt Ihres Dateisystems anzeigen können, müssen Sie es mounten. Dazu benötige ich den Gerätestandort, den Dateisystemtyp und einen Mountpoint. Der Mountpoint ist ein Verzeichnis auf dem System, an das das Dateisystem angehängt wird. Wir möchten also unser Gerät im Grunde an einen Mountpoint mounten.

Erstellen Sie zuerst den Mountpoint; in unserem Fall **mkdir /mydrive**.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

So einfach ist das! Wenn wir jetzt zu /mydrive gehen, können wir den Inhalt unseres Dateisystems sehen. Das **-t** gibt den Typ des Dateisystems an, dann haben wir den Gerätestandort, dann den Mountpoint.

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

Wir können unsere Gerätenamen, die entsprechenden Dateisystemtypen und ihre UUIDs sehen. Wenn wir nun etwas mounten möchten, können wir Folgendes verwenden:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Meistens müssen Sie Geräte nicht über ihre UUIDs mounten; es ist viel einfacher, den Gerätenamen zu verwenden, und oft weiß das Betriebssystem, wie gängige Geräte wie USB-Laufwerke gemountet werden. Wenn Sie jedoch ein Dateisystem beim Start automatisch mounten müssen, z. B. wenn Sie eine sekundäre Festplatte hinzugefügt haben, sollten Sie die UUID verwenden, und das werden wir in der nächsten Lektion behandeln.

## Exercise

Look at the manpage for `mount` and `umount` and see what other options you can use.

## Quiz Question

Welcher Befehl wird verwendet, um ein Dateisystem anzuhängen?

## Quiz Answer

mount
