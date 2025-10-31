---
index: 4
lang: "de"
title: "CPU-Überwachung"
meta_title: "CPU-Überwachung - Prozessauslastung"
meta_description: "Lernen Sie die Grundlagen der Linux-CPU-Überwachung mit dem uptime-Befehl. Dieser Anfängerleitfaden erklärt, wie man die Lastdurchschnittswerte interpretiert, die Prozessauslastung versteht und die Systemleistung bewertet."
meta_keywords: "uptime-Befehl, Linux CPU-Überwachung, Lastdurchschnitt, Systemleistung, Prozessauslastung, Linux Tutorial, Anfängerleitfaden"
---

## Lesson Content

Eine grundlegende Fähigkeit bei der Verwaltung eines Linux-Systems ist das Verständnis seiner Leistung. Eines der nützlichsten Befehle für einen schnellen Gesundheitscheck ist **uptime**.

```
pete@icebox:~$ uptime
 17:23:35 up 1 day,  5:59,  2 users,  load average: 0.00, 0.02, 0.05
```

Obwohl wir `uptime` schon einmal gesehen haben, konzentrieren wir uns auf das Feld `load average` (Auslastungsdurchschnitt), das für das **Linux CPU Monitoring** entscheidend ist.

### Verständnis des Load Average

Der Load Average liefert eine Momentaufnahme der CPU-Auslastung Ihres Systems. Die drei Zahlen stehen für die durchschnittliche CPU-Auslastung über die letzten 1, 5 und 15 Minuten. Aber was ist CPU-Auslastung? Es ist die durchschnittliche Anzahl von Prozessen in der Warteschlange (run-queue), was bedeutet, dass sie entweder aktiv von der CPU ausgeführt werden oder auf ihren Einsatz warten. Diese Metrik ist ein Schlüsselindikator für die **Prozessauslastung** und die allgemeine **Systemleistung**.

### Eine Verkehrsanalyse

Stellen Sie sich eine Single-Core-CPU als eine einspurige Autobahn vor.

- Wenn die Autobahn bei konstantem Verkehrsfluss zu 100 % ausgelastet ist, entspricht dies einem Load Average von 1,0.
- Wenn ein großer Stau entsteht und sich Autos doppelt so weit stauen, wie die Autobahn Kapazität hat, beträgt die Auslastung 200 % oder ein Load Average von 2,0.
- Wenn die Autobahn halb leer ist, beträgt die Auslastung 0,5.
- Idealerweise wünschen Sie sich einen niedrigen Load Average, wie eine Autobahn um 2 Uhr morgens ohne Verkehr.

In dieser Analogie sind die Autos Prozesse, die darauf warten, von der CPU bearbeitet zu werden.

### Interpretation des Load Average auf modernen Systemen

Ein Load Average von 1,0 bedeutet nicht zwangsläufig, dass Ihr System überlastet ist. Die meisten modernen Computer verfügen über Mehrkernprozessoren. Wenn Sie einen Quad-Core (4-Kern)-Prozessor haben, bedeutet ein Load Average von 1,0, dass nur 25 % Ihrer gesamten CPU-Kapazität genutzt werden. Jeder Kern fungiert als zusätzliche Spur auf der Autobahn.

Um den Load Average richtig zu interpretieren, müssen Sie die Anzahl der CPU-Kerne berücksichtigen. Sie können die Anzahl der Kerne auf Ihrem System mit dem Befehl `cat /proc/cpuinfo` anzeigen.

Eine allgemeine Regel für gute **Systemleistung** ist, Ihren Load Average unter der Anzahl der Kerne zu halten. Wenn Sie feststellen, dass Ihr Rechner durchgehend einen Load Average hat, der höher ist als seine Kernanzahl, könnte dies auf einen Leistungsengpass hindeuten, wie z. B. einen fehlerhaften Prozess oder unzureichende Hardware-Ressourcen.

## Exercise

Um praktische Erfahrungen mit dem **Linux CPU Monitoring** und der Analyse der **Systemleistung** zu sammeln, probieren Sie diese praktischen Labs aus. Sie helfen Ihnen, die Konzepte von **Load Average** und **Prozessauslastung** in realen Szenarien anzuwenden.

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion mit und die Inspektion von Prozessen sowie die Überwachung von Ressourcen mit Tools wie `ps` und `top`, was direkt mit dem Verständnis der CPU-Last zusammenhängt.
2. **[Linux top-Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** – Lernen Sie, den `top`-Befehl für die Echtzeit-Systemüberwachung zu verwenden, einschließlich des Sortierens und Filterns von Prozessen, was einen tieferen Einblick in die CPU- und Prozessaktivität bietet.
3. **[Linux free-Befehl: Systemspeicher überwachen](https://labex.io/de/labs/linux-linux-free-command-monitoring-system-memory-388496)** – Lernen Sie, die Systemspeichernutzung zu überwachen und zu analysieren, was oft ein kritischer Faktor neben der CPU-Last für die Gesamtleistung des Systems ist.

## Quiz Question

Welchen Befehl können Sie verwenden, um den Load Average des Systems anzuzeigen? Bitte antworten Sie auf Englisch, und beachten Sie, dass der Befehl groß- und kleingeschrieben werden muss.

## Quiz Answer

uptime
