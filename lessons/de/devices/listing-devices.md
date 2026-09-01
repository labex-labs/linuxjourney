---
lesson_id: "listing-devices"
course_id: "devices"
lang: "de"
order_index: 6
title: "lsusb, lspci, lsscsi"
description: "Lerne, USB-Topologie, PCI-Funktionen, Geräte der SCSI-Schicht und ihre aktiven Treiber zu untersuchen."
meta_title: "lsusb, lspci, lsscsi – Geräte"
meta_description: "Lerne, USB-, PCI- und SCSI-Hardware unter Linux mit lsusb, lspci und lsscsi zu untersuchen und die Ergebnisse mit Treibern und Kernelmeldungen abzugleichen."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, USB Geräte auflisten, PCI Geräte auflisten, SCSI Geräte auflisten, Linux Hardware"
---

Linux bietet bus- und subsystembezogene Inventarwerkzeuge. Jeder Befehl zeigt eine andere Ansicht. Verknüpfe deshalb Kennungen, Topologie, Treiber, sysfs-Pfade und Protokolle, statt von einer einzigen vollständigen Hardwareliste auszugehen.

## USB-Geräte untersuchen

`lsusb` listet Geräte auf, die über das USB-Subsystem sichtbar sind:

```bash
$ lsusb
```

Die Ausgabe enthält normalerweise Bus- und Gerätenummer, ein Paar aus Hersteller- und Produktkennung sowie eine Beschreibung aus der lokalen USB-ID-Datenbank. Die numerische Bus-/Geräteadresse kann sich nach dem erneuten Anschließen oder Neustarten ändern und darf nicht als dauerhafte Identität behandelt werden.

Zeige Beziehungen zwischen Controller, Hub, Port, Schnittstelle, Treiber und Geschwindigkeit an:

```bash
$ lsusb -t
```

Eine ausführliche Ausgabe der Deskriptoren ist verfügbar, doch manche Angaben erfordern erhöhte Leseberechtigungen. Vergib keine umfassenden USB-Geräteberechtigungen, nur damit ein Untersuchungsbefehl weniger Meldungen ausgibt.

:::single-choice{#listing-devices-usb-tree} Welcher Befehl zeigt USB-Geräte als Topologiebaum an?

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="Dieser Befehl listet PCI-Funktionen und Kernel-Treiberinformationen statt der USB-Topologie auf."}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="Dies ist nicht der hier vorgestellte Befehl für den USB-Baum."}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="Die Baumoption zeigt Geräte unter Controllern und Hubs einschließlich Port- und Schnittstellenbeziehungen."}
:::

## PCI-Funktionen untersuchen

`lspci` listet Funktionen auf, die auf PCI- und PCI-Express-Bussen erkannt wurden:

```bash
$ lspci
```

Interne und extern angeschlossene PCIe-Geräte können Grafik-, Netzwerk-, Speicher-, USB-, Audio- und Bridge-Controller umfassen. Zeige den verwendeten Kernel-Treiber und infrage kommende Module an:

```bash
$ lspci -k
```

Das Erscheinen eines PCI-Controllers in dieser Liste beweist nicht, dass jedes dahinterliegende Gerät initialisiert oder funktionsfähig ist. Prüfe bei der Fehlersuche die Treiberbindung und Kernel-Protokolle.

:::single-choice{#listing-devices-pci-driver} Welcher Befehl ergänzt eine PCI-Auflistung um Kernel-Treiberinformationen?

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="Die Option `-k` zeigt für jedes PCI-Gerät den aktiven Kernel-Treiber und geeignete Module an."}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="Dieser Befehl beschreibt die USB-Hierarchie und Schnittstellentreiber."}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="Dieser Befehl meldet Blockgeräte- und Dateisystemfelder, nicht die PCI-Treiberbindung."}
:::

## Geräte der SCSI-Schicht untersuchen

