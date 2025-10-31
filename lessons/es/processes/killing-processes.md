---
index: 7
lang: "es"
title: "kill (Terminar)"
meta_title: "kill (Terminar) - Procesos"
meta_description: "Domina el comando kill de Linux para gestionar y terminar procesos. Esta guía cubre las diferencias entre kill vs terminar, y explica señales como kill sigterm (SIGTERM), SIGKILL y kill sighup (SIGHUP)."
meta_keywords: "comando kill, kill sigterm, kill sighup, linux kill -0, kill vs terminar, kill -15 linux, SIGTERM, SIGKILL, gestión de procesos, terminar proceso"
---

## Lesson Content

En Linux, puedes gestionar procesos enviándoles señales. El comando principal para esto es `kill`, que, a pesar de su nombre, puede enviar varias señales, no solo las que terminan un proceso.

### Terminación por Defecto con kill sigterm

Cuando usas el comando `kill` solo con un ID de Proceso (PID), envía una señal `TERM` por defecto. Esta es la forma estándar y elegante de pedirle a un programa que termine.

```bash
kill 12445
```

La señal `kill sigterm` (también conocida como `SIGTERM` o señal 15) solicita que el proceso se apague limpiamente. Esto le da al proceso la oportunidad de guardar su progreso y liberar recursos adecuadamente. También puedes usar explícitamente el número de señal, haciendo que `kill -15 12445` sea equivalente al comando anterior. Esto aborda la consulta común de `kill -15 linux`.

### Forzar la Terminación con SIGKILL

A veces, un proceso deja de responder y no reacciona a una señal `SIGTERM`. En estos casos, puedes forzar su detención usando la señal `KILL`.

```bash
kill -9 12445
```

La señal `SIGKILL` (señal 9) termina el proceso inmediatamente, sin darle oportunidad de limpieza. Esta es una diferencia clave en el debate `kill vs terminate`; `SIGKILL` es una terminación incondicional, mientras que `SIGTERM` es una solicitud cortés.

### Entendiendo Otras Señales Comunes

Aunque `SIGTERM` y `SIGKILL` son las más comunes, otras señales también son útiles para la gestión de procesos.

- **SIGHUP**: La señal `kill sighup` (Hangup o Colgar, señal 1) se envía tradicionalmente a un proceso cuando se cierra su terminal de control. Se puede usar para indicar a los procesos daemon que recarguen sus archivos de configuración.
- **SIGINT**: La señal de Interrupción (señal 2) se envía cuando presionas `Ctrl-C`. Solicita al proceso que interrumpa su operación actual.
- **SIGSTOP**: Esta señal (señal 19) pausa un proceso sin terminarlo. El proceso puede reanudarse más tarde con la señal `SIGCONT`.

### Comprobar la Existencia del Proceso con kill -0

Un caso de uso especial es `linux kill -0`. Este comando en realidad no envía una señal, sino que comprueba si existe un proceso con el PID especificado y si tienes permiso para enviarle una señal.

```bash
kill -0 12445
```

Si el comando se ejecuta con éxito (código de salida 0), el proceso existe. Si falla, el proceso no existe o no tienes permisos.

## Exercise

Para aplicar lo aprendido, prueba este laboratorio práctico para reforzar tu comprensión de la gestión y terminación de procesos:

1.  **[Gestionar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderás habilidades esenciales para gestionar y monitorear procesos en un sistema Linux. Explorarás cómo interactuar con procesos en primer plano y segundo plano, inspeccionarlos con `ps`, monitorear recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Este laboratorio te ayudará a aplicar los conceptos de control y terminación de procesos en escenarios reales y a ganar confianza en la gestión de procesos de Linux.

## Quiz Question

¿Cuál es el nombre de la señal para el comando `kill` por defecto? Por favor, responda en inglés. Tenga en cuenta que la respuesta distingue entre mayúsculas y minúsculas.

## Quiz Answer

SIGTERM
