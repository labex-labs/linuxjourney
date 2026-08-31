---
lesson_id: "boot-process-bios"
course_id: "boot-system"
lang: "de"
order_index: 2
title: "Bootvorgang: BIOS"
description: "Lerne, wie die ältere BIOS- und die moderne UEFI-Firmware die nächste Bootstufe finden und autorisieren."
meta_title: "Bootvorgang: BIOS – Systemstart"
meta_description: "Lerne die erste Stufe des Linux-Bootvorgangs kennen: BIOS und UEFI, MBR- und GPT-Datenträger, EFI-Systempartition sowie Secure Boot."
meta_keywords: "Linux Bootvorgang, BIOS, MBR, UEFI, BIOS Linux, BIOS starten, Bootloader, Systemstart, Secure Boot, EFI Systempartition"
---

Die Firmware wird vor dem Linux-Kernel ausgeführt. Auf PC-Hardware sind die beiden wichtigsten Schnittstellen das ältere BIOS und UEFI. Sie verwenden unterschiedliche Modelle zur Ermittlung des Bootpfads. Die Aussage „Das BIOS liest den Bootloader“ beschreibt daher nur einen möglichen Weg.

## Booten mit einem älteren BIOS

Nach der frühen Plattforminitialisierung und der Auswahl des Bootgeräts liest ein älteres BIOS üblicherweise den ersten 512 Byte großen Sektor des ausgewählten Datenträgers und übergibt die Kontrolle an dessen Bootcode, sofern der Sektor die erwartete Signatur besitzt.

Bei einem MBR-Aufbau enthält dieser Sektor einen kleinen Bereich für Bootcode, vier Partitionseinträge und eine Signatur. Der Code ist zu klein für einen funktionsreichen Bootloader und sucht deshalb häufig eine weitere Stufe an einer anderen Stelle des Datenträgers oder in einem Dateisystem.

Ein BIOS-Start von einem GPT-Datenträger ist möglich, doch der Protective MBR allein enthält nicht die späteren Stufen des Bootloaders. GRUB verwendet auf GPT dafür häufig eine kleine BIOS-Bootpartition mit eingebettetem Kerncode. Der genaue Aufbau hängt vom installierten Bootloader ab.

