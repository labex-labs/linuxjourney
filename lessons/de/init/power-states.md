---
index: 7
lang: "de"
title: "Zustände der Energieverwaltung"
meta_title: "Energiezustände - Init"
meta_description: "Erfahren Sie, wie Sie die Energiezustände von Linux-Systemen verwalten. Dieser Leitfaden behandelt die wesentlichen Befehle zum Herunterfahren, Neustarten und Anhalten, um Ihr Linux-System sicher auszuschalten oder neu zu starten. Meistern Sie diese grundlegenden Linux-Befehle für die Systemadministration."
meta_keywords: "linux energiezustände, shutdown befehl, reboot befehl, halt befehl, poweroff linux, neustart linux, linux systemadministration, linux für anfänger, linux befehle, systemd, init"
---

## Lesson Content

Die ordnungsgemäße Verwaltung des Energiestatus Ihres Linux-Systems ist eine grundlegende Fähigkeit. Obwohl Sie eine grafische Oberfläche verwenden können, bietet die Befehlszeile leistungsstarke und flexible Optionen zum Herunterfahren oder Neustarten Ihres Computers. Diese Prozesse sind an das Initialisierungssystem des Systems gebunden, wie z. B. `init` oder `systemd`, das verschiedene Betriebsmodi, einschließlich Start und Herunterfahren, verwaltet.

### Herunterfahren des Systems

Der primäre Befehl zur Verwaltung von Energiestatus ist `shutdown`. Um Ihr Linux-System sofort auszuschalten, können Sie den Befehl `shutdown` mit dem Flag `-h` (halt) und dem Zeitargument `now` verwenden. Administratorrechte sind erforderlich, daher müssen Sie `sudo` verwenden.

```bash
sudo shutdown -h now
```

Das Flag `-h` weist das System an, nach dem Herunterfahren der Dienste anzuhalten (halt). Auf den meisten modernen Geräten schaltet dies den Computer vollständig aus. Sie können das Herunterfahren auch für einen zukünftigen Zeitpunkt planen. Um das System nach einer bestimmten Anzahl von Minuten auszuschalten, verwenden Sie das Format `+m`:

```bash
sudo shutdown -h +2
```

Dieser Befehl fährt Ihr System in zwei Minuten herunter, was nützlich ist, um anderen Benutzern eine Warnung zu geben oder Hintergrundprozessen eine ordnungsgemäße Beendigung zu ermöglichen.

### Neustarten des Systems

Um Ihr Linux-System neu zu starten, können Sie den Befehl `shutdown` mit dem Flag `-r` (reboot) verwenden.

```bash
sudo shutdown -r now
```

Eine direktere und häufiger verwendete Alternative ist der Befehl `reboot`, der dasselbe Ziel – das sichere Neustarten des Systems – erreicht.

```bash
sudo reboot
```

### Alternative Energiebefehle

Für eine direktere Steuerung stoßen Sie möglicherweise auch auf die Befehle `halt` und `poweroff`. In vielen modernen Linux-Distributionen sind dies im Wesentlichen Verknüpfungen, die den Befehl `shutdown` aufrufen. Zum Beispiel ist die Ausführung von `poweroff` oft gleichbedeutend mit der Ausführung von `shutdown -h now`.

## Exercise

Sie können diese Befehle gerne in einer virtuellen Maschine üben. Für stärker geführte Übungen erkunden Sie den umfassenden [Linux Lernpfad](https://labex.io/de/learn/linux), um eine breite Palette von Linux-Fähigkeiten zu trainieren.

## Quiz Question

What is the full command, including `sudo`, to schedule a system power off in 4 minutes? Please provide the complete command in English, paying attention to spacing and case.

## Quiz Answer

sudo shutdown -h +4
