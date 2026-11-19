---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "es"
order_index: 1
title: "Eventos de auditoría"
description: "Aprende a elegir qué eventos auditar para responder a una pregunta sobre un archivo protegido."
meta_title: "Eventos de auditoría - Auditoría de sistemas"
meta_description: "Aprende a elegir qué eventos auditar para responder a una pregunta sobre un archivo protegido."
meta_keywords: "eventos de auditoría, auditoría de sistemas, ciberseguridad, Linux Journey"
---

Un registro de servicio puede indicar que se cargó una página. Un **registro de auditoría** puede describir una acción que tu sistema estaba configurado para observar, como una escritura en un archivo de configuración. Empieza por decidir qué acción importa y qué información necesitas para revisarla.

## Elegir una pregunta de auditoría

Supón que la configuración del servicio web controla quién puede abrir una vista previa. Quieres revisar los cambios en ese archivo. Un registro útil indicaría el objeto, la operación, la hora, la cuenta vinculada a la acción y el resultado. Cada campo ayuda a reconstruir una parte de la acción.

:::single-choice{#system-audit-events-choose-object} ¿Qué debería identificar un registro de auditoría para esta revisión?

::option[Solo el número de peticiones web de ese día.]{#system-audit-events-choose-object-b explanation="El volumen de peticiones describe otra actividad."}
::option[El archivo de configuración al que iba dirigida la operación.]{#system-audit-events-choose-object-a .correct explanation="El objeto permite distinguir este cambio de las escrituras en otros archivos."}
::option[Solo el tipo de operación, por ejemplo, una escritura.]{#system-audit-events-choose-object-c explanation="La operación indica qué se intentó hacer. El archivo de destino permite saber si era pertinente."}
:::

## Interpretar el resultado

Un registro puede describir una escritura que se completó o un intento fallido. Fíjate tanto en la operación como en su resultado. Una escritura denegada puede ser una prueba útil de un intento. La conclusión es distinta de la que corresponde a una escritura completada.

:::single-choice{#system-audit-events-operation-result} Un registro menciona una escritura en la configuración e indica que se denegó. ¿Qué muestra?

::option[Se denegó el intento de escritura registrado.]{#system-audit-events-operation-result-b .correct explanation="La operación y su resultado describen juntos la acción observada."}
::option[El archivo se reemplazó con seguridad.]{#system-audit-events-operation-result-a explanation="Un resultado denegado no demuestra que se hiciera el cambio."}
::option[La página prevista devolvió HTTP 200.]{#system-audit-events-operation-result-c explanation="Aquí no se describe ninguna petición a una página."}
:::

## Comprobar la cobertura

El sistema de auditoría solo registra los eventos que sus mecanismos y políticas pueden observar. Antes de interpretar una búsqueda sin resultados, comprueba que la política cubría la ruta, las operaciones y el intervalo adecuados. Anota qué fuente revisaste.

:::single-choice{#system-audit-events-empty-audit} No encuentras ningún registro de escritura en el archivo que consultaste. ¿Qué conviene comprobar antes de concluir que no hubo escrituras?

::option[Contar cuántos editores están instalados.]{#system-audit-events-empty-audit-a explanation="El software instalado no determina la cobertura de auditoría."}
::option[Buscar en el mismo periodo solo con el nombre de otra cuenta.]{#system-audit-events-empty-audit-b explanation="Otra búsqueda puede ayudar si sabes que la recopilación funciona. Comprueba primero si los eventos pertinentes podían quedar registrados."}
::option[Verificar la política y el intervalo de tiempo disponible.]{#system-audit-events-empty-audit-c .correct explanation="Si falta cobertura, puede haber habido actividad sin que exista un registro coincidente."}
:::

## Resumen

Ya puedes elegir pruebas de auditoría útiles para revisar un recurso protegido.

1. Identifica la operación y el objeto que necesitas revisar.
2. Lee el resultado registrado junto con la acción solicitada.
3. Comprueba la cobertura antes de usar una búsqueda vacía como prueba.
