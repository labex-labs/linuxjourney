---
index: 8
lang: "de"
title: "Niceness"
meta_title: "Niceness - Prozesse"
meta_description: "Erfahren Sie mehr über Linux Niceness und Prozesspriorität. Verstehen Sie die Befehle nice und renice, um die CPU-Zeit für Prozesse zu verwalten. Verbessern Sie die Systemleistung!"
meta_keywords: "Linux Niceness, Prozesspriorität, nice Befehl, renice Befehl, Linux Tutorial, CPU-Planung, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Wenn Sie mehrere Dinge gleichzeitig auf Ihrem Computer ausführen, wie zum Beispiel Chrome, Microsoft Word oder Photoshop, mag es so aussehen, als würden diese Prozesse gleichzeitig laufen, aber das stimmt nicht ganz.

Prozesse nutzen die CPU für eine kurze Zeitspanne, die als Zeitscheibe bezeichnet wird. Dann pausieren sie für Millisekunden, und ein anderer Prozess erhält eine kleine Zeitscheibe. Standardmäßig erfolgt die Prozessplanung nach dem Round-Robin-Verfahren. Jeder Prozess erhält genügend Zeitscheiben, bis er die Verarbeitung abgeschlossen hat. Der Kernel übernimmt all diese Prozesswechsel, und das macht er die meiste Zeit ziemlich gut.

Prozesse können nicht selbst entscheiden, wann und wie lange sie CPU-Zeit erhalten. Wenn sich alle Prozesse normal verhalten würden, würden sie jeweils (ungefähr) die gleiche Menge an CPU-Zeit erhalten. Es gibt jedoch eine Möglichkeit, den Prozessplanungsalgorithmus des Kernels mit einem Nice-Wert zu beeinflussen. Niceness ist ein ziemlich seltsamer Name, aber es bedeutet, dass Prozesse eine Zahl haben, um ihre Priorität für die CPU zu bestimmen. Eine hohe Zahl bedeutet, dass der Prozess "nett" ist und eine niedrigere Priorität für die CPU hat, und eine niedrige oder negative Zahl bedeutet, dass der Prozess nicht sehr "nett" ist und so viel CPU wie möglich erhalten möchte.

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

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis des Linux-Prozessmanagements und der -Planung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit Vordergrund- und Hintergrundprozessen, deren Überprüfung mit `ps`, die Überwachung von Ressourcen mit `top`, die Anpassung der Priorität mit `renice` und deren Beendigung mit `kill`.

Dieses Labor wird Ihnen helfen, die Konzepte der Prozessplanung und Niceness in realen Szenarien anzuwenden und Vertrauen in die Verwaltung von Prozessen unter Linux aufzubauen.

## Quiz Question

Wenn ich möchte, dass ein Prozess mehr CPU-Priorität erhält, verwende ich dann eine niedrigere oder höhere Nice-Zahl?

## Quiz Answer

lower
