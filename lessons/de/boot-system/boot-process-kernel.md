---
lesson_id: "boot-process-kernel"
course_id: "boot-system"
lang: "de"
order_index: 4
title: "Bootvorgang: Kernel"
description: "Lerne, wie der Kernel Hardware initialisiert, den frühen initramfs-Userspace ausführt, das eigentliche Root-Dateisystem erreicht und PID 1 startet."
meta_title: "Bootvorgang: Kernel – Systemstart"
meta_description: "Erkunde den Linux-Kernel-Bootvorgang: Initialisierung, initramfs, frühe Treiber, Wechsel zum eigentlichen Root-Dateisystem und Start von PID 1."
meta_keywords: "Boot Root, initramfs, Kernel Boot, Boot Partition, initramfs Ubuntu, Linux Bootvorgang, Root Dateisystem, Kernel Initialisierung"
---

Nachdem die Kontrolle den Linux-Kernel erreicht hat, initialisiert er Speicherverwaltung, Ablaufplanung, Interrupts, integrierte Treiber, Sicherheitsframeworks und weitere zentrale Subsysteme. Er wertet die Befehlszeile aus und bereitet den Start des ersten Userspace-Prozesses vor.

## Warum es einen frühen Userspace gibt

Ein einfaches Root-Dateisystem lässt sich manchmal mit fest in den Kernel eingebauten Treibern einhängen. Komplexere Systeme benötigen Module und Werkzeuge, bevor das eigentliche Root-Dateisystem erreichbar ist. Beispiele sind:

- Module für Speichercontroller oder Dateisysteme
- Entsperren eines verschlüsselten Root-Dateisystems
- Zusammensetzen von LVM oder RAID
- Netzwerkkonfiguration für ein Root-Dateisystem im Netzwerk
- Geräteerkennung und Auflösung dauerhafter Kennungen

Eine initramfs bündelt diese Komponenten in einer frühen Userspace-Umgebung, die zusammen mit dem Kernel bereitgestellt wird.

