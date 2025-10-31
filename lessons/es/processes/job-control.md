---
index: 11
lang: "es"
title: "Control de Trabajos"
meta_title: "Control de Trabajos - Procesos"
meta_description: "Explore nuestro tutorial de Linux sobre control de trabajos para gestionar eficazmente los procesos en segundo plano. Aprenda a usar los comandos jobs, bg, fg y kill para una potente multitarea en la shell."
meta_keywords: "control de trabajos Linux, procesos en segundo plano, comando jobs, comando bg, comando fg, comando kill, tutorial Linux, Linux para principiantes"
---

## Lesson Content

En Linux, a menudo te encuentras con comandos que tardan mucho en completarse. En lugar de esperar y dejar tu terminal inutilizable, puedes usar el **control de trabajos de Linux** para administrar estas tareas. Esta potente función te permite ejecutar y gestionar múltiples **procesos en segundo plano** dentro de una sola sesión de shell, mejorando significativamente tu flujo de trabajo.

### Ejecutar un Comando en Segundo Plano

Para iniciar un proceso directamente en segundo plano, simplemente añade un ampersand (`&`) al final de tu comando. Esto devuelve inmediatamente el prompt de tu shell, permitiéndote continuar trabajando mientras el comando se ejecuta.

```bash
sleep 1000 &
sleep 1001 &
sleep 1002 &
```

### Listar Trabajos en Segundo Plano

Puedes ver todos los trabajos que se ejecutan en segundo plano usando el comando `jobs`.

```bash
$ jobs

[1]    Running     sleep 1000 &
[2]-   Running     sleep 1001 &
[3]+   Running     sleep 1002 &
```

La salida proporciona el ID del trabajo en la primera columna, su estado y el comando original. El símbolo `+` indica el trabajo en segundo plano iniciado más recientemente, mientras que el símbolo `-` marca el segundo más reciente.

### Administrar Procesos Activos

¿Qué pasa si un comando ya se está ejecutando en primer plano y decides que necesitas recuperar tu terminal? No necesitas detenerlo. Primero, suspende el proceso en ejecución presionando `Ctrl-Z`. Luego, usa el comando `bg` para enviar ese trabajo suspendido al segundo plano.

```bash
pete@icebox ~ $ sleep 1003
^Z
[4]+    Stopped     sleep 1003

pete@icebox ~ $ bg
[4]+    sleep 1003 &
```

Ahora, el proceso `sleep 1003` se está ejecutando como un trabajo en segundo plano, y puedes verificarlo con el comando `jobs`.

### Traer un Trabajo al Primer Plano

Para devolver un proceso en segundo plano al primer plano, usa el comando `fg`. Puedes especificar un trabajo concreto por su ID (ejemplo: `fg %1`). Si ejecutas el comando `fg` sin argumentos, traerá al primer plano el trabajo en segundo plano más reciente (el marcado con `+`).

```bash
fg %1
```

### Terminar Trabajos en Segundo Plano

Si necesitas detener un proceso en segundo plano, puedes usar el comando `kill`. Similar al comando `fg`, haces referencia al trabajo usando su ID precedido por un signo de porcentaje (`%`). Esta es una función clave del control de trabajos de Linux.

```bash
kill %1
```

Dominar estos comandos es esencial para cualquier usuario principiante de Linux que busque realizar múltiples tareas de manera eficiente en el shell.

## Exercise

Para poner en práctica tus conocimientos sobre el control de trabajos de Linux, prueba este laboratorio práctico. Te ayudará a solidificar tu comprensión de la gestión de procesos en primer plano y en segundo plano.

1. **[Administrar y Monitorear Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - Practica la interacción con procesos en primer plano y en segundo plano, monitorea recursos y termina procesos, abordando directamente el escenario de comandos de larga ejecución.

## Quiz Question

What command is used to list background jobs? (Please answer in English, using only lowercase letters.)

## Quiz Answer

jobs
