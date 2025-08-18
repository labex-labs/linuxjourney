---
index: 1
lang: "es"
title: "Seguimiento de procesos: top"
meta_title: "Seguimiento de procesos: top - Utilización de Procesos"
meta_description: "Aprenda a usar el comando `top` de Linux para monitorear los recursos del sistema y rastrear procesos. Comprenda los detalles de CPU, memoria y procesos para el análisis de rendimiento."
meta_keywords: "comando top de Linux, monitorear procesos, utilización del sistema, rendimiento de Linux, principiante, tutorial, guía"
---

## Lesson Content

En este curso, repasaremos cómo leer y analizar la utilización de recursos en su sistema. Esta lección muestra algunas herramientas excelentes para usar cuando necesita rastrear lo que está haciendo un proceso.

### top

Ya hemos hablado de `top` antes, pero vamos a profundizar en los detalles de lo que realmente muestra. Recuerde, `top` es la herramienta que usamos para obtener una vista en tiempo real de la utilización del sistema por parte de nuestros procesos:

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

Repasemos lo que significa esta salida. No tiene que memorizar esto, pero vuelva a consultarlo cuando necesite una referencia.

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

Los campos son de izquierda a derecha:

1. Current time
2. How long the system has been running
3. How many users are currently logged on
4. System load average (more to come)

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - Porcentaje de tiempo de CPU dedicado a ejecutar procesos de usuario que no están niced.
2. `sy`: system CPU time - Porcentaje de tiempo de CPU dedicado a ejecutar el kernel y los procesos del kernel.
3. `ni`: nice CPU time - Porcentaje de tiempo de CPU dedicado a ejecutar procesos niced.
4. `id`: CPU idle time - Porcentaje de tiempo de CPU que se pasa inactivo.
5. `wa`: I/O wait - Porcentaje de tiempo de CPU que se pasa esperando I/O. Si este valor es bajo, el problema probablemente no sea de I/O de disco o red.
6. `hi`: hardware interrupts - Porcentaje de tiempo de CPU dedicado a atender interrupciones de hardware.
7. `si`: software interrupts - Porcentaje de tiempo de CPU dedicado a atender interrupciones de software.
8. `st`: steal time - Si está ejecutando máquinas virtuales, este es el porcentaje de tiempo de CPU que le fue robado para otras tareas.

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

1. `PID`: ID del proceso
2. `USER`: usuario propietario del proceso
3. `PR`: Priority of process
4. `NI`: The nice value
5. `VIRT`: Virtual memory used by the process
6. `RES`: Physical memory used by the process
7. `SHR`: Shared memory of the process
8. `S`: Indica el estado del proceso: `S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible, `T`=stopped
9. `%CPU`: este es el porcentaje de CPU utilizado por este proceso
10. `%MEM`: porcentaje de RAM utilizado por este proceso
11. `TIME+`: total time of activity of this process
12. `COMMAND`: name of the process

También puede especificar un ID de proceso si solo desea rastrear ciertos procesos:

```bash
top -p 1
```

## Exercise

Experimente con el comando `top` y vea qué procesos están utilizando la mayoría de los recursos.

## Quiz Question

¿Qué comando muestra la misma salida que la primera línea en `top`?

## Quiz Answer

uptime
