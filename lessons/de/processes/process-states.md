---
index: 9
lang: "de"
title: "Prozesszustände"
meta_title: "Prozesszustände - Prozesse"
meta_description: "Ein umfassender Leitfaden zu Linux-Prozesszuständen. Erfahren Sie mehr über die verschiedenen Prozesszustände in Linux (R, S, D, Z, T) und wie Sie diese mit dem Befehl `ps` interpretieren können."
meta_keywords: "linux prozesszustände, prozesszustände in linux, linux prozesszustand, prozesszustand in linux, linux prozesszustände erklärt, ps befehl, STAT codes, prozessverwaltung"
---

## Lesson Content

Wenn Sie laufende Prozesse inspizieren, beispielsweise mit dem Befehl `ps aux`, werden Sie eine STAT-Spalte bemerken. Das Verständnis der Codes in dieser Spalte ist der Schlüssel zur Beherrschung der Prozessverwaltung. Jeder Code repräsentiert einen spezifischen **linux process state** (Linux-Prozesszustand).

```bash
ps aux
```

Ein **process state in Linux** (Prozesszustand unter Linux) liefert eine Momentaufnahme dessen, was ein Prozess gerade tut. Nutzt er aktiv die CPU, wartet er auf Eingaben oder wurde er beendet? Lassen Sie uns die häufigsten Zustände untersuchen, denen Sie begegnen werden.

### Dekodierung gängiger Prozesszustandscodes

Die STAT-Spalte zeigt den aktuellen **linux process state** (Linux-Prozesszustand). Obwohl es viele mögliche Zustände gibt, sind die folgenden diejenigen, die Sie am häufigsten sehen werden. Diese **linux process states explained** (erklärten Linux-Prozesszustände) helfen Ihnen bei der Diagnose des Systemverhaltens.

- **R (Running or Runnable)**: Ein Prozess in diesem Zustand führt entweder aktiv auf einem CPU-Kern aus oder befindet sich in der Warteschlange (Run Queue) und ist bereit zur Ausführung, sobald ein CPU-Kern verfügbar wird.

- **S (Interruptible Sleep)**: Dies ist einer der häufigsten **process states in Linux** (Prozesszustände unter Linux). Der Prozess wartet auf den Abschluss eines Ereignisses, wie z. B. Benutzereingaben vom Terminal oder das Eintreffen eines Netzwerkpakets. Er ist „unterbrechbar“ (interruptible), was bedeutet, dass er durch Signale geweckt werden kann.

- **D (Uninterruptible Sleep)**: Dieser Prozess schläft ebenfalls, befindet sich jedoch in einem Zustand, in dem er nicht durch ein Signal unterbrochen werden kann. Dies wird typischerweise für kurze Zeiträume bei E/A-Operationen verwendet, da eine Unterbrechung des Prozesses zu einem beschädigten Zustand führen könnte. Bleibt ein Prozess lange in diesem Zustand, kann dies auf ein Problem mit der Hardware oder einem Treiber hindeuten.

- **Z (Zombie)**: Ein Zombie-Prozess hat seine Ausführung beendet, besitzt aber immer noch einen Eintrag in der Prozesstabelle. Er wartet darauf, dass sein Elternprozess seinen Exit-Status ausliest. Einige Zombies sind normal, aber eine große Anzahl kann auf einen Fehler in der Elternanwendung hinweisen.

- **T (Stopped)**: Ein Prozess wechselt in diesen Zustand, wenn er durch ein Job-Control-Signal (wie das Drücken von `Ctrl+Z`) angehalten oder weil er von einem Debugger verfolgt wird. Er kann mit dem Signal `SIGCONT` fortgesetzt werden.

Durch das Verständnis dieser grundlegenden **linux process states** (Linux-Prozesszustände) können Sie tiefere Einblicke in die Aktivität Ihres Systems gewinnen und laufende Anwendungen effektiver verwalten.

## Exercise

Wenden Sie Ihr Wissen in der Praxis an. Das folgende Labor hilft Ihnen, Ihr Verständnis für die Linux-Prozessverwaltung und -zustände zu festigen:

1. **[Manage and Monitor Linux Processes](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - In diesem Labor erlernen Sie wesentliche Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System. Sie werden untersuchen, wie man mit Vordergrund- und Hintergrundprozessen interagiert, sie mit `ps` inspiziert, Ressourcen mit `top` überwacht, die Priorität mit `renice` anpasst und sie mit `kill` beendet.

Dieses Labor hilft Ihnen, die Konzepte der Prozesszustände in realen Szenarien anzuwenden und Vertrauen in die Linux-Prozessverwaltung aufzubauen.

## Quiz Question

Welcher STAT-Code wird verwendet, um einen nicht unterbrechbaren Schlaf (uninterruptible sleep) darzustellen? (Bitte geben Sie den einzelnen, großgeschriebenen englischen Buchstaben für den Zustands-Code an.)

## Quiz Answer

D
