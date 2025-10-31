---
index: 1
lang: "de"
title: "Prozesse verfolgen: top"
meta_title: "Prozesse verfolgen: top - Prozessauslastung"
meta_description: "Entdecken Sie den besten Weg, Linux zu lernen, indem Sie den Befehl `top` meistern. Dieser Leitfaden erklärt, wie Sie Systemressourcen überwachen, Prozesse verfolgen und Metriken wie VIRT und RES verstehen. Ein wesentlicher Bestandteil des Verständnisses der Funktionsweise von Linux."
meta_keywords: "Linux top Befehl, Prozesse überwachen, Systemauslastung, wie linux funktioniert, linux top virt res, bester weg linux lernen, linux performance, prozessverwaltung, kostenlose online linux schulung mit zertifikat"
---

## Lesson Content

Zu verstehen, wie man die Ressourcennutzung liest und analysiert, ist eine entscheidende Fähigkeit für jeden Linux-Benutzer. Viele halten die Beherrschung von Befehlszeilenwerkzeugen für den **besten Weg, Linux** von Grund auf zu lernen, da sie tiefe Einblicke geben, **wie Linux funktioniert**. Diese Lektion stellt `top` vor, ein leistungsstarkes Dienstprogramm zur Verfolgung dessen, was Ihre Prozesse in Echtzeit tun.

### Die top-Anweisung verstehen

Wir haben `top` bereits kurz erwähnt, aber jetzt tauchen wir in die Details dessen ein, was es anzeigt. Der Befehl `top` bietet eine dynamische Echtzeitansicht der Prozesse und der Systemauslastung auf Ihrem Rechner.

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

Gehen wir durch, was diese Ausgabe bedeutet. Sie müssen sich dies nicht merken, aber Sie können diese Lektion als Referenz verwenden.

### Systemübersicht

Die ersten Zeilen geben eine allgemeine Zusammenfassung des Systemzustands.

- **1. Zeile**: Dies sind dieselben Informationen, die Sie sehen würden, wenn Sie den Befehl `uptime` ausführen würden. Sie zeigt die aktuelle Uhrzeit, die Systemlaufzeit, die Anzahl der angemeldeten Benutzer und die Systemlastdurchschnitte der letzten 1, 5 und 15 Minuten an.
- **2. Zeile**: Eine Zusammenfassung aller Aufgaben (Prozesse), kategorisiert als laufend, schlafend, gestoppt oder Zombie.

### CPU-Auslastungsaufschlüsselung

Die dritte Zeile detailliert die CPU-Auslastung.

- `us`: Prozentsatz der CPU-Zeit, die für das Ausführen von Benutzerprozessen aufgewendet wird, die nicht "niced" sind.
- `sy`: Prozentsatz der CPU-Zeit, die für die Ausführung des Kernels und seiner Prozesse aufgewendet wird.
- `ni`: Prozentsatz der CPU-Zeit, die für das Ausführen von "niced" (niedrig priorisierten) Benutzerprozessen aufgewendet wird.
- `id`: Prozentsatz der CPU-Zeit, die untätig ist.
- `wa`: Prozentsatz der CPU-Zeit, die auf den Abschluss von E/A-Vorgängen wartet. Ein hoher Wert kann auf einen Engpass bei der Festplatte oder im Netzwerk hindeuten.
- `hi`: Prozentsatz der CPU-Zeit, die für die Behandlung von Hardware-Interrupts aufgewendet wird.
- `si`: Prozentsatz der CPU-Zeit, die für die Behandlung von Software-Interrupts aufgewendet wird.
- `st`: "Steal Time". In virtualisierten Umgebungen ist dies der Prozentsatz der CPU-Zeit, den eine virtuelle CPU auf eine reale CPU wartet, während der Hypervisor einen anderen virtuellen Prozessor bedient.

### Speicher- und Swap-Informationen

Die vierte und fünfte Zeile zeigen die Nutzung des Speicher- und Swap-Speichers an. Dies umfasst die Gesamt-, die verwendete und die freie Menge.

### Die Prozessliste

Der Hauptteil von `top` ist eine Liste der ressourcenintensivsten Prozesse.

- `PID`: Die eindeutige Prozess-ID.
- `USER`: Der Benutzer, dem der Prozess gehört.
- `PR`: Die Scheduling-Priorität des Prozesses.
- `NI`: Der "nice"-Wert, der seine Priorität beeinflusst.
- `VIRT`: Virtueller Speicher, der vom Prozess verwendet wird. Dies ist die Gesamtmenge an Speicher, auf die der Prozess zugreifen kann.
- `RES`: Resident Memory (Arbeitsspeicher), der vom Prozess verwendet wird. Dies ist der nicht ausgelagerte physische Speicher, den eine Aufgabe nutzt. Das Verständnis des Unterschieds zwischen **linux top virt res** ist der Schlüssel zur Speicheranalyse.
- `SHR`: Gemeinsam genutzter Speicher, der vom Prozess verwendet wird.
- `S`: Der Status des Prozesses: `S`=schlafend, `R`=laufend, `Z`=Zombie, `D`=nicht unterbrechbarer Schlaf, `T`=gestoppt.
- `%CPU`: Der Prozentsatz der CPU-Zeit, die dieser Prozess seit der letzten Aktualisierung verwendet hat.
- `%MEM`: Der Prozentsatz des physischen RAMs, der von diesem Prozess verwendet wird.
- `TIME+`: Die gesamte CPU-Zeit, die der Prozess seit seiner Erstellung verbraucht hat.
- `COMMAND`: Der Befehlsname oder die Befehlszeile, die den Prozess gestartet hat.

You can also monitor a specific process by its ID, which is useful for focused troubleshooting:

```bash
top -p 1
```

## Exercise

Übung ist für die Beherrschung unerlässlich. Diese praktischen Labs sind einige der **besten Ressourcen, um Linux** Prozessmanagement zu lernen, und bieten eine praktische Umgebung, um das Gelernte anzuwenden.

1.  **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** - Üben Sie die Interaktion mit, Inspektion, Überwachung und Beendigung von Prozessen in einer realen Linux-Umgebung.
2.  **[Linux top-Befehl: Systemüberwachung in Echtzeit](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Lernen Sie, den `top`-Befehl zu verwenden, um CPU-Auslastung, Speicher und laufende Prozesse in Echtzeit zu überwachen.
3.  **[Linux free-Befehl: Systemspeicher überwachen](https://labex.io/de/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Lernen Sie, den `free`-Befehl zu verwenden, um die Systemspeichernutzung zu überwachen und zu analysieren.

## Quiz Question

Welcher Befehl zeigt dieselbe Ausgabe wie die erste Zeile in `top`? Bitte antworten Sie nur mit dem kleingeschriebenen englischen Befehlsnamen.

## Quiz Answer

uptime
