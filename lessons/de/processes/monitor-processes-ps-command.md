---
index: 1
lang: "de"
title: "ps (Prozesse)"
meta_title: "ps (Prozesse) - Prozesse"
meta_description: "Erfahren Sie mehr über den Linux-Befehl 'ps', um laufende Prozesse anzuzeigen und Prozess-IDs (PIDs) zu verstehen. Erhalten Sie eine Einführung in die Prozessverwaltung für Anfänger."
meta_keywords: "ps-Befehl, Linux-Prozesse, Prozess-ID, PID, Linux-Tutorial, Anfänger, Leitfaden, top-Befehl"
---

## Lesson Content

Prozesse sind die Programme, die auf Ihrem Computer ausgeführt werden. Sie werden vom Kernel verwaltet, und jedem Prozess ist eine ID zugeordnet, die als **Prozess-ID (PID)** bezeichnet wird. Diese PID wird in der Reihenfolge zugewiesen, in der die Prozesse erstellt werden.

Führen Sie den Befehl `ps` aus, um eine Liste der laufenden Prozesse anzuzeigen:

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Dies zeigt Ihnen eine schnelle Momentaufnahme der aktuellen Prozesse:

- PID: Prozess-ID
- TTY: Steuerndes Terminal, das dem Prozess zugeordnet ist (darauf gehen wir später noch genauer ein)
- STAT: Prozessstatuscode
- TIME: Gesamte CPU-Nutzungszeit
- CMD: Name der ausführbaren Datei/des Befehls

Wenn Sie die Manpage für `ps` aufrufen, werden Sie feststellen, dass es viele Befehlsoptionen gibt, die Sie übergeben können. Diese variieren je nachdem, welche Optionen Sie verwenden möchten – BSD, GNU oder Unix. Meiner Meinung nach ist der BSD-Stil beliebter, daher werden wir diesen verwenden. Wenn Sie neugierig sind, der Unterschied zwischen den Stilen liegt in der Anzahl der Bindestriche, die Sie verwenden, und den Flags.

```bash
ps aux
```

Das **a** zeigt alle laufenden Prozesse an, einschließlich derer, die von anderen Benutzern ausgeführt werden. Das **u** zeigt weitere Details zu den Prozessen an. Und schließlich listet das **x** alle Prozesse auf, denen kein TTY zugeordnet ist. Diese Programme zeigen ein `?` im TTY-Feld an; sie sind am häufigsten bei Daemon-Prozessen, die als Teil des Systemstarts gestartet werden.

Sie werden feststellen, dass Sie jetzt viel mehr Felder sehen. Sie müssen sich nicht alle merken; in einem späteren Kurs über fortgeschrittene Prozesse werden wir einige davon noch einmal durchgehen:

- USER: Der effektive Benutzer (derjenige, dessen Zugriff wir verwenden)
- PID: Prozess-ID
- %CPU: CPU-Zeit, die durch die Laufzeit des Prozesses geteilt wird
- %MEM: Verhältnis der Resident Set Size des Prozesses zum physischen Speicher auf dem Computer
- VSZ: Virtueller Speichernutzung des gesamten Prozesses
- RSS: Resident Set Size, der nicht ausgelagerte physische Speicher, den eine Aufgabe verwendet hat
- TTY: Steuerndes Terminal, das dem Prozess zugeordnet ist
- STAT: Prozessstatuscode
- START: Startzeit des Prozesses
- TIME: Gesamte CPU-Nutzungszeit
- COMMAND: Name der ausführbaren Datei/des Befehls

Der Befehl `ps` kann etwas unübersichtlich aussehen. Vorerst werden wir uns am häufigsten die Felder PID, STAT und COMMAND ansehen.

Ein weiterer sehr nützlicher Befehl ist der Befehl **top**. `top` liefert Ihnen Echtzeitinformationen über die auf Ihrem System laufenden Prozesse anstelle einer Momentaufnahme. Standardmäßig erhalten Sie alle 10 Sekunden eine Aktualisierung. `top` ist ein äußerst nützliches Werkzeug, um zu sehen, welche Prozesse viele Ihrer Ressourcen beanspruchen.

```bash
top
```

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis von Linux-Prozessen und deren Überwachung zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie grundlegende Fähigkeiten zur Verwaltung und Überwachung von Prozessen auf einem Linux-System, einschließlich der Interaktion mit Vordergrund-/Hintergrundprozessen, der Inspektion mit `ps`, der Überwachung mit `top` und der Beendigung mit `kill`.
2. **[Linux top-Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Lernen Sie, den Linux `top`-Befehl für die Echtzeit-Systemüberwachung zu verwenden, einschließlich des Sortierens von Prozessen, des Anpassen von Aktualisierungsintervallen und des Filterns nach Benutzer.

Diese Labs helfen Ihnen, die Konzepte der Prozessidentifikation und -überwachung in realen Szenarien anzuwenden und Vertrauen in die Linux-Systemadministration aufzubauen.

## Quiz Question

Welches `ps`-Flag wird verwendet, um detaillierte Informationen über Prozesse anzuzeigen?

## Quiz Answer

u
