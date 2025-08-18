---
lang: "de"
title: "Prozess-Threads"
meta_title: "Prozess-Threads - Prozessauslastung"
meta_description: "Erfahren Sie mehr über Linux-Prozess-Threads, Single-Threaded- vs. Multi-Threaded-Konzepte und wie Sie diese mit 'ps m' anzeigen können. Verstehen Sie Lightweight-Prozesse effizient!"
meta_keywords: "Linux-Threads, Prozess-Threads, ps m Befehl, Multi-Threaded, Single-Threaded, Linux-Prozesse, Linux für Anfänger, Linux-Tutorial"
---

## Lesson Content

Vielleicht haben Sie schon von den Begriffen Single-Threaded- und Multi-Threaded-Prozesse gehört. Threads ähneln Prozessen sehr, da sie zur Ausführung desselben Programms verwendet werden; sie werden oft als Lightweight-Prozesse bezeichnet. Wenn ein Prozess einen Thread hat, ist er Single-Threaded, und wenn ein Prozess mehr als einen Thread hat, ist er Multi-Threaded. Allerdings haben alle Prozesse mindestens einen Thread.

Prozesse arbeiten mit ihren eigenen isolierten Systemressourcen; Threads können diese Ressourcen jedoch leicht untereinander teilen, was die Kommunikation erleichtert. Manchmal ist es effizienter, eine Multi-Threaded-Anwendung zu haben als eine Multi-Prozess-Anwendung.

Grundsätzlich: Nehmen wir an, Sie öffnen LibreOffice Writer und Chrome; jedes ist ein eigener, separater Prozess. Jetzt gehen Sie in Writer und beginnen, Text zu bearbeiten. Wenn Sie den Text bearbeiten, wird er automatisch gespeichert. Diese beiden parallelen "Lightweight-Prozesse" des Speicherns und Bearbeitens sind Threads.

Um Prozess-Threads anzuzeigen, können Sie Folgendes verwenden:

```plaintext
pete@icebox:~$ ps m
  PID TTY      STAT   TIME COMMAND
 2207 pts/2    -      0:01 bash
    - -        Ss     0:01 -
 5252 pts/2    -      0:00 ps m
    - -        R+     0:00 -
```

Die Prozesse werden mit jeder PID bezeichnet, und unter den Prozessen befinden sich ihre Threads (gekennzeichnet durch ein `--`). Sie können also sehen, dass die oben genannten Prozesse beide Single-Threaded sind.

## Exercise

Führen Sie den Befehl `ps m` aus und sehen Sie, welche Ihrer laufenden Prozesse Multi-Threaded sind.

## Quiz Question

Wahr oder falsch: Alle Prozesse beginnen Single-Threaded.

## Quiz Answer

True
