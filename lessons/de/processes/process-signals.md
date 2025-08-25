---
index: 6
lang: "de"
title: "Signale"
meta_title: "Signale - Prozesse"
meta_description: "Erfahren Sie mehr über Linux-Signale, ihren Zweck, gängige Typen wie SIGINT & SIGKILL und wie Prozesse sie handhaben. Verstehen Sie die Grundlagen von Signalen für eine bessere Linux-Kontrolle."
meta_keywords: "Linux-Signale, SIGKILL, SIGINT, Prozesskommunikation, Linux-Tutorial, Linux für Anfänger, Linux-Anleitung"
---

## Lesson Content

Ein Signal ist eine Benachrichtigung an einen Prozess, dass etwas passiert ist.

### Warum wir Signale haben

Sie sind Software-Interrupts und haben viele Verwendungszwecke:

- Ein Benutzer kann eines der speziellen Terminalzeichen (Strg-C) oder (Strg-Z) eingeben, um Prozesse zu beenden, zu unterbrechen oder anzuhalten.
- Hardwareprobleme können auftreten, und der Kernel möchte den Prozess benachrichtigen.
- Softwareprobleme können auftreten, und der Kernel möchte den Prozess benachrichtigen.
- Sie sind im Grunde genommen Möglichkeiten, wie Prozesse kommunizieren können.

### Signalprozess

Wenn ein Signal durch ein Ereignis erzeugt wird, wird es an einen Prozess übermittelt; es befindet sich in einem ausstehenden Zustand, bis es übermittelt wird. Wenn der Prozess ausgeführt wird, wird das Signal übermittelt. Prozesse haben jedoch Signalmasken, und sie können die Signalübermittlung blockieren, wenn dies angegeben ist. Wenn ein Signal übermittelt wird, kann ein Prozess eine Vielzahl von Dingen tun:

- Das Signal ignorieren.
- Das Signal "abfangen" und eine bestimmte Handler-Routine ausführen.
- Der Prozess kann beendet werden, im Gegensatz zum normalen Exit-Systemaufruf.
- Das Signal blockieren, abhängig von der Signalmaske.

### Häufige Signale

Jedes Signal wird durch Ganzzahlen mit symbolischen Namen definiert, die die Form SIGxxx haben. Einige der häufigsten Signale sind:

- SIGHUP oder HUP oder 1: Hangup
- SIGINT oder INT oder 2: Interrupt
- SIGKILL oder KILL oder 9: Kill
- SIGSEGV oder SEGV oder 11: Segmentation fault
- SIGTERM oder TERM oder 15: Software termination
- SIGSTOP oder STOP: Stop

Die Nummern können bei Signalen variieren, daher werden sie normalerweise mit ihren Namen bezeichnet.

Einige Signale sind nicht blockierbar; ein Beispiel ist das SIGKILL-Signal. Das KILL-Signal zerstört den Prozess.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Prozessen und der Verwendung von Signalen zur Interaktion mit ihnen zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – In diesem Labor lernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie Sie mit Vordergrund- und Hintergrundprozessen interagieren, diese mit `ps` inspizieren, Ressourcen mit `top` überwachen, die Priorität mit `renice` anpassen und sie mit `kill` beenden. Das Beenden von Prozessen mit `kill` ist eine direkte Anwendung des Sendens von Signalen.

Dieses Labor wird Ihnen helfen, die Konzepte des Prozessmanagements und die zugrunde liegende Verwendung von Signalen in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Welches Signal ist nicht blockierbar?

## Quiz Answer

SIGKILL
