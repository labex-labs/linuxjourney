---
lesson_id: "job-control"
course_id: "processes"
lang: "es"
order_index: 11
title: "Control de trabajos"
description: "Aprende cómo un shell interactivo gestiona trabajos en primer plano, en segundo plano y detenidos."
meta_title: "Control de trabajos - Procesos"
meta_description: "Aprende a gestionar procesos en segundo plano con el control de trabajos de Linux y las órdenes jobs, bg, fg y kill."
meta_keywords: "control de trabajos Linux, procesos en segundo plano, orden jobs, orden bg, orden fg, orden kill"
---

Los shells interactivos utilizan el control de trabajos para coordinar tuberías dentro de una sesión de terminal. Un trabajo puede contener un solo proceso o una tubería completa, normalmente agrupados en un grupo de procesos para que la terminal y el shell puedan tratarlos como una unidad.

## Iniciar un trabajo en segundo plano

Añade `&` para iniciar una tubería de forma asíncrona:

```bash
$ sleep 1000 &
[1] 18420
```

El shell devuelve el prompt sin esperar a que termine el trabajo. Ejecutarlo en segundo plano no redirige automáticamente su salida, no lo desvincula de la terminal de control ni hace que sobreviva al cierre de la sesión. Redirige explícitamente la entrada y la salida cuando sea necesario, y utiliza un gestor de servicios, un planificador o un multiplexor de terminal para los trabajos que deban sobrevivir al shell interactivo.

Un trabajo en segundo plano que intenta leer de la terminal de control suele detenerse mediante `SIGTTIN` porque no pertenece al grupo de procesos en primer plano de la terminal.

