---
lesson_id: "process-details"
course_id: "processes"
lang: "es"
order_index: 3
title: "Detalles de los procesos"
description: "Aprende qué estado y recursos distinguen un proceso en ejecución de un programa almacenado en disco."
meta_title: "Detalles de los procesos - Procesos"
meta_description: "Descubre qué es un proceso de Linux, qué estado mantiene el kernel y cómo se gestionan la CPU, la memoria y la finalización."
meta_keywords: "proceso Linux, detalles de procesos, kernel, gestión de procesos, recursos del sistema, CPU, memoria, tutorial Linux"
---

Un programa es código ejecutable y datos almacenados en un archivo. Un proceso es un contexto de ejecución activo: incluye código mapeado, memoria, credenciales, descriptores de archivos abiertos, estado de señales, información de planificación y uno o más hilos. El mismo programa puede tener muchas instancias de procesos independientes.

## Instancias de programas y PID

Por ejemplo, inicia `cat` sin operandos en dos terminales. Cada instancia espera una entrada y tiene su propio ID de proceso:

```bash
$ pgrep -a cat
18420 cat
18457 cat
```

Ambos procesos ejecutan el mismo programa, pero pueden tener flujos de entrada, contenidos de memoria, credenciales, directorios de trabajo y ciclos de vida distintos. Un PID identifica un proceso activo cada vez y puede reutilizarse después de que ese proceso termine.

:::single-choice{#process-details-program-versus-process}
¿Qué distingue dos instancias en ejecución del mismo programa?

::option[El archivo ejecutable debe copiarse una vez por instancia.]{#process-details-copied-executable explanation="Varios procesos pueden mapear y compartir las mismas páginas de código del archivo ejecutable sin duplicar el archivo."}
::option[Únicamente una instancia puede tener memoria o archivos abiertos.]{#process-details-one-instance-resources explanation="Cada proceso puede tener sus propios mapas de memoria y tabla de descriptores de archivos."}
::option[Cada instancia tiene su propio contexto de proceso y PID.]{#process-details-independent-context .correct explanation="Las ejecuciones separadas reciben un estado de proceso activo distinto, aunque su código ejecutable proceda del mismo archivo."}
:::

## Estado que mantiene el kernel

El kernel conserva la información necesaria para planificar y controlar cada proceso, incluida:

- identificadores del proceso y de su padre;
- credenciales de usuario y grupo;
- mapas de memoria virtual;
- descriptores de archivos abiertos y directorio actual;
- disposiciones de señales y señales pendientes;
- política de planificación, prioridad y estado de ejecución;
- datos contables como el tiempo de CPU.

Algunos recursos subyacentes pueden compartirse. Los procesos relacionados pueden compartir memoria mapeada, y los hilos de un proceso comparten un espacio de direcciones y muchos recursos de todo el proceso. Por tanto, un proceso proporciona límites de aislamiento sin implicar que cada byte u objeto del kernel sea físicamente privado.

:::single-choice{#process-details-kernel-state}
¿Qué componente mantiene el estado de planificación y credenciales de los procesos de Linux?

::option[El kernel.]{#process-details-kernel .correct explanation="El kernel mantiene el estado de los procesos y aplica las reglas de planificación, memoria, señales y control de acceso."}
::option[El directorio del archivo ejecutable.]{#process-details-directory explanation="Un directorio almacena correspondencias de nombres con inodos y no planifica procesos en ejecución."}
::option[Únicamente el emulador de terminal del usuario.]{#process-details-terminal explanation="Una terminal puede interactuar con procesos, pero su gestión sigue siendo responsabilidad del kernel."}
:::

## Planificación de CPU y memoria

Los hilos ejecutables compiten por tiempo de CPU. El planificador del kernel elige qué hilo se ejecuta en qué CPU según la clase de planificación, prioridad, afinidad de CPU, carga y política. Esto no promete que todos los procesos reciban una parte igual.

Cada proceso suele ver un espacio de direcciones virtual. El kernel y el hardware asocian direcciones virtuales con memoria física u otro almacenamiento de respaldo, aplican protecciones y pueden compartir páginas cuando corresponde. Por tanto, una cifra de memoria de `ps` o `top` no representa automáticamente la cantidad de RAM física exclusiva atribuible a ese proceso.

:::single-choice{#process-details-scheduler-role}
¿Qué selecciona el planificador de Linux?

::option[Qué hilo ejecutable se ejecuta en una CPU disponible.]{#process-details-runnable-thread .correct explanation="La política de planificación elige entre contextos de ejecución preparados y asigna tiempo de CPU."}
::option[Qué propietario de archivo se registra al formatear un disco.]{#process-details-format-owner explanation="La propiedad del sistema de archivos no está relacionada con la planificación de CPU."}
::option[Qué línea de órdenes puede escribir un usuario.]{#process-details-command-entry explanation="El planificador gestiona el tiempo de ejecución, no la sintaxis interactiva de las órdenes."}
:::

## Salida del proceso y liberación de recursos

Cuando un proceso termina, el kernel libera la mayoría de sus recursos privados, cierra los descriptores restantes y registra información de terminación para su padre. Un pequeño registro en la tabla de procesos puede permanecer como zombi hasta que el padre recupere el estado de salida. Esto significa que «el proceso ha terminado de ejecutarse» y «todo rastro ha desaparecido de la tabla» no siempre ocurren al mismo tiempo.

:::single-choice{#process-details-exit-status}
¿Por qué puede un proceso terminado permanecer brevemente como zombi?

::option[Sigue ejecutando instrucciones con toda su memoria asignada.]{#process-details-zombie-running explanation="Un zombi ha terminado de ejecutarse y ya no conserva un espacio de direcciones normal en ejecución."}
::option[Su padre todavía no ha recogido el estado de terminación registrado.]{#process-details-parent-wait .correct explanation="El kernel conserva información mínima de salida hasta que el padre realiza una operación de espera."}
::option[El kernel ha bloqueado permanentemente su archivo ejecutable.]{#process-details-zombie-file-lock explanation="El estado zombi se refiere a la contabilidad de salida entre padre e hijo, no a un bloqueo permanente del ejecutable."}
:::

Usa el laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) para iniciar varias instancias y comparar sus PID y estados. El laboratorio [Orden top de Linux](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500) ofrece una vista cambiante de métricas de planificación y recursos.

## Resumen

Ahora puedes describir un proceso como algo más que un archivo de programa.

1. Distingue el código ejecutable almacenado de una instancia de proceso activa.
2. Identifica el estado y los recursos mantenidos por el kernel.
3. Relaciona la planificación con hilos ejecutables, no con repartos iguales.
4. Reconoce que el estado de salida puede permanecer hasta que el padre lo recoja.
