---
index: 4
lang: "de"
title: "sysfs"
meta_title: "sysfs - Geräte"
meta_description: "Erfahren Sie mehr über sysfs, ein virtuelles Dateisystem für detaillierte Linux-Geräteinformationen und -verwaltung. Verstehen Sie /sys vs /dev. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "sysfs, /sys Verzeichnis, Linux-Geräte, virtuelles Dateisystem, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Sysfs wurde vor langer Zeit geschaffen, um Geräte auf unserem System besser zu verwalten, eine Aufgabe, die das Verzeichnis `/dev` nicht ausreichend erfüllen konnte. Sysfs ist ein virtuelles Dateisystem, das meistens im Verzeichnis `/sys` gemountet ist. Es liefert uns detailliertere Informationen, als wir sie im Verzeichnis `/dev` sehen könnten. Beide Verzeichnisse, `/sys` und `/dev`, scheinen sehr ähnlich zu sein und sind es in gewisser Hinsicht auch, aber sie weisen große Unterschiede auf. Grundsätzlich ist das Verzeichnis `/dev` einfach; es ermöglicht anderen Programmen den Zugriff auf die Geräte selbst, während das Dateisystem `/sys` verwendet wird, um Informationen anzuzeigen und das Gerät zu verwalten.

Das Dateisystem `/sys` enthält im Grunde alle Informationen für alle Geräte auf Ihrem System, wie z. B. Hersteller und Modell, wo das Gerät angeschlossen ist, den Zustand des Geräts, die Hierarchie der Geräte und vieles mehr. Die Dateien, die Sie hier sehen, sind keine Geräteknoten, daher interagieren Sie nicht wirklich mit Geräten aus dem Verzeichnis `/sys`; vielmehr verwalten Sie Geräte.

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

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Hardware-Geräteerkundung unter Linux zu vertiefen:

1. **[Hardware-Geräte unter Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** – Üben Sie das Identifizieren und Inspizieren von Hardware-Geräten in einer Linux-Umgebung, ähnlich wie das `/sys`-Dateisystem Geräteinformationen bereitstellt.

Dieses Labor wird Ihnen helfen, die Konzepte des Verständnisses von Systemhardware und ihrer Darstellung unter Linux anzuwenden und Vertrauen in die Geräteerkundung aufzubauen.

## Quiz Question

Welches Verzeichnis wird verwendet, um detaillierte Informationen zu Geräten anzuzeigen?

## Quiz Answer

/sys
