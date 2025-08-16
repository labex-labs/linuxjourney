---
lang: "de"
title: "Speicherüberwachung"
description: "Lernen Sie, die Linux-Speichernutzung mit vmstat zu überwachen. Verstehen Sie Speicher-, Swap- und CPU-Metriken für die Systemleistung. Beginnen Sie Ihre Linux-Reise!"
keywords: "vmstat, Linux Speicherüberwachung, Systemleistung, Linux Tutorial, Speichernutzung, Linux für Anfänger, Linux Anleitung"
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

### procs

- r - Anzahl der Prozesse für die Laufzeit
- b - Anzahl der Prozesse im ununterbrechbaren Schlafzustand

### memory

- swpd - Menge des verwendeten virtuellen Speichers
- free - Menge des freien Speichers
- buff - Menge des als Puffer verwendeten Speichers
- cache - Menge des als Cache verwendeten Speichers

### swap

- si - Menge des von der Festplatte eingelagerten Speichers (swapped in)
- so - Menge des auf die Festplatte ausgelagerten Speichers (swapped out)

### io

- bi - Menge der von einem Blockgerät empfangenen Blöcke
- bo - Menge der an ein Blockgerät gesendeten Blöcke

### system

- in - Anzahl der Interrupts pro Sekunde
- cs - Anzahl der Kontextwechsel pro Sekunde

### cpu

- us - Zeit, die im Benutzer-Modus verbracht wurde
- sy - Zeit, die im Kernel-Modus verbracht wurde
- id - Zeit, die im Leerlauf verbracht wurde
- wa - Zeit, die auf I/O gewartet wurde

## Exercise

Betrachten Sie Ihre Speichernutzung mit vmstat.

## Quiz Question

Welches Tool wird verwendet, um die Speichernutzung anzuzeigen?

## Quiz Answer

vmstat
