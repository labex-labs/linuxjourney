---
index: 4
lang: "es"
title: "Creación de Procesos"
meta_title: "Creación de Procesos - Procesos"
meta_description: "Explore los fundamentos de la creación de procesos en Linux. Esta guía cubre las llamadas al sistema fork y execve, las relaciones padre/hijo (PID y PPID) y el papel del proceso init. Aprenda a crear un proceso en Linux y comprenda los conceptos centrales de la creación de procesos en el sistema operativo."
meta_keywords: "creación de procesos en linux, creación de procesos linux, crear un proceso en linux, creación de procesos en sistema operativo, creación de procesos, fork, execve, PID, PPID, proceso init, procesos Linux"
---

## Lesson Content

Esta lección explora los conceptos fundamentales de cómo se inician nuevos procesos en un sistema Linux. Comprender este mecanismo proporciona una visión del funcionamiento interno del sistema operativo.

### El Modelo Fork y Exec

El mecanismo principal para la **creación de procesos en Linux** implica que un proceso existente se clona a sí mismo utilizando la llamada al sistema `fork`. La llamada `fork` crea un proceso hijo casi idéntico. Este nuevo proceso hijo recibe su propio Identificador de Proceso (PID) único, mientras que el proceso original se convierte en su padre, identificado por un Identificador de Proceso Padre (**PPID**).

Después de bifurcarse (forking), el proceso hijo puede continuar ejecutando el mismo programa que su padre o, más comúnmente, usar la llamada al sistema `execve` para cargar y ejecutar un nuevo programa. La llamada `execve` reemplaza efectivamente el espacio de memoria del proceso con el del nuevo programa, permitiendo que comience una tarea diferente. Este modelo de dos pasos "fork-exec" es una piedra angular de cómo se **crea un proceso en Linux**.

### Observando las Relaciones Padre-Hijo

Podemos observar esta relación padre-hijo en acción usando el comando `ps`:

```bash
ps l
```

La opción `l` proporciona una vista de "formato largo", mostrando más detalles sobre los procesos en ejecución. Verá una columna etiquetada como **PPID**, que significa Parent Process ID (Identificador de Proceso Padre). Observe el proceso de su shell actual (por ejemplo, `bash`). Cuando ejecuta el comando `ps l`, notará que el **PID** de su proceso shell coincide con el **PPID** del proceso `ps l`. Esto se debe a que su shell se bifurcó para crear el proceso `ps`.

### El Proceso Init

Si cada proceso es hijo de otro, debe haber un ancestro original. Este es el proceso `init`. Cuando el sistema arranca, el kernel crea `init` como el primer proceso de espacio de usuario, asignándole un PID de 1. El proceso `init` es el padre definitivo de todos los demás procesos y se ejecuta con privilegios de root para administrar el sistema. No se puede terminar hasta que el sistema se apague y es responsable de iniciar muchos de los servicios que mantienen el sistema en funcionamiento.

## Exercise

¡La práctica hace al maestro! Aquí hay un laboratorio práctico para reforzar su comprensión de los procesos de Linux y su gestión:

- **[Gestionar y Supervisar Procesos de Linux](https://labex.io/es/labs/comptia-manage-and-monitor-linux-processes-590864)** - En este laboratorio, aprenderá habilidades esenciales para gestionar y supervisar procesos en un sistema Linux. Explorará cómo interactuar con procesos en primer plano y en segundo plano, inspeccionarlos con `ps`, supervisar recursos con `top`, ajustar la prioridad con `renice` y terminarlos con `kill`.

Este laboratorio le ayudará a aplicar los conceptos de identificadores de proceso, identificadores de proceso padre y supervisión de procesos en un escenario real y a ganar confianza con la gestión de procesos.

## Quiz Question

What system call creates a new process? (Please answer in a single lowercase English word.)

## Quiz Answer

fork
