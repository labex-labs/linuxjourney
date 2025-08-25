---
index: 5
lang: "es"
title: "Monitoreo de E/S"
meta_title: "Monitoreo de E/S - Utilización de Procesos"
meta_description: "Aprende a usar iostat para el monitoreo de E/S en Linux. Comprende las métricas de uso de CPU y disco con este comando esencial. ¡Mejora el rendimiento del sistema!"
meta_keywords: "iostat, monitoreo de E/S en Linux, uso de CPU, uso de disco, comandos de Linux, principiante, tutorial, guía"
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
- **%iowait** - Muestra el porcentaje de tiempo que la CPU o CPUs estuvieron inactivas durante el cual el sistema tenía una solicitud de E/S de disco pendiente.
- **%steal** - Muestra el porcentaje de tiempo que la CPU o CPUs virtuales pasaron en espera involuntaria mientras el hipervisor estaba atendiendo a otro procesador virtual.
- **%idle** - Muestra el porcentaje de tiempo que la CPU o CPUs estuvieron inactivas y el sistema no tenía una solicitud de E/S de disco pendiente.

La segunda parte es la utilización del disco:

- **tps** - Indica el número de transferencias por segundo que se emitieron al dispositivo. Una transferencia es una solicitud de E/S al dispositivo. Múltiples solicitudes lógicas pueden combinarse en una única solicitud de E/S al dispositivo. Una transferencia es de tamaño indeterminado.
- **kB_read/s** - Indica la cantidad de datos leídos del dispositivo, expresada en kilobytes por segundo.
- **kB_wrtn/s** - Indica la cantidad de datos escritos en el dispositivo, expresada en kilobytes por segundo.
- **kB_read** - El número total de kilobytes leídos.
- **kB_wrtn** - El número total de kilobytes escritos.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del monitoreo del sistema y el uso del disco:

1. **[Comando Linux df: Informe de espacio en disco](https://labex.io/es/labs/linux-linux-df-command-disk-space-reporting-219188)** - Practica la generación de informes sobre el uso del espacio en disco en sistemas de archivos montados, un aspecto clave del monitoreo.
2. **[Comando Linux du: Estimación del espacio de archivos](https://labex.io/es/labs/linux-linux-du-command-file-space-estimating-219190)** - Aprende a estimar el uso del espacio en disco para directorios y subdirectorios, complementando la información de E/S de disco de `iostat`.
3. **[Comando Linux top: Monitoreo del sistema en tiempo real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Explora el monitoreo del sistema en tiempo real, incluyendo el uso de CPU y memoria, lo que proporciona un contexto más amplio para las métricas de CPU vistas en `iostat`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a generar confianza en el monitoreo de los recursos del sistema Linux.

## Quiz Question

¿Qué comando se puede usar para ver el uso de E/S y CPU?

## Quiz Answer

iostat
