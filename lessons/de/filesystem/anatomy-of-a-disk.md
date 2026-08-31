---
lesson_id: "anatomy-of-a-disk"
course_id: "filesystem"
lang: "de"
order_index: 3
title: "Aufbau eines Datenträgers"
description: "Lerne, wie Blockgeräte, Partitionstabellen, Partitionen und Dateisysteme getrennte Speicherebenen bilden."
meta_title: "Aufbau eines Datenträgers – Das Dateisystem"
meta_description: "Erkunde den Aufbau eines Datenträgers unter Linux. Lerne Blockgeräte, MBR- und GPT-Partitionstabellen, Partitionen und Dateisysteme voneinander zu unterscheiden."
meta_keywords: "Datenträger Linux, Linux Partitionen, MBR, GPT, Partitionstabelle, Dateisystem, Blockgerät, Datenträgeraufbau"
---

Ein Speichergerät wird als Blockgerät wie `/dev/sda` oder `/dev/nvme0n1` bereitgestellt. Es kann eine Partitionstabelle enthalten, deren Einträge Bereiche beschreiben, die als untergeordnete Blockgeräte erscheinen. Eine Partition kann anschließend ein Dateisystem, eine Swap-Signatur, ein RAID-Mitglied, einen Verschlüsselungscontainer, ein Physical Volume für logische Volumes oder ein anderes Datenformat enthalten.

Diese Ebenen sind unabhängig: Nicht jeder Datenträger besitzt eine Partitionstabelle, nicht jede Partition enthält ein Dateisystem, und ein Dateisystem kann auf einem logischen Volume oder einem vollständigen Gerät liegen.

## Partitionstabellen und Grenzen

Eine Partitionstabelle zeichnet Startpositionen, Längen, Typkennungen und schemaspezifische Attribute auf. Der Kernel liest sie und erzeugt daraus Partitionsblockgeräte wie `/dev/sda1` oder `/dev/nvme0n1p1`.

In gewöhnlichen Strukturen dürfen sich Partitionsgrenzen nicht überschneiden. Speicher außerhalb aller Einträge ist aus Sicht der Partitionstabelle nicht zugewiesen, kann aber noch alte Signaturen oder Daten enthalten. Das Ändern einer Tabelle verschiebt Dateisysteminhalte nicht automatisch passend zu den neuen Grenzen.

