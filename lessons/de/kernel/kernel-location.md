---
lang: "de"
title: "Kernel-Speicherort"
meta_title: "Kernel-Speicherort - Kernel"
meta_description: "Erfahren Sie mehr über den Speicherort des Linux-Kernels im Verzeichnis /boot und verstehen Sie vmlinuz, initrd und System.map. Erkunden Sie Kernel-Dateien und verwalten Sie den Speicherplatz effektiv."
meta_keywords: "Linux-Kernel, /boot-Verzeichnis, vmlinuz, initrd, System.map, Linux-Anfänger, Kernel-Tutorial, Linux-Anleitung"
---

## Lesson Content

Was passiert, wenn Sie einen neuen Kernel installieren? Nun, es fügt Ihrem System tatsächlich ein paar Dateien hinzu; diese Dateien werden normalerweise im Verzeichnis `/boot` abgelegt.

Sie werden mehrere Dateien für verschiedene Kernel-Versionen sehen:

- `vmlinuz` – dies ist der eigentliche Linux-Kernel
- `initrd` – wie bereits besprochen, wird die `initrd` als temporäres Dateisystem verwendet, bevor der Kernel geladen wird
- `System.map` – symbolische Nachschlagetabelle
- `config` – Kernel-Konfigurationseinstellungen; wenn Sie Ihren eigenen Kernel kompilieren, können Sie festlegen, welche Module geladen werden können

Wenn Ihr `/boot`-Verzeichnis keinen Speicherplatz mehr hat, können Sie jederzeit alte Versionen dieser Dateien löschen oder einfach einen Paketmanager verwenden. Seien Sie jedoch vorsichtig bei der Wartung in diesem Verzeichnis und löschen Sie nicht versehentlich den Kernel, den Sie gerade verwenden.

## Exercise

Go into your boot directory and see what files are in there.

## Quiz Question

Wie heißt das Kernel-Image in `/boot`?

## Quiz Answer

vmlinuz
