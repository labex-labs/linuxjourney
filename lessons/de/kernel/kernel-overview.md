---
lesson_id: "kernel-overview"
course_id: "kernel"
lang: "de"
order_index: 1
title: "Überblick über den Kernel"
description: "Erfahre, wie der Linux-Kernel Hardware, Ressourcen, Isolation und Anfragen aus dem User-Space vermittelt."
meta_title: "Überblick über den Kernel – Kernel"
meta_description: "Beginne deine Linux-Reise mit einem Überblick über den Linux-Kernel. Verstehe seine zentrale Rolle bei der Verwaltung von Hardware und User-Space – ein grundlegendes Konzept auf linuxjourney.com."
meta_keywords: "Linux-Kernel, Betriebssystem, Hardware, User-Space, Linux-Reise, linuxjourney.com, Kernel-Überblick"
---

Linux ist der Betriebssystemkernel: die privilegierte Software, die Prozessoren, Speicher, Geräte, Prozesse und allgemeine Ressourcenabstraktionen verwaltet. Ein vollständiges Linux-System umfasst außerdem Bibliotheken, Werkzeuge, Dienste, Shells und grafische Software im User-Space sowie die Richtlinien einer Distribution.

## Hardwareressourcen

Prozessoren führen Anweisungen aus, Speicher hält aktive Zustände und Controller verbinden Massenspeicher, Netzwerke, Bildschirme, Eingabegeräte und andere Peripherie. Hardware stellt architektur- und gerätespezifische Mechanismen bereit und keine einzelne sichere Schnittstelle für jede Anwendung.

Der Kernel initialisiert und steuert diese Ressourcen durch Architekturcode und Gerätetreiber. Er behandelt Interrupts, DMA-Koordination, Zeitgeber und Energieverwaltungsereignisse und setzt dabei Zugriffsgrenzen zwischen Arbeitslasten durch.

