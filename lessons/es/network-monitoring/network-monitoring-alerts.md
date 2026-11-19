---
lesson_id: "network-monitoring-alerts"
course_id: "network-monitoring"
lang: "es"
order_index: 6
title: "Alertas de red"
description: "Aprende a relacionar una alerta de red con los datos que necesitas para decidir cómo responder."
meta_title: "Alertas de red - Monitorización de redes"
meta_description: "Aprende a relacionar una alerta de red con los datos que necesitas para decidir cómo responder."
meta_keywords: "alertas de red, monitorización de redes, ciberseguridad, Linux Journey"
---

Una alerta de red indica que se cumplió una condición de monitorización. Lee la condición y revisa de dónde vienen los datos antes de decidir qué ocurrió. Las alertas pueden señalar tráfico inesperado, fallos repetidos o falta de datos.

## Entender qué abarca la alerta

La alerta simulada de abajo se basa en registros DNS. Agrupa los fallos por cliente durante un intervalo de cinco minutos.

```text
Window: 09:20–09:25 UTC
Client: 192.0.2.10
Condition: at least 10 failed name lookups
Observed: 12 failures
```

La alerta te da un motivo para examinar las consultas y sus resultados. Queda por averiguar qué programa hizo las consultas.

:::single-choice{#network-monitoring-alerts-alert-scope} ¿Qué observó directamente la alerta?

::option[Doce consultas fallidas para el cliente indicado en ese intervalo.]{#network-monitoring-alerts-alert-scope-b .correct explanation="Ese es el recuento y el alcance que indica la alerta."}
::option[Una pérdida de datos confirmada.]{#network-monitoring-alerts-alert-scope-a explanation="La regla cuenta las consultas de nombres que fallaron."}
::option[Doce clientes distintos.]{#network-monitoring-alerts-alert-scope-c explanation="La alerta agrupa los registros de una sola dirección de cliente."}
:::

## Buscar un registro relacionado en el equipo

Supón que la mayoría de los fallos correspondían a `preview.example`. Un registro de servicio del cliente podría mostrar que una configuración antigua provocó varios reintentos. Busca registros de esas horas del programa que esperas que haga las peticiones. Comprueba qué etiqueta usa el sistema de monitorización para identificar el equipo antes de atribuirle la actividad.

:::single-choice{#network-monitoring-alerts-evidence-choice} ¿Qué registro ayudaría a comprobar si un servicio estaba repitiendo la consulta?

::option[Una visita posterior a la página pública de otro equipo.]{#network-monitoring-alerts-evidence-choice-b explanation="El destino y la hora no coinciden con el patrón investigado."}
::option[Una lista de aplicaciones instaladas sin horas de actividad.]{#network-monitoring-alerts-evidence-choice-c explanation="El software instalado no indica por sí solo qué programa hizo la consulta."}
::option[Un registro del servicio que indique la consulta fallida en el intervalo de la alerta.]{#network-monitoring-alerts-evidence-choice-a .correct explanation="Puede vincular el patrón de peticiones con ese programa."}
:::

## Documentar el siguiente paso

Si el registro del servicio coincide, anota el motivo y verifica una consulta representativa después de corregir la configuración autorizada. Si faltan pruebas, indica cuáles. Conserva juntos la alerta, el registro que la respalda y el resultado de la comprobación.

:::single-choice{#network-monitoring-alerts-uncertainty} Tienes la alerta DNS, pero no los registros correspondientes del equipo. ¿Qué debes informar?

::option[Se identificó el programa exacto.]{#network-monitoring-alerts-uncertainty-a explanation="Los datos de DNS por sí solos no identificaron el proceso."}
::option[Se ha confirmado el patrón de consultas y aún se desconoce qué programa las hizo.]{#network-monitoring-alerts-uncertainty-c .correct explanation="Así se conserva la observación y se indica qué falta por averiguar."}
::option[La alerta no aporta ningún dato.]{#network-monitoring-alerts-uncertainty-b explanation="La alerta sí describe la condición que observó el resolvedor."}
:::

## Comprobar un patrón de reintentos previsto

Supón que un equipo programó una tarea que resuelve repetidamente un nombre de equipo de prueba. Compara la hora prevista, los nombres de los registros DNS y el registro de la propia tarea. Si coinciden varios campos, esa explicación gana peso. Deja pendientes de revisión los fallos que no coincidan.

:::single-choice{#network-monitoring-alerts-final-application} ¿Cuál sería la mejor prueba de que la tarea programada explica el patrón?

::option[La alerta procede de un equipo que ejecuta otras tareas programadas.]{#network-monitoring-alerts-final-application-c explanation="Saber qué equipo es no basta para saber qué programa hizo esas consultas."}
::option[El registro de la tarea indica el mismo nombre de equipo y reintentos durante el intervalo de la alerta.]{#network-monitoring-alerts-final-application-a .correct explanation="La coincidencia de nombre y hora permite relacionar el patrón observado con la tarea conocida."}
::option[La tarea estaba programada para algún momento de ese día.]{#network-monitoring-alerts-final-application-b explanation="Un horario aproximado deja sin comprobar el intervalo y los nombres consultados."}
:::

## Resumen

Ya puedes decidir qué investigar a partir de una alerta de red.

1. Identifica la regla de detección y su alcance.
2. Elige un registro relacionado para comprobar una explicación.
3. Documenta lo observado y lo que sigue sin aclararse.
