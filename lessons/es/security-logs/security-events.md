---
lesson_id: "security-events"
course_id: "security-logs"
lang: "es"
order_index: 1
title: "Eventos de seguridad"
description: "Aprende a distinguir un evento de seguridad, el registro que lo describe y una alerta que pide revisarlo."
meta_title: "Eventos de seguridad - Registros de seguridad"
meta_description: "Lee un registro breve de seguridad de Linux, compáralo con una alerta y decide qué comprobar si faltan datos."
meta_keywords: "eventos de seguridad, registros de seguridad, entradas de registro, alertas, registros de Linux"
---

Un servidor informa de un inicio de sesión fallido. ¿Qué ocurrió? ¿Qué puedes deducir? Empieza por separar lo que registró el equipo de las conclusiones que saques.

## Eventos y entradas de registro

Un **evento** es algo que sucedió, como la denegación de un intento de inicio de sesión. Una **entrada de registro** guarda una descripción del evento. Un **registro** reúne entradas. Los ejemplos del curso usan entradas simuladas con nombres de campo uniformes para que practiques su lectura. Las herramientas reales pueden usar otros nombres y guardar los registros de distintas maneras.

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

Esta entrada informa de un intento de inicio de sesión remoto rechazado para la cuenta `alex`. Puedes leer la entrada guardada después del intento. En otras lecciones verás cómo comparar las marcas de tiempo de fuentes diferentes.

![Terminal de LabEx con un registro simulado de inicio de sesión SSH rechazado para alex en web-01](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

La terminal de LabEx muestra el mismo registro simulado a partir de un archivo de texto.

:::single-choice{#security-events-event-versus-record} ¿Qué parte del ejemplo es el evento en sí?

::option[La línea guardada que describe el rechazo.]{#security-events-event-line explanation="La línea es la entrada que puedes leer una vez que ha ocurrido el evento."}
::option[La revisión posterior de la línea guardada.]{#security-events-event-review explanation="Leer la línea es una acción posterior. El evento que describe es el rechazo del intento de inicio de sesión."}
::option[El intento de inicio de sesión fue rechazado.]{#security-events-event-attempt .correct explanation="El rechazo ocurrió en el servidor. La línea deja constancia de lo que sucedió."}
:::

## Leer los campos

Un **campo** contiene un dato de la entrada. En estos ejemplos, `t` indica la hora registrada, `host` identifica el equipo donde ocurrió el evento y `source` indica la herramienta que lo notificó. `account` contiene la cuenta y `login` indica el resultado del intento de inicio de sesión.

:::single-choice{#security-events-field-host} Quieres saber qué equipo registró el rechazo del inicio de sesión. ¿Qué valor lo identifica?

::option[`alex`, del campo account.]{#security-events-field-host-account explanation="El campo account indica la cuenta del intento de inicio de sesión."}
::option[`web-01`, del campo host.]{#security-events-field-host-web .correct explanation="El campo host identifica el equipo en el que ocurrió el evento."}
::option[`ssh`, del campo source.]{#security-events-field-host-tool explanation="El campo source indica qué herramienta informó del evento."}
:::

## Alertas y reglas

Una **alerta** llama la atención sobre algo que puede requerir una revisión. Una regla de monitorización puede generar una alerta cuando detecta tres intentos rechazados para la misma cuenta en el mismo equipo en un plazo de cinco minutos. La regla agrupa las entradas por cuenta, equipo y hora. La alerta indica que se cumplieron sus condiciones. Quizá alguien solo escribió mal la contraseña varias veces.

:::single-choice{#security-events-alert-interpretation} La regla avisa de tres fallos de alex en web-01. ¿Qué indica la alerta?

::option[Los fallos registrados cumplieron las condiciones de la regla.]{#security-events-alert-condition .correct explanation="La alerta señala un patrón que merece atención. La regla no identifica quién lo provocó."}
::option[Tres personas distintas intentaron iniciar sesión.]{#security-events-alert-people explanation="Los tres intentos pueden ser de una sola persona o de varias. La regla cuenta entradas."}
::option[Alguien logró iniciar sesión después de tres intentos.]{#security-events-alert-success explanation="La regla cuenta los intentos rechazados. No indica si hubo un inicio de sesión posterior."}
:::

## Elegir qué comprobar después

Si quieres saber si `alex` inició sesión más tarde, busca en `web-01` el resultado de los intentos posteriores a los fallos. Comprueba qué periodo cubren los registros antes de sacar conclusiones. Una exportación, es decir, una copia de las entradas seleccionadas, puede terminar antes del periodo que necesitas.

:::single-choice{#security-events-next-record} La exportación termina a las 09:00. Quieres comprobar si hubo un inicio de sesión correcto a las 09:05. ¿Qué debes buscar?

::option[La misma exportación ordenada de la entrada más reciente a la más antigua.]{#security-events-next-sort explanation="Ordenar cambia la secuencia. No añade entradas posteriores a las 09:00."}
::option[Registros de inicio de sesión de web-01 que incluyan las 09:05.]{#security-events-next-window .correct explanation="Necesitas la fuente pertinente y un intervalo que abarque el evento que buscas."}
::option[Otro recuento de los fallos anteriores a las 09:00.]{#security-events-next-count explanation="Ese recuento describe otro resultado de un periodo anterior."}
:::

## Resumen

Ya puedes leer un registro de seguridad y elegir qué comprobar tras una alerta.

1. Distinguir un evento de la línea que lo registra.
2. Encontrar la cuenta, el equipo y el resultado en un ejemplo.
3. Usar la regla de una alerta para entender qué se observó.
4. Comprobar si la fuente y el intervalo de tiempo permiten responder a tu pregunta.
