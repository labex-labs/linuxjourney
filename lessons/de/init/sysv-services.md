---
index: 2
lang: "de"
title: "System V Dienst"
meta_title: "System V Dienst - Init"
meta_description: "Lernen Sie, System V-Dienste mit Befehlszeilentools zu verwalten. Entdecken Sie, wie Sie Dienste auflisten, starten, stoppen und neu starten können, mit diesem anfängerfreundlichen Linux-Tutorial."
meta_keywords: "System V-Dienste, Linux-Dienste, service-Befehl, SysV init, Linux-Tutorial, Linux für Anfänger, Dienstverwaltung, Linux-Anleitung"
---

## Lesson Content

Es gibt viele Befehlszeilentools, die Sie zur Verwaltung von Sys V-Diensten verwenden können.

### Dienste auflisten

```bash
service --status-all
```

### Einen Dienst starten

```bash
sudo service networking start
```

### Einen Dienst stoppen

```bash
sudo service networking stop
```

### Einen Dienst neu starten

```bash
sudo service networking restart
```

Diese Befehle sind nicht spezifisch für Sys V Init-Systeme; Sie können sie auch zur Verwaltung von Upstart-Diensten verwenden. Da Linux versucht, von den traditionelleren Sys V Init-Skripten wegzukommen, gibt es immer noch Mechanismen, die diesen Übergang unterstützen.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Prozess- und Aufgabenmanagements zu vertiefen, die für die Verwaltung von Diensten unter Linux von grundlegender Bedeutung sind:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit, die Überprüfung, Überwachung und Beendigung von Prozessen in einer echten Linux-Umgebung.
2. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** – Lernen Sie, Aufgaben mit `at` für einmalige Jobs und `cron` für wiederkehrende Aufgaben zu automatisieren, eine Schlüsselkompetenz für die Dienstautomatisierung.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Systemoperationen aufzubauen.

## Quiz Question

Wie lautet der Befehl, um einen Dienst namens `peanut` mit Sys V zu stoppen?

## Quiz Answer

sudo service peanut stop
