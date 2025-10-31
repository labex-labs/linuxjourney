---
index: 1
lang: "de"
title: "Überblick über den Bootvorgang"
meta_title: "Bootvorgang Übersicht - System starten"
meta_description: "Ein klarer Überblick über den Linux-Bootvorgang, der die vier Schlüsselphasen detailliert beschreibt: BIOS, Bootloader, Kernel und Init. Erfahren Sie mehr über den gesamten Startprozess des Linux-Betriebssystems, von der Inbetriebnahme bis zur Anmeldeaufforderung."
meta_keywords: "Linux Bootvorgang, Bootvorgang Linux, Startvorgang Linux, Startvorgang Linux Betriebssystem, BIOS, Bootloader, Kernel, Init, Linux Tutorial, Linux Anleitung, Anfänger"
---

## Lesson Content

Nachdem wir einige Schlüsselkomponenten von Linux kennengelernt haben, sehen wir uns nun an, wie diese beim Systemstart zusammenspielen. Die gesamte Abfolge, vom Drücken des Netzschalters bis zum Erscheinen der Anmeldeaufforderung, wird als **Linux-Bootvorgang** bezeichnet. Es ist eine faszinierende Reise, die eine ausgeschaltete Maschine in ein voll funktionsfähiges Betriebssystem verwandelt.

Der **Bootvorgang des Linux-Betriebssystems** lässt sich in vier Hauptphasen vereinfachen.

### Phase 1 BIOS

Das BIOS (Basic Input/Output System) oder sein moderner Nachfolger, UEFI (Unified Extensible Firmware Interface), ist die erste Software, die beim Einschalten Ihres Computers ausgeführt wird. Es führt einen Power-On Self-Test (POST) durch, um die Hardware des Systems wie CPU, Speicher und Speichergeräte zu initialisieren und zu überprüfen. Sobald die Hardware in Ordnung ist, besteht die Hauptaufgabe des BIOS darin, den Bootloader auf einem Speichergerät zu lokalisieren und zu laden.

### Phase 2 Bootloader

Der Bootloader übernimmt die Kontrolle vom BIOS. Seine Hauptaufgabe ist es, den Linux-Kernel in den Speicher zu laden. Ein gängiger Bootloader für Linux ist GRUB (GRand Unified Bootloader). GRUB zeigt oft ein Menü an, in dem Sie auswählen können, welches Betriebssystem oder welche Kernel-Version gestartet werden soll. Nach Ihrer Auswahl (oder nach Ablauf eines Timeouts) lädt er den ausgewählten Kernel und eine initiale RAM-Disk (initrd) in den Speicher und übergibt die Kontrolle an den Kernel.

### Phase 3 Kernel

Sobald der Kernel in den Speicher geladen ist, übernimmt er die Kontrolle über das System. Er beginnt damit, sich selbst zu dekomprimieren und die Kern-Hardware sowie die Speicherverwaltung zu initialisieren. Anschließend bindet der Kernel das Root-Dateisystem ein, das alle Systemdateien enthält. Seine letzte und wichtigste Aufgabe im **Boot-Prozess Linux** besteht darin, das erste Programm im Benutzermodus auszuführen: den `init`-Prozess.

### Phase 4 Init

Der `init`-Prozess ist der erste vom Kernel gestartete Prozess und der Vorfahre aller anderen Prozesse im System. Seine Hauptaufgabe ist es, das System in einen nutzbaren Zustand zu versetzen, indem er wesentliche Dienste und Hintergrundprozesse (Daemons) gemäß seiner Konfiguration startet. Es gibt verschiedene Implementierungen von `init`, wie das traditionelle System V init, Upstart und das heute weit verbreitete systemd.

Dies bietet einen Überblick über den **Bootvorgang Linux** durchläuft. In den folgenden Lektionen werden wir tiefer auf jede dieser Phasen eingehen.

## Exercise

Um Ihr Verständnis zu festigen, empfehlen wir Ihnen, dieses praktische Labor auszuprobieren. Es bietet eine Umgebung, um das Gelernte über den Linux-Bootvorgang praktisch anzuwenden.

1. **[Anpassen des GRUB2-Bootmenüs in Linux](https://labex.io/de/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - Üben Sie die Modifikation des GRUB2-Bootmenüs, einer kritischen Komponente der Linux-Bootsequenz.

## Quiz Question

What is the last stage in the Linux boot process? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

init
