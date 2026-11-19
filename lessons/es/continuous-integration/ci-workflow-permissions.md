---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "es"
order_index: 7
title: "Permisos de los flujos de trabajo"
description: "Aprende a dar a una comprobación habitual de CI solo el acceso al repositorio que necesita."
meta_title: "Permisos de los flujos de trabajo - Integración continua"
meta_description: "Aprende a dar a una comprobación habitual de CI solo el acceso al repositorio que necesita."
meta_keywords: "permisos, acceso de lectura, flujos de trabajo, integración continua, DevOps, Linux Journey"
---

Un trabajo de CI ejecuta comandos y también puede recibir credenciales. Un **permiso** define qué se puede leer o modificar con esas credenciales. Un trabajo que solo comprueba la página suele necesitar leer los archivos fuente.

## Dar acceso de lectura a una comprobación

Este fragmento de GitHub Actions limita el token integrado del flujo al acceso de lectura del contenido del repositorio.

```yaml
permissions:
  contents: read
```

El checkout y la prueba local pueden leer el repositorio. Un trabajo que publica un paquete necesita otro permiso, sobre un recurso diferente. Concede el permiso de publicación al trabajo concreto que lo necesita.

:::single-choice{#ci-workflow-permissions-choose-permission} Un trabajo lee la página y ejecuta grep. ¿Qué permiso sobre el contenido del repositorio necesita?

::option[Escritura, porque el resultado de la prueba se escribe en el terminal.]{#ci-workflow-permissions-choose-permission-a explanation="Escribir en el terminal no requiere permiso para modificar el contenido del repositorio."}
::option[Lectura.]{#ci-workflow-permissions-choose-permission-c .correct explanation="El trabajo necesita obtener el contenido y no tiene que cambiar nada en el repositorio."}
::option[Escritura, porque el código fuente está en un repositorio de Git.]{#ci-workflow-permissions-choose-permission-b explanation="Para la comprobación descrita basta con leer los archivos fuente."}
:::

## Proteger los valores confidenciales

Un **secreto** es un valor como un token privado. Usa el almacén de secretos de la plataforma cuando un trabajo autorizado necesite uno. Mantén los ajustes normales de la página separados de los secretos. Las comprobaciones habituales de un ejemplo local deben funcionar sin credenciales de publicación.

:::single-choice{#ci-workflow-permissions-secret-needed} ¿Qué valor debe guardarse en un almacén de secretos con acceso controlado?

::option[Una credencial privada para subir un paquete.]{#ci-workflow-permissions-secret-needed-a .correct explanation="Una credencial puede dar acceso a otro sistema."}
::option[El texto Welcome que usa la prueba.]{#ci-workflow-permissions-secret-needed-b explanation="Es contenido público de ejemplo."}
::option[El nombre del directorio de salida dist.]{#ci-workflow-permissions-secret-needed-c explanation="El nombre del directorio es un ajuste normal."}
:::

## Mantener registros útiles

Los registros del flujo se pueden compartir con otras personas. Indica qué acción se realizó y cuál fue el resultado sin mostrar valores secretos. Un error puede indicar que faltaba una credencial requerida o que se denegó el acceso. Facilita el nombre del trabajo y su revisión a quien mantenga el flujo para que pueda investigar. Deja el valor de la credencial fuera del mensaje.

:::single-choice{#ci-workflow-permissions-safe-diagnostic} Un trabajo de publicación no puede autenticarse. ¿Qué mensaje ayuda a investigar el fallo sin revelar la credencial?

::option[Mostrar la credencial completa para poder copiarla.]{#ci-workflow-permissions-safe-diagnostic-a explanation="Cualquiera con acceso al registro podría ver la credencial."}
::option[Mostrar todos los valores de entorno para explicar el estado del trabajo.]{#ci-workflow-permissions-safe-diagnostic-c explanation="Listar todas las variables de entorno puede exponer valores confidenciales."}
::option[Indicar qué paso de publicación falló y qué ocurrió al intentar acceder.]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="Así se localiza el fallo y se puede comprobar por separado el acceso configurado."}
:::

## Revisar un trabajo nuevo

Una propuesta ejecuta comprobaciones de página en las pull requests y añade un trabajo que publica un paquete. Cada trabajo necesita permisos distintos. Deja a la comprobación solo el acceso de lectura necesario y concede permisos de publicación autorizados únicamente al trabajo que publica.

:::single-choice{#ci-workflow-permissions-final-application} ¿Qué cambio en la propuesta encaja mejor con lo que necesitan los dos trabajos?

::option[Dar permiso de escritura en el repositorio a los dos trabajos.]{#ci-workflow-permissions-final-application-b explanation="La comprobación solo lee los archivos fuente. Para publicar un paquete puede hacer falta otro permiso."}
::option[Usar la misma credencial de subida en todos los pasos para que las repeticiones funcionen igual.]{#ci-workflow-permissions-final-application-c explanation="Solo el trabajo de publicación necesita una credencial de subida."}
::option[Mantener las comprobaciones con acceso de solo lectura y dar al trabajo de publicación solo el acceso al paquete que necesita.]{#ci-workflow-permissions-final-application-a .correct explanation="Así cada trabajo tiene el acceso necesario y se limitan los permisos del resto del flujo."}
:::

## Resumen

Ya puedes determinar qué permisos necesita una canalización de CI sencilla.

1. Ajusta los permisos del repositorio a la tarea que realiza el trabajo.
2. Guarda las credenciales privadas en un almacén con acceso controlado.
3. Registra errores útiles sin mostrar valores confidenciales.
