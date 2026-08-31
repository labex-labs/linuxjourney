---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "es"
order_index: 3
title: "Hilos de proceso"
description: "Aprende cómo los hilos de Linux comparten recursos del proceso y cómo examinarlos con ps."
meta_title: "Hilos de proceso - Utilización de procesos"
meta_description: "Aprende la diferencia entre procesos e hilos de Linux y cómo mostrar hilos con la orden ps."
meta_keywords: "hilos Linux, hilos de proceso, ps mostrar hilos, procesos multihilo, gestión de procesos"
---

Un hilo es un flujo de ejecución planificado dentro de un proceso. Todo proceso en ejecución tiene al menos un hilo, y un proceso multihilo tiene varios flujos que pueden avanzar simultáneamente.

## Procesos e hilos

Los hilos de un proceso comparten recursos como el espacio de direcciones virtual y los descriptores de archivo abiertos. Cada hilo conserva su propio estado de ejecución, incluidos los registros y una pila. Compartir recursos hace eficiente la comunicación, pero también significa que un cambio sin sincronizar de un hilo puede afectar a los demás.

Los procesos independientes suelen tener espacios de direcciones distintos y se comunican mediante mecanismos explícitos entre procesos. Ninguno de los diseños es automáticamente más rápido o seguro; la carga de trabajo y la implementación determinan las ventajas e inconvenientes.

:::single-choice{#threads-shared-resource}
¿Qué recurso comparten normalmente los hilos de un mismo proceso?

::option[El espacio de direcciones virtual del proceso.]{#threads-shared-address-space .correct explanation="Los hilos pueden acceder a la misma memoria del proceso, sujetos a la sincronización del programa."}
::option[Una instalación distinta del kernel para cada hilo.]{#threads-separate-kernel explanation="Todos los hilos utilizan el kernel del sistema en ejecución."}
::option[Una raíz del sistema de archivos distinta para cada hilo.]{#threads-different-root explanation="Los hilos suelen compartir el contexto del sistema de archivos del proceso en vez de recibir raíces independientes."}
:::

## Identificadores de hilos

Linux representa cada hilo como una tarea planificable con su propio identificador de hilo. El identificador del líder del grupo de hilos suele presentarse como identificador de proceso, mientras que todos los miembros comparten un identificador de grupo de hilos. Las herramientas utilizan etiquetas como `PID`, `TID`, `LWP` y `SPID`; consulta las definiciones de campos de la herramienta en vez de suponer que todas significan lo mismo.

:::single-choice{#threads-own-scheduling-state}
¿Qué mantiene de forma independiente cada hilo?

::option[La tabla completa de archivos abiertos del proceso.]{#threads-open-files-shared explanation="Los hilos de un proceso suelen compartir los descriptores de archivo abiertos."}
::option[La base de datos de usuarios de todo el sistema.]{#threads-user-database explanation="Las bases de datos de cuentas no son estado privado de un hilo."}
::option[Su estado de ejecución y su pila.]{#threads-stack-state .correct explanation="Un hilo necesita su propio contexto de ejecución aunque comparta recursos del proceso."}
:::

## Mostrar hilos con ps

Utiliza campos de salida explícitos para evitar diseños predeterminados ambiguos:

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

En `ps` de procps, `-L` muestra hilos y `-e` selecciona todos los procesos. `pid` identifica el grupo de hilos, `tid` identifica un hilo concreto, `psr` muestra la CPU en la que se ejecutó por última vez y `stat` comunica el estado. Para examinar un proceso:

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

Los listados de hilos son instantáneas. Un hilo puede terminar o cambiar de estado inmediatamente después.

:::single-choice{#threads-ps-one-process}
¿Qué orden muestra los hilos pertenecientes al PID 1234 con campos explícitos?

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="Esta salida no solicita filas para cada hilo."}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="La opción `-L` solicita filas de hilos para el proceso seleccionado."}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="Esta orden selecciona procesos de todo el sistema sin identificadores de hilos."}
:::

## Interpretar la actividad de los hilos

Una actividad de CPU alta en un hilo puede quedar oculta por el promedio de todo el proceso. Combina muestras de CPU a nivel de hilo con registros de la aplicación, trazas de pilas y herramientas de perfilado. No conectes depuradores ni envíes señales a tareas de producción sin comprender sus efectos sobre las pausas, los permisos y el servicio.

:::single-choice{#threads-snapshot-limit}
¿Por qué no debe tratarse un listado de hilos de `ps` como estado permanente?

::option[Porque `ps` crea un hilo de sustitución por cada fila.]{#threads-ps-creates explanation="La orden observa tareas; no clona cada una de las que muestra."}
::option[Porque los identificadores de hilos son idénticos en todos los equipos Linux.]{#threads-identical-ids explanation="Los identificadores se asignan dentro de un sistema en ejecución y no son universales."}
::option[Porque los hilos pueden cambiar de estado o terminar después de la instantánea.]{#threads-change-after-snapshot .correct explanation="La inspección de procesos observa un instante de un sistema que cambia continuamente."}
:::

## Resumen

Ahora puedes distinguir los recursos del proceso del estado de ejecución de cada hilo.

1. Reconoce que todo proceso tiene al menos un hilo.
2. Identifica los recursos compartidos por los hilos de un proceso.
3. Muestra identificadores explícitos de procesos e hilos con `ps -L`.
4. Trata la salida de hilos como una instantánea y relaciónala con otras pruebas.
