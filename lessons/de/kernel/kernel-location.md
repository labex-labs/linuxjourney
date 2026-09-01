---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "de"
order_index: 5
title: "Speicherort des Kernels"
description: "Erfahre, wo Distributionen Kernelabbilder, initramfs-Dateien, Konfiguration, Symbole und versionierte Module ablegen."
meta_title: "Speicherort des Kernels – Kernel"
meta_description: "Entdecke, wo der Kernel unter Linux gespeichert ist. Dieser Leitfaden erklärt den Speicherort des Linux-Kernels im Verzeichnis /boot und beschreibt wichtige Dateien wie vmlinuz und initrd."
meta_keywords: "Speicherort des Linux-Kernels, wo ist der Kernel, Kernel-Speicherort, wo befindet sich der Kernel, wo wird der Kernel unter Linux gespeichert, vmlinuz, Verzeichnis /boot"
---

Linux-Distributionen speichern startfähige Kernelartefakte gewöhnlich unter `/boot`. UEFI- und Boot-Loader-Specification-Layouts können Artefakte jedoch auch auf einer EFI-Systempartition oder erweiterten Bootpartition ablegen, die unter Pfaden wie `/boot`, `/boot/efi` oder `/efi` eingehängt ist. Prüfe Einhängepunkte und die Bootloaderkonfiguration, statt einen universellen Pfad anzunehmen.

## Versionierte Dateien unter `/boot`

Ein traditionelles Distributionslayout kann Folgendes enthalten:

- `vmlinuz-KERNEL_RELEASE`: ein startfähiges Linux-Kernelabbild
- `initrd.img-KERNEL_RELEASE` oder `initramfs-KERNEL_RELEASE.img`: ein frühes User-Space-Abbild
- `config-KERNEL_RELEASE`: die für den Build dieses paketierten Kernels verwendete Konfiguration
- `System.map-KERNEL_RELEASE`: eine Symbol-Adress-Zuordnung aus dem Kernel-Build

Die Namen unterscheiden sich. Eine auf einem modernen System als `initrd` benannte Datei enthält häufig ein initramfs-Archiv. Aus der Namenskonvention `vmlinuz` lassen sich weder die genaue interne Komprimierung noch das plattformspezifische Startformat ableiten; prüfe die Datei mit Distributionswerkzeugen.

