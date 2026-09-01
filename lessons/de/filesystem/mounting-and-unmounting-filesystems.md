---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "de"
order_index: 6
title: "mount und umount"
description: "Lerne, Dateisysteme mit geprüften Quellen und Einhängepunkten anzuhängen, zu untersuchen und sicher zu trennen."
meta_title: "mount und umount – Das Dateisystem"
meta_description: "Lerne, Dateisysteme unter Linux mit mount und umount sicher ein- und auszuhängen, UUIDs zu verwenden und beschäftigte Einhängungen zu untersuchen."
meta_keywords: "mount, umount, sudo umount, Linux aushängen, Dateisystem einhängen, UUID, Einhängepunkt, busy filesystem"
---

Beim Einhängen wird ein Dateisystem mit einem Verzeichnis im sichtbaren Namensraum verbunden. Die Quelle kann ein Blockgerät, eine Netzwerkfreigabe, ein virtuelles Dateisystem, eine Bind-Quelle oder ein anderes implementierungsspezifisches Objekt sein. Das Zielverzeichnis heißt Einhängepunkt.

## Einen Einhängepunkt vorbereiten und untersuchen

Erstelle ein bewusst benanntes Verzeichnis, wenn die lokale Richtlinie es vorsieht:

```bash
$ sudo mkdir -p /mnt/mydrive
```

Untersuche es vor dem Einhängen:

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

Das Einhängen auf einem nicht leeren Verzeichnis verbirgt dessen vorhandene Einträge hinter dem neuen Dateisystem, bis dieses ausgehängt wird; die Einträge werden nicht gelöscht. Das kann Anwendungen verwirren und unsichtbar Speicherplatz belegen. Verwende deshalb einen leeren, eigens vorgesehenen Einhängepunkt.

