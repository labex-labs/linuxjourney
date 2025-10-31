---
index: 2
lang: "de"
title: "Steuerndes Terminal"
meta_title: "Steuerndes Terminal - Prozesse"
meta_description: "Erkunden Sie das Konzept eines steuernden Terminals unter Linux. Erfahren Sie, was ein TTY ist, der Unterschied zwischen TTY und PTS und wie Sie die Ausgabe von 'ps tty' verwenden, um Prozesse ohne steuerndes Terminal, wie Daemons, zu identifizieren."
meta_keywords: "steuerndes Terminal, ps tty, was ist tty, ps verwenden, TTY, PTS, Linux Terminal, Daemon Prozess, Linux Prozesse"
---

## Lesson Content

Wenn Sie laufende Prozesse untersuchen, werden Sie ein Feld `TTY` in der Ausgabe des `ps`-Befehls bemerken. Dieses Feld ist wichtig, da es das **steuernde Terminal** angibt, das den Befehl ausgeführt hat. Das Verständnis dieses Konzepts ist der Schlüssel zur effektiven Prozessverwaltung.

### Was ist ein TTY

TTY ist eine Abkürzung für „Teletype“, was historisch ein physisches Gerät zur Interaktion mit einem Computer war. In modernen Linux-Systemen bezieht sich ein TTY auf das Terminal, das die Standardeingabe und -ausgabe für einen Prozess bereitstellt.

Es gibt zwei Haupttypen von Terminals, denen Sie begegnen werden: Terminalgeräte und Pseudo-Terminalgeräte.

### Terminalgeräte im Vergleich zu Pseudo-Terminals

A true terminal device (echtes Terminalgerät) ist eine native Konsole, die es Ihnen ermöglicht, Befehle einzugeben und die Ausgabe direkt zu sehen. Sie können dies erleben, indem Sie zu einer virtuellen Konsole wechseln. Auf vielen Systemen können Sie `Strg-Alt-F1` drücken, um auf TTY1 zuzugreifen. Sie sehen eine Anmeldeaufforderung in einer rein textbasierten Umgebung, ohne grafische Oberfläche. Dies ist ein klassisches Terminalgerät. Um zu Ihrer grafischen Sitzung zurückzukehren, können Sie typischerweise `Strg-Alt-F7` verwenden (die genaue Tastenkombination kann variieren).

A pseudo-terminal (PTS), auf Deutsch Pseudo-Terminal, ist hingegen das, was Sie am häufigsten verwenden. Wenn Sie eine Terminalanwendung innerhalb Ihrer grafischen Desktop-Umgebung öffnen, verwenden Sie ein PTS. Diese emulieren ein Terminal in einem Fenster. Wenn Sie die `ps tty`-Ausgabe für Ihre Shell überprüfen, sehen Sie deren TTY als `pts/*` aufgeführt.

### Die Rolle des steuernden Terminals

Die meisten Prozesse sind an ein **steuerndes Terminal** gebunden. Das bedeutet, dass der Lebenszyklus des Prozesses mit der Terminal-Sitzung verknüpft ist, die ihn gestartet hat. Wenn Sie beispielsweise ein Programm wie `find` in Ihrem Terminalfenster ausführen und dieses Fenster dann schließen, wird auch der `find`-Prozess beendet.

### Prozesse ohne steuerndes Terminal

Einige Prozesse, bekannt als Daemons, sind dafür konzipiert, im Hintergrund zu laufen und Systemdienste zu verwalten. Diese Prozesse starten oft beim Systemstart und werden erst beim Herunterfahren beendet.

Um zu verhindern, dass sie versehentlich beendet werden, sind Daemons nicht an ein **steuerndes Terminal** angeschlossen. Wenn Sie lernen, **wie man ps verwendet**, um diese Prozesse zu untersuchen, sehen Sie ein Fragezeichen (`?`) in der TTY-Spalte. Dieses `?` signalisiert, dass der Prozess kein steuerndes Terminal hat und unabhängig von einer Benutzersitzung läuft.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Linux-Prozessen und deren Interaktion mit Terminals zu festigen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - In diesem Labor erlernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie man mit Vordergrund- und Hintergrundprozessen interagiert, sie mit `ps` inspiziert, Ressourcen mit `top` überwacht, die Priorität mit `renice` anpasst und sie mit `kill` beendet.

Dieses Labor hilft Ihnen, die Konzepte der Prozessverwaltung in realen Szenarien anzuwenden und Vertrauen in das Verständnis dafür zu gewinnen, wie Prozesse laufen und mit dem System interagieren.

## Quiz Question

Welcher Wert wird für einen Prozess angegeben, der kein steuerndes Terminal hat?

## Quiz Answer

?