`lsscsi` listet Geräte auf, die über die mittlere SCSI-Schicht von Linux dargestellt werden:

```bash
$ lsscsi
```

Dazu können echte SCSI-Geräte sowie SATA-, USB-Speicher- oder virtuelle Datenträger gehören, die über SCSI-kompatible Schichten bereitgestellt werden. NVMe-Namespaces gehören normalerweise zu einem anderen Subsystem und werden von `lsscsi` nicht vollständig inventarisiert.

Verwende für eine speicherbezogene Hierarchie mit vielen Blockgerätetypen zusätzlich `lsblk`:

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope} Was listet `lsscsi` in erster Linie auf?

::option[Ausschließlich sämtliche NVMe-Namespaces und -Controller.]{#listing-devices-only-nvme explanation="NVMe verwendet ein eigenes Subsystem und eigene Werkzeuge, auch wenn verwandte Blockansichten an anderer Stelle erscheinen können."}
::option[Nur Dateien, deren Namen mit `.scsi` enden.]{#listing-devices-scsi-extension explanation="Der Befehl fragt Kernel-Geräteschnittstellen und keine Dateinamenerweiterungen ab."}
::option[Geräte, die über die mittlere SCSI-Schicht von Linux dargestellt werden.]{#listing-devices-scsi-mid-layer .correct explanation="Der Befehl meldet SCSI-Hosts, Targets, logische Einheiten und, soweit vorhanden, zugehörige Geräteknoten."}
:::

## Inventarergebnisse auswerten

Beschreibungen stammen häufig aus lokalen ID-Datenbanken und können allgemein oder veraltet sein. Ein aufgelistetes Gerät kann ohne funktionierenden Treiber sein, und eine virtualisierte Umgebung kann emulierte oder paravirtuelle Hardware bereitstellen. Gleiche die Ergebnisse abhängig von Berechtigungen und Fragestellung mit `udevadm info`, sysfs, `lsblk`, Netzwerkwerkzeugen und `journalctl -k` oder `dmesg` ab.

Die Dienstprogramme können getrennt paketiert sein, üblicherweise in Paketen wie `usbutils`, `pciutils` und `lsscsi`. Fehlt ein Befehl, installiere ihn über den Paketmanager der Distribution, statt unbekannte Ersatzprogramme herunterzuladen.

:::single-choice{#listing-devices-listed-not-working} Beweist das Erscheinen eines Geräts in `lspci`, dass sein Treiber aktiv ist und richtig funktioniert?

::option[Nein; prüfe zusätzlich Treiberbindung und relevante Kernelmeldungen.]{#listing-devices-needs-correlation .correct explanation="Die Aufzählung belegt, dass eine PCI-Funktion sichtbar ist, nicht dass ihre weitergehende Initialisierung erfolgreich war."}
::option[Ja; die PCI-Aufzählung führt einen vollständigen Funktionstest aus.]{#listing-devices-complete-test explanation="Die Auflistung übt nicht jede Hardwarefunktion aus und überprüft kein Dienstverhalten."}
::option[Ja; `lspci` installiert automatisch einen geeigneten Treiber.]{#listing-devices-installs-driver explanation="Der Befehl ist ein Inventarwerkzeug und installiert keine Treiberpakete."}
:::

Nutze das Lab [Hardwaregeräte unter Linux erkunden](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861), um diese Subsystemansichten auf einem kontrollierten Host zu vergleichen.

## Zusammenfassung

Du kannst nun einen Inventarbefehl passend zum betreffenden Gerätesubsystem auswählen.

1. Verwende `lsusb` und `lsusb -t` für USB-Identität und -Topologie.
2. Verwende `lspci -k` für PCI-Funktionen und Treiberbindung.
3. Verwende `lsscsi` für Geräte der SCSI-Schicht und `lsblk` für die Blocktopologie.
4. Gleiche die Aufzählung mit Treibern, sysfs und Kernelmeldungen ab.
