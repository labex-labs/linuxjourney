---
index: 8
lang: "de"
title: "Nettigkeit"
meta_title: "Nettigkeit - Prozesse"
meta_description: "Erfahren Sie, was die Nettigkeit (Niceness) unter Linux ist und wie sie die Prozesspriorität beeinflusst. Diese Lektion erklärt die Linux-Prozess-Nettigkeit und die Verwendung der Befehle nice und renice zur Verwaltung der CPU-Planung und Verbesserung der Systemleistung."
meta_keywords: "niceness linux, linux niceness, was ist niceness in linux, linux prozess niceness, niceness von prozess, prozesspriorität, nice befehl, renice befehl, cpu-planung"
---

## Lesson Content

Wenn Sie mehrere Anwendungen auf Ihrem Computer ausführen, scheint es, als würden sie alle gleichzeitig laufen. In Wirklichkeit schaltet die CPU schnell zwischen ihnen um und gibt jedem Prozess eine kleine Menge an Verarbeitungszeit.

### Wie die CPU Prozesse verwaltet

Jedem Prozess wird eine kleine Menge an CPU-Zeit zugewiesen, die als "Zeitscheibe" (time slice) bezeichnet wird. Nach seiner Zeitscheibe wird ein Prozess angehalten, und die CPU wechselt zum nächsten. Standardmäßig plant der Linux-Kernel Prozesse in einer Round-Robin-Methode, um sicherzustellen, dass jeder Prozess einen fairen Anteil an CPU-Zeit erhält, bis er abgeschlossen ist. Der Scheduler des Kernels ist sehr effizient bei der Verwaltung dieser schnellen Wechsel.

### Was ist Niceness unter Linux

Obwohl Prozesse ihre CPU-Zeit nicht direkt steuern können, können Sie die Scheduling-Entscheidungen des Kernels beeinflussen. Dies geschieht durch die Anpassung des **linux niceness**-Wertes eines Prozesses. Der Begriff "Niceness" (Nettigkeit) bezieht sich darauf, wie "nett" ein Prozess zu anderen Prozessen auf dem System ist.

Die **Niceness eines Prozesses** wird durch eine Zahl zwischen -20 (höchste Priorität) und 19 (niedrigste Priorität) dargestellt.

- Ein hoher Niceness-Wert (z. B. 19) bedeutet, dass der Prozess sehr "nett" ist und eine niedrige Priorität hat, wodurch er CPU-Zeit an andere abgibt.
- Ein niedriger oder negativer Niceness-Wert (z. B. -20) bedeutet, dass der Prozess nicht "nett" ist und mehr CPU-Zeit beansprucht, was ihm eine höhere Priorität einräumt.

Das Verständnis der **linux process niceness** ist der Schlüssel zur effektiven Verwaltung von Systemressourcen.

### Anpassen der Prozesspriorität

Sie können den aktuellen Niceness-Level laufender Prozesse mit dem Befehl `top` anzeigen. Achten Sie auf die Spalte `NI`, die den Niceness-Wert anzeigt.

```bash
top
```

Um den **niceness linux**-Wert zu steuern, können Sie die Befehle `nice` und `renice` verwenden.

Verwenden Sie den Befehl `nice`, um einen neuen Prozess mit einem bestimmten Niceness-Level zu starten. Der folgende Befehl startet beispielsweise `apt upgrade` mit einer Niceness von 5.

```bash
nice -n 5 apt upgrade
```

Um die Priorität eines bereits laufenden Prozesses zu ändern, verwenden Sie den Befehl `renice`. Der folgende Befehl ändert die Niceness eines Prozesses mit der PID 3245 auf 10.

```bash
renice 10 -p 3245
```

## Exercise

Wenden Sie Ihr Wissen in diesem praktischen Labor an, um Ihr Verständnis für die Verwaltung und Planung von Linux-Prozessen zu festigen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, inspizieren Sie diese mit `ps`, überwachen Sie Ressourcen mit `top`, passen Sie die Priorität mit `renice` an und beenden Sie sie mit `kill`.

Dieses Labor hilft Ihnen, die Konzepte der Prozessplanung und Niceness in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Prozessen unter Linux aufzubauen.

## Quiz Question

Wenn Sie möchten, dass ein Prozess mehr CPU-Priorität erhält, sollten Sie eine niedrigere oder höhere "nice"-Zahl verwenden? Bitte antworten Sie in einem einzigen englischen Wort, alles kleingeschrieben.

## Quiz Answer

lower
