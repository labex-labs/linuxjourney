---
lang: "de"
title: "/etc/fstab"
description: "Erfahren Sie mehr über /etc/fstab in Linux, wie Sie Dateisystem-Mounts beim Start konfigurieren und Geräteeinträge verwalten. Verstehen Sie fstab für Anfänger!"
keywords: "/etc/fstab, Linux fstab, Dateisysteme mounten, Linux Boot, fstab Tutorial, Anfänger, Anleitung"
---

## Lesson Content

Wenn wir Dateisysteme beim Systemstart automatisch mounten möchten, können wir sie einer Datei namens `/etc/fstab` (ausgesprochen „eff es tab“, nicht „eff stab“) hinzufügen, kurz für Dateisystemtabelle. Diese Datei enthält eine permanente Liste der gemounteten Dateisysteme.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

Jede Zeile repräsentiert ein Dateisystem; die Felder sind:

- UUID – Device identifier
- Mount point – Verzeichnis, in das das Dateisystem gemountet wird
- Filesystem type
- Options – Weitere Mount-Optionen; siehe manpage für weitere Details
- Dump – Wird vom dump utility verwendet, um zu entscheiden, wann ein Backup erstellt werden soll; Sie sollten einfach 0 als Standardwert verwenden
- Pass – Wird von fsck verwendet, um zu entscheiden, in welcher Reihenfolge Dateisysteme überprüft werden sollen; wenn der Wert 0 ist, wird es nicht überprüft

Um einen Eintrag hinzuzufügen, ändern Sie einfach direkt die Datei `/etc/fstab` unter Verwendung der oben genannten Syntax. Seien Sie vorsichtig beim Ändern dieser Datei; Sie könnten sich das Leben potenziell etwas schwerer machen, wenn Sie Fehler machen.

## Exercise

Fügen Sie das USB-Laufwerk, an dem wir gearbeitet haben, als Eintrag in `/etc/fstab` hinzu. Nach einem Neustart sollte es immer noch gemountet sein.

## Quiz Question

Welche Datei wird verwendet, um zu definieren, wie Dateisysteme gemountet werden sollen?

## Quiz Answer

/etc/fstab
