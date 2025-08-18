---
lang: "de"
title: "Boot-Prozess: BIOS"
meta_description: "Erfahren Sie mehr über den Linux-Bootprozess, BIOS und MBR. Verstehen Sie, wie Ihr System startet, mit diesem anfängerfreundlichen Leitfaden. Entdecken Sie UEFI-Konzepte!"
meta_keywords: "Linux-Bootprozess, BIOS, MBR, UEFI, Linux-Tutorial, Bootloader, Linux für Anfänger, Systemstart"
---

## Lesson Content

### BIOS

Der erste Schritt im Linux-Bootprozess ist das BIOS, das Systemintegritätsprüfungen durchführt. Das BIOS ist eine Firmware, die am häufigsten in IBM PC-kompatiblen Computern vorkommt, dem heute dominierenden Computertyp. Sie haben wahrscheinlich die BIOS-Firmware verwendet, um die Bootreihenfolge Ihrer Festplatten zu ändern, die Systemzeit, die MAC-Adresse Ihres Computers usw. zu überprüfen. Das Hauptziel des BIOS ist es, den System-Bootloader zu finden.

Sobald das BIOS die Festplatte hochfährt, sucht es nach dem Bootblock, um herauszufinden, wie das System gestartet werden soll. Je nachdem, wie Sie Ihre Festplatte partitionieren, wird es den Master Boot Record (MBR) oder GPT berücksichtigen. Der MBR befindet sich im ersten Sektor der Festplatte, den ersten 512 Bytes. Der MBR enthält den Code, um ein anderes Programm irgendwo auf der Festplatte zu laden; dieses Programm lädt wiederum tatsächlich unseren Bootloader.

Wenn Sie Ihre Festplatte mit GPT partitioniert haben, ändert sich der Speicherort des Bootloaders ein wenig.

### UEFI

Es gibt eine andere Möglichkeit, Ihr System zu starten, anstatt das BIOS zu verwenden, und das ist mit UEFI (steht für "Unified Extensible Firmware Interface"). UEFI wurde entwickelt, um der Nachfolger des BIOS zu sein; die meisten heutigen Hardware wird mit integrierter UEFI-Firmware geliefert. Macintosh-Computer verwenden seit Jahren EFI-Booting, und Windows hat die meisten ihrer Dinge auf UEFI-Booting umgestellt. Das GPT-Format war für die Verwendung mit EFI vorgesehen. Sie benötigen EFI nicht unbedingt, wenn Sie eine GPT-Festplatte booten. Der erste Sektor einer GPT-Festplatte ist für einen "schützenden MBR" reserviert, um das Booten einer BIOS-basierten Maschine zu ermöglichen.

UEFI speichert alle Informationen über den Start in einer `.efi`-Datei. Diese Datei wird auf einer speziellen Partition namens EFI System Partition auf der Hardware gespeichert. Innerhalb dieser Partition befindet sich der Bootloader. UEFI bietet viele Verbesserungen gegenüber der traditionellen BIOS-Firmware. Da wir jedoch Linux verwenden, verwenden die meisten von uns das BIOS. Daher werden alle diese Lektionen von dieser Prämisse ausgehen.

## Exercise

Gehen Sie in Ihr BIOS-Menü und prüfen Sie, ob UEFI-Booting aktiviert ist.

## Quiz Question

Was lädt das BIOS?

## Quiz Answer

bootloader
