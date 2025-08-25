---
index: 6
lang: "de"
title: "Systemd-Ziele"
meta_title: "Systemd-Ziele - Init"
meta_description: "Lernen Sie die Grundlagen von systemd-Units und wichtige systemctl-Befehle. Verstehen Sie, wie Sie Dienste verwalten, Status anzeigen und Units in Linux aktivieren. Beginnen Sie Ihre Reise!"
meta_keywords: "systemd, systemctl, Linux-Dienste, Unit-Dateien, Anfänger, Tutorial, Anleitung, Linux-Befehle"
---

## Lesson Content

Wir werden nicht auf die Details des Schreibens von systemd-Unit-Dateien eingehen. Wir werden jedoch einen kurzen Überblick über eine Unit-Datei geben und wie man Units manuell steuert.

Hier ist eine grundlegende Dienst-Unit-Datei: foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Dies ist ein einfaches Dienst-Target. Am Anfang der Datei sehen wir einen Abschnitt für `[Unit]`. Dies ermöglicht es uns, unserer Unit-Datei eine Beschreibung zu geben und die Reihenfolge der Aktivierung der Unit zu steuern. Der nächste Teil ist der Abschnitt `[Service]`; hier können wir einen Dienst starten, stoppen oder neu laden. Und der Abschnitt `[Install]` wird für Abhängigkeiten verwendet. Dies ist nur die Spitze des Eisbergs beim Schreiben von systemd-Dateien, daher bitte ich Sie dringend, sich mit dem Thema zu befassen, wenn Sie mehr wissen möchten.

Nun, kommen wir zu einigen Befehlen, die Sie mit systemd-Units verwenden können:

### Units auflisten

```bash
systemctl list-units
```

### Status einer Unit anzeigen

```bash
systemctl status networking.service
```

### Einen Dienst starten

```bash
sudo systemctl start networking.service
```

### Einen Dienst stoppen

```bash
sudo systemctl stop networking.service
```

### Einen Dienst neu starten

```bash
sudo systemctl restart networking.service
```

### Eine Unit aktivieren

```bash
sudo systemctl enable networking.service
```

### Eine Unit deaktivieren

```bash
sudo systemctl disable networking.service
```

Auch hier haben Sie noch nicht gesehen, wie tief systemd geht, also lesen Sie sich ein, wenn Sie mehr erfahren möchten.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Prozessverwaltung zu vertiefen, die oft von systemd-Diensten gesteuert wird:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, deren Überprüfung mit `ps`, die Überwachung von Ressourcen mit `top`, die Anpassung der Priorität mit `renice` und deren Beendigung mit `kill`. Dieses Labor vermittelt Ihnen praktische Erfahrungen mit den Laufzeiteffekten der systemd-Unit-Verwaltung.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Prozessverwaltung unter Linux aufzubauen.

## Quiz Question

Wie lautet der Befehl zum Starten eines Dienstes namens peanut.service?

## Quiz Answer

sudo systemctl start peanut.service
