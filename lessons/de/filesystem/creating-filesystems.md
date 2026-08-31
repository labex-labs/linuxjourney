---
lesson_id: "creating-filesystems"
course_id: "filesystem"
lang: "de"
order_index: 5
title: "Dateisysteme erstellen"
description: "Lerne, das Ziel eines Blockgeräts zu prüfen und mit formatspezifischen Werkzeugen ein Dateisystem zu erstellen."
meta_title: "Dateisysteme erstellen – Das Dateisystem"
meta_description: "Lerne, mit mkfs ein Dateisystem auf einem geprüften Linux-Blockgerät zu erstellen und Typ, Signaturen, aktive Verbraucher, Label und UUID sicher zu prüfen."
meta_keywords: "mkfs, Dateisystem erstellen, ext4, Linux Partitionierung, Blockgerät formatieren, Linux Datenträgerverwaltung"
---

Beim Erstellen eines Dateisystems werden neue Zuweisungs- und Metadatenstrukturen auf ein Blockgerät geschrieben. Das ist ein zerstörerischer Initialisierungsschritt und nicht nur eine Änderung des Labels. Verwende zum Üben ausschließlich entbehrlichen Speicher und halte eine geprüfte Sicherung vor, bevor du ein Gerät formatierst, das jemals wertvolle Daten enthielt.

## `mkfs` verstehen

`mkfs` ist häufig eine Oberfläche, die an ein dateisystemspezifisches Programm wie `mkfs.ext4`, `mkfs.xfs` oder `mkfs.btrfs` weiterleitet. Ein allgemeiner Befehl hat diese Form:

```bash
$ sudo mkfs -t ext4 /dev/GEPRUEFTE-PARTITION
```

Der Platzhalter darf erst nach der Überprüfung ersetzt werden. Eine entsprechende formatspezifische Syntax lautet häufig:

```bash
$ sudo mkfs.ext4 /dev/GEPRUEFTE-PARTITION
```

Unterstützte Optionen, Standardwerte, Funktionsgruppen und Fragen vor dem Überschreiben unterscheiden sich zwischen Implementierungen. Lies das lokale Handbuch des konkreten Formatierungswerkzeugs, statt identisches Verhalten aller `mkfs`-Backends anzunehmen.

