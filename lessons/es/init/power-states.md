---
lesson_id: "power-states"
course_id: "init"
lang: "es"
order_index: 7
title: "Estados de energía"
description: "Aprende a programar, cancelar y comprobar de forma segura operaciones de apagado y reinicio de Linux."
meta_title: "Estados de energía - Init"
meta_description: "Aprende a gestionar los estados de energía de un sistema Linux. Esta guía explica los comandos esenciales shutdown, reboot y halt para apagar o reiniciar Linux de forma segura. Domina estos comandos fundamentales de administración de sistemas."
meta_keywords: "estados de energía linux, comando shutdown, comando reboot, comando halt, apagar linux, reiniciar linux, administración de sistemas linux, linux para principiantes, comandos linux, systemd, init"
---

Apagar o reiniciar cambia la disponibilidad de todo el sistema. Antes de actuar, confirma la máquina de destino, obtén autorización, avisa a los usuarios conectados y asegúrate de que las escrituras, copias de seguridad y tareas de mantenimiento importantes puedan finalizar. En un sistema remoto, conserva una consola independiente u otra vía de recuperación por si la máquina no vuelve a estar disponible.

## Apagar de forma segura

En una distribución basada en systemd, solicita un apagado ordenado con:

```bash
$ sudo systemctl poweroff
```

La interfaz tradicional `shutdown` también está disponible de forma generalizada:

```bash
$ sudo shutdown -h now
```

Un apagado ordenado pide a los servicios que se detengan, desmonta los sistemas de archivos y después cambia el estado de energía de la máquina. No trates un reinicio forzado o el interruptor físico como atajos habituales: cualquiera de ellos puede interrumpir escrituras y dejar datos o servicios en un estado incoherente.

