---
lesson_id: "boot-process-overview"
course_id: "boot-system"
lang: "de"
order_index: 1
title: "Überblick über den Bootvorgang"
description: "Lerne die wichtigsten Übergaben von der Plattform-Firmware über den Kernel bis zum ersten Prozess im Userspace kennen."
meta_title: "Überblick über den Bootvorgang – Systemstart"
meta_description: "Ein klarer Überblick über den Linux-Bootvorgang und seine wichtigsten Stationen: Firmware, Bootloader, Kernel, früher Userspace und Init-System."
meta_keywords: "Linux Bootvorgang, Bootvorgang Linux, Startvorgang Linux, Linux Betriebssystem starten, BIOS, UEFI, Bootloader, Kernel, Init, Linux Tutorial"
---

Der Bootvorgang ist eine Kette von Vertrauens- und Kontrollübergaben, die aus dem Zurücksetzen der Plattform eine laufende Userspace-Umgebung macht. Ein verbreiteter Ablauf auf PCs lässt sich als Firmware, Bootmanager oder Bootloader, Kernel mit optionalem frühem Userspace und Init-System mit PID 1 zusammenfassen. Andere Architekturen, virtuelle Maschinen, eingebettete Systeme und Container können abweichende Wege verwenden.

## Initialisierung durch die Firmware

Die Plattform-Firmware initialisiert genügend Zustand von CPU, Arbeitsspeicher und Geräten, um ein Bootziel auszuwählen. Herkömmliche PCs verwenden BIOS-Konventionen; aktuelle PCs arbeiten meist mit UEFI. Firmware-Einstellungen, Bootreihenfolge, Plattformprüfung und Secure-Boot-Richtlinien können bestimmen, welche ausführbare Datei der nächsten Stufe gestartet werden darf.

Die Firmware versteht nicht zwangsläufig das installierte Linux-Root-Dateisystem. Sie findet einen Bootpfad gemäß ihrer Schnittstelle, beispielsweise BIOS-Bootcode auf einem ausgewählten Datenträger oder einen UEFI-Booteintrag, der auf eine EFI-Datei auf einer EFI-Systempartition verweist.

