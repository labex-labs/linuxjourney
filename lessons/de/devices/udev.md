---
lesson_id: "udev"
course_id: "devices"
lang: "de"
order_index: 5
title: "udev"
description: "Lerne, wie udev Geräteereignisse des Kernels verarbeitet und Richtlinien, Berechtigungen sowie dauerhafte Links anwendet."
meta_title: "udev – Geräte"
meta_description: "Lerne, wie udev Kernel-Ereignisse verarbeitet, Linux-Geräteknoten dynamisch verwaltet und mit udevadm Eigenschaften und Ereignisse untersucht."
meta_keywords: "udev, udevadm, Linux Geräteverwaltung, Gerätedateien, Linux Tutorial, udev Regeln, Linux Anleitung"
---

Der Linux-Kernel meldet Geräteänderungen durch Uevents an den Userspace. Auf vielen aktuellen Distributionen verarbeitet `systemd-udevd` diese Ereignisse mithilfe von udev-Regeln und einer Gerätedatenbank. Zusammen mit dem vom Kernel befüllten `devtmpfs` entstehen daraus Eigentümerschaft, Berechtigungen, Eigenschaften und symbolische Links, die Anwendungen unter und um `/dev` sehen.

## Vom Kernel-Ereignis zur Geräterichtlinie

Wenn ein Gerät hinzugefügt, geändert, verschoben oder entfernt wird, kann udev:

- Attribute aus sysfs und Ereigniseigenschaften lesen
- Richtlinien für Eigentümer, Gruppe und Modus auf einen Geräteknoten anwenden
- stabile symbolische Links wie `/dev/disk/by-id/...` hinzufügen
- Geräte für andere Dienste markieren
- eng begrenzte Hilfsverarbeitung ausführen

Der Kernel bleibt für das eigentliche Gerät und seinen Treiber zuständig. Das Löschen eines Knotens aus `/dev` entfernt keine physische Hardware. Auch das manuelle Erstellen eines Knotens mit `mknod` lässt nicht unterstützte Hardware weder entstehen noch bindet es einen Treiber.

