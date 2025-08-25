---
index: 5
lang: "de"
title: "udev"
meta_title: "udev - Geräte"
meta_description: "Erfahren Sie mehr über udev, wie es Linux-Gerätedateien dynamisch verwaltet und udevadm verwendet. Verstehen Sie die Erstellung von Geräteknoten für Anfänger."
meta_keywords: "udev, udevadm, Linux-Geräteverwaltung, Gerätedateien, Linux-Tutorial, Linux für Anfänger, udev-Regeln, Linux-Anleitung"
---

## Lesson Content

Früher, und auch heute noch, wenn man es wirklich wollte, konnte man Geräteknoten mit einem Befehl wie diesem erstellen:

```bash
mknod /dev/sdb1 b 8 3
```

Dieser Befehl erstellt einen Geräteknoten `/dev/sdb1` und macht ihn zu einem Blockgerät (b) mit einer Major-Nummer von 8 und einer Minor-Nummer von 3.

Um ein Gerät zu entfernen, würde man einfach die Gerätedatei im Verzeichnis `/dev` **rm**.

Glücklicherweise müssen wir dies dank udev nicht mehr tun. Das udev-System erstellt und entfernt Gerätedateien dynamisch für uns, je nachdem, ob sie verbunden sind oder nicht. Es gibt einen `udevd`-Daemon, der auf dem System läuft und auf Nachrichten vom Kernel über mit dem System verbundene Geräte lauscht. `Udevd` analysiert diese Informationen und gleicht die Daten mit den Regeln ab, die in `/etc/udev/rules.d` angegeben sind. Abhängig von diesen Regeln werden höchstwahrscheinlich Geräteknoten und symbolische Links für die Geräte erstellt. Sie können Ihre eigenen udev-Regeln schreiben, aber das geht für diese Lektion etwas zu weit. Glücklicherweise enthält Ihr System bereits viele udev-Regeln, sodass Sie möglicherweise nie Ihre eigenen schreiben müssen.

Sie können die udev-Datenbank und sysfs auch mit dem Befehl **udevadm** anzeigen. Dieses Tool ist sehr nützlich, kann aber manchmal sehr kompliziert werden. Ein einfacher Befehl zum Anzeigen von Informationen für ein Gerät wäre:

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Hardware-Interaktion und Geräteverwaltung unter Linux zu vertiefen:

1. **[Hardware-Geräte unter Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** - In diesem Lab lernen Sie die wesentlichen Fähigkeiten, um Hardware-Geräte in einer Linux-Umgebung zu erkunden, zu identifizieren und zu inspizieren. Sie sammeln praktische Erfahrungen mit leistungsstarken Befehlszeilenprogrammen, um zu verstehen, wie das Betriebssystem mit physischen Komponenten interagiert, was entscheidend ist, um Geräteknoten und die Rolle von udev zu verstehen.

Dieses Lab hilft Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Hardwareverwaltung aufzubauen.

## Quiz Question

Was fügt Geräte dynamisch hinzu und entfernt sie?

## Quiz Answer

udev
