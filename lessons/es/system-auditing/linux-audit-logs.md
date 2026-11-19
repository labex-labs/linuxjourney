---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "es"
order_index: 2
title: "Registros de auditoría de Linux"
description: "Aprende a agrupar los registros de auditoría de Linux que describen una misma operación."
meta_title: "Registros de auditoría de Linux - Auditoría de sistemas"
meta_description: "Aprende a agrupar los registros de auditoría de Linux que describen una misma operación."
meta_keywords: "registros de auditoría de Linux, auditoría de sistemas, ciberseguridad, Linux Journey"
---

El sistema de auditoría de Linux puede escribir varios registros para un solo evento. Una línea puede describir la operación y otra indicar una ruta. Agrupa primero las líneas relacionadas para entender lo que muestran.

## Leer un evento compartido

Los siguientes valores son registros abreviados de prácticas del mismo equipo y fecha. El número que aparece después de los dos puntos en la referencia de auditoría ayuda a agrupar registros con la misma marca de tiempo y el mismo ID de evento. Estas líneas corresponden a un solo evento.

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

La primera línea recoge el resultado y los campos de cuenta. La línea de ruta nombra un archivo asociado con el evento.

:::single-choice{#linux-audit-logs-group-rows} ¿Qué campos permiten relacionar la operación con la ruta en este ejemplo?

::option[Solo los dos tipos de registro, SYSCALL y PATH.]{#linux-audit-logs-group-rows-a explanation="Los tipos indican la función de cada línea. Muchos eventos pueden contener los mismos tipos."}
::option[El hecho de que ambas líneas empiecen por type.]{#linux-audit-logs-group-rows-c explanation="Cada línea puede tener un tipo aunque describa un evento distinto."}
::option[La referencia de auditoría que coincide en el mismo equipo.]{#linux-audit-logs-group-rows-b .correct explanation="Agrupa las líneas que describen el evento 42."}
:::

![Filas simuladas SYSCALL y PATH de la auditoría de Linux que comparten la misma referencia de evento](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## Interpretar dos identidades

En esta muestra, `auid` es el ID de auditoría del usuario que inició sesión y `euid` es el ID de usuario efectivo con el que se realizó la acción. Un programa puede usar una identidad efectiva distinta de la identidad de inicio de sesión. El ID numérico identifica una cuenta del equipo. Para identificar a la persona que usó esa cuenta pueden hacer falta otros registros.

:::single-choice{#linux-audit-logs-identify-login} ¿Qué campo muestra la identidad de auditoría de inicio de sesión en esta muestra?

::option[El campo euid con valor 0.]{#linux-audit-logs-identify-login-b explanation="Indica la identidad efectiva del programa para ese evento."}
::option[El campo auid con valor 1001.]{#linux-audit-logs-identify-login-a .correct explanation="El campo auid indica el ID de auditoría de inicio de sesión y euid indica la identidad efectiva."}
::option[El número de evento 42.]{#linux-audit-logs-identify-login-c explanation="Ese número agrupa registros y es independiente de la identidad de las cuentas."}
:::

## Limitar la conclusión a lo observado

El campo de resultado informa de que la operación registrada se completó correctamente. Examina el evento completo para identificar la operación. Para comprobar si cambió el contenido, compara el archivo con una referencia conocida.

:::single-choice{#linux-audit-logs-useful-follow-up} ¿Qué ayudaría a determinar si el contenido difiere del archivo aprobado?

::option[Compararlo con una copia de referencia aprobada o con un registro de integridad.]{#linux-audit-logs-useful-follow-up-c .correct explanation="Esa prueba puede mostrar qué cambió en el archivo."}
::option[Un segundo registro de auditoría que indique otra operación completada.]{#linux-audit-logs-useful-follow-up-a explanation="Eso confirma otra acción registrada. Para saber si el contenido cambió, hay que comparar los bytes actuales con la copia aprobada."}
::option[El ID de la cuenta que inició sesión en el mismo evento.]{#linux-audit-logs-useful-follow-up-b explanation="El ID de inicio de sesión ayuda a identificar la cuenta asociada. Los cambios en los bytes se comprueban por separado."}
:::

## Resumen

Ya puedes agrupar registros para interpretar un evento de auditoría.

1. Relaciona los registros por equipo y por referencia del evento de auditoría.
2. Lee por separado la identidad de inicio de sesión y la efectiva.
3. Elige qué comprobar a continuación si el resultado registrado deja una pregunta abierta.
