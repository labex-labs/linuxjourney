---
index: 1
lang: "de"
title: "System V Übersicht"
meta_title: "System V Übersicht - Init"
meta_description: "Erkunden Sie das traditionelle System V Init-System, auch bekannt als SysV oder init v. Diese Anleitung behandelt, wie systemv Prozesse verwaltet, seinen sequenziellen Start und die Rolle der Runlevels unter Linux. Lernen Sie die Grundlagen des klassischen initv-Prozesses kennen."
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, Linux Runlevels, Init-System, Prozessmanagement, Linux Tutorial"
---

## Lesson Content

Die Hauptaufgabe eines Init-Systems besteht darin, wesentliche Prozesse zu starten und zu stoppen. Unter Linux gab es drei wichtige Init-Implementierungen: System V, Upstart und systemd. Diese Lektion konzentriert sich auf die traditionellste Version, **System V init**, oft als **SysV** oder einfach **systemv** (ausgesprochen „System Five“) bezeichnet.

Um festzustellen, ob Ihr System die **systemv**-Implementierung verwendet, suchen Sie nach einer Datei `/etc/inittab`. Wenn diese Datei existiert, verwenden Sie höchstwahrscheinlich eine SysV-basierte Distribution.

### Wie System V Prozesse verwaltet

Der Prozess **systemv init** startet und stoppt Dienste sequenziell. Wenn beispielsweise ein Dienst namens `foo-b` von `foo-a` abhängt, kann `foo-b` erst starten, wenn `foo-a` vollständig läuft. Das **initv**-System erreicht dies mithilfe von Shell-Skripten. Diese Skripte, die sich in bestimmten Verzeichnissen befinden, kümmern sich um das Starten und Stoppen von Diensten. Obwohl Sie benutzerdefinierte Skripte schreiben können, verlassen sich die meisten Systeme auf die vorinstallierten, die wesentliche OS-Dienste verwalten.

### Vorteile und Nachteile

Der Hauptvorteil dieses sequenziellen Ansatzes ist seine Einfachheit und Vorhersehbarkeit. Die Fehlerbehebung bei Abhängigkeiten ist unkompliziert, da Sie wissen, dass `foo-a` immer vor `foo-b` startet. Der größte Nachteil des **init v**-Modells ist jedoch die Leistung, da Dienste typischerweise nacheinander gestartet werden, was im Vergleich zu modernen parallelen Systemen zu längeren Bootzeiten führt.

### Runlevels in System V verstehen

In einer **systemv**-Umgebung wird der Zustand der Maschine durch **Runlevels** definiert, die von 0 bis 6 nummeriert sind. Diese Modi können zwischen Linux-Distributionen leicht variieren, folgen aber im Allgemeinen dieser Standardkonvention:

- 0: Herunterfahren (Shutdown)
- 1: Einzelbenutzermodus (Single User Mode)
- 2: Mehrbenutzermodus ohne Netzwerk
- 3: Mehrbenutzermodus mit Netzwerk
- 4: Unbenutzt
- 5: Mehrbenutzermodus mit Netzwerk und GUI
- 6: Neustart (Reboot)

### Init-Skripte und Verzeichnisse

Wenn Ihr System bootet, überprüft es seinen konfigurierten Runlevel und führt die entsprechenden Skripte aus. Diese Skripte befinden sich typischerweise in Verzeichnissen wie **/etc/rc.d/rc[runlevel].d/** oder in einem zentralen Verzeichnis **/etc/init.d**. Skripte, die mit `S` (Start) beginnen, werden beim Hochfahren ausgeführt, während diejenigen, die mit `K` (Kill) beginnen, beim Herunterfahren ausgeführt werden. Die Zahlen nach `S` oder `K` bestimmen die Ausführungsreihenfolge.

Zum Beispiel:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

In diesem Beispiel wird beim Wechsel zu Runlevel 0 (Herunterfahren) zuerst das Skript zum Beenden des Update-Dienstes und danach das Skript für OpenVPN ausgeführt. Den Standard-Runlevel Ihres Systems finden Sie in der Datei `/etc/inittab`, wo Sie ihn auch ändern können.

Es ist wichtig zu beachten, dass **System V** in den meisten modernen Linux-Distributionen weitgehend durch `systemd` ersetzt wurde. Sie können das Konzept der Runlevels jedoch immer noch in neueren Init-Systemen antreffen, da diese oft eine Kompatibilitätsschicht bieten, um ältere Dienste zu unterstützen, die auf **systemv init**-Skripten basieren.

## Exercise

Übung macht den Meister! Hier sind einige praktische Labs, um Ihr Verständnis für die Linux-Prozessverwaltung und Systemkonfiguration zu festigen, die grundlegend dafür sind, wie Init-Systeme funktionieren:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, inspizieren Sie diese mit `ps`, überwachen Sie Ressourcen mit `top` und beenden Sie sie mit `kill`. Dies bezieht sich direkt auf den Aspekt „wesentliche Prozesse starten und stoppen“ des Init-Systems.
2. **[Aufgaben mit at und cron unter Linux planen](https://labex.io/de/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** – Lernen Sie, einmalige und wiederkehrende Aufgaben zu planen, was auf dem Konzept der automatisierten Ausführung aufbaut, ähnlich wie Init-Skripte Dienste verwalten.
3. **[Datei- und Verzeichnisberechtigungen unter Linux verwalten](https://labex.io/de/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** – Verstehen Sie, wie Datei- und Verzeichnisberechtigungen verwaltet werden, eine entscheidende Fähigkeit für die Arbeit mit Systemkonfigurationsdateien und Skripten wie denen in `/etc/init.d`.

Diese Labs helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in grundlegende Aufgaben der Linux-Systemadministration aufzubauen.

## Quiz Question

Welcher Runlevel wird normalerweise zum Herunterfahren verwendet?

## Quiz Answer

0
