---
index: 6
lang: "de"
title: "lsusb, lspci, lsscsi"
meta_title: "lsusb, lspci, lsscsi - Geräte"
meta_description: "Erfahren Sie, wie Sie USB-, PCI- und SCSI-Hardware auf Ihrem Linux-System auflisten und überprüfen. Diese Anleitung behandelt die Befehle lsusb, lspci und lsscsi, einschließlich Optionen wie lsusb -t zur Anzeige von Gerätebäumen."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, usb geräte auflisten, pci geräte auflisten, scsi geräte auflisten, linux hardware, geräteinformationen"
---

## Lesson Content

So wie Sie den Befehl `ls` verwenden, um Dateien aufzulisten, bietet Linux ähnliche Werkzeuge zum Auflisten von Hardware-Geräten. Diese Befehle sind unerlässlich, um die an Ihrem System angeschlossene Hardware zu identifizieren.

### Auflisten von USB-Geräten mit lsusb

Um alle an Ihr System angeschlossenen USB-Geräte anzuzeigen, können Sie den Befehl `lsusb` verwenden. Dieser Befehl scannt die USB-Hubs und meldet Informationen über die gefundenen Geräte, wie Webcams, Tastaturen und externe Laufwerke.

```bash
lsusb
```

Für eine strukturiertere Ansicht können Sie den Befehl `lsusb -t` verwenden. Diese Option zeigt die USB-Geräte in einer Baumstruktur an, was hilfreich ist, um zu verstehen, wie Geräte physisch mit den USB-Controllern und Hubs verbunden sind.

### Auflisten von PCI-Geräten mit lspci

Der Befehl `lspci` wird verwendet, um alle PCI-Geräte (Peripheral Component Interconnect) aufzulisten. Dies sind typischerweise interne Komponenten, die mit dem Motherboard verbunden sind, wie z. B. Grafikkarten, Netzwerkadapter und Soundkarten. Dieser Befehl bietet einen schnellen Überblick über die Kernhardware Ihres Systems.

```bash
lspci
```

### Auflisten von SCSI- und SATA-Geräten mit lsscsi

Für Speichergeräte ist der Befehl `lsscsi` besonders nützlich. Er listet alle angeschlossenen SCSI- und SATA-Geräte auf, wozu üblicherweise Festplatten, SSDs und optische Laufwerke (CD/DVD/Blu-ray) gehören. Während andere Befehle möglicherweise den Speichercontroller anzeigen, liefert `lsscsi` direkte Informationen über die Speichergeräte selbst, was ihn zu einem wertvollen Werkzeug für Systemadministratoren und Benutzer macht, die Speicher verwalten.

```bash
lsscsi
```

## Exercise

Um Ihr Verständnis der Erkundung von Hardware-Geräten unter Linux zu festigen, versuchen Sie das folgende praktische Labor:

1. **[Hardware-Geräte unter Linux erkunden](https://labex.io/de/labs/comptia-explore-hardware-devices-in-linux-590861)** – In diesem Labor erlernen Sie die wesentlichen Fähigkeiten, um Hardware-Geräte in einer Linux-Umgebung zu erkunden, zu identifizieren und zu inspizieren. Sie erhalten praktische Erfahrung mit leistungsstarken Befehlszeilenprogrammen, um zu verstehen, wie das Betriebssystem mit physischen Komponenten interagiert.

Dieses Labor hilft Ihnen, diese Konzepte in einem realen Szenario anzuwenden und Vertrauen in die Verwaltung von Geräteinformationen aufzubauen.

## Quiz Question

Welcher Befehl wird verwendet, um eine Liste der angeschlossenen USB-Geräte anzuzeigen? (Bitte antworten Sie nur in Kleinbuchstaben auf Englisch)

## Quiz Answer

lsusb
