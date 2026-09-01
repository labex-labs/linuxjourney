---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "es"
order_index: 5
title: "Supervisión de E/S"
description: "Aprende a utilizar muestras de iostat para investigar la actividad de la CPU y de los dispositivos de bloques."
meta_title: "Supervisión de E/S - Utilización de procesos"
meta_description: "Aprende a supervisar la E/S de Linux con iostat e interpreta la actividad de CPU, la latencia y la utilización de dispositivos."
meta_keywords: "supervisión E/S Linux, iostat, uso de CPU, uso de disco, latencia, iowait"
---

`iostat`, proporcionado habitualmente por el paquete `sysstat`, comunica la actividad de la CPU y de los dispositivos de bloques. Utiliza muestras repetidas junto con la latencia de la aplicación: el rendimiento o la utilización por sí solos no establecen si el almacenamiento está causando un problema visible para el usuario.

## Recopilar muestras útiles

Ejecuta estadísticas ampliadas de dispositivos a intervalos de un segundo:

```bash
$ iostat -xz 1
```

En las implementaciones habituales, el primer informe contiene promedios desde el arranque y los posteriores abarcan cada intervalo. La opción `-x` añade campos ampliados y `-z` oculta los dispositivos inactivos. Deja que transcurran varios intervalos para capturar períodos normales y problemáticos.

:::single-choice{#iostat-first-report} ¿Qué representa habitualmente el primer informe de `iostat`?

::option[Únicamente las operaciones del último segundo de la orden.]{#iostat-final-second explanation="Eso no describe el informe acumulado inicial."}
::option[Promedios de actividad desde que arrancó el sistema.]{#iostat-since-boot .correct explanation="Los informes posteriores suelen corresponder a cada intervalo, por lo que el primero debe interpretarse por separado."}
::option[Una predicción de la utilización de dispositivos de mañana.]{#iostat-forecast explanation="La herramienta comunica estadísticas observadas, no demanda futura."}
:::

## Leer los campos de CPU

La sección de CPU suele incluir tiempo de usuario (`%user`), del sistema (`%system`), inactivo (`%idle`), de espera de E/S (`%iowait`) y sustraído por máquinas virtuales (`%steal`). La espera de E/S es tiempo de CPU inactivo durante el cual el sistema tiene una solicitud de E/S pendiente; no es el porcentaje de ocupación de un disco.

:::single-choice{#iostat-iowait-meaning} ¿Qué describe `%iowait`?

::option[El porcentaje de capacidad del disco que ya está ocupado.]{#iostat-capacity explanation="La capacidad del sistema de archivos y el tiempo de CPU son mediciones distintas."}
::option[El tiempo de CPU inactivo mientras existe una solicitud de E/S pendiente.]{#iostat-iowait-cpu .correct explanation="Es una categoría de tiempo de CPU y por sí sola no puede identificar un dispositivo."}
::option[El número de archivos que esperan ser eliminados.]{#iostat-delete-queue explanation="Este campo no representa el número de eliminaciones de archivos."}
:::

## Leer los campos de dispositivos

Los nombres de los campos varían según la versión de sysstat, pero algunos conceptos útiles son:

- Las operaciones o los datos leídos y escritos por segundo muestran la tasa de la carga de trabajo.
- `await` comunica la latencia media de las solicitudes, incluido el tiempo en cola y de servicio.
- Los campos de tamaño medio de la cola muestran solicitudes que esperan o están siendo atendidas.
- `%util` comunica el porcentaje del tiempo transcurrido durante el cual el dispositivo tuvo E/S en curso.

Un `%util` alto puede indicar saturación en un dispositivo serie sencillo, pero no se traduce directamente en capacidad de rendimiento para almacenamiento paralelo, matrices o dispositivos virtuales. Compara la latencia con el diseño del dispositivo, el patrón de la carga de trabajo y el objetivo del servicio.

:::single-choice{#iostat-await-purpose} ¿Qué campo se asocia de forma más directa con la latencia media de las solicitudes de E/S?

::option[El nombre del dispositivo.]{#iostat-device-name explanation="El nombre identifica el dispositivo, pero no mide la duración de las solicitudes."}
::option[`await`]{#iostat-await .correct explanation="Await refleja el tiempo medio de las solicitudes, incluidos el tiempo en cola y el de servicio."}
::option[`%idle`]{#iostat-idle explanation="Este es un campo de CPU, no la latencia de las solicitudes del dispositivo."}
:::

## Relacionar las pruebas

Relaciona los nombres de dispositivos con los montajes y los dispositivos subyacentes antes de extraer conclusiones:

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

Después, relaciona los intervalos de `iostat` con el tiempo de respuesta de la aplicación, las métricas de la base de datos o del sistema de archivos y la E/S a nivel de proceso. El mapeador de dispositivos, RAID, los contenedores y el almacenamiento respaldado por red pueden añadir capas que necesiten sus propias herramientas.

:::single-choice{#iostat-high-util-conclusion} ¿Qué debes hacer después de observar un `%util` alto en un dispositivo?

::option[Suponer que todos los sistemas de archivos se han quedado sin espacio libre.]{#iostat-assume-full explanation="El tiempo ocupado no comunica la capacidad del sistema de archivos."}
::option[Eliminar archivos antes de identificar la carga de trabajo montada.]{#iostat-delete-first explanation="Eliminar es una acción que cambia el estado y no guarda relación con demostrar un cuello de botella de E/S."}
::option[Relacionar la latencia y el comportamiento de la carga con el diseño del almacenamiento.]{#iostat-correlate .correct explanation="El paralelismo del dispositivo y los objetivos de la carga determinan si la observación es perjudicial."}
:::

## Resumen

Ahora puedes utilizar `iostat` como prueba en una investigación de E/S.

1. Recopila varios intervalos de estadísticas ampliadas.
2. Distingue la espera de E/S de la CPU del tiempo de ocupación del dispositivo.
3. Interpreta juntos la latencia, las colas, el rendimiento y la utilización.
4. Relaciona los dispositivos con las cargas de trabajo y verifica el impacto en la aplicación.
