---
lesson_id: "process-signals"
course_id: "processes"
lang: "es"
order_index: 6
title: "Señales"
description: "Aprende cómo Linux genera, bloquea, entrega y trata señales para controlar procesos y notificar eventos."
meta_title: "Señales - Procesos"
meta_description: "Descubre cómo funcionan las señales de Linux, incluidas SIGINT, SIGTERM y SIGKILL, sus disposiciones, bloqueo y entrega."
meta_keywords: "señales Linux, señales de procesos Linux, SIGKILL, SIGTERM, SIGINT, gestión de procesos, tutorial Linux"
---

Una señal es una notificación asíncrona entregada a un proceso o a un hilo concreto. Las señales comunican eventos y solicitan acciones, pero transportan información limitada frente a mecanismos de comunicación entre procesos orientados a datos.

## Origen de las señales

Las señales pueden proceder de varios lugares:

- Una terminal puede generar `SIGINT` para `Ctrl-C` o `SIGTSTP` para `Ctrl-Z` y dirigirla al grupo de procesos en primer plano.
- El kernel puede generar una señal síncrona como `SIGSEGV` cuando un hilo realiza una referencia de memoria no válida.
- Un proceso puede enviar una señal autorizada a otro proceso o grupo de procesos.
- Los temporizadores, los cambios de estado de hijos y las desconexiones de terminal pueden generar otras señales.

El emisor debe tener los permisos apropiados, normalmente basados en credenciales o capacidades. Por tanto, las señales son una interfaz de control mediada por el kernel, no mensajes sin restricciones entre usuarios arbitrarios.

:::single-choice{#process-signals-ctrl-c}
¿Qué señal genera normalmente una terminal para `Ctrl-C`?

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="`SIGTSTP` suele estar asociada al carácter de suspensión de la terminal, como `Ctrl-Z`."}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="`SIGCONT` reanuda un proceso detenido en vez de representar una interrupción del teclado."}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="El carácter de interrupción de la terminal suele generar `SIGINT` para el grupo de procesos en primer plano."}
:::

## Disposiciones y acciones predeterminadas

La mayoría de las señales tienen una disposición para todo el proceso que selecciona una de tres respuestas:

- realizar la acción predeterminada definida para la señal;
- ignorar la señal;
- invocar un manejador instalado por el usuario.

Las acciones predeterminadas varían: una señal puede terminar, terminar y crear un volcado de memoria, detener, continuar o ignorarse. Capturar `SIGTERM` puede permitir que un programa inicie un cierre ordenado, pero el manejador debe seguir reglas estrictas de seguridad asíncrona y el programa aún puede retrasar o rechazar la salida.

Los nombres de las señales son más portables y legibles que los números. Aunque arquitecturas habituales de Linux usan el 15 para `SIGTERM`, no supongas que todos los números, salvo los garantizados por la norma correspondiente, son idénticos en todas partes. Usa `kill -l` para consultar la correspondencia local.

:::single-choice{#process-signals-term-behavior}
¿Por qué puede un proceso responder de forma ordenada a `SIGTERM`?

::option[Puede instalar un manejador para esa señal.]{#process-signals-term-handler .correct explanation="A diferencia de `SIGKILL`, `SIGTERM` puede capturarse para que un programa inicie su propia lógica de cierre."}
::option[El kernel guarda siempre todos los documentos abiertos automáticamente.]{#process-signals-term-kernel-save explanation="La limpieza de una aplicación depende de su código; el kernel no comprende ni guarda estados arbitrarios de documentos."}
::option[`SIGTERM` no puede causar la terminación de forma predeterminada.]{#process-signals-term-no-default explanation="Su acción predeterminada es terminar cuando el proceso no ha cambiado la disposición."}
:::

## Señales bloqueadas y pendientes

Los hilos tienen máscaras de señales que pueden bloquear temporalmente la entrega de determinadas señales. Una señal generada y bloqueada permanece pendiente hasta que pueda entregarse, según las reglas de las señales estándar y en tiempo real. Las señales estándar del mismo tipo pueden fusionarse en vez de ponerse en cola una vez por aparición.

En un proceso multihilo, una señal dirigida al proceso puede entregarse a un hilo apto que no la bloquee; una señal dirigida a un hilo apunta al hilo especificado. Por tanto, un diseño correcto requiere más que comprobar si «el proceso la bloqueó».

:::single-choice{#process-signals-blocked-state}
¿Qué ocurre normalmente cuando se genera una señal bloqueable mientras su destino la bloquea?

::option[Permanece pendiente hasta que la entrega sea posible.]{#process-signals-pending .correct explanation="El bloqueo aplaza el tratamiento; la señal pendiente puede entregarse después de desbloquearla."}
::option[Se convierte automáticamente en `SIGKILL`.]{#process-signals-convert-kill explanation="El kernel no eleva una señal ordinaria bloqueada a una señal que no pueda capturarse."}
::option[Cambia el ID de usuario del proceso de destino.]{#process-signals-change-uid explanation="Las máscaras de señales afectan a la entrega y no modifican las credenciales del proceso."}
:::

## Señales que no pueden tratarse

`SIGKILL` termina un proceso y `SIGSTOP` lo detiene. Ninguna puede capturarse, ignorarse ni bloquearse. Esto garantiza que el kernel conserve el control final, pero también significa que `SIGKILL` no ofrece ninguna oportunidad para la limpieza de la aplicación.

Incluso `SIGKILL` puede no hacer que una tarea desaparezca inmediatamente desde la perspectiva de un observador. Una tarea puede estar esperando en una operación del kernel no interrumpible y, después de terminar, su padre todavía debe recoger su estado.

:::single-choice{#process-signals-uncatchable-pair}
¿Qué pareja no puede capturarse, ignorarse ni bloquearse?

::option[`SIGKILL` y `SIGSTOP`]{#process-signals-kill-stop .correct explanation="El kernel reserva estas dos señales para que un proceso no pueda anular ni aplazar sus acciones fundamentales."}
::option[`SIGINT` y `SIGTERM`]{#process-signals-int-term explanation="Ambas pueden tener manejadores instalados por el usuario y pueden bloquearse."}
::option[`SIGHUP` y `SIGCONT`]{#process-signals-hup-cont explanation="Estas señales tienen una semántica especial, pero no son la pareja imposible de capturar."}
:::

## Resumen

Ahora puedes explicar las principales etapas y restricciones del tratamiento de señales en Linux.

1. Identifica señales generadas por terminales, el kernel y otros procesos.
2. Distingue acciones predeterminadas, señales ignoradas y manejadores.
3. Relaciona el bloqueo con la entrega pendiente y las máscaras de hilos.
4. Recuerda que `SIGKILL` y `SIGSTOP` no pueden tratarse ni bloquearse.
