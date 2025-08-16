---
title: "Control de Trabajos"
description: "Aprenda el control de trabajos de Linux para gestionar procesos en segundo plano. Comprenda los comandos 'jobs', 'bg', 'fg' y 'kill' para un uso eficiente del shell. ¡Comience su viaje en Linux!"
keywords: "control de trabajos de Linux, procesos en segundo plano, comando jobs, comando bg, comando fg, comando kill, tutorial de Linux, Linux para principiantes"
---

## Lesson Content

Supongamos que está trabajando en una sola ventana de terminal y está ejecutando un comando que tarda una eternidad. No puede interactuar con el shell hasta que se complete. Sin embargo, queremos seguir trabajando en nuestras máquinas, por lo que necesitamos tener ese shell abierto. Afortunadamente, podemos controlar cómo se ejecutan nuestros procesos con los trabajos:

### Enviando un trabajo al segundo plano

Agregar un ampersand (`&`) al comando lo ejecutará en segundo plano para que pueda seguir usando su shell. Veamos un ejemplo:

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Ver todos los trabajos en segundo plano

Ahora puede ver los trabajos que acaba de enviar al segundo plano.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

Esto le mostrará el ID del trabajo en la primera columna, luego el estado y el comando que se ejecutó. El **+** junto al ID del trabajo significa que es el trabajo en segundo plano más reciente que se inició. El trabajo con el **-** es el segundo comando más reciente.

### Enviando un trabajo al segundo plano en un trabajo existente

Si ya ejecutó un trabajo y desea enviarlo al segundo plano, no tiene que terminarlo y comenzar de nuevo. Primero, suspenda el trabajo con Ctrl-Z, luego ejecute el comando **bg** para enviarlo al segundo plano.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &

pete@icebox ~ $ jobs

[1]    Running     sleep 1000 &
[2]    Running     sleep 1001 &
[3]-   Running     sleep 1002 &
[4]+   Running     sleep 1003 &
```

### Moviendo un trabajo del segundo plano al primer plano

Para sacar un trabajo del segundo plano, simplemente especifique el ID del trabajo que desea. Si ejecuta `fg` sin ninguna opción, traerá de vuelta el trabajo en segundo plano más reciente (el trabajo con el signo + al lado).

```bash
fg %1
```

### Matar trabajos en segundo plano

De manera similar a mover trabajos fuera del segundo plano, puede usar la misma forma para matar los procesos usando su ID de trabajo.

```bash
kill %1
```

## Exercise

Mueva algunos trabajos entre el segundo plano y el primer plano.

## Quiz Question

¿Qué comando se utiliza para listar los trabajos en segundo plano?

## Quiz Answer

jobs
