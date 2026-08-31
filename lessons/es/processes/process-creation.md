---
lesson_id: "process-creation"
course_id: "processes"
lang: "es"
order_index: 4
title: "Creación de procesos"
description: "Aprende cómo fork, exec, los PID y las relaciones de parentesco intervienen en la creación de procesos de Linux."
meta_title: "Creación de procesos - Procesos"
meta_description: "Descubre la creación de procesos en Linux mediante fork y execve, las relaciones PID y PPID y las responsabilidades de PID 1."
meta_keywords: "creación de procesos Linux, fork, execve, PID, PPID, proceso init, procesos Linux"
---

Los procesos de Linux forman relaciones entre padres e hijos. Un shell suele iniciar una orden externa creando un proceso hijo y haciendo que este ejecute el programa solicitado. La explicación clásica separa este trabajo en operaciones `fork` y `exec`.

## Crear un hijo con `fork`

La llamada al sistema `fork()` crea un proceso hijo basado en el proceso que la invoca. Padre e hijo continúan desde el punto de retorno de `fork`, pero reciben valores de retorno distintos y tienen PID diferentes.

El hijo obtiene un estado de proceso lógicamente independiente. Linux puede compartir inicialmente páginas de memoria física mediante copia en escritura y copiar una página únicamente cuando uno de los procesos la modifica. Los descriptores de archivos abiertos se heredan y se refieren a las mismas descripciones de archivos abiertas subyacentes, por lo que detalles como los desplazamientos pueden seguir compartidos.

:::single-choice{#process-creation-fork-result}
¿Qué crea un `fork()` correcto?

::option[Únicamente un programa de reemplazo dentro del mismo proceso.]{#process-creation-fork-replacement explanation="Sustituir la imagen del programa actual es la función de una operación `exec`."}
::option[Un proceso hijo con un PID nuevo.]{#process-creation-fork-child .correct explanation="`fork()` establece un proceso hijo independiente y una relación padre-hijo."}
::option[Una copia permanente e inmediata de todas las páginas de memoria física.]{#process-creation-fork-full-copy explanation="Linux suele usar copia en escritura en vez de duplicar inmediatamente todas las páginas físicas."}
:::

## Sustituir un programa con `execve`

Una llamada `execve()` carga un programa nuevo en el proceso que la invoca. Si tiene éxito, sustituye la imagen del proceso y no vuelve al programa anterior. El PID permanece igual porque `execve()` no crea un proceso nuevo.

Por tanto, muchas órdenes del shell siguen un patrón fork-exec:

1. El shell crea un hijo.
2. El hijo prepara redirecciones y otro estado de ejecución.
3. El hijo ejecuta el programa solicitado.
4. El shell espera o continúa, según se ejecute en primer o segundo plano.

Las bibliotecas y aplicaciones pueden ofrecer interfaces de nivel superior como `posix_spawn()`, y Linux tiene primitivas adicionales como `clone()`. El conocido modelo fork-exec sigue siendo útil sin ser la única interfaz posible.

:::single-choice{#process-creation-exec-pid}
¿Qué ocurre con el PID de un proceso después de un `execve()` correcto?

::option[Pasa a ser idéntico al PID del padre.]{#process-creation-exec-parent-pid explanation="Padre e hijo conservan identificadores de proceso distintos."}
::option[Permanece igual mientras se sustituye la imagen del programa.]{#process-creation-exec-same-pid .correct explanation="`execve()` transforma el proceso que la invoca en vez de crear otro."}
::option[Se elimina antes de que comience el programa nuevo.]{#process-creation-exec-pid-removed explanation="El proceso existente continúa bajo su PID con código, datos, pila y otro estado de programa nuevos."}
:::

## Consultar los ID de padres e hijos

`PID` identifica el proceso, mientras que `PPID` identifica a su padre. Solicita esos campos explícitamente:

```bash
$ ps -o pid,ppid,stat,cmd
```

Si un shell inicia `ps`, el PID del shell suele aparecer como `PPID` de ese proceso `ps`. El momento importa: los procesos de corta duración pueden terminar antes de que otra observación consiga capturarlos.

:::single-choice{#process-creation-ppid}
¿Qué representa `PPID` en un listado de procesos?

::option[El PID anterior asignado previamente al proceso.]{#process-creation-previous-pid explanation="Los PID pueden reutilizarse, pero `PPID` no registra el historial de identificadores."}
::option[El identificador de prioridad de planificación del proceso.]{#process-creation-priority-id explanation="La prioridad de planificación se representa mediante otros campos, como prioridad o valor nice."}
::option[El ID de proceso del proceso padre.]{#process-creation-parent-pid .correct explanation="PPID registra la relación actual del proceso con su padre."}
:::

## PID 1 y reasignación de padre

El kernel inicia el primer proceso del espacio de usuario con PID 1. Según el sistema, puede ser `systemd`, otra implementación de init o un init pequeño dentro de un contenedor o espacio de nombres PID. PID 1 inicia y supervisa partes del entorno de espacio de usuario y tiene responsabilidades especiales sobre señales y recogida de procesos huérfanos.

Cuando un padre termina antes que su hijo, este se reasigna a un subreaper apropiado o al proceso init de su espacio de nombres PID. No necesita terminar simplemente porque haya finalizado su padre original.

:::single-choice{#process-creation-pid-one}
¿Qué afirmación sobre PID 1 es correcta?

::option[Siempre debe ser un programa cuyo ejecutable se llame exactamente `init`.]{#process-creation-pid-one-name explanation="La implementación puede ser `systemd`, otro init o un programa específico de un contenedor."}
::option[Es el padre que creó directamente todos los procesos que se ejecutan actualmente.]{#process-creation-pid-one-direct explanation="La mayoría de los procesos se crean a través de muchas generaciones de padres intermedios."}
::option[Es el primer proceso de su espacio de nombres PID y tiene responsabilidades de tipo init.]{#process-creation-pid-one-init .correct explanation="PID 1 sustenta la supervisión y recogida de procesos del espacio de usuario dentro de un espacio de nombres PID."}
:::

El laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) permite observar los ID de padres e hijos al ejecutar órdenes en primer y segundo plano.

## Resumen

Ahora puedes seguir la secuencia clásica de creación de procesos de Linux.

1. Usa `fork()` para crear un hijo con un PID distinto.
2. Usa `execve()` para sustituir la imagen de un proceso sin cambiar su PID.
3. Lee PID y PPID para identificar relaciones entre padres e hijos.
4. Reconoce PID 1 y los subreapers como destinos de hijos reasignados.
