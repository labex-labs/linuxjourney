---
index: 5
lang: "de"
title: "Systemd-Übersicht"
meta_title: "Systemd-Übersicht - Init"
meta_description: "Lernen Sie die Grundlagen des systemd Init-Systems kennen. Dieser Leitfaden behandelt, wie systemd (oder system d) Units und Targets verwendet, um den Linux-Bootvorgang und Systemdienste zu verwalten. Verstehen Sie die Kernkonzepte des modernen Standards für die Linux-Initialisierung."
meta_keywords: "systemd, system d, init system, systemd units, systemd targets, linux bootprozess, linux dienste, systemverwaltung, anfänger, tutorial"
---

## Lesson Content

### Was ist Systemd?

Systemd ist das Standard-Init-System und der Dienstmanager für die meisten modernen Linux-Distributionen. Es ist dafür verantwortlich, das System nach dem Laden des Kernels in der richtigen Reihenfolge zu initialisieren. Eine einfache Möglichkeit zu prüfen, ob Ihr System es verwendet, besteht darin, zu sehen, ob das Verzeichnis `/usr/lib/systemd` existiert. Wenn ja, verwenden Sie wahrscheinlich ein von **systemd** verwaltetes System.

### Der Systemd-Bootprozess

Anstelle starrer sequenzieller Skripte verwendet **systemd** das Konzept der "Ziele" (Goals), um Ihr System in einen funktionsfähigen Zustand zu versetzen. Es identifiziert ein primäres Ziel oder einen `target` und arbeitet daran, dessen Abhängigkeiten zu erfüllen. Dieser Ansatz ermöglicht mehr Flexibilität und Parallelisierung beim Start. Ein typischer Bootprozess, der von **systemd** verwaltet wird, folgt diesen Schritten:

1. **systemd** lädt zuerst seine Konfigurationsdateien aus Verzeichnissen wie `/etc/systemd/system` und `/usr/lib/systemd/system`.
2. Es identifiziert dann das Standard-Bootziel, was typischerweise ein symbolischer Link namens `default.target` ist.
3. Schließlich löst **systemd** alle Abhängigkeiten für dieses Ziel auf und aktiviert die notwendigen Units, um den gewünschten Systemzustand zu erreichen.

### Systemd Targets verstehen

Targets in **systemd** sind analog zu den Runlevels im älteren SysV-Init-System. Sie repräsentieren verschiedene Zustände, in denen sich das System befinden kann. Häufige Targets sind:

- `poweroff.target`: Fährt das System herunter.
- `rescue.target`: Bootet in eine Einzelbenutzer-Shell zur Wartung.
- `multi-user.target`: Eine Standard-Multi-User-Umgebung mit Netzwerk, aber ohne grafische Oberfläche.
- `graphical.target`: Eine vollständige Multi-User-Umgebung mit Netzwerk und grafischer Benutzeroberfläche (GUI).
- `reboot.target`: Startet das System neu.

The `default.target` ist ein symbolischer Link, der auf das Ziel zeigt, in das das System standardmäßig bootet, oft `graphical.target` auf Desktop-Systemen.

### Kernkonzept: Systemd Units

Die grundlegenden Objekte, die **systemd** verwaltet, werden als "Units" bezeichnet. Eine Unit ist eine Konfigurationsdatei, die eine Ressource oder einen Dienst beschreibt. Die Stärke der **system d**-Architektur liegt in ihrer Fähigkeit, verschiedene Arten von Ressourcen zu verwalten, nicht nur Dienste. Jeder Unit-Typ wird durch seine Dateiendung identifiziert. Die häufigsten Typen sind:

- **Service Units (`.service`):** Diese verwalten System-Daemons oder Dienste, wie einen Webserver oder eine Datenbank.
- **Mount Units (`.mount`):** Diese steuern Dateisystem-Mountpoints.
- **Target Units (`.target`):** Diese werden verwendet, um andere Units zu gruppieren und Synchronisationspunkte während des Bootvorgangs zu erstellen.

Wenn das System beispielsweise in `graphical.target` bootet, stellt diese Target-Unit sicher, dass alle ihre Abhängigkeiten, wie `multi-user.target` und verschiedene Service-Units wie `network.service`, zuerst gestartet werden.

## Exercise

Obwohl es für dieses Thema keine spezifischen Übungen gibt, empfehlen wir Ihnen, den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux) zu erkunden, um verwandte Linux-Fähigkeiten und -Konzepte zu üben.

## Quiz Question

Welche Unit wird verwendet, um andere Units zusammenzufassen? Bitte antworten Sie in einem einzigen kleingeschriebenen englischen Wort.

## Quiz Answer

target
