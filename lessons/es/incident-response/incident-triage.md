---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "es"
order_index: 1
title: "Triaje de incidentes"
description: "Aprende a acotar la primera investigación a partir de un informe inicial de incidente."
meta_title: "Triaje de incidentes - Respuesta a incidentes"
meta_description: "Aprende a acotar la primera investigación a partir de un informe inicial de incidente."
meta_keywords: "triaje de incidentes, respuesta a incidentes, ciberseguridad, Linux Journey"
---

Un informe inicial puede indicar que falló una página o que se activó una alerta. El **triaje** consiste en decidir qué requiere atención primero. Anota el servicio afectado, la hora y el comportamiento observado antes de decidir cómo responder.

## Leer el informe

Una persona de tu equipo redacta este informe simulado.

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

El informe identifica dos rutas y describe un resultado distinto para cada una. Confirma el resultado de la página de inicio pública y anota la hora y la dirección que comprobaste.

:::single-choice{#incident-triage-affected-service} ¿En qué síntoma debe centrarse la primera comprobación?

::option[La vista previa del personal devuelve 503.]{#incident-triage-affected-service-b explanation="El informe indica que esa vista previa seguía cargando."}
::option[La página de inicio pública devuelve 503.]{#incident-triage-affected-service-a .correct explanation="Esa es la ruta afectada que menciona el informe."}
::option[Falta una página en otro equipo ajeno al incidente.]{#incident-triage-affected-service-c explanation="Esa ruta queda fuera del alcance del informe."}
:::

## Estimar el impacto

Comprueba cuántos usuarios o peticiones se ven afectados y si el servicio sigue siendo utilizable. Averigua si el problema sigue ocurriendo. Señala que las cifras inciertas son estimaciones hasta que tengas mejores pruebas. Usa el plan de respuesta para decidir a quién avisar.

:::single-choice{#incident-triage-triage-scope} ¿Qué observación ayuda a decidir si el problema sigue siendo urgente?

::option[Una comprobación actual de la ruta que falla y el resultado de peticiones recientes.]{#incident-triage-triage-scope-b .correct explanation="Así puedes ver si el síntoma persiste y qué alcance tiene."}
::option[La antigüedad del primer commit del repositorio.]{#incident-triage-triage-scope-a explanation="Ese dato no muestra el efecto actual."}
::option[Solo la etiqueta de gravedad del informe original.]{#incident-triage-triage-scope-c explanation="La etiqueta original aporta contexto. El impacto actual ayuda a decidir si el problema sigue siendo urgente."}
:::

## Elegir una primera acción

Si la petición actual también falla, conserva el resultado y revisa los cambios recientes del servicio y los registros del intervalo afectado. Una ruta alternativa que sigue funcionando ayuda a acotar el problema. Evita dar por confirmada la primera causa que parezca plausible.

:::single-choice{#incident-triage-first-next-step} La ruta pública aún falla y la vista previa del personal sigue funcionando. ¿Qué debes revisar a continuación?

::option[Todos los proyectos de la empresa ajenos al incidente.]{#incident-triage-first-next-step-a explanation="El informe señala un servicio y un intervalo concretos."}
::option[Un error antiguo al azar de otra fecha.]{#incident-triage-first-next-step-b explanation="Empieza por las pruebas cercanas a la hora del fallo observado."}
::option[Los registros de la ruta pública durante el intervalo indicado.]{#incident-triage-first-next-step-c .correct explanation="Pueden ayudar a distinguir un problema de enrutamiento de un fallo del servicio."}
:::

## Resumen

Ya puedes preparar una primera respuesta centrada en el incidente que se ha comunicado.

1. Identifica la ruta afectada, la hora y el síntoma.
2. Comprueba el impacto actual en los usuarios.
3. Elige la siguiente fuente de pruebas para la ruta afectada.
