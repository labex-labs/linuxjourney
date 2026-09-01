---
lesson_id: "upstart-jobs"
course_id: "init"
lang: "es"
order_index: 4
title: "Trabajos de Upstart"
description: "Aprende a inspeccionar y controlar trabajos con `initctl` en un sistema antiguo que se haya confirmado que usa Upstart."
meta_title: "Trabajos de Upstart - Init"
meta_description: "Guía para gestionar servicios mediante trabajos de Upstart en un entorno Linux. Aprende a usar la utilidad initctl para listar, iniciar, detener y reiniciar trabajos en un sistema Linux con Upstart."
meta_keywords: "trabajos Upstart, initctl, upstart linux, servicios Linux, administración de sistemas, sistema init, tutorial Linux"
---

`initctl` se comunica con un demonio de inicio Upstart en ejecución. Úsalo únicamente después de confirmar que el espacio de nombres de PID correspondiente ejecuta realmente Upstart; en una máquina actual con systemd, utiliza las herramientas nativas de systemd.

## Listar e interpretar el estado de los trabajos

Lista los trabajos y las instancias conocidas:

```bash
$ initctl list
```

Inspecciona un trabajo:

```bash
$ initctl status networking
networking start/running
```

Upstart informa tanto de un **objetivo**, como `start` o `stop`, como de un **estado** actual, como `running` o `waiting`. `stop/waiting` significa que el trabajo no se está ejecutando y espera una condición de inicio o una solicitud manual; no indica necesariamente un error.

