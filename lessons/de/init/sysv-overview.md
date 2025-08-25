---
index: 1
lang: "de"
title: "System V Übersicht"
meta_title: "System V Übersicht - Init"
meta_description: "Erfahren Sie mehr über System V init, seine Runlevels und wie es Prozesse in Linux verwaltet. Verstehen Sie die Grundlagen von SysV für Anfänger und fortgeschrittene Benutzer."
meta_keywords: "System V, SysV init, Linux Runlevels, init System, Linux Tutorial, Anfängerhandbuch, Prozessmanagement"
---

## Lesson Content

Der Hauptzweck von init ist das Starten und Stoppen wesentlicher Prozesse auf dem System. Es gibt drei Hauptimplementierungen von init in Linux: System V, Upstart und systemd. In dieser Lektion werden wir die traditionellste Version von init behandeln, System V init oder Sys V (ausgesprochen als 'System Five').

Um herauszufinden, ob Sie die Sys V init-Implementierung verwenden, suchen Sie nach einer `/etc/inittab`-Datei; wenn sie existiert, verwenden Sie höchstwahrscheinlich Sys V.

Sys V startet und stoppt Prozesse sequenziell. Wenn Sie beispielsweise einen Dienst namens `foo-a` starten möchten, kann `foo-b` erst funktionieren, wenn `foo-a` bereits läuft. Sys V erreicht dies mit Skripten. Diese Skripte starten und stoppen Dienste für uns. Wir können unsere eigenen Skripte schreiben oder, meistens, die verwenden, die bereits in das Betriebssystem integriert sind und zum Laden wesentlicher Dienste verwendet werden.

Die Vorteile der Verwendung dieser init-Implementierung sind, dass es relativ einfach ist, Abhängigkeiten zu lösen, da Sie wissen, dass `foo-a` vor `foo-b` kommt. Die Leistung ist jedoch nicht großartig, da normalerweise nur eine Sache gleichzeitig startet oder stoppt.

Bei der Verwendung von Sys V wird der Zustand der Maschine durch Runlevels definiert, die von 0 bis 6 eingestellt sind. Diese verschiedenen Modi variieren je nach Distribution, sehen aber meistens wie folgt aus:

- 0: Herunterfahren
- 1: Einzelbenutzermodus
- 2: Mehrbenutzermodus ohne Netzwerk
- 3: Mehrbenutzermodus mit Netzwerk
- 4: Unbenutzt
- 5: Mehrbenutzermodus mit Netzwerk und GUI
- 6: Neustart

Wenn Ihr System startet, prüft es, in welchem Runlevel Sie sich befinden, und führt Skripte aus, die sich in dieser Runlevel-Konfiguration befinden. Die Skripte befinden sich in **/etc/rc.d/rc[Runlevel-Nummer].d/** oder **/etc/init.d**. Skripte, die mit S (start) oder K (kill) beginnen, werden beim Start bzw. Herunterfahren ausgeführt. Die Zahlen neben diesen Zeichen geben die Reihenfolge an, in der sie ausgeführt werden.

Zum Beispiel:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Wir sehen, dass, wenn wir zu Runlevel 0 oder dem Herunterfahrmodus wechseln, unsere Maschine versuchen wird, ein Skript auszuführen, um die Update-Dienste und dann OpenVPN zu beenden. Um herauszufinden, in welchen Runlevel Ihre Maschine bootet, können Sie den Standard-Runlevel in der Datei `/etc/inittab` sehen. Sie können Ihren Standard-Runlevel auch in dieser Datei ändern.

Eine Sache ist zu beachten: System V wird langsam ersetzt, vielleicht nicht heute oder erst in Jahren. Es kann jedoch sein, dass Runlevels in anderen init-Implementierungen auftauchen. Dies dient hauptsächlich dazu, Dienste zu unterstützen, die nur mit System V init-Skripten gestartet oder gestoppt werden.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Prozessmanagements und der Systemkonfiguration zu vertiefen, die grundlegend für die Funktionsweise von Init-Systemen sind:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, deren Überprüfung mit `ps`, die Überwachung von Ressourcen mit `top` und deren Beendigung mit `kill`. Dies bezieht sich direkt auf den Aspekt des „Startens und Stoppens wesentlicher Prozesse“ von init.
2. **[Aufgaben mit at und cron in Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** – Lernen Sie, einmalige und wiederkehrende Aufgaben zu planen, was auf dem Konzept der automatisierten Ausführung aufbaut, ähnlich wie Init-Skripte Dienste verwalten.
3. **[Datei- und Verzeichnisberechtigungen in Linux verwalten](https://labex.io/de/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** – Verstehen Sie, wie Datei- und Verzeichnisberechtigungen verwaltet werden, eine entscheidende Fähigkeit für die Arbeit mit Systemkonfigurationsdateien und Skripten wie denen in `/etc/init.d`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in grundlegende Linux-Systemadministrationsaufgaben aufzubauen.

## Quiz Question

Welcher Runlevel wird normalerweise zum Herunterfahren verwendet?

## Quiz Answer

0
