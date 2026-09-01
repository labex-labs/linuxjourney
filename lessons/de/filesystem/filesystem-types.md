---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "de"
order_index: 2
title: "Dateisystemtypen"
description: "Lerne, wie Linux VFS lokale, Netzwerk- und virtuelle Dateisysteme über eine gemeinsame Schnittstelle bereitstellt."
meta_title: "Dateisystemtypen – Das Dateisystem"
meta_description: "Entdecke Linux-Dateisystemtypen wie ext4, XFS und Btrfs. Lerne VFS, Journaling sowie lokale, Netzwerk- und virtuelle Dateisysteme kennen."
meta_keywords: "Linux Dateisystemtypen, Dateisystemtypen, ext4, Btrfs, XFS, Journaling, VFS, Linux Tutorial"
---

Linux unterstützt viele Dateisystemimplementierungen mit unterschiedlichen Datenträgerformaten, Netzwerkprotokollen, Konsistenzmodellen, Funktionen und Betriebswerkzeugen. Die richtige Wahl hängt von Distributionsunterstützung, Arbeitslast, Wiederherstellungsanforderungen, Speichertopologie und Erfahrung der Administratoren ab.

## Die Virtual-Filesystem-Schicht

Die Virtual-Filesystem-Schicht (VFS) des Kernels stellt gemeinsame Operationen wie Öffnen, Lesen, Schreiben, Umbenennen und Berechtigungsprüfungen bereit. Dateisystemimplementierungen verbinden diese Operationen mit ihren eigenen Datenstrukturen und Speichermedien.

Dadurch kann ein Prozess über ein gemeinsames Modell aus Pfaden und Dateideskriptoren auf ext4, XFS, NFS, tmpfs und procfs zugreifen. Dennoch sind nicht alle Dateisystemfunktionen und Verhaltensweisen identisch: Groß-/Kleinschreibung, Sperren, Berechtigungen, Garantien beim Umbenennen, erweiterte Attribute und Fehlerbehandlung können sich unterscheiden.