:::single-choice{#boot-bios-legacy-first-sector}
Was lädt ein älteres BIOS üblicherweise zuerst vom ausgewählten Bootdatenträger?

::option[Den anfänglichen Bootsektor mit kleinem Bootcode.]{#boot-bios-boot-sector .correct explanation="Der ältere Festplattenpfad der Firmware übergibt die Kontrolle an Code im ersten Sektor des ausgewählten Datenträgers."}
::option[Das gesamte Linux-Root-Dateisystem in den Firmware-Speicher.]{#boot-bios-entire-root explanation="Der Sektor der ersten Stufe ist sehr klein; spätere Software findet den Kernel und den Root-Speicher."}
::option[Alle Konfigurationen von Benutzerdiensten unter `/etc`.]{#boot-bios-etc-config explanation="Die Firmware wertet nicht die vollständige Dienstkonfiguration des installierten Systems aus."}
:::

## Booten mit UEFI

UEFI-Firmware kann ein definiertes Dateisystem auf einer EFI-Systempartition (ESP) lesen und ausführbare EFI-Dateien laden. In nichtflüchtigen Variablen gespeicherte Firmware-Booteinträge geben normalerweise Datenträger, Partition und Dateipfad an. Für Wechselmedien oder Wiederherstellungsfälle steht ein standardisierter Ersatzpfad zur Verfügung.

Die ESP enthält Bootanwendungen und unterstützende Dateien, nicht „alle Startinformationen“. Kernel-Abbilder, initramfs-Dateien und Bootloader-Konfiguration können sich abhängig vom Bootdesign dort oder an anderer Stelle befinden. GPT ist für UEFI-Systeme üblich, doch Firmware-Schnittstelle und Partitionstabellenschema bleiben getrennte Ebenen.

:::single-choice{#boot-bios-uefi-esp}
Was lädt UEFI üblicherweise von einer EFI-Systempartition?

::option[Eine durch einen Firmware-Booteintrag ausgewählte ausführbare EFI-Datei.]{#boot-bios-efi-executable .correct explanation="Die UEFI-Bootverwaltung verweist die Firmware auf eine ausführbare Datei auf einer unterstützten Systempartition."}
::option[Ein POSIX-Shellskript aus einem beliebigen ext4-Home-Verzeichnis.]{#boot-bios-shell-script explanation="Die Firmware lädt definierte ausführbare Formate von unterstützten Bootpfaden, statt eine gewöhnliche Benutzershell auszuführen."}
::option[Eine erweiterte MBR-Partition mit Benutzerkonten.]{#boot-bios-extended-users explanation="Kontodaten stehen in keinem Zusammenhang mit der Suche nach ausführbaren UEFI-Dateien."}
:::

## Secure Boot und Vertrauen

Ist Secure Boot aktiviert, überprüft UEFI anhand der hinterlegten Plattformschlüssel und Richtlinien die Signaturen innerhalb der Bootkette. Eine Linux-Distribution kann diese Kette mit einem signierten Shim, Bootloader, Kernel und einer Richtlinie für Kernelmodule fortsetzen.

Secure Boot verschlüsselt den Datenträger nicht und beweist nicht, dass jedes Userspace-Programm sicher ist. Es hilft dabei, die Annahme nicht autorisierten Codes vor dem Systemstart gemäß der konfigurierten Vertrauensrichtlinie zu verhindern.

:::single-choice{#boot-bios-secure-boot-purpose}
Was setzt UEFI Secure Boot in erster Linie durch?

::option[Die automatische Verschlüsselung jeder Datei auf jedem Datenträger.]{#boot-bios-secure-encryption explanation="Für die Vertraulichkeit von Datenträgern ist ein getrenntes Verschlüsselungssystem erforderlich."}
::option[Die signaturbasierte Autorisierung ausführbarer Dateien in der Bootkette.]{#boot-bios-secure-signatures .correct explanation="Firmware und später geprüfte Komponenten akzeptieren Code anhand hinterlegter Schlüssel und Richtlinien."}
::option[Die garantierte Abwesenheit von Schwachstellen in signierter Software.]{#boot-bios-secure-no-vulnerabilities explanation="Eine gültige Signatur belegt Autorisierung und Integrität, aber keine Fehlerfreiheit des Codes."}
:::

## Firmware-Einstellungen aufrufen

Die Taste zum Aufrufen der Firmware-Einstellungen hängt von Hersteller und Modell ab. Häufig sind es Entf, Esc oder eine Funktionstaste während der frühen Startphase. Schlage in der Gerätedokumentation nach, statt Einstellungen auf gut Glück zu verändern. Einige UEFI-Systeme bieten außerdem eine Betriebssystemanforderung für einen Neustart direkt in die Firmware-Einstellungen.

Notiere vorhandene Werte und Wiederherstellungsschlüssel, bevor du Secure Boot, den Modus des Speichercontrollers, TPM, Virtualisierung oder die Bootreihenfolge änderst. Eine Firmware-Änderung kann verschlüsselte Datenträger oder das installierte Betriebssystem vorübergehend unzugänglich machen.

:::single-choice{#boot-bios-setup-key}
Warum gibt es keine universelle Taste zum Aufrufen der Firmware-Einstellungen?

::option[Linux weist nach jedem Start zufällig eine neue Taste zu.]{#boot-bios-random-key explanation="Das Betriebssystem legt die Taste der frühen Firmware-Startphase nicht zufällig fest."}
::option[Taste und Zeitpunkt werden vom Systemhersteller festgelegt.]{#boot-bios-vendor-key .correct explanation="Firmware-Schnittstellen unterscheiden sich zwischen Modellen, weshalb die maßgebliche Gerätedokumentation erforderlich ist."}
::option[Die Einstellungen lassen sich nur nach dem Löschen des Bootloaders öffnen.]{#boot-bios-delete-loader explanation="Die Firmware-Einstellungen sind unabhängig von der Zerstörung installierter Bootdateien."}
:::

## Zusammenfassung

Du kannst nun die Modelle zur Bootpfadermittlung von älterem BIOS und UEFI unterscheiden.

1. Ordne dem älteren BIOS den Bootcode im ersten Sektor und spätere Bootloader-Stufen zu.
2. Ordne UEFI-Booteinträge ausführbaren EFI-Dateien auf einer ESP zu.
3. Betrachte GPT, Firmware-Schnittstelle und Bootloader-Aufbau als getrennte Entscheidungen.
4. Ändere Vertrauens- und Speichereinstellungen der Firmware nur mit einem Wiederherstellungsweg.
