---
index: 2
lang: "de"
title: "Gerätetypen"
meta_title: "Gerätetypen - Geräte"
meta_description: "Entdecken Sie die verschiedenen Linux-Gerätetypen, einschließlich Zeichen-, Block-, Pipe- und Socket-Geräte. Erfahren Sie, wie Linux Geräte verwaltet, wie Sie eine Gerätedatei mit `ls -l /dev` identifizieren und welche Rolle Haupt- und Neben-Gerätenummern spielen."
meta_keywords: "linux geräte, linux gerätetypen, gerätedatei, zeichengerät, blockgerät, haupt neben nummern, linux für geräte, /dev verzeichnis"
---

## Lesson Content

In Linux ist ein Kernprinzip, dass „alles eine Datei ist“. Diese Philosophie erstreckt sich auf Hardwarekomponenten, die als spezielle Dateien im Dateisystem dargestellt werden. Das Verständnis dieser **Linux-Geräte** und ihrer entsprechenden Dateien ist für die Systemadministration von entscheidender Bedeutung. Beginnen wir mit der Erkundung des Verzeichnisses `/dev`, dem traditionellen Speicherort für jede **Gerätedatei**.

### Erkundung von Linux-Geräten in /dev

Sie können die Dateien im Verzeichnis `/dev` auflisten, um zu sehen, wie das System verschiedene **Linux-Geräte** darstellt.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

Hier ist eine Aufschlüsselung der Spalten von links nach rechts:

- Berechtigungen
- Besitzer
- Gruppe
- Hauptgerätenummer
- Nebengerätenummer
- Zeitstempel
- Gerätebezeichnung

### Identifizierung von Linux-Gerätetypen

Das erste Zeichen in der Berechtigungszeichenfolge der `ls -l`-Ausgabe gibt den Dateityp an. Für eine **Gerätedatei** sehen Sie eines der folgenden Zeichen, was hilft, die spezifischen **Linux-Gerätetypen** zu identifizieren:

- `c` - Zeichen (character)
- `b` - Block (block)
- `p` - Pipe
- `s` - Socket

### Zeichengeräte (Character Devices)

Diese Geräte übertragen Daten zeichenweise. Viele Pseudo-Geräte, die nicht physisch angeschlossene Hardware sind, sondern wesentliche Betriebssystemfunktionen bereitstellen, werden als Zeichengeräte dargestellt. Ein klassisches Beispiel ist `/dev/null`.

### Blockgeräte (Block Devices)

Diese Geräte übertragen Daten in großen, festen Blöcken. Sie werden häufig feststellen, dass Speicherhardware wie Festplatten (`/dev/sda`), SSDs und andere Massenspeicherkomponenten als Blockgeräte dargestellt werden, da sie für den blockbasierten Datenzugriff optimiert sind.

### Pipe-Geräte (Pipe Devices)

Benannte Pipes oder FIFOs (First-In, First-Out) ermöglichen die Prozesskommunikation. Sie verhalten sich wie Zeichengeräte, leiten ihre Ausgabe jedoch an einen anderen Prozess anstatt an ein physisches Gerät weiter.

### Socket-Geräte (Socket Devices)

Socket-Geräte erleichtern ebenfalls die Kommunikation zwischen Prozessen. Im Gegensatz zu Pipes sind sie vielseitiger und können die Kommunikation zwischen mehreren Prozessen unterstützen, sogar über ein Netzwerk hinweg.

### Verständnis der Gerätenummern

Jedes **Linux-Gerät** wird eindeutig durch zwei Zahlen identifiziert: die **Hauptgerätenummer** und die **Nebengerätenummer**. Sie können diese in der `ls`-Ausgabe sehen, durch ein Komma getrennt. Für ein Gerät mit den Nummern **8, 0**:

Die Hauptnummer (8) identifiziert den Treiber, der für das Gerät verantwortlich ist. In diesem Fall wird 8 üblicherweise für SCSI-Festplatten verwendet. Die Nebennummer (0) teilt dem Treiber mit, welche spezifische Instanz des Geräts es ist. Hier repräsentiert 0 die erste Festplatte (`a`).

## Exercise

Um das Gelernte über **Linux-Geräte** anzuwenden, empfehlen wir die folgenden praktischen Übungen. Diese Übungen helfen Ihnen, Vertrauen in die Geräteinteraktion und -verwaltung in realen Szenarien aufzubauen.

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Üben Sie das Erstellen und Verwalten von Festplattenpartitionen und Dateisystemen, die grundlegende Blockgeräte in Linux sind.
2. **[Hardware-Geräte in Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** – Lernen Sie, verschiedene Hardware-Geräte zu identifizieren und zu inspizieren und zu verstehen, wie sie im Verzeichnis `/dev` dargestellt werden.
3. **[Eine Swap-Datei in Linux erstellen und aktivieren](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** – Sammeln Sie praktische Erfahrungen beim Erstellen und Aktivieren einer Swap-Datei, die als virtuelles Speichergerät fungiert.

## Quiz Question

Welches Symbol steht für Zeichengeräte (character devices) im Befehl `ls -l`? (Geben Sie als Antwort den einzelnen kleingeschriebenen englischen Buchstaben an)

## Quiz Answer

c
