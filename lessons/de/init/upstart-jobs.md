---
index: 4
lang: "de"
title: "Upstart-Jobs"
meta_title: "Upstart-Jobs - Init"
meta_description: "Lernen Sie, Upstart-Jobs in Linux mit initctl-Befehlen zu verwalten. Verstehen Sie den Job-Status, starten, stoppen und starten Sie Dienste neu. Verbessern Sie Ihre Linux-Systemadministrationsfähigkeiten."
meta_keywords: "Upstart-Jobs, initctl, Linux-Dienste, Systemadministration, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Upstart kann viele Ereignisse und Jobs auslösen. Leider gibt es keine einfache Möglichkeit zu sehen, woher ein Ereignis oder Job stammt, daher müssen Sie die Job-Konfigurationen in `/etc/init` durchsuchen. Meistens werden Sie die Upstart-Job-Konfigurationsdateien nie ansehen müssen, aber Sie werden einige spezifische Jobs einfacher steuern wollen. Es gibt viele nützliche Befehle, die Sie in einem Upstart-System verwenden können.

### Jobs anzeigen

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Sie sehen eine Liste von Upstart-Jobs mit verschiedenen Status. In jeder Zeile ist der Job-Name der erste Wert, und das zweite Feld (vor dem `/`) ist tatsächlich das Ziel des Jobs. Der dritte Wert (nach dem `/`) ist der aktuelle Status. Wir sehen also, dass unser `shutdown`-Job irgendwann stoppen möchte, sich aber derzeit in einem Wartezustand befindet. Der Job-Status und die Ziele ändern sich, wenn Sie Jobs starten oder stoppen.

### Spezifischen Job anzeigen

```plaintext
initctl status networking
networking start/running
```

Wir werden nicht auf die Details eingehen, wie man eine Upstart-Job-Konfiguration schreibt; wir wissen jedoch bereits, dass Jobs in diesen Konfigurationen gestoppt, gestartet und neu gestartet werden. Diese Jobs senden auch Ereignisse aus, sodass sie andere Jobs starten können. Wir werden die manuellen Befehle des Upstart-Betriebs durchgehen, aber wenn Sie neugierig sind, sollten Sie die `.conf`-Dateien genauer untersuchen.

### Job manuell starten

```bash
sudo initctl start networking
```

### Job manuell stoppen

```bash
sudo initctl stop networking
```

### Job manuell neu starten

```bash
sudo initctl restart networking
```

### Ereignis manuell auslösen

```bash
sudo initctl emit some_event
```

## Exercise

Übung macht den Meister! Obwohl es keine spezifischen Labs für Upstart gibt, ist das Verständnis, wie man Aufgaben plant und verwaltet, entscheidend für die Steuerung von Systemprozessen. Hier ist ein praktisches Lab, um Ihr Verständnis des Task-Managements zu vertiefen:

1. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** – Üben Sie das Erstellen, Verwalten und Entfernen von einmaligen und wiederkehrenden Jobs, die grundlegende Konzepte im Zusammenhang mit der Verwaltung von Diensten und Aufgaben in Linux-Umgebungen sind, wie sie von Upstart gehandhabt werden.

Dieses Lab wird Ihnen helfen, die Konzepte der Aufgabenautomatisierung in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Systemoperationen aufzubauen.

## Quiz Question

Wie würde ich einen Upstart-Job namens `peanuts` manuell neu starten?

## Quiz Answer

sudo initctl restart peanuts
