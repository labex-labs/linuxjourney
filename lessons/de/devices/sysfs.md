---
lesson_id: "sysfs"
course_id: "devices"
lang: "de"
order_index: 4
title: "sysfs"
description: "Lerne, wie sysfs das aktive Geräte-, Treiber-, Bus- und Klassenmodell des Linux-Kernels unter `/sys` bereitstellt."
meta_title: "sysfs – Geräte"
meta_description: "Erkunde sysfs als virtuelles Linux-Dateisystem unter /sys. Lerne Gerätehierarchien und Attribute kennen und grenze /sys von Geräteknoten unter /dev ab."
meta_keywords: "sysfs, was ist sysfs, /sys, Linux /sys, virtuelles Dateisystem, Linux Geräte, Kernel Objekte, /dev"
---

`sysfs` ist ein virtuelles Dateisystem, das normalerweise unter `/sys` eingehängt ist. Es stellt Kernel-Objekte und ihre Beziehungen durch Verzeichnisse, symbolische Links und kleine Attributdateien dar. Werkzeuge und Manager zur Geräteerkennung verwenden es, um das aktuelle Gerätemodell des Kernels zu verstehen.

## Im Gerätemodell navigieren

Wichtige Ansichten der obersten Ebene sind:

- `/sys/devices/`: die physische und logische Gerätehierarchie
- `/sys/class/`: nach Funktionsklasse gruppierte Geräte, beispielsweise Block- oder Netzwerkgeräte
- `/sys/bus/`: Busse mit ihren Geräten und Treibern
- `/sys/block/`: eine praktische Ansicht der Blockgeräte
- `/sys/dev/`: nach Major- und Minor-Nummern von Zeichen- oder Blockgeräten indizierte Links

Viele Einträge außerhalb von `/sys/devices` sind symbolische Links in die maßgebliche Hierarchie. Löse einen Link mit `readlink -f` auf, wenn du den tatsächlichen Elternpfad benötigst:

```bash
$ readlink -f /sys/class/block/sda
```

Der Beispielname ist auf Systemen mit anderen Speicherschnittstellen möglicherweise nicht vorhanden.

:::single-choice{#sysfs-canonical-device-tree}
Welcher sysfs-Unterbaum enthält die hauptsächliche Gerätehierarchie des Kernels?

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="Sysfs ist kein Speicherort für Authentifizierungsgeheimnisse von Benutzern."}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="Der Unterbaum devices stellt die Eltern-Kind-Topologie der Geräte dar; Klassen- und Busansichten verweisen dorthin."}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="Den Zustand installierter Pakete verwalten die Paketwerkzeuge der Distribution und nicht dieser sysfs-Pfad."}
:::

## Attribute lesen