:::single-choice{#upstart-jobs-stop-waiting} ¿Qué suele significar `stop/waiting` en la salida de estado de Upstart?

::option[El trabajo está en ejecución, pero no consume CPU.]{#upstart-jobs-running-idle explanation="Un trabajo en ejecución normalmente mostraría un objetivo de inicio y el estado de ejecución."}
::option[El objetivo del trabajo es permanecer detenido y no hay ninguna instancia del proceso en ejecución.]{#upstart-jobs-stopped-waiting .correct explanation="La definición sigue siendo conocida mientras Upstart espera una condición o un comando futuros."}
::option[Todo el sistema operativo está esperando para apagarse.]{#upstart-jobs-system-poweroff explanation="La pareja describe esta instancia del trabajo, no necesariamente el estado global del sistema."}
:::

## Iniciar y detener un trabajo

Después de revisar las dependencias y el impacto:

```bash
$ sudo initctl start JOB_NAME
$ sudo initctl stop JOB_NAME
```

Los trabajos pueden definir varias instancias identificadas mediante variables de entorno. En ese caso, proporciona exactamente las variables que exige la configuración e inclúyelas de forma coherente al consultar o detener una instancia. Iniciar trabajos de red, almacenamiento, autenticación o acceso remoto puede interrumpir la sesión, así que conserva una vía de recuperación desde la consola.

:::single-choice{#upstart-jobs-start-command} ¿Qué comando solicita manualmente que se inicie el trabajo `peanuts`?

::option[`sudo initctl start peanuts`]{#upstart-jobs-start-peanuts .correct explanation="El subcomando start va seguido del nombre configurado del trabajo y de las variables de instancia necesarias."}
::option[`sudo initctl peanuts start`]{#upstart-jobs-name-first explanation="La sintaxis de initctl coloca el subcomando antes del nombre del trabajo."}
::option[`sudo systemctl initctl peanuts`]{#upstart-jobs-systemctl-mixed explanation="Esta orden mezcla incorrectamente las interfaces de dos gestores de servicios distintos."}
:::

## Reinicios y cambios de configuración

Solicita el reinicio de un trabajo que ya está en ejecución con:

```bash
$ sudo initctl restart peanuts
```

En Upstart, `restart` no siempre equivale a ejecutar un `stop` nuevo seguido de `start` después de editar un archivo de trabajo: la configuración existente del trabajo en ejecución puede seguir prevaleciendo. Valida el archivo `.conf` modificado, pide a Upstart que vuelva a cargar la configuración según la versión instalada y sigue el procedimiento documentado de detención e inicio cuando la nueva configuración deba entrar en vigor.

Un reinicio provoca una interrupción y puede no conseguir que el servicio vuelva a funcionar. Comprueba después el punto de acceso real y los registros.

:::single-choice{#upstart-jobs-restart-peanuts} ¿Qué comando solicita reiniciar el trabajo de Upstart `peanuts` que está en ejecución?

::option[`sudo initctl restart peanuts`]{#upstart-jobs-restart-command .correct explanation="El subcomando restart opera sobre el trabajo indicado mediante la interfaz de control de Upstart."}
::option[`sudo initctl emit peanuts`]{#upstart-jobs-emit-not-restart explanation="Emitir un evento afecta a todas las condiciones coincidentes de los trabajos y no constituye una solicitud directa de reinicio."}
::option[`sudo service --status-all peanuts`]{#upstart-jobs-status-all explanation="Un listado de estados no solicita un reinicio."}
:::

## Validar la configuración de un trabajo

Antes de instalar un archivo de trabajo modificado, usa la herramienta de validación que proporcione la distribución antigua, normalmente `init-checkconf`, y revisa los scripts incluidos, el entorno, los ajustes de usuario y grupo, la política de reaparición y las expresiones de eventos. Después, vuelve a cargar las definiciones mediante el flujo `initctl reload-configuration` apropiado para la versión.

La validación sintáctica no puede demostrar que las rutas existan, que las credenciales permitan la ejecución, que los eventos lleguen ni que el proceso quede disponible. Haz la prueba en un entorno que permita la recuperación.

:::single-choice{#upstart-jobs-syntax-validation-limit} ¿Qué no puede demostrar la validación sintáctica de un trabajo?

::option[Que el servicio se iniciará correctamente y quedará disponible.]{#upstart-jobs-runtime-not-proven .correct explanation="Las rutas, los permisos, las dependencias y el flujo de eventos durante la ejecución requieren una prueba real y controlada."}
::option[Que el texto de configuración se puede analizar.]{#upstart-jobs-parse-purpose explanation="Analizar el texto es precisamente el propósito principal de la validación sintáctica."}
::option[Que se proporcionó un archivo al validador.]{#upstart-jobs-file-supplied explanation="La herramienta puede informar inmediatamente de que falta la entrada."}
:::

## Emitir eventos con cuidado

Upstart puede emitir un evento con nombre:

```bash
$ sudo initctl emit EVENT_NAME
```

Todos los trabajos cuya expresión de inicio o detención coincida pueden reaccionar. Un evento no va dirigido a un único trabajo, y sus efectos pueden propagarse mediante eventos posteriores. Inspecciona todas las configuraciones coincidentes antes de emitir un evento personalizado o del sistema; no reproduzcas despreocupadamente eventos esenciales del arranque en una máquina de producción.

:::single-choice{#upstart-jobs-emit-scope} ¿Qué puede suceder cuando se ejecuta `initctl emit EVENT_NAME`?

::option[Todas las expresiones de trabajos que coincidan con ese evento pueden cambiar de estado.]{#upstart-jobs-event-matches .correct explanation="Los eventos se difunden en el modelo de dependencias de Upstart en lugar de enviarse solo a un servicio determinado."}
::option[Solo puede responder un trabajo cuyo nombre coincida exactamente con el evento.]{#upstart-jobs-event-name-only explanation="La coincidencia se define mediante expresiones `start on` y `stop on`, no mediante la igualdad con el nombre del trabajo."}
::option[El evento se almacena para siempre como mensaje de una cola persistente.]{#upstart-jobs-event-durable explanation="Los eventos de Upstart son notificaciones del ciclo de vida, no una cola de mensajes persistente de propósito general."}
:::

## Resumen

Ahora puedes operar trabajos de Upstart teniendo en cuenta explícitamente el estado y el alcance de los eventos.

1. Interpreta por separado el objetivo y el estado en la salida de `initctl`.
2. Inicia y detén la instancia exacta del trabajo después de revisar el impacto.
3. Trata el reinicio y los cambios en la configuración del trabajo como cuestiones distintas.
4. Valida la sintaxis y después comprueba la disponibilidad durante la ejecución.
5. Inspecciona todas las expresiones coincidentes antes de emitir un evento.
