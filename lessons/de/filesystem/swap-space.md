---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "de"
order_index: 8
title: "Swap"
description: "Lerne, wie Linux Swap-Speicher verwendet, initialisiert, aktiviert, dimensioniert und sicher deaktiviert."
meta_title: "Swap – Das Dateisystem"
meta_description: "Lerne Linux-Swap als Ressource der Speicherverwaltung kennen und verwalte Swap-Geräte und -Dateien sicher mit mkswap, swapon und swapoff."
meta_keywords: "Linux Swap, mkswap, swapon, swapoff, /etc/fstab, virtueller Speicher, Swap Datei, zram"
---

Linux kann ausgewählte anonyme Speicherseiten zwischen RAM und Swap-gestütztem Speicher verschieben. Dadurch lässt sich inaktiver Speicher erhalten, während RAM für aktive Arbeitslasten und den Dateisystemcache frei wird. Speichergeräte sind jedoch wesentlich langsamer als RAM. Swap ist ein Werkzeug für Kapazität und Speicherverwaltung, kein Ersatz für ausreichenden Arbeitsspeicher oder ein Speicherlimit der Anwendung.

## Wie Swap an der Speicherverwaltung teilnimmt

Abhängig von Arbeitslast, Speicherdruck, cgroups und einstellbaren Werten wie Swappiness kann der Kernel Swap verwenden, bevor der RAM vollständig erschöpft ist. Saubere dateigestützte Seiten lassen sich häufig verwerfen und erneut aus ihren Dateien lesen. Anonyme Seiten benötigen dagegen Swap oder müssen im RAM bleiben.

Starkes dauerhaftes Swapping kann erhebliche Latenz oder Thrashing verursachen. Untersuche Speicherbedarf, Working Sets, Druck und Anwendungslimits, statt einen größeren Swap-Bereich als universelle Leistungsverbesserung zu behandeln.

