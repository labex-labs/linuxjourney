---
index: 6
lang: "de"
title: "Speicherüberwachung"
meta_title: "Speicherüberwachung - Prozessauslastung"
meta_description: "Meistern Sie die Linux-Speicherüberwachung mit dem vmstat-Befehl. Diese Anleitung erklärt, wie Sie diesen leistungsstarken Monitor zur Speicherbelegung nutzen, um Systemleistungskennzahlen zu analysieren."
meta_keywords: "speicherüberwachung, speicherauslastungsmonitor, vmstat, linux speicher, systemleistung, speichernutzung, linux tutorial"
---

## Lesson Content

Eine effektive Systemadministration erfordert eine genaue Beobachtung der Ressourcennutzung, und **Speicherüberwachung** (memory monitoring) ist ein kritischer Teil dieses Prozesses. Wenn einem System der Arbeitsspeicher ausgeht, kann seine Leistung erheblich beeinträchtigt werden. Linux bietet verschiedene Tools, um den Speicherverbrauch zu verfolgen, und eines der vielseitigsten ist `vmstat`.

### Einführung in vmstat

Der Befehl `vmstat` (virtual memory statistics) ist ein leistungsstarker **Speicherauslastungsmonitor** (memory utilization monitor), der Informationen über Prozesse, Speicher, Paging, Block-I/O, Interrupts und CPU-Aktivität meldet. Wenn er ohne Argumente ausgeführt wird, liefert er eine Momentaufnahme des aktuellen Systemzustands seit dem letzten Start.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

Die Ausgabe ist in mehrere Spalten unterteilt. Lassen Sie uns aufschlüsseln, was jedes Feld bedeutet.

### Procs (Prozesse)

- `r`: Die Anzahl der lauffähigen Prozesse, die auf ihre Ausführungszeit warten.
- `b`: Die Anzahl der Prozesse im nicht unterbrechbaren Schlafmodus, typischerweise wartend auf I/O.

### Memory (Speicher)

- `swpd`: Die Menge des verwendeten virtuellen Speichers (in Kilobytes).
- `free`: Die Menge des ungenutzten Speichers (in Kilobytes).
- `buff`: Die Menge des als Puffer verwendeten Speichers.
- `cache`: Die Menge des als Seitencache verwendeten Speichers.

### Swap

- `si`: Die Menge des pro Sekunde von der Festplatte eingewechselten Speichers (swapped in) (in Kilobytes). Hohe Werte deuten darauf hin, dass dem System physischer Speicher fehlt.
- `so`: Die Menge des pro Sekunde auf die Festplatte ausgelagerten Speichers (swapped out) (in Kilobytes). Dieser Wert sollte idealerweise Null sein.

### IO (E/A)

- `bi`: Empfangene Blöcke von einem Blockgerät (Blöcke/s).
- `bo`: Gesendete Blöcke an ein Blockgerät (Blöcke/s).

### System

- `in`: Die Anzahl der Interrupts pro Sekunde, einschließlich der Uhr.
- `cs`: Die Anzahl der Kontextwechsel pro Sekunde.

### CPU

Dies sind Prozentsätze der gesamten CPU-Zeit.

- `us`: Zeit, die für die Ausführung von Nicht-Kernel-Code aufgewendet wurde (Benutzerzeit).
- `sy`: Zeit, die für die Ausführung von Kernel-Code aufgewendet wurde (Systemzeit).
- `id`: Zeit, die im Leerlauf verbracht wurde.
- `wa`: Zeit, die auf I/O gewartet wurde.
- `st`: Gestohlene Zeit von einer virtuellen Maschine (für virtualisierte Umgebungen).

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der System- und Speicherüberwachung zu festigen:

1. **[Linux free Befehl: Systemspeicher überwachen](https://labex.io/de/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Lernen Sie, die Systemspeichernutzung zu überwachen und zu analysieren, verschiedene Anzeigeformate und den gesamten Speicherverbrauch zu verstehen.
2. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Lernen Sie, die Systemleistung in Echtzeit zu überwachen, einschließlich Prozessen, CPU- und Speichernutzung, unter Verwendung verschiedener Optionen zum Sortieren und Filtern.

Diese Labs helfen Ihnen, die Konzepte der Systemressourcenüberwachung in realen Szenarien anzuwenden und Vertrauen in die Analyse der Linux-Systemleistung aufzubauen.

## Quiz Question

Welches Tool wird verwendet, um die Speicherauslastung anzuzeigen? (Bitte antworten Sie auf Englisch, achten Sie auf die Groß-/Kleinschreibung).

## Quiz Answer

vmstat
