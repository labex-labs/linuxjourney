---
index: 6
lang: "de"
title: "Systemd Ziele"
meta_title: "Systemd Ziele - Init"
meta_description: "Erkunden Sie Systemd-Ziele und lernen Sie, Linux-Dienste mit essentiellen systemctl-Befehlen zu verwalten. Dieser Leitfaden behandelt die Grundlagen von Systemd-Unit-Dateien, wie man Dienste startet, stoppt und aktiviert und deren Status anzeigt."
meta_keywords: "systemd, systemctl, Linux-Dienste, Unit-Dateien, systemd-Ziele, Dienstverwaltung, systemd-Units, Anfänger, Tutorial, Leitfaden, Linux-Befehle"
---

## Lesson Content

Diese Lektion bietet einen grundlegenden Überblick über systemd Unit-Dateien und wie man sie mit `systemctl` verwaltet, dem primären Werkzeug zur Steuerung des Init-Systems. Wir werden die grundlegende Struktur einer Unit-Datei und die wesentlichen Befehle zur Verwaltung von Linux-Diensten behandeln.

### Verständnis einer Systemd Unit-Datei

A systemd Unit-Datei ist eine einfache Textdatei, die einen Dienst, einen Einhängepunkt, ein Gerät oder eine andere Ressource beschreibt, die systemd verwalten kann. Hier ist ein einfaches Beispiel für eine Service-Unit-Datei namens `foobar.service`:

```
[Unit]
Description=Mein Foobar Dienst
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

Diese einfache Service-Datei ist in Abschnitte unterteilt:

- **[Unit]**: Dieser Abschnitt enthält Metadaten und Abhängigkeitsinformationen. Die `Description` liefert einen für Menschen lesbaren Namen für die Unit. Direktiven wie `After` und `Before` steuern die Startreihenfolge und stellen sicher, dass diese Unit startet, nachdem das Netzwerk verfügbar ist.
- **[Service]**: Dieser Abschnitt definiert, wie der Dienst verwaltet wird. Die Direktive `ExecStart` ist entscheidend, da sie den Befehl angibt, der zur Ausführung des Dienstes ausgeführt wird. Andere Direktiven wie `ExecStop` und `ExecReload` können definieren, wie der Dienst gestoppt oder neu geladen wird.
- **[Install]**: Dieser Abschnitt definiert das Verhalten der Unit, wenn sie mit `systemctl` aktiviert oder deaktiviert wird. Die Direktive `WantedBy` weist systemd an, diesen Dienst als Teil eines bestimmten Ziels zu starten, wie z.B. dem `multi-user.target` für einen Standard-Nicht-Grafik-Boot.

Dies ist nur ein kleiner Einblick in systemd Unit-Dateien. Für fortgeschrittenere Konfigurationen wird dringend empfohlen, sich weiter mit dem Thema zu befassen.

### Wesentliche Systemctl-Befehle

Nun erkunden wir die wesentlichen `systemctl`-Befehle, die Sie verwenden werden, um mit systemd Units zu interagieren und Linux-Dienste zu verwalten.

### Auflisten von Systemd Units

Um alle aktiven Units anzuzeigen, die systemd gerade verwaltet, verwenden Sie den Befehl `list-units`.

```bash
systemctl list-units
```

### Überprüfen des Status einer Unit

Um den detaillierten Status einer bestimmten Unit anzuzeigen, einschließlich ob sie aktiv und aktiviert ist, sowie deren letzte Protokolleinträge, verwenden Sie den Befehl `status`.

```bash
systemctl status networking.service
```

### Verwalten von Dienstzuständen

Sie können den Laufzeitzustand eines Dienstes mit `start`, `stop` und `restart` steuern.

Um einen Dienst sofort zu starten:

```bash
sudo systemctl start networking.service
```

Um einen laufenden Dienst zu stoppen:

```bash
sudo systemctl stop networking.service
```

Um den Dienst zu stoppen und dann erneut zu starten:

```bash
sudo systemctl restart networking.service
```

### Dienste aktivieren und deaktivieren

Das Aktivieren eines Dienstes erstellt einen symbolischen Link, der ihn mit dem Boot-Prozess verbindet und sicherstellt, dass er automatisch startet. Das Deaktivieren entfernt diesen Link.

Um einen Dienst so zu aktivieren, dass er beim Booten startet:

```bash
sudo systemctl enable networking.service
```

Um einen Dienst vom automatischen Start beim Booten zu deaktivieren:

```bash
sudo systemctl disable networking.service
```

Diese Befehle sind die Bausteine für die Dienstverwaltung auf modernen Linux-Systemen. Ihre Beherrschung ist ein wichtiger Schritt auf Ihrem Linux-Weg.

## Exercise

Übung ist der Schlüssel zum Erlernen neuer Fähigkeiten. Dieses praktische Labor hilft Ihnen, Ihr Verständnis für die Verwaltung von Prozessen zu festigen, die oft von systemd-Diensten gesteuert werden:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, inspizieren Sie diese mit `ps`, überwachen Sie Ressourcen mit `top`, passen Sie die Priorität mit `renice` an und beenden Sie sie mit `kill`. Dieses Labor vermittelt Ihnen praktische Erfahrung mit den Laufzeitauswirkungen der systemd Unit-Verwaltung.

Dieses Labor hilft Ihnen, diese Konzepte in einem realen Szenario anzuwenden und Selbstvertrauen in die Prozessverwaltung unter Linux aufzubauen.

## Quiz Question

What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

## Quiz Answer

sudo systemctl start peanut.service
