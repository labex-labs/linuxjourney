---
lesson_id: "killing-processes"
course_id: "processes"
lang: "es"
order_index: 7
title: "kill (terminar)"
description: "Aprende a identificar un proceso y enviarle una señal apropiada con kill mediante una secuencia de escalada segura."
meta_title: "kill (terminar) - Procesos"
meta_description: "Domina la orden kill de Linux: verifica el proceso de destino, usa SIGTERM para una salida ordenada y reserva SIGKILL para una escalada justificada."
meta_keywords: "orden kill, kill SIGTERM, kill -0 Linux, SIGTERM, SIGKILL, gestión de procesos, terminar proceso"
---

La orden `kill` envía una señal a un proceso o grupo de procesos. Su nombre es histórico: la señal solicitada puede terminar, detener, continuar o provocar alguna acción definida por la aplicación. Confirma siempre el destino exacto y comprende el comportamiento documentado del programa para esa señal antes de enviarla.

## Solicitar una terminación ordenada

Con solo un PID, `kill` envía `SIGTERM` de forma predeterminada:

```bash
$ kill 12445
```

Prefiere el nombre simbólico cuando indiques explícitamente una señal:

```bash
$ kill -TERM 12445
```

La acción predeterminada de `SIGTERM` es terminar, pero un programa puede capturarla o ignorarla. Un servicio bien diseñado puede usar un manejador para dejar de aceptar trabajo, guardar el estado apropiado y liberar recursos de la aplicación. Es una posibilidad, no una garantía de limpieza inmediata o correcta.

:::single-choice{#killing-processes-default-signal}
¿Qué señal solicita `kill PID` de forma predeterminada?

::option[`SIGKILL`]{#killing-processes-default-kill explanation="La señal forzosa que no puede capturarse debe seleccionarse explícitamente."}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="Sin otro operando de señal, `kill` envía la solicitud estándar de terminación."}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="Detener un proceso no es la acción predeterminada solicitada por `kill`."}
:::

## Verificar el destino

Los PID pueden reutilizarse, por lo que un PID antiguo puede identificar después un proceso diferente. Consulta el destino activo inmediatamente antes de actuar:

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

Comprueba su usuario, hora de inicio, orden, padre, propiedad por un servicio y función operativa. Si un gestor de servicios controla el proceso, usa su orden de parada o recarga cuando sea posible, para que pueda mantener el estado correcto y evitar reiniciar inmediatamente al hijo.

Puedes enviar señales a procesos de tu propiedad, sujeto a las reglas de credenciales. Para señalizar el proceso de otro usuario suelen necesitarse los privilegios apropiados. No uses una orden amplia basada en nombres hasta haber revisado todas las coincidencias.

:::single-choice{#killing-processes-pid-reuse}
¿Por qué debes consultar un PID inmediatamente antes de enviarle una señal?

::option[Un PID cambia cada vez que el proceso lee un archivo.]{#killing-processes-pid-read explanation="Un proceso activo suele conservar el mismo PID durante toda su existencia."}
::option[El kernel puede reutilizar un PID después de que termine su proceso anterior.]{#killing-processes-pid-reused .correct explanation="Un PID numérico recordado puede referirse posteriormente a otro proceso activo."}
::option[`kill` acepta nombres de órdenes, pero no identificadores numéricos.]{#killing-processes-no-numeric explanation="Un PID numérico es el operando de destino normal de `kill`."}
:::

## Comprobar el permiso de señal con la señal cero

La señal número cero realiza comprobaciones de errores sin entregar una señal real:

```bash
$ kill -0 12445
```

Un resultado correcto significa que existe un proceso con ese PID y que quien ejecuta la orden puede enviarle una señal en ese instante. Un fallo es ambiguo: puede que el proceso no exista o que falten permisos. Examina el error y el estado de salida en vez de traducir todos los fallos como «no está en ejecución». Además, solo es una comprobación momentánea y no elimina una carrera posterior por reutilización del PID.

:::single-choice{#killing-processes-signal-zero}
¿Qué demuestra un `kill -0 PID` correcto en ese instante?

::option[El proceso ha completado toda la limpieza y ha terminado.]{#killing-processes-zero-exited explanation="El éxito indica un destino activo al que se pueden enviar señales, no una terminación completada."}
::option[El proceso conservará ese PID permanentemente.]{#killing-processes-zero-permanent explanation="La comprobación es instantánea y los PID pueden reutilizarse después de la salida."}
::option[El proceso existe y quien ejecuta la orden puede enviarle señales.]{#killing-processes-zero-permitted .correct explanation="La señal cero comprueba la existencia y autorización del destino sin entregar una señal normal."}
:::

## Escalar solo cuando sea necesario

Si un destino autorizado no termina después de `SIGTERM`, espera un tiempo apropiado para la carga de trabajo e investiga el motivo. Después, cuando esté justificada la terminación forzosa, envía:

```bash
$ kill -KILL 12445
```

`SIGKILL` no puede capturarse, ignorarse ni bloquearse, por lo que el programa no puede realizar una limpieza en el nivel de aplicación. Puede dejar transacciones incompletas, estado temporal o trabajo de recuperación para otros componentes. Úsala como escalada, no como primer paso habitual.

Otras señales solo tienen significado según el contrato del programa receptor. `SIGHUP` suele solicitar una recarga de configuración, pero algunos programas conservan su acción predeterminada de terminación. `SIGSTOP` pausa sin limpiar y `SIGCONT` reanuda un proceso detenido.

:::single-choice{#killing-processes-kill-tradeoff}
¿Cuál es la principal desventaja operativa de `SIGKILL`?

::option[Únicamente el propietario del proceso puede tratarla.]{#killing-processes-kill-owner-handler explanation="Ningún proceso de destino puede instalar un manejador para `SIGKILL`."}
::option[Pausa el proceso, pero nunca lo termina.]{#killing-processes-kill-pauses explanation="`SIGSTOP` pausa; `SIGKILL` termina."}
::option[No ofrece al programa ninguna oportunidad de limpieza en el nivel de aplicación.]{#killing-processes-kill-no-cleanup .correct explanation="El kernel impone la terminación sin invocar un manejador de señales del espacio de usuario."}
:::

Practica la selección de señales únicamente con procesos que hayas iniciado en un entorno aislado. El laboratorio [Gestionar y supervisar procesos de Linux](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) ofrece un flujo controlado de inspección y terminación.

## Resumen

Ahora puedes enviar señales a procesos mediante un flujo deliberado y verificable.

1. Confirma el destino activo y su supervisor antes de actuar.
2. Usa `SIGTERM` como solicitud normal de terminación.
3. Interpreta la señal cero como una comprobación momentánea de existencia y permisos.
4. Reserva `SIGKILL` para una escalada justificada después de investigar.
