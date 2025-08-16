---
lang: "de"
title: "Übersicht über den Bootvorgang"
description: "Lernen Sie die Phasen des Linux-Bootvorgangs kennen: BIOS, Bootloader, Kernel und Init. Verstehen Sie, wie Linux vom Einschalten bis zur Anmeldung startet. Ein unverzichtbarer Leitfaden für Linux-Anfänger."
keywords: "Linux-Bootvorgang, BIOS, Bootloader, Kernel, Init, Linux-Tutorial, Linux-Anleitung, Anfänger"
---

## Lesson Content

Nachdem wir nun ein ziemlich gutes Verständnis einiger wichtiger Komponenten von Linux gewonnen haben, wollen wir sie zusammensetzen, indem wir lernen, wie das System bootet. Wenn Sie Ihren Rechner einschalten, tut er einige nette Dinge, wie das Anzeigen des Logo-Bildschirms, das Durchlaufen verschiedener Meldungen, und am Ende werden Sie mit einem Anmeldefenster aufgefordert. Nun, es passiert tatsächlich eine Menge zwischen dem Drücken des Netzschalters und dem Anmelden, und wir werden diese in diesem Kurs besprechen.

Der Linux-Bootvorgang kann in 4 einfache Phasen unterteilt werden:

### 1. BIOS

Das BIOS (steht für "Basic Input/Output System") initialisiert die Hardware und stellt mit einem Power-on Self-Test (POST) sicher, dass die gesamte Hardware betriebsbereit ist. Die Hauptaufgabe des BIOS ist es, den Bootloader zu laden.

### 2. Bootloader

Der Bootloader lädt den Kernel in den Speicher und startet dann den Kernel mit einer Reihe von Kernel-Parametern. Einer der gebräuchlichsten Bootloader ist GRUB, ein universeller Linux-Standard.

### 3. Kernel

Wenn der Kernel geladen ist, initialisiert er sofort Geräte und Speicher. Die Hauptaufgabe des Kernels ist es, den init-Prozess zu laden.

### 4. Init

Denken Sie daran, der init-Prozess ist der erste Prozess, der gestartet wird. Init startet und stoppt wesentliche Dienstprozesse auf dem System. Es gibt drei Hauptimplementierungen von init in Linux-Distributionen. Wir werden sie kurz durchgehen und dann in einem anderen Kurs tiefer darauf eingehen.

Das ist sie, die (sehr) einfache Erklärung des Linux-Bootvorgangs. Wir werden in den nächsten Lektionen detaillierter auf diese Phasen eingehen.

## Exercise

Starten Sie Ihr System neu und versuchen Sie, jeden Schritt zu erkennen, während Ihr Rechner hochfährt.

## Quiz Question

Was ist die letzte Phase im Linux-Bootvorgang?

## Quiz Answer

init
