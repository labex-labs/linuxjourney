---
lesson_id: "device-names"
course_id: "devices"
lang: "de"
order_index: 3
title: "Gerätenamen"
description: "Lerne, wie Linux verbreitete Speichergeräte, Partitionen, logische Geräte und dauerhafte Gerätelinks benennt."
meta_title: "Gerätenamen – Geräte"
meta_description: "Erkunde gängige Linux-Gerätenamen für Datenträger, Partitionen, NVMe, Device Mapper, RAID, Loop-Geräte und dauerhafte Links unter /dev/disk."
meta_keywords: "Linux Gerätenamen, Linux Gerätename, sda Bedeutung, /dev, SCSI Geräte, NVMe, Device Mapper, dauerhafte Gerätelinks, Pseudogeräte"
---

Linux-Gerätenamen spiegeln das Kernel-Subsystem und den Treiber wider, der eine Schnittstelle bereitstellt, und nicht immer den auf der Hardware aufgedruckten physischen Anschluss. Lerne die üblichen Muster, ermittle aber vor Änderungen am Speicher stets die tatsächliche Zuordnung auf dem aktuellen System.

## Namen von Datenträgern der SCSI-Schicht

Datenträger, die über die SCSI-Datenträgerschicht bereitgestellt werden, verwenden häufig Namen mit `sd`. Dazu gehören viele SCSI-, SATA-, USB-Speicher- und virtuelle Datenträger:

- `/dev/sda`: ein vollständiger Datenträger
- `/dev/sdb`: ein weiterer vollständiger Datenträger
- `/dev/sda3`: Partition 3 auf `/dev/sda`
- `/dev/sdb1`: Partition 1 auf `/dev/sdb`

Die Buchstaben spiegeln die Aufzählungsreihenfolge wider und sind keine dauerhafte Identität. Das Hinzufügen eines Controllers, eine geänderte Firmware-Reihenfolge oder das Anschließen eines Geräts kann verändern, welcher Datenträger einen bestimmten Buchstaben erhält.

:::single-choice{#device-names-sdb-first-partition}
Welcher Pfad bezeichnet im `sd`-Namensmuster Partition 1 auf `/dev/sdb`?

::option[`/dev/sda2`]{#device-names-sda-two explanation="Dieser Pfad bezeichnet Partition 2 auf dem aktuell `/dev/sda` genannten Datenträger."}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="Das Trennzeichen `p` wird bei Mustern verwendet, deren Grundname bereits mit einer Ziffer endet, nicht bei gewöhnlichen `sd`-Namen."}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="Bei `sd`-Datenträgern wird die Partitionsnummer direkt an den Namen des vollständigen Datenträgers angehängt."}
:::

## Namen, die mit Ziffern enden

Einige Namen vollständiger Geräte enthalten bereits Ziffern. Ihre Partitionsnamen verwenden deshalb `p` als Trennzeichen:

- `/dev/nvme0n1`: NVMe-Namespace 1 auf Controller 0
- `/dev/nvme0n1p2`: Partition 2 auf diesem Namespace
- `/dev/mmcblk0`: ein MMC-Blockgerät
- `/dev/mmcblk0p1`: Partition 1 auf diesem Gerät

NVMe-Geräte heißen normalerweise nicht `/dev/sdX`, sondern folgen der Namenskonvention des NVMe-Subsystems.

:::single-choice{#device-names-nvme-partition}
Welcher Pfad bezeichnet Partition 2 von `/dev/nvme0n1`?

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="NVMe-Partitionsnamen fügen vor der Partitionsnummer ein `p` ein."}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="Ohne Trennzeichen wären die abschließenden Ziffern gegenüber der Namespace-Nummer mehrdeutig."}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="Dies ist eine Partition eines Datenträgers der `sd`-Schicht und bezeichnet nicht den angegebenen NVMe-Namespace."}
:::

## Logische und virtuelle Blockgeräte

Linux erstellt außerdem Blockgeräte, die keinem physischen Datenträger eins zu eins entsprechen:

- `/dev/dm-N` für Device-Mapper-Geräte, häufig ergänzt durch beschreibende Links unter `/dev/mapper/`
- `/dev/mdN` für Linux-Software-RAID-Arrays
- `/dev/loopN` für gewöhnliche Dateien, die als Loop-Blockgeräte eingebunden sind

Partitionen, Verschlüsselungsebenen, RAID, logische Volumes und Dateisysteme bilden einen Stapel. Verwende Werkzeuge wie `lsblk`, um Eltern-Kind-Beziehungen zu sehen, statt den Stapel allein aus einem Namen abzuleiten.