:::single-choice{#swap-space-anonymous-pages}
Welcher Speicher ist ein hauptsächlicher Kandidat für die Ablage in Swap?

::option[Jede unter `/usr` installierte ausführbare Datei.]{#swap-space-installed-files explanation="Installierte Dateien bleiben in ihren Dateisystemen; saubere abgebildete Seiten können von dort erneut gelesen werden."}
::option[Inaktive anonyme Speicherseiten.]{#swap-space-anonymous-memory .correct explanation="Anonyme Seiten besitzen keine gewöhnliche zugrunde liegende Datei, aus der sie einfach erneut gelesen werden können."}
::option[Die Partitionstabelleneinträge des Datenträgers.]{#swap-space-partition-table explanation="Partitionsmetadaten bleiben auf dem Blockgerät und sind kein aus dem RAM ausgelagerter Prozessspeicher."}
:::

## Aktiven Swap untersuchen

Verwende zuerst schreibgeschützte Befehle:

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

Sie zeigen konfigurierte aktive Swap-Bereiche und zusammengefasste Speicherwerte. Ein Wert größer null bei „used“ ist nicht automatisch ein Problem. Setze ihn mit Swap-in-/Swap-out-Raten, Speicherdruck, Latenz und dem Verhalten der Arbeitslast in Beziehung.

:::single-choice{#swap-space-show-active}
Welcher Befehl listet aktive Swap-Bereiche in einer strukturierten Ansicht auf?

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="Der Show-Modus meldet aktive Swap-Dateien oder -Geräte und, soweit verfügbar, Größe, Nutzung und Priorität."}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="Mkswap initialisiert Swap-Signaturen und ist kein schreibgeschützter Befehl zur Auflistung aktiver Bereiche."}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="Das Standardwerkzeug zur Initialisierung ist `mkswap`; eine Formatierung ist keine Statusabfrage."}
:::

## Ein Swap-Gerät initialisieren und aktivieren

`mkswap` schreibt eine Swap-Signatur und zerstört die zuvor nutzbaren Metadaten des Ziels. Übe ausschließlich auf einem geprüften, entbehrlichen Ziel:

```bash
$ sudo mkswap /dev/GEPRUEFTES-SWAP-ZIEL
$ sudo swapon /dev/GEPRUEFTES-SWAP-ZIEL
```

Prüfe vor `mkswap` Modell, Seriennummer, Größe, dauerhafte Identität, vorhandene Signaturen, Einhängungen, RAID, LVM, Verschlüsselung und Sicherungen genauso wie vor `mkfs`. Bestätige nach der Aktivierung die genaue Quelle mit `swapon --show`.

Verwende für eine dauerhafte Konfiguration die Swap-UUID mit einem zur lokalen Richtlinie passenden Typ und passenden Optionen in `/etc/fstab`:

```text
UUID=GEPRUEFTE-SWAP-UUID none swap sw 0 0
```

:::single-choice{#swap-space-enable-command}
Welcher Befehl aktiviert einen initialisierten Swap-Bereich?

::option[`swapon`]{#swap-space-command-swapon .correct explanation="Swapon fügt der aktiven Swap-Gruppe des Kernels ein gültiges Swap-Gerät oder eine gültige Swap-Datei hinzu."}
::option[`mkswap`]{#swap-space-command-mkswap explanation="Mkswap initialisiert die Signatur, aktiviert den Bereich aber nicht selbst."}
::option[`mount`]{#swap-space-command-mount explanation="Swap wird über das Swap-Subsystem aktiviert und nicht als Verzeichnisdateisystem eingehängt."}
:::

## Swap-Dateien und andere Backends

Eine Swap-Datei kann flexible Kapazität ohne Neupartitionierung bereitstellen, doch die Anforderungen an ihre Erstellung hängen vom Dateisystem ab. Die Datei benötigt restriktive Berechtigungen, eine geeignete Zuweisung ohne nicht unterstützte Löcher oder Copy-on-Write-Verhalten, eine Swap-Signatur und Aktivierung. Folge der Dokumentation des Dateisystems und der Distribution, statt überall ein allgemeines `fallocate`-Rezept zu übernehmen.

Komprimierte RAM-Geräte wie zram können eine weitere Swap-Stufe mit anderen CPU- und Kapazitätsabwägungen bereitstellen. Verschlüsselter Swap kann ruhende Seiten schützen, während der Ruhezustand eine Resume-Konfiguration und genügend geeigneten Speicher erfordert. Diese Ziele beeinflussen Größe und Aufbau.

Es gibt keine universelle Regel, nach der Swap das Doppelte des RAM betragen muss. Dimensioniere ihn anhand von Lastspitzen, gewünschtem Fehlerverhalten, Anforderungen des Ruhezustands, Speicherlatenz und -haltbarkeit, Crash-Dump-Konzept und betrieblicher Überwachung.

:::single-choice{#swap-space-sizing-rule}
Was ist die beste Grundlage für die Dimensionierung von Swap?

::option[Immer genau das Doppelte des installierten RAM.]{#swap-space-twice-ram explanation="Diese historische Faustregel passt nicht zu jeder Arbeitslast oder modernen Speichergröße."}
::option[Gemessene Anforderungen der Arbeitslast, Ziele des Ruhezustands und Fehlerrichtlinie.]{#swap-space-sizing-requirements .correct explanation="Systemzweck und beobachtetes Speicherverhalten sind wichtiger als ein fester RAM-Multiplikator."}
::option[Immer null, sobald das System eine SSD besitzt.]{#swap-space-zero-ssd explanation="Der Speichertyp allein bestimmt weder Speicherdruck noch Anforderungen des Ruhezustands."}
:::

## Swap sicher deaktivieren

Deaktiviere einen bestimmten geprüften Bereich mit:

```bash
$ sudo swapoff /dev/GEPRUEFTES-SWAP-ZIEL
```

Der Kernel muss die darin vorhandenen ausgelagerten Seiten an anderer Stelle unterbringen. Wenn RAM und verbleibender Swap dafür nicht ausreichen, kann der Vorgang fehlschlagen oder gefährlichen Speicherdruck erzeugen. Beende oder begrenze zuerst Arbeitslasten, überwache den Speicher, entferne den dauerhaften fstab-Eintrag erst nach Prüfung des richtigen Ziels und bestätige die Deaktivierung mit `swapon --show`, bevor du den Speicher anders verwendest.

:::single-choice{#swap-space-swapoff-capacity}
Warum kann `swapoff` auf einem stark ausgelasteten System fehlschlagen oder es gefährden?

::option[Swapoff formatiert immer jedes RAM-Modul neu.]{#swap-space-formats-ram explanation="Der Befehl verändert die aktive Swap-Konfiguration und formatiert keine physische Speicherhardware."}
::option[Seiten in diesem Bereich benötigen Kapazität im RAM oder in anderem Swap.]{#swap-space-pages-need-capacity .correct explanation="Die Deaktivierung erfordert das Verschieben aktiver ausgelagerter Seiten, während das System weiterläuft."}
::option[Ein inaktiver Swap-Bereich muss unter `/swap` eingehängt bleiben.]{#swap-space-mounted-path explanation="Swap-Bereiche sind keine in Verzeichnissen eingehängten Dateisysteme."}
:::

Nutze das Lab [Eine Swap-Datei unter Linux erstellen und aktivieren](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858), um Berechtigungen, Aktivierung und dauerhafte Konfiguration in einer kontrollierten Umgebung zu üben.

## Zusammenfassung

Du kannst Swap nun als ausdrückliche Ressource der Speicherverwaltung behandeln.

1. Ordne Swap hauptsächlich anonymem Speicher unter Druck zu.
2. Untersuche aktiven Swap und das Verhalten der Arbeitslast vor Kapazitätsänderungen.
3. Initialisiere nur ein geprüftes entbehrliches Ziel und aktiviere es anschließend mit `swapon`.
4. Dimensioniere und schütze Swap passend zu Arbeitslast und Anforderungen des Ruhezustands.
5. Stelle vor `swapoff` genügend Kapazität zum Verschieben der Seiten sicher.
