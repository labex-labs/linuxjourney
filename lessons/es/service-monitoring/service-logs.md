---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "es"
order_index: 2
title: "Registros del servicio"
description: "Aprende a seguir una petición en los registros de varios servicios usando su ID y la hora."
meta_title: "Registros del servicio - Monitorización de servicios"
meta_description: "Aprende a seguir una petición en los registros de varios servicios usando su ID y la hora."
meta_keywords: "registros del servicio, monitorización de servicios, DevOps, Linux Journey"
---

Un usuario ve un error. El registro de un servicio puede indicar en qué parte del proceso falló la petición. Empieza por la hora y busca después un **ID de petición**, una etiqueta que se propaga a los registros de la misma petición.

## Seguir una petición

El ejemplo siguiente muestra dos servicios. Una **dependencia** es un servicio que otro programa necesita para completar una tarea. Aquí el servicio web solicita una lista de artículos al servicio de catálogo.

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

La línea del servicio web muestra una respuesta fallida para `r17`. La línea del catálogo con el mismo ID indica que se agotó el tiempo de espera. La petición al catálogo que aparece cerca y sí se completó corresponde a `r18`.

:::single-choice{#service-logs-matching-request} ¿Qué resultado del catálogo corresponde al fallo del servicio web para r17?

::option[El resultado correcto de r18.]{#service-logs-matching-request-a explanation="Esa línea corresponde a otra petición."}
::option[Ambos resultados del catálogo.]{#service-logs-matching-request-c explanation="Dos registros con horas cercanas pueden corresponder a peticiones distintas."}
::option[El tiempo de espera agotado en r17.]{#service-logs-matching-request-b .correct explanation="El ID compartido vincula los dos registros de esta petición."}
:::

## Filtrar la muestra

Guarda las tres líneas anteriores en `requests.log` dentro de un directorio de prácticas. Usa `grep -F` para buscar texto literal. Incluye el espacio después del identificador para que, en este ejemplo, la coincidencia llegue justo hasta el final del campo.

```bash
$ grep -F 'request=r17 ' requests.log
```

Verás las líneas del servicio web y del catálogo para `r17`. Los registros reales pueden usar otros formatos u omitir el ID de petición. Comprueba que los campos que buscas representen lo mismo en todos los servicios.

:::single-choice{#service-logs-choose-filter} ¿Por qué buscar el campo de petición completo en vez de la palabra timeout?

::option[Garantiza que todo el tráfico tuvo el mismo error.]{#service-logs-choose-filter-b explanation="El filtro selecciona los registros de una sola petición."}
::option[Devuelve los registros correspondientes del servicio web y del catálogo aunque solo uno contenga timeout.]{#service-logs-choose-filter-a .correct explanation="El ID compartido permite seguir la petición en ambos servicios."}
::option[Modifica el archivo de registro para que las siguientes búsquedas den el resultado correcto.]{#service-logs-choose-filter-c explanation="Grep lee el archivo e imprime las líneas que coinciden."}
:::

![Salida de grep que vincula el error web con el tiempo de espera agotado del catálogo para la petición r17](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## Describir el alcance del fallo

El tiempo de espera agotado indica dónde se observó el fallo de esta petición. Aún queda por averiguar qué componente del catálogo se ralentizó. Revisa las métricas o los registros recientes de la dependencia. Si compartes un fragmento con alguien de tu equipo, conserva el ID de petición y elimina los secretos y datos personales que no hagan falta.

:::single-choice{#service-logs-evidence-limit} ¿Qué debes indicar en un primer informe?

::option[Se agotó el tiempo de espera del catálogo durante r17 y conviene investigar.]{#service-logs-evidence-limit-c .correct explanation="Esto resume los registros de la petición sin dar por supuesta la causa."}
::option[Se agotó el tiempo de espera en todas las peticiones al catálogo.]{#service-logs-evidence-limit-a explanation="La muestra contiene otra petición al catálogo que sí se completó."}
::option[Falló un disco concreto de la base de datos.]{#service-logs-evidence-limit-b explanation="Ningún registro contiene datos sobre discos."}
:::

Para practicar la consulta de registros de servicio en un equipo Linux, prueba [Analizar registros para responder a incidentes](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586).

## Resumen

Ya puedes seguir una petición en los registros de varios servicios.

1. Busca el mismo ID de petición en los registros pertinentes.
2. Usa un filtro literal para acotar la muestra.
3. Informa de lo que muestran los registros y decide qué investigar a continuación.
