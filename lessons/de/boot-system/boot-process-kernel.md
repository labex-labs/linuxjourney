---
index: 4
lang: "de"
title: "Boot-Prozess: Kernel"
meta_title: "Boot-Prozess: Kernel – System starten"
meta_description: "Erkunden Sie den Linux-Kernel-Bootprozess. Erfahren Sie, wie initramfs Treiber von einem temporären Dateisystem lädt, um die endgültige Boot-Root-Partition einzuhängen. Verstehen Sie die Schritte von der Kernel-Ladung bis zur Ausführung von init."
meta_keywords: "Boot-Root, initramfs, Kernel-Boot, Boot-Partition, initramfs Ubuntu, /etc/default/grub, Linux-Bootprozess, Root-Dateisystem, Kernel-Initialisierung"
---

## Lesson Content

Sobald der Bootloader den Kernel in den Speicher geladen und die notwendigen Parameter übergeben hat, übernimmt der Kernel die Kontrolle über das System. Lassen Sie uns untersuchen, was als Nächstes geschieht.

### Kernel-Initialisierung und das Initramfs

Eine klassische Herausforderung beim Booten besteht darin, dass der Kernel Treiber benötigt, um auf Hardwaregeräte zuzugreifen, diese Treiber sich aber oft auf einem Speichergerät befinden, auf das der Kernel noch nicht zugreifen kann. Um dieses Problem zu lösen, verwendet Linux ein temporäres Root-Dateisystem.

In älteren Systemen wurde dies durch eine `initrd` (initial RAM disk) gehandhabt. Der Kernel lud dieses Plattenabbild, fand die notwendigen Treiber und wechselte dann zum eigentlichen Root-Dateisystem. Moderne Systeme, einschließlich Distributionen wie Ubuntu, verwenden `initramfs` (initial RAM filesystem). Im Gegensatz zu `initrd` ist `initramfs` ein `cpio`-Archiv, das direkt im Speicher in ein temporäres Dateisystem entpackt wird. Dieser Ansatz ist effizienter, da der Aufwand für die Erstellung und das Einhängen eines Blockgeräts entfällt. Das `initramfs` enthält nur die wesentlichen Module, die der Kernel benötigt, um auf die eigentliche `boot partition` und andere Hardware zuzugreifen.

### Einhängen des Boot-Root-Dateisystems

Mit den aus dem `initramfs` geladenen Treibern kann der Kernel nun das Haupt-`boot root`-Dateisystem lokalisieren und einhängen. Der Speicherort dieses Dateisystems wird dem Kernel typischerweise als Parameter vom Bootloader übergeben, was in Dateien wie `/etc/default/grub` konfiguriert werden kann.

Zuerst hängt der Kernel die `boot root`-Partition im Nur-Lese-Modus ein. Dies ist eine Sicherheitsmaßnahme, die es dem Dienstprogramm `fsck` (file system check) ermöglicht, die Integrität des Dateisystems zu überprüfen, ohne Datenkorruption zu riskieren. Nachdem die Überprüfung erfolgreich abgeschlossen wurde, hängt der Kernel das Dateisystem im Lese-/Schreibmodus erneut ein.

Schließlich, wenn das Root-Dateisystem vollständig verfügbar ist, startet der Kernel das allererste Benutzerprogramm: `init`. Dieses Programm ist dafür verantwortlich, den Rest des Systems hochzufahren.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis des Linux-Bootvorgangs zu festigen:

- **[Anpassen des GRUB2 Boot-Menüs unter Linux](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Lernen Sie, wie Sie das GRUB2 Boot-Menü anpassen, einschließlich der Änderung des Timeouts und des Standardeintrags, und wie Sie diese Änderungen anwenden. Dieses Labor hilft Ihnen zu verstehen, wie der Bootloader konfiguriert werden kann.

Dieses Labor hilft Ihnen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Linux-Bootkonfiguration aufzubauen.

## Quiz Question

What is used in modern systems to load a temporary root filesystem? Please answer in English, using only lowercase letters.

## Quiz Answer

initramfs
