---
index: 4
lang: "de"
title: "sysfs"
meta_title: "sysfs - Geräte"
meta_description: "Erfahren Sie, was sysfs ist und welche Rolle es im Linux-Sys-System spielt. Dieser Leitfaden erklärt das Linux /sys-Verzeichnis, ein virtuelles Dateisystem für Geräteinformationen, und grenzt es von /dev ab."
meta_keywords: "sysfs, was ist sysfs, /sys, linux /sys, linux sys, sys system, virtuelles Dateisystem, linux geräte, /dev"
---

## Lesson Content

Das `sysfs`-Dateisystem wurde eingeführt, um Geräte in einem Linux-System besser verwalten zu können, eine Aufgabe, für die das Verzeichnis `/dev` nicht vollständig ausgestattet war. Das Verständnis dafür, **was /sys in Linux ist**, ist der Schlüssel zur modernen Systemadministration.

### Was ist sysfs?

`sysfs` ist ein virtuelles Dateisystem, das typischerweise unter `/sys` eingehängt wird und Informationen über Kernel-Objekte, Hardware-Geräte und Treiber aus dem Gerätemodell des Kernels an den Userspace exportiert. Im Gegensatz zu Dateien auf einer physischen Festplatte werden die Dateien und Verzeichnisse in `/sys` "on the fly" generiert und stellen den aktuellen Zustand des **sys-Systems** dar.

### Die Rolle des linux /sys Verzeichnisses

Der Hauptzweck des **linux /sys** Verzeichnisses besteht darin, eine strukturierte Ansicht aller Geräte auf Ihrem System bereitzustellen. Es enthält detaillierte Informationen wie Hersteller und Modell, wo das Gerät angeschlossen ist, seinen aktuellen Zustand und seine Position in der Gerätehierarchie.

Die hier angezeigten Dateien sind keine Geräteknoten wie die in `/dev`. Sie interagieren nicht direkt über `/sys` mit dem Gerät selbst; vielmehr verwenden Sie es, um Informationen anzuzeigen und die Attribute des Geräts zu verwalten.

### sysfs vs. /dev

Obwohl sich `/sys` und `/dev` beide auf Geräte beziehen, erfüllen sie unterschiedliche Funktionen.

- Das `/dev`-Verzeichnis stellt Geräteknoten bereit, spezielle Dateien, die es Programmen ermöglichen, auf die Geräte selbst zuzugreifen.
- Das `/sys`-Dateisystem wird verwendet, um Informationen über die Geräte anzuzeigen und sie zu verwalten. Es legt das zugrunde liegende Gerätemodell offen.

Betrachten wir zum Beispiel den Inhalt eines Blockgeräteverzeichnisses innerhalb von `/sys`:

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

Diese Ausgabe zeigt verschiedene Attribute und Unterverzeichnisse, die sich auf die Festplatte `sda` beziehen, und bietet eine weitaus detailliertere Ansicht als nur `/dev/sda` allein.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Hardware-Geräteerkundung unter Linux zu festigen:

1. **[Hardware-Geräte unter Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** - Üben Sie die Identifizierung und Inspektion von Hardware-Geräten in einer Linux-Umgebung, ähnlich wie das `/sys`-Dateisystem Geräteinformationen bereitstellt.

Dieses Labor hilft Ihnen dabei, die Konzepte des Verständnisses der Systemhardware und ihrer Darstellung in Linux anzuwenden und Vertrauen in die Geräteerkundung aufzubauen.

## Quiz Question

Welches Verzeichnis wird verwendet, um detaillierte Informationen zu Geräten anzuzeigen? Bitte antworten Sie auf Englisch.

## Quiz Answer

/sys