:::single-choice{#device-names-device-mapper-link}
Welcher Ort enthält häufig beschreibende Links für Device-Mapper-Geräte?

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="Nutzer des Device Mappers wie LVM und Datenträgerverschlüsselung stellen in diesem Verzeichnis häufig benannte Links bereit."}
::option[`/dev/null/`]{#device-names-null-directory explanation="`/dev/null` ist ein Zeichengerät und kein Verzeichnis abgebildeter Blockgeräte."}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="Dies ist nicht der übliche Pfad für Namenslinks des Device Mappers."}
:::

## Dauerhafte Links für Speichergeräte

Die Userspace-Geräteverwaltung erzeugt Links unter `/dev/disk/`, die häufig folgendermaßen gruppiert sind:

- `by-id` für Hardware- oder Transportkennungen
- `by-uuid` für Dateisystem-UUIDs
- `by-label` für Dateisystembezeichnungen
- `by-partuuid` für UUIDs aus der Partitionstabelle
- `by-path` für topologieabhängige Pfade

Wähle eine Kennung passend zu der Eigenschaft, die stabil bleiben muss. Eine Dateisystem-UUID identifiziert ein Dateisystem und nicht zwangsläufig den darunterliegenden physischen Datenträger. Beim Klonen eines Dateisystems kann dessen UUID dupliziert werden; prüfe deshalb ihre Eindeutigkeit, bevor du dich darauf verlässt.

:::single-choice{#device-names-persistent-config}
Warum sind Links unter `/dev/disk/by-id/` in gerätespezifischen Konfigurationen häufig besser geeignet als `/dev/sdX`?

::option[Sie machen zerstörerische Schreibvorgänge automatisch rückgängig.]{#device-names-by-id-reversible explanation="Ein stabiler Name stellt weder Snapshots noch Sicherungen oder Schreibschutz bereit."}
::option[Sie wandeln ein Blockgerät in eine gewöhnliche Datei um.]{#device-names-by-id-regular explanation="Der Eintrag ist ein symbolischer Link, der weiterhin auf einen Blockgeräteknoten verweist."}
::option[Sie werden aus der Geräteidentität statt aus der aktuellen Aufzählungsreihenfolge abgeleitet.]{#device-names-by-id-stable .correct explanation="Das Linkziel kann sich ändern, während der identitätsbasierte Link weiterhin demselben erkannten Gerät zugeordnet bleibt."}
:::

## Namen von Pseudogeräten

Namen wie `/dev/null`, `/dev/zero` und `/dev/urandom` bezeichnen Kernel-Pseudogeräte statt physischen Speicher. `/dev/null` verwirft Schreibvorgänge und liefert beim Lesen sofort das Dateiende; `/dev/zero` stellt Nullbytes bereit; `/dev/urandom` liefert Bytes aus dem Zufallszahlengenerator des Kernels.

:::single-choice{#device-names-zero-read}
Was erzeugt das Lesen aus `/dev/zero`?

::option[Eine Liste unbenutzter Speichergeräte.]{#device-names-zero-storage-list explanation="Es ist ein byteserzeugendes Zeichengerät und kein Erkennungsbefehl."}
::option[Einen Strom von Bytes mit dem Wert null.]{#device-names-zero-bytes .correct explanation="Das Zero-Pseudogerät gibt bei Leseanforderungen Nullbytes zurück."}
::option[Sofort das Dateiende, wie beim Lesen aus `/dev/null`.]{#device-names-zero-eof explanation="`/dev/zero` erzeugt fortlaufend Bytes, während Lesevorgänge auf `/dev/null` das Dateiende zurückgeben."}
:::

Nutze das Lab [Hardwaregeräte unter Linux erkunden](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861), um vor Partitionsarbeiten Namen, dauerhafte Links und `lsblk`-Beziehungen zu vergleichen.

## Zusammenfassung

Du kannst gängige Linux-Speichernamen nun entschlüsseln, ohne sie als dauerhafte Identität zu behandeln.

1. Lies `sdXNUMBER` als Partition eines `sd`-Datenträgers.
2. Verwende `pNUMBER`, wenn der Name des vollständigen Geräts bereits mit einer Ziffer endet.
3. Erkenne logische Geräte wie Device Mapper, RAID und Loop-Geräte.
4. Bevorzuge dauerhafte Links passend zur benötigten Identität.
5. Unterscheide Speichernamen von Kernel-Pseudogeräten.
