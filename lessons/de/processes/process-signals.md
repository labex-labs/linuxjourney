---
title: "Signale"
description: "Erfahren Sie mehr über Linux-Signale, ihren Zweck, gängige Typen wie SIGINT & SIGKILL und wie Prozesse sie handhaben. Verstehen Sie die Grundlagen von Signalen für eine bessere Linux-Kontrolle."
keywords: "Linux-Signale, SIGKILL, SIGINT, Prozesskommunikation, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Ein Signal ist eine Benachrichtigung an einen Prozess, dass etwas passiert ist.

### Warum wir Signale haben

Sie sind Software-Interrupts und haben viele Verwendungszwecke:

- Ein Benutzer kann eines der speziellen Terminalzeichen (Ctrl-C) oder (Ctrl-Z) eingeben, um Prozesse zu beenden, zu unterbrechen oder anzuhalten.
- Hardwareprobleme können auftreten, und der Kernel möchte den Prozess benachrichtigen.
- Softwareprobleme können auftreten, und der Kernel möchte den Prozess benachrichtigen.
- Sie sind im Grunde genommen Möglichkeiten, wie Prozesse kommunizieren können.

### Signalprozess

Wenn ein Signal durch ein Ereignis erzeugt wird, wird es an einen Prozess übermittelt; es befindet sich in einem ausstehenden Zustand, bis es zugestellt wird. Wenn der Prozess ausgeführt wird, wird das Signal zugestellt. Prozesse haben jedoch Signalmasken, und sie können die Signalzustellung blockieren, wenn dies angegeben ist. Wenn ein Signal zugestellt wird, kann ein Prozess eine Vielzahl von Dingen tun:

- Das Signal ignorieren.
- Das Signal "abfangen" und eine spezifische Handler-Routine ausführen.
- Der Prozess kann beendet werden, im Gegensatz zum normalen `exit` Systemaufruf.
- Das Signal blockieren, abhängig von der Signalmaske.

### Häufige Signale

Jedes Signal ist durch Ganzzahlen mit symbolischen Namen definiert, die in der Form `SIGxxx` vorliegen. Einige der häufigsten Signale sind:

- `SIGHUP` oder `HUP` oder 1: Hangup
- `SIGINT` oder `INT` oder 2: Interrupt
- `SIGKILL` oder `KILL` oder 9: Kill
- `SIGSEGV` oder `SEGV` oder 11: Segmentation fault
- `SIGTERM` oder `TERM` oder 15: Software termination
- `SIGSTOP` oder `STOP`: Stop

Die Nummern können bei Signalen variieren, daher werden sie normalerweise mit ihren Namen bezeichnet.

Einige Signale sind nicht blockierbar; ein Beispiel ist das `SIGKILL` Signal. Das `KILL` Signal zerstört den Prozess.

## Exercise

Keine Übungen für diese Lektion.

## Quiz Question

Welches Signal ist nicht blockierbar?

## Quiz Answer

SIGKILL
