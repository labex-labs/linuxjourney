---
index: 7
lang: "de"
title: "/etc/fstab"
meta_title: "/etc/fstab - Das Dateisystem"
meta_description: "Erfahren Sie mehr über /etc/fstab in Linux, wie Sie Dateisystem-Mounts beim Start konfigurieren und Geräteeinträge verwalten. Verstehen Sie fstab für Anfänger!"
meta_keywords: "/etc/fstab, Linux fstab, Dateisysteme mounten, Linux-Boot, fstab-Tutorial, Anfänger, Anleitung"
---

## Lesson Content

Wenn wir Dateisysteme beim Start automatisch mounten möchten, können wir sie einer Datei namens `/etc/fstab` (ausgesprochen „eff es tab“, nicht „eff stab“) hinzufügen, kurz für Dateisystemtabelle. Diese Datei enthält eine permanente Liste der gemounteten Dateisysteme.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

Jede Zeile repräsentiert ein Dateisystem; die Felder sind:

- UUID – Gerätekennung
- Mount-Punkt – Verzeichnis, in das das Dateisystem gemountet wird
- Dateisystemtyp
- Optionen – Weitere Mount-Optionen; weitere Details finden Sie in der Manpage
- Dump – Wird vom Dump-Dienstprogramm verwendet, um zu entscheiden, wann eine Sicherung erstellt werden soll; Sie sollten einfach 0 als Standardwert verwenden
- Pass – Wird von fsck verwendet, um zu entscheiden, in welcher Reihenfolge Dateisysteme überprüft werden sollen; wenn der Wert 0 ist, wird es nicht überprüft

Um einen Eintrag hinzuzufügen, ändern Sie einfach direkt die Datei `/etc/fstab` mit der oben genannten Syntax. Seien Sie vorsichtig, wenn Sie diese Datei ändern; Sie könnten sich das Leben etwas schwerer machen, wenn Sie einen Fehler machen.

## Exercise

Übung macht den Meister! Praktische Erfahrung ist entscheidend, um zu verstehen, wie Dateisysteme verwaltet und sichergestellt werden, dass sie beim Systemstart korrekt gemountet werden. Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Dateisystemverwaltung und der Datei `/etc/fstab` zu vertiefen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Üben Sie das Erstellen von Partitionen, deren Formatierung, das Mounten und das Konfigurieren des persistenten Mountens mithilfe von `/etc/fstab`.
2. **[Eine Swap-Datei in Linux erstellen und aktivieren](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** – Lernen Sie die wesentliche administrative Aufgabe des Erstellens und Aktivierens einer Swap-Datei, die oft Einträge in `/etc/fstab` beinhaltet.

Diese Übungen helfen Ihnen, die Konzepte des Dateisystem-Mountings und der Konfiguration in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Festplattenressourcen in Linux aufzubauen.

## Quiz Question

Welche Datei wird verwendet, um zu definieren, wie Dateisysteme gemountet werden sollen?

## Quiz Answer

/etc/fstab