:::single-choice{#mount-umount-nonempty-target} Was geschieht mit vorhandenen Dateien eines Verzeichnisses, wenn dort ein anderes Dateisystem eingehängt wird?

::option[Sie werden automatisch in das neue Dateisystem kopiert.]{#mount-umount-copied-files explanation="Das Einhängen verändert die Verbindung im Namensraum und verschiebt keine Verzeichnisinhalte."}
::option[Sie werden vom Kernel dauerhaft gelöscht.]{#mount-umount-erased-files explanation="Die Dateien erscheinen nach dem Aushängen normalerweise wieder, weil sie nur verdeckt und nicht gelöscht wurden."}
::option[Sie werden bis zum Trennen der Einhängung verborgen.]{#mount-umount-hidden-files .correct explanation="Das darunterliegende Verzeichnis bleibt bestehen, doch die Pfadauflösung wechselt in das eingehängte Dateisystem."}
:::

## Ein geprüftes Dateisystem einhängen

Hänge die Quelle nach Prüfung ihrer Identität, des erkannten Typs und des erwarteten Inhalts ausdrücklich ein:

```bash
$ sudo mount -t ext4 /dev/GEPRUEFTE-PARTITION /mnt/mydrive
```

Die Option `-t` gibt die Dateisystemimplementierung an. Mount kann den Typ häufig erkennen, doch ein ausdrücklicher Typ und geprüfte Optionen machen die Absicht deutlicher. Erwäge für nicht vertrauenswürdige oder wechselbare Inhalte einschränkende Optionen wie `ro`, `nosuid`, `nodev` und `noexec`, sofern sie zur Arbeitslast passen. Jede besitzt Grenzen und ist keine vollständige Sandbox.

Prüfe, was tatsächlich eingehängt ist:

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Einhängungen sind an einen Namespace gebunden. Eine in einem Container oder privaten Dienst-Namespace erzeugte Einhängung ist in der Ansicht eines anderen Prozesses möglicherweise nicht sichtbar.

:::single-choice{#mount-umount-mount-role} Was bewirkt der Befehl `mount` in diesem Arbeitsablauf?

::option[Er erstellt ein neues Dateisystem und löscht die Quelle.]{#mount-umount-format-source explanation="Das Erstellen eines Dateisystems ist eine getrennte zerstörerische `mkfs`-Operation."}
::option[Er verbindet eine Dateisystemquelle mit einem Verzeichnis in einem Mount-Namespace.]{#mount-umount-attach-filesystem .correct explanation="Die Pfadauflösung unterhalb des Ziels wechselt anschließend in das verbundene Dateisystem."}
::option[Er verändert die Partitionsgrenzen des Datenträgers.]{#mount-umount-change-partitions explanation="Die Bearbeitung der Partitionstabelle ist vom Einhängen in den Namensraum getrennt."}
:::

## Dateisystem-UUIDs verwenden

Aufzählungsnamen wie `/dev/sdb2` können sich ändern. Ermittle Dateisystemkennungen mit:

```bash
$ lsblk -f
$ sudo blkid
```

Hänge anschließend ein geprüftes Dateisystem anhand seiner UUID ein:

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

Eine UUID bezeichnet das Dateisystem und nicht zwangsläufig den physischen Datenträger. Durch Neuformatierung ändert sie sich, während sie beim Klonen dupliziert werden kann. Prüfe ihre Eindeutigkeit, bevor du Original und Klon gleichzeitig mit demselben System verbindest.

:::single-choice{#mount-umount-uuid-benefit} Warum ist eine Dateisystem-UUID für dauerhafte Konfigurationen häufig besser geeignet als `/dev/sdX`?

::option[Sie verhindert jeden zukünftigen Ausfall von Speichergeräten.]{#mount-umount-uuid-no-failure explanation="Eine Kennung bietet weder Redundanz noch Integritätsreparatur oder Sicherung."}
::option[Sie garantiert, dass geklonte Dateisysteme verschiedene Kennungen besitzen.]{#mount-umount-uuid-clone-unique explanation="Ein Klon auf Blockebene kann die UUID kopieren und eine Kollision erzeugen."}
::option[Sie ist an die Dateisystemidentität statt an die aktuelle Aufzählungsreihenfolge gebunden.]{#mount-umount-uuid-identity .correct explanation="Der Blockgerätepfad kann sich ändern, während die Dateisystemmetadaten ihre UUID behalten."}
:::

## Sicher aushängen

Trenne das Dateisystem anhand des genauen Einhängepunkts:

```bash
$ sudo umount /mnt/mydrive
```

Der Befehl heißt `umount`, ohne das erste `n`. Ein erfolgreiches Aushängen trennt das Dateisystem, nachdem der Kernel erforderliche Schreibvorgänge abgeschlossen hat und keine Referenzen den Vorgang verhindern. Bestätige die Trennung anschließend mit `findmnt`, bevor du den Speicher entfernst.

Ein erfolgreiches Aushängen ist bei Wechselmedien nicht immer der letzte Schritt zum sicheren Entfernen. Desktop-Speicherstapel können eine Auswurf- oder Ausschaltaktion anbieten, die Geräte-Caches leert und ein USB-Gerät deaktiviert. Folge dem Ablauf der Plattform und Hardware.

:::single-choice{#mount-umount-command-name} Welcher Befehl trennt `/mnt/mydrive`?

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount` trennt das am angegebenen Ziel eingehängte Dateisystem."}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="Im Namen des Standardbefehls fehlt das erste `n`."}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="Mkfs erstellt Dateisystemstrukturen und darf nicht zum Trennen verwendet werden."}
:::

## Ein beschäftigtes Dateisystem untersuchen

Das Aushängen schlägt fehl, wenn im Namespace noch aktive Referenzen vorhanden sind, etwa offene Dateien, das Arbeitsverzeichnis eines Prozesses, verschachtelte Einhängungen, Swap oder andere Speicherebenen. Untersuche die Ursache, statt den Vorgang sofort zu erzwingen:

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

Bewege Shells aus dem Baum heraus, beende die verantwortliche Anwendung geordnet und hänge untergeordnete Einhängungen vor dem Elternknoten aus. Verzögertes Aushängen und Force-Optionen besitzen besondere Semantik und können aktive Referenzen zurücklassen oder Datenverlust verursachen. Verwende sie nur mit dokumentierter Begründung für die Wiederherstellung.

:::single-choice{#mount-umount-busy-cause} Welche Bedingung kann dazu führen, dass `umount` ein beschäftigtes Dateisystem meldet?

::option[Der Name des Einhängepunktverzeichnisses enthält Kleinbuchstaben.]{#mount-umount-lowercase explanation="Die Groß-/Kleinschreibung eines Pfads erzeugt für sich allein keine aktive Dateisystemreferenz."}
::option[Ein Prozess besitzt sein aktuelles Arbeitsverzeichnis innerhalb der Einhängung.]{#mount-umount-cwd-busy .correct explanation="Der Prozess hält eine Referenz in das eingehängte Dateisystem und verhindert dadurch die gewöhnliche Trennung."}
::option[Die Dateisystem-UUID ist länger als der Gerätename.]{#mount-umount-uuid-length explanation="Die Länge der Kennungszeichenfolge steht in keinem Zusammenhang mit der Beschäftigt-Prüfung."}
:::

Nutze das Lab [Linux-Partitionen und Dateisysteme verwalten](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845), um auf dem dafür vorgesehenen entbehrlichen Speicher zu üben.

## Zusammenfassung

Du kannst Dateisysteme nun mit überprüfbarem Umfang verbinden und trennen.

1. Verwende einen leeren, eigens vorgesehenen Einhängepunkt.
2. Prüfe Quelle, Typ, Optionen und die entstandene Einhängung.
3. Bevorzuge eine eindeutige Dateisystemkennung für dauerhafte Verweise.
4. Hänge anhand des Ziels aus und bestätige die Trennung vor dem Entfernen.
5. Untersuche aktive Referenzen, statt ein beschäftigtes Aushängen zu erzwingen.
