---
index: 3
lang: "de"
title: "Prozess-Threads"
meta_title: "Prozess-Threads - Prozessauslastung"
meta_description: "Erfahren Sie mehr über Linux-Prozess-Threads, Single-Threaded- vs. Multi-Threaded-Konzepte und wie Sie diese mit 'ps m' anzeigen können. Verstehen Sie Lightweight-Prozesse effizient!"
meta_keywords: "Linux-Threads, Prozess-Threads, ps m Befehl, Multi-Threaded, Single-Threaded, Linux-Prozesse, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Vielleicht haben Sie schon von den Begriffen Single-Threaded- und Multi-Threaded-Prozesse gehört. Threads ähneln Prozessen sehr, da sie zur Ausführung desselben Programms verwendet werden; sie werden oft als Lightweight-Prozesse bezeichnet. Wenn ein Prozess einen Thread hat, ist er Single-Threaded, und wenn ein Prozess mehr als einen Thread hat, ist er Multi-Threaded. Alle Prozesse haben jedoch mindestens einen Thread.

Prozesse arbeiten mit ihren eigenen isolierten Systemressourcen; Threads können diese Ressourcen jedoch leicht untereinander teilen, was die Kommunikation erleichtert. Manchmal ist es effizienter, eine Multi-Threaded-Anwendung als eine Multi-Prozess-Anwendung zu haben.

Grundsätzlich, nehmen wir an, Sie öffnen LibreOffice Writer und Chrome; jedes ist ein eigener separater Prozess. Jetzt gehen Sie in Writer und beginnen, Text zu bearbeiten. Wenn Sie den Text bearbeiten, wird er automatisch gespeichert. Diese beiden parallelen "Lightweight-Prozesse" des Speicherns und Bearbeitens sind Threads.

Um Prozess-Threads anzuzeigen, können Sie Folgendes verwenden:

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

Die Prozesse werden mit jeder PID bezeichnet, und unter den Prozessen befinden sich ihre Threads (gekennzeichnet durch ein `--`). Sie können also sehen, dass die obigen Prozesse beide Single-Threaded sind.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Prozessen und deren Verwaltung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – In diesem Lab lernen Sie grundlegende Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie Sie mit Vordergrund- und Hintergrundprozessen interagieren, diese mit `ps` inspizieren, Ressourcen mit `top` überwachen, die Priorität mit `renice` anpassen und sie mit `kill` beenden.

Dieses Lab hilft Ihnen, die Konzepte der Prozessverwaltung in realen Szenarien anzuwenden und Vertrauen in die Überwachung der Systemaktivität aufzubauen.

## Quiz Question

Wahr oder falsch, alle Prozesse beginnen Single-Threaded.

## Quiz Answer

True
