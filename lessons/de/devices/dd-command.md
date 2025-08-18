---
lang: "de"
title: "dd"
meta_description: "Lernen Sie den Linux dd-Befehl zum Kopieren von Daten und zur Erstellung von Disk-Images. Verstehen Sie seine Optionen wie if, of und bs. Beginnen Sie Ihre Reise ins Linux-Datenmanagement!"
meta_keywords: "dd Befehl, Linux dd, Daten kopieren, Disk-Imaging, Linux Tutorial, Anfänger, Leitfaden, Datensicherung"
---

## Lesson Content

Das `dd`-Tool ist äußerst nützlich zum Konvertieren und Kopieren von Daten. Es liest Eingaben aus einer Datei oder einem Datenstrom und schreibt sie in eine Datei oder einen Datenstrom.

Betrachten Sie den folgenden Befehl:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

Dieser Befehl kopiert den Inhalt von `backup.img` nach `/dev/sdb`. Er kopiert die Daten in Blöcken von 1024 Bytes, bis keine Daten mehr zu kopieren sind.

- `if=file` – Eingabedatei; liest aus einer Datei anstelle der Standardeingabe.
- `of=file` – Ausgabedatei; schreibt in eine Datei anstelle der Standardausgabe.
- `bs=bytes` – Blockgröße; es liest und schreibt diese Anzahl von Bytes an Daten auf einmal. Sie können verschiedene Größenmetriken verwenden, indem Sie die Größe mit einem `k` für Kilobyte, `m` für Megabyte usw. kennzeichnen, sodass 1024 Bytes 1k sind.
- `count=number` – Anzahl der zu kopierenden Blöcke.

Sie werden einige `dd`-Befehle sehen, die die Option `count` verwenden. Normalerweise, wenn Sie mit `dd` eine Datei kopieren möchten, die 1 Megabyte groß ist, möchten Sie diese Datei normalerweise als 1 Megabyte sehen, wenn sie fertig kopiert ist. Nehmen wir an, Sie führen den folgenden Befehl aus:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Unsere `backup.img`-Datei ist 10M groß; wir sagen jedoch in diesem Befehl, dass 1M 2 Mal kopiert werden soll, sodass nur 2M kopiert werden, wodurch unsere kopierten Daten unvollständig bleiben. `count` kann in vielen Situationen nützlich sein, aber wenn Sie nur Daten kopieren, können Sie `count` und sogar `bs` weglassen. Wenn Sie Ihre Datenübertragungen wirklich optimieren möchten, dann sollten Sie diese Optionen verwenden.

`dd` ist extrem leistungsfähig; Sie können es verwenden, um Backups von allem zu erstellen, einschließlich ganzer Festplatten, zum Wiederherstellen von Disk-Images und vielem mehr. Seien Sie vorsichtig, dieses leistungsstarke Tool kann einen Preis haben, wenn Sie nicht sicher sind, was Sie tun.

## Exercise

Verwenden Sie den `dd`-Befehl, um ein Backup Ihres Laufwerks zu erstellen und die Ausgabe in eine `.img`-Datei zu schreiben.

## Quiz Question

Was ist die `dd`-Option für die Blockgröße?

## Quiz Answer

bs
