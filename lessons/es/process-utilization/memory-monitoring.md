---
index: 6
lang: "es"
title: "Monitoreo de Memoria"
meta_title: "Monitoreo de Memoria - Utilización de Procesos"
meta_description: "Aprende a monitorear el uso de la memoria en Linux con vmstat. Comprende las métricas de memoria, swap y CPU para el rendimiento del sistema. ¡Comienza tu viaje en Linux!"
meta_keywords: "vmstat, monitoreo de memoria Linux, rendimiento del sistema, tutorial de Linux, uso de memoria, Linux para principiantes, guía de Linux"
---

## Lesson Content

Además del monitoreo de CPU y el monitoreo de E/S, puedes monitorear el uso de tu memoria con **vmstat**.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

Los campos son los siguientes:

### procs

- r - Número de procesos en tiempo de ejecución
- b - Número de procesos en suspensión ininterrumpible

### memory

- swpd - Cantidad de memoria virtual utilizada
- free - Cantidad de memoria libre
- buff - Cantidad de memoria utilizada como buffers
- cache - Cantidad de memoria utilizada como caché

### swap

- si - Cantidad de memoria intercambiada desde el disco (swapped in)
- so - Cantidad de memoria intercambiada hacia el disco (swapped out)

### io

- bi - Cantidad de bloques recibidos de un dispositivo de bloques
- bo - Cantidad de bloques enviados a un dispositivo de bloques

### system

- in - Número de interrupciones por segundo
- cs - Número de cambios de contexto por segundo

### cpu

- us - Tiempo dedicado en tiempo de usuario
- sy - Tiempo dedicado en tiempo de kernel
- id - Tiempo dedicado inactivo
- wa - Tiempo dedicado esperando E/S

## Exercise

Observa el uso de tu memoria con vmstat.

## Quiz Question

¿Qué herramienta se utiliza para ver la utilización de la memoria?

## Quiz Answer

vmstat
