---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "es"
order_index: 2
title: "Eventos que activan un flujo"
description: "Aprende a predecir cuándo se ejecuta un flujo de GitHub Actions a partir de sus eventos y filtros de rama."
meta_title: "Eventos que activan un flujo - Integración continua"
meta_description: "Aprende a predecir cuándo se ejecuta un flujo de GitHub Actions a partir de sus eventos y filtros de rama."
meta_keywords: "eventos de flujo de trabajo, filtros de rama, integración continua, DevOps, Linux Journey"
---

Un flujo de trabajo se inicia cuando ocurre algo. En GitHub Actions, la sección `on` indica qué eventos pueden activarlo. Un **evento** puede ser un envío a una rama, un cambio en una pull request u otra acción compatible.

## Comprobar un envío

Lee este fragmento de un flujo de trabajo. En YAML, la sangría indica que `branches` es un ajuste de `push`.

```yaml
on:
  push:
    branches:
      - main
```

El flujo se ejecuta al enviar un commit a la rama `main`, siempre que el flujo esté habilitado y se cumplan los demás requisitos. Crear un commit en el terminal local no lo envía a GitHub. Este fragmento espera a que lo envíes.

:::single-choice{#ci-workflow-triggers-push-filter} ¿Qué acción coincide con este evento push?

::option[Crear un commit local en main.]{#ci-workflow-triggers-push-filter-a explanation="El flujo espera un evento en el repositorio de GitHub."}
::option[Enviar un commit a una rama llamada draft.]{#ci-workflow-triggers-push-filter-b explanation="El filtro de ramas selecciona main."}
::option[Enviar el commit a main.]{#ci-workflow-triggers-push-filter-c .correct explanation="El evento coincide con push y con el filtro de rama."}
:::

## Comprobar una pull request

Otro evento permite comprobar los cambios propuestos antes de fusionarlos. En este fragmento, el filtro de rama se aplica a la rama de destino de la pull request.

```yaml
on:
  pull_request:
    branches:
      - main
```

Una propuesta de `health-page` a `main` coincide con el filtro. Con los tipos de actividad predeterminados, el flujo puede ejecutarse cuando se abre la solicitud o cuando se envía otro commit a la rama de origen.

:::single-choice{#ci-workflow-triggers-pr-target} Una pull request propone integrar notes en main. ¿Qué nombre se usa para este filtro de rama?

::option[Notes, la rama de origen.]{#ci-workflow-triggers-pr-target-b explanation="Notes contiene los cambios propuestos."}
::option[Main, la rama de destino.]{#ci-workflow-triggers-pr-target-a .correct explanation="El filtro de rama de la pull request se aplica a la rama base, la que recibe los cambios."}
::option[El nombre del archivo que modifica la propuesta.]{#ci-workflow-triggers-pr-target-c explanation="Este fragmento filtra por nombre de rama."}
:::

## Leer más de un evento de activación

Un archivo puede incluir ambos eventos bajo la misma clave `on`. Una ejecución iniciada por una pull request puede comprobar la integración propuesta. Cuando una fusión actualiza `main`, una ejecución iniciada por un push puede comprobar el nuevo estado de esa rama. Los resultados corresponden al evento y a la revisión que indica cada ejecución.

:::single-choice{#ci-workflow-triggers-after-merge} Un flujo tiene los dos eventos de los ejemplos. Una fusión actualiza main. ¿Qué evento coincide con esa actualización?

::option[Un push a main.]{#ci-workflow-triggers-after-merge-b .correct explanation="La rama de destino se actualizó y coincide con el filtro de push."}
::option[La apertura de una pull request en otra rama.]{#ci-workflow-triggers-after-merge-a explanation="La acción descrita es una actualización de main después de fusionar los cambios."}
::option[Un commit local sin actualización remota.]{#ci-workflow-triggers-after-merge-c explanation="En este caso, main ya cambió en GitHub."}
:::

## Resumen

Ya puedes relacionar el evento de un repositorio con el inicio de un flujo de trabajo.

1. Lee un evento push y su filtro de rama.
2. Identifica la rama de destino a la que se aplica el filtro de una pull request.
3. Asocia el resultado del flujo con el evento que lo inició.
