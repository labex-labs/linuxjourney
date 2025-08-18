---
index: 4
lang: "de"
title: "sysfs"
meta_title: "sysfs - Geräte"
meta_description: "Erfahren Sie mehr über sysfs, ein virtuelles Dateisystem für detaillierte Linux-Geräteinformationen und -verwaltung. Verstehen Sie /sys vs /dev. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "sysfs, /sys directory, Linux devices, virtual filesystem, Linux tutorial, beginner guide"
---

## Lesson Content

Sysfs wurde vor langer Zeit geschaffen, um Geräte in unserem System besser zu verwalten, eine Aufgabe, die das Verzeichnis `/dev` nicht ausreichend erfüllen konnte. Sysfs ist ein virtuelles Dateisystem, das meistens im Verzeichnis `/sys` gemountet ist. Es gibt uns detailliertere Informationen, als wir sie im Verzeichnis `/dev` sehen könnten. Beide Verzeichnisse, `/sys` und `/dev`, scheinen sehr ähnlich zu sein und sind es in gewisser Hinsicht auch, aber sie weisen große Unterschiede auf. Grundsätzlich ist das Verzeichnis `/dev` einfach; es ermöglicht anderen Programmen den Zugriff auf die Geräte selbst, während das Dateisystem `/sys` verwendet wird, um Informationen anzuzeigen und das Gerät zu verwalten.

Das Dateisystem `/sys` enthält im Grunde alle Informationen für alle Geräte in Ihrem System, wie z. B. Hersteller und Modell, wo das Gerät angeschlossen ist, den Zustand des Geräts, die Hierarchie der Geräte und vieles mehr. Die Dateien, die Sie hier sehen, sind keine Geräteknoten, sodass Sie nicht wirklich mit Geräten aus dem Verzeichnis `/sys` interagieren; vielmehr verwalten Sie Geräte.

Werfen Sie einen Blick auf den Inhalt des Verzeichnisses `/sys`:

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

## Exercise

Schauen Sie sich den Inhalt des Verzeichnisses `/sys` an und sehen Sie, welche Dateien sich dort befinden.

## Quiz Question

Welches Verzeichnis wird verwendet, um detaillierte Informationen zu Geräten anzuzeigen?

## Quiz Answer

/sys