Attributdateien stellen einzelne Werte oder Steuerelemente bereit. Für ein Blockgerät können beispielsweise folgende Attribute vorhanden sein:

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev` meldet die Major- und Minor-Gerätenummern. `ro` zeigt das Schreibschutzkennzeichen des Blockgeräts. Bei Linux-Blockgeräten wird `size` üblicherweise in 512-Byte-Sektoren ausgedrückt, unabhängig von der physischen Sektorgröße des Geräts. Schlage Einheit und Bedeutung eines konkreten Attributs immer in der Kernel-ABI-Dokumentation nach.

:::single-choice{#sysfs-dev-attribute}
Was enthält das sysfs-Attribut `dev` eines Blockgeräts normalerweise?

::option[Jede aktuell auf dem Gerät gespeicherte Datei.]{#sysfs-file-list explanation="Ein Dateisystem-Verzeichnisbaum ist nicht in dieses kleine Geräteattribut eingebettet."}
::option[Den Paketnamen, mit dem die Hardware installiert wurde.]{#sysfs-package-name explanation="Hardware wird nicht als Paket installiert, das durch das Attribut `dev` bezeichnet wird."}
::option[Seine Major- und Minor-Gerätenummern.]{#sysfs-major-minor .correct explanation="Das Attribut verbindet das sysfs-Objekt mit der entsprechenden Identität des Blockgeräts."}
:::

## `/sys` und `/dev` in Beziehung setzen

`/dev` enthält Knoten, die Anwendungen für Geräte-Ein-/Ausgabe öffnen. `/sys` stellt Objektbeziehungen, Eigenschaften, Zustand und ausgewählte Steuerelemente bereit. Ein Blockgeräteknoten wie `/dev/sda` kann `/sys/dev/block/8:0` zugeordnet werden; dieser Link wird zum betreffenden sysfs-Objekt aufgelöst.

Die beiden Schnittstellen ergänzen sich. Keine von ihnen enthält für sich allein ein vollständiges Inventar aller Hardwareeigenschaften, und ein Gerät kann während der Untersuchung verschwinden.

:::single-choice{#sysfs-versus-dev}
Welche Aussage unterscheidet `/sys` richtig von `/dev`?

::option[`/sys` speichert Benutzerdokumente, `/dev` Paketarchive.]{#sysfs-dev-user-files explanation="Keines der beiden Verzeichnisse besitzt diese Rollen zur gewöhnlichen Datenspeicherung."}
::option[`/sys` stellt Attribute von Kernel-Objekten bereit; `/dev` bietet Geräteknoten für Ein-/Ausgabe.]{#sysfs-dev-distinction .correct explanation="Sysfs bildet Objekte und Steuerelemente ab, während Geräteknoten Operationen an Zeichen- oder Blocktreiber weiterleiten."}
::option[Beide sind statische Listen, die einmalig bei der Installation angelegt werden.]{#sysfs-dev-static explanation="Ihr sichtbarer Zustand ändert sich, wenn Geräte und Kernel-Objekte erscheinen oder verschwinden."}
:::

## Attribute sicher schreiben

Einige sysfs-Attribute sind beschreibbar und können Energiezustand, Treiberbindung, Warteschlangenverhalten, Geräteautorisierung, LEDs oder andere aktive Steuerelemente verändern. Ein erfolgreicher Textschreibvorgang kann sich unmittelbar auf Hardware oder Dienste auswirken; er entspricht nicht dem Bearbeiten einer dauerhaften Konfigurationsdatei.

Lies die dokumentierte ABI und den aktuellen Wert, ermittle, wie die Einstellung dauerhaft vorgenommen werden soll, und teste nur auf einem autorisierten System. Ändere unter `/sys` niemals rekursiv Berechtigungen und schreibe dort keine geratenen Werte.

:::single-choice{#sysfs-write-risk}
Warum kann das Schreiben in ein sysfs-Attribut betrieblich bedeutsam sein?

::option[Jeder Schreibvorgang legt eine gewöhnliche Sicherungskopie auf dem Datenträger an.]{#sysfs-backup-copy explanation="Sysfs ist virtuell und erstellt keine automatischen Sicherungen von Steueränderungen."}
::option[Sysfs ignoriert alle Schreibvorgänge, auch wenn ein Attribut beschreibbar ist.]{#sysfs-ignore-writes explanation="Beschreibbare Attribute sind gerade dazu vorhanden, unterstützte Steuerwerte anzunehmen."}
::option[Der Schreibvorgang kann eine aktive Steuerfunktion des Kernels oder Treibers aufrufen.]{#sysfs-live-control .correct explanation="Beschreibbare Attribute sind aktive Schnittstellen und können das Geräteverhalten sofort verändern."}
:::

Nutze das Lab [Hardwaregeräte unter Linux erkunden](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861), um schreibgeschützt durch sysfs zu navigieren und es Geräteknoten zuzuordnen.

## Zusammenfassung

Du kannst sysfs nun als strukturierte Ansicht aktiver Kernel-Objekte verwenden.

1. Navigiere durch Geräte-, Klassen-, Bus-, Block- und Gerätenummernansichten.
2. Lies jeweils ein dokumentiertes Attribut mit der richtigen Einheit.
3. Ordne sysfs-Objekte den Knoten unter `/dev` zu.
4. Behandle beschreibbare Attribute als aktive Steuerschnittstellen.
