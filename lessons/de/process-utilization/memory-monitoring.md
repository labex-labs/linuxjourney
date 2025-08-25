---
index: 6
lang: "de"
title: "Speicherüberwachung"
meta_title: "Speicherüberwachung - Prozessauslastung"
meta_description: "Lernen Sie, die Linux-Speichernutzung mit vmstat zu überwachen. Verstehen Sie Speicher-, Swap- und CPU-Metriken für die Systemleistung. Beginnen Sie Ihre Linux-Reise!"
meta_keywords: "vmstat, Linux Speicherüberwachung, Systemleistung, Linux Tutorial, Speichernutzung, Linux für Anfänger, Linux Anleitung"
---

## Lesson Content

Zusätzlich zur CPU-Überwachung und I/O-Überwachung können Sie Ihre Speichernutzung mit **vmstat** überwachen.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

Die Felder sind wie folgt:

### Prozesse

- r – Anzahl der Prozesse für die Laufzeit
- b – Anzahl der Prozesse im ununterbrechbaren Schlafzustand

### Speicher

- swpd – Genutzter virtueller Speicher
- free – Freier Speicher
- buff – Als Puffer genutzter Speicher
- cache – Als Cache genutzter Speicher

### Swap

- si – Von der Festplatte eingelagerter Speicher
- so – Auf die Festplatte ausgelagerter Speicher

### I/O

- bi – Anzahl der von einem Blockgerät empfangenen Blöcke
- bo – Anzahl der an ein Blockgerät gesendeten Blöcke

### System

- in – Anzahl der Interrupts pro Sekunde
- cs – Anzahl der Kontextwechsel pro Sekunde

### CPU

- us – Zeit im Benutzerbereich
- sy – Zeit im Kernelbereich
- id – Zeit im Leerlauf
- wa – Zeit, die auf I/O gewartet wurde

## Exercise

Übung macht den Meister! Hier sind einige praktische Übungen, um Ihr Verständnis der System- und Speicherüberwachung zu vertiefen:

1. **[Linux free Befehl: System-Speicher überwachen](https://labex.io/de/labs/linux-linux-free-command-monitoring-system-memory-388496)** – Lernen Sie, die System-Speichernutzung zu überwachen und zu analysieren, verschiedene Anzeigeformate und den gesamten Speicherverbrauch zu verstehen.
2. **[Linux top Befehl: Echtzeit-Systemüberwachung](https://labex.io/de/labs/linux-linux-top-command-real-time-system-monitoring-388500)** – Lernen Sie, die Systemleistung in Echtzeit zu überwachen, einschließlich Prozesse, CPU- und Speichernutzung, unter Verwendung verschiedener Optionen zum Sortieren und Filtern.

Diese Übungen helfen Ihnen, die Konzepte der Systemressourcenüberwachung in realen Szenarien anzuwenden und Vertrauen in die Analyse der Linux-Systemleistung aufzubauen.

## Quiz Question

Welches Tool wird verwendet, um die Speichernutzung anzuzeigen?

## Quiz Answer

vmstat
