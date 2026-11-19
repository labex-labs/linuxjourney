---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "es"
order_index: 1
title: "Registros de red"
description: "Aprende a elegir un registro de red que responda a una pregunta concreta de monitorización."
meta_title: "Registros de red - Monitorización de redes"
meta_description: "Aprende a elegir un registro de red que responda a una pregunta concreta de monitorización."
meta_keywords: "registros de red, monitorización de redes, ciberseguridad, Linux Journey"
---

Una observación de red describe lo que una herramienta pudo ver desde un punto determinado. Empieza por preguntarte qué necesitas averiguar. Cada fuente muestra aspectos distintos de la misma actividad.

## Elegir un tipo de registro

Un **registro de flujo** resume la comunicación entre dos extremos de la red. Un **registro DNS** muestra consultas de nombres que observó un resolvedor. Una **captura de paquetes** guarda copias de los paquetes que pasan por el punto de captura. Un extremo es uno de los lados de una comunicación y suele identificarse por una dirección y un puerto.

:::single-choice{#network-monitoring-records-choose-dns} Quieres saber qué respuesta dio un resolvedor para site.example. ¿Qué fuente es la más adecuada?

::option[Un recuento de los procesos que atienden peticiones web.]{#network-monitoring-records-choose-dns-b explanation="Ese recuento no tiene relación con la consulta."}
::option[Un registro DNS de ese resolvedor.]{#network-monitoring-records-choose-dns-a .correct explanation="El resolvedor puede registrar la consulta que atendió y su respuesta."}
::option[Un resumen de flujo que muestre solo el volumen de tráfico.]{#network-monitoring-records-choose-dns-c explanation="Un resumen de flujo puede omitir la consulta DNS y su respuesta."}
:::

## Identificar el punto de observación

Una captura hecha en un portátil incluye los paquetes visibles desde la interfaz seleccionada. El registro del servidor recoge lo que llegó hasta él o lo que el servidor pudo registrar. Por ejemplo, una petición de un usuario puede fallar antes de llegar al servidor. Usa una fuente cuya ubicación te permita responder a la pregunta.

:::single-choice{#network-monitoring-records-capture-scope} No encuentras una petición en una captura hecha en otro equipo. ¿Qué debes comprobar antes de sacar conclusiones?

::option[Si la interfaz de captura podía observar la ruta y el intervalo que te interesan.]{#network-monitoring-records-capture-scope-b .correct explanation="La ausencia de un paquete puede deberse a los límites de visibilidad de ese punto de observación."}
::option[Si la captura incluye paquetes que no tienen relación con la petición.]{#network-monitoring-records-capture-scope-a explanation="Ver otro tráfico confirma que se recogieron datos. Aún queda por averiguar si la captura cubría la ruta y el intervalo pertinentes."}
::option[Si otro equipo estaba capturando al mismo tiempo.]{#network-monitoring-records-capture-scope-c explanation="Una captura simultánea en otro equipo no establece qué podía ver esta interfaz."}
:::

## Usar una muestra pequeña

Las capturas de paquetes pueden contener información que nadie pretendía compartir. Para aprender a leer paquetes, usa una captura preparada con tráfico de prácticas inofensivo. Cuando compartas un pequeño fragmento, indica el intervalo revisado y el filtro para que quien lo lea entienda los límites de la muestra.

:::single-choice{#network-monitoring-records-choosing-evidence} ¿Qué muestra sirve mejor para enseñar a identificar una respuesta DNS?

::option[Una captura extensa de tráfico del personal que no guarda relación con el ejercicio.]{#network-monitoring-records-choosing-evidence-a explanation="Añade datos innecesarios y puede exponer información privada."}
::option[Un resumen sin campos que describan la consulta.]{#network-monitoring-records-choosing-evidence-b explanation="El estudiante se quedaría sin los datos necesarios para interpretar la consulta."}
::option[Una captura pequeña y preparada que contenga la consulta y la respuesta de prácticas.]{#network-monitoring-records-choosing-evidence-c .correct explanation="Incluye el intercambio necesario para responder a la pregunta."}
:::

## Resumen

Ya puedes elegir un registro de red y explicar qué pudo observar.

1. Distingue los resúmenes de flujo, los registros DNS y las capturas de paquetes.
2. Relaciona el punto de observación con la ruta de red.
3. Usa una muestra acotada y adecuada para la revisión.
