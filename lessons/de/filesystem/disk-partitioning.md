---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "de"
order_index: 4
title: "Datenträger partitionieren"
description: "Lerne einen prüfungsorientierten Ablauf zum Untersuchen, Erstellen und Ändern von Partitionsgrenzen mit `parted`."
meta_title: "Datenträger partitionieren – Das Dateisystem"
meta_description: "Lerne Linux-Datenträger sicher mit parted zu partitionieren. Untersuche Ziele, erstelle Einträge und ändere Partitionsgrenzen in der richtigen Reihenfolge."
meta_keywords: "Linux Datenträger partitionieren, parted Befehl, sudo parted -l, GParted, fdisk, Partition erstellen, Partition vergrößern, Partition verkleinern"
---

Das Bearbeiten von Partitionen verändert die Karte, die Speichergrenzen definiert. Ein falsches Gerät oder eine falsche Start- beziehungsweise Endposition kann vorhandene Daten unzugänglich machen oder wichtige Metadaten überschreiben. Übe ausschließlich auf einem entbehrlichen virtuellen Datenträger und halte vor Änderungen an wertvollem Speicher eine getrennt geprüfte Sicherung vor.

## Ein Werkzeug auswählen

Verbreitete Werkzeuge sind:

- `fdisk`, ein Terminal-Partitionierungswerkzeug aus util-linux mit Unterstützung für MBR und GPT
- `parted`, ein Terminal- und skriptfähiges Werkzeug für GPT, MBR und andere Tabellenformate
- `gdisk`, ein interaktives, auf GPT ausgerichtetes Werkzeug
- GParted, eine grafische Oberfläche für Partitionen und Dateisysteme

Die Unterstützung der Werkzeuge entwickelt sich weiter. Verwende deshalb das lokale Handbuch und die Distributionsdokumentation. Eine grafische Oberfläche macht zerstörerische Operationen nicht sicher; sie verändert dieselben Datenträgermetadaten.

