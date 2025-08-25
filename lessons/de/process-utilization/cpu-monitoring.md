---
index: 4
lang: "de"
title: "CPU-Überwachung"
meta_title: "CPU-Überwachung - Prozessauslastung"
meta_description: "Lernen Sie die CPU-Überwachung mit dem uptime-Befehl. Verstehen Sie Lastdurchschnitt, CPU-Auslastung und wie Sie die Systemleistung für Linux-Anfänger interpretieren."
meta_keywords: "uptime Befehl, Linux CPU-Überwachung, Lastdurchschnitt, Systemleistung, Linux Tutorial, Anfängerleitfaden"
---

## Lesson Content

Lassen Sie uns einen nützlichen Befehl durchgehen: **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Wir haben in der ersten Lektion dieses Kurses über uptime gesprochen, aber wir haben das Feld für die Lastdurchschnitte noch nicht behandelt. Lastdurchschnitte sind eine gute Möglichkeit, die CPU-Auslastung Ihres Systems zu sehen. Diese Zahlen stellen die durchschnittliche CPU-Last in Intervallen von 1, 5 und 15 Minuten dar. Was meine ich mit CPU-Last? Die CPU-Last ist die durchschnittliche Anzahl von Prozessen, die darauf warten, von der CPU ausgeführt zu werden.

Nehmen wir an, Sie haben eine Single-Core-CPU; stellen Sie sich diesen Kern als eine einzelne Fahrspur im Verkehr vor. Wenn es auf der Autobahn Stoßzeit ist, wird diese Spur sehr stark befahren sein, und der Verkehr wird bei 100 % oder einer Last von 1 liegen. Jetzt ist der Verkehr so schlimm geworden, dass er die Autobahn staut und die regulären Straßen doppelt so viele Autos aufweisen; wir können sagen, dass Ihre Last 200 % oder eine Last von 2 beträgt. Nehmen wir nun an, es klärt sich etwas auf und es sind nur noch halb so viele Autos auf der Autobahnspur; wir können sagen, dass die Last der Spur 0,5 beträgt. Wenn kein Verkehr vorhanden ist und wir schneller nach Hause kommen können, sollte die Last idealerweise sehr niedrig sein, wie der Verkehr um 2 Uhr morgens. Die Autos sind in diesem Fall Prozesse, und diese Prozesse warten nur darauf, von der Autobahn zu kommen und nach Hause zu gelangen.

Nur weil Sie einen Lastdurchschnitt von 1 haben, bedeutet das nicht, dass Ihr Computer langsam ist. Die meisten modernen Maschinen haben heutzutage mehrere Kerne. Wenn Sie einen Quad-Core-Prozessor (4 Kerne) hätten und Ihr Lastdurchschnitt 1 beträgt, betrifft dies wirklich nur 25 % Ihrer CPU. Stellen Sie sich jeden Kern als eine Fahrspur im Verkehr vor. Sie können die Anzahl der Kerne, die Sie auf Ihrem System haben, mit **cat /proc/cpuinfo** anzeigen.

Bei der Beobachtung des Lastdurchschnitts müssen Sie die Anzahl der Kerne berücksichtigen. Wenn Sie feststellen, dass Ihre Maschine immer eine überdurchschnittliche Last aufweist, könnte etwas nicht in Ordnung sein.

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Überwachung der Linux-Systemleistung und der CPU-Auslastung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit und die Inspektion von Prozessen sowie die Überwachung von Ressourcen mit Tools wie `ps` und `top`, was direkt mit dem Verständnis der CPU-Last zusammenhängt.
2. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** – Lernen Sie, den Befehl `top` für die Echtzeit-Systemüberwachung zu verwenden, einschließlich des Sortierens von Prozessen und des Filterns, was einen tieferen Einblick in die CPU- und Prozessaktivität bietet.
3. **[Linux free Befehl: Systemarbeitsspeicher überwachen](https://labex.io/de/labs/linux-linux-free-command-monitoring-system-memory-388496)** – Lernen Sie, die Systemarbeitsspeichernutzung zu überwachen und zu analysieren, was oft ein kritischer Faktor neben der CPU-Last für die Gesamtleistung des Systems ist.

Diese Labs helfen Ihnen, die Konzepte der Systemüberwachung und des Ressourcenmanagements in realen Szenarien anzuwenden und Vertrauen in die Analyse der Systemleistung aufzubauen.

## Quiz Question

Welchen Befehl können Sie verwenden, um den Lastdurchschnitt anzuzeigen?

## Quiz Answer

uptime
