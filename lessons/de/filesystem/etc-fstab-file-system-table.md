---
index: 7
lang: "de"
title: "/etc/fstab"
meta_title: "/etc/fstab - Das Dateisystem"
meta_description: "Erfahren Sie, wie Sie die Datei /etc/fstab unter Linux verwenden, um Dateisysteme beim Booten automatisch einzubinden. Diese Anleitung behandelt die fstab-Syntax, die sichere Bearbeitung der etc fstab-Datei und ihre Rolle beim Systemstart."
meta_keywords: "fstab, fstab linux, etc fstab, /etc/fstab, fstab datei, dateisysteme einbinden, Linux boot, fstab tutorial"
---

## Lesson Content

Unter Linux konfigurieren Sie Dateisysteme, die beim Systemstart automatisch eingehängt werden sollen, in einer speziellen Konfigurationsdatei unter `/etc/fstab`. Der Name `fstab` steht für „Filesystem Table“ (Dateisystemtabelle), und diese Datei enthält eine permanente Liste von Dateisystemen, die das System während des Bootvorgangs einhängen soll. Das Verständnis der **fstab linux**-Konfiguration ist eine Schlüsselqualifikation für jeden Systemadministrator.

### Was ist /etc/fstab

Die Datei `/etc/fstab` ist eine Systemkonfigurationsdatei, die alle verfügbaren Festplattenpartitionen und andere Arten von Dateisystemen und Datenquellen definiert, die nicht notwendigerweise auf Festplatten basieren. Das System zieht diese Datei beim Start zurate, um festzustellen, welche Dateisysteme automatisch eingehängt werden sollen.

Hier ist ein Beispiel für eine typische **fstab file**:

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

### Die fstab Dateistruktur

Jede Zeile in der **etc fstab**-Datei repräsentiert ein Dateisystem und enthält sechs Felder, die durch Leerzeichen oder Tabulatoren getrennt sind. Lassen Sie uns aufschlüsseln, was jedes Feld bedeutet:

- **Gerätebezeichner**: Dieser gibt das einzuhängende Gerät an. Moderne Systeme verwenden eine UUID (Universally Unique Identifier), um Probleme zu vermeiden, falls sich der Gerätename (z. B. `/dev/sda1`) ändert.
- **Einhängepunkt (Mount Point)**: Das Verzeichnis im Dateisystem, in das das Gerät eingehängt wird (z. B. `/` oder `/home`).
- **Dateisystemtyp**: Die Art des Dateisystems auf dem Gerät, wie z. B. `ext4`, `xfs`, `btrfs` oder `swap`.
- **Optionen**: Einhängeoptionen, die steuern, wie das Dateisystem eingehängt wird. Häufige Optionen sind `defaults`, `relatime` und `errors=remount-ro`. Eine vollständige Liste finden Sie in der `mount`-Manpage.
- **Dump**: Dieses Feld wird vom `dump`-Dienstprogramm verwendet, um festzustellen, ob ein Dateisystem gesichert werden muss. Ein Wert von `0` bedeutet, dass es ignoriert wird, was eine sichere Standardeinstellung ist.
- **Pass (Prüfnummer)**: Dieses Feld wird von `fsck` verwendet, um die Reihenfolge der Überprüfung der Dateisysteme beim Booten festzulegen. Das Root-Dateisystem (`/`) sollte `1` sein, andere Dateisysteme sollten `2` sein, und ein Wert von `0` bedeutet, dass das Dateisystem nicht überprüft wird.

### Wie man /etc/fstab bearbeitet

Sie können einen Eintrag hinzufügen, indem Sie die Datei `/etc/fstab` direkt mit Root-Rechten in einem Texteditor bearbeiten. Seien Sie äußerst vorsichtig beim Bearbeiten dieser Datei; ein falscher Eintrag in der **fstab** kann verhindern, dass Ihr System korrekt startet. Es ist immer eine gute Vorgehensweise, die Datei vor Änderungen zu sichern. Nachdem Sie Ihre Änderungen gespeichert haben, können Sie diese testen, ohne neu zu starten, indem Sie den Befehl `sudo mount -a` ausführen, der alle in `/etc/fstab` aufgeführten Dateisysteme einhängt.

## Exercise

Übung macht den Meister! Praktische Erfahrung ist entscheidend, um zu verstehen, wie Dateisysteme verwaltet werden und sichergestellt wird, dass sie beim Systemstart korrekt eingehängt werden. Hier sind einige praktische Labs, um Ihr Verständnis für die Linux-Dateisystemverwaltung und die Datei `/etc/fstab` zu festigen:

1. **[Linux-Partitionen und Dateisysteme verwalten](https://labex.io/de/labs/comptia-manage-linux-partitions-and-filesystems-590845)** – Üben Sie das Erstellen von Partitionen, deren Formatierung, das Einhängen und die Konfiguration des permanenten Einhängens mithilfe von `/etc/fstab`.
2. **[Erstellen und Aktivieren einer Swap-Datei in Linux](https://labex.io/de/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** – Lernen Sie die wesentliche administrative Aufgabe des Erstellens und Aktivierens einer Swap-Datei kennen, was oft Einträge in `/etc/fstab` beinhaltet.

Diese Labs helfen Ihnen, die Konzepte des Einhängens und Konfigurierens von Dateisystemen in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Festplattenressourcen unter Linux aufzubauen.

## Quiz Question

Welche Datei wird verwendet, um zu definieren, wie Dateisysteme eingehängt werden sollen? (Bitte geben Sie den vollständigen Pfad an. Die Antwort ist groß-/kleingeschrieben.)

## Quiz Answer

/etc/fstab