:::single-choice{#anatomy-disk-partition-table-role}
Was teilt dem Betriebssystem mit, wo Datenträgerpartitionen beginnen und enden?

::option[Das aktuelle Arbeitsverzeichnis der Shell.]{#anatomy-disk-shell-directory explanation="Ein Shellpfad spielt für Partitionsgrenzen auf einem Datenträger keine Rolle."}
::option[Die Partitionstabelle des Datenträgers.]{#anatomy-disk-table-boundaries .correct explanation="Partitionseinträge beschreiben Bereiche, die der Kernel als untergeordnete Blockgeräte bereitstellen kann."}
::option[Die primäre Gruppe des Benutzerkontos.]{#anatomy-disk-user-group explanation="Anmeldedaten definieren weder Datenträgergeometrie noch Partitionsstruktur."}
:::

## MBR-Partitionierung

Das ältere DOS-/MBR-Schema speichert seine primäre Tabelle im ersten logischen Sektor. Sie besitzt vier primäre Tabelleneinträge. Ein Eintrag kann eine erweiterte Partition beschreiben, die als Container für eine verkettete Reihe logischer Partitionen dient und so mehr als vier nutzbare Bereiche ermöglicht.

Mit 32-Bit-Sektoradressen und logischen Sektoren von 512 Byte erreicht MBR eine häufig genannte Grenze von etwa 2 TiB. Die genaue Adressierbarkeit hängt von Sektorgröße und Werkzeugunterstützung ab. MBR besitzt außerdem weder die redundanten Kopf- und Tabellenkopien von GPT noch GUIDs pro Partition.

:::single-choice{#anatomy-disk-mbr-more-than-four}
Welche MBR-Struktur ermöglicht mehr als vier nutzbare Partitionen?

::option[Eine Journal-Partition mit weiteren primären Einträgen.]{#anatomy-disk-mbr-journal explanation="Dateisystem-Journaling steht in keinem Zusammenhang mit der MBR-Tabelle aus vier Einträgen."}
::option[Eine erweiterte Partition, die logische Partitionen enthält.]{#anatomy-disk-mbr-extended .correct explanation="Ein primärer Eintrag kann einen erweiterten Container definieren, in dem logische Partitionen verkettet sind."}
::option[Ein Dateisystem-Superblock, der die Einträge neu nummeriert.]{#anatomy-disk-mbr-superblock explanation="Metadaten eines Dateisystems erweitern die Partitionstabelle des Datenträgers nicht."}
:::

## GPT-Partitionierung

Die GUID Partition Table (GPT) verwendet 64-Bit-Adressen logischer Blöcke und speichert normalerweise einen primären Kopf und ein Eintragsarray nahe dem Anfang sowie Sicherungskopien nahe dem Ende des Datenträgers. Ein Protective MBR verhindert, dass ältere, ausschließlich MBR-fähige Software den Datenträger als leer behandelt.

Jeder GPT-Eintrag enthält eine Partitionstyp-GUID und eine eindeutige Partitions-GUID; GPT besitzt daher nicht nur einen einzigen Partitionstyp. Die Anzahl verfügbarer Einträge wird durch die zugewiesene Tabelle und die Werkzeuge bestimmt und ist üblicherweise wesentlich größer als vier, ohne erweiterte oder logische Partitionen zu benötigen.

GPT wird normalerweise für UEFI-Bootdatenträger verwendet, doch Partitionierung und Firmware-Bootmodus sind getrennte Konzepte. Ein UEFI-System benötigt außerdem passende Bootdateien und eine EFI-Systempartition; GPT allein macht einen Datenträger nicht bootfähig.

:::single-choice{#anatomy-disk-gpt-identifiers}
Welche Kennungen enthält ein GPT-Partitionseintrag?

::option[Eine Typ-GUID und eine eindeutige Partitions-GUID.]{#anatomy-disk-gpt-guids .correct explanation="Der Typ beschreibt die vorgesehene Verwendung, während die eindeutige GUID genau diesen Partitionseintrag identifiziert."}
::option[Nur einen universellen Typ, den jede GPT-Partition gemeinsam verwendet.]{#anatomy-disk-gpt-one-type explanation="GPT definiert zahlreiche Typ-GUIDs für verschiedene Partitionszwecke."}
::option[Anmelde-UID und -GID des Benutzers, der die Partition erstellt hat.]{#anatomy-disk-gpt-user-ids explanation="Dateisystem-Kontokennungen sind keine Identitätsfelder einer GPT-Partition."}
:::

## Dateisystemstrukturen hängen vom Format ab

Nach der Partitionierung schreibt ein Werkzeug zur Dateisystemerstellung die vom jeweiligen Dateisystem festgelegten Strukturen. Viele Formate besitzen Konzepte wie Superblocks, Zuweisungsmetadaten, Verzeichniseinträge und Datenextents oder -blöcke. Aufbau, Redundanz und Begriffe unterscheiden sich jedoch.

Ext-Dateisysteme verwenden beispielsweise Inodes und Blockgruppen, während andere Dateisysteme Metadaten durch andere Bäume oder Zuweisungsstrukturen organisieren. Übertrage kein vereinfachtes Diagramm aus „Bootblock, einem Superblock, Inode-Tabelle und Datenblöcken“ auf jedes Dateisystem.

:::single-choice{#anatomy-disk-filesystem-layer}
Erzeugt das Anlegen einer Partition automatisch ein Dateisystem darin?

::option[Nein; Formatieren oder eine andere ausdrückliche Nutzung ist ein getrennter Schritt.]{#anatomy-disk-partition-not-filesystem .correct explanation="Die Partitionstabelle definiert nur einen Blockbereich; dessen Inhalt bleibt davon unabhängig."}
::option[Ja; jede Partition wird automatisch als ext4 formatiert.]{#anatomy-disk-auto-ext4 explanation="Partitionierungswerkzeuge erstellen nicht universell ein ext4-Dateisystem."}
::option[Ja; GPT-Einträge sind selbst eingehängte Verzeichnisse.]{#anatomy-disk-gpt-mounted explanation="Ein Partitionseintrag beschreibt Speicher und ist kein Einhängepunkt eines Dateisystems."}
:::

## Die aktuelle Struktur untersuchen

Verwende vor jeder Änderung schreibgeschützte Ansichten:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,PTTYPE,PARTTYPE,FSTYPE,MOUNTPOINTS
$ sudo parted --list
```

`PTTYPE` beschreibt ein erkanntes Partitionstabellenschema, `PARTTYPE` eine Partitionstypkennung und `FSTYPE` eine erkannte Inhaltssignatur. Die Erkennung ist ein Beleg, aber keine Garantie dafür, dass der Inhalt intakt oder sicher einzuhängen ist.

Gerätenamen können sich ändern, und veraltete Signaturen können die Erkennung verwirren. Bestätige Modell, Seriennummer, Größe, Transport, dauerhafte Links, aktive Einhängungen, Swap, RAID, LVM, Verschlüsselung und Sicherungen, bevor du ein Partitionierungswerkzeug im Schreibmodus öffnest.

:::single-choice{#anatomy-disk-lsblk-fields}
Welches `lsblk`-Feld unterscheidet erkannte Dateisysteminhalte vom Partitionstabellenschema?

::option[`FSTYPE`]{#anatomy-disk-fstype .correct explanation="`FSTYPE` meldet ein erkanntes Dateisystem oder eine andere bekannte Inhaltssignatur, während `PTTYPE` das Tabellenschema meldet."}
::option[`NAME`]{#anatomy-disk-name-field explanation="`NAME` bezeichnet den Blockgeräteeintrag des Kernels und identifiziert nicht ausdrücklich das Inhaltsformat."}
::option[`SIZE`]{#anatomy-disk-size-field explanation="Die Größe meldet Kapazität und nicht den Dateisystemtyp."}
:::

Nutze das Lab [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) ausschließlich auf entbehrlichem Speicher, um diese Ebenen zu üben.

## Zusammenfassung

Du kannst Metadaten der Datenträgerstruktur nun von den darin gespeicherten Datenformaten trennen.

1. Erkenne vollständige Geräte und ihre untergeordneten Partitionsgeräte.
2. Ordne erweiterte MBR-Partitionen der älteren Grenze von vier Einträgen zu.
3. Ordne GPT redundanten Tabellen und GUIDs pro Partition zu.
4. Behandle das Erstellen eines Dateisystems getrennt vom Erstellen einer Partition.
5. Untersuche vor Änderungen jede Speicherebene und jeden aktiven Verbraucher.
