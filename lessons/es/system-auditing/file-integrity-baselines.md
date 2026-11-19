---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "es"
order_index: 4
title: "Referencias de integridad"
description: "Aprende a interpretar un informe de integridad y a decidir cuándo aprobar una nueva referencia."
meta_title: "Referencias de integridad - Auditoría de sistemas"
meta_description: "Aprende a interpretar un informe de integridad y a decidir cuándo aprobar una nueva referencia."
meta_keywords: "referencias de integridad, auditoría de sistemas, ciberseguridad, Linux Journey"
---

Una **referencia de integridad** es un registro fiable de las propiedades esperadas de los archivos en un momento determinado. Una comprobación posterior puede comparar los archivos actuales con esa referencia y mostrar las diferencias.

## Leer un informe de diferencias

Este fragmento simulado compara un equipo con su último estado aprobado.

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

La primera fila muestra un cambio en los bytes. La segunda muestra un cambio de permisos. La tercera indica que un archivo que se controlaba ya no estaba presente cuando se hizo la comprobación.

:::single-choice{#file-integrity-baselines-report-mode} ¿Qué fila indica que cambiaron los permisos de acceso?

::option[La fila de site.conf.]{#file-integrity-baselines-report-mode-a explanation="Indica que cambió el hash del contenido."}
::option[La fila de banner.txt.]{#file-integrity-baselines-report-mode-b .correct explanation="El modo cambió de 644 a 640."}
::option[La fila de site.prev.]{#file-integrity-baselines-report-mode-c explanation="Esta fila indica si existía un archivo en esa ruta."}
:::

![Informe de integridad simulado que compara el contenido de los archivos, el modo de acceso y su presencia](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## Comprobar la referencia

El informe solo sirve si la referencia anterior es fiable. Conserva su identificador y su fecha de creación. Si la copia de referencia se tomó cuando ya había un problema, la comparación puede llevar a conclusiones equivocadas. Averigua qué estado aprobado representa la referencia.

:::single-choice{#file-integrity-baselines-reference-source} ¿Qué referencia resulta más útil para revisar la configuración de hoy?

::option[Una copia registrada y aprobada antes del cambio.]{#file-integrity-baselines-reference-source-a .correct explanation="Proporciona una referencia conocida que puede verificarse durante la revisión."}
::option[Una referencia creada a partir de los archivos actuales con cambios sin explicar.]{#file-integrity-baselines-reference-source-b explanation="Incorporaría las diferencias antes de revisarlas."}
::option[La configuración de otro equipo, sin contexto para comparar.]{#file-integrity-baselines-reference-source-c explanation="Equipos con funciones distintas pueden requerir archivos y permisos diferentes."}
:::

## Revisar antes de actualizar la referencia

Compara cada diferencia con un cambio aprobado y comprueba el resultado en el servicio. Si estaba previsto cambiar los permisos del archivo del aviso, revisa por separado el cambio de configuración que no se había previsto. Actualiza la referencia una vez que hayas entendido las diferencias y se hayan aprobado. Conserva un registro de la referencia anterior.

:::single-choice{#file-integrity-baselines-update-timing} El cambio de permisos del archivo del aviso está aprobado y el cambio en site.conf sigue sin explicación. ¿Qué debes hacer antes de aceptar una nueva referencia?

::option[Aprobar todo porque esperabas una de las filas.]{#file-integrity-baselines-update-timing-a explanation="Las diferencias de los archivos corresponden a cambios distintos."}
::option[Desechar el informe de diferencias.]{#file-integrity-baselines-update-timing-b explanation="El informe documenta lo que aún queda por revisar."}
::option[Investigar el cambio sin explicar en site.conf.]{#file-integrity-baselines-update-timing-c .correct explanation="Antes de adoptar una nueva referencia debes revisar el estado actual."}
:::

Para crear y comparar una referencia de integridad en un entorno de prácticas, prueba [Monitorización de la integridad de archivos](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122).

## Resumen

Ya puedes usar una referencia como prueba en una comparación concreta.

1. Distingue entre contenido, modo y presencia en un informe.
2. Comprueba que la referencia corresponda a un estado fiable.
3. Revisa las diferencias inesperadas antes de aceptar una nueva referencia.
