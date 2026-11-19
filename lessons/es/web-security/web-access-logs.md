---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "es"
order_index: 7
title: "Registros de acceso web"
description: "Aprende a usar los registros de acceso HTTP para averiguar qué devolvió un servicio sin exponer credenciales."
meta_title: "Registros de acceso web - Seguridad web"
meta_description: "Aprende a usar los registros de acceso HTTP para averiguar qué devolvió un servicio sin exponer credenciales."
meta_keywords: "registros de acceso web, seguridad web, ciberseguridad, Linux Journey"
---

Un servidor web puede guardar una entrada en el **registro de acceso** por cada petición. El registro puede incluir la hora, la ruta, el código de respuesta y el ID de petición. Usa solo los campos necesarios para responder a la pregunta que investigas.

## Interpretar el resultado de la petición

Este fragmento simulado identifica cada campo por su nombre. Las dos peticiones se enviaron a rutas distintas.

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

Un código `403` indica que el servicio rechazó la petición. Comprueba la ruta exacta y el ID de petición antes de comparar la respuesta con otro registro.

:::single-choice{#web-access-logs-log-result} ¿Qué petición debes seguir para investigar el rechazo?

::option[r31 en /health.]{#web-access-logs-log-result-a explanation="Esa fila muestra una comprobación de estado correcta."}
::option[r32 en /staff.]{#web-access-logs-log-result-b .correct explanation="El estado 403 corresponde al rechazo de este fragmento."}
::option[Ambas, como si fueran la misma petición.]{#web-access-logs-log-result-c explanation="Sus identificadores y rutas permiten distinguirlas."}
:::

## Buscar la decisión de acceso

El registro de acceso indica qué devolvió el servidor. Puede que no explique el motivo de una decisión de permisos. Si la aplicación también registra sus decisiones de autorización, busca una que coincida en ID de petición y hora. Así puedes saber qué regla se aplicó en este ejemplo.

:::single-choice{#web-access-logs-refusal-reason} La fila del registro de acceso indica 403. ¿Qué otro registro explicaría mejor el motivo?

::option[La decisión de permisos de la aplicación para r32.]{#web-access-logs-refusal-reason-a .correct explanation="El registro correspondiente puede indicar qué regla se aplicó."}
::option[Una respuesta correcta de otro sitio.]{#web-access-logs-refusal-reason-b explanation="Ese resultado no guarda relación con el rechazo."}
::option[Una petición anterior a la ruta de comprobación de estado.]{#web-access-logs-refusal-reason-c explanation="Registra otra operación con otro resultado."}
:::

## Mantener las credenciales fuera de los registros

Evita registrar valores que permitan usar la sesión de otra persona, como una cookie de sesión completa o un token de autorización. El ID de petición y el estado de respuesta siguen sirviendo para investigar problemas. Cuando compartas una muestra del registro, elimina los campos sensibles y conserva solo los datos necesarios para la investigación.

:::single-choice{#web-access-logs-safe-fields} ¿Qué dos datos ayudan a seguir la petición rechazada sin copiar credenciales?

::option[La cookie de sesión completa y la contraseña de la cuenta.]{#web-access-logs-safe-fields-a explanation="Ambos valores son sensibles y deben quedar fuera de los registros que se comparten."}
::option[El token de autorización y una ruta pública.]{#web-access-logs-safe-fields-b explanation="La ruta puede ser útil, pero el token es una credencial privada."}
::option[El ID de petición y el estado de su respuesta.]{#web-access-logs-safe-fields-c .correct explanation="Permiten comparar los registros pertinentes sin revelar un valor de sesión."}
:::

## Compartir un fragmento pequeño

Imagina que alguien necesita contexto para revisar una petición rechazada. Conserva la hora, el ID, el método, la ruta depurada y el estado si esos campos bastan. Algunas rutas incluyen datos privados en los parámetros de consulta. Revisa el fragmento antes de compartirlo.

:::single-choice{#web-access-logs-final-application} ¿Qué fragmento sirve mejor para esa revisión?

::option[La petición completa con todas sus cabeceras por defecto.]{#web-access-logs-final-application-b explanation="Las peticiones pueden contener credenciales o datos personales innecesarios."}
::option[Solo el código de estado, sin ningún identificador.]{#web-access-logs-final-application-c explanation="Puede ser difícil relacionar el código por sí solo con el registro de la decisión de acceso."}
::option[Una ruta depurada con la hora, el ID de petición y el estado de respuesta.]{#web-access-logs-final-application-a .correct explanation="Conserva los campos necesarios para relacionar los registros sin revelar valores de sesión."}
:::

## Resumen

Ya puedes interpretar un registro de acceso básico y conservar el contexto necesario de forma segura.

1. Relaciona el ID de petición, la ruta y la respuesta.
2. Busca el registro de la decisión de acceso si necesitas conocer el motivo.
3. Evita guardar credenciales en registros o incluirlas al compartirlos.
