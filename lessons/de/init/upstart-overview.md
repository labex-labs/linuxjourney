---
index: 3
lang: "de"
title: "Upstart Übersicht"
meta_title: "Upstart Übersicht - Init"
meta_description: "Erfahren Sie mehr über Upstart, sein ereignisgesteuertes Modell und wie es Dienste in Linux verwaltet. Verstehen Sie Upstart-Job-Konfigurationen und seine Rolle als Init-System."
meta_keywords: "Upstart, Init-System, Linux-Dienste, Ubuntu, SysV, Anfänger-Tutorial, Linux-Anleitung"
---

## Lesson Content

Upstart wurde von Canonical entwickelt und war daher eine Zeit lang die Init-Implementierung unter Ubuntu; auf modernen Ubuntu-Installationen wird jedoch inzwischen systemd verwendet. Upstart wurde entwickelt, um die Probleme von SysV zu verbessern, wie z. B. strikte Startprozesse, Blockierung von Aufgaben usw. Das ereignis- und auftragsgesteuerte Modell von Upstart ermöglicht es, auf Ereignisse zu reagieren, sobald sie eintreten.

Um herauszufinden, ob Sie Upstart verwenden, ist das Vorhandensein eines Verzeichnisses `/usr/share/upstart` ein ziemlich guter Indikator.

Jobs sind die Aktionen, die Upstart ausführt, und Events sind Nachrichten, die von anderen Prozessen empfangen werden, um Jobs auszulösen. Um eine Liste der Jobs und ihrer Konfiguration anzuzeigen:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

Innerhalb dieser Job-Konfigurationen finden Sie Informationen darüber, wie und wann Jobs gestartet werden sollen.

Zum Beispiel könnte in der Datei `networking.conf` etwas so Einfaches stehen wie:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

Das bedeutet, dass die Netzwerkkonfiguration auf den Runlevels 2, 3 oder 5 gestartet und auf Runlevel 0 beendet wird. Es gibt viele Möglichkeiten, die Konfigurationsdatei zu schreiben, und das werden Sie feststellen, wenn Sie sich die verschiedenen verfügbaren Job-Konfigurationen ansehen.

Die Funktionsweise von Upstart ist wie folgt:

1. Zuerst lädt es die Job-Konfigurationen aus `/etc/init`.
2. Sobald ein Start-Ereignis auftritt, werden die durch dieses Ereignis ausgelösten Jobs ausgeführt.
3. Diese Jobs erzeugen neue Ereignisse, und diese Ereignisse lösen dann weitere Jobs aus.
4. Upstart fährt damit fort, bis alle notwendigen Jobs abgeschlossen sind.

## Exercise

Übung macht den Meister! Obwohl Upstart ein älteres Init-System ist, ist das Verständnis, wie Prozesse verwaltet und Aufgaben geplant werden, für jeden Linux-Administrator entscheidend. Hier sind einige praktische Übungen, um Ihr Verständnis von Prozessmanagement und Aufgabenautomatisierung zu vertiefen, die grundlegend für die Funktionsweise von Init-Systemen sind:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, deren Überprüfung mit `ps`, die Ressourcenüberwachung mit `top` und deren Beendigung mit `kill`. Dieses Lab hilft Ihnen, den Lebenszyklus von Prozessen zu verstehen, die von Init-Systemen wie Upstart verwaltet werden.
2. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** – Lernen Sie, einmalige Jobs mit `at` und wiederkehrende Aufgaben mit `cron` zu planen. Dies bietet praktische Erfahrung mit der Aufgabenautomatisierung, einer Kernfunktion, die Init-Systeme für Systemdienste ermöglichen.

Diese Labs helfen Ihnen, die Konzepte der Prozesskontrolle und Aufgabenautomatisierung in realen Szenarien anzuwenden und Vertrauen in die Verwaltung eines Linux-Systems aufzubauen, unabhängig vom verwendeten Init-System.

## Quiz Question

Welche Init-Implementierung wird von Ubuntu verwendet?

## Quiz Answer

upstart