:::single-choice{#job-control-ampersand-effect} ¿Qué solicita a un shell interactivo un `&` al final?

::option[Que garantice que el trabajo sobreviva al cierre de sesión y al reinicio del sistema.]{#job-control-survive-restart explanation="La ejecución en segundo plano por sí sola no proporciona supervisión duradera ni persistencia tras un reinicio."}
::option[Que ejecute la tubería como trabajo en segundo plano sin esperar antes de mostrar el siguiente prompt.]{#job-control-background-job .correct explanation="El shell inicia el trabajo de forma asíncrona y queda disponible para recibir más órdenes."}
::option[Que descarte la salida estándar y los errores del trabajo.]{#job-control-discard-output explanation="Si no se redirigen, un trabajo en segundo plano todavía puede escribir en la terminal."}
:::

## Listar los trabajos del shell

La orden interna `jobs` muestra los trabajos conocidos por el shell actual:

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

El número entre corchetes es un identificador de trabajo del shell, no un PID. El prefijo `%` forma una especificación de trabajo como `%1`. El marcador `+` identifica el trabajo actual que muchas órdenes seleccionan cuando no reciben un operando; `-` identifica el trabajo anterior.

Como la tabla de trabajos pertenece a un único shell, el shell de otra terminal no puede normalmente mostrar ni referirse a estos trabajos mediante sus propias órdenes internas `jobs`, `fg` o `bg`.

:::single-choice{#job-control-jobs-scope} ¿Qué muestra la orden interna `jobs`?

::option[Los trabajos seguidos por la sesión de shell actual.]{#job-control-jobs-current-shell .correct explanation="El shell interactivo que inició o adoptó los trabajos mantiene sus identificadores y estados."}
::option[Todos los procesos visibles en ese momento en el sistema.]{#job-control-jobs-all-processes explanation="La inspección de procesos de todo el sistema corresponde a herramientas como `ps`; la tabla de trabajos del shell es más limitada."}
::option[Únicamente los servicios iniciados durante el arranque del sistema.]{#job-control-jobs-boot-services explanation="Un gestor de servicios, no la tabla de trabajos del shell interactivo, suele supervisar los servicios de arranque."}
:::

## Detener y continuar un trabajo

Mientras un trabajo está en primer plano, al pulsar `Ctrl-Z` la terminal suele enviar `SIGTSTP` a su grupo de procesos en primer plano. El shell recupera el control después de que el trabajo se detenga:

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

Continúa el trabajo actual detenido en segundo plano con:

```bash
$ bg
```

`bg` envía una señal de continuación y deja el trabajo fuera del primer plano de la terminal. Solo resulta útil para un trabajo detenido; una orden que ya se ejecuta en segundo plano no necesita reanudarse.

:::single-choice{#job-control-bg-purpose} ¿Qué hace `bg %3` con el trabajo 3 detenido?

::option[Mueve sus archivos a un directorio llamado `bg`.]{#job-control-bg-files explanation="`bg` es una orden interna del shell para el control de trabajos y no mueve objetos del sistema de archivos."}
::option[Lo continúa como trabajo en segundo plano.]{#job-control-bg-continue .correct explanation="El shell reanuda el trabajo detenido seleccionado sin asignarle el primer plano de la terminal."}
::option[Lo termina mediante `SIGKILL`.]{#job-control-bg-kill explanation="La orden interna continúa el trabajo en vez de terminarlo."}
:::

## Mover un trabajo al primer plano

Utiliza `fg` con una especificación de trabajo para convertir un trabajo en el grupo de procesos en primer plano de la terminal y esperar a que termine:

```bash
$ fg %1
```

Sin un operando, `fg` suele seleccionar el trabajo actual marcado con `+`. Un trabajo detenido se continúa al pasar al primer plano.

:::single-choice{#job-control-fg-effect} ¿Qué hace `fg %1`?

::option[Asigna el trabajo 1 al primer plano de la terminal y espera a que termine.]{#job-control-fg-foreground .correct explanation="El shell lleva al primer plano el trabajo seleccionado para que pueda interactuar con la terminal."}
::option[Convierte el trabajo 1 en el PID 1.]{#job-control-fg-pid-one explanation="Un identificador de trabajo del shell no sustituye ni modifica los identificadores de proceso."}
::option[Inicia una segunda copia del trabajo 1 en segundo plano.]{#job-control-fg-copy explanation="`fg` actúa sobre el trabajo existente en vez de crear un duplicado."}
:::

## Enviar señales a un trabajo

Los shells permiten que `kill` acepte una especificación de trabajo:

```bash
$ kill -TERM %1
```

Normalmente, esto envía la señal al grupo de procesos del trabajo y no solo a un miembro de la tubería. Examina primero el trabajo seleccionado y utiliza `SIGTERM` antes de plantearte una medida forzosa. Las especificaciones de trabajo son sintaxis del shell; los scripts y las herramientas externas suelen trabajar con PID o identificadores de grupo de procesos verificados.

:::single-choice{#job-control-job-specification} ¿Qué operando se refiere al trabajo 1 del shell en vez de al proceso con PID 1?

::option[`1`]{#job-control-plain-one explanation="Un operando numérico sin prefijo para `kill` suele interpretarse como un PID."}
::option[`#1`]{#job-control-hash-one explanation="El prefijo de almohadilla no es la sintaxis presentada para un identificador de trabajo del shell."}
::option[`%1`]{#job-control-percent-one .correct explanation="El prefijo de porcentaje identifica una especificación de trabajo del shell."}
:::

Practica estas operaciones con órdenes inofensivas como `sleep` en el laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864).

## Resumen

Ahora puedes mover deliberadamente trabajos entre los estados controlados por el shell.

1. Utiliza `&` para iniciar un trabajo en segundo plano sin desvincularlo automáticamente.
2. Utiliza `jobs` para examinar la tabla de trabajos del shell actual.
3. Detén un trabajo con `Ctrl-Z` y continúalo en segundo plano con `bg`.
4. Devuelve un trabajo seleccionado a la terminal con `fg`.
5. Especifica los trabajos del shell mediante `%JOB_ID` al enviar señales.
