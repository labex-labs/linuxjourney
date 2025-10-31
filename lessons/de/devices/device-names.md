---
index: 3
lang: "de"
title: "Gerätenamen"
meta_title: "Gerätenamen - Geräte"
meta_description: "Entdecken Sie gängige Linux-Gerätenamen für Speicher und Peripheriegeräte. Dieser Leitfaden erklärt die Benennungskonvention für SCSI-Festplatten (wie sda), wofür sda steht, und Pseudo-Geräte wie /dev/null."
meta_keywords: "linux gerätenamen, linux gerätename, wofür steht sda, sd elementname, was wäre üblicherweise der gerätename für die erste partition auf der zweiten scsi-festplatte, /dev, scsi geräte, pseudo geräte, pata geräte"
---

## Lesson Content

In Linux wird jedes Gerät durch eine Datei im Verzeichnis `/dev` repräsentiert. Das Verständnis der Namenskonventionen für diese Dateien ist für die Systemadministration von entscheidender Bedeutung. Hier sind die häufigsten Arten von Linux-Gerätenamen, denen Sie begegnen werden.

### SCSI- und moderne Speichergeräte

Auch wenn Ihr Rechner moderne Speicher wie SATA, NVMe oder USB-Laufwerke verwendet, verwaltet der Linux-Kernel diese oft über sein SCSI (Small Computer System Interface) Subsystem. Deshalb ist das häufigste Präfix für Speichergeräte `sd`, was ursprünglich für „SCSI disk“ stand.

Der `sd element name` folgt einem klaren Muster:

- Das Präfix `sd` kennzeichnet ein Massenspeichergerät.
- Der nächste Buchstabe repräsentiert das Laufwerk selbst, zugewiesen in der Reihenfolge der Erkennung (`a` für das erste, `b` für das zweite usw.).
- Eine Zahl am Ende gibt die Partition auf diesem Laufwerk an.

Zu den gängigen SCSI-Gerätedateien gehören:

- `/dev/sda`: Das erste Speicherlaufwerk.
- `/dev/sdb`: Das zweite Speicherlaufwerk.
- `/dev/sda3`: Die dritte Partition auf dem ersten Speicherlaufwerk.

Wie lautet also der Gerätename für die erste Partition auf der zweiten SCSI-Festplatte? Dem Muster folgend ist die zweite Festplatte `sdb` und ihre erste Partition `1`. Daher lautet der Gerätename `/dev/sdb1`.

### Pseudo-Geräte

Pseudo-Geräte sind spezielle Dateien, die keiner physischen Hardware entsprechen, aber nützliche Systemfunktionen bereitstellen. Es handelt sich typischerweise um Zeichengeräte.

- `/dev/zero`: Akzeptiert und verwirft alle Eingaben. Beim Lesen erzeugt es einen kontinuierlichen Strom von NULL-Bytes (Nullwert).
- `/dev/null`: Akzeptiert und verwirft alle an ihn geschriebenen Eingaben und erzeugt beim Lesen keine Ausgabe.
- `/dev/random`: Erzeugt einen Strom von Zufallszahlen, die aus Umgebungsrauschen generiert werden.

### Veraltete PATA-Geräte

Auf älteren Systemen stoßen Sie möglicherweise auf Festplatten, die die Parallel ATA (PATA) Schnittstelle verwenden. Der Linux-Gerätename für diese Laufwerke verwendet das Präfix `hd`.

- `/dev/hda`: Die erste PATA-Festplatte.
- `/dev/hdd2`: Die zweite Partition auf der vierten PATA-Festplatte.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis von Linux-Gerätenamen und Speicherverwaltung zu festigen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Üben Sie das Erstellen, Formatieren und Einhängen von Partitionen, was direkt die Arbeit mit Gerätenamen beinhaltet.
2. **[Hardware-Geräte in Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** – Lernen Sie, verschiedene Hardware-Geräte und ihre zugehörigen Namen in einer Linux-Umgebung zu identifizieren und zu überprüfen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Speicher und das Verständnis von Hardware in Linux aufzubauen.

## Quiz Question

Wie lautet üblicherweise der Gerätename für die erste Partition auf der zweiten SCSI-Festplatte? Bitte geben Sie die Antwort auf Englisch an und achten Sie auf die korrekte Groß-/Kleinschreibung.

## Quiz Answer

/dev/sdb1
