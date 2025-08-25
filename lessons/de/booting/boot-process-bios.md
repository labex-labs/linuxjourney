---
index: 2
lang: "de"
title: "Bootprozess: BIOS"
meta_title: "Bootprozess: BIOS - System starten"
meta_description: "Erfahren Sie mehr über den Linux-Bootprozess, BIOS und MBR. Verstehen Sie, wie Ihr System startet, mit dieser anfängerfreundlichen Anleitung. Entdecken Sie UEFI-Konzepte!"
meta_keywords: "Linux-Bootprozess, BIOS, MBR, UEFI, Linux-Tutorial, Bootloader, Linux für Anfänger, Systemstart"
---

## Lesson Content

### BIOS

Der erste Schritt im Linux-Bootprozess ist das BIOS, das Systemintegritätsprüfungen durchführt. Das BIOS ist eine Firmware, die am häufigsten in IBM PC-kompatiblen Computern vorkommt, dem heute dominierenden Computertyp. Sie haben wahrscheinlich die BIOS-Firmware verwendet, um die Bootreihenfolge Ihrer Festplatten zu ändern, die Systemzeit zu überprüfen, die MAC-Adresse Ihres Computers usw. Das Hauptziel des BIOS ist es, den System-Bootloader zu finden.

Sobald das BIOS die Festplatte hochfährt, sucht es nach dem Boot-Block, um herauszufinden, wie das System gestartet werden soll. Je nachdem, wie Sie Ihre Festplatte partitionieren, wird es den Master Boot Record (MBR) oder GPT suchen. Der MBR befindet sich im ersten Sektor der Festplatte, den ersten 512 Bytes. Der MBR enthält den Code, um ein anderes Programm irgendwo auf der Festplatte zu laden; dieses Programm lädt wiederum unseren Bootloader.

Wenn Sie Ihre Festplatte mit GPT partitioniert haben, ändert sich der Speicherort des Bootloaders ein wenig.

### UEFI

Es gibt eine andere Möglichkeit, Ihr System zu starten, anstatt BIOS zu verwenden, und das ist mit UEFI (steht für "Unified Extensible Firmware Interface"). UEFI wurde als Nachfolger von BIOS entwickelt; die meisten heutigen Hardwareprodukte werden mit integrierter UEFI-Firmware geliefert. Macintosh-Computer verwenden EFI-Booting schon seit Jahren, und Windows hat die meisten seiner Dinge auf UEFI-Booting umgestellt. Das GPT-Format war für die Verwendung mit EFI vorgesehen. Sie benötigen nicht unbedingt EFI, wenn Sie eine GPT-Festplatte booten. Der erste Sektor einer GPT-Festplatte ist für einen "schützenden MBR" reserviert, um das Booten einer BIOS-basierten Maschine zu ermöglichen.

UEFI speichert alle Informationen zum Start in einer `.efi`-Datei. Diese Datei wird auf einer speziellen Partition namens EFI System Partition auf der Hardware gespeichert. Innerhalb dieser Partition befindet sich der Bootloader. UEFI bietet viele Verbesserungen gegenüber der traditionellen BIOS-Firmware. Da wir jedoch Linux verwenden, verwendet die Mehrheit von uns BIOS. Daher werden alle diese Lektionen von dieser Prämisse ausgehen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Benutzer- und Gruppenverwaltung zu vertiefen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** – Üben Sie den gesamten Lebenszyklus der Benutzerverwaltung, vom Erstellen und Sichern neuer Konten bis zum Ändern und Löschen.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** – Sammeln Sie praktische Erfahrungen mit Befehlszeilenprogrammen für die Gruppenverwaltung, einschließlich des Erstellens neuer Gruppen, des Änderns von Benutzerzugehörigkeiten und des Entfernens von Gruppen.
3. **[Benutzerkonten und Sudo-Berechtigungen in Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** – Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen, um die Sicherheit eines Linux-Systems zu verbessern.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Benutzer- und Gruppenverwaltung unter Linux aufzubauen.

## Quiz Question

Was lädt das BIOS?

## Quiz Answer

bootloader
