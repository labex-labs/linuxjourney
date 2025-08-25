---
index: 1
lang: "de"
title: "Bootvorgang Überblick"
meta_title: "Bootvorgang Überblick - Das System booten"
meta_description: "Lernen Sie die Phasen des Linux-Bootvorgangs kennen: BIOS, Bootloader, Kernel und Init. Verstehen Sie, wie Linux vom Einschalten bis zur Anmeldung startet. Ein unverzichtbarer Linux-Anfängerleitfaden."
meta_keywords: "Linux-Bootvorgang, BIOS, Bootloader, Kernel, Init, Linux-Tutorial, Linux-Leitfaden, Anfänger"
---

## Lesson Content

Nachdem wir nun ein ziemlich gutes Verständnis einiger wichtiger Komponenten von Linux erlangt haben, wollen wir sie alle zusammenfügen, indem wir lernen, wie das System bootet. Wenn Sie Ihren Rechner einschalten, macht er einige nette Dinge, wie das Anzeigen des Logo-Bildschirms, das Durchlaufen verschiedener Meldungen, und am Ende werden Sie mit einem Anmeldefenster aufgefordert. Nun, es passiert tatsächlich eine Menge Zeug zwischen dem Drücken des Netzschalters und dem Anmelden, und wir werden diese in diesem Kurs besprechen.

Der Linux-Bootvorgang lässt sich in 4 einfache Phasen unterteilen:

### 1. BIOS

Das BIOS (steht für "Basic Input/Output System") initialisiert die Hardware und stellt mit einem Power-on Self-Test (POST) sicher, dass die gesamte Hardware betriebsbereit ist. Die Hauptaufgabe des BIOS ist es, den Bootloader zu laden.

### 2. Bootloader

Der Bootloader lädt den Kernel in den Speicher und startet dann den Kernel mit einer Reihe von Kernel-Parametern. Einer der gebräuchlichsten Bootloader ist GRUB, ein universeller Linux-Standard.

### 3. Kernel

Wenn der Kernel geladen ist, initialisiert er sofort Geräte und Speicher. Die Hauptaufgabe des Kernels ist es, den init-Prozess zu laden.

### 4. Init

Denken Sie daran, der init-Prozess ist der erste Prozess, der gestartet wird. Init startet und stoppt wesentliche Dienstprozesse auf dem System. Es gibt drei Hauptimplementierungen von init in Linux-Distributionen. Wir werden sie kurz behandeln und dann in einem anderen Kurs näher darauf eingehen.

Das ist sie, die (sehr) einfache Erklärung des Linux-Bootvorgangs. In den nächsten Lektionen werden wir detaillierter auf diese Phasen eingehen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Bootvorgangs zu vertiefen:

1. **[Das GRUB2-Bootmenü in Linux anpassen](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** – Üben Sie das Ändern des GRUB2-Bootmenüs, einer kritischen Komponente in der Linux-Bootsequenz.

Dieses Lab hilft Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen im Umgang mit der Linux-Bootumgebung aufzubauen.

## Quiz Question

Was ist die letzte Phase im Linux-Bootvorgang?

## Quiz Answer

init
