---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "es"
order_index: 6
title: "Alertas del servicio"
description: "Aprende a interpretar la condición de una alerta, el intervalo que cubre y el siguiente paso."
meta_title: "Alertas del servicio - Monitorización de servicios"
meta_description: "Aprende a interpretar la condición de una alerta, el intervalo que cubre y el siguiente paso."
meta_keywords: "alertas del servicio, monitorización de servicios, DevOps, Linux Journey"
---

Un panel muestra mediciones. Una **alerta** pide a alguien que revise una situación que puede requerir una respuesta. Una buena alerta te ayuda a entender qué pasó y qué debes comprobar.

## Interpretar la condición

Imagina una regla que comprueba si falla más del 5 % de las peticiones a la página de inicio en cinco minutos. También exige al menos 100 peticiones para contar con una muestra útil para este servicio.

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

Doce fallos de 120 peticiones equivalen al 10 %. Se cumplen ambas condiciones. El aviso señala los fallos observados en la página de inicio.

:::single-choice{#service-alerts-condition-match} ¿Se activaría la misma alerta si fallara una de cada diez peticiones?

::option[No, porque no se alcanzó el mínimo de peticiones.]{#service-alerts-condition-match-b .correct explanation="Para que se active la alerta, tanto la tasa como el número de peticiones deben cumplir la regla."}
::option[Sí, porque la tasa de errores supera el 5 %.]{#service-alerts-condition-match-a explanation="La regla también exige al menos 100 peticiones."}
::option[No, porque un fallo en diez peticiones equivale al 1 %.]{#service-alerts-condition-match-c explanation="Uno de diez equivale al 10 %, pero la muestra sigue siendo demasiado pequeña para esta regla."}
:::

## Revisar el intervalo de tiempo

Usa el intervalo indicado en la alerta, aunque el panel muestre ahora que el servicio funciona bien. El aviso puede referirse a un problema anterior. Comprueba si la señal ha vuelto a su rango habitual y si los usuarios pueden realizar de nuevo las acciones importantes.

:::single-choice{#service-alerts-alert-window} La alerta llegó a las 09:16 y cubría el intervalo de 09:10 a 09:15. ¿Dónde buscarías primero los errores correspondientes?

::option[Solo en un informe de la semana anterior.]{#service-alerts-alert-window-b explanation="El informe puede servir como referencia, pero no cubre el intervalo afectado."}
::option[Solo después de las 09:16.]{#service-alerts-alert-window-c explanation="La notificación puede llegar después de que se hayan registrado los fallos."}
::option[En el intervalo indicado en la alerta.]{#service-alerts-alert-window-a .correct explanation="En ese periodo se contabilizaron los errores que activaron la regla."}
:::

## Elegir el siguiente paso

Una alerta sobre peticiones fallidas a la página de inicio puede enlazar a las métricas y los registros recientes de esa ruta. Comprueba el impacto en los usuarios e investiga la causa por separado. Si el servicio se ha recuperado, guarda suficiente contexto para investigar si la alerta vuelve a activarse.

:::single-choice{#service-alerts-next-check} ¿Qué acción comprueba directamente si la página de inicio sigue fallando?

::option[Contar todas las imágenes de contenedor de la caché.]{#service-alerts-next-check-a explanation="La alerta se refiere al resultado de peticiones reales al servicio."}
::option[Hacer una petición de prueba autorizada a la ruta afectada.]{#service-alerts-next-check-c .correct explanation="Una nueva petición permite comprobar si el problema persiste en esa ruta."}
::option[Desactivar la regla para dejar de ver el aviso.]{#service-alerts-next-check-b explanation="Eso cambia las notificaciones sin comprobar cómo responde el servicio."}
:::

## Resumen

Ya puedes interpretar una alerta y decidir qué verificar.

1. Revisa la métrica, el umbral y el tamaño mínimo de la muestra.
2. Usa el intervalo de la alerta para encontrar datos del mismo periodo.
3. Comprueba con una prueba adecuada si los usuarios siguen experimentando el problema.
