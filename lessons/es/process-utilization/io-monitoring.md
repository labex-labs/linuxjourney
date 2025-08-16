---
lang: "es"
title: "Monitoreo de I/O"
description: "Aprende a usar iostat para el monitoreo de I/O en Linux. Comprende las métricas de uso de CPU y disco con este comando esencial. ¡Mejora el rendimiento del sistema!"
keywords: "iostat, monitoreo de I/O en Linux, uso de CPU, uso de disco, comandos de Linux, principiante, tutorial, guía"
---

## Lesson Content

Podemos monitorear el uso de la CPU, así como el uso del disco, con una herramienta útil conocida como **iostat**.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

La primera parte es la información de la CPU:

- **%user** - Muestra el porcentaje de utilización de la CPU que ocurrió mientras se ejecutaba a nivel de usuario (aplicación).
- **%nice** - Muestra el porcentaje de utilización de la CPU que ocurrió mientras se ejecutaba a nivel de usuario con prioridad nice.
- **%system** - Muestra el porcentaje de utilización de la CPU que ocurrió mientras se ejecutaba a nivel de sistema (kernel).
- **%iowait** - Muestra el porcentaje de tiempo que la CPU o CPUs estuvieron inactivas durante el cual el sistema tenía una solicitud de I/O de disco pendiente.
- **%steal** - Muestra el porcentaje de tiempo pasado en espera involuntaria por la CPU o CPUs virtuales mientras el hipervisor estaba atendiendo a otro procesador virtual.
- **%idle** - Muestra el porcentaje de tiempo que la CPU o CPUs estuvieron inactivas y el sistema no tenía una solicitud de I/O de disco pendiente.

La segunda parte es la utilización del disco:

- **tps** - Indica el número de transferencias por segundo que se emitieron al dispositivo. Una transferencia es una solicitud de I/O al dispositivo. Múltiples solicitudes lógicas pueden combinarse en una única solicitud de I/O al dispositivo. Una transferencia es de tamaño indeterminado.
- **kB_read/s** - Indica la cantidad de datos leídos del dispositivo, expresada en kilobytes por segundo.
- **kB_wrtn/s** - Indica la cantidad de datos escritos en el dispositivo, expresada en kilobytes por segundo.
- **kB_read** - El número total de kilobytes leídos.
- **kB_wrtn** - El número total de kilobytes escritos.

## Exercise

Use iostat para ver su uso de disco.

## Quiz Question

¿Qué comando se puede usar para ver el uso de I/O y CPU?

## Quiz Answer

iostat