:::single-choice{#creating-filesystems-mkfs-role}
Was fordert `mkfs -t ext4 TARGET` an?

::option[Ein vorhandenes Dateisystem einhängen, ohne es zu verändern.]{#creating-filesystems-mount-existing explanation="Das Einhängen ist eine getrennte Operation; mkfs initialisiert Metadaten auf dem Gerät."}
::option[Ext4-Dateisystemstrukturen auf dem Ziel erstellen.]{#creating-filesystems-create-ext4 .correct explanation="Die Oberfläche wählt für das angegebene Blockgerät die ext4-Formatierungsimplementierung aus."}
::option[Jedes aktuell eingehängte Dateisystem auflisten.]{#creating-filesystems-list-mounted explanation="Schreibgeschützte Einhängeinventare erstellen Werkzeuge wie `findmnt`."}
:::

## Jede Speicherebene prüfen

Bestimme das Ziel vor dem Formatieren anhand von Modell, Seriennummer, Größe, Topologie, dauerhaftem Link und beabsichtigter Aufgabe:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
$ findmnt --real
$ sudo wipefs --no-act /dev/GEPRUEFTE-PARTITION
```

`wipefs --no-act` meldet erkannte Signaturen, ohne sie zu löschen. Prüfe außerdem die Nutzung durch Swap, LVM, RAID, Verschlüsselung, virtuelle Maschinen, Container und Anwendungen. Ein Gerät kann aktiv sein, obwohl `MOUNTPOINTS` leer ist.

Hänge jede relevante Ebene mit ihrem eigenen Werkzeug aus oder deaktiviere sie. Prüfe die Identität unmittelbar vor dem Formatierungsbefehl erneut, weil sich Aufzählungsnamen ändern können.

:::single-choice{#creating-filesystems-wipefs-no-act}
Was liefert `wipefs --no-act TARGET` in diesem Arbeitsablauf?

::option[Einen schreibgeschützten Bericht erkannter Signaturen.]{#creating-filesystems-signature-report .correct explanation="Der No-Act-Modus hilft, vorhandene Dateisystem-, Partitionstabellen-, RAID- oder andere Signaturen zu erkennen, ohne sie zu entfernen."}
::option[Ein neues leeres Dateisystem, das eingehängt werden kann.]{#creating-filesystems-wipefs-formats explanation="Das Untersuchen von Signaturen initialisiert kein neues Dateisystem."}
::option[Eine Garantie, dass kein Prozess das Ziel verwendet.]{#creating-filesystems-wipefs-no-users explanation="Die Nutzung muss getrennt für Einhängungen und den weiteren Speicherstapel geprüft werden."}
:::

## Den Dateisystemtyp bewusst auswählen

Wähle einen Typ, der von Distribution, Bootumgebung, Sicherungs- und Reparaturwerkzeugen sowie der Arbeitslast unterstützt wird. Berücksichtige benötigte Grenzen, Snapshots, Prüfsummen, Quoten, Verschlüsselungsebenen, Vergrößerungs- oder Verkleinerungsverhalten und plattformübergreifenden Zugriff.

Wähle ein Format nicht allein aufgrund seiner Beliebtheit. Ext4, XFS und Btrfs besitzen beispielsweise unterschiedliche Betriebsfunktionen und Wiederherstellungsverfahren. Ein Wechselmedium zum Datenaustausch kann ein anderes Format mit abweichender Unix-Berechtigungssemantik benötigen.

:::single-choice{#creating-filesystems-type-choice}
Was ist eine sinnvolle Grundlage für die Auswahl eines Dateisystemtyps?

::option[Der Name, der sich am kürzesten tippen lässt.]{#creating-filesystems-shortest-name explanation="Die Befehlslänge sagt nichts über Haltbarkeit, Funktionen oder Unterstützung aus."}
::option[Das Versprechen, dass künftig kein Speicherausfall auftreten kann.]{#creating-filesystems-no-failure explanation="Kein Dateisystem verhindert Hardwareausfälle oder beseitigt die Notwendigkeit von Sicherungen."}
::option[Anforderungen der Arbeitslast sowie unterstützte Sicherungs-, Boot- und Wiederherstellungswerkzeuge.]{#creating-filesystems-supported-workflow .correct explanation="Das Format muss sowohl zu den technischen Anforderungen als auch zu den Betriebs- und Wiederherstellungsmöglichkeiten der Umgebung passen."}
:::

## Label, UUIDs und Überprüfung

Formatierungswerkzeuge erzeugen normalerweise eine Dateisystem-UUID und können häufig ein menschenlesbares Label festlegen. Verwende Labels, die in der Umgebung hinreichend eindeutig sind, und stelle sicher, dass geklonte Dateisysteme keine widersprüchlichen Kennungen behalten, wenn sie gleichzeitig eingehängt werden.

Untersuche das Dateisystem nach erfolgreicher Erstellung, ohne es einzuhängen:

```bash
$ lsblk -f /dev/GEPRUEFTE-PARTITION
$ sudo blkid /dev/GEPRUEFTE-PARTITION
```

Notiere die UUID für die spätere Einhängekonfiguration. Das Erstellen eines Dateisystems hängt es nicht ein, legt keine Anwendungsverzeichnisse an, spielt keine Sicherungen ein und macht die Einhängung nicht dauerhaft über Neustarts hinweg.

:::single-choice{#creating-filesystems-after-mkfs}
Was bleibt nach dem Erstellen eines Dateisystems ein getrennter Schritt?

::option[Es am vorgesehenen Verzeichnis einhängen.]{#creating-filesystems-mount-separate .correct explanation="Das Formatieren schreibt Dateisystemstrukturen, während das Einhängen das Dateisystem mit dem sichtbaren Verzeichnisbaum verbindet."}
::option[Dem Blockgerät überhaupt eine Kapazität zuweisen.]{#creating-filesystems-capacity explanation="Die darunterliegende Partition oder das logische Gerät stellt bereits die zu formatierende Kapazität bereit."}
::option[Das Kernel-Verzeichnis `/dev` von Grund auf neu erstellen.]{#creating-filesystems-create-dev explanation="Die Verwaltung von Geräteknoten ist unabhängig vom Formatieren eines einzelnen Ziels."}
:::

Nutze das Lab [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) ausschließlich auf dem entbehrlichen zweiten Datenträger des Labs.

## Zusammenfassung

Du kannst die Erstellung eines Dateisystems nun als geprüfte, zerstörerische Operation beschreiben.

1. Behandle `mkfs` als Weiterleitung an formatspezifische Werkzeuge.
2. Prüfe dauerhafte Identität, Signaturen und jeden aktiven Verbraucher.
3. Wähle ein Dateisystem anhand von Unterstützungs- und Wiederherstellungsanforderungen.
4. Untersuche erzeugten Typ, Label und UUID vor dem Einhängen.
