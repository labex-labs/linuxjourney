---
index: 6
lang: "es"
title: "Monitorización de Memoria"
meta_title: "Monitorización de Memoria - Utilización de Procesos"
meta_description: "Aprende a monitorizar el uso de la memoria de Linux con vmstat. Comprende las métricas de memoria, swap y CPU para el rendimiento del sistema. ¡Comienza tu viaje en Linux!"
meta_keywords: "vmstat, monitorización de memoria Linux, rendimiento del sistema, tutorial Linux, uso de memoria, Linux para principiantes, guía Linux"
---

## Lesson Content

Además de la monitorización de la CPU y la monitorización de E/S, puedes monitorizar el uso de tu memoria con **vmstat**.

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

### memoria

- swpd - Cantidad de memoria virtual utilizada
- free - Cantidad de memoria libre
- buff - Cantidad de memoria utilizada como búferes
- cache - Cantidad de memoria utilizada como caché

### intercambio

- si - Cantidad de memoria intercambiada desde el disco
- so - Cantidad de memoria intercambiada al disco

### io

- bi - Cantidad de bloques recibidos de un dispositivo de bloques
- bo - Cantidad de bloques enviados a un dispositivo de bloques

### sistema

- in - Número de interrupciones por segundo
- cs - Número de cambios de contexto por segundo

### cpu

- us - Tiempo dedicado en modo usuario
- sy - Tiempo dedicado en modo kernel
- id - Tiempo dedicado inactivo
- wa - Tiempo dedicado esperando E/S

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la monitorización del sistema y la memoria:

1. **[Comando Linux free: Monitorización de la memoria del sistema](https://labex.io/es/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprende a monitorizar y analizar el uso de la memoria del sistema, comprendiendo varios formatos de visualización y el consumo total de memoria.
2. **[Comando Linux top: Monitorización del sistema en tiempo real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprende a monitorizar el rendimiento del sistema en tiempo real, incluyendo procesos, CPU y uso de memoria, utilizando varias opciones para ordenar y filtrar.

Estos laboratorios te ayudarán a aplicar los conceptos de monitorización de recursos del sistema en escenarios reales y a ganar confianza en el análisis del rendimiento del sistema Linux.

## Quiz Question

¿Qué herramienta se utiliza para ver la utilización de la memoria?

## Quiz Answer

vmstat
