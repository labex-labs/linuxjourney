---
lesson_id: "upstart-overview"
course_id: "init"
lang: "es"
order_index: 3
title: "Descripción general de Upstart"
description: "Aprende cómo el antiguo sistema de inicio Upstart relaciona expresiones de eventos con objetivos del ciclo de vida de los trabajos."
meta_title: "Descripción general de Upstart - Init"
meta_description: "Aprende sobre Upstart, su modelo basado en eventos y cómo gestiona servicios en Linux. Comprende las configuraciones de trabajos de Upstart y su función como sistema de inicio."
meta_keywords: "Upstart, sistema init, servicios Linux, Ubuntu, SysV, tutorial para principiantes, guía Linux"
---

Upstart es un antiguo sistema de inicio y gestión de servicios basado en eventos que desarrolló Canonical. Las versiones anteriores de Ubuntu y varias distribuciones más lo utilizaron, pero las versiones actuales de Ubuntu usan systemd. Estudia Upstart cuando mantengas una máquina antigua confirmada, no como supuesto predeterminado para una instalación moderna.

## Confirmar una máquina antigua con Upstart

Inspecciona el PID 1 y la interfaz de control activa:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
$ initctl version
```

El último comando solo ofrece un resultado significativo cuando están presentes el servicio de control y el cliente de Upstart. Un directorio como `/usr/share/upstart` o archivos residuales bajo `/etc/init` son indicios débiles, porque los paquetes y restos de una migración pueden permanecer después de que otro sistema de inicio tome el control.

:::single-choice{#upstart-overview-active-evidence}
¿Cuál es la prueba más sólida de que una máquina usa realmente Upstart?

::option[El nombre de un directorio contiene la palabra `upstart`.]{#upstart-overview-directory-only explanation="La documentación instalada o los restos pueden permanecer en un sistema que usa otro sistema de inicio."}
::option[El sistema tiene al menos un script de shell.]{#upstart-overview-shell-script explanation="Los scripts de shell son habituales en todos los entornos de inicio."}
::option[El PID 1 y la interfaz `initctl` activa identifican Upstart.]{#upstart-overview-live-interface .correct explanation="Las pruebas del proceso y del control en ejecución son más sólidas que la mera existencia de archivos antiguos."}
:::

## Trabajos y eventos

Un **trabajo** de Upstart describe un servicio o una tarea, incluidos sus comandos de proceso y las condiciones de su ciclo de vida. Un **evento** es una notificación con nombre y variables de entorno opcionales. La configuración del trabajo puede expresar cuándo su objetivo debe pasar a iniciar o detener.

Los archivos de trabajos del sistema suelen estar bajo `/etc/init/` y tener el sufijo `.conf`. Por ejemplo:

```text
description "Example worker"
start on runlevel [2345]
stop on runlevel [016]
exec /usr/local/sbin/example-worker
```

Este ejemplo utiliza eventos de niveles de ejecución como entradas de compatibilidad. Upstart también puede reaccionar a eventos del sistema de archivos, de dispositivos, de la red o definidos por aplicaciones, según lo que emita el sistema.

:::single-choice{#upstart-overview-start-on}
¿Qué define una sección `start on` de Upstart?

::option[La versión del kernel que debe compilarse a continuación.]{#upstart-overview-kernel-version explanation="Las condiciones de eventos de los trabajos no seleccionan una compilación del kernel."}
::option[La expresión de eventos que orienta el objetivo del trabajo hacia su inicio.]{#upstart-overview-start-condition .correct explanation="Cuando se satisface la expresión, Upstart intenta realizar la transición de inicio configurada para el trabajo."}
::option[La partición de disco donde todos los trabajos almacenan datos.]{#upstart-overview-partition explanation="La ubicación del almacenamiento no está relacionada con la sintaxis de eventos de Upstart."}
:::

## Inicio basado en eventos

Durante el arranque, Upstart carga las definiciones de los trabajos y recibe eventos. Las expresiones `start on` o `stop on` que coinciden actualizan los objetivos de los trabajos; las transiciones de estos pueden emitir eventos adicionales que desbloqueen otras tareas. Los trabajos independientes pueden avanzar de forma simultánea.

Este modelo evita una única secuencia global de scripts codificada de forma rígida, pero puede ser difícil de diagnosticar cuando los nombres, el orden y las condiciones de los eventos son implícitos. De forma predeterminada, los eventos no constituyen una cola de mensajes persistente, por lo que un trabajo añadido o una condición modificada posteriormente no deben suponer que todos los eventos pasados se volverán a reproducir.

:::single-choice{#upstart-overview-event-chain}
¿Cómo puede un trabajo de Upstart provocar que se inicie otro?

::option[Reescribe en memoria el binario ejecutable del otro trabajo.]{#upstart-overview-rewrite-binary explanation="La coordinación se realiza mediante eventos, no modificando el código."}
::option[Todos los trabajos siempre se inician estrictamente según el orden de sus nombres de archivo.]{#upstart-overview-filename-order explanation="Upstart utiliza expresiones de eventos en lugar de una lista de inicio ordenada por nombres de archivo."}
::option[Su transición puede emitir un evento que coincida con la condición de otro trabajo.]{#upstart-overview-emitted-event .correct explanation="Las expresiones de eventos conectan las transiciones del ciclo de vida de trabajos que, por lo demás, son independientes."}
:::

## Migración y compatibilidad

Systemd puede ofrecer compatibilidad limitada con algunos scripts de servicio antiguos, pero no ejecuta la sintaxis de los trabajos de Upstart como unidades nativas de systemd. Al migrar, traduce las condiciones del ciclo de vida, el entorno, la política de reaparición, el registro, las dependencias y la semántica de disponibilidad en lugar de limitarte a cambiar el nombre de los archivos.

:::single-choice{#upstart-overview-current-ubuntu}
¿Qué sistema de inicio utilizan las versiones estándar actuales de Ubuntu?

::option[Upstart de forma exclusiva en todas las instalaciones.]{#upstart-overview-current-upstart explanation="Eso solo fue cierto durante determinados periodos y configuraciones de versiones antiguas."}
::option[systemd.]{#upstart-overview-current-systemd .correct explanation="Upstart pertenece a generaciones anteriores de Ubuntu; las versiones actuales utilizan systemd como PID 1."}
::option[Ningún proceso de inicio.]{#upstart-overview-no-init explanation="Un sistema Ubuntu completo sigue necesitando un gestor de servicios como PID 1."}
:::

## Resumen

Ahora puedes interpretar Upstart como un antiguo modelo de eventos y trabajos.

1. Confirma el PID 1 activo y la interfaz de control.
2. Distingue las definiciones de trabajos de las notificaciones de eventos.
3. Interpreta `start on` y `stop on` como expresiones del ciclo de vida.
4. Migra explícitamente la semántica en lugar de cambiar el nombre de los archivos de configuración.
