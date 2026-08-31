---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "es"
order_index: 7
title: "Permisos de procesos"
description: "Aprende cómo los ID de usuario real, efectivo y guardado ayudan a los procesos de Linux a identificar al llamador y gestionar privilegios."
meta_title: "Permisos de procesos - Permisos"
meta_description: "Aprende los permisos de procesos de Linux y los ID de usuario real, efectivo y guardado. Comprende cómo influyen en la autorización y los cambios de privilegios."
meta_keywords: "permisos de procesos Linux, UID real, UID efectivo, UID guardado, seguridad Linux, tutorial Linux"
---

Las comprobaciones de autorización de Linux actúan sobre credenciales de procesos, no directamente sobre un nombre de usuario escrito. Un proceso tiene varios ID de usuario y grupo relacionados, cada uno con una función distinta. La mayoría de los programas normales empiezan con identidades coincidentes, mientras que los programas con privilegios pueden usar deliberadamente valores diferentes.

## ID de usuario real

El ID de usuario real identifica la cuenta que inició el proceso o su sesión de inicio antecesora. Los programas pueden consultarlo para distinguir al llamador de una identidad efectiva elevada.

En una orden normal iniciada por el usuario Bob, el ID de usuario real suele coincidir con el UID de Bob. Crear otro proceso no crea una cuenta nueva ni cambia por sí solo esta identidad.

:::single-choice{#process-permissions-real-uid}
¿Qué identifica normalmente el ID de usuario real de un proceso?

::option[El propietario del archivo abierto más recientemente.]{#process-permissions-real-opened-file explanation="Abrir un archivo no sustituye el UID real del proceso por el propietario de ese archivo."}
::option[La cuenta asociada al llamador original del proceso.]{#process-permissions-real-caller .correct explanation="El UID real registra la identidad de usuario llamadora heredada cuando se inicia el proceso."}
::option[El grupo seleccionado para todas las comprobaciones de acceso.]{#process-permissions-real-group explanation="Un UID es una identidad de usuario; las comprobaciones de grupo usan credenciales de grupo separadas."}
:::

## ID de usuario efectivo

El ID de usuario efectivo es la credencial de usuario que se emplea en muchas comprobaciones de sistema de archivos y privilegios. Normalmente coincide con el UID real. Al ejecutar un programa setuid respetado, puede inicializarse en su lugar a partir del propietario del ejecutable.

Por ejemplo, una utilidad de contraseñas cuidadosamente diseñada puede ejecutarse con un UID efectivo elevado para actualizar datos protegidos de autenticación. El programa todavía debe aplicar la política según el llamador, la cuenta solicitada, los resultados de PAM y otro contexto. Poseer un UID efectivo no hace que todas las operaciones solicitadas sean automáticamente legítimas.

:::single-choice{#process-permissions-effective-uid}
¿Qué ID de usuario se usa en muchas decisiones de control de acceso realizadas en nombre de un proceso?

::option[El ID de usuario efectivo.]{#process-permissions-effective-active .correct explanation="El UID efectivo es la credencial de usuario activa que se consulta en muchas comprobaciones de autorización."}
::option[Únicamente el ID de usuario guardado.]{#process-permissions-effective-saved-only explanation="El ID guardado permite transiciones de credenciales, pero no suele ser la identidad activa en las comprobaciones de acceso."}
::option[El UID almacenado en el directorio actual.]{#process-permissions-effective-directory explanation="La propiedad del sistema de archivos es metadato de los objetos, no la credencial activa de usuario del proceso."}
:::

## ID set-user-ID guardado

El ID set-user-ID guardado permite que un programa conserve una identidad que puede restaurar después, con sujeción a las reglas de las llamadas al sistema. Un programa con privilegios puede cambiar temporalmente su UID efectivo a un valor menos privilegiado, realizar trabajo normal con autoridad reducida y restaurar la identidad guardada únicamente para una operación de ámbito reducido.

Esto es más seguro que mantener autoridad elevada durante todo el programa, pero solo si se implementa correctamente. Los programas deben descartar los privilegios de forma permanente cuando ya no sean necesarios y comprobar si falla cada llamada que cambia credenciales.

:::single-choice{#process-permissions-saved-uid}
¿Por qué puede un programa con privilegios conservar un ID set-user-ID guardado?

::option[Para cambiar su identidad efectiva entre fases controladas con y sin privilegios.]{#process-permissions-saved-switch .correct explanation="La identidad guardada puede permitir una reducción temporal de privilegios y una restauración posterior permitida."}
::option[Para asignar automáticamente ese UID a todos los archivos que lee.]{#process-permissions-saved-file-owner explanation="Leer un archivo no cambia su propiedad al UID guardado del proceso."}
::option[Para sustituir la base de datos de cuentas del sistema para el proceso.]{#process-permissions-saved-database explanation="Las credenciales de procesos no sustituyen los registros de cuentas ni los datos de servicios de nombres."}
:::

## Los ID de usuario son solo parte del conjunto de credenciales

Los procesos también tienen credenciales de grupo reales, efectivas, guardadas y complementarias. Los ID del sistema de archivos, las capacidades, los espacios de nombres, los módulos de seguridad, las ACL, las opciones de montaje y las políticas de servicios pueden afectar también a la autorización. Por tanto, «el UID lo permite» suele ser solo parte de una explicación completa.

Usa herramientas como `ps` y `/proc/PROCESS/status` para consultar las credenciales en Linux. La disponibilidad de los campos y los formatos de visualización varían, así que consulta la documentación local y no cambies credenciales simplemente para experimentar en un sistema compartido.

:::single-choice{#process-permissions-ordinary-identities}
Para la mayoría de las órdenes normales sin transición de privilegios, ¿cómo se comparan los UID real y efectivo?

::option[El UID efectivo siempre es cero.]{#process-permissions-effective-root explanation="Las órdenes normales no reciben automáticamente el UID de root."}
::option[El UID real siempre coincide con el propietario del archivo ejecutable.]{#process-permissions-real-file-owner explanation="El propietario del ejecutable afecta al comportamiento setuid, no al UID real normal."}
::option[Normalmente coinciden con el UID del usuario que invoca la orden.]{#process-permissions-uids-match .correct explanation="Sin setuid ni un cambio explícito de credenciales, los procesos normales suelen ejecutarse con identidades real y efectiva coincidentes."}
:::

## Resumen

Ahora puedes explicar por qué un proceso de Linux puede llevar varias identidades de usuario.

1. Usa el UID real para identificar al llamador original.
2. Relaciona el UID efectivo con las comprobaciones activas de autorización.
3. Usa la identidad guardada para comprender transiciones controladas de privilegios.
4. Considera los ID de grupo y los mecanismos de seguridad adicionales como parte de la decisión completa.
