---
index: 6
lang: "es"
title: "Monitoreo de Memoria"
meta_title: "Monitoreo de Memoria - Utilización de Procesos"
meta_description: "Domina el monitoreo de memoria de Linux con el comando vmstat. Esta guía explica cómo usar este potente monitor de utilización de memoria para analizar métricas de rendimiento del sistema."
meta_keywords: "monitoreo de memoria, monitor de utilización de memoria, vmstat, memoria linux, rendimiento del sistema, uso de memoria, tutorial linux"
---

## Lesson Content

La administración eficaz del sistema requiere vigilar de cerca el uso de recursos, y la **monitorización de la memoria** es una parte crítica de este proceso. Cuando un sistema se queda sin memoria, su rendimiento puede degradarse significativamente. Linux proporciona varias herramientas para ayudarle a rastrear el consumo de memoria, y una de las más versátiles es `vmstat`.

### Introducción a vmstat

El comando `vmstat` (estadísticas de memoria virtual) es un potente **monitor de utilización de memoria** que informa sobre procesos, memoria, paginación, E/S de bloques, interrupciones y actividad de la CPU. Ejecutarlo sin argumentos proporciona una instantánea del estado actual del sistema desde el último arranque.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

La salida se organiza en varias columnas. Analicemos qué significa cada campo.

### Procs (Procesos)

- `r`: El número de procesos ejecutables que esperan tiempo de ejecución.
- `b`: El número de procesos en suspensión no interrumpible, generalmente esperando E/S.

### Memory (Memoria)

- `swpd`: La cantidad de memoria virtual utilizada (en kilobytes).
- `free`: La cantidad de memoria inactiva (en kilobytes).
- `buff`: La cantidad de memoria utilizada como búferes.
- `cache`: La cantidad de memoria utilizada como caché de páginas.

### Swap (Intercambio)

- `si`: La cantidad de memoria intercambiada desde el disco por segundo (en kilobytes). Los valores altos indican que el sistema tiene poca memoria física.
- `so`: La cantidad de memoria intercambiada al disco por segundo (en kilobytes). Idealmente, esto debería ser cero.

### IO (E/S)

- `bi`: Bloques recibidos de un dispositivo de bloques (bloques/s).
- `bo`: Bloques enviados a un dispositivo de bloques (bloques/s).

### System (Sistema)

- `in`: El número de interrupciones por segundo, incluyendo el reloj.
- `cs`: El número de cambios de contexto por segundo.

### CPU

Estos son porcentajes del tiempo total de la CPU.

- `us`: Tiempo dedicado a ejecutar código no kernel (tiempo de usuario).
- `sy`: Tiempo dedicado a ejecutar código kernel (tiempo de sistema).
- `id`: Tiempo dedicado a estar inactivo.
- `wa`: Tiempo dedicado a esperar E/S.
- `st`: Tiempo robado a una máquina virtual (para entornos virtualizados).

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la monitorización del sistema y la memoria:

1. **[Comando Linux free: Monitorización de la Memoria del Sistema](https://labex.io/es/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a monitorizar y analizar el uso de la memoria del sistema, comprendiendo varios formatos de visualización y el consumo total de memoria.
2. **[Comando Linux top: Monitorización del Sistema en Tiempo Real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a monitorizar el rendimiento del sistema en tiempo real, incluyendo procesos, CPU y uso de memoria, utilizando varias opciones para ordenar y filtrar.

Estos laboratorios le ayudarán a aplicar los conceptos de monitorización de recursos del sistema en escenarios reales y a ganar confianza al analizar el rendimiento del sistema Linux.

## Quiz Question

What tool is used to view memory utilization? (Please answer in English, paying attention to case sensitivity)

## Quiz Answer

vmstat
