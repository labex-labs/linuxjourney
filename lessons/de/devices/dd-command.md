---
index: 7
lang: "de"
title: "dd"
meta_title: "dd - Geräte"
meta_description: "Lernen Sie den Linux-Befehl dd zum Kopieren von Daten und zur Erstellung von Disk-Images. Verstehen Sie seine Optionen wie if, of und bs. Beginnen Sie Ihre Linux-Datenverwaltung!"
meta_keywords: "dd Befehl, Linux dd, Daten kopieren, Disk-Imaging, Linux Tutorial, Anfänger, Anleitung, Datensicherung"
---

## Lesson Content

Das Tool `dd` ist äußerst nützlich zum Konvertieren und Kopieren von Daten. Es liest die Eingabe aus einer Datei oder einem Datenstrom und schreibt sie in eine Datei oder einen Datenstrom.

Betrachten Sie den folgenden Befehl:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

Dieser Befehl kopiert den Inhalt von `backup.img` nach `/dev/sdb`. Er kopiert die Daten in Blöcken von 1024 Bytes, bis keine Daten mehr zu kopieren sind.

- `if=file` – Eingabedatei; liest aus einer Datei anstelle der Standardeingabe.
- `of=file` – Ausgabedatei; schreibt in eine Datei anstelle der Standardausgabe.
- `bs=bytes` – Blockgröße; es liest und schreibt so viele Bytes Daten auf einmal. Sie können verschiedene Größenmetriken verwenden, indem Sie die Größe mit einem `k` für Kilobyte, `m` für Megabyte usw. angeben, sodass 1024 Bytes 1k sind.
- `count=number` – Anzahl der zu kopierenden Blöcke.

Sie werden einige `dd`-Befehle sehen, die die Option `count` verwenden. Normalerweise möchten Sie bei `dd`, wenn Sie eine Datei kopieren möchten, die 1 Megabyte groß ist, diese Datei nach dem Kopieren als 1 Megabyte sehen. Nehmen wir an, Sie führen den folgenden Befehl aus:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Unsere Datei `backup.img` ist 10 MB groß; wir sagen jedoch in diesem Befehl, dass 1 MB 2 Mal kopiert werden soll, sodass nur 2 MB kopiert werden, wodurch unsere kopierten Daten unvollständig bleiben. `count` kann in vielen Situationen nützlich sein, aber wenn Sie nur Daten kopieren, können Sie `count` und sogar `bs` weglassen. Wenn Sie Ihre Datenübertragungen wirklich optimieren möchten, sollten Sie diese Optionen verwenden.

`dd` ist extrem leistungsfähig; Sie können es verwenden, um Backups von allem zu erstellen, einschließlich ganzer Festplatten, zum Wiederherstellen von Disk-Images und vielem mehr. Seien Sie vorsichtig, dieses leistungsstarke Tool kann einen Preis haben, wenn Sie nicht sicher sind, was Sie tun.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Datenmanipulation und Festplattenverwaltung unter Linux zu vertiefen:

1. **[Erstellen und Wiederherstellen eines Backups mit tar unter Linux](https://labex.io/de/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** – Üben Sie das Erstellen und Wiederherstellen von Dateisystem-Backups, eine wichtige Fähigkeit im Zusammenhang mit Datenintegrität und -wiederherstellung, für die `dd` ebenfalls verwendet werden kann.
2. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Lernen Sie, Festplattenpartitionen und Dateisysteme zu verwalten, einschließlich des Erstellens, Formatierens und Einhängens, was grundlegende Konzepte bei der Arbeit mit Tools wie `dd` für die Disk-Image-Erstellung sind.

Diese Labs helfen Ihnen, die Konzepte der Datenverarbeitung und Festplattenoperationen in realen Szenarien anzuwenden und Vertrauen in Systemadministrationsaufgaben aufzubauen.

## Quiz Question

Was ist die `dd`-Option für die Blockgröße?

## Quiz Answer

bs
