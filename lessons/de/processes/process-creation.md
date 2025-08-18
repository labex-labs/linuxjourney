---
index: 4
lang: "de"
title: "Prozesserstellung"
meta_title: "Prozesserstellung - Prozesse"
meta_description: "Erfahren Sie mehr über die Prozesserstellung unter Linux, fork und Eltern-/Kindprozesse. Verstehen Sie PID, PPID und den Init-Prozess. Ein Leitfaden für Anfänger zur Linux-Prozessverwaltung."
meta_keywords: "Linux Prozesserstellung, fork, PID, PPID, Init-Prozess, Linux Prozesse, Anfänger, Tutorial, Leitfaden"
---

## Lesson Content

Auch diese und die nächste Lektion sind rein informativ, um Ihnen einen Einblick in die Funktionsweise zu geben. Sie können gerne darauf zurückkommen, sobald Sie etwas mehr mit Prozessen gearbeitet haben.

Wenn ein neuer Prozess erstellt wird, klont sich ein bestehender Prozess im Grunde selbst mithilfe eines sogenannten `fork`-Systemaufrufs (Systemaufrufe werden erst sehr viel später besprochen). Der `fork`-Systemaufruf erstellt einen größtenteils identischen Kindprozess. Dieser Kindprozess erhält eine neue Prozess-ID (PID), und der ursprüngliche Prozess wird zu seinem Elternprozess und hat eine sogenannte Elternprozess-ID **PPID**. Danach kann der Kindprozess entweder dasselbe Programm weiterverwenden, das sein Elternteil zuvor verwendet hat, oder, häufiger, den `execve`-Systemaufruf verwenden, um ein neues Programm zu starten. Dieser Systemaufruf zerstört die Speicherverwaltung, die der Kernel für diesen Prozess eingerichtet hat, und richtet neue für das neue Programm ein.

Wir können dies in Aktion sehen:

```bash
ps l
```

Die Option `l` gibt uns ein „langes Format“ oder eine noch detailliertere Ansicht unserer laufenden Prozesse. Sie sehen eine Spalte mit der Bezeichnung **PPID**; dies ist die Eltern-ID. Schauen Sie nun auf Ihr Terminal; Sie sehen einen laufenden Prozess, der Ihre Shell ist. Auf meinem System läuft also ein Prozess `bash`. Denken Sie daran, als Sie den Befehl `ps l` ausführten, führten Sie ihn von dem Prozess aus, der `bash` ausführte. Sie werden sehen, dass die **PID** der `bash`-Shell die **PPID** des Befehls `ps l` ist.

Wenn also jeder Prozess einen Elternteil haben muss und sie nur Abspaltungen voneinander sind, muss es doch eine Mutter aller Prozesse geben, oder? Sie haben Recht. Wenn das System hochfährt, erstellt der Kernel einen Prozess namens **init**; er hat eine PID von 1. Der `init`-Prozess kann nicht beendet werden, es sei denn, das System fährt herunter. Er läuft mit Root-Rechten und führt viele Prozesse aus, die das System am Laufen halten. Wir werden `init` im Kurs zum Systemstart genauer betrachten; vorerst wissen Sie einfach, dass es der Prozess ist, der alle anderen Prozesse erzeugt.

## Exercise

Take a look at your running processes. Can you see what other processes have parents?

## Quiz Question

Welcher Systemaufruf erstellt einen neuen Prozess?

## Quiz Answer

fork
