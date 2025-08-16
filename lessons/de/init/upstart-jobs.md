---
title: "Upstart-Jobs"
description: "Lernen Sie, Upstart-Jobs in Linux mit initctl-Befehlen zu verwalten. Verstehen Sie den Job-Status, starten, stoppen und neu starten Sie Dienste. Verbessern Sie Ihre Linux-Systemadministrationsfähigkeiten."
keywords: "Upstart-Jobs, initctl, Linux-Dienste, Systemadministration, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Upstart kann viele Ereignisse und Jobs auslösen. Leider gibt es keine einfache Möglichkeit zu sehen, woher ein Ereignis oder Job stammt, daher müssen Sie die Job-Konfigurationen in `/etc/init` durchsuchen. Meistens müssen Sie die Upstart-Job-Konfigurationsdateien nie ansehen, aber Sie möchten bestimmte Jobs einfacher steuern können. Es gibt viele nützliche Befehle, die Sie in einem Upstart-System verwenden können.

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Sie sehen eine Liste von Upstart-Jobs mit verschiedenen Status. In jeder Zeile ist der Job-Name der erste Wert, und das zweite Feld (vor dem `/`) ist tatsächlich das Ziel des Jobs. Der dritte Wert (nach dem `/`) ist der aktuelle Status. Wir sehen also, dass unser `shutdown`-Job irgendwann stoppen möchte, sich aber derzeit in einem Wartezustand befindet. Der Job-Status und die Ziele ändern sich, wenn Sie Jobs starten oder stoppen.

### View specific job

```plaintext
initctl status networking
networking start/running
```

Wir werden nicht auf die Details eingehen, wie man eine Upstart-Job-Konfiguration schreibt; wir wissen jedoch bereits, dass Jobs in diesen Konfigurationen gestoppt, gestartet und neu gestartet werden. Diese Jobs senden auch Ereignisse aus, sodass sie andere Jobs starten können. Wir werden die manuellen Befehle des Upstart-Betriebs durchgehen, aber wenn Sie neugierig sind, sollten Sie die `.conf`-Dateien genauer untersuchen.

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

Beobachten Sie Ihre Liste der Upstart-Jobs. Ändern Sie nun den Job-Status mit einem der Befehle, die wir heute gelernt haben. Was bemerken Sie danach?

## Quiz Question

Wie würde ich einen Upstart-Job namens `peanuts` manuell neu starten?

## Quiz Answer

sudo initctl restart peanuts
