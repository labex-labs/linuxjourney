---
index: 3
lang: "de"
title: "Upstart-Übersicht"
meta_title: "Upstart-Übersicht - Init"
meta_description: "Erfahren Sie mehr über Upstart, sein ereignisgesteuertes Modell und wie es Dienste unter Linux verwaltet. Verstehen Sie die Upstart-Jobkonfigurationen und seine Rolle als Init-System."
meta_keywords: "Upstart, Init-System, Linux-Dienste, Ubuntu, SysV, Anfänger-Tutorial, Linux-Anleitung"
---

## Lesson Content

Upstart wurde von Canonical entwickelt und war daher eine Zeit lang die Init-Implementierung unter Ubuntu; bei modernen Ubuntu-Installationen wird jedoch mittlerweile systemd verwendet. Upstart wurde entwickelt, um die Probleme von SysV zu verbessern, wie z. B. starre Startprozesse, Blockierung von Aufgaben usw. Das ereignis- und jobgesteuerte Modell von Upstart ermöglicht es ihm, auf Ereignisse zu reagieren, sobald sie auftreten.

Um herauszufinden, ob Sie Upstart verwenden, ist das Vorhandensein eines Verzeichnisses `/usr/share/upstart` ein ziemlich guter Indikator.

Jobs sind die Aktionen, die Upstart ausführt, und Ereignisse sind Nachrichten, die von anderen Prozessen empfangen werden, um Jobs auszulösen. Um eine Liste der Jobs und ihrer Konfiguration anzuzeigen:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

Innerhalb dieser Jobkonfigurationen finden Sie Informationen darüber, wie und wann Jobs gestartet werden sollen.

Zum Beispiel könnte in der Datei `networking.conf` etwas so Einfaches stehen wie:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

Dies bedeutet, dass die Netzwerkkonfiguration auf den Runlevels 2, 3 oder 5 gestartet wird und auf Runlevel 0 gestoppt wird. Es gibt viele Möglichkeiten, die Konfigurationsdatei zu schreiben, und Sie werden dies entdecken, wenn Sie sich die verschiedenen verfügbaren Jobkonfigurationen ansehen.

Die Funktionsweise von Upstart ist wie folgt:

1. Zuerst lädt es die Jobkonfigurationen aus `/etc/init`.
2. Sobald ein Startereignis auftritt, führt es die durch dieses Ereignis ausgelösten Jobs aus.
3. Diese Jobs erzeugen neue Ereignisse, und diese Ereignisse lösen dann weitere Jobs aus.
4. Upstart fährt damit fort, bis alle notwendigen Jobs abgeschlossen sind.

## Exercise

Übung macht den Meister! Obwohl Upstart ein älteres Init-System ist, ist das Verständnis dafür, wie Prozesse verwaltet und Aufgaben geplant werden, für jeden Linux-Administrator von entscheidender Bedeutung. Hier sind einige praktische Übungen, um Ihr Verständnis für Prozessmanagement und Aufgabenautomatisierung zu festigen, die die Grundlage dafür bilden, wie Init-Systeme funktionieren:

1. **[Prozesse unter Linux verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, inspizieren Sie diese mit `ps`, überwachen Sie Ressourcen mit `top` und beenden Sie sie mit `kill`. Dieses Labor hilft Ihnen, den Lebenszyklus von Prozessen zu verstehen, den Init-Systeme wie Upstart verwalten.
2. **[Aufgaben mit at und cron unter Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** – Lernen Sie, einmalige Jobs mit `at` und wiederkehrende Aufgaben mit `cron` zu planen. Dies vermittelt praktische Erfahrung mit der Aufgabenautomatisierung, einer Kernfunktion, die Init-Systeme für Systemdienste ermöglichen.

Diese Labs helfen Ihnen, die Konzepte der Prozesssteuerung und Aufgabenautomatisierung in realen Szenarien anzuwenden und Vertrauen in die Verwaltung eines Linux-Systems aufzubauen, unabhängig vom verwendeten spezifischen Init-System.

## Quiz Question

Was ist die Init-Implementierung, die von Ubuntu verwendet wird?

## Quiz Answer

systemd
