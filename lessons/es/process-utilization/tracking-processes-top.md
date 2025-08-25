---
index: 1
lang: "es"
title: "Seguimiento de procesos: top"
meta_title: "Seguimiento de procesos: top - Utilización de procesos"
meta_description: "Aprenda a usar el comando `top` de Linux para monitorear los recursos del sistema y rastrear procesos. Comprenda los detalles de CPU, memoria y procesos para el análisis de rendimiento."
meta_keywords: "comando top de Linux, monitorear procesos, utilización del sistema, rendimiento de Linux, principiante, tutorial, guía"
---

## Lesson Content

En este curso, veremos cómo leer y analizar la utilización de recursos en su sistema. Esta lección muestra algunas herramientas excelentes para usar cuando necesita rastrear lo que está haciendo un proceso.

### top

Ya hemos hablado de `top` antes, pero vamos a profundizar en los detalles de lo que realmente muestra. Recuerde, `top` es la herramienta que usamos para obtener una vista en tiempo real de la utilización del sistema por nuestros procesos:

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

### Primera línea: Esta es la misma información que vería si ejecutara el comando `uptime` (más por venir)

Los campos son de izquierda a derecha:

1. Hora actual
2. Cuánto tiempo lleva el sistema en funcionamiento
3. Cuántos usuarios han iniciado sesión actualmente
4. Carga promedio del sistema (más por venir)

### Segunda línea: Tareas que se están ejecutando, en suspensión, detenidas y zombis

### Tercera línea: Información de la CPU

1. `us`: tiempo de CPU de usuario - Porcentaje de tiempo de CPU dedicado a ejecutar procesos de usuario que no están "niced".
2. `sy`: tiempo de CPU del sistema - Porcentaje de tiempo de CPU dedicado a ejecutar el kernel y los procesos del kernel.
3. `ni`: tiempo de CPU "nice" - Porcentaje de tiempo de CPU dedicado a ejecutar procesos "niced".
4. `id`: tiempo de inactividad de la CPU - Porcentaje de tiempo de CPU que se pasa inactivo.
5. `wa`: espera de E/S - Porcentaje de tiempo de CPU que se pasa esperando E/S. Si este valor es bajo, el problema probablemente no sea la E/S de disco o red.
6. `hi`: interrupciones de hardware - Porcentaje de tiempo de CPU dedicado a atender interrupciones de hardware.
7. `si`: interrupciones de software - Porcentaje de tiempo de CPU dedicado a atender interrupciones de software.
8. `st`: tiempo de robo - Si está ejecutando máquinas virtuales, este es el porcentaje de tiempo de CPU que le fue robado para otras tareas.

### Cuarta y quinta línea: Uso de memoria y uso de intercambio

### Lista de procesos que están actualmente en uso

1. `PID`: ID del proceso
2. `USER`: usuario propietario del proceso
3. `PR`: Prioridad del proceso
4. `NI`: El valor "nice"
5. `VIRT`: Memoria virtual utilizada por el proceso
6. `RES`: Memoria física utilizada por el proceso
7. `SHR`: Memoria compartida del proceso
8. `S`: Indica el estado del proceso: `S`=sleep (dormido), `R`=running (ejecutándose), `Z`=zombie, `D`=uninterruptible (ininterrumpible), `T`=stopped (detenido)
9. `%CPU`: este es el porcentaje de CPU utilizado por este proceso
10. `%MEM`: porcentaje de RAM utilizado por este proceso
11. `TIME+`: tiempo total de actividad de este proceso
12. `COMMAND`: nombre del proceso

También puede especificar un ID de proceso si solo desea rastrear ciertos procesos:

```bash
top -p 1
```

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la utilización de recursos y la gestión de procesos en Linux:

1. **[Administrar y monitorear procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción, inspección, monitoreo y terminación de procesos en un entorno Linux real.
2. **[Comando Linux top: Monitoreo del sistema en tiempo real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar el comando `top` para monitorear el uso de la CPU, la memoria y los procesos en ejecución en tiempo real.
3. **[Comando Linux free: Monitoreo de la memoria del sistema](https://labex.io/es/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a usar el comando `free` para monitorear y analizar el uso de la memoria del sistema.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con el monitoreo del sistema y la gestión de procesos.

## Quiz Question

¿Qué comando muestra la misma salida que la primera línea en `top`?

## Quiz Answer

uptime
