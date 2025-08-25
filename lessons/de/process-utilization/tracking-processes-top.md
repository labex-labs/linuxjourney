---
index: 1
lang: "de"
title: "Prozesse verfolgen: top"
meta_title: "Prozesse verfolgen: top - Prozessauslastung"
meta_description: "Erfahren Sie, wie Sie den Linux-Befehl `top` verwenden, um Systemressourcen zu überwachen und Prozesse zu verfolgen. Verstehen Sie CPU-, Speicher- und Prozessdetails für die Leistungsanalyse."
meta_keywords: "Linux top Befehl, Prozesse überwachen, Systemauslastung, Linux-Leistung, Anfänger, Tutorial, Anleitung"
---

## Lesson Content

In diesem Kurs werden wir besprechen, wie man die Ressourcennutzung auf Ihrem System liest und analysiert. Diese Lektion zeigt einige großartige Tools, die Sie verwenden können, wenn Sie verfolgen müssen, was ein Prozess tut.

### top

Wir haben `top` bereits besprochen, aber wir werden uns die Besonderheiten dessen, was es tatsächlich anzeigt, genauer ansehen. Denken Sie daran, `top` ist das Tool, das wir verwendet haben, um eine Echtzeitansicht der Systemauslastung durch unsere Prozesse zu erhalten:

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

Lassen Sie uns durchgehen, was diese Ausgabe bedeutet. Sie müssen sich das nicht merken, aber kommen Sie darauf zurück, wenn Sie eine Referenz benötigen.

### 1. Zeile: Dies ist dieselbe Information, die Sie sehen würden, wenn Sie den Befehl `uptime` ausführen würden (mehr dazu folgt)

Die Felder sind von links nach rechts:

1. Aktuelle Uhrzeit
2. Wie lange das System bereits läuft
3. Wie viele Benutzer aktuell angemeldet sind
4. Systemlastdurchschnitt (mehr dazu folgt)

### 2. Zeile: Aufgaben, die laufen, schlafen, gestoppt und Zombie sind

### 3. Zeile: CPU-Informationen

1. `us`: Benutzer-CPU-Zeit – Prozentsatz der CPU-Zeit, die für die Ausführung von Benutzerprozessen aufgewendet wird, die nicht „niced“ sind.
2. `sy`: System-CPU-Zeit – Prozentsatz der CPU-Zeit, die für die Ausführung des Kernels und der Kernel-Prozesse aufgewendet wird.
3. `ni`: Nice-CPU-Zeit – Prozentsatz der CPU-Zeit, die für die Ausführung von „niced“ Prozessen aufgewendet wird.
4. `id`: CPU-Leerlaufzeit – Prozentsatz der CPU-Zeit, die im Leerlauf verbracht wird.
5. `wa`: I/O-Wartezeit – Prozentsatz der CPU-Zeit, die auf I/O wartet. Wenn dieser Wert niedrig ist, liegt das Problem wahrscheinlich nicht an der Festplatten- oder Netzwerk-I/O.
6. `hi`: Hardware-Interrupts – Prozentsatz der CPU-Zeit, die für die Bearbeitung von Hardware-Interrupts aufgewendet wird.
7. `si`: Software-Interrupts – Prozentsatz der CPU-Zeit, die für die Bearbeitung von Software-Interrupts aufgewendet wird.
8. `st`: Steal Time – Wenn Sie virtuelle Maschinen betreiben, ist dies der Prozentsatz der CPU-Zeit, der Ihnen für andere Aufgaben gestohlen wurde.

### 4. und 5. Zeile: Speichernutzung und Swap-Nutzung

### Liste der aktuell verwendeten Prozesse

1. `PID`: ID des Prozesses
2. `USER`: Benutzer, der der Eigentümer des Prozesses ist
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

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der Linux-Ressourcennutzung und des Prozessmanagements zu vertiefen:

1. **[Linux-Prozesse verwalten und überwachen](https://labex.io/de/labs/comptia-manage-and-monitor-linux-processes-590864)** – Üben Sie die Interaktion, Inspektion, Überwachung und Beendigung von Prozessen in einer echten Linux-Umgebung.
2. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** – Lernen Sie, den Befehl `top` zu verwenden, um die CPU-Auslastung, den Speicher und laufende Prozesse in Echtzeit zu überwachen.
3. **[Linux free Befehl: System-Speicher überwachen](https://labex.io/de/labs/linux-linux-free-command-monitoring-system-memory-388496)** – Lernen Sie, den Befehl `free` zu verwenden, um die System-Speichernutzung zu überwachen und zu analysieren.

Diese Übungen helfen Ihnen, die Konzepte in realen Szenarien anzuwenden und Vertrauen in die Systemüberwachung und das Prozessmanagement aufzubauen.

## Quiz Question

Welcher Befehl zeigt dieselbe Ausgabe wie die erste Zeile in `top` an?

## Quiz Answer

uptime
