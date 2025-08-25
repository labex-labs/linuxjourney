---
index: 4
lang: "de"
title: "Bootvorgang: Kernel"
meta_title: "Bootvorgang: Kernel - Das System booten"
meta_description: "Erfahren Sie mehr über den Linux-Bootvorgang, die Kernel-Initialisierung und die Rolle von initramfs. Verstehen Sie, wie der Kernel das Root-Dateisystem mountet. Leitfaden zum Linux-Bootvorgang."
meta_keywords: "Linux-Bootvorgang, Kernel-Boot, initramfs, initrd, Root-Dateisystem, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Nachdem unser Bootloader nun die notwendigen Parameter übergeben hat, wollen wir sehen, wie er startet:

### Initrd vs Initramfs

Es gibt ein kleines Henne-Ei-Problem, wenn wir über den Kernel-Boot sprechen. Der Kernel verwaltet die Hardware unseres Systems; jedoch sind nicht alle Treiber dem Kernel während des Bootvorgangs verfügbar. Wir sind also auf ein temporäres Root-Dateisystem angewiesen, das nur die wesentlichen Module enthält, die der Kernel benötigt, um auf den Rest der Hardware zuzugreifen. In älteren Linux-Versionen wurde diese Aufgabe der initrd (initial ramdisk) zugewiesen. Der Kernel mountete die initrd, holte die notwendigen Boot-Treiber, und wenn er mit dem Laden alles Notwendigen fertig war, ersetzte er die initrd durch das eigentliche Root-Dateisystem. Heutzutage haben wir etwas namens initramfs; dies ist ein temporäres Root-Dateisystem, das in den Kernel selbst integriert ist, um alle notwendigen Treiber für das echte Root-Dateisystem zu laden, sodass das Auffinden der initrd-Datei nicht mehr nötig ist.

### Das Root-Dateisystem mounten

Nun hat der Kernel alle Module, die er benötigt, um ein Root-Gerät zu erstellen und die Root-Partition zu mounten. Bevor es weitergeht, wird die Root-Partition zunächst im Nur-Lese-Modus gemountet, damit fsck sicher ausgeführt werden und die Systemintegrität überprüfen kann. Danach wird das Root-Dateisystem im Lese-Schreib-Modus erneut gemountet. Dann lokalisiert der Kernel das init-Programm und führt es aus.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis des Linux-Bootvorgangs zu vertiefen:

- **[Das GRUB2-Bootmenü in Linux anpassen](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** – Lernen Sie, das GRUB2-Bootmenü zu ändern, einschließlich der Änderung des Timeouts und des Standardeintrags, und wenden Sie diese Änderungen an. Dieses Labor wird Ihnen helfen zu verstehen, wie der Bootloader konfiguriert werden kann.

Dieses Labor wird Ihnen helfen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Linux-Bootkonfiguration aufzubauen.

## Quiz Question

Was wird in modernen Systemen verwendet, um ein temporäres Root-Dateisystem zu laden?

## Quiz Answer

initramfs
