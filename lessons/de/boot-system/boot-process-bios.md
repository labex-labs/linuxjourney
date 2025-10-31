---
index: 2
lang: "de"
title: "Bootvorgang: BIOS"
meta_title: "Bootvorgang: BIOS - System starten"
meta_description: "Entdecken Sie den ersten Schritt des Linux-Bootvorgangs: das BIOS. Erfahren Sie, wie es den Bootloader über MBR oder GPT findet, und verstehen Sie die Rolle von UEFI. Diese Anleitung erklärt den Systemstart und berührt, wie man für die Konfiguration ins BIOS bootet."
meta_keywords: "Linux Bootvorgang, BIOS, MBR, UEFI, BIOS in Linux, BIOS Linux, ins BIOS booten, Bootloader, Systemstart"
---

## Lesson Content

Der erste Schritt im Linux-Bootvorgang ist das BIOS (Basic Input/Output System), das beim Hochfahren wichtige Systemintegritätsprüfungen durchführt. Das BIOS ist eine Firmware, die üblicherweise in IBM PC-kompatiblen Computern zu finden ist, welche die Mehrheit der heute verwendeten Computer ausmachen.

### Die Rolle des BIOS unter Linux

Wenn Sie Ihren Computer einschalten, ist das **BIOS unter Linux**-Systemen die erste Software, die ausgeführt wird. Seine Hauptfunktion besteht darin, die Systemhardware wie CPU, Speicher und Festplatten zu initialisieren und zu testen. Sie haben wahrscheinlich schon einmal mit der BIOS-Firmware interagiert, um die Boot-Reihenfolge zu ändern, die Systemzeit zu überprüfen oder die MAC-Adresse Ihres Geräts anzuzeigen. Nachdem die Hardwareprüfungen abgeschlossen sind, besteht das Hauptziel des **bios linux**-Prozesses darin, den System-Bootloader zu lokalisieren und die Kontrolle an ihn zu übergeben.

### Wie das BIOS den Bootloader findet

Sobald das BIOS die Festplatte initialisiert hat, sucht es nach einem Boot-Block, um festzustellen, wie das Betriebssystem gestartet werden soll. Der Ort, den es überprüft, hängt vom Partitionierungsschema der Festplatte ab: Master Boot Record (MBR) oder GUID Partition Table (GPT).

Der MBR befindet sich in den ersten 512 Bytes der Festplatte. Dieser kleine Abschnitt enthält den anfänglichen Boot-Code und die Partitionstabelle. Der Code des MBR ist dafür verantwortlich, ein anderes Programm zu laden, welches wiederum unseren eigentlichen Bootloader lädt. Wenn Sie eine GPT-partitionierte Festplatte verwenden, ist der Prozess etwas anders.

### Wie man ins BIOS bootet

Viele Benutzer müssen wissen, **wie man ins BIOS bootet**, um Hardwareeinstellungen zu konfigurieren. Die Methode hierfür beinhaltet typischerweise das Drücken einer bestimmten Taste (wie F2, F10, DEL oder ESC) unmittelbar nach dem Einschalten des Computers. Zu wissen, **wie man ins bios bootet**, ist für Aufgaben wie das Ändern der Boot-Gerätepriorität oder das Aktivieren der Virtualisierungstechnologie unerlässlich. Die genaue Taste variiert je nach Hersteller, daher müssen Sie möglicherweise die Dokumentation Ihres Computers konsultieren.

### Der Aufstieg von UEFI

Eine Alternative zum traditionellen BIOS ist UEFI (Unified Extensible Firmware Interface). Als Nachfolger des BIOS konzipiert, ist UEFI heute auf den meisten modernen Geräten Standard. Es speichert alle Startinformationen in einer `.efi`-Datei, die sich auf einer dedizierten EFI System Partition (ESP) befindet. Diese Partition enthält den Bootloader für das installierte Betriebssystem.

UEFI bietet viele Verbesserungen gegenüber dem BIOS, darunter schnellere Bootzeiten und Unterstützung für größere Festplatten. Obwohl das GPT-Format für UEFI entwickelt wurde, sorgt ein "schützender MBR" auf GPT-Festplatten für Abwärtskompatibilität, wodurch es möglich ist, von ihnen auf älteren BIOS-basierten Maschinen zu booten. Obwohl viele Linux-Systeme heute UEFI verwenden, konzentriert sich dieser Leitfaden auf den traditionellen BIOS-Bootvorgang zum grundlegenden Verständnis.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis der Linux Benutzer- und Gruppenverwaltung zu festigen:

1. **[Linux-Benutzerkonten mit useradd, usermod und userdel verwalten](https://labex.io/de/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Üben Sie den gesamten Lebenszyklus der Benutzeradministration, vom Erstellen und Sichern neuer Konten bis hin zum Ändern und Löschen dieser.
2. **[Linux-Gruppen mit groupadd, usermod und groupdel verwalten](https://labex.io/de/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Sammeln Sie praktische Erfahrungen mit Befehlszeilenprogrammen für die Gruppenadministration, einschließlich der Erstellung neuer Gruppen, der Änderung von Benutzerzuordnungen und der Entfernung von Gruppen.
3. **[Benutzerkonten und Sudo-Berechtigungen unter Linux konfigurieren](https://labex.io/de/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Lernen Sie wesentliche Techniken zur Verwaltung von Benutzerkonten und Sudo-Berechtigungen kennen, um die Sicherheit eines Linux-Systems zu erhöhen.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Benutzer- und Gruppenverwaltung unter Linux aufzubauen.

## Quiz Question

Was lädt das BIOS? Bitte antworten Sie in einem einzigen Wort, auf Englisch und in Kleinbuchstaben.

## Quiz Answer

bootloader
