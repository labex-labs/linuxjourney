---
lang: "de"
title: "udev"
meta_description: "Erfahren Sie mehr über udev, wie es Linux-Gerätedateien dynamisch verwaltet und udevadm verwendet. Verstehen Sie die Erstellung von Geräteknoten für Anfänger."
meta_keywords: "udev, udevadm, Linux-Geräteverwaltung, Gerätedateien, Linux-Tutorial, Linux für Anfänger, udev-Regeln, Linux-Anleitung"
---

## Lesson Content

Früher, und auch heute noch, wenn man es wirklich wollte, erstellte man Geräteknoten mit einem Befehl wie diesem:

```bash
mknod /dev/sdb1 b 8 3
```

Dieser Befehl erstellt einen Geräteknoten `/dev/sdb1` und macht ihn zu einem Blockgerät (b) mit einer Major-Nummer von 8 und einer Minor-Nummer von 3.

Um ein Gerät zu entfernen, würde man einfach die Gerätedatei im Verzeichnis `/dev` **rm**.

Glücklicherweise müssen wir das dank udev nicht mehr tun. Das udev-System erstellt und entfernt Gerätedateien dynamisch für uns, je nachdem, ob sie verbunden sind oder nicht. Es gibt einen `udevd`-Daemon, der auf dem System läuft und auf Nachrichten vom Kernel über mit dem System verbundene Geräte lauscht. `Udevd` analysiert diese Informationen und gleicht die Daten mit den Regeln ab, die in `/etc/udev/rules.d` angegeben sind. Abhängig von diesen Regeln werden höchstwahrscheinlich Geräteknoten und symbolische Links für die Geräte erstellt. Sie können Ihre eigenen udev-Regeln schreiben, aber das geht über den Rahmen dieser Lektion hinaus. Glücklicherweise verfügt Ihr System bereits über viele udev-Regeln, sodass Sie möglicherweise nie Ihre eigenen schreiben müssen.

Sie können die udev-Datenbank und sysfs auch mit dem Befehl **udevadm** anzeigen. Dieses Tool ist sehr nützlich, kann aber manchmal sehr kompliziert werden. Ein einfacher Befehl zum Anzeigen von Informationen für ein Gerät wäre:

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

Führen Sie den angegebenen `udevadm`-Befehl aus und überprüfen Sie die Ausgabe.

## Quiz Question

Was fügt Geräte dynamisch hinzu und entfernt sie?

## Quiz Answer

udev
