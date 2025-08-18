---
index: 3
lang: "de"
title: "Bootvorgang: Bootloader"
meta_title: "Bootvorgang: Bootloader - System booten"
meta_description: "Erfahren Sie mehr über den Linux-Bootloader, seine Funktionen und gängige Kernel-Parameter wie initrd und root. Verstehen Sie GRUB und optimieren Sie Ihren Linux-Bootvorgang."
meta_keywords: "Linux Bootloader, GRUB, Kernel-Parameter, initrd, Root-Dateisystem, Linux-Bootvorgang, Linux-Tutorial, Linux für Anfänger"
---

## Lesson Content

Die Hauptaufgaben des Bootloaders sind:

- Starten eines Betriebssystems; er kann auch zum Booten von Nicht-Linux-Betriebssystemen verwendet werden.
- Auswahl eines zu verwendenden Kernels.
- Angabe von Kernel-Parametern.

Der gebräuchlichste Bootloader für Linux ist GRUB; Sie verwenden ihn höchstwahrscheinlich auf Ihrem System. Es gibt viele andere Bootloader, die Sie verwenden können, wie LILO, EFILINUX, Coreboot, SYSLINUX und weitere. Wir werden uns jedoch nur mit GRUB als unserem Bootloader beschäftigen.

Wir wissen also, dass das Hauptziel des Bootloaders darin besteht, den Kernel zu laden, aber wo findet er den Kernel? Um ihn zu finden, müssen wir uns unsere Kernel-Parameter ansehen. Die Parameter können durch Aufrufen des GRUB-Menüs beim Start mit der Taste 'e' gefunden werden. Wenn Sie GRUB nicht haben, keine Sorge, wir werden die Boot-Parameter durchgehen, die Sie sehen werden:

- `initrd` – Gibt den Speicherort der initialen RAM-Disk an (mehr dazu in der nächsten Lektion).
- `BOOT_IMAGE` – Hier befindet sich das Kernel-Image.
- `root` – Der Speicherort des Root-Dateisystems; der Kernel sucht an diesem Speicherort nach `init`. Es wird oft durch seine UUID oder den Gerätenamen, wie `/dev/sda1`, dargestellt.
- `ro` – Dieser Parameter ist ziemlich Standard; er bindet das Dateisystem im Nur-Lese-Modus ein.
- `quiet` – Dies wird hinzugefügt, damit Sie keine Anzeigemeldungen sehen, die während des Bootvorgangs im Hintergrund ablaufen.
- `splash` – Dies ermöglicht die Anzeige des Startbildschirms.

## Exercise

Wenn Sie GRUB als Bootloader haben, gehen Sie mit 'e' in das GRUB-Menü und sehen Sie sich die Einstellungen an.

## Quiz Question

Welcher Kernel-Parameter bewirkt, dass Sie keine Startmeldungen sehen?

## Quiz Answer

quiet
