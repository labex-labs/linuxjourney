---
index: 4
lang: "de"
title: "CPU-Überwachung"
meta_title: "CPU-Überwachung - Prozessauslastung"
meta_description: "Lernen Sie die CPU-Überwachung mit dem uptime-Befehl. Verstehen Sie Load Average, CPU-Auslastung und wie Sie die Systemleistung für Linux-Anfänger interpretieren."
meta_keywords: "uptime-Befehl, Linux CPU-Überwachung, Load Average, Systemleistung, Linux-Tutorial, Anfängerleitfaden"
---

## Lesson Content

Lassen Sie uns einen nützlichen Befehl durchgehen: **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Wir haben in der ersten Lektion dieses Kurses über uptime gesprochen, aber wir haben das Feld "load average" noch nicht behandelt. Load averages sind eine gute Möglichkeit, die CPU-Auslastung Ihres Systems zu sehen. Diese Zahlen stellen die durchschnittliche CPU-Auslastung in Intervallen von 1, 5 und 15 Minuten dar. Was meine ich mit CPU-Auslastung? Die CPU-Auslastung ist die durchschnittliche Anzahl von Prozessen, die auf die Ausführung durch die CPU warten.

Nehmen wir an, Sie haben eine Single-Core-CPU; stellen Sie sich diesen Kern als eine einzelne Fahrspur im Verkehr vor. Wenn es auf der Autobahn Stoßzeit ist, wird diese Spur sehr stark befahren sein, und der Verkehr wird bei 100% oder einer Last von 1 liegen. Nun ist der Verkehr so schlimm geworden, dass er die Autobahn staut und die normalen Straßen doppelt so viele Autos aufweisen; wir können sagen, dass Ihre Last 200% oder eine Last von 2 beträgt. Nehmen wir nun an, es klärt sich etwas auf und es sind nur noch halb so viele Autos auf der Autobahnspur; wir können sagen, die Last der Spur beträgt 0,5. Wenn kein Verkehr vorhanden ist und wir schneller nach Hause kommen können, sollte die Last idealerweise sehr niedrig sein, wie der Verkehr um 2 Uhr morgens. Die Autos in diesem Fall sind Prozesse, und diese Prozesse warten nur darauf, von der Autobahn zu kommen und nach Hause zu gelangen.

Nur weil Sie einen Load Average von 1 haben, bedeutet das nicht, dass Ihr Computer langsam ist. Die meisten modernen Maschinen haben heutzutage mehrere Kerne. Wenn Sie einen Quad-Core-Prozessor (4 Kerne) hätten und Ihr Load Average 1 beträgt, betrifft dies wirklich nur 25% Ihrer CPU. Stellen Sie sich jeden Kern als eine Fahrspur im Verkehr vor. Sie können die Anzahl der Kerne, die Sie auf Ihrem System haben, mit **cat /proc/cpuinfo** anzeigen.

Bei der Beobachtung des Load Average müssen Sie die Anzahl der Kerne berücksichtigen. Wenn Sie feststellen, dass Ihre Maschine immer eine überdurchschnittliche Last aufweist, könnte etwas nicht in Ordnung sein.

## Exercise

Überprüfen Sie die durchschnittliche Auslastung Ihres Systems und sehen Sie, was es tut.

## Quiz Question

Welchen Befehl können Sie verwenden, um die durchschnittliche Auslastung (load average) anzuzeigen?

## Quiz Answer

uptime
