---
index: 5
lang: "es"
title: "Monitorización de E/S"
meta_title: "Monitorización de E/S - Utilización de Procesos"
meta_description: "Domina la monitorización de E/S en Linux con el comando iostat. Esta guía explica cómo analizar métricas de uso de CPU y disco para optimizar el rendimiento de tu sistema."
meta_keywords: "monitorización de e/s, iostat, monitorización de e/s linux, uso de cpu, uso de disco, rendimiento del sistema, iowait, comandos linux"
---

## Lesson Content

La **monitorización de E/S** (I/O) eficaz es crucial para mantener un sistema Linux sano y receptivo. Una potente herramienta de línea de comandos para esta tarea es **iostat**, que proporciona informes detallados tanto de la actividad de la CPU como del disco.

Ejecutar el comando `iostat` genera una instantánea de las métricas de rendimiento de su sistema.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

La salida se divide en dos secciones principales. Vamos a desglosarlas.

### Comprensión de las Métricas de la CPU

El primer informe detalla la utilización de la CPU, proporcionando información sobre cómo el procesador está empleando su tiempo.

- **%user**: Porcentaje de tiempo de CPU dedicado a ejecutar procesos a nivel de usuario.
- **%nice**: Porcentaje de tiempo de CPU dedicado a procesos a nivel de usuario con una prioridad modificada (nice).
- **%system**: Porcentaje de tiempo de CPU dedicado a ejecutar procesos a nivel de sistema (kernel).
- **%iowait**: Porcentaje de tiempo que la CPU estuvo inactiva mientras esperaba a que se completara una solicitud de E/S de disco pendiente. Los valores altos aquí pueden indicar un cuello de botella en el almacenamiento.
- **%steal**: En un entorno virtualizado, este es el porcentaje de tiempo que una CPU virtual espera a una CPU real mientras el hipervisor atiende a otro procesador virtual.
- **%idle**: Porcentaje de tiempo que la CPU estuvo inactiva y no esperó ninguna solicitud de E/S de disco.

### Análisis de la Utilización del Disco

El segundo informe se centra en la **monitorización de E/S** a nivel de dispositivo, mostrando cómo se transfieren los datos hacia y desde sus dispositivos de almacenamiento.

- **tps**: Transferencias por segundo emitidas al dispositivo. Una transferencia es una solicitud de E/S, y varias solicitudes lógicas pueden combinarse en una sola.
- **kB_read/s**: La cantidad de datos leídos desde el dispositivo, expresada en kilobytes por segundo.
- **kB_wrtn/s**: La cantidad de datos escritos en el dispositivo, expresada en kilobytes por segundo.
- **kB_read**: El número total de kilobytes leídos desde el dispositivo desde el último reinicio.
- **kB_wrtn**: El número total de kilobytes escritos en el dispositivo desde el último reinicio.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la monitorización del sistema y el uso del disco:

1. **[Comando Linux df: Informes de Espacio en Disco](https://labex.io/es/labs/linux-linux-df-command-disk-space-reporting-219188)** - Practique la generación de informes sobre el uso del espacio en disco en sistemas de archivos montados, un aspecto clave de la monitorización.
2. **[Comando Linux du: Estimación del Espacio en Archivos](https://labex.io/es/labs/linux-linux-du-command-file-space-estimating-219190)** - Aprenda a estimar el uso del espacio en disco para directorios y subdirectorios, complementando la información de E/S de disco de `iostat`.
3. **[Comando Linux top: Monitorización del Sistema en Tiempo Real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Explore la monitorización del sistema en tiempo real, incluido el uso de CPU y memoria, lo que proporciona un contexto más amplio para las métricas de CPU vistas en `iostat`.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la monitorización de los recursos del sistema Linux.

## Quiz Question

¿Qué comando se puede utilizar para ver el uso de E/S y CPU? (Por favor, responda solo con caracteres ingleses en minúsculas)

## Quiz Answer

iostat