:::single-choice{#disk-partitioning-fdisk-gpt}
Welche Aussage über aktuelles Linux-`fdisk` trifft zu?

::option[Es unterstützt MBR- und GPT-Partitionstabellen.]{#disk-partitioning-fdisk-supports-gpt .correct explanation="Aktuelles util-linux fdisk kann unter anderem DOS-/MBR- und GPT-Strukturen bearbeiten."}
::option[Es kann ausschließlich GPT und niemals MBR bearbeiten.]{#disk-partitioning-fdisk-only-gpt explanation="Das auf GPT ausgerichtete `gdisk` entspricht dieser Beschreibung eher; fdisk unterstützt mehrere Label-Typen."}
::option[Es erstellt Dateisysteme, kann aber keine Partitionseinträge bearbeiten.]{#disk-partitioning-fdisk-filesystem-only explanation="Sein Hauptzweck ist das Anzeigen und Bearbeiten von Partitionstabellen."}
:::

## Das Ziel identifizieren und stilllegen

Beginne mit einem schreibgeschützten Inventar:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

Bestätige das vollständige Gerät anhand dauerhafter Identität, Modell, Seriennummer, Größe, Transport und Topologie – nicht nur anhand von `/dev/sdX`. Ermittle anschließend jeden Verbraucher: eingehängte Dateisysteme, Swap, LVM, RAID, Verschlüsselung, Container, virtuelle Maschinen, Datenbanken und offene Dateideskriptoren.

Hänge alle betreffenden Ebenen gemäß ihren dokumentierten Verfahren aus oder deaktiviere sie. Bearbeite die Partitionstabelle des laufenden Systemdatenträgers nicht nur deshalb, weil sich das Werkzeug erfolgreich öffnen lässt. Zeichne die vorhandene Tabelle in wiederherstellbarer Form auf und bestätige, dass deine Sicherung in einer anderen Ausfalldomäne liegt.

:::single-choice{#disk-partitioning-target-identity}
Warum reicht ein Gerätename wie `/dev/sdb` als einzige Zielprüfung nicht aus?

::option[Linux stellt niemals vollständige Datenträger unter `/dev` bereit.]{#disk-partitioning-no-whole-disks explanation="Vollständige Datenträger besitzen häufig Blockgeräteknoten unter `/dev`."}
::option[Aufzählungsnamen können sich bei Änderungen an Geräten oder Topologie ändern.]{#disk-partitioning-enumeration-changes .correct explanation="Ein Buchstabe wird anhand der Erkennungsreihenfolge vergeben und kann in einer späteren Sitzung einen anderen Datenträger bezeichnen."}
::option[Partitionierungswerkzeuge akzeptieren ausschließlich Dateisystem-UUIDs als Operanden.]{#disk-partitioning-only-uuid explanation="Partitionierungswerkzeuge arbeiten normalerweise nach erfolgter Identitätsprüfung mit dem Pfad eines vollständigen Blockgeräts."}
:::

## Ein Gerät mit `parted` untersuchen

Öffne das ausdrücklich geprüfte vollständige Gerät:

```bash
$ sudo parted /dev/GEPRUEFTER-DATENTRAEGER
```

Wähle anschließend konsistente Anzeigeeinheiten und gib die Tabelle aus:

```text
(parted) unit MiB
(parted) print free
```

`print free` zeigt vorhandene Einträge und nicht zugewiesene Bereiche. Parted-Befehle können Datenträgermetadaten sofort aktualisieren, statt auf einen abschließenden Speichervorgang zu warten. Behandle die interaktive Eingabeaufforderung daher als aktiven Schreibzugriff.

:::single-choice{#disk-partitioning-print-free}
Was hilft `print free` in `parted` anzuzeigen?

::option[Dateien, die zum sicheren Verkleinern jedes Dateisystems gelöscht werden können.]{#disk-partitioning-free-files explanation="Parted liest die Partitionsstruktur und nicht die Dateizuweisung innerhalb eines Dateisystems."}
::option[Jede auf entfernten Systemen gespeicherte Sicherung.]{#disk-partitioning-remote-backups explanation="Das Inventar entfernter Sicherungen liegt außerhalb der Aufgaben eines Partitionierungswerkzeugs."}
::option[Vorhandene Partitionseinträge und nicht zugewiesene Bereiche.]{#disk-partitioning-free-regions .correct explanation="Die Ansicht hilft, Grenzen anhand der aktuellen Tabelle und verbleibender Lücken auszuwählen."}
:::

## Einen Partitionseintrag erstellen

Die genaue Syntax von `mkpart` hängt vom Tabellentyp ab. Ein GPT-Beispiel in MiB-Einheiten sieht so aus:

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

Dadurch entsteht ein Partitionseintrag mit Name, vorgeschlagenem Inhaltstyp, Start und Ende. Es wird **kein** ext4-Dateisystem erstellt. Das Formatieren ist ein getrennter, zerstörerischer Schritt, der erst erfolgt, nachdem der Kernel die beabsichtigte neue Partition erkennt und ihre Identität geprüft wurde.

Nutze die vom Werkzeug empfohlene Ausrichtung und verstehe, ob Endpunkte eingeschlossen und wie sie gerundet werden. Prüfe das Ergebnis mit `print` und `lsblk`; gehe nicht davon aus, dass eine angeforderte Dezimalgrenze exakt gespeichert wurde.

:::single-choice{#disk-partitioning-mkpart-effect}
Was erstellt `mkpart` von `parted`?

::option[Ein eingehängtes ext4-Dateisystem mit einem Home-Verzeichnis.]{#disk-partitioning-mounted-filesystem explanation="Formatieren und Einhängen sind getrennte Operationen nach der Partitionserstellung."}
::option[Eine vollständige Sicherung des vorherigen Partitionsinhalts.]{#disk-partitioning-automatic-backup explanation="Partitionierungswerkzeuge erstellen nicht automatisch eine Wiederherstellungssicherung."}
::option[Einen Partitionstabelleneintrag, ohne ein Dateisystem zu formatieren.]{#disk-partitioning-entry-only .correct explanation="Das Dateisystemtyp-Argument beeinflusst Partitionsmetadaten, führt aber kein `mkfs` aus."}
:::

## Grenzen und Inhalte in der Größe ändern

`resizepart NUMBER END` verschiebt ausschließlich die Endgrenze einer Partition. Der Befehl ändert nicht die Größe des darin gespeicherten Dateisystems oder einer anderen Struktur.

Die Reihenfolge ist entscheidend:

- Zum Vergrößern erweiterst du zuerst die enthaltende Partition oder das logische Gerät und anschließend das Dateisystem mit seinem eigenen unterstützten Werkzeug.
- Zum Verkleinern prüfst du zunächst, ob das Dateisystem Verkleinern unterstützt, verkleinerst es unter Beachtung seiner Offline-/Online-Anforderungen und reduzierst erst danach die enthaltende Grenze, ohne das neue Ende zu unterschreiten.

Manche Dateisysteme lassen sich nicht verkleinern. Verschlüsselung, LVM, RAID und verschachtelte Strukturen fügen weitere geordnete Ebenen hinzu. Der Kernel kann sich außerdem weigern, eine geänderte Tabelle bei beschäftigten Geräten neu einzulesen, sodass ein kontrollierter Neustart nötig wird, bevor die neue Struktur nutzbar ist.

:::single-choice{#disk-partitioning-shrink-order}
Welche Reihenfolge verhindert bei einem verkleinerbaren Dateisystem das Abschneiden aktiver Dateisystemdaten?

::option[Zuerst die Partition verkleinern und danach prüfen, ob das Dateisystem hineinpasst.]{#disk-partitioning-shrink-partition-first explanation="Das frühzeitige Verkürzen des Containers kann Dateisystemstrukturen und Daten abschneiden."}
::option[Zuerst das Dateisystem verkleinern und danach die Grenze seiner enthaltenden Partition reduzieren.]{#disk-partitioning-shrink-filesystem-first .correct explanation="Der Inhalt muss in den kleineren Bereich passen, bevor das äußere Blockgerät verkürzt wird."}
::option[Die Partitionstabelle löschen und vom Dateisystem neu erstellen lassen.]{#disk-partitioning-delete-table explanation="Ein Dateisystem baut beim gewöhnlichen Verkleinern keine sichere Partitionstabelle neu auf."}
:::

Nutze das Lab [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) auf dem dafür vorgesehenen zweiten virtuellen Datenträger; ersetze ihn nicht durch einen Hostdatenträger.

## Zusammenfassung

Du kannst die Partitionsbearbeitung nun als geschichtete, zerstörerische Speicheroperation beschreiben.

1. Wähle ein Werkzeug, das die tatsächliche Tabelle und den Arbeitsablauf unterstützt.
2. Prüfe die dauerhafte Datenträgeridentität und deaktiviere jeden Verbraucher.
3. Untersuche Einheiten, Einträge und freie Bereiche vor Schreibvorgängen.
4. Denke daran, dass `mkpart` kein Dateisystem erstellt.
5. Ändere die Größe innerer Inhalte und äußerer Grenzen in der sicheren Reihenfolge.
