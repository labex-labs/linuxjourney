---
index: 3
lang: "de"
title: "Boot-Prozess: Bootloader"
meta_title: "Boot-Prozess: Bootloader – System starten"
meta_description: "Ein Leitfaden zum Bootloader in Linux. Erfahren Sie, was ein Linux-Bootloader ist, welche Hauptfunktionen er hat und wie GRUB Kernel-Parameter wie initrd und root verwendet, um das System zu starten."
meta_keywords: "linux bootloader, bootloader in linux, linux bootloader, grub, was ist bootloader in linux, kernel parameter, initrd, root dateisystem, linux boot prozess"
---

## Lesson Content

### Was ist ein Bootloader in Linux

Nachdem das BIOS/UEFI seine Aufgaben beendet hat, übergibt es die Kontrolle an die nächste Stufe des Bootvorgangs: den Bootloader. Ein **Bootloader in Linux** ist ein kleines Programm, das den Kernel des Betriebssystems in den Speicher lädt und ihn dann ausführt. Er fungiert als Brücke zwischen der System-Firmware und dem Linux-Kernel.

### Die Rolle des Linux-Bootloaders

The primary responsibilities of a **Linux boot loader** are straightforward but critical:

- **Betriebssystemauswahl**: Er kann ein Menü anzeigen, um in verschiedene Betriebssysteme zu booten, einschließlich Nicht-Linux-Systemen, falls Sie eine Multi-Boot-Umgebung eingerichtet haben.
- **Kernel-Auswahl**: Er ermöglicht Ihnen die Auswahl, welche Version des Linux-Kernels geladen werden soll, was bei der Fehlerbehebung oder beim Testen nützlich ist.
- **Übergabe von Kernel-Parametern**: Er legt entscheidende Parameter fest, die der Kernel benötigt, um korrekt zu starten.

The most common **Linux bootloader** is GRUB (GRand Unified Bootloader), which you are most likely using. While other bootloaders like LILO, SYSLINUX, and Coreboot exist, this lesson will focus on GRUB.

### Häufige Kernel-Parameter in GRUB

The main goal of the bootloader is to load the kernel, but it needs instructions on how and where to find it. These instructions are provided as kernel parameters. You can typically view or edit these parameters by pressing the 'e' key in the **GRUB** menu during startup.

Here are some of the most common parameters you will encounter:

- `initrd` - Gibt den Speicherort des initialen RAM-Disks an, eines temporären Root-Dateisystems, das in den Speicher geladen wird. Wir werden dies in der nächsten Lektion genauer behandeln.
- `BOOT_IMAGE` - Definiert den Pfad zur Kernel-Image-Datei, die geladen werden soll.
- `root` - Zeigt auf den Speicherort des tatsächlichen Root-Dateisystems. Der Kernel verwendet diesen Pfad, um den `init`-Prozess zu finden. Dies wird oft durch einen Gerätenamen (z. B. `/dev/sda1`) oder eine UUID dargestellt.
- `ro` - Ein Standardparameter, der dem Kernel anweist, das Root-Dateisystem zunächst im schreibgeschützten Modus einzuhängen. Dies ist eine Sicherheitsmaßnahme, um Dateisystemprüfungen zu ermöglichen, bevor Änderungen vorgenommen werden.
- `quiet` - Dieser Parameter unterdrückt die meisten detaillierten Boot-Meldungen und sorgt für einen saubereren, weniger ausführlichen Startbildschirm.
- `splash` - Aktiviert die Anzeige eines grafischen Splash-Screens während des Bootvorgangs anstelle von Textmeldungen.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis des GRUB-Bootloaders und seiner Konfiguration zu festigen:

1. **[Anpassen des GRUB2-Bootmenüs in Linux](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Üben Sie die Änderung der primären GRUB2-Konfigurationsdatei, um die Einstellungen des Bootmenüs zu ändern und diese Änderungen anzuwenden.

Dieses Labor hilft Ihnen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Bootloader-Verwaltung aufzubauen.

## Quiz Question

Welcher Kernel-Parameter sorgt dafür, dass Sie beim Hochfahren keine Meldungen sehen? Bitte antworten Sie mit dem einzelnen Parameter in kleingeschriebenem Englisch.

## Quiz Answer

quiet
