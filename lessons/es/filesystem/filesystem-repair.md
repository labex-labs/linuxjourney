---
lesson_id: "filesystem-repair"
course_id: "filesystem"
lang: "es"
order_index: 10
title: "Reparación del sistema de archivos"
description: "Aprende a diagnosticar daños en sistemas de archivos y elegir un flujo de reparación sin conexión, específico del tipo y con copias de seguridad."
meta_title: "Reparación del sistema de archivos - El sistema de archivos"
meta_description: "Aprende a diagnosticar y reparar sistemas de archivos Linux sin conexión mediante herramientas específicas del formato y copias de seguridad."
meta_keywords: "fsck, reparación de sistemas de archivos, errores de disco, recuperación de datos, e2fsck, xfs_repair"
---

Reparar un sistema de archivos reescribe metadatos para restaurar la coherencia interna. Puede descartar referencias o datos dañados y agravar la pérdida cuando falla el hardware de almacenamiento. Trata la reparación como una operación de recuperación: conserva primero las pruebas y los datos recuperables y después utiliza la herramienta documentada para el sistema de archivos exacto.

## Diagnosticar antes de reparar

Síntomas como errores de E/S, remontajes de solo lectura, archivos ausentes o fallos al montar no demuestran todos que exista corrupción del sistema de archivos. Recopila primero pruebas de solo lectura:

```bash
$ findmnt --target /affected/path
$ lsblk -f
$ journalctl -k -b
```

Comprueba la pila de almacenamiento, el estado del dispositivo, los cables o la ruta de red, el estado de RAID, el cifrado y los sucesos recientes. Si falla el dispositivo, los recorridos repetidos pueden consumir su vida restante. Captura una imagen o un clon con una herramienta orientada a la recuperación y trabaja sobre la copia cuando sea posible.