:::single-choice{#boot-kernel-initramfs-purpose}
Welches Problem löst eine initramfs häufig?

::option[Sie stellt frühe Werkzeuge und Module bereit, die vor dem eigentlichen Root-Dateisystem benötigt werden.]{#boot-kernel-early-tools .correct explanation="Der frühe Userspace kann Speicher erkennen und zusammensetzen, auf den der Kernel allein mit integrierter Unterstützung nicht zugreifen kann."}
::option[Sie speichert die dauerhaften Home-Verzeichnisse aller Benutzer in der Firmware.]{#boot-kernel-home-firmware explanation="Das Archiv ist ein Bootartefakt und kein dauerhafter Speicher für Benutzerdaten."}
::option[Sie ersetzt den Linux-Kernel nach der ersten Anmeldung.]{#boot-kernel-replace-kernel explanation="Der Kernel bleibt aktiv, während initramfs-Code im Userspace ausgeführt wird."}
:::

## Initramfs und ältere Initrd

Eine moderne initramfs besteht üblicherweise aus einem oder mehreren, oft komprimierten cpio-Archiven, die der Kernel in sein anfängliches Root-Dateisystem entpackt. Aus dieser Umgebung führt der Kernel ein frühes `/init`-Programm aus.

Eine ältere initrd ist konzeptionell ein Dateisystemabbild, das in ein RAM-gestütztes Blockgerät geladen und eingehängt wird. In Dateinamen und Bootloader-Befehlen werden die Begriffe häufig unscharf verwendet. Prüfe deshalb die tatsächlich eingesetzten Werkzeuge, statt das Format allein aus der Bezeichnung abzuleiten.

Die initramfs muss zum Kernel und zum Bootdesign passen. Fehlende Module, veraltete Gerätekennungen oder nicht enthaltene Kryptografie- und LVM-Werkzeuge können einen neu installierten Kernel unbootbar machen, obwohl sein Abbild selbst gültig ist.

:::single-choice{#boot-kernel-initramfs-format}
In welcher Form wird dem Kernel eine moderne initramfs häufig bereitgestellt?

::option[Ausschließlich als interaktives Paketrepository über HTTP.]{#boot-kernel-http-repository explanation="Ein Netzwerkzugang kann im frühen Userspace konfiguriert werden, bestimmt aber nicht das initramfs-Format."}
::option[Als cpio-basiertes Archiv, das in das anfängliche Root-Dateisystem entpackt wird.]{#boot-kernel-cpio-archive .correct explanation="Der Kernel entpackt das Archiv und führt dessen frühes Userspace-Initialisierungsprogramm aus."}
::option[Als GPT-Sicherungskopf des Datenträgers.]{#boot-kernel-gpt-header explanation="Die Redundanz der Partitionstabelle ist unabhängig vom Archiv des frühen Userspace."}
:::

## Das eigentliche Root-Dateisystem erreichen

Der frühe Userspace wertet Parameter wie `root=` aus, wartet auf die erforderlichen Geräte, aktiviert Speicherebenen und hängt das vorgesehene Root-Dateisystem ein. Anschließend macht er dieses Dateisystem mit einem Root-Wechsel zum neuen `/` und gibt die temporäre frühe Umgebung soweit möglich frei.

Die anfängliche Befehlszeilenanforderung `ro` kann Konsistenzprüfungen und einen kontrollierten Start unterstützen, doch die genaue Abfolge hängt von der Distribution ab. Dateisystemprüfungen sind Userspace-Vorgänge. Die initramfs oder das spätere Init-System kann das Root-Dateisystem mit Schreibzugriff neu einhängen, sofern die Richtlinie dies erlaubt.

:::single-choice{#boot-kernel-root-switch}
Was geschieht, nachdem der frühe Userspace das vorgesehene eigentliche Root-Dateisystem erfolgreich eingehängt hat?

::option[Die Partitionstabelle jedes Datenträgers wird neu erstellt.]{#boot-kernel-recreate-tables explanation="Ein Root-Wechsel partitioniert keine Datenträger neu."}
::option[Der Kernel wird beendet und die Firmware übernimmt die normale Prozessplanung.]{#boot-kernel-firmware-schedules explanation="Der Linux-Kernel bleibt nach der Übergabe für Prozesse und Hardware zuständig."}
::option[Der Bootvorgang wechselt die Root-Ansicht zu diesem Dateisystem und setzt den Userspace-Start fort.]{#boot-kernel-switch-root .correct explanation="Das temporäre frühe Root-Dateisystem übergibt an die Root-Hierarchie des installierten Systems."}
:::

## PID 1 starten

Der Kernel führt das konfigurierte Init-Programm aus, das normalerweise über einen Pfad wie `/sbin/init` erreicht oder mit `init=` ausgewählt wird. Dieser Prozess erhält PID 1 und übernimmt die hauptsächliche Userspace-Dienstumgebung.

Kann kein verwendbares Init-Programm ausgeführt werden, erreicht der Kernel kein normales Userspace-System und meldet üblicherweise einen Bootfehler oder eine Kernel Panic. Untersuche die früheste fehlerhafte Ebene: Kernel und Befehlszeile, initramfs-Inhalt, Root-Erkennung, Root-Einhängung oder Ausführung von PID 1.

:::single-choice{#boot-kernel-pid-one}
Was ist in dieser vereinfachten Bootstufe die letzte große Übergabe des Kernels?

::option[Das erste Userspace-Programm als PID 1 ausführen.]{#boot-kernel-exec-init .correct explanation="PID 1 startet anschließend Dienste und stellt den konfigurierten Systemzustand her."}
::option[`/proc` in eine dauerhafte Paketdatenbank umwandeln.]{#boot-kernel-proc-package explanation="Procfs bleibt eine Laufzeitschnittstelle des Kernels."}
::option[Jedem späteren Prozess dieselbe PID zuweisen.]{#boot-kernel-same-pid explanation="Jeder laufende Prozess erhält innerhalb eines Namespace eine eigene PID."}
:::

## Zusammenfassung

Du kannst den Kernel-Start nun durch den frühen Userspace bis zu PID 1 verfolgen.

1. Trenne die integrierte Kernel-Initialisierung von früh ladbaren Modulen.
2. Ordne die initramfs einem cpio-basierten temporären Root-Dateisystem und `/init` zu.
3. Verfolge das Zusammensetzen des Speichers und den Wechsel zum eigentlichen Root-Dateisystem.
4. Erkenne die Ausführung von PID 1 als Übergabe an den Userspace.
