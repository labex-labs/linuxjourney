---
lang: "de"
title: "System V Überblick"
description: "Erfahren Sie mehr über System V init, seine Runlevels und wie es Prozesse in Linux verwaltet. Verstehen Sie die Grundlagen von SysV für Anfänger und fortgeschrittene Benutzer."
keywords: "System V, SysV init, Linux Runlevels, init System, Linux Tutorial, Anfängerleitfaden, Prozessmanagement"
---

## Lesson Content

Der Hauptzweck von init ist es, essenzielle Prozesse auf dem System zu starten und zu stoppen. Es gibt drei wichtige Implementierungen von init in Linux: System V, Upstart und systemd. In dieser Lektion werden wir die traditionellste Version von init behandeln, System V init oder Sys V (ausgesprochen als 'System Five').

Um herauszufinden, ob Sie die Sys V init-Implementierung verwenden, überprüfen Sie, ob eine Datei `/etc/inittab` existiert; falls ja, verwenden Sie höchstwahrscheinlich Sys V.

Sys V startet und stoppt Prozesse sequenziell. Wenn Sie beispielsweise einen Dienst namens `foo-a` starten möchten, kann `foo-b` erst funktionieren, wenn `foo-a` bereits läuft. Sys V erreicht dies mit Skripten. Diese Skripte starten und stoppen Dienste für uns. Wir können unsere eigenen Skripte schreiben oder, meistens, die bereits im Betriebssystem integrierten verwenden, die zum Laden essenzieller Dienste genutzt werden.

Die Vorteile der Verwendung dieser init-Implementierung sind, dass es relativ einfach ist, Abhängigkeiten zu lösen, da man weiß, dass `foo-a` vor `foo-b` kommt. Die Leistung ist jedoch nicht großartig, da normalerweise nur eine Sache gleichzeitig startet oder stoppt.

Bei der Verwendung von Sys V wird der Zustand der Maschine durch Runlevels definiert, die von 0 bis 6 eingestellt sind. Diese verschiedenen Modi variieren je nach Distribution, sehen aber meistens wie folgt aus:

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

Wenn Ihr System startet, prüft es, in welchem Runlevel Sie sich befinden, und führt Skripte aus, die sich in der Konfiguration dieses Runlevels befinden. Die Skripte befinden sich in **/etc/rc.d/rc[runlevel number].d/** oder **/etc/init.d**. Skripte, die mit S (start) oder K (kill) beginnen, werden beim Start bzw. Herunterfahren ausgeführt. Die Zahlen neben diesen Zeichen geben die Reihenfolge an, in der sie ausgeführt werden.

Zum Beispiel:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

Wir sehen, dass, wenn wir zu Runlevel 0 oder dem Shutdown-Modus wechseln, unsere Maschine versuchen wird, ein Skript auszuführen, um die Updates-Dienste und dann OpenVPN zu beenden. Um herauszufinden, in welchen Runlevel Ihre Maschine bootet, können Sie den Standard-Runlevel in der Datei `/etc/inittab` sehen. Sie können Ihren Standard-Runlevel auch in dieser Datei ändern.

Eine Anmerkung: System V wird langsam ersetzt, vielleicht nicht heute oder erst in Jahren. Es kann jedoch sein, dass Runlevels in anderen init-Implementierungen auftauchen. Dies dient hauptsächlich dazu, Dienste zu unterstützen, die nur mit System V init-Skripten gestartet oder gestoppt werden.

## Exercise

Wenn Sie System V verwenden, ändern Sie den Standard-Runlevel Ihrer Maschine auf etwas anderes und sehen Sie, was passiert.

## Quiz Question

Welcher Runlevel wird normalerweise zum Herunterfahren verwendet?

## Quiz Answer

0
