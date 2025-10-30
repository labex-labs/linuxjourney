---
index: 3
lang: "de"
title: "Bootvorgang: Bootloader"
meta_title: "Bootvorgang: Bootloader - Das System booten"
meta_description: "Erfahren Sie mehr über den Linux-Bootloader, seine Funktionen und gängige Kernel-Parameter wie initrd und root. Verstehen Sie GRUB und optimieren Sie Ihren Linux-Bootvorgang."
meta_keywords: "Linux Bootloader, GRUB, Kernel-Parameter, initrd, Root-Dateisystem, Linux Bootvorgang, Linux Tutorial, Linux für Anfänger"
---

## Lesson Content

Die Hauptaufgaben des Bootloaders sind:

- Starten eines Betriebssystems; er kann auch zum Booten von Nicht-Linux-Betriebssystemen verwendet werden.
- Auswahl eines zu verwendenden Kernels.
- Angabe von Kernel-Parametern.

Der gebräuchlichste Bootloader für Linux ist GRUB; Sie verwenden ihn höchstwahrscheinlich auf Ihrem System. Es gibt viele andere Bootloader, die Sie verwenden können, wie LILO, EFILINUX, Coreboot, SYSLINUX und mehr. Wir werden jedoch nur mit GRUB als unserem Bootloader arbeiten.

Wir wissen also, dass das Hauptziel des Bootloaders darin besteht, den Kernel zu laden, aber wo findet er den Kernel? Um ihn zu finden, müssen wir uns unsere Kernel-Parameter ansehen. Die Parameter können durch Aufrufen des GRUB-Menüs beim Start mit der Taste 'e' gefunden werden. Wenn Sie kein GRUB haben, keine Sorge, wir werden die Boot-Parameter durchgehen, die Sie sehen werden:

- `initrd` - Gibt den Speicherort des initialen RAM-Disks an (darüber sprechen wir in der nächsten Lektion mehr).
- `BOOT_IMAGE` - Hier befindet sich das Kernel-Image.
- `root` - Der Speicherort des Root-Dateisystems; der Kernel sucht an diesem Speicherort nach `init`. Es wird oft durch seine UUID oder den Gerätenamen dargestellt, wie z.B. `/dev/sda1`.
- `ro` - Dieser Parameter ist ziemlich Standard; er bindet das Dateisystem im schreibgeschützten Modus ein.
- `quiet` - Dies wird hinzugefügt, damit Sie keine Anzeigemeldungen sehen, die während des Starts im Hintergrund ablaufen.
- `splash` - Dies ermöglicht die Anzeige des Startbildschirms.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis des GRUB-Bootloaders und seiner Konfiguration zu vertärken:

1. **[Das GRUB2-Bootmenü in Linux anpassen](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Üben Sie das Ändern der primären GRUB2-Konfigurationsdatei, um die Einstellungen des Bootmenüs zu ändern und diese Änderungen anzuwenden.

Dieses Labor wird Ihnen helfen, die Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Bootloader-Verwaltung aufzubauen.

## Quiz Question

Welcher Kernel-Parameter bewirkt, dass Sie keine Startmeldungen sehen?

## Quiz Answer

quiet
