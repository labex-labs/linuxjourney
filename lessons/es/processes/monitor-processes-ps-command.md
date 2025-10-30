---
index: 1
lang: "es"
title: "ps (Procesos)"
meta_title: "ps (Procesos) - Procesos del Sistema"
meta_description: "Explora el comando ps de Linux con nuestra guía completa. Aprende a usar el comando ps -ef en Linux y otras opciones para ver procesos en ejecución, entender los PIDs y gestionar tareas del sistema. Un comienzo perfecto para tu viaje en Linux."
meta_keywords: "comando ps, ps -ef linux, comando ps -ef, linux ps -ef, ps -e linux, procesos linux, ID de proceso, PID, comando top, viaje linux"
---

## Lesson Content

### Entendiendo los Procesos de Linux

Los procesos son los programas que se están ejecutando actualmente en su máquina. El kernel de Linux los administra, y a cada proceso se le asigna un número único llamado **identificador de proceso (PID)**. Los PID generalmente se asignan secuencialmente a medida que se crean nuevos procesos.

### Uso Básico del Comando ps

Para obtener un vistazo de sus procesos activos, simplemente ejecute el comando `ps`. Esto proporciona una instantánea rápida de los procesos asociados con su sesión de terminal actual.

```plaintext
$ ps

PID        TTY     STAT   TIME          CMD
41230    pts/4    Ss        00:00:00     bash
51224    pts/4    R+        00:00:00     ps
```

Esta salida muestra algunos detalles clave:

- **PID**: El identificador de proceso único.
- **TTY**: La terminal de control para el proceso.
- **STAT**: El estado actual del proceso.
- **TIME**: El tiempo total de CPU que ha utilizado el proceso.
- **CMD**: El comando que inició el proceso.

### Explorando ps con Opciones Estilo BSD

El comando `ps` es muy versátil, con muchas opciones que caen en diferentes estilos de sintaxis (BSD, System V, GNU). El estilo BSD, que no usa un guion para las opciones, es bastante común. Una combinación popular es `ps aux`:

```bash
ps aux
```

Aquí está lo que significan estas opciones:

- **a**: Muestra todos los procesos de todos los usuarios.
- **u**: Proporciona un formato detallado y orientado al usuario.
- **x**: Incluye procesos que no están adjuntos a ninguna terminal. Estos a menudo incluyen demonios del sistema que comienzan al arrancar y muestran un `?` en la columna TTY.

Este comando ofrece una salida mucho más rica con columnas adicionales como `USER`, `%CPU`, `%MEM`, `VSZ` y `RSS`. Por ahora, nos centraremos en PID, STAT y COMMAND.

### Usando el Comando ps -ef en Linux

Otra sintaxis extremadamente popular es el estilo System V. Frecuentemente verá el **comando ps -ef** utilizado por los administradores de sistemas. Esta es una forma poderosa de obtener una imagen completa de todo lo que se ejecuta en su sistema.

```bash
ps -ef
```

El comando **ps -ef linux** proporciona una lista completa de todos los procesos.

- **-e**: Selecciona cada proceso en el sistema.
- **-f**: Muestra una lista de "formato completo", que incluye detalles como UID, PPID (Identificador de Proceso Padre), C (Utilización de CPU) y STIME (hora de inicio).

Muchos usuarios prefieren `ps -ef` sobre `ps aux` por su vista jerárquica clara e información detallada. Al solucionar problemas en un sistema Linux, ejecutar **linux ps -ef** es a menudo uno de los primeros pasos para diagnosticar problemas. Una variación más simple, `ps -e linux`, también listará todos los procesos pero en un formato menos detallado.

### Monitoreo en Tiempo Real con top

Mientras que `ps` le da una instantánea, el comando `top` proporciona una vista dinámica y en tiempo real de los procesos en su sistema. Es una excelente herramienta para identificar qué procesos están consumiendo más CPU o memoria. Por defecto, la pantalla se actualiza cada pocos segundos.

```bash
top
```

## Exercise

La práctica es clave para dominar los comandos de Linux. Los siguientes laboratorios prácticos le ayudarán a reforzar su comprensión de la monitorización y gestión de procesos:

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practique habilidades esenciales para administrar y monitorear procesos en un sistema Linux, incluida la interacción con procesos en primer plano/segundo plano, la inspección con `ps`, el monitoreo con `top` y la terminación con `kill`.
2. **[Comando Linux top: Monitoreo del Sistema en Tiempo Real](https://labex.io/es/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - Aprenda a usar el comando Linux `top` para el monitoreo del sistema en tiempo real, incluida la clasificación de procesos, el ajuste de los intervalos de actualización y el filtrado por usuario.

Estos laboratorios le ayudarán a aplicar los conceptos de identificación y monitoreo de procesos en escenarios del mundo real, aumentando su confianza como administrador de sistemas Linux.

## Quiz Question

¿Qué indicador de `ps`, cuando se usa con los indicadores `a` y `x`, se utiliza para ver información detallada y orientada al usuario sobre los procesos? Responda con una sola letra minúscula en inglés.

## Quiz Answer

u
