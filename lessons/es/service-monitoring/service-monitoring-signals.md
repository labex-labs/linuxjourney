---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "es"
order_index: 1
title: "Señales de monitorización"
description: "Aprende a elegir una señal de monitorización que responda a una pregunta sobre un servicio web."
meta_title: "Señales de monitorización - Monitorización de servicios"
meta_description: "Aprende a elegir una señal de monitorización que responda a una pregunta sobre un servicio web."
meta_keywords: "señales de monitorización, monitorización de servicios, DevOps, Linux Journey"
---

Un visitante dice que la página va lenta. Empieza por lo que experimentó y elige una medición que permita describirlo. Una **señal** es un dato observado, como un recuento, una medición o un evento registrado.

## Comprobar lo que experimenta el usuario

La **disponibilidad** indica si el servicio puede hacer el trabajo esperado. Por ejemplo, puedes solicitar la página de inicio y comprobar si el servicio responde correctamente. La **latencia** es el tiempo que tarda la petición. Una página puede abrirse correctamente y aun así tardar varios segundos.

:::single-choice{#service-monitoring-signals-slow-page} Los visitantes reciben la página, pero tarda varios segundos en llegar. ¿Qué señal describe mejor este síntoma?

::option[El número de contenedores del servidor.]{#service-monitoring-signals-slow-page-b explanation="Ese recuento no mide cuánto esperan los visitantes."}
::option[El tiempo que tarda en llegar la página.]{#service-monitoring-signals-slow-page-a .correct explanation="La latencia mide cuánto tardó la petición."}
::option[El número de bytes del repositorio de código fuente.]{#service-monitoring-signals-slow-page-c explanation="El tamaño del repositorio no indica cuánto tardan las peticiones."}
:::

## Contar peticiones y errores

El **tráfico** es la demanda que recibe el servicio y puede medirse, por ejemplo, en peticiones por minuto. Observa el total de peticiones junto al número de fallos. Cinco errores en 1000 peticiones tienen un peso distinto de cinco errores en diez peticiones.

:::single-choice{#service-monitoring-signals-count-context} Ves cinco fallos en cada uno de dos intervalos. ¿Qué dato te ayuda a comparar el impacto en los usuarios?

::option[El total de peticiones de cada intervalo.]{#service-monitoring-signals-count-context-b .correct explanation="Necesitas ambos totales como denominadores para comparar las tasas de errores."}
::option[El nombre del panel.]{#service-monitoring-signals-count-context-a explanation="El nombre indica dónde está el gráfico, pero no mide el tráfico."}
::option[El orden de los servicios en la lista.]{#service-monitoring-signals-count-context-c explanation="El orden de la lista no indica cuántas peticiones se vieron afectadas."}
:::

## Comprobar si un recurso está al límite

La **saturación** indica lo cerca que está un recurso de su capacidad máxima. Un servicio puede tener trabajo a la espera de una respuesta de la base de datos aunque el proceso web siga en ejecución. Compara lo que observan los usuarios con la señal del recurso antes de sacar conclusiones.

:::single-choice{#service-monitoring-signals-saturation-check} Las peticiones se ralentizan al mismo tiempo que aumenta el trabajo en espera. ¿Qué conviene hacer a continuación?

::option[Afirmar que la acumulación de trabajo es sin duda la causa del problema.]{#service-monitoring-signals-saturation-check-a explanation="Los dos cambios son una pista. Necesitas más datos para establecer la causa."}
::option[Volver a contar las imágenes almacenadas en el equipo anfitrión.]{#service-monitoring-signals-saturation-check-b explanation="La disponibilidad de imágenes no explica la cola de peticiones pendientes."}
::option[Revisar el recurso que atiende el trabajo en espera.]{#service-monitoring-signals-saturation-check-c .correct explanation="Al examinar ese recurso, puedes comprobar si es capaz de seguir el ritmo."}
:::

## Resumen

Ya puedes elegir una señal según lo que observó un usuario.

1. Distingue la disponibilidad de la latencia.
2. Interpreta los fallos junto con el volumen de peticiones.
3. Usa la saturación como pista sobre la capacidad disponible.
