---
lang: "de"
title: "Systemd-Ziele"
description: "Lernen Sie die Grundlagen von systemd-Units und wichtige systemctl-Befehle. Verstehen Sie, wie Sie Dienste verwalten, Status anzeigen und Units in Linux aktivieren. Beginnen Sie Ihre Reise!"
keywords: "systemd, systemctl, Linux-Dienste, Unit-Dateien, Anfänger, Tutorial, Anleitung, Linux-Befehle"
---

## Lesson Content

Wir werden nicht auf die Details des Schreibens von systemd-Unit-Dateien eingehen. Wir werden jedoch einen kurzen Überblick über eine Unit-Datei geben und wie man Units manuell steuert.

Hier ist eine grundlegende Service-Unit-Datei: foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Dies ist ein einfaches Service-Target. Am Anfang der Datei sehen wir einen Abschnitt für `[Unit]`. Dies ermöglicht es uns, unserer Unit-Datei eine Beschreibung zu geben und die Reihenfolge der Aktivierung der Unit zu steuern. Der nächste Teil ist der Abschnitt `[Service]`; hier können wir einen Dienst starten, stoppen oder neu laden. Und der Abschnitt `[Install]` wird für Abhängigkeiten verwendet. Dies ist nur die Spitze des Eisbergs beim Schreiben von systemd-Dateien, daher empfehle ich Ihnen dringend, sich mit dem Thema zu befassen, wenn Sie mehr wissen möchten.

Nun, lassen Sie uns einige Befehle betrachten, die Sie mit systemd-Units verwenden können:

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

Auch hier haben Sie noch nicht gesehen, wie tief systemd geht, also lesen Sie sich ein, wenn Sie mehr erfahren möchten.

## Exercise

Zeigen Sie die Unit-Status an und starten und stoppen Sie einige Dienste. Was beobachten Sie?

## Quiz Question

Wie lautet der Befehl, um einen Dienst namens peanut.service zu starten?

## Quiz Answer

sudo systemctl start peanut.service
