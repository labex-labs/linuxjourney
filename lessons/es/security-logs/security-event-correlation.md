---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "es"
order_index: 5
title: "Correlación de eventos"
description: "Aprende a relacionar registros de seguridad usando la hora, el equipo, la cuenta y la sesión."
meta_title: "Correlación de eventos - Registros de seguridad"
meta_description: "Compara registros de SSH y sudo, unifica sus marcas de tiempo y determina qué pruebas apuntan a una relación entre los eventos."
meta_keywords: "correlación de eventos, registros de seguridad, inicios de sesión SSH, eventos de sudo, marcas de tiempo"
---

Un registro dice que alguien inició sesión en un equipo. Otro muestra que se autorizó un comando. ¿Están relacionados? La **correlación de eventos** consiste en comparar registros para averiguar si describen actividades relacionadas.

## Leer dos registros

SSH permite iniciar sesión en otro equipo. Una vez dentro, se puede usar `sudo` para solicitar permiso para ejecutar un comando con otra cuenta. A continuación tienes dos registros simulados del mismo día. Usan los mismos nombres de campo para facilitar la práctica. Los registros reales pueden usar nombres distintos u omitir campos.

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

El campo `source` indica qué herramienta notificó el evento y `host` muestra en qué equipo sucedió. Los dos registros describen actividad con la cuenta `alex`. Para identificar a quien la usó, hacen falta más pruebas.

:::single-choice{#security-event-correlation-account-evidence} Una persona del equipo dice que Alex hizo personalmente la solicitud de sudo. ¿Qué demuestran los registros por ahora?

::option[Que Alex hizo personalmente la solicitud de sudo.]{#security-event-correlation-account-person explanation="El nombre de una cuenta por sí solo no identifica a la persona que la utilizó."}
::option[Que los registros muestran actividad de dos cuentas distintas.]{#security-event-correlation-account-different explanation="En ambos campos account aparece alex. Los valores distintos de source indican qué herramientas registraron la actividad."}
::option[Que ambos eventos mencionan la misma cuenta.]{#security-event-correlation-account-shared .correct explanation="Los dos registros indican alex. Hacen falta más pruebas para identificar a quien usó esa cuenta."}
:::

## Comparar las horas de los eventos

El campo `t` contiene la hora registrada. En el primero, `Z` indica UTC, una referencia común para comparar las horas. El segundo usa `+02:00`, dos horas por delante de UTC. Resta dos horas a `11:15:10` para obtener `09:15:10` UTC.

Ahora compara `09:14:02` con `09:15:10`. El inicio de sesión se registró primero. La cercanía en el tiempo no basta para saber si dos eventos corresponden al mismo inicio de sesión.

:::single-choice{#security-event-correlation-time-order} Otro día se registra un inicio a las `09:14Z` y una solicitud a las `11:13+02:00`. ¿Qué ocurrió primero?

::option[La solicitud ocurrió un minuto antes.]{#security-event-correlation-time-request-first .correct explanation="Al restar dos horas a la solicitud, obtienes las 09:13 UTC. El inicio fue a las 09:14 UTC."}
::option[El inicio de sesión ocurrió un minuto antes.]{#security-event-correlation-time-login-first explanation="La solicitud corresponde a las 09:13 UTC, un minuto antes del inicio de las 09:14 UTC."}
::option[El inicio de sesión ocurrió casi dos horas antes.]{#security-event-correlation-time-unadjusted explanation="Eso compara las horas tal como se muestran. Convierte ambas a UTC antes de ordenarlas."}
:::

## Comprobar el equipo y la sesión

Una **sesión** abarca la actividad desde el inicio de sesión hasta el cierre o la desconexión. En estos registros de práctica, la entrada de SSH incluye el identificador de la sesión abierta tras el inicio aceptado. Las dos fuentes usan el mismo identificador para ese inicio de sesión en el mismo equipo. Los dos primeros registros muestran `host=web-01` y `session=42`, lo que vincula el inicio y la solicitud con una sola sesión.

En estos ejemplos, el número de sesión es propio de cada equipo. La entrada siguiente tiene la misma cuenta y el mismo número de sesión, y aparece solo unos segundos más tarde.

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![Terminal de LabEx con registros simulados de web-01 y web-02 y una conversión a las 09:15:10 UTC](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

La terminal muestra los tres registros simulados y usa el comando `date` de Ubuntu para comprobar la conversión a UTC.

:::single-choice{#security-event-correlation-host-scope} ¿Qué relación tiene el tercer registro con la sesión SSH original?

::option[Pertenece a esa sesión por la coincidencia de la cuenta y la cercanía en el tiempo.]{#security-event-correlation-host-scope-account explanation="Dos equipos pueden registrar actividad con la misma cuenta en cuestión de segundos."}
::option[Pertenece a otra sesión porque el equipo es diferente.]{#security-event-correlation-host-scope-machine .correct explanation="La sesión 42 de web-02 es local a ese equipo. El inicio original ocurrió en web-01."}
::option[Pertenece a esa sesión porque coincide el número de sesión.]{#security-event-correlation-host-scope-session explanation="En este ejemplo, el número solo tiene sentido dentro de su equipo. Aquí los nombres de los equipos son distintos."}
:::

## Expresar lo que respaldan los registros

En `web-01` se aceptó el inicio de sesión y `sudo` autorizó un comando durante esa sesión. Eso es lo que demuestran los datos disponibles. Para saber cómo terminó el comando, busca un registro del resultado. Como una sesión puede contener varios comandos, relaciona el resultado con la solicitud concreta. Si no encuentras un registro que coincida, deja el resultado como desconocido.

:::single-choice{#security-event-correlation-completion-evidence} ¿Qué nuevo registro aclararía si ese comando terminó correctamente?

::option[El resultado de otro comando ejecutado en la misma sesión.]{#security-event-correlation-completion-other-command explanation="En una sesión pueden ejecutarse varios comandos. El resultado debe corresponder a la solicitud que investigas."}
::option[Una segunda entrada que indique que se autorizó la solicitud.]{#security-event-correlation-completion-permission explanation="Esto confirma que hubo permiso. Todavía falta un registro del resultado."}
::option[Un registro del resultado del comando de esa solicitud concreta.]{#security-event-correlation-completion-result .correct explanation="Un registro que coincida puede indicar cómo terminó el comando."}
:::

Para practicar cómo filtrar y comparar otros registros de autenticación y sudo, prueba el [análisis de registros del sistema](https://labex.io/tutorials/linux-system-log-analysis-656124).

## Resumen

Ya puedes usar varios registros de seguridad para llegar a una conclusión e indicar qué queda por verificar.

1. Identificar la cuenta que figura en un evento.
2. Convertir las marcas de tiempo a una misma zona antes de compararlas.
3. Usar el equipo y la sesión juntos para enlazar actividades.
4. Explicar qué respaldan los registros y buscar pruebas que respondan lo que queda pendiente.