:::single-choice{#boot-overview-first-stage} Welche Komponente beginnt auf einem typischen PC nach dem Zurücksetzen mit der Initialisierung der Plattform?

::option[Die interaktive Shell des Benutzers.]{#boot-overview-shell explanation="Eine Shell wird erst viel später durch Userspace-Dienste oder den Anmeldevorgang gestartet."}
::option[Die Plattform-Firmware wie BIOS oder UEFI.]{#boot-overview-firmware .correct explanation="Die Firmware stellt den frühen Hardwarezustand her und wählt das nächste Bootziel aus, bevor Linux ausgeführt wird."}
::option[Das Dienstprogramm zur Dateisystemreparatur.]{#boot-overview-fsck explanation="Eine Prüfung kann gemäß der Bootrichtlinie später beteiligt sein, ist aber nicht die erste Firmware-Stufe."}
:::

## Bootloader oder Bootmanager

Ein Bootloader wie GRUB kann Einträge anzeigen, einen ausgewählten Linux-Kernel und ein initiales RAM-Dateisystem in den Speicher laden, die Kernel-Befehlszeile zusammenstellen und die Kontrolle übergeben. UEFI kann auch einen als EFI-Datei gebauten Kernel direkt laden. Ein getrennter mehrstufiger Bootloader ist daher zwar verbreitet, aber nicht universell.

Die ausgewählten Artefakte müssen zusammenpassen: Kernel-Version, Inhalt der initramfs, Root-Kennung, Sicherheitssignaturen und Befehlszeilenoptionen beeinflussen, ob die nächste Übergabe gelingt.

:::single-choice{#boot-overview-loader-role} Was gehört häufig zu den Aufgaben eines Linux-Bootloaders?

::option[Einen ausgewählten Kernel laden und seine Befehlszeile übergeben.]{#boot-overview-load-kernel .correct explanation="Der Bootloader bereitet das Kernel-Abbild und seine Parameter vor, häufig zusammen mit einer initramfs."}
::option[Bei jedem Start alle Benutzerkonten von Grund auf neu anlegen.]{#boot-overview-create-users explanation="Dauerhafte Kontendatenbanken sind Userspace-Konfiguration und werden nicht vom Bootloader neu erstellt."}
::option[Nach der Anmeldung jeden Anwendungsprozess einplanen.]{#boot-overview-schedule-apps explanation="Die CPU-Ablaufplanung ist Aufgabe des laufenden Kernels."}
:::

## Kernel und früher Userspace

Der Kernel dekomprimiert oder verschiebt sich nach Bedarf, initialisiert zentrale Subsysteme, wertet seine Befehlszeile aus und erkennt verfügbare Hardware. Eine initramfs kann Module und frühe Werkzeuge für Speichererkennung, RAID, Verschlüsselung, LVM, Netzwerk oder andere Arbeiten bereitstellen, die zum Zusammensetzen des eigentlichen Root-Dateisystems nötig sind.

Sobald das vorgesehene Root-Dateisystem verfügbar ist, wechselt der frühe Userspace dorthin und der Kernel führt das konfigurierte erste Userspace-Programm aus. Einzelheiten wie die Zuständigkeit für Dateisystemprüfungen oder das erneute Einhängen mit Schreibzugriff gehören zum Bootdesign der jeweiligen Distribution und nicht zu einer universellen Abfolge.

:::single-choice{#boot-overview-initramfs-purpose} Warum kann ein System eine initramfs verwenden?

::option[Um die Desktop-Sitzung jedes Benutzers dauerhaft in der Firmware zu speichern.]{#boot-overview-desktop-firmware explanation="Eine initramfs ist ein Dateisystemabbild für den Systemstart und kein Firmware-Speicher für Sitzungen."}
::option[Um frühe Werkzeuge und Treiber bereitzustellen, die zum Erreichen des eigentlichen Root-Dateisystems nötig sind.]{#boot-overview-early-root-tools .correct explanation="Der frühe Userspace kann verschlüsselten, logischen, netzgebundenen oder treiberabhängigen Root-Speicher zusammensetzen."}
::option[Um nach der Anmeldung den Prozess-Scheduler des Kernels zu ersetzen.]{#boot-overview-replace-scheduler explanation="Der Kernel bleibt während des gesamten Betriebs für die Ablaufplanung zuständig."}
:::

## PID 1 und Systembereitschaft

Der erste Userspace-Prozess erhält PID 1. Auf vielen Distributionen ist dies systemd; andere Systeme verwenden sysvinit, OpenRC, runit, BusyBox init oder ein spezialisiertes Programm. PID 1 richtet die Dienstumgebung im Userspace ein, räumt verwaiste Kindprozesse auf und übernimmt Aufgaben beim Herunterfahren.

Das Erreichen von PID 1 bedeutet nicht, dass das System vollständig bereit ist. Dienste können noch starten, Speicher kann noch eingehängt und das Netzwerk konfiguriert werden. Eine grafische oder Konsolenanmeldung ist nur einer von mehreren möglichen Zielzuständen.

:::single-choice{#boot-overview-final-stage} Was leitet die hauptsächliche Initialisierung des Userspace ein?

::option[Das Anlegen des Protective MBR des Datenträgers bei jedem Start.]{#boot-overview-create-mbr explanation="Das Erstellen einer Partitionstabelle ist keine normale, wiederkehrende Bootstufe."}
::option[Das Löschen aller Kernel-Befehlszeilenparameter.]{#boot-overview-delete-command-line explanation="Der Kernel wertet seine Befehlszeile aus und stellt sie bereit; eine solche Löschung ist nicht erforderlich."}
::option[Die Ausführung des Init-Programms mit PID 1.]{#boot-overview-pid-one .correct explanation="Nach dem Einrichten des Root-Dateisystems startet oder überwacht der erste Userspace-Prozess die für den konfigurierten Systemzustand erforderlichen Dienste."}
:::

Das Lab [GRUB2-Bootmenü anpassen](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) zeigt einen möglichen Weg zur Konfiguration des Bootloaders. Nimm Änderungen nur in einem wiederherstellbaren Lab-System vor.

## Zusammenfassung

Du kannst nun die wichtigsten Übergaben des Linux-Bootvorgangs nachvollziehen, ohne ihre konkrete Umsetzung für universell zu halten.

1. Beginne mit der Firmware-Initialisierung und der Auswahl des Bootziels.
2. Ordne dem Bootloader die Auswahl von Kernel, initramfs und Befehlszeile zu.
3. Nutze den frühen Userspace, um den Aufbau komplexer Root-Dateisysteme zu verstehen.
4. Betrachte PID 1 als Beginn der Dienstinitialisierung und nicht als Beweis vollständiger Bereitschaft.
