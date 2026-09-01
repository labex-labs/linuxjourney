---
lesson_id: "filesystem-repair"
course_id: "filesystem"
lang: "de"
order_index: 10
title: "Dateisysteme reparieren"
description: "Lerne, Dateisystemschäden zu diagnostizieren und einen typspezifischen Offline-Reparaturablauf mit Sicherungen auszuwählen."
meta_title: "Dateisysteme reparieren – Das Dateisystem"
meta_description: "Lerne, Dateisystemschäden sicher zu diagnostizieren und mit typspezifischen Werkzeugen wie e2fsck oder xfs_repair offline zu bearbeiten."
meta_keywords: "fsck, Dateisystem reparieren, Linux Befehle, Datenträgerfehler, Datenwiederherstellung, e2fsck, xfs_repair"
---

Eine Dateisystemreparatur schreibt Metadaten neu, um die interne Konsistenz wiederherzustellen. Dabei können beschädigte Referenzen oder Daten verworfen werden; bei ausfallender Speicherhardware kann sich der Verlust vergrößern. Behandle eine Reparatur als Wiederherstellungsoperation: Bewahre zuerst Belege und wiederherstellbare Daten und verwende anschließend das für das genaue Dateisystem dokumentierte Werkzeug.

## Vor der Reparatur diagnostizieren

Symptome wie Ein-/Ausgabefehler, schreibgeschützte Neueinhängungen, fehlende Dateien oder fehlgeschlagene Einhängungen beweisen nicht in jedem Fall eine Dateisystembeschädigung. Sammle zunächst schreibgeschützte Belege:

```bash
$ findmnt --target /affected/path
$ lsblk -f
$ journalctl -k -b
```

Prüfe Speicherstapel, Gerätezustand, Kabel oder Netzwerkpfad, RAID-Zustand, Verschlüsselung und kürzliche Ereignisse. Wenn das Gerät ausfällt, können wiederholte Scans seine verbleibende Lebensdauer aufbrauchen. Erstelle soweit möglich mit einem wiederherstellungsorientierten Werkzeug ein Abbild oder einen Klon und arbeite mit der Kopie.

