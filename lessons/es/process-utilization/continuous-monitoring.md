---
lesson_id: "continuous-monitoring"
course_id: "process-utilization"
lang: "es"
order_index: 7
title: "Supervisión continua"
description: "Aprende cómo la recopilación de sysstat y los informes de sar permiten analizar históricamente el rendimiento de Linux."
meta_title: "Supervisión continua - Utilización de procesos"
meta_description: "Aprende a supervisar continuamente sistemas Linux con sysstat y sar, y a analizar datos históricos de recursos."
meta_keywords: "sar, sysstat, supervisión Linux, rendimiento del sistema, supervisión continua, datos históricos"
---

Las herramientas interactivas muestran lo que ocurre mientras las observas. Cuando una ralentización ya ha terminado, se necesita supervisión histórica. El conjunto `sysstat` recopila periódicamente contadores del sistema, y `sar` lee los contadores actuales o archivos de actividad guardados.

## Habilitar la recopilación de datos

Instala el paquete `sysstat` de la distribución y después confirma que su recopilador y su mecanismo de retención estén habilitados. Las rutas exactas de servicios, temporizadores y configuración varían según la distribución; instalar el paquete no garantiza que haya comenzado la recopilación.

En un equipo con systemd, examina las unidades proporcionadas por el paquete en vez de adivinar sus nombres:

```bash
$ systemctl list-unit-files | grep sysstat
$ systemctl list-timers --all | grep sysstat
```

Verifica que se estén creando archivos de actividad nuevos en el directorio de datos de sysstat de la distribución y revisa sus permisos y su política de retención.

:::single-choice{#sar-installation-verification} ¿Qué debes verificar después de instalar `sysstat`?

::option[Que la recopilación esté habilitada y los archivos de actividad se actualicen.]{#sar-collector-updating .correct explanation="La instalación del paquete y la recopilación periódica activa son condiciones independientes."}
::option[Que todos los procesos se hayan reiniciado manualmente.]{#sar-restart-processes explanation="Instalar un recopilador de supervisión no exige reiniciar todas las cargas de trabajo."}
::option[Que todos los archivos históricos permitan escribir a todo el mundo.]{#sar-world-writable explanation="Los datos de supervisión deben conservar controles de acceso apropiados."}
:::

## Leer muestras actuales

Solicita a `sar` tres informes de CPU a intervalos de un segundo:

```bash
$ sar -u 1 3
```

Otros informes habituales incluyen la cola de ejecución y la carga (`-q`), la memoria (`-r`), la paginación (`-B`), los dispositivos de bloques (`-d`) y la actividad de cada CPU (`-P ALL`). Las opciones y los campos varían según la versión de sysstat, así que consulta `sar --help` o el manual local.

:::single-choice{#sar-one-second-count} ¿Qué solicita `sar -u 1 3`?

::option[Tres informes de CPU a intervalos de un segundo.]{#sar-three-cpu-samples .correct explanation="El primer número es el intervalo en segundos y el segundo es la cantidad de informes."}
::option[Un informe que abarca exactamente tres días.]{#sar-three-days explanation="Los operandos indican el intervalo y el número de muestras, no un intervalo de fechas."}
::option[La eliminación de tres archivos de CPU guardados.]{#sar-delete-files explanation="La orden lee contadores y no solicita ninguna eliminación."}
:::

## Leer archivos históricos

Las ubicaciones y los nombres de los archivos guardados varían; suelen encontrarse bajo `/var/log/sysstat` o `/var/log/sa`. Pasa un archivo de actividad seleccionado mediante `-f`:

```bash
$ sar -q -f /var/log/sysstat/sa02
```

Confirma la fecha completa del archivo en los encabezados del informe; un sufijo de dos dígitos suele referirse al día del mes y puede ser ambiguo entre períodos de retención. Los formatos binarios guardados también pueden necesitar una versión compatible de sysstat.

:::single-choice{#sar-historical-file-option} ¿Qué opción indica a `sar` que lea un archivo de actividad determinado?

::option[`-P`]{#sar-option-p explanation="Esta opción selecciona informes de procesadores, no un archivo de entrada."}
::option[`-q`]{#sar-option-q explanation="Esta opción selecciona informes de colas y carga."}
::option[`-f`]{#sar-option-f .correct explanation="La opción de archivo selecciona los datos de actividad guardados que se deben leer."}
:::

## Relacionar un incidente

Establece la hora y la zona horaria del incidente y compara después varias señales durante el mismo intervalo. Busca cambios en la carga, la CPU, la cola de ejecución, la paginación, la actividad de dispositivos, el tráfico de red y la latencia de la aplicación. Los cambios de contadores muestran correlación, no necesariamente causalidad; los registros de despliegues y de aplicaciones pueden explicar el desencadenante.

Los huecos pueden significar que el equipo estaba apagado, que falló el recopilador o que la retención eliminó datos. Supervisa la propia canalización de supervisión para que la ausencia de pruebas resulte visible antes de un incidente.

:::single-choice{#sar-incident-method} ¿Cómo deben utilizarse los datos históricos de `sar` al revisar un incidente?

::option[Tratar el contador individual más alto como causa raíz demostrada.]{#sar-single-root explanation="Una sola correlación no establece causalidad."}
::option[Comparar varias métricas durante el mismo intervalo de tiempo verificado.]{#sar-correlate-window .correct explanation="Las señales alineadas ayudan a distinguir hipótesis y a conectar el comportamiento del sistema con el incidente."}
::option[Ignorar los huecos porque la recopilación está garantizada después de instalar el paquete.]{#sar-ignore-gaps explanation="La recopilación puede fallar o estar deshabilitada, y los huecos necesitan una explicación."}
:::

## Resumen

Ahora puedes utilizar `sar` para investigar el rendimiento fuera de una sesión interactiva.

1. Verifica que la recopilación y la retención estén realmente activas.
2. Solicita muestras actuales limitadas mediante un intervalo y una cantidad.
3. Selecciona explícitamente archivos históricos de actividad.
4. Alinea varias métricas con la hora del incidente y las pruebas de la carga de trabajo.