:::single-choice{#filesystem-types-vfs-role} Was ist die Hauptaufgabe des Linux-VFS?

::option[Jedes eingehängte Dateisystem auf dem Datenträger in ext4 umwandeln.]{#filesystem-types-vfs-convert-ext4 explanation="Die Abstraktion bewahrt die unterschiedlichen Dateisystemimplementierungen und Formate."}
::option[Jede Datei sichern, bevor eine Anwendung sie beschreibt.]{#filesystem-types-vfs-backup explanation="VFS leitet Operationen weiter und bietet keinen automatischen Sicherungsverlauf."}
::option[Gemeinsame Kernel-Dateioperationen für verschiedene Dateisystemimplementierungen bereitstellen.]{#filesystem-types-vfs-common-interface .correct explanation="VFS lässt Anwendungen gemeinsame Systemaufrufe verwenden, während jedes Dateisystem das zugrunde liegende Verhalten implementiert."}
:::

## Journaling und Absturzkonsistenz

Ein Journaling-Dateisystem zeichnet ausgewählte Aktualisierungen in einem Journal auf, damit es nach einem Absturz unvollständige Transaktionen wiederholen oder verwerfen kann. Journaling dient in erster Linie dazu, die strukturelle Konsistenz des Dateisystems schneller als durch eine vollständige Prüfung wiederherzustellen.

Es garantiert weder, dass die neuesten Anwendungsdaten erhalten geblieben sind, noch dass anwendungsbezogene Transaktionen über mehrere Dateien gültig sind oder die Speicherhardware jeden abgeschlossenen Schreibvorgang tatsächlich ausgeführt hat. Dateisysteme bieten unterschiedliche Datenmodi und Reihenfolgegarantien; Anwendungen müssen geeignete Flush- und atomare Aktualisierungsmuster verwenden. Ein Journal ist keine Sicherung und schützt nicht vor Löschen, Schadsoftware oder Geräteausfall.

:::single-choice{#filesystem-types-journal-scope} Was hilft Dateisystem-Journaling nach einem Absturz in erster Linie wiederherzustellen?

::option[Konsistente Dateisystemmetadaten und aufgezeichnete Transaktionen.]{#filesystem-types-journal-consistency .correct explanation="Das Wiederholen des Journals hilft, Dateisystemstrukturen wieder in einen schlüssigen Zustand zu versetzen."}
::option[Jede historische Version jedes Benutzerdokuments.]{#filesystem-types-journal-versions explanation="Ein Journal ist kein versionierter Sicherungsspeicher."}
::option[Daten von einem physisch zerstörten Speichergerät.]{#filesystem-types-journal-hardware-loss explanation="Die Wiederherstellung nach einem Geräteausfall erfordert Redundanz oder Sicherungen außerhalb des ausgefallenen Geräts."}
:::

## Verbreitete lokale Dateisysteme

- **ext4** ist ein ausgereiftes Journaling-Dateisystem, das von Linux-Distributionen und Wiederherstellungswerkzeugen breit unterstützt wird.
- **XFS** ist ein skalierbares Journaling-Dateisystem, das häufig für große Dateisysteme und parallele Ein-/Ausgabe-Arbeitslasten gewählt wird.
- **Btrfs** ist ein Copy-on-Write-Dateisystem mit Prüfsummen, Subvolumes, Snapshots und integrierten Funktionen für mehrere Geräte.

Funktionen benötigen betrieblichen Kontext. Ein Btrfs-Snapshot teilt anfangs Speicher mit seiner Quelle und ist keine unabhängige Sicherung, solange er auf demselben ausfallenden Gerät liegt. XFS und ext4 besitzen unterschiedliche Möglichkeiten zum Vergrößern, Verkleinern, Reparieren und Abstimmen. Bestätige vor Auswahl oder Änderung eines Root-Dateisystems die Unterstützung durch installierten Kernel, Bootumgebung und Wiederherstellungswerkzeuge.

:::single-choice{#filesystem-types-btrfs-snapshot} Warum ist ein Btrfs-Snapshot auf demselben Gerät keine vollständige Sicherung?

::option[Snapshots löschen das ursprüngliche Subvolume immer sofort.]{#filesystem-types-snapshot-deletes explanation="Ein Snapshot erzeugt eine weitere Subvolume-Ansicht und entfernt seine Quelle nicht automatisch."}
::option[Er teilt dieselbe Speicherausfalldomäne wie das Original.]{#filesystem-types-snapshot-failure-domain .correct explanation="Geräteverlust oder schwere Dateisystemschäden können sowohl die Quelle als auch ihren lokalen Snapshot betreffen."}
::option[Btrfs kann nicht mehr als eine Datei darstellen.]{#filesystem-types-btrfs-one-file explanation="Btrfs ist ein Allzweck-Dateisystem für Verzeichnisbäume und viele Dateien."}
:::

## Austausch-, Netzwerk- und virtuelle Dateisysteme

Linux kann Austauschformate wie FAT-Varianten, exFAT und NTFS einhängen, doch ihre Semantik für Unix-Eigentümerschaft, Berechtigungen, Links und Dateinamen unterscheidet sich. Einhängeoptionen und Treiberimplementierung bestimmen, wie Linux fehlende Funktionen darstellt.

Netzwerkdateisysteme wie NFS und SMB hängen von einem Server und Netzwerkprotokoll ab und besitzen eigene Regeln für Caching und Identitäten. Virtuelle Dateisysteme wie tmpfs, procfs und sysfs verwenden kein gewöhnliches dauerhaftes Datenträgerformat: tmpfs speichert flüchtige Daten in speichergestützten Seiten, während procfs und sysfs Kernel-Schnittstellen bereitstellen.

:::single-choice{#filesystem-types-procfs-category} Welche Beschreibung passt am besten zu procfs?

::option[Ein Windows-Austauschformat für Wechselmedien.]{#filesystem-types-procfs-windows explanation="FAT oder exFAT entsprechen diesem Zweck eher; procfs ist eine Linux-Kernel-Schnittstelle."}
::option[Ein virtuelles Dateisystem, das Prozess- und Kernel-Schnittstellen bereitstellt.]{#filesystem-types-procfs-virtual .correct explanation="Procfs erzeugt eine aktive Kernel-Ansicht, statt gewöhnliche dauerhafte Dateien auf einem Datenträger zu speichern."}
::option[Ein Journaling-Datenträgerdateisystem für Datenbankvolumes.]{#filesystem-types-procfs-journal explanation="Procfs besitzt weder ein gewöhnliches Journal auf dem Datenträger noch die Rolle eines Datenvolumes."}
:::

## Aktive Typen ermitteln

Zeige die Typen eingehängter Dateisysteme an:

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Alternative Ansichten sind `df -T` für die Speicherbelegung eingehängter Dateisysteme, `lsblk -f` für Blockgeräte und erkannte Dateisystemsignaturen sowie `/proc/filesystems` für vom laufenden Kernel unterstützte oder bekannte Typen. Diese beantworten verschiedene Fragen; ein nicht eingehängtes Dateisystem erscheint nicht in einer gewöhnlichen Liste eingehängter Dateisysteme.

:::single-choice{#filesystem-types-findmnt-output} Welcher Befehl listet in dieser Lektion eingehängte Ziele direkt mit Quelle, Typ und Optionen auf?

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="Findmnt liest die Einhängetabelle und formatiert die angeforderten Felder eingehängter Dateisysteme."}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="Dieser Befehl listet Hardwaredetails von Blockgeräten und nicht die tatsächlich eingehängten Dateisystemtypen und -optionen auf."}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="Dies meldet vom Kernel unterstützte Dateisystemtypen statt tatsächlicher Einhängequellen und -optionen."}
:::

Nutze das Lab [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) auf entbehrlichem Speicher, um Typen, Einhängeoptionen und Erkennungsansichten zu vergleichen.

## Zusammenfassung

Du kannst Dateisystemkategorien nun vergleichen, ohne von identischer Semantik auszugehen.

1. Ordne VFS gemeinsamen Operationen verschiedener Implementierungen zu.
2. Behandle Journaling als Unterstützung für Absturzkonsistenz und nicht als Sicherung.
3. Vergleiche ext4, XFS und Btrfs anhand unterstützter Operationen und Arbeitslast.
4. Unterscheide lokale Datenträger-, Netzwerk-, Austausch- und virtuelle Dateisysteme.
5. Verwende Einhänge- und Blockgerätewerkzeuge für unterschiedliche Inventarfragen.
