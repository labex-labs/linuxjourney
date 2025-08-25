---
index: 4
lang: "de"
title: "Prozesserstellung"
meta_title: "Prozesserstellung - Prozesse"
meta_description: "Erfahren Sie mehr über die Erstellung von Linux-Prozessen, Fork und Eltern-/Kindprozesse. Verstehen Sie PID, PPID und den Init-Prozess. Erhalten Sie eine Einführung in die Linux-Prozessverwaltung für Anfänger."
meta_keywords: "Linux-Prozesserstellung, Fork, PID, PPID, Init-Prozess, Linux-Prozesse, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

Auch diese und die nächste Lektion dienen ausschließlich der Information, damit Sie sehen können, was sich unter der Haube verbirgt. Fühlen Sie sich frei, hierher zurückzukehren, sobald Sie etwas mehr mit Prozessen gearbeitet haben.

Wenn ein neuer Prozess erstellt wird, klont sich ein bestehender Prozess im Grunde selbst mithilfe eines sogenannten `fork`-Systemaufrufs (Systemaufrufe werden erst sehr viel später besprochen). Der `fork`-Systemaufruf erstellt einen größtenteils identischen Kindprozess. Dieser Kindprozess erhält eine neue Prozess-ID (PID), und der ursprüngliche Prozess wird zu seinem Elternprozess und hat eine sogenannte Elternprozess-ID **PPID**. Danach kann der Kindprozess entweder weiterhin dasselbe Programm verwenden, das sein Elternteil zuvor verwendet hat, oder, häufiger, den `execve`-Systemaufruf verwenden, um ein neues Programm zu starten. Dieser Systemaufruf zerstört die Speicherverwaltung, die der Kernel für diesen Prozess eingerichtet hat, und richtet neue für das neue Programm ein.

Wir können dies in Aktion sehen:

```bash
ps l
```

Die Option `l` gibt uns eine „lange Format“- oder noch detailliertere Ansicht unserer laufenden Prozesse. Sie sehen eine Spalte mit der Bezeichnung **PPID**; dies ist die Eltern-ID. Schauen Sie nun auf Ihr Terminal; Sie sehen einen laufenden Prozess, der Ihre Shell ist. Auf meinem System läuft also ein Prozess `bash`. Erinnern Sie sich nun, als Sie den Befehl `ps l` ausführten, führten Sie ihn von dem Prozess aus, der `bash` ausführte. Sie werden sehen, dass die **PID** der `bash`-Shell die **PPID** des Befehls `ps l` ist.

Wenn also jeder Prozess einen Elternteil haben muss und sie nur Forks voneinander sind, muss es doch eine Mutter aller Prozesse geben, oder? Sie haben Recht. Wenn das System hochfährt, erstellt der Kernel einen Prozess namens **init**; er hat eine PID von 1. Der `init`-Prozess kann nicht beendet werden, es sei denn, das System fährt herunter. Er läuft mit Root-Rechten und führt viele Prozesse aus, die das System am Laufen halten. Wir werden `init` im Kurs zum Systemstart genauer betrachten; vorerst wissen Sie einfach, dass es der Prozess ist, der alle anderen Prozesse erzeugt.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Linux-Prozessen und deren Verwaltung zu vertiefen:

- **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – In diesem Labor lernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie Sie mit Vordergrund- und Hintergrundprozessen interagieren, diese mit `ps` inspizieren, Ressourcen mit `top` überwachen, die Priorität mit `renice` anpassen und sie mit `kill` beenden.

Dieses Labor wird Ihnen helfen, die Konzepte von Prozess-IDs, Elternprozess-IDs und Prozessüberwachung in einem realen Szenario anzuwenden und Vertrauen in die Prozessverwaltung aufzubauen.

## Quiz Question

Welcher Systemaufruf erstellt einen neuen Prozess?

## Quiz Answer

fork