:::single-choice{#udev-kernel-event-input} Was löst bei einer Geräteänderung normalerweise die Verarbeitung durch udev aus?

::option[Eine von APT ausgeführte Aktualisierung des Paketrepositories.]{#udev-apt-refresh explanation="Aktualisierungen von Paketmetadaten stehen in keinem Zusammenhang mit der Verarbeitung aktiver Geräteereignisse."}
::option[Das manuelle Umbenennen jeder Datei unter `/dev` durch einen Benutzer.]{#udev-manual-renaming explanation="Dynamische Richtlinien werden von Kernel-Ereignissen und Regeln gesteuert, nicht durch massenhaftes manuelles Umbenennen."}
::option[Ein Kernel-Uevent, das die Geräteaktion beschreibt.]{#udev-kernel-uevent .correct explanation="Udev empfängt Geräteereignisse vom Kernel und wendet passende Userspace-Regeln an."}
:::

## Speicherorte und Priorität von Regeln

Regeln befinden sich häufig in:

- `/usr/lib/udev/rules.d/` für vom Hersteller oder Paket bereitgestellte Regeln
- `/run/udev/rules.d/` für flüchtige Laufzeitregeln
- `/etc/udev/rules.d/` für lokale Richtlinien des Administrators

Dateien werden in lexikografischer Reihenfolge ihrer Namen verarbeitet. Gleichnamige Dateien in Verzeichnissen höherer Priorität ersetzen gemäß der installierten udev-Implementierung Versionen niedrigerer Priorität. Lokale Regeln sollten einen bewusst gewählten Dateinamen verwenden und stabile Eigenschaften statt Aufzählungsnamen abgleichen.

Eine Regel kann jedes passende Gerät betreffen. Prüfe ihren Geltungsbereich daher sorgfältig. Bearbeite paketierte Regeln nicht direkt, wenn eine lokale Überschreibung oder Ergänzungsregel angebracht ist.

:::single-choice{#udev-local-rules-directory} Welches Verzeichnis ist für dauerhafte lokale udev-Regeln des Administrators vorgesehen?

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="Procfs stellt kein dauerhaftes Verzeichnis für lokale Regeln bereit."}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="Lokale Richtlinien gehören unter `/etc`, getrennt von paketverwalteten Herstellerregeln."}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="`/dev` enthält laufzeitbezogene, geräteseitige Objekte und keine dauerhafte Regelkonfiguration."}
:::

## Ein Gerät mit `udevadm` untersuchen

Frage die udev-Eigenschaften eines vorhandenen Knotens ab:

```bash
$ udevadm info --query=all --name=/dev/sda
```

Verwende einen Knoten, der auf dem aktuellen System existiert. `udevadm info --attribute-walk --name=...` kann Attribute entlang der sysfs-Elternkette anzeigen und so beim Erstellen einer Regel helfen. `udevadm monitor --kernel --udev --property` beobachtet Kernel- und verarbeitete Ereignisse. Die Ausgabe kann Gerätekennungen offenlegen und sollte entsprechend behandelt werden.

:::single-choice{#udev-info-purpose} Was fordert `udevadm info --query=all --name=/dev/sda` an?

::option[Eine zerstörerische Neuerstellung der Partitionstabelle des Datenträgers.]{#udev-info-partition-write explanation="Die Abfrage dient der Untersuchung und formatiert oder partitioniert keinen Speicher."}
::option[Die Installation eines fehlenden Kernel-Treibers aus dem Internet.]{#udev-info-install-driver explanation="Die Untersuchung mit udevadm ist kein Paketdownload."}
::option[Die bekannten udev-Eigenschaften des benannten Geräteknotens.]{#udev-info-properties .correct explanation="Der Befehl info fragt die Gerätedatenbank und zugehörige sysfs-Informationen ab."}
:::

## Regeländerungen vorsichtig anwenden

Das Neuladen von Regeldateien wirkt sich auf die Verarbeitung zukünftiger Ereignisse aus; es baut nicht automatisch den Zustand jedes vorhandenen Geräts neu auf. Das manuelle Auslösen von Ereignissen kann viele Geräte und Dienste betreffen. Grenze das Ziel deshalb ein und verwende die Dokumentation des installierten `udevadm`. Ein Testbefehl kann die Regelauswertung simulieren, bildet aber möglicherweise nicht jede Nebenwirkung eines echten Ereignisses nach.

Sichere lokale Regeln, prüfe ihre Syntax, beobachte ein bekanntes Testgerät und halte einen Wiederherstellungsweg bereit, bevor du Berechtigungen oder Namen änderst. Führe keine lang laufende Arbeit direkt in der udev-Ereignisverarbeitung aus, sondern übertrage sie einem geeigneten Dienst.

:::single-choice{#udev-reload-effect} Was verändert das Neuladen von udev-Regeln in erster Linie?

::option[Wie nachfolgende passende Geräteereignisse verarbeitet werden.]{#udev-future-events .correct explanation="Das Neuladen aktualisiert die Regeln im Arbeitsspeicher; ein Ereignis muss dennoch auftreten oder bewusst ausgelöst werden, damit ein Gerät neu ausgewertet wird."}
::option[Die physische Verkabelung jedes angeschlossenen Geräts.]{#udev-physical-wiring explanation="Das Laden von Softwareregeln kann Hardwareverbindungen nicht verändern."}
::option[Jeden vorhandenen Geräteknoten unabhängig von Ereignissen oder Übereinstimmungen.]{#udev-all-existing explanation="Ein Neuladen allein garantiert keine sofortige Neuauswertung aller vorhandenen Geräte."}
:::

Nutze das Lab [Hardwaregeräte unter Linux erkunden](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861), um `udevadm`-Eigenschaften, sysfs-Pfade und Links unter `/dev` in einer kontrollierten Umgebung einander zuzuordnen.

## Zusammenfassung

Du kannst udev nun zwischen Kernel-Ereignissen und Userspace-Geräterichtlinien einordnen.

1. Ordne Uevents und sysfs-Attribute dem Regelabgleich von udev zu.
2. Trenne die Speicherorte für Hersteller-, Laufzeit- und lokale Regeln.
3. Untersuche Eigenschaften und Ereignisfluss mit `udevadm`.
4. Lade Regeln neu und löse sie nur in einem eng begrenzten, getesteten Umfang aus.