:::single-choice{#kernel-overview-hardware-manager}
Welche Schicht koordiniert unter Linux gewöhnlich Gerätetreiber und Hardware-Interrupts?

::option[Die Shell-Verlaufsdatei jedes Benutzers.]{#kernel-overview-shell-history explanation="Ein Verlauf erfasst Befehle und verarbeitet keine Hardwareausführung."}
::option[Der Index einer Paketquelle.]{#kernel-overview-repository-index explanation="Paketquellenmetadaten beschreiben Softwarepakete und keine aktiven Hardwareereignisse."}
::option[Der Kernel.]{#kernel-overview-kernel-layer .correct explanation="Privilegierter Kernelcode verbindet Hardwareereignisse und Treibervorgänge mit kontrollierten Systemschnittstellen."}
:::

## Zuständigkeiten des Kernels

Zu den wichtigsten Zuständigkeiten gehören:

- ausführungsbereite Threads auf CPUs einzuplanen
- virtuelle Adressräume zu erstellen und zu isolieren
- Prozesszugangsdaten, Berechtigungen und Sicherheitsrichtlinien durchzusetzen
- Dateisystem-, Netzwerk-, IPC- und Geräteschnittstellen bereitzustellen
- Signale, Zeitgeber und den Prozesslebenszyklus zu behandeln
- Ressourcen zuzuweisen, abzurechnen und zurückzugewinnen

Linux wird gewöhnlich als monolithischer Kernel bezeichnet, weil zentrale Dienste und viele Treiber in einem einzigen privilegierten Kerneladressraum laufen. Zugleich ist er modular: Unterstützte Komponenten können als Kernelmodule geladen und entladen werden. Ein Fehler in privilegiertem Kernelcode kann das gesamte System gefährden, wodurch Kernelaktualisierungen und die Herkunft von Modulen sicherheitskritisch sind.

:::single-choice{#kernel-overview-scheduler-role}
Was verwaltet der Kernel-Scheduler?

::option[Welche Dokumentationsseite ein Benutzer als Nächstes liest.]{#kernel-overview-documentation explanation="Die Lernnavigation gehört nicht zum Kernel-Scheduling."}
::option[Welche ausführungsbereiten Threads CPU-Ausführungszeit erhalten.]{#kernel-overview-thread-scheduling .correct explanation="Der Scheduler wählt Ausführungskontexte anhand von Richtlinie, Priorität, Affinität und CPU-Verfügbarkeit aus."}
::option[Welchem Signaturschlüssel einer Paketquelle ein Administrator vertrauen sollte.]{#kernel-overview-repository-key explanation="Die Vertrauenskonfiguration gehört zur Paketverwaltungsrichtlinie."}
:::

## User-Space

Der User-Space enthält gewöhnliche Prozesse: init und Dienste, Befehlszeilenwerkzeuge, Sprachlaufzeiten, Datenbanken, Shells und Desktop-Anwendungen. Hardwareprivilegien verhindern, dass diese Programme viele vertrauliche Anweisungen unmittelbar ausführen oder auf beliebigen Kernelspeicher zugreifen.

Prozesse fordern Kernelarbeit über Systemaufrufe an und interagieren mit bereitgestellten Schnittstellen wie Dateideskriptoren, Sockets, Geräteknoten, procfs, sysfs, Netlink und Speicherabbildungen. Bibliotheken kapseln diese Schnittstellen häufig in übergeordneten APIs.

root im User-Space besitzt aufgrund von Richtlinien weitreichende Berechtigungen, führt seine Anweisungen aber gewöhnlich weiterhin im Benutzermodus des Prozessors aus. Benutzeridentität und CPU-Privilegienmodus sind getrennte Konzepte.

:::single-choice{#kernel-overview-root-user-mode}
Führt eine gewöhnliche Anwendung im Besitz von root alle ihre Anweisungen im Kernelmodus aus?

::option[Ja; UID 0 wandelt jede Anweisung dauerhaft in Ring 0 um.]{#kernel-overview-root-ring-zero explanation="Ein gewöhnlicher root-Prozess bleibt ein User-Space-Prozess."}
::option[Ja; root-Anwendungen werden automatisch zu ladbaren Kernelmodulen.]{#kernel-overview-root-module explanation="Eine ausführbare Benutzerdatei wird durch die UID ihres Eigentümers nicht in Kernelcode umgewandelt."}
::option[Nein; sie läuft gewöhnlich im Benutzermodus und tritt über kontrollierte Schnittstellen in den Kernel ein.]{#kernel-overview-root-userspace .correct explanation="root-Zugangsdaten beeinflussen die Autorisierung, während sich der Prozessormodus nur für den Kerneleintritt und die Kernelausführung ändert."}
:::

## Grenzen und Abstraktionen

Der Kernel stellt virtuelle Prozesse, Dateien, Sockets und Adressräume bereit, statt die rohe physische Maschine unmittelbar offenzulegen. Diese Abstraktionen unterstützen Isolation und Portabilität, sind für sich allein aber keine perfekten Sicherheitsgrenzen. Namensräume, cgroups, Capabilities, Sicherheitsmodule, seccomp und Virtualisierung ergänzen spezialisierte Kontrollen.

Frage bei der Fehlersuche, welcher Schicht das Verhalten gehört: Anwendung, Bibliothek, Systemaufrufschnittstelle, Dateisystem, Treiber, Kernel-Subsystem, Firmware oder Hardware. Belege aus der falschen Schicht können zu falschen Lösungen führen.

:::single-choice{#kernel-overview-system-call-boundary}
Was ist ein Systemaufruf?

::option[Eine kontrollierte Anfrage aus dem User-Space an einen Kerneldienst.]{#kernel-overview-controlled-request .correct explanation="Der Prozessor tritt an einer festgelegten Schnittstelle in den Kernelmodus ein, wo der Kernel den Vorgang validiert und ausführt."}
::option[Ein direkter Befehl, der jede Zugriffskontrolle umgeht.]{#kernel-overview-bypass-checks explanation="Gerade bei Systemaufrufen finden viele Validierungs- und Autorisierungsprüfungen statt."}
::option[Ein Paketarchiv, das einen Gerätetreiber enthält.]{#kernel-overview-package-archive explanation="Pakete können Software ausliefern, doch ein Systemaufruf ist eine Ausführungsschnittstelle zur Laufzeit."}
:::

Nutze [Kernelmodule unter Linux verwalten](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865), um einen modularen Teil des Kernels in einer kontrollierten Umgebung zu beobachten.

## Zusammenfassung

Du kannst den Kernel nun zwischen physischen Ressourcen und isolierten User-Space-Prozessen einordnen.

1. Setze Treiber und Architekturcode mit der Hardwaresteuerung in Beziehung.
2. Bestimme Zuständigkeiten für Scheduling, Speicher, Sicherheit, Dateisystem und Netzwerk.
3. Behandle root-Zugangsdaten und den Kernelmodus des Prozessors als getrennte Konzepte.
4. Verorte die Interaktion zwischen Benutzer und Kernel an kontrollierten Laufzeitschnittstellen.