:::single-choice{#filesystem-repair-first-response} Was sollte einer schreibfähigen Dateisystemreparatur vorausgehen, wenn ein Hardwareausfall möglich ist?

::option[Jedes Reparaturwerkzeug wiederholt ausführen, bis eines mit Status null endet.]{#filesystem-repair-repeat-tools explanation="Unpassende Werkzeuge und wiederholte Schreibvorgänge können den Schaden vergrößern."}
::option[Sofort eine neue Partitionstabelle über das Gerät schreiben.]{#filesystem-repair-new-table explanation="Das Überschreiben von Strukturmetadaten zerstört Belege und kann die Wiederherstellung erschweren."}
::option[Wiederherstellbare Daten oder ein Abbild sichern und den Gerätezustand untersuchen.]{#filesystem-repair-preserve-first .correct explanation="Die Reparatur verändert Metadaten, während ausfallende Medien durch wiederholten Zugriff weiter verfallen können."}
:::

## Das genaue Dateisystem und Gerät bestimmen

Ermittle, ob das Dateisystem auf einer Partition, einem logischen Volume, RAID-Gerät, einer verschlüsselten Abbildung oder einem vollständigen Datenträger liegt. Führe einen Prüfer nicht einfach auf `/dev/sda` aus, nur weil eine untergeordnete Partition wie `/dev/sda1` betroffen ist.

Ordne das Ziel mit `lsblk -f`, `blkid`, `findmnt` und Werkzeugen der Speicherebenen zu. Erkannte Signaturen können veraltet sein; gleiche sie deshalb mit bekannter Konfiguration und Sicherungen ab.

:::single-choice{#filesystem-repair-target-layer} Welche Ebene sollte ein ext4-Prüfwerkzeug normalerweise erhalten, wenn ext4 auf `/dev/sda1` gespeichert ist?

::option[Unabhängig von der Partitionstabelle immer `/dev/sda`.]{#filesystem-repair-whole-disk explanation="Der vollständige Datenträger enthält die Partitionstabelle und möglicherweise mehrere untergeordnete Bereiche, nicht direkt die ext4-Instanz."}
::option[`/dev/sda1`, nachdem sie sicher offline ist.]{#filesystem-repair-partition-target .correct explanation="Das Prüfwerkzeug arbeitet auf dem Blockgerät, das dieses Dateisystem direkt enthält."}
::option[`/mnt/data`, während Anwendungen dort weiter schreiben.]{#filesystem-repair-live-mount explanation="Ein Pfadname als Einhängepunkt ist nicht das vom Prüfwerkzeug erwartete Offline-Blockgeräteziel."}
:::

## Das Dateisystem offline nehmen

Die meisten traditionellen Konsistenzprüfer verlangen ein ausgehängtes Dateisystem. Ein eingehängtes Dateisystem verändert sich, während das Werkzeug es liest. Reparaturschreibvorgänge können mit dem Cache-Zustand des Kernels in Konflikt geraten und Beschädigungen verursachen.

Beende abhängige Dienste, hänge verschachtelte Dateisysteme aus, verschiebe Arbeitsverzeichnisse von Prozessen und deaktiviere höhere Ebenen nach Bedarf. Starte für das Root-Dateisystem eine Rettungsumgebung oder verwende den dokumentierten Offline-Prüfmechanismus der Distribution. Bestätige mit `findmnt`, dass das Ziel im relevanten Namespace nicht eingehängt ist.

:::single-choice{#filesystem-repair-mounted-risk} Warum sollte ein Dateisystem normalerweise ausgehängt sein, bevor ein Reparaturwerkzeug hineinschreibt?

::option[Gleichzeitige Aktualisierungen durch Kernel und Prüfwerkzeug können in Konflikt geraten und Metadaten beschädigen.]{#filesystem-repair-concurrent-writes .correct explanation="Eine Offline-Ansicht verhindert, dass sich das Dateisystem während der Reparatur verändert."}
::option[Das Aushängen stellt jede beschädigte Datei automatisch aus der Sicherung wieder her.]{#filesystem-repair-unmount-restores explanation="Das Trennen schafft Konsistenz für die Prüfung, ist aber keine Datenwiederherstellung."}
::option[Dateisystemwerkzeuge können nur Verzeichnisse und niemals Blockgeräte lesen.]{#filesystem-repair-tools-directories explanation="Reparaturwerkzeuge arbeiten normalerweise direkt auf Offline-Blockgeräten."}
:::

## Das dateisystemspezifische Werkzeug verwenden

`fsck` ist eine Oberfläche, die dateisystemspezifische Hilfsprogramme aufrufen kann. Es ist keine universelle Reparatur-Engine. Beispiele verschiedener Abläufe sind `e2fsck` für Ext-Dateisysteme, `xfs_repair` für XFS sowie Btrfs-spezifische Diagnose- und Wiederherstellungswerkzeuge.

Ähnlich benannte Optionen können unterschiedliche Bedeutungen besitzen. Übertrage insbesondere keine `--repair`- oder Force-Optionen aus der Anleitung eines anderen Dateisystems. Lies das installierte Handbuch sowie aktuelle Wiederherstellungsdokumentation des Projekts oder der Distribution. Beginne mit einem nicht verändernden oder diagnostischen Modus, wenn die Implementierung einen verlässlichen anbietet, zeichne die Ausgabe auf und verstehe die vorgeschlagenen Korrekturen.

:::single-choice{#filesystem-repair-fsck-role} Wofür ist `fsck` unter Linux häufig zuständig?

::option[Prüfungen an ein zum Dateisystemtyp passendes Hilfsprogramm weiterleiten.]{#filesystem-repair-fsck-dispatch .correct explanation="Die eigentliche Validierungs- und Reparaturlogik gehört zu formatspezifischen Werkzeugen und Abläufen."}
::option[Jedes Dateisystem vor der Prüfung in ext4 umwandeln.]{#filesystem-repair-fsck-convert explanation="Ein Prüfwerkzeug muss das vorhandene Format bewahren und verstehen."}
::option[Ausgefallene Hardwaresektoren ohne Risiko von Datenverlust reparieren.]{#filesystem-repair-fsck-hardware explanation="Werkzeuge für Dateisystemkonsistenz können weder physische Hardware reparieren noch Datenwiederherstellung garantieren."}
:::

## Prüfen und den Dienst wiederherstellen

Notiere Reparaturwerkzeug, Version, Optionen, Ausgabe und Exit-Status. Wiederhole nach der Reparatur die Prüfungen des Gerätezustands, hänge das Dateisystem soweit angebracht zunächst schreibgeschützt ein, untersuche wichtige Daten und vergleiche sie mit bekannten Sicherungen. Stelle anschließend normale Einhängungen und Dienste schrittweise wieder her und überwache Kernel- und Anwendungsprotokolle.

Ein einhängbares Dateisystem beweist nicht, dass jede Datei korrekt ist. Stelle verlorene oder beschädigte Anwendungsdaten aus Sicherungen wieder her und validiere sie auf Anwendungsebene.

:::single-choice{#filesystem-repair-mountable-proof} Beweist eine erfolgreiche Einhängung nach der Reparatur, dass alle Anwendungsdaten korrekt sind?

::option[Nein; Konsistenzreparatur und Datenvalidierung auf Anwendungsebene sind verschieden.]{#filesystem-repair-not-data-proof .correct explanation="Das Dateisystem kann strukturell einhängbar sein, obwohl Dateien oder Transaktionen fehlen oder beschädigt sind."}
::option[Ja; beim Einhängen wird jede Datei kryptografisch mit einer Sicherung verglichen.]{#filesystem-repair-mount-verifies explanation="Eine gewöhnliche Einhängung führt keinen vollständigen Sicherungsvergleich aus."}
::option[Ja; Reparaturwerkzeuge rekonstruieren alle unbekannten Inhalte automatisch.]{#filesystem-repair-recreates-data explanation="Eine Metadatenreparatur kann beliebige verlorene Benutzerdaten nicht herleiten."}
:::

## Zusammenfassung

Du kannst die Dateisystemreparatur nun als stufenweisen Wiederherstellungsablauf planen.

1. Diagnostiziere Hardware und sichere wiederherstellbare Daten vor Schreibvorgängen.
2. Ordne die genaue, das Dateisystem enthaltende Blockebene zu.
3. Nimm das Dateisystem im relevanten Namespace offline.
4. Verwende das dokumentierte dateisystemspezifische Diagnose- und Reparaturwerkzeug.
5. Validiere Gerätezustand, Dateisystemzustand und Anwendungsdaten getrennt.
