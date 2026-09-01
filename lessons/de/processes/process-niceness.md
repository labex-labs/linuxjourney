---
lesson_id: "process-niceness"
course_id: "processes"
lang: "de"
order_index: 8
title: "Niceness"
description: "Erfahre, wie Nice-Werte das Gewicht beim CPU-Scheduling gewöhnlicher Linux-Prozesse beeinflussen."
meta_title: "Niceness – Prozesse"
meta_description: "Entdecke, was Niceness unter Linux ist und wie sie die Prozesspriorität beeinflusst. Diese Lektion erklärt die Niceness von Linux-Prozessen und den Einsatz der Befehle nice und renice zur Verwaltung des CPU-Schedulings und Verbesserung der Systemleistung."
meta_keywords: "Niceness Linux, Linux-Niceness, was ist Niceness unter Linux, Niceness von Linux-Prozessen, Niceness eines Prozesses, Prozesspriorität, nice-Befehl, renice-Befehl, CPU-Scheduling"
---

Linux kann Threads gleichzeitig auf verschiedenen CPU-Kernen ausführen und einen Kern zeitlich unter mehr ausführungsbereiten Threads aufteilen, als gleichzeitig laufen können. Der Scheduler trifft diese Entscheidungen anhand von Scheduling-Richtlinie, Priorität, Affinität und Arbeitslast. Ein Nice-Wert ist eine Eingabe für gewöhnliche Richtlinien mit zeitlicher Aufteilung.

## Nice-Werte interpretieren

Der konventionelle Nice-Bereich reicht von `-20` bis `19`:

- Ein niedrigerer Wert verleiht einer Aufgabe im Verhältnis zu vergleichbaren Aufgaben ein größeres Scheduling-Gewicht.
- Ein höherer Wert macht sie „netter“, indem er ihr ein geringeres relatives Gewicht gibt.
- Der Standardwert ist gewöhnlich `0`.

Niceness reserviert weder einen Prozentsatz einer CPU noch garantiert sie eine sofortige Ausführung. Ihre Wirkung ist am deutlichsten, wenn vergleichbare ausführungsbereite Aufgaben um CPU-Zeit konkurrieren. Echtzeitrichtlinien, cgroups, CPU-Affinität, E/A-Wartezeiten und andere Kontrollen können das beobachtete Verhalten stärker bestimmen.

:::single-choice{#process-niceness-lower-value} Welcher Nice-Wert verleiht unter derselben gewöhnlichen Scheduling-Richtlinie ein größeres relatives CPU-Gewicht?

::option[`10`]{#process-niceness-value-ten explanation="Ein positiver Wert ist netter und besitzt gewöhnlich weniger Gewicht als null oder ein negativer Wert."}
::option[`19`]{#process-niceness-value-nineteen explanation="Dies ist das netteste Ende des konventionellen Bereichs und besitzt ein vergleichsweise geringes Gewicht."}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="Niedrigere Nice-Werte entsprechen einem größeren relativen Gewicht unter vergleichbaren gewöhnlichen Aufgaben."}
:::

## Niceness anzeigen

In `top` zeigt die Spalte `NI` den Nice-Wert an. Du kannst ihn auch ausdrücklich von `ps` anfordern:

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI` ist der für Benutzer sichtbare Nice-Wert. Eine Spalte `PRI` oder eine ähnliche Spalte kann eine abgeleitete Scheduler-Priorität darstellen, deren Skala sich je nach Werkzeug und Scheduling-Klasse unterscheidet. Gehe daher nicht davon aus, dass beide Spalten austauschbar sind.

:::single-choice{#process-niceness-top-column} Welche Spalte von `top` zeigt gewöhnlich den Nice-Wert an?

::option[`PID`]{#process-niceness-column-pid explanation="`PID` kennzeichnet einen Prozess und zeigt nicht seine Scheduling-Anpassung an."}
::option[`TTY`]{#process-niceness-column-tty explanation="`TTY` kennzeichnet die Zuordnung zu einem steuernden Terminal."}
::option[`NI`]{#process-niceness-column-ni .correct explanation="`NI` ist die übliche Abkürzung für den Nice-Wert eines Prozesses oder Threads."}
:::

## Einen Befehl mit `nice` starten

Verwende `nice`, um einen neuen Befehl mit einem angepassten Wert zu starten:

```bash
$ nice -n 5 long-computation
```

Die angeforderte Anpassung und die akzeptierte Syntax kannst du im lokalen Handbuch prüfen. Ein unprivilegierter Benutzer kann einen Befehl gewöhnlich netter machen, indem er seinen Wert erhöht. Ein niedrigerer Nice-Wert und damit ein günstigeres Scheduling-Gewicht erfordern entsprechende Privilegien oder konfigurierte Ressourcenlimits.

:::single-choice{#process-niceness-nice-command} Was bewirkt `nice -n 5 long-computation`?

::option[Es startet den Befehl mit Nice-Wert 5, sofern dies erlaubt ist.]{#process-niceness-start-five .correct explanation="`nice` startet einen neuen Befehl mit der angeforderten Scheduling-Anpassung."}
::option[Es ändert PID 5 auf den niedrigstmöglichen Nice-Wert.]{#process-niceness-pid-five explanation="Der Operand nach `-n` ist ein Nice-Wert und kein PID-Ziel."}
::option[Es garantiert dem Befehl genau fünf Prozent einer CPU.]{#process-niceness-five-percent explanation="Nice-Werte drücken relatives Gewicht aus und reservieren keine festen CPU-Prozentsätze."}
:::

## Einen bestehenden Prozess mit `renice` ändern

Verwende `renice` für einen bereits laufenden Prozess:

```bash
$ renice -n 10 -p 3245
```

Dies fordert den Nice-Wert `10` für PID `3245` an. Prüfe zuerst das Ziel, da PIDs wiederverwendet werden können, und bestätige anschließend den resultierenden Wert. Berechtigungen hängen von Eigentum, Privilegien, Ressourcenlimits und Systemrichtlinien ab. Die Erhöhung des Nice-Werts ist für einen eigenen Prozess gewöhnlich erlaubt; das Rückgängigmachen dieser Änderung kann ohne Privilegien untersagt sein.

:::single-choice{#process-niceness-renice-purpose} Welches Werkzeug ändert den Nice-Wert eines bestehenden Prozesses?

::option[`nice`]{#process-niceness-tool-nice explanation="`nice` startet hauptsächlich einen neuen Befehl mit einem angepassten Wert."}
::option[`kill`]{#process-niceness-tool-kill explanation="`kill` sendet Signale und dient nicht als gewöhnlicher Niceness-Editor."}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="`renice` richtet sich abhängig von seinen Optionen an eine bestehende PID, Prozessgruppe oder einen Benutzer."}
:::

Das Lab [Linux-Prozesse verwalten und überwachen](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) bietet eine kontrollierte Umgebung zum Anzeigen und Ändern von Nice-Werten. Vergleiche konkurrierende CPU-intensive Aufgaben, statt auf einem untätigen System einen sichtbaren Unterschied zu erwarten.

## Zusammenfassung

Du kannst nun Niceness interpretieren und anpassen, ohne sie als CPU-Garantie zu behandeln.

1. Lies niedrigere Nice-Werte als größeres relatives Scheduling-Gewicht.
2. Prüfe `NI` getrennt von abgeleiteten Prioritätsfeldern.
3. Verwende `nice` beim Starten eines Befehls.
4. Verwende `renice` für einen bestehenden, überprüften Prozess.
