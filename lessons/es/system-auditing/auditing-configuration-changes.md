---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "es"
order_index: 5
title: "Cambios de configuración"
description: "Aprende a relacionar un cambio autorizado, una diferencia entre archivos y un evento de auditoría."
meta_title: "Cambios de configuración - Auditoría de sistemas"
meta_description: "Aprende a relacionar un cambio autorizado, una diferencia entre archivos y un evento de auditoría."
meta_keywords: "cambios de configuración, auditoría de sistemas, ciberseguridad, Linux Journey"
---

Una solicitud de cambio documenta lo que se piensa hacer. Una comparación de archivos muestra las diferencias actuales. Un evento de auditoría describe una acción observada que estaba dentro de la cobertura de la auditoría. Usa las tres fuentes para determinar qué puedes afirmar sobre un cambio de configuración.

## Identificar el cambio previsto

Revisa esta anotación de mantenimiento simulada.

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

Indica qué archivo y qué propiedad se autorizó modificar. Una diferencia en otro lugar requiere su propia explicación, incluso si aparece en el mismo intervalo.

:::single-choice{#auditing-configuration-changes-approve-scope} ¿Qué cambio coincide con la acción autorizada tal como se describe?

::option[Cambió el contenido de site.conf en web-01.]{#auditing-configuration-changes-approve-scope-b explanation="Ese archivo de configuración queda fuera de la autorización."}
::option[El archivo banner.txt desapareció de otro equipo.]{#auditing-configuration-changes-approve-scope-c explanation="Tanto la operación indicada como el equipo son distintos."}
::option[El modo de banner.txt cambió a 640 en web-01.]{#auditing-configuration-changes-approve-scope-a .correct explanation="Coinciden el archivo, la propiedad, el equipo y el resultado autorizado."}
:::

## Comparar las observaciones

Una comparación indica que cambió el modo del archivo del aviso y que cambiaron los bytes de `site.conf`. Otro evento de auditoría registra a las 09:15 una escritura en `site.conf` en `web-01`. El evento te da una hora para investigar. La autorización de la acción se comprueba por separado.

:::single-choice{#auditing-configuration-changes-source-comparison} ¿Qué conclusión se desprende de las dos observaciones sobre site.conf?

::option[La escritura estaba autorizada porque ocurrió dentro del intervalo.]{#auditing-configuration-changes-source-comparison-a explanation="La solicitud describe una acción distinta."}
::option[Vale la pena revisar este archivo porque se registró una escritura y sus bytes cambiaron.]{#auditing-configuration-changes-source-comparison-b .correct explanation="La comparación muestra la diferencia y el evento de auditoría acota la hora."}
::option[El cambio en el archivo del aviso provocó la escritura.]{#auditing-configuration-changes-source-comparison-c explanation="Estas observaciones no demuestran que una acción provocara la otra."}
:::

## Redactar la nota de revisión

Indica qué diferencia coincide con el plan y cuál sigue sin explicación. Incluye el archivo, el equipo, la hora y la referencia a la fuente. Un siguiente paso es comparar la configuración actual con la copia aprobada y comprobar si otro cambio autorizado cubre esa diferencia.

:::single-choice{#auditing-configuration-changes-useful-review} ¿Qué debes comunicar al equipo que continuará la revisión de site.conf?

::option[Describe la diferencia, cita la escritura observada y solicita la autorización que la respalde.]{#auditing-configuration-changes-useful-review-c .correct explanation="La nota conserva las pruebas y la pregunta pendiente."}
::option[Márcalo como aprobado y omite la ruta.]{#auditing-configuration-changes-useful-review-a explanation="Así pierdes la referencia al archivo y das por hecha una autorización que no figura en los registros."}
::option[Atribuye el cambio a la persona responsable del archivo del aviso.]{#auditing-configuration-changes-useful-review-b explanation="Los registros no permiten establecer esa atribución."}
:::

## Comparar dos anotaciones de mantenimiento

Otra solicitud autoriza una edición posterior de site.conf. Compara la hora observada, el equipo de destino y el archivo con la solicitud antes de cerrar la revisión. Un cambio autorizado en el archivo correcto puede dejar sin explicar un evento anterior.

:::single-choice{#auditing-configuration-changes-final-application} La solicitud cubre site.conf en web-01 de 09:40 a 10:00. ¿Qué queda por aclarar sobre la escritura registrada a las 09:15?

::option[Si site.conf existe fuera del sistema de solicitudes.]{#auditing-configuration-changes-final-application-b explanation="La comparación de archivos ya confirma que la configuración está presente."}
::option[Si la solicitud posterior debe explicar automáticamente todas las escrituras previas.]{#auditing-configuration-changes-final-application-c explanation="La autorización se aplica a la acción y al intervalo indicados."}
::option[Si otra autorización cubre esa escritura anterior.]{#auditing-configuration-changes-final-application-a .correct explanation="El equipo y la ruta coinciden, pero la hora registrada queda fuera del intervalo autorizado."}
:::

## Resumen

Ya puedes reconstruir lo que se sabe de un cambio de configuración.

1. Identifica el alcance previsto en la solicitud de cambio autorizada.
2. Usa comparaciones y eventos de auditoría para describir lo observado.
3. Explica qué prueba falta y elige la siguiente comprobación.
