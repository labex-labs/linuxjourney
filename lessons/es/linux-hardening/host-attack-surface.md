---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "es"
order_index: 1
title: "Superficie de ataque"
description: "Aprende a identificar qué debe exponer un equipo Linux y qué vías de acceso conviene revisar."
meta_title: "Superficie de ataque - Endurecimiento de Linux"
meta_description: "Aprende a identificar qué debe exponer un equipo Linux y qué vías de acceso conviene revisar."
meta_keywords: "superficie de ataque, endurecimiento de Linux, ciberseguridad, Linux Journey"
---

Un equipo Linux puede alojar una página web pública, ofrecer acceso para mantenimiento y ejecutar servicios en segundo plano. Empieza por anotar qué hace cada servicio y quién necesita acceder a él. Así podrás detectar accesos que carecen de un propósito claro.

## Enumerar los accesos previstos

Un inventario sencillo vincula cada recurso con las personas o los programas que lo necesitan. Este es el inventario de un equipo de prácticas.

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

Una **vía de acceso** es el medio por el que un usuario o un programa llega a un recurso. El conjunto de interfaces accesibles a través de las cuales alguien podría afectar al sistema forma parte de su **superficie de ataque**.

:::single-choice{#host-attack-surface-intended-audience} ¿Qué recurso de este inventario necesita acceso desde una red pública?

::option[El acceso SSH para mantenimiento.]{#host-attack-surface-intended-audience-b explanation="Está destinado al equipo de operaciones."}
::option[La página de inicio pública.]{#host-attack-surface-intended-audience-a .correct explanation="Entre sus destinatarios están los visitantes externos al equipo."}
::option[El panel de vista previa.]{#host-attack-surface-intended-audience-c explanation="Su uso previsto es local al equipo."}
:::

## Comparar el acceso previsto con el observado

Supón que se puede acceder al panel de vista previa por la red y el inventario aún dice que el acceso es solo local. Consulta a la persona responsable y comprueba la vía de acceso real antes de cambiarla. Puede ser necesario mantener un servicio en ejecución aunque no necesite aceptar peticiones remotas.

:::single-choice{#host-attack-surface-mismatch} ¿Qué observación merece revisarse según la política descrita?

::option[Un visitante puede acceder al panel de vista previa.]{#host-attack-surface-mismatch-b .correct explanation="Eso abre una vía de acceso al panel para personas ajenas a su público previsto."}
::option[Un visitante puede cargar la página de inicio.]{#host-attack-surface-mismatch-a explanation="Ese es el uso previsto de la página."}
::option[El personal puede abrir la vista previa desde el propio equipo.]{#host-attack-surface-mismatch-c explanation="El acceso local coincide con la necesidad indicada."}
:::

## Priorizar las comprobaciones

Empieza por los accesos innecesarios que puedan tener consecuencias importantes. En un ejemplo de prácticas, un panel de vista previa que permite cambiar el sitio tiene más prioridad que un servicio sin uso y sin datos importantes. Anota quién necesita acceso, qué exposición observaste y con qué prueba confirmarías que la restricción funciona sin interrumpir el acceso legítimo.

:::single-choice{#host-attack-surface-priority-check} Tras cambiar el acceso a la vista previa, ¿qué dos observaciones confirmarían que la restricción cumplió su objetivo?

::option[El panel sigue aceptando una petición local.]{#host-attack-surface-priority-check-a explanation="Eso confirma el acceso necesario y deja sin probar la vía remota que se quería cerrar."}
::option[El equipo se reinició y usa el mismo nombre de anfitrión.]{#host-attack-surface-priority-check-b explanation="El estado del equipo no indica si se cumple la política."}
::option[El personal aún puede acceder de forma local y la vía remota no prevista está cerrada.]{#host-attack-surface-priority-check-c .correct explanation="Las dos comprobaciones validan el acceso necesario y la restricción."}
:::

## Resumen

Ya puedes identificar qué vías de acceso conviene revisar para reforzar la seguridad.

1. Describe el recurso y quién necesita acceder a él.
2. Compara el acceso previsto con el observado.
3. Verifica la protección y el acceso legítimo después de cada cambio.
