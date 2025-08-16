---
lang: "de"
title: "Terminal steuern"
description: "Erfahren Sie mehr über die Steuerung von Terminals in Linux, einschließlich TTY vs. PTS, und wie Prozesse an diese gebunden sind. Verstehen Sie Daemon-Prozesse. Beginnen Sie Ihre Linux-Reise!"
keywords: "Controlling Terminal, TTY, PTS, Linux Terminal, Daemon-Prozesse, Linux-Anfänger, Linux-Tutorial, Linux-Anleitung"
---

## Lesson Content

Wir haben besprochen, dass es im `ps`-Output ein TTY-Feld gibt. Das TTY ist das Terminal, das den Befehl ausgeführt hat.

Es gibt zwei Arten von Terminals: reguläre **Terminalgeräte** und **Pseudoterminalgeräte**. Ein reguläres Terminalgerät ist ein natives Terminalgerät, in das Sie tippen und Ausgaben an Ihr System senden können. Das klingt wie die Terminalanwendung, die Sie gestartet haben, um zu Ihrer Shell zu gelangen, aber das ist es nicht.

Wir werden einen kleinen Exkurs machen, damit Sie dies in Aktion sehen können. Tippen Sie Strg-Alt-F1, um in TTY1 (die erste virtuelle Konsole) zu gelangen. Sie werden bemerken, dass Sie nichts außer dem Terminal haben – keine Grafiken usw. Dies wird als reguläres Terminalgerät betrachtet. Sie können dies mit Strg-Alt-F7 verlassen.

Ein Pseudoterminal ist das, womit Sie bisher gearbeitet haben. Sie emulieren Terminals mit dem Shell-Terminalfenster und werden durch PTS gekennzeichnet. Wenn Sie sich `ps` noch einmal ansehen, sehen Sie Ihren Shell-Prozess unter `pts/*`.

Okay, nun zurück zum Controlling Terminal: Prozesse sind normalerweise an ein Controlling Terminal gebunden. Wenn Sie beispielsweise ein Programm in Ihrem Shell-Fenster, wie `find`, ausgeführt und das Fenster geschlossen hätten, würde Ihr Prozess ebenfalls damit beendet werden.

Es gibt Prozesse wie Daemon-Prozesse, die spezielle Prozesse sind, die im Wesentlichen das System am Laufen halten. Sie starten oft beim Systemstart und werden normalerweise beim Herunterfahren des Systems beendet. Sie laufen im Hintergrund, und da wir nicht möchten, dass diese speziellen Prozesse beendet werden, sind sie nicht an ein Controlling Terminal gebunden. Im `ps`-Output wird das TTY als **?** aufgeführt, was bedeutet, dass es kein Controlling Terminal hat.

## Exercise

Sehen Sie sich Ihren `ps`-Output an und listen Sie alle eindeutigen TTY-Werte auf.

## Quiz Question

Welcher Wert wird für einen Prozess angegeben, der kein Controlling Terminal hat?

## Quiz Answer

?