:::single-choice{#kernel-location-vmlinuz} Was enthält eine versionierte Datei `vmlinuz-*` gewöhnlich?

::option[Ein startfähiges Linux-Kernelabbild.]{#kernel-location-kernel-image .correct explanation="Der Bootloader oder die Firmware lädt dieses architekturspezifische Kernelartefakt."}
::option[Jedes ladbare Modul für alle installierten Kernel.]{#kernel-location-all-modules explanation="Module werden getrennt in einem veröffentlichungsspezifischen Modulbaum gespeichert."}
::option[Den Shell-Verlauf des Benutzers vom vorherigen Start.]{#kernel-location-shell-history explanation="Startfähige Kernelabbilder enthalten keinen persönlichen Befehlsverlauf."}
:::

## Initiales RAM-Dateisystem und Build-Metadaten

Das initramfs muss die frühen Module und Werkzeuge enthalten, die sein zugehöriger Kernel und der Aufbau des Root-Speichers benötigen. Ein übereinstimmender Dateiname reicht nicht aus; eine veraltete oder fehlgeschlagene Erzeugung kann weiterhin einen unbrauchbaren Starteintrag hervorbringen.

`config-*` hilft zu verstehen, welche Funktionen fest eingebaut, modular oder ausgelassen wurden. `System.map-*` kann bei der Symbolisierung und Fehlersuche helfen, doch Adressrandomisierung, getrennte Debuginformationen und Distributionswerkzeuge beeinflussen seine Verwendung. Diese Dateien sind unterstützende Artefakte und keine alternativen Kernel.

:::single-choice{#kernel-location-initramfs-match} Warum ist ein initramfs an eine bestimmte Kernelveröffentlichung und Systemkonfiguration gebunden?

::option[Es speichert den dauerhaften Inhalt jedes eingehängten Dateisystems.]{#kernel-location-all-filesystems explanation="Ein initramfs ist eine kleine frühe Startumgebung und keine vollständige Systemsicherung."}
::option[Es weist Benutzern bei jedem Start neue UIDs zu.]{#kernel-location-user-ids explanation="Die Verwaltung von Kontoidentitäten gehört nicht zu seiner gewöhnlichen Aufgabe."}
::option[Es enthält frühe Module und Werkzeuge, die dieser Startpfad benötigt.]{#kernel-location-early-modules .correct explanation="Modul-ABI und erforderliche Komponenten zur Speicherzusammensetzung müssen mit dem ausgewählten Kernel übereinstimmen."}
:::

## Versionierte Kernelmodule

Ladbare Module für die laufende Veröffentlichung befinden sich gewöhnlich unter:

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

Bei zusammengeführten Dateisystemlayouts kann dies zu `/usr/lib/modules/KERNEL_RELEASE` aufgelöst werden. Jeder installierte Kernel benötigt einen kompatiblen Modulbaum und Abhängigkeitsindizes. `modprobe` verwendet veröffentlichungsspezifische Metadaten, statt beliebige `.ko`-Dateien auf dem gesamten Datenträger zu durchsuchen.

:::single-choice{#kernel-location-module-tree} Welches Verzeichnis enthält konventionsgemäß die Module für die laufende Kernelveröffentlichung?

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="Benutzer-Home-Verzeichnisse sind nicht der standardmäßige Systemmodulbaum."}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="Die Veröffentlichungskomponente trennt Modul-ABI und Abhängigkeitsdaten für jeden installierten Kernel."}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="`/proc/modules` meldet geladene Module und ist kein Verzeichnis mit Modulbinärdateien."}
:::

## Unified Kernel Images und Firmwarepfade

Ein Unified Kernel Image oder UKI ist eine einzelne signierte EFI-Programmdatei, die Kernel, initrd, Befehlszeile und Metadaten bündeln kann. UKIs werden gewöhnlich an einem für EFI zugänglichen Startort gespeichert, statt durch getrennte `vmlinuz`- und initramfs-Dateien dargestellt zu werden.

Ein leer wirkendes traditionelles `/boot`-Layout beweist daher nicht, dass kein Kernel installiert ist. Verwende `findmnt`, die Paketdatenbank, Bootmanagerwerkzeuge und die Konfiguration des Bootloaders, um die aktiven Artefakte zuzuordnen.

:::single-choice{#kernel-location-uki} Was kann ein Unified Kernel Image verbinden?

::option[Alle Benutzer-Home-Verzeichnisse in einem GPT-Header.]{#kernel-location-uki-homes explanation="Ein UKI ist eine ausführbare Startdatei und weder ein Benutzerdatencontainer noch eine Partitionstabelle."}
::option[Jedes installierte Paket in einem einzelnen Shell-Skript.]{#kernel-location-uki-packages explanation="Es paketiert Startkomponenten und nicht die vollständige Betriebssystem-Paketquelle."}
::option[Kernel, initrd, Befehlszeile und Metadaten in einer EFI-Programmdatei.]{#kernel-location-uki-components .correct explanation="Das kombinierte Artefakt kann an einem signierten UEFI-Startablauf teilnehmen."}
:::

## Speicherplatz sicher verwalten

Wenn das Bootdateisystem voll ist, ordne zuerst die eingehängten Bootpfade zu und frage ab, welchem Paket jedes Artefakt gehört. Verwende den Kernelbereinigungsablauf der Paketverwaltung, bewahre den laufenden Kernel und einen bekanntermaßen funktionierenden Fallback, erzeuge oder prüfe Starteinträge und kontrolliere anschließend den freien Speicherplatz.

Lösche `vmlinuz`, initramfs, UKI oder Modulbäume nicht allein aufgrund ihres Alters manuell. Eine Datei kann der einzige startfähige Wiederherstellungseintrag sein, selbst wenn sie derzeit nicht läuft.

## Zusammenfassung

Du kannst nun ein Kernelpaket seinen Start- und Modulartefakten zuordnen.

1. Prüfe die tatsächlichen Einhängepunkte für `/boot` und EFI.
2. Unterscheide Kernelabbild, initramfs, Konfiguration und Symbolzuordnung.
3. Ordne Modulbäume exakt der Kernelveröffentlichung zu.
4. Berücksichtige Unified Kernel Images und distributionsspezifische Layouts.
5. Gib Startspeicher nur mit einem verifizierten Paket- und Fallbackplan frei.
