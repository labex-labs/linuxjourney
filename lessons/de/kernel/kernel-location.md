---
index: 5
lang: "de"
title: "Kernel-Speicherort"
meta_title: "Kernel-Speicherort - Kernel"
meta_description: "Erfahren Sie mehr über den Speicherort des Linux-Kernels im Verzeichnis /boot und verstehen Sie vmlinuz, initrd und System.map. Erkunden Sie Kernel-Dateien und verwalten Sie den Speicherplatz effektiv."
meta_keywords: "Linux-Kernel, /boot-Verzeichnis, vmlinuz, initrd, System.map, Linux-Anfänger, Kernel-Tutorial, Linux-Anleitung"
---

## Lesson Content

Was passiert, wenn Sie einen neuen Kernel installieren? Nun, es fügt Ihrem System tatsächlich ein paar Dateien hinzu; diese Dateien werden normalerweise im Verzeichnis `/boot` abgelegt.

Sie werden mehrere Dateien für verschiedene Kernel-Versionen sehen:

- `vmlinuz` - dies ist der eigentliche Linux-Kernel
- `initrd` - wie bereits besprochen, wird die `initrd` als temporäres Dateisystem verwendet, das vor dem Laden des Kernels genutzt wird
- `System.map` - symbolische Nachschlagetabelle
- `config` - Kernel-Konfigurationseinstellungen; wenn Sie Ihren eigenen Kernel kompilieren, können Sie festlegen, welche Module geladen werden können

Wenn Ihr `/boot`-Verzeichnis keinen Speicherplatz mehr hat, können Sie jederzeit alte Versionen dieser Dateien löschen oder einfach einen Paketmanager verwenden. Seien Sie jedoch vorsichtig bei der Wartung in diesem Verzeichnis und löschen Sie nicht versehentlich den Kernel, den Sie gerade verwenden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Bootvorgangs und der Kernel-Verwaltung zu vertiefen:

1. **[GRUB2-Bootmenü in Linux anpassen](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Üben Sie das Ändern der GRUB2-Konfiguration, die sich direkt darauf auswirkt, wie Ihr Linux-System bootet und Kernel-Versionen auswählt. Dieses Lab hilft Ihnen, die praktischen Auswirkungen der im Verzeichnis `/boot` besprochenen Dateien zu verstehen.

Dieses Lab hilft Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Linux-Kernel- und Boot-Verwaltung aufzubauen.

## Quiz Question

Wie wird das Kernel-Image in `/boot` genannt?

## Quiz Answer

vmlinuz
