---
index: 1
lang: "de"
title: "System V Übersicht"
meta_title: "System V Übersicht - Init"
meta_description: "Erfahren Sie mehr über System V init, seine Runlevels und wie es Prozesse in Linux verwaltet. Verstehen Sie die SysV-Grundlagen für Anfänger und fortgeschrittene Benutzer."
meta_keywords: "System V, SysV init, Linux Runlevels, init System, Linux Tutorial, Anfängerleitfaden, Prozessverwaltung"
---

## Lesson Content

Der Hauptzweck von init ist das Starten und Stoppen essentieller Prozesse auf dem System. Es gibt drei Hauptimplementierungen von init in Linux: System V, Upstart und systemd. In dieser Lektion werden wir uns die traditionellste Version von init ansehen, System V init oder Sys V (ausgesprochen als 'System Five').

Um herauszufinden, ob Sie die Sys V init Implementierung verwenden, suchen Sie nach einer Datei `/etc/inittab`; wenn diese existiert, verwenden Sie höchstwahrscheinlich Sys V.

Sys V startet und stoppt Prozesse sequenziell. Wenn Sie beispielsweise einen Dienst namens `foo-a` starten wollten, kann `foo-b` erst funktionieren, wenn `foo-a` bereits läuft. Sys V erreicht dies mit Skripten. Diese Skripte starten und stoppen Dienste für uns. Wir können unsere eigenen Skripte schreiben oder meistens die verwenden, die bereits im Betriebssystem eingebaut sind und zum Laden essentieller Dienste dienen.

Die Vorteile dieser Init-Implementierung sind, dass Abhängigkeiten relativ einfach zu lösen sind, da Sie wissen, dass `foo-a` vor `foo-b` kommt. Die Leistung ist jedoch nicht optimal, da normalerweise immer nur eine Sache gleichzeitig startet oder stoppt.

Bei der Verwendung von Sys V wird der Zustand der Maschine durch Runlevels definiert, die von 0 bis 6 festgelegt werden. Diese verschiedenen Modi variieren je nach Distribution, sehen aber meistens wie folgt aus:

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

Wenn Ihr System startet, prüft es, in welchem Runlevel es sich befindet, und führt Skripte aus, die sich in der Runlevel-Konfiguration befinden. Die Skripte befinden sich in **/etc/rc.d/rc[runlevel number].d/** oder **/etc/init.d**. Skripte, die mit S (start) oder K (kill) beginnen, werden beim Start bzw. Herunterfahren ausgeführt. Die Zahlen neben diesen Zeichen geben die Reihenfolge an, in der sie ausgeführt werden.

Zum Beispiel:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Wir sehen, dass unsere Maschine beim Wechsel zu Runlevel 0 oder dem Shutdown-Modus versuchen wird, ein Skript auszuführen, um die Updates-Dienste und dann OpenVPN zu beenden (kill). Um herauszufinden, in welchen Runlevel Ihr System bootet, können Sie den Standard-Runlevel in der Datei `/etc/inittab` einsehen. Sie können den Standard-Runlevel auch in dieser Datei ändern.

Eine Anmerkung: System V wurde in den meisten modernen Linux-Distributionen weitgehend durch systemd ersetzt. Sie können jedoch Runlevels in anderen Init-Implementierungen sehen. Dies dient hauptsächlich zur Unterstützung jener Dienste, die nur mithilfe von System V init-Skripten gestartet oder gestoppt werden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Prozessverwaltung und Systemkonfiguration zu festigen, die grundlegend dafür sind, wie Init-Systeme funktionieren:

1. **[Manage and Monitor Linux Processes](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, inspizieren Sie diese mit `ps`, überwachen Sie Ressourcen mit `top` und beenden Sie sie mit `kill`. Dies bezieht sich direkt auf den Aspekt des 'Startens und Stoppens essentieller Prozesse' von init.
2. **[Schedule Tasks with at and cron in Linux](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Lernen Sie, einmalige und wiederkehrende Aufgaben zu planen, was auf dem Konzept der automatisierten Ausführung aufbaut, ähnlich wie Init-Skripte Dienste verwalten.
3. **[Manage File and Directory Permissions in Linux](https://labex.io/de/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - Verstehen Sie, wie Sie Datei- und Verzeichnisberechtigungen verwalten, eine entscheidende Fähigkeit für die Arbeit mit Systemkonfigurationsdateien und Skripten wie denen in `/etc/init.d`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Selbstvertrauen bei grundlegenden Linux-Systemadministrationsaufgaben aufzubauen.

## Quiz Question

Welcher Runlevel wird normalerweise für das Herunterfahren verwendet?

## Quiz Answer

0