:::single-choice{#power-states-orderly-poweroff} ¿Qué debes hacer antes de apagar una máquina remota de producción?

::option[Desconectar su consola de administración antes de ejecutar el comando.]{#power-states-remove-console explanation="Una consola de administración proporciona un acceso de recuperación útil y debe seguir disponible."}
::option[Forzar el apagado para que los servicios no puedan retrasar la operación.]{#power-states-force-first explanation="Una operación forzada puede interrumpir escrituras y no debe ser el método habitual."}
::option[Confirmar la máquina y conservar una vía de acceso para la recuperación.]{#power-states-confirm-and-recover .correct explanation="Confirmar el destino evita actuar sobre la máquina equivocada, mientras que el acceso de recuperación ayuda si no vuelve a estar disponible."}
:::

## Programar y cancelar un apagado

Da tiempo a los usuarios y a las cargas de trabajo para prepararse programando la operación. La forma `+m` expresa una cantidad de minutos a partir de ahora:

```bash
$ sudo shutdown -h +4
```

Esto programa una detención o un apagado dentro de cuatro minutos y envía avisos a los usuarios que han iniciado sesión. Si se pospone el mantenimiento, cancela el apagado pendiente antes de que venza el plazo:

```bash
$ sudo shutdown -c
```

No supongas que un aviso hace que la operación sea segura. Comprueba las sesiones activas y las cargas de trabajo específicas del sistema, y sigue el procedimiento documentado de drenaje del servicio o clúster cuando exista.

:::single-choice{#power-states-four-minute-schedule} ¿Qué comando programa un apagado dentro de cuatro minutos?

::option[`sudo shutdown -h +4`]{#power-states-relative-four .correct explanation="La acción `-h` combinada con `+4` solicita el apagado dentro de cuatro minutos."}
::option[`sudo shutdown -h 4`]{#power-states-absolute-four explanation="Sin el signo más, el argumento de tiempo no utiliza la forma documentada de minutos relativos."}
::option[`sudo shutdown -c +4`]{#power-states-cancel-four explanation="La opción `-c` cancela un apagado pendiente en lugar de crear uno."}
:::

## Reiniciar el sistema

Usa un reinicio ordenado cuando la máquina deba detenerse y volver a arrancar:

```bash
$ sudo systemctl reboot
```

Entre los comandos de compatibilidad equivalentes suelen encontrarse:

```bash
$ sudo shutdown -r now
$ sudo reboot
```

Antes de reiniciar, comprueba que los discos cifrados, la configuración de arranque, la red y los servicios necesarios puedan recuperarse sin la sesión interactiva actual. Coordina primero la conmutación por error o la migración de cargas de trabajo cuando otros sistemas dependan de la máquina.

:::single-choice{#power-states-reboot-action} ¿Qué comando solicita un reinicio ordenado inmediato mediante `shutdown`?

::option[`sudo shutdown -c now`]{#power-states-cancel-now explanation="La opción `-c` cancela un apagado pendiente."}
::option[`sudo shutdown -r now`]{#power-states-reboot-now .correct explanation="La opción `-r` selecciona el reinicio y `now` lo programa de inmediato."}
::option[`sudo shutdown -h now`]{#power-states-halt-now explanation="La acción `-h` detiene o apaga el sistema en lugar de reiniciarlo."}
:::

## Distinguir entre detener y apagar

`halt`, `poweroff` y `reboot` pueden ser interfaces de compatibilidad del sistema de inicio, pero los estados finales que solicitan son distintos. Detener interrumpe el funcionamiento normal del sistema; según la plataforma y la implementación, puede dejar la alimentación conectada. Apagar solicita además que el hardware compatible corte la alimentación. Es preferible usar el comando que nombre el resultado deseado y consultar el manual local, porque el comportamiento de compatibilidad puede variar.

:::single-choice{#power-states-halt-versus-poweroff} ¿Por qué debes distinguir `halt` de `poweroff`?

::option[El apagado solicita cortar la alimentación, mientras que la detención puede mantenerla.]{#power-states-power-distinction .correct explanation="El estado final solicitado al hardware puede ser distinto, aunque ambos detengan el funcionamiento normal."}
::option[La detención siempre reinicia los servicios después de pararlos.]{#power-states-halt-restarts explanation="Detener es un estado de parada, no una solicitud para reiniciar servicios."}
::option[El apagado solo cierra la sesión del usuario de la terminal actual.]{#power-states-power-logout explanation="Apagar es una transición de estado de todo el sistema, no el cierre de una sesión de shell."}
:::

## Comprobar el resultado

Para una operación programada, confirma que los usuarios recibieron el aviso y que el trabajo crítico se ha drenado. Después de un reinicio, comprueba el kernel y el estado de arranque esperados, las unidades fallidas, la salud de las aplicaciones, los montajes de almacenamiento, la conectividad de red y los registros del arranque reciente. Poder iniciar sesión no demuestra por sí solo que todo el servicio se haya recuperado.

```bash
$ uptime
$ systemctl --failed
$ journalctl -b -p warning
```

Estos son puntos de partida; usa las comprobaciones de salud propias de la aplicación para la carga de trabajo real.

:::single-choice{#power-states-post-reboot-check} ¿Qué proporciona la prueba más sólida de que una aplicación reiniciada está disponible?

::option[El estado del servicio, los registros y su comprobación de salud son satisfactorios.]{#power-states-health-evidence .correct explanation="Varias comprobaciones del sistema y de la aplicación verifican la carga de trabajo en lugar de limitarse al acceso a la máquina."}
::option[El indicador de alimentación del chasis está encendido.]{#power-states-light-on explanation="Que el hardware tenga alimentación no demuestra que la aplicación funcione correctamente."}
::option[Un administrador puede iniciar sesión en un shell.]{#power-states-shell-open explanation="El acceso al shell solo demuestra una parte de la disponibilidad del sistema."}
:::

## Resumen

Ahora puedes cambiar los estados de energía de Linux con preparación, una intención clara y comprobaciones posteriores.

1. Confirma el destino, el impacto, la autorización y la vía de recuperación.
2. Usa comandos de apagado o reinicio ordenados para las operaciones normales.
3. Programa un apagado cuando los usuarios y las cargas de trabajo necesiten un aviso.
4. Cancela un apagado pendiente cuando cambie el plan de mantenimiento.
5. Comprueba la salud del sistema y de las aplicaciones cuando la máquina vuelva a estar disponible.
