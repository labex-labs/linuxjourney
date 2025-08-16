---
lang: "de"
title: "Bootprozess: Kernel"
description: "Erfahren Sie mehr über den Linux-Bootprozess, die Kernel-Initialisierung und die Rolle von initramfs. Verstehen Sie, wie der Kernel das Root-Dateisystem mountet. Leitfaden zum Linux-Bootprozess."
keywords: "Linux-Bootprozess, Kernel-Boot, initramfs, initrd, Root-Dateisystem, Linux-Tutorial, Linux für Anfänger, Linux-Leitfaden"
---

## Lesson Content

Nachdem unser Bootloader nun die notwendigen Parameter übergeben hat, wollen wir sehen, wie er startet:

### Initrd vs Initramfs

Es gibt ein kleines Henne-Ei-Problem, wenn wir über den Kernel-Boot sprechen. Der Kernel verwaltet die Hardware unseres Systems; jedoch sind nicht alle Treiber dem Kernel während des Bootvorgangs verfügbar. Wir sind also auf ein temporäres Root-Dateisystem angewiesen, das nur die wesentlichen Module enthält, die der Kernel benötigt, um auf den Rest der Hardware zuzugreifen. In älteren Linux-Versionen wurde diese Aufgabe der initrd (initial ramdisk) zugewiesen. Der Kernel würde die initrd mounten, die notwendigen Boot-Treiber erhalten, und wenn er mit dem Laden alles Notwendigen fertig war, würde er die initrd durch das eigentliche Root-Dateisystem ersetzen. Heutzutage haben wir etwas namens initramfs; dies ist ein temporäres Root-Dateisystem, das in den Kernel selbst integriert ist, um alle notwendigen Treiber für das echte Root-Dateisystem zu laden, sodass die initrd-Datei nicht mehr gesucht werden muss.

### Mounting the root filesystem

Nun hat der Kernel alle Module, die er benötigt, um ein Root-Gerät zu erstellen und die Root-Partition zu mounten. Bevor es weitergeht, wird die Root-Partition tatsächlich zuerst im Read-Only-Modus gemountet, damit fsck sicher ausgeführt werden und die Systemintegrität überprüfen kann. Danach wird das Root-Dateisystem im Read-Write-Modus erneut gemountet. Dann lokalisiert der Kernel das init-Programm und führt es aus.

## Exercise

No exercises for this lesson.

## Quiz Question

Was wird in modernen Systemen verwendet, um ein temporäres Root-Dateisystem zu laden?

## Quiz Answer

initramfs
