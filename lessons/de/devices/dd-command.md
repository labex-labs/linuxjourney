---
index: 7
lang: "de"
title: "dd"
meta_title: "dd - Geräte"
meta_description: "Entdecken Sie das leistungsstarke dd-Tool unter Linux. Diese Anleitung erklärt, wie Sie den dd Linux-Befehl für effizientes Kopieren von Daten, Festplatten-Imaging und Backups verwenden. Lernen Sie wichtige Optionen wie if, of und bs kennen."
meta_keywords: "dd Befehl, dd linux, dd Tool, Daten kopieren, Festplatten-Imaging, Linux Tutorial, Anfänger, Anleitung, Datensicherung"
---

## Lesson Content

Der Befehl `dd` ist ein vielseitiges und leistungsstarkes Dienstprogramm zum Konvertieren und Kopieren von Daten. Er arbeitet, indem er von einer Eingabedatei oder einem Datenstrom liest und in eine Ausgabedatei oder einen Datenstrom schreibt, was ihn zu einem unverzichtbaren `dd tool` für viele Systemadministrationsaufgaben macht.

### Die dd-Befehlsstruktur verstehen

Im Kern kopiert `dd` Daten Byte für Byte. Betrachten Sie den folgenden Befehl:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

Dieser Befehl kopiert den Inhalt der Datei `backup.img` auf das Blockgerät `/dev/sdb`. Er führt diese Operation durch, indem er die Daten in Blöcken von 1024 Bytes kopiert, bis die gesamte Eingabedatei gelesen wurde.

### Wesentliche dd-Optionen

Das Verhalten des `dd`-Befehls wird durch mehrere Schlüsseloptionen gesteuert:

- `if=file`: Gibt die **Eingabedatei** an. `dd` liest von dieser Datei anstelle der Standardeingabe.
- `of=file`: Gibt die **Ausgabedatei** an. `dd` schreibt in diese Datei anstelle der Standardausgabe.
- `bs=bytes`: Legt die **Blockgröße** fest. `dd` liest und schreibt jeweils diese Anzahl von Bytes. Sie können Suffixe für größere Einheiten verwenden, wie z. B. `k` für Kilobytes (1024 Bytes), `M` für Megabytes und `G` für Gigabytes. Zum Beispiel `bs=1M`.
- `count=number`: Kopiert nur diese angegebene **Anzahl von Blöcken**.

### Verwendung von bs und count zusammen

Die Option `count` ist nützlich, wenn Sie eine bestimmte Datenmenge kopieren müssen. Die insgesamt kopierte Datenmenge ergibt sich aus `bs` multipliziert mit `count`. Wenn Sie beispielsweise den folgenden Befehl für eine 10M-Datei ausführen:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Obwohl `backup.img` 10M groß ist, weist dieser Befehl `dd` an, 2 Blöcke zu je 1M Größe zu kopieren. Infolgedessen werden nur 2M Daten kopiert, was zu einer unvollständigen Übertragung führt. Obwohl `count` in bestimmten Szenarien wertvoll ist, können Sie es oft weglassen, wenn Ihr Ziel darin besteht, eine ganze Datei zu kopieren. Die Optimierung von `bs` kann die Übertragungsgeschwindigkeiten erheblich verbessern, aber die Standardeinstellungen sind oft ausreichend.

### Die Macht und Gefahr von dd

Der Befehl `dd linux` ist extrem leistungsfähig. Sie können ihn verwenden, um Backups ganzer Festplatten zu erstellen, Festplatten-Images wiederherzustellen und Daten sicher zu löschen. Diese Macht birgt jedoch ein Risiko. Ein kleiner Fehler, wie das Vertauschen der Werte für `if` und `of`, kann zu irreversiblen Datenverlusten führen. Überprüfen Sie Ihre Befehle immer sorgfältig, bevor Sie sie ausführen, insbesondere wenn Sie auf ein Gerät wie `/dev/sda` schreiben.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der Datenmanipulation und Festplattenverwaltung in Linux zu festigen:

1. **[Erstellen und Wiederherstellen eines Backups mit tar in Linux](https://labex.io/de/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Üben Sie das Erstellen und Wiederherstellen von Dateisystem-Backups, eine entscheidende Fähigkeit im Zusammenhang mit Datenintegrität und Wiederherstellung, für die auch `dd` verwendet werden kann.
2. **[Verwalten von Linux-Partitionen und Dateisystemen](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Lernen Sie, wie man Festplattenpartitionen und Dateisysteme verwaltet, einschließlich Erstellung, Formatierung und Einhängepunkte, was grundlegende Konzepte sind, wenn man mit Tools wie `dd` für das Disk-Imaging arbeitet.

Diese Labs helfen Ihnen, die Konzepte der Datenverarbeitung und Festplattenoperationen in realen Szenarien anzuwenden und Vertrauen in Systemadministrationsaufgaben aufzubauen.

## Quiz Question

Was ist die `dd`-Option für die Blockgröße? Bitte antworten Sie nur mit Kleinbuchstaben in englischer Sprache.

## Quiz Answer

bs
