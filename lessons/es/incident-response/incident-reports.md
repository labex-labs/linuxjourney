---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "es"
order_index: 6
title: "Informes de incidentes"
description: "Aprende a redactar una actualización breve sobre un incidente que recoja las pruebas observadas y las preguntas pendientes."
meta_title: "Informes de incidentes - Respuesta a incidentes"
meta_description: "Aprende a redactar una actualización breve sobre un incidente que recoja las pruebas observadas y las preguntas pendientes."
meta_keywords: "informes de incidentes, respuesta a incidentes, ciberseguridad, Linux Journey"
---

Un informe de incidente breve ayuda a otra persona a hacerse cargo sin reconstruir toda la investigación. Incluye el servicio afectado, algunas observaciones con sus horas y la acción siguiente.

## Comunicar las observaciones

Estos son tres registros simulados del incidente en el servicio.

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

Los registros describen un cambio, un fallo y una comprobación que salió bien tras la recuperación. Incluye la ruta afectada y la hora. Conserva los detalles de lo que se probó.

:::single-choice{#incident-reports-report-claim} ¿Qué afirmación puedes hacer directamente a partir de los registros?

::option[La comprobación de la página de inicio falló a las 09:22 y salió bien tras la reversión.]{#incident-reports-report-claim-b .correct explanation="Eso resume los resultados observados y su orden."}
::option[La versión 3 estropeó la base de datos con seguridad.]{#incident-reports-report-claim-a explanation="Los registros no muestran el mecanismo que causó el fallo."}
::option[Todos los usuarios se vieron afectados durante todo el intervalo.]{#incident-reports-report-claim-c explanation="Los resultados disponibles no abarcan todas las peticiones."}
:::

![Pruebas simuladas de un incidente que muestran un cambio en producción, un 503 y una comprobación de recuperación correcta](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## Explicar qué queda por aclarar

Si una petición funciona después de revertir un despliegue, conviene investigar ese despliegue. Deja abierta la cuestión de la causa hasta contar con pruebas que la respalden. Por ejemplo, el equipo de mantenimiento puede comparar los registros de servicio de ambas versiones en el intervalo de la petición fallida.

:::single-choice{#incident-reports-uncertainty-statement} ¿Qué frase corresponde a una cuestión pendiente?

::option[No hay nada que merezca la pena investigar.]{#incident-reports-uncertainty-statement-b explanation="Los registros de la versión y del error permiten acotar la siguiente comprobación."}
::option[El servicio dejó de estar disponible para siempre.]{#incident-reports-uncertainty-statement-c explanation="El resultado posterior contradice esa afirmación para la petición de prueba."}
::option[Aún no se conoce la causa del 503.]{#incident-reports-uncertainty-statement-a .correct explanation="Las pruebas muestran un fallo y una comprobación de recuperación. La causa aún requiere pruebas."}
:::

## Asignar una tarea a quien continúe la investigación

Indica quién puede dar el siguiente paso, qué registros debe buscar y qué resultado permitiría responder a la pregunta pendiente. Evita incluir secretos y datos personales en actualizaciones de amplia difusión. Un informe breve puede enlazar a las pruebas protegidas para que las consulte el personal autorizado.

:::single-choice{#incident-reports-useful-handoff} ¿Qué acción de seguimiento encaja mejor con este caso?

::option[Pedir a alguien una captura genérica sin especificar la hora ni el servicio.]{#incident-reports-useful-handoff-a explanation="Eso no indica qué pruebas buscar para aclarar el fallo."}
::option[Pedir al responsable del servicio que revise los registros de la versión 3 durante el intervalo de la petición fallida a la página de inicio.]{#incident-reports-useful-handoff-c .correct explanation="Así se asignan una fuente y un intervalo concretos a la pregunta que queda abierta."}
::option[Pedir al responsable que se limite a repetir la comprobación de la versión 2 que ya salió bien.]{#incident-reports-useful-handoff-b explanation="Eso puede volver a confirmar la recuperación. El fallo anterior con la versión 3 seguirá sin explicación."}
:::

## Registrar el alcance de la recuperación

Puede que el informe deba recoger tanto una comprobación de recuperación como una estimación de impacto aún pendiente. Si la página de inicio supera la prueba después de la reversión, hay pruebas de que se recuperó la ruta probada. Para estimar cuántos visitantes resultaron afectados, hacen falta recuentos de peticiones u otros datos adecuados del intervalo del fallo.

:::single-choice{#incident-reports-final-application} ¿Qué mensaje para quien retome el caso describe con precisión ambos tipos de datos?

::option[El servicio se recuperó para todos los visitantes porque una petición devolvió 200.]{#incident-reports-final-application-b explanation="La petición correcta solo verifica la ruta y la hora que se probaron."}
::option[Hay que quitar del informe la comprobación fallida porque la de recuperación salió bien.]{#incident-reports-final-application-c explanation="El fallo anterior forma parte de las pruebas del incidente."}
::option[La comprobación de la página de inicio salió bien tras la reversión y aún se desconoce el total de peticiones afectadas.]{#incident-reports-final-application-a .correct explanation="El informe distingue entre la comprobación de recuperación y el recuento que los registros disponibles no permiten obtener."}
:::

Si quieres un ejercicio más largo después de trabajar con pruebas de paquetes y de equipos, consulta [Repaso de los fundamentos de SOC](https://labex.io/courses/project-soc-foundations-review).

## Resumen

Ya puedes pasar el seguimiento de un incidente a otra persona con los hechos, las dudas y una acción concreta.

1. Indica la ruta afectada y la cronología observada.
2. Distingue una causa sospechada de las pruebas confirmadas.
3. Asigna una tarea de seguimiento que especifique la fuente y el intervalo.
