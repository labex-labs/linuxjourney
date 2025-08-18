---
lang: "de"
title: "ps (Prozesse)"
meta_title: "ps (Prozesse) - Prozesse"
meta_description: "Erfahren Sie mehr über den Linux-Befehl 'ps', um laufende Prozesse anzuzeigen und Prozess-IDs (PIDs) zu verstehen. Erhalten Sie eine Einführung in die Prozessverwaltung für Anfänger."
meta_keywords: "ps Befehl, Linux Prozesse, Prozess-ID, PID, Linux Tutorial, Anfänger, Anleitung, top Befehl"
---

## Lesson Content

Prozesse sind die Programme, die auf Ihrem Rechner laufen. Sie werden vom Kernel verwaltet, und jedem Prozess ist eine ID zugeordnet, die als **Prozess-ID (PID)** bezeichnet wird. Diese PID wird in der Reihenfolge zugewiesen, in der die Prozesse erstellt werden.

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
- CMD: Name des ausführbaren Programms/Befehls

Wenn Sie die Manpage für `ps` aufrufen, werden Sie feststellen, dass es viele Befehlsoptionen gibt, die Sie übergeben können. Diese variieren je nachdem, welche Optionen Sie verwenden möchten – BSD, GNU oder Unix. Meiner Meinung nach ist der BSD-Stil beliebter, daher werden wir diesen verwenden. Wenn Sie neugierig sind, der Unterschied zwischen den Stilen liegt in der Anzahl der Bindestriche, die Sie verwenden, und den Flags.

```bash
ps aux
```

Das **a** zeigt alle laufenden Prozesse an, einschließlich derer, die von anderen Benutzern ausgeführt werden. Das **u** zeigt weitere Details zu den Prozessen an. Und schließlich listet das **x** alle Prozesse auf, die kein TTY zugeordnet haben. Diese Programme zeigen ein `?` im TTY-Feld an; sie sind am häufigsten bei Daemon-Prozessen, die als Teil des Systemstarts gestartet werden.

Sie werden feststellen, dass Sie jetzt viel mehr Felder sehen. Sie müssen sich nicht alle merken; in einem späteren Kurs über fortgeschrittene Prozesse werden wir einige davon noch einmal durchgehen:

- USER: Der effektive Benutzer (derjenige, dessen Zugriff wir verwenden)
- PID: Prozess-ID
- %CPU: Verwendete CPU-Zeit geteilt durch die Laufzeit des Prozesses
- %MEM: Verhältnis der Resident Set Size des Prozesses zum physischen Speicher auf dem Rechner
- VSZ: Virtueller Speicherverbrauch des gesamten Prozesses
- RSS: Resident Set Size, der nicht ausgelagerte physische Speicher, den eine Aufgabe verwendet hat
- TTY: Steuerndes Terminal, das dem Prozess zugeordnet ist
- STAT: Prozessstatuscode
- START: Startzeit des Prozesses
- TIME: Gesamte CPU-Nutzungszeit
- COMMAND: Name des ausführbaren Programms/Befehls

Der Befehl `ps` kann etwas unübersichtlich werden. Vorerst werden wir uns am häufigsten die Felder PID, STAT und COMMAND ansehen.

Ein weiterer sehr nützlicher Befehl ist der Befehl **top**. `top` liefert Ihnen Echtzeitinformationen über die auf Ihrem System laufenden Prozesse anstelle einer Momentaufnahme. Standardmäßig erhalten Sie alle 10 Sekunden eine Aktualisierung. `top` ist ein äußerst nützliches Werkzeug, um zu sehen, welche Prozesse viele Ihrer Ressourcen beanspruchen.

```bash
top
```

## Exercise

Use the `ps` command with different flags and see how the output changes.

## Quiz Question

Welches `ps`-Flag wird verwendet, um detaillierte Informationen über Prozesse anzuzeigen?

## Quiz Answer

u
