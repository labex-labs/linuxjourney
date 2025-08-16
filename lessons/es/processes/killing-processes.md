---
lang: "es"
title: "kill (Terminar)"
description: "Aprende a usar el comando 'kill' de Linux para terminar procesos. Comprende SIGTERM, SIGKILL y otras señales para la gestión de procesos. ¡Empieza a aprender ahora!"
keywords: "comando kill, procesos Linux, SIGTERM, SIGKILL, tutorial Linux, principiante, gestión de procesos, guía Linux"
---

## Lesson Content

Puedes enviar señales que terminan procesos; un comando así se llama apropiadamente el comando `kill`.

```bash
kill 12445
```

El `12445` es el PID del proceso que quieres terminar. Por defecto, envía una señal `TERM`. La señal `SIGTERM` se envía a un proceso para solicitar su terminación, permitiéndole liberar limpiamente sus recursos y guardar su estado.

También puedes especificar una señal con el comando `kill`:

```bash
kill -9 12445
```

Esto ejecutará la señal `SIGKILL` y terminará el proceso.

### Differences between SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP?

Todas estas señales suenan razonablemente similares, pero tienen sus diferencias.

- SIGHUP - Hangup, se envía a un proceso cuando se cierra el terminal de control. Por ejemplo, si cerraste una ventana de terminal que tenía un proceso ejecutándose en ella, recibirías una señal `SIGHUP`. Así que, básicamente, te han colgado.
- SIGINT - Es una señal de interrupción, por lo que puedes usar Ctrl-C, y el sistema intentará terminar el proceso de forma elegante.
- SIGTERM - Termina el proceso, pero le permite hacer alguna limpieza primero.
- SIGKILL - Termina el proceso, mátalo con fuego, no hace ninguna limpieza.
- SIGSTOP - Detiene/suspende un proceso.

## Exercise

Kill some processes using different signals.

## Quiz Question

¿Cuál es el nombre de la señal para el comando `kill` por defecto?

## Quiz Answer

SIGTERM
