---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "es"
order_index: 4
title: "Registros de sesiones"
description: "Aprende a emparejar registros de apertura y cierre y a saber qué sesiones puede describir un extracto."
meta_title: "Registros de sesiones - Registros de seguridad"
meta_description: "Lee registros de sesiones de Linux, relaciona los eventos de apertura y cierre y comprueba qué hacer cuando falta un cierre."
meta_keywords: "registros de sesiones Linux, apertura de sesión, cierre de sesión, identificador de sesión, conservación de registros"
---

La comprobación de inicio de sesión confirma que alguien pudo autenticarse con una cuenta. Una **sesión** es el periodo de actividad que empieza tras el inicio de sesión y termina al cerrar la sesión o desconectarse. Si se registraron ambos eventos, puedes saber cuándo comenzó y cuándo acabó.

## Leer un registro de apertura

El sistema puede asignar un **identificador de sesión** para distinguir cada sesión en un equipo. Estas líneas simuladas muestran dos aperturas para la misma cuenta en `web-01`. Todas las horas de esta lección están en la misma zona horaria.

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

La primera línea indica que empezó la sesión 42. La segunda registra otra sesión, la 43, en el mismo equipo.

:::single-choice{#security-session-records-two-openings} ¿Qué afirmación respaldan las dos aperturas?

::option[La primera sesión terminó cuando comenzó la segunda.]{#security-session-records-open-ended explanation="La segunda apertura indica que comenzó otra sesión. No da la hora de cierre de la primera."}
::option[Dos cuentas distintas iniciaron sesión en el equipo.]{#security-session-records-open-accounts explanation="Las dos líneas indican la misma cuenta. El campo de sesión distingue los dos periodos de actividad."}
::option[La misma cuenta abrió dos sesiones diferentes.]{#security-session-records-open-two .correct explanation="Las dos líneas dicen alex y cada sesión tiene su propio identificador en web-01."}
:::

## Emparejar una apertura con un cierre

Lee juntos el nombre del equipo y el identificador de sesión antes de relacionar dos registros. Compara la línea de cierre con las dos aperturas.

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

En `web-01`, hay seis minutos entre la apertura y el cierre de la sesión 42. El par muestra el inicio y el final registrados. No enumera las acciones realizadas entre ambos.

![Terminal de LabEx con las aperturas simuladas de las sesiones 42 y 43 y el cierre de la sesión 42](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

En esta vista aparecen juntos los registros simulados de apertura y cierre.

:::single-choice{#security-session-records-pair-ids} Si la línea de cierre indicara `session=43` y el equipo y la hora no cambiaran, ¿cuándo habría empezado esa sesión?

::option[A las 09:14:05.]{#security-session-records-pair-forty-two explanation="Esa apertura corresponde a la misma cuenta, pero pertenece a la sesión 42."}
::option[A las 09:17:00.]{#security-session-records-pair-forty-three .correct explanation="Al combinar web-01 con la sesión 43, encuentras la segunda apertura, que se produjo a las 09:17:00."}
::option[A las 09:20:05.]{#security-session-records-pair-end-time explanation="Esa es la hora de cierre registrada. La hora de inicio aparece en la apertura correspondiente."}
:::

## Investigar un cierre que falta

Vuelve al registro original del cierre de la sesión 42. El extracto termina a las 09:21 y sigue sin mostrar un cierre para la sesión 43. Tal vez aún estuviera activa al final del extracto. También es posible que el cierre quede fuera del periodo disponible o que no se haya guardado en esta fuente. El **periodo de conservación** indica cuánto tiempo se guarda una entrada y se puede consultar.

:::single-choice{#security-session-records-missing-close} ¿Qué puedes afirmar sobre la sesión 43 basándote solo en el extracto?

::option[Seguía activa al final del extracto.]{#security-session-records-missing-active explanation="Es posible, pero la falta de un cierre no basta para determinar su estado real."}
::option[El extracto no contiene la hora de cierre de esa sesión.]{#security-session-records-missing-unknown .correct explanation="Eso describe los datos disponibles. Una fuente posterior o distinta puede aportar la hora."}
::option[Se cerró al mismo tiempo que la sesión 42.]{#security-session-records-missing-together explanation="El cierre registrado es de la sesión 42. Aquí no hay uno que corresponda a la 43."}
:::

## Elegir la fuente según la pregunta

Si quieres averiguar a qué hora se cerró, busca un cierre correspondiente en un extracto posterior del mismo equipo. Si necesitas saber si la sesión está activa ahora, consulta la lista actual de sesiones de ese equipo. Un registro guardado y una lista actual responden preguntas sobre momentos distintos.

:::single-choice{#security-session-records-current-status} Necesitas saber si la sesión 43 está activa ahora. ¿Qué fuente es más útil?

::option[Una lista actual de sesiones de web-01.]{#security-session-records-current-list .correct explanation="La lista actual muestra las sesiones que el equipo considera activas en este momento."}
::option[Una copia antigua del registro de apertura.]{#security-session-records-current-opening explanation="Muestra que la sesión empezó. No indica si sigue activa."}
::option[Un registro de cierre de la sesión 42 en web-01.]{#security-session-records-current-other explanation="Un cierre de otra sesión no responde la pregunta sobre la 43."}
:::

## Resumen

Ya puedes usar registros de sesiones para describir el inicio y el final observados.

1. Identificar una apertura, su equipo y su identificador de sesión.
2. Emparejar el cierre con la apertura correspondiente.
3. Explicar qué queda por saber cuando falta un cierre.
4. Elegir entre registros históricos y una lista actual de sesiones.