:::single-choice{#filesystem-repair-first-response}
¿Qué debe preceder a una reparación del sistema de archivos con capacidad de escritura cuando pueda existir un fallo de hardware?

::option[Ejecutar repetidamente todas las herramientas de reparación hasta que una devuelva cero.]{#filesystem-repair-repeat-tools explanation="Utilizar herramientas incompatibles y realizar escrituras repetidas puede agravar los daños."}
::option[Crear inmediatamente una tabla de particiones nueva sobre el dispositivo.]{#filesystem-repair-new-table explanation="Sobrescribir los metadatos del diseño destruye pruebas y puede dificultar la recuperación."}
::option[Conservar los datos recuperables o una imagen e investigar el estado del dispositivo.]{#filesystem-repair-preserve-first .correct explanation="La reparación modifica metadatos, mientras que un soporte defectuoso puede deteriorarse durante accesos repetidos."}
:::

## Identificar el sistema de archivos y el dispositivo exactos

Determina si el sistema de archivos reside en una partición, un volumen lógico, un dispositivo RAID, un mapeo cifrado o un disco completo. No ejecutes un comprobador sobre `/dev/sda` solo porque esté afectada una partición hija como `/dev/sda1`.

Utiliza `lsblk -f`, `blkid`, `findmnt` y herramientas de las capas de almacenamiento para localizar el destino. Las firmas detectadas pueden estar obsoletas, así que contrástalas con la configuración conocida y las copias de seguridad.

:::single-choice{#filesystem-repair-target-layer}
Si ext4 está almacenado en `/dev/sda1`, ¿qué capa debe recibir normalmente su comprobador de ext4?

::option[`/dev/sda`, con independencia de su tabla de particiones.]{#filesystem-repair-whole-disk explanation="El disco completo contiene la tabla de particiones y quizá varias regiones hijas, no directamente la instancia ext4."}
::option[`/dev/sda1`, después de desconectarla de forma segura.]{#filesystem-repair-partition-target .correct explanation="El comprobador actúa sobre el dispositivo de bloques que contiene directamente el sistema de archivos."}
::option[`/mnt/data`, mientras las aplicaciones siguen escribiendo allí.]{#filesystem-repair-live-mount explanation="Una ruta de punto de montaje no es el destino de bloques sin conexión que espera el comprobador."}
:::

## Desconectar el sistema de archivos

La mayoría de los comprobadores de coherencia tradicionales necesitan que el sistema de archivos esté desmontado. Un sistema montado cambia mientras el comprobador lo lee, y las escrituras de reparación pueden entrar en conflicto con el estado en caché del kernel y provocar corrupción.

Detén los servicios dependientes, desmonta sistemas de archivos anidados, saca los directorios de trabajo de los procesos y desactiva las capas superiores necesarias. Para el sistema de archivos raíz, arranca un entorno de rescate o utiliza el mecanismo documentado por la distribución para comprobarlo sin conexión. Confirma con `findmnt` que el destino no esté montado en el espacio de nombres pertinente.

:::single-choice{#filesystem-repair-mounted-risk}
¿Por qué debe desmontarse normalmente un sistema de archivos antes de que un comprobador de reparación escriba en él?

::option[Porque las actualizaciones simultáneas del kernel y el comprobador pueden entrar en conflicto y corromper metadatos.]{#filesystem-repair-concurrent-writes .correct explanation="Una vista sin conexión impide que el sistema de archivos cambie durante la reparación."}
::option[Porque desmontarlo restaura automáticamente desde una copia todos los archivos dañados.]{#filesystem-repair-unmount-restores explanation="Desconectarlo proporciona coherencia para la comprobación, pero no restaura datos."}
::option[Porque las herramientas de sistemas de archivos solo pueden leer directorios, nunca dispositivos de bloques.]{#filesystem-repair-tools-directories explanation="Las herramientas de reparación suelen actuar directamente sobre dispositivos de bloques sin conexión."}
:::

## Utilizar la herramienta específica del sistema de archivos

`fsck` es una interfaz que puede invocar auxiliares específicos de cada sistema de archivos. No es un único motor universal de reparación. Algunos flujos distintos utilizan `e2fsck` para sistemas ext, `xfs_repair` para XFS y herramientas específicas de diagnóstico y recuperación para Btrfs.

Las opciones con nombres parecidos pueden tener una semántica diferente. En particular, no apliques opciones `--repair` o de fuerza copiadas de la guía de otro sistema de archivos. Lee el manual instalado y la documentación actual de recuperación del proyecto o la distribución. Empieza con un modo de diagnóstico o sin modificaciones si la implementación ofrece uno fiable, captura la salida y comprende las correcciones propuestas.

:::single-choice{#filesystem-repair-fsck-role}
¿De qué se encarga habitualmente `fsck` en Linux?

::option[De delegar las comprobaciones en un auxiliar apropiado para el tipo de sistema de archivos.]{#filesystem-repair-fsck-dispatch .correct explanation="La lógica real de validación y reparación pertenece a herramientas y flujos específicos del formato."}
::option[De convertir todos los sistemas de archivos a ext4 antes de comprobarlos.]{#filesystem-repair-fsck-convert explanation="Un comprobador debe conservar y comprender el formato existente."}
::option[De reparar sectores físicos defectuosos sin riesgo de perder datos.]{#filesystem-repair-fsck-hardware explanation="Las herramientas de coherencia no pueden reparar hardware físico ni garantizar la recuperación de datos."}
:::

## Verificar y restaurar el servicio

Registra la herramienta de reparación, su versión, las opciones, la salida y el estado de salida. Después de reparar, repite las comprobaciones del dispositivo, monta primero como solo lectura cuando corresponda, examina los datos esenciales y compáralos con copias conocidas. Restaura después los montajes y servicios normales gradualmente mientras supervisas los registros del kernel y las aplicaciones.

Que un sistema de archivos vuelva a poder montarse no demuestra que todos los archivos sean correctos. Restaura desde copias los datos de aplicación perdidos o dañados y valídalos a nivel de la aplicación.

:::single-choice{#filesystem-repair-mountable-proof}
¿Un montaje correcto después de reparar demuestra que todos los datos de la aplicación son correctos?

::option[No; reparar la coherencia y validar los datos de la aplicación son tareas distintas.]{#filesystem-repair-not-data-proof .correct explanation="El sistema de archivos puede ser estructuralmente montable aunque falten archivos o transacciones o estén dañados."}
::option[Sí; montar verifica criptográficamente todos los archivos frente a una copia de seguridad.]{#filesystem-repair-mount-verifies explanation="Un montaje ordinario no realiza una comparación completa con copias de seguridad."}
::option[Sí; las herramientas de reparación recrean automáticamente todo el contenido desconocido.]{#filesystem-repair-recreates-data explanation="Reparar metadatos no permite deducir datos de usuario arbitrarios perdidos."}
:::

## Resumen

Ahora puedes planificar la reparación de un sistema de archivos como un procedimiento de recuperación por etapas.

1. Diagnostica el hardware y conserva los datos recuperables antes de escribir.
2. Localiza la capa de bloques exacta que contiene el sistema de archivos.
3. Desconecta el sistema de archivos en el espacio de nombres pertinente.
4. Utiliza la herramienta documentada de diagnóstico y reparación específica del sistema.
5. Valida por separado el estado del dispositivo, del sistema de archivos y de los datos de la aplicación.
