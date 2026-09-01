---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "es"
order_index: 4
title: "Registro del kernel"
description: "Aprende a consultar los mensajes actuales y conservados del kernel de Linux con dmesg y journalctl."
meta_title: "Registro del kernel - Logging"
meta_description: "Explora el registro del kernel de Linux, incluidos /var/log/kern.log y dmesg. Aprende a consultar mensajes de arranque e información de controladores de hardware y a diagnosticar problemas del sistema."
meta_keywords: "registro del kernel, kern.log, /var/log/kern.log, kernel log linux, registro kern, dmesg, registro linux, mensajes de arranque, eventos del kernel"
---

El kernel emite mensajes sobre el arranque, los controladores, los dispositivos, los sistemas de archivos, la red, la memoria y los fallos. Estos registros pueden explicar síntomas de bajo nivel, pero una sola cadena de advertencia no demuestra que el hardware esté averiado.

## Leer el búfer circular del kernel

`dmesg` lee los mensajes del búfer circular del kernel:

```bash
$ dmesg --human
```

El búfer tiene una capacidad limitada, por lo que los mensajes nuevos pueden sobrescribir los antiguos. El acceso también puede estar restringido a usuarios con privilegios. `dmesg --follow` sigue los mensajes nuevos del kernel en las implementaciones compatibles; detenlo después de una reproducción limitada.

:::single-choice{#kernel-log-ring-buffer-limit} ¿Por qué puede faltar un evento antiguo del kernel en la salida actual de `dmesg`?

::option[Los eventos del kernel solo pueden contener un carácter.]{#kernel-log-one-character explanation="Los mensajes del kernel pueden contener texto de diagnóstico y metadatos normales."}
::option[`dmesg` elimina permanentemente todas las líneas después de mostrarlas.]{#kernel-log-display-deletes explanation="Una lectura normal no consume todos los mensajes mostrados del kernel."}
::option[El búfer circular limitado puede haberlo sobrescrito.]{#kernel-log-overwritten .correct explanation="El búfer en memoria conserva una cantidad limitada de datos de mensajes del kernel."}
:::

## Usar marcas de tiempo legibles

Las marcas de tiempo sin procesar del kernel suelen ser relativas al arranque. `dmesg --ctime` o `--human` pueden mostrarlas como horas de reloj, pero los valores convertidos dependen del historial del reloj y pueden ser inexactos si este cambió después del arranque. Conserva los tiempos relativos al arranque cuando sea importante ordenar los eventos con precisión.

:::single-choice{#kernel-log-timestamp-caution} ¿Por qué deben interpretarse con cuidado las marcas de tiempo de reloj convertidas por `dmesg`?

::option[Siempre hacen referencia a otra máquina.]{#kernel-log-other-machine explanation="Se derivan localmente, aunque los cambios del reloj pueden afectar a la conversión."}
::option[Dependen de relacionar el tiempo relativo al arranque con un reloj que puede cambiar.]{#kernel-log-clock-change .correct explanation="La sincronización horaria o los cambios manuales del reloj pueden hacer que la hora mostrada resulte engañosa."}
::option[Muestran el espacio libre del sistema de archivos en lugar de la hora.]{#kernel-log-free-space explanation="Las opciones de marcas de tiempo siguen mostrando horas, no capacidad de almacenamiento."}
:::

## Consultar registros persistentes del kernel

En una máquina con systemd, consulta los registros del kernel del arranque actual con:

```bash
$ journalctl -k -b
```

Si el almacenamiento persistente del diario conservó arranques anteriores, inspecciona la lista y selecciona uno:

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

El enrutamiento tradicional de syslog puede crear `/var/log/kern.log` u otro archivo, pero esto depende de la configuración. Un archivo `/var/log/dmesg` guardado tampoco es universal y puede representar únicamente una instantánea del momento del arranque.

:::single-choice{#kernel-log-previous-boot} ¿Qué comando solicita los mensajes del kernel del arranque anterior conservado?

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="Los mensajes del kernel se seleccionan con `-k`, y seguirlos no elige el arranque anterior."}
::option[`dmesg --clear`]{#kernel-log-clear explanation="Borrar cambia el estado del búfer y no recupera un arranque anterior."}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="El filtro del kernel combinado con el desplazamiento de arranque menos uno selecciona el arranque anterior conservado."}
:::

## Investigar un evento del kernel

Identifica el arranque, la marca de tiempo, el dispositivo, el subsistema y la acción que tenía lugar en ese momento. Consulta los registros circundantes del kernel y de los servicios, y compáralos después con el inventario del hardware y el estado actual:

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

Utiliza únicamente herramientas pertinentes para el subsistema. Antes de recargar un controlador, desvincular un dispositivo o reiniciar, evalúa el impacto sobre el almacenamiento, la red, la consola y los servicios, y conserva un acceso de recuperación.

:::single-choice{#kernel-log-warning-response} ¿Cuál es la mejor respuesta ante una sola línea de advertencia del kernel?

::option[Descargar inmediatamente todos los controladores cargados.]{#kernel-log-unload-all explanation="Esto puede interrumpir dispositivos esenciales y no aísla la causa de la advertencia."}
::option[Suponer que hay que sustituir toda la máquina.]{#kernel-log-replace-machine explanation="Un solo registro no proporciona pruebas suficientes para esa conclusión."}
::option[Correlacionarla con los eventos circundantes y el estado actual del subsistema.]{#kernel-log-correlate .correct explanation="Se necesitan contexto y un impacto reproducible antes de elegir una medida correctiva."}
:::

## Resumen

Ahora puedes distinguir los mensajes activos del búfer del kernel de sus registros conservados.

1. Lee el búfer circular limitado con `dmesg`.
2. Interpreta con cuidado las marcas de tiempo relativas al arranque y las convertidas.
3. Consulta el arranque actual o los anteriores con `journalctl -k`.
4. Correlaciona los mensajes del kernel antes de realizar cambios que puedan causar interrupciones.
