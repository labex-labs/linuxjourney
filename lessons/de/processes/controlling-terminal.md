---
index: 2
lang: "de"
title: "Terminal steuern"
meta_title: "Terminal steuern - Prozesse"
meta_description: "Erfahren Sie mehr über die Steuerung von Terminals in Linux, einschließlich TTY vs. PTS, und wie Prozesse an diese gebunden sind. Verstehen Sie Daemon-Prozesse. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "steuerndes Terminal, TTY, PTS, Linux-Terminal, Daemon-Prozesse, Linux-Anfänger, Linux-Tutorial, Linux-Anleitung"
---

## Lesson Content

Wir haben besprochen, dass es im `ps`-Output ein TTY-Feld gibt. Das TTY ist das Terminal, das den Befehl ausgeführt hat.

Es gibt zwei Arten von Terminals: reguläre **Terminalgeräte** und **Pseudoterminalgeräte**. Ein reguläres Terminalgerät ist ein natives Terminalgerät, in das Sie tippen und Ausgaben an Ihr System senden können. Das klingt wie die Terminalanwendung, die Sie gestartet haben, um zu Ihrer Shell zu gelangen, aber das ist es nicht.

Wir werden einen kleinen Exkurs machen, damit Sie dies in Aktion sehen können. Drücken Sie Strg-Alt-F1, um in TTY1 (die erste virtuelle Konsole) zu gelangen. Sie werden bemerken, dass Sie nichts außer dem Terminal haben – keine Grafiken usw. Dies wird als reguläres Terminalgerät betrachtet. Sie können dies mit Strg-Alt-F7 beenden.

Ein Pseudoterminal ist das, woran Sie gewöhnt sind zu arbeiten. Sie emulieren Terminals mit dem Shell-Terminalfenster und werden durch PTS gekennzeichnet. Wenn Sie sich `ps` noch einmal ansehen, sehen Sie Ihren Shell-Prozess unter `pts/*`.

Okay, nun zurück zum steuernden Terminal: Prozesse sind normalerweise an ein steuerndes Terminal gebunden. Wenn Sie beispielsweise ein Programm in Ihrem Shell-Fenster, wie `find`, ausgeführt und das Fenster geschlossen hätten, würde Ihr Prozess ebenfalls damit beendet werden.

Es gibt Prozesse wie Daemon-Prozesse, die spezielle Prozesse sind, die im Wesentlichen das System am Laufen halten. Sie starten oft beim Systemstart und werden normalerweise beendet, wenn das System heruntergefahren wird. Sie laufen im Hintergrund, und da wir nicht möchten, dass diese speziellen Prozesse beendet werden, sind sie nicht an ein steuerndes Terminal gebunden. Im `ps`-Output wird das TTY als **?** aufgeführt, was bedeutet, dass es kein steuerndes Terminal hat.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Linux-Prozessen und deren Interaktion mit Terminals zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - In diesem Labor lernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden erkunden, wie Sie mit Vordergrund- und Hintergrundprozessen interagieren, diese mit `ps` inspizieren, Ressourcen mit `top` überwachen, die Priorität mit `renice` anpassen und sie mit `kill` beenden.

Dieses Labor wird Ihnen helfen, die Konzepte der Prozessverwaltung in realen Szenarien anzuwenden und Vertrauen in das Verständnis zu gewinnen, wie Prozesse ablaufen und mit dem System interagieren.

## Quiz Question

Welcher Wert wird für einen Prozess angegeben, der kein steuerndes Terminal hat?

## Quiz Answer

?
