---
title: "Prozesse verfolgen: top"
description: "Erfahren Sie, wie Sie den Linux-Befehl `top` verwenden, um Systemressourcen zu überwachen und Prozesse zu verfolgen. Verstehen Sie CPU-, Speicher- und Prozessdetails für die Leistungsanalyse."
keywords: "Linux top Befehl, Prozesse überwachen, Systemauslastung, Linux Performance, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

In diesem Kurs werden wir uns ansehen, wie man die Ressourcennutzung auf Ihrem System liest und analysiert. Diese Lektion zeigt einige großartige Tools, die Sie verwenden können, wenn Sie verfolgen müssen, was ein Prozess tut.

### top

Wir haben `top` schon einmal besprochen, aber wir werden uns jetzt genauer ansehen, was es tatsächlich anzeigt. Denken Sie daran, `top` ist das Tool, das wir verwendet haben, um eine Echtzeitansicht der Systemauslastung durch unsere Prozesse zu erhalten:

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

Gehen wir durch, was diese Ausgabe bedeutet. Sie müssen sich das nicht merken, aber kommen Sie darauf zurück, wenn Sie eine Referenz benötigen.

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

Die Felder sind von links nach rechts:

1. Aktuelle Uhrzeit
2. Wie lange das System schon läuft
3. Wie viele Benutzer aktuell angemeldet sind
4. Systemlastdurchschnitt (mehr dazu folgt)

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - Prozentsatz der CPU-Zeit, die für die Ausführung von Benutzerprozessen aufgewendet wird, die nicht niced sind.
2. `sy`: system CPU time - Prozentsatz der CPU-Zeit, die für die Ausführung des Kernels und von Kernelprozessen aufgewendet wird.
3. `ni`: nice CPU time - Prozentsatz der CPU-Zeit, die für die Ausführung von niced Prozessen aufgewendet wird.
4. `id`: CPU idle time - Prozentsatz der CPU-Zeit, die im Leerlauf verbracht wird.
5. `wa`: I/O wait - Prozentsatz der CPU-Zeit, die auf I/O wartet. Wenn dieser Wert niedrig ist, liegt das Problem wahrscheinlich nicht an der Festplatten- oder Netzwerk-I/O.
6. `hi`: hardware interrupts - Prozentsatz der CPU-Zeit, die für die Bearbeitung von Hardware-Interrupts aufgewendet wird.
7. `si`: software interrupts - Prozentsatz der CPU-Zeit, die für die Bearbeitung von Software-Interrupts aufgewendet wird.
8. `st`: steal time - Wenn Sie virtuelle Maschinen betreiben, ist dies der Prozentsatz der CPU-Zeit, der Ihnen für andere Aufgaben gestohlen wurde.

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

1. `PID`: ID des Prozesses
2. `USER`: Benutzer, der der Besitzer des Prozesses ist
3. `PR`: Priorität des Prozesses
4. `NI`: Der Nice-Wert
5. `VIRT`: Virtueller Speicher, der vom Prozess verwendet wird
6. `RES`: Physischer Speicher, der vom Prozess verwendet wird
7. `SHR`: Gemeinsamer Speicher des Prozesses
8. `S`: Zeigt den Status des Prozesses an: `S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible, `T`=stopped
9. `%CPU`: Dies ist der Prozentsatz der CPU, der von diesem Prozess verwendet wird
10. `%MEM`: Prozentsatz des RAM, der von diesem Prozess verwendet wird
11. `TIME+`: Gesamtzeit der Aktivität dieses Prozesses
12. `COMMAND`: Name des Prozesses

Sie können auch eine Prozess-ID angeben, wenn Sie nur bestimmte Prozesse verfolgen möchten:

```bash
top -p 1
```

## Exercise

Spielen Sie mit dem Befehl `top` herum und sehen Sie, welche Prozesse die meisten Ressourcen verbrauchen.

## Quiz Question

Welcher Befehl zeigt die gleiche Ausgabe wie die erste Zeile in `top` an?

## Quiz Answer

uptime
