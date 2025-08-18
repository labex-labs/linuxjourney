---
lang: "de"
title: "Niceness"
meta_title: "Niceness - Prozesse"
meta_description: "Erfahren Sie mehr über Linux Niceness und Prozesspriorität. Verstehen Sie die Befehle nice und renice, um die CPU-Zeit für Prozesse zu verwalten. Verbessern Sie die Systemleistung!"
meta_keywords: "Linux Niceness, Prozesspriorität, nice Befehl, renice Befehl, Linux Tutorial, CPU-Scheduling, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Wenn Sie mehrere Dinge gleichzeitig auf Ihrem Computer ausführen, wie zum Beispiel Chrome, Microsoft Word oder Photoshop, mag es so aussehen, als würden diese Prozesse gleichzeitig laufen, aber das stimmt nicht ganz.

Prozesse nutzen die CPU für eine kleine Zeitspanne, die als Zeitscheibe bezeichnet wird. Dann pausieren sie für Millisekunden, und ein anderer Prozess erhält eine kleine Zeitscheibe. Standardmäßig erfolgt die Prozessplanung nach dem Round-Robin-Verfahren. Jeder Prozess erhält genügend Zeitscheiben, bis er die Verarbeitung abgeschlossen hat. Der Kernel übernimmt all diese Prozesswechsel, und das macht er die meiste Zeit ziemlich gut.

Prozesse können nicht selbst entscheiden, wann und wie lange sie CPU-Zeit erhalten. Wenn sich alle Prozesse normal verhalten würden, würden sie jeweils (ungefähr) die gleiche Menge an CPU-Zeit erhalten. Es gibt jedoch eine Möglichkeit, den Prozessplanungsalgorithmus des Kernels mit einem nice value zu beeinflussen. Niceness ist ein ziemlich seltsamer Name, aber es bedeutet, dass Prozesse eine Zahl haben, um ihre Priorität für die CPU zu bestimmen. Eine hohe Zahl bedeutet, dass der Prozess "nice" ist und eine niedrigere Priorität für die CPU hat, und eine niedrige oder negative Zahl bedeutet, dass der Prozess nicht sehr "nice" ist und so viel CPU wie möglich erhalten möchte.

```bash
top
```

Sie sehen jetzt eine Spalte für `NI`; das ist der Niceness-Level eines Prozesses.

Um den Niceness-Level zu ändern, können Sie die Befehle `nice` und `renice` verwenden:

```bash
nice -n 5 apt upgrade
```

Der Befehl `nice` wird verwendet, um die Priorität für einen neuen Prozess festzulegen. Der Befehl `renice` wird verwendet, um die Priorität für einen bestehenden Prozess festzulegen.

```bash
renice 10 -p 3245
```

## Exercise

Welche Prozesse sind nicht sehr "nice" und warum?

## Quiz Question

Wenn ich möchte, dass ein Prozess mehr CPU-Priorität erhält, verwende ich eine niedrigere oder höhere nice number?

## Quiz Answer

lower
