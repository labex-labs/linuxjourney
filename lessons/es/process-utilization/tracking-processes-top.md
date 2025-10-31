---
index: 1
lang: "es"
title: "Seguimiento de procesos: top"
meta_title: "Seguimiento de procesos: top - Utilización de Procesos"
meta_description: "Descubre la mejor forma de aprender Linux dominando el comando `top`. Esta guía explica cómo monitorear recursos del sistema, rastrear procesos y entender métricas como VIRT y RES. Una parte clave para entender cómo funciona Linux."
meta_keywords: "comando top linux, monitorear procesos, utilización del sistema, cómo funciona linux, linux top virt res, mejor forma de aprender linux, rendimiento linux, gestión de procesos, formación linux gratis online con certificado"
---

## Lesson Content

Comprender cómo leer y analizar la utilización de recursos es una habilidad crítica para cualquier usuario de Linux. Muchos consideran que dominar las herramientas de línea de comandos es la **mejor manera de aprender Linux** desde cero, ya que proporcionan una visión profunda de **cómo funciona Linux**. Esta lección presenta `top`, una potente utilidad para rastrear lo que sus procesos están haciendo en tiempo real.

### Entendiendo el comando top

Hemos mencionado brevemente `top` antes, pero ahora profundizaremos en los detalles de lo que muestra. El comando `top` le ofrece una vista dinámica y en tiempo real de los procesos y la utilización del sistema en su máquina.

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

Repasemos lo que significa esta salida. No tiene que memorizarlo, pero puede usar esta lección como referencia.

### Resumen del Sistema

Las primeras líneas proporcionan un resumen de alto nivel del estado del sistema.

- **1ª línea**: Esta es la misma información que vería si ejecutara el comando `uptime`. Muestra la hora actual, el tiempo de actividad del sistema, el número de usuarios conectados y el promedio de carga del sistema durante los últimos 1, 5 y 15 minutos.
- **2ª línea**: Un resumen de todas las tareas (procesos), categorizados como en ejecución, durmiendo, detenidos o zombis.

### Desglose del Uso de CPU

La tercera línea detalla la utilización de la CPU.

- `us`: Porcentaje de tiempo de CPU dedicado a ejecutar procesos de usuario que no tienen nice.
- `sy`: Porcentaje de tiempo de CPU dedicado a ejecutar el kernel y sus procesos.
- `ni`: Porcentaje de tiempo de CPU dedicado a ejecutar procesos de usuario con nice (baja prioridad).
- `id`: Porcentaje de tiempo de CPU que está inactivo.
- `wa`: Porcentaje de tiempo de CPU dedicado a esperar a que se completen las operaciones de E/S. Un valor alto podría indicar un cuello de botella en el disco o la red.
- `hi`: Porcentaje de tiempo de CPU dedicado a atender interrupciones de hardware.
- `si`: Porcentaje de tiempo de CPU dedicado a atender interrupciones de software.
- `st`: Tiempo de robo (Steal time). En entornos virtualizados, este es el porcentaje de tiempo de CPU que una CPU virtual espera a una CPU real, mientras el hipervisor está atendiendo a otro procesador virtual.

### Información de Memoria y Swap

La cuarta y quinta líneas muestran el uso del espacio de memoria y swap, respectivamente. Esto incluye las cantidades total, utilizada y libre.

### La Lista de Procesos

El cuerpo principal de `top` es una lista de los procesos que consumen más recursos.

- `PID`: El Identificador de Proceso único.
- `USER`: El usuario propietario del proceso.
- `PR`: La prioridad de planificación del proceso.
- `NI`: El valor "nice", que afecta su prioridad.
- `VIRT`: Memoria Virtual utilizada por el proceso. Es la cantidad total de memoria a la que el proceso puede acceder.
- `RES`: Memoria Residente utilizada por el proceso. Es la memoria física no paginada que está utilizando una tarea. Comprender la diferencia entre **linux top virt res** es clave para el análisis de memoria.
- `SHR`: Memoria Compartida utilizada por el proceso.
- `S`: El estado del proceso: `S`=dormido (sleep), `R`=ejecutándose (running), `Z`=zombi (zombie), `D`=sueño ininterrumpible (uninterruptible sleep), `T`=detenido (stopped).
- `%CPU`: El porcentaje de tiempo de CPU utilizado por este proceso desde la última actualización.
- `%MEM`: El porcentaje de RAM física utilizada por este proceso.
- `TIME+`: El tiempo total de CPU que el proceso ha utilizado desde que comenzó.
- `COMMAND`: El nombre del comando o la línea de comandos que inició el proceso.

You can also monitor a specific process by its ID, which is useful for focused troubleshooting:

```bash
top -p 1
```

## Exercise

La práctica es esencial para el dominio. Estos laboratorios prácticos son algunos de los **mejores recursos para aprender Linux** sobre gestión de procesos, proporcionando un entorno práctico para aplicar lo aprendido.

1.  **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique la interacción, inspección, monitoreo y terminación de procesos en un entorno Linux real.
2.  **[Comando top de Linux: Monitoreo del Sistema en Tiempo Real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar el comando `top` para monitorear el uso de CPU, la memoria y los procesos en ejecución en tiempo real.
3.  **[Comando free de Linux: Monitoreo de la Memoria del Sistema](https://labex.io/es/labs/linux-linux-free-command-monitoring-system-memory-388496)** - Aprenda a usar el comando `free` para monitorear y analizar el uso de la memoria del sistema.

## Quiz Question

¿Qué comando muestra la misma salida que la primera línea en `top`? Por favor, responda usando solo el nombre del comando en inglés en minúsculas.

## Quiz Answer

uptime
