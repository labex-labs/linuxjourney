---
index: 4
lang: "de"
title: "Prozesserstellung"
meta_title: "Prozesserstellung - Prozesse"
meta_description: "Erkunden Sie die Grundlagen der Prozesserstellung in Linux. Dieser Leitfaden behandelt die Systemaufrufe fork und execve, Eltern-/Kind-Beziehungen (PID und PPID) und die Rolle des Init-Prozesses. Erfahren Sie, wie man einen Prozess in Linux erstellt und verstehen Sie die Kernkonzepte der Prozesserstellung im Betriebssystem."
meta_keywords: "prozesserstellung in linux, linux prozesserstellung, prozess in linux erstellen, prozesserstellung im betriebssystem, prozesserstellung, fork, execve, PID, PPID, init prozess, linux prozesse"
---

## Lesson Content

Diese Lektion untersucht die grundlegenden Konzepte, wie neue Prozesse auf einem Linux-System gestartet werden. Das Verständnis dieses Mechanismus gibt Einblick in die Funktionsweise des Betriebssystems.

### Das Fork- und Exec-Modell

der primäre Mechanismus für die **ProzessErstellung unter Linux** beinhaltet, dass ein existierender Prozess sich selbst mithilfe des Systemaufrufs `fork` klont. Der `fork`-Aufruf erzeugt einen nahezu identischen Kindprozess. Dieser neue Kindprozess erhält seine eigene eindeutige Prozess-ID (PID), während der ursprüngliche Prozess sein Elternteil wird, identifiziert durch eine Elternprozess-ID (**PPID**).

Nach dem Forken kann der Kindprozess entweder das gleiche Programm wie sein Elternteil weiter ausführen oder, was häufiger vorkommt, den Systemaufruf `execve` verwenden, um ein neues Programm zu laden und auszuführen. Der `execve`-Aufruf ersetzt effektiv den Speicherbereich des Prozesses durch den des neuen Programms und ermöglicht so den Beginn einer anderen Aufgabe. Dieses zweistufige „Fork-Exec“-Modell ist ein Eckpfeiler dafür, wie man unter Linux **einen Prozess erstellt**.

### Beobachtung von Eltern-Kind-Beziehungen

Wir können diese Eltern-Kind-Beziehung in Aktion beobachten, indem wir den Befehl `ps` verwenden:

```bash
ps l
```

Die Option `l` liefert eine Ansicht im „langen Format“ und zeigt mehr Details zu laufenden Prozessen. Sie werden eine Spalte mit der Bezeichnung **PPID** sehen, was für Parent Process ID (Elternprozess-ID) steht. Betrachten Sie den Prozess Ihrer aktuellen Shell (z. B. `bash`). Wenn Sie den Befehl `ps l` ausführen, werden Sie feststellen, dass die **PID** Ihres Shell-Prozesses mit der **PPID** des `ps l`-Prozesses übereinstimmt. Das liegt daran, dass Ihre Shell sich selbst geforkt hat, um den `ps`-Prozess zu erzeugen.

### Der Init-Prozess

Wenn jeder Prozess ein Kind eines anderen ist, muss es einen ursprünglichen Vorfahren geben. Das ist der `init`-Prozess. Wenn das System bootet, erstellt der Kernel `init` als allerersten Benutzerraumprozess und weist ihm die PID 1 zu. Der `init`-Prozess ist der ultimative Elternteil aller anderen Prozesse und läuft mit Root-Rechten, um das System zu verwalten. Er kann nicht beendet werden, bis das System heruntergefahren wird, und ist dafür verantwortlich, viele der Dienste zu starten, die das System am Laufen halten.

## Exercise

Übung macht den Meister! Hier ist ein praktisches Labor, um Ihr Verständnis von Linux-Prozessen und deren Verwaltung zu festigen:

- **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - In diesem Labor erlernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie man mit Vordergrund- und Hintergrundprozessen interagiert, sie mit `ps` inspiziert, Ressourcen mit `top` überwacht, die Priorität mit `renice` anpasst und sie mit `kill` beendet.

Dieses Labor hilft Ihnen, die Konzepte von Prozess-IDs, Elternprozess-IDs und Prozessüberwachung in einem realen Szenario anzuwenden und Selbstvertrauen im Prozessmanagement aufzubauen.

## Quiz Question

Welcher Systemaufruf erzeugt einen neuen Prozess? (Bitte antworten Sie in einem einzigen kleingeschriebenen englischen Wort.)

## Quiz Answer

fork
