---
lesson_id: "general-logging"
course_id: "logging"
lang: "es"
order_index: 3
title: "Registro general"
description: "Aprende a descubrir, filtrar, seguir y correlacionar registros generales del sistema Linux."
meta_title: "Registro general - Logging"
meta_description: "Guía para principiantes sobre los registros generales de Linux. Aprende sobre /var/log/messages y syslog para supervisar sistemas, analizar registros y diagnosticar problemas de Linux eficazmente."
meta_keywords: "registros de Linux, syslog, var/log/messages, solución de problemas Linux, registros del sistema, análisis de registros, monitorización del sistema, guía Linux, principiante Linux, /var/log"
---

Los registros generales del sistema combinan avisos rutinarios, advertencias y errores de varias fuentes. Son puntos de partida útiles, pero sus nombres de archivo y su contenido son decisiones de la política de enrutamiento, no garantías universales de Linux.

## Encontrar la fuente pertinente

Según la distribución y la configuración, los mensajes generales pueden aparecer en `/var/log/syslog`, `/var/log/messages`, el diario de systemd o más de un destino. Empieza por identificar la máquina y el intervalo del incidente y después inspecciona las fuentes disponibles:

```bash
$ ls -lh /var/log
$ journalctl --since '2026-08-31 09:00' --until '2026-08-31 09:15'
```

Los registros de las aplicaciones pueden residir en sus propios subdirectorios o en un servicio externo. Los registros de autenticación, auditoría, paquetes, bases de datos y servidores web pueden estar separados deliberadamente del flujo general.

:::single-choice{#general-logs-universal-file}
¿Por qué no debes suponer que `/var/log/messages` existe en todas las máquinas Linux?

::option[Los destinos de los registros generales dependen de los recolectores locales y de la política de enrutamiento.]{#general-logs-local-routing .correct explanation="Un sistema que solo use el diario o una configuración de syslog distinta puede utilizar otros destinos."}
::option[Linux solo permite un archivo de registro en cada disco.]{#general-logs-one-file explanation="Los sistemas mantienen habitualmente muchos archivos de registro y almacenes de diarios."}
::option[La ruta está reservada exclusivamente para documentos de usuarios.]{#general-logs-user-documents explanation="La jerarquía `/var/log` se utiliza convencionalmente para registros."}
:::

## Inspeccionar registros de texto

Usa `less` para navegar de forma controlada y `tail` para consultar los registros más recientes:

```bash
$ sudo less /var/log/syslog
$ sudo tail -n 100 /var/log/messages
```

Sigue las líneas que se añadan durante una reproducción limitada con `tail -F FILE`. A diferencia de una instantánea sencilla, `-F` vuelve a intentarlo cuando el archivo se sustituye durante una rotación. Deja de seguirlo con `Ctrl-C` y evita mantener abiertas sesiones amplias con privilegios.

:::single-choice{#general-logs-tail-f-capability}
¿Para qué resulta útil `tail -F` durante una reproducción controlada?

::option[Para seguir un archivo por su nombre a través de las sustituciones habituales de la rotación.]{#general-logs-tail-follow .correct explanation="El comportamiento de reintento por nombre permite continuar después de que el archivo activo se renombre y se vuelva a crear."}
::option[Para cambiar todas las gravedades de registro a debug.]{#general-logs-tail-debug explanation="Tail lee el contenido de los archivos y no reconfigura los emisores."}
::option[Para descifrar archivos comprimidos sin otro programa.]{#general-logs-tail-decrypt explanation="No proporciona descompresión o descifrado general de archivos."}
:::

## Filtrar sin perder el contexto

Busca en un archivo o intervalo limitado del diario en lugar de canalizar inmediatamente un flujo activo sin límites:

```bash
$ grep -n -C 3 'connection refused' /var/log/example.log
$ journalctl -u example.service --since '10 minutes ago' --grep='connection refused'
```

El uso de mayúsculas, la redacción, los límites de frecuencia y la localización pueden hacer que una búsqueda literal resulte incompleta. Registra tanto los eventos satisfactorios como los fallidos y conserva las líneas circundantes, porque la causa puede preceder al error visible.

:::single-choice{#general-logs-context-lines}
¿Por qué debes incluir las líneas que rodean un error coincidente?

::option[El evento anterior puede explicar el fallo posterior.]{#general-logs-preceding-context .correct explanation="El contexto temporal ayuda a reconstruir una secuencia en lugar de tratar una cadena como si fuera todo el incidente."}
::option[El contexto garantiza que la primera coincidencia sea la causa raíz.]{#general-logs-guaranteed-cause explanation="Aún es necesario correlacionar otras pruebas; el contexto no demuestra causalidad."}
::option[Modifica automáticamente la configuración del servicio.]{#general-logs-context-config explanation="La salida de búsqueda es de solo lectura y no actualiza los ajustes del servicio."}
:::

## Incluir registros rotados y archivados

Un incidente puede atravesar el límite de una rotación. Los archivos activos, los archivos numerados y los archivos comprimidos pueden contener partes distintas de la misma secuencia. Herramientas como `zgrep` y `zless` leen archivos comprimidos con gzip:

```bash
$ sudo zgrep -n 'connection refused' /var/log/example.log*.gz
```

Ordena los resultados según las marcas de tiempo reales, no solo por el sufijo. Antes de copiar pruebas, conserva los metadatos y restringe el acceso, porque los registros pueden contener datos personales o credenciales.

:::single-choice{#general-logs-rotation-boundary}
¿Qué debes comprobar cuando un incidente abarca una rotación de registros?

::option[Únicamente el archivo activo nuevo y vacío.]{#general-logs-active-only explanation="Los registros anteriores pueden haberse trasladado a archivos rotados."}
::option[Los registros activos y archivados ordenados por el momento del evento.]{#general-logs-all-intervals .correct explanation="La secuencia pertinente puede estar dividida entre los archivos actuales y los rotados."}
::option[Únicamente los nombres de archivo, sin tener en cuenta las marcas de tiempo de los registros.]{#general-logs-filenames-only explanation="El orden de los sufijos y el momento de los eventos no siempre son equivalentes."}
:::

## Resumen

Ahora puedes investigar registros generales en archivos, diarios y a través de los límites de rotación.

1. Descubre los destinos en lugar de suponer que existe un nombre de archivo universal.
2. Lee un intervalo limitado y solo síguelo durante la reproducción.
3. Conserva el contexto temporal alrededor de los registros coincidentes.
4. Incluye los archivos rotados y protege las pruebas sensibles.
