---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "es"
order_index: 2
title: "Tipos de sistemas de archivos"
description: "Aprende cómo VFS de Linux presenta sistemas de archivos locales, de red y virtuales mediante una interfaz común."
meta_title: "Tipos de sistemas de archivos - El sistema de archivos"
meta_description: "Descubre tipos de sistemas de archivos Linux como ext4, XFS y Btrfs, y comprende VFS y el journaling."
meta_keywords: "tipos de sistemas de archivos Linux, ext4, Btrfs, XFS, journaling, VFS"
---

Linux admite muchas implementaciones de sistemas de archivos con distintos formatos en disco, protocolos de red, modelos de coherencia, funciones y herramientas operativas. La elección adecuada depende de la compatibilidad de la distribución, la carga de trabajo, los requisitos de recuperación, la topología del almacenamiento y la experiencia del administrador.

## La capa del sistema de archivos virtual

La capa del sistema de archivos virtual del kernel, o VFS, proporciona operaciones comunes como abrir, leer, escribir, cambiar nombres y comprobar permisos. Las implementaciones de sistemas de archivos conectan esas operaciones con sus propias estructuras de datos y soportes subyacentes.

Esto permite que un proceso acceda a ext4, XFS, NFS, tmpfs y procfs mediante un modelo compartido de rutas y descriptores de archivos. No hace que todas las funciones o comportamientos sean idénticos: la distinción entre mayúsculas y minúsculas, los bloqueos, los permisos, las garantías al cambiar nombres, los atributos ampliados y el tratamiento de errores pueden diferir.

:::single-choice{#filesystem-types-vfs-role} ¿Cuál es la función principal de VFS en Linux?

::option[Convertir en disco todos los sistemas de archivos montados a ext4.]{#filesystem-types-vfs-convert-ext4 explanation="La abstracción conserva las distintas implementaciones y formatos de sistemas de archivos."}
::option[Crear una copia de seguridad de cada archivo antes de que una aplicación escriba en él.]{#filesystem-types-vfs-backup explanation="VFS distribuye operaciones y no proporciona automáticamente un historial de copias de seguridad."}
::option[Proporcionar operaciones comunes del kernel para distintas implementaciones de sistemas de archivos.]{#filesystem-types-vfs-common-interface .correct explanation="VFS permite que las aplicaciones utilicen llamadas al sistema compartidas mientras cada sistema de archivos implementa el comportamiento subyacente."}
:::

## Journaling y coherencia tras fallos

Un sistema de archivos con journaling registra determinadas actualizaciones en un diario para poder reproducir o descartar transacciones incompletas después de un fallo. La finalidad principal del journaling es restaurar la coherencia estructural del sistema de archivos más rápidamente que con un recorrido completo.

No garantiza que sobrevivieran los datos más recientes de la aplicación, que sean válidas las transacciones de aplicaciones entre varios archivos ni que el hardware de almacenamiento respetara cada escritura completada. Los sistemas de archivos ofrecen distintos modos de datos y garantías de orden, mientras que las aplicaciones deben emplear patrones apropiados de vaciado y actualización atómica. Un diario no es una copia de seguridad y no protege frente a eliminaciones, software malicioso o fallos del dispositivo.

:::single-choice{#filesystem-types-journal-scope} ¿Qué ayuda principalmente a recuperar el journaling del sistema de archivos después de un fallo?

::option[Metadatos coherentes del sistema de archivos y transacciones registradas.]{#filesystem-types-journal-consistency .correct explanation="Reproducir el diario ayuda a devolver las estructuras del sistema de archivos a un estado coherente."}
::option[Todas las versiones históricas de todos los documentos de los usuarios.]{#filesystem-types-journal-versions explanation="Un diario no es un almacén de copias de seguridad con versiones."}
::option[Datos de un dispositivo de almacenamiento destruido físicamente.]{#filesystem-types-journal-hardware-loss explanation="Recuperarse de la pérdida de un dispositivo exige redundancia o copias de seguridad externas al dispositivo averiado."}
:::

## Sistemas de archivos locales habituales

- **ext4** es un sistema de archivos con journaling maduro y ampliamente compatible con las distribuciones y herramientas de recuperación de Linux.
- **XFS** es un sistema de archivos con journaling escalable que suele elegirse para sistemas grandes y cargas de E/S paralela.
- **Btrfs** es un sistema de archivos de copia al escribir con sumas de comprobación, subvolúmenes, instantáneas y funciones multidispositivo integradas.

Las funciones necesitan contexto operativo. Una instantánea de Btrfs comparte inicialmente almacenamiento con su origen y no es una copia de seguridad independiente si permanece en el mismo dispositivo que falla. XFS y ext4 tienen capacidades distintas para crecer, reducirse, repararse y ajustarse. Confirma la compatibilidad del kernel, el entorno de arranque y las herramientas de recuperación instalados antes de elegir o cambiar un sistema de archivos raíz.

:::single-choice{#filesystem-types-btrfs-snapshot} ¿Por qué una instantánea de Btrfs en el mismo dispositivo no es una copia de seguridad completa?

::option[Porque las instantáneas siempre eliminan inmediatamente el subvolumen original.]{#filesystem-types-snapshot-deletes explanation="Una instantánea crea otra vista de subvolumen y no elimina por sí misma su origen."}
::option[Porque comparte el mismo dominio de fallo de almacenamiento que el original.]{#filesystem-types-snapshot-failure-domain .correct explanation="La pérdida del dispositivo o daños graves en el sistema de archivos pueden afectar al origen y a su instantánea local."}
::option[Porque Btrfs no puede representar más de un archivo.]{#filesystem-types-btrfs-one-file explanation="Btrfs es un sistema de archivos de uso general para árboles de directorios y muchos archivos."}
:::

## Sistemas de interoperabilidad, de red y virtuales

Linux puede montar formatos de interoperabilidad como las variantes de FAT, exFAT y NTFS, pero su semántica de propiedad, permisos, enlaces y nombres de archivo de Unix difiere. Las opciones de montaje y la implementación del controlador determinan cómo presenta Linux las funciones ausentes.

Los sistemas de archivos de red como NFS y SMB dependen de un servidor y un protocolo de red, con reglas distintas de caché e identidad. Los sistemas virtuales como tmpfs, procfs y sysfs no utilizan un formato de disco persistente normal: tmpfs almacena datos volátiles en páginas respaldadas por memoria, mientras que procfs y sysfs exponen interfaces del kernel.

:::single-choice{#filesystem-types-procfs-category} ¿Qué descripción corresponde mejor a procfs?

::option[Un formato de intercambio de Windows para medios extraíbles.]{#filesystem-types-procfs-windows explanation="FAT o exFAT se aproximan más a ese uso; procfs está orientado al kernel de Linux."}
::option[Un sistema de archivos virtual que expone interfaces de procesos y del kernel.]{#filesystem-types-procfs-virtual .correct explanation="Procfs genera una vista actual del kernel en vez de almacenar archivos persistentes ordinarios en disco."}
::option[Un sistema de archivos de disco con journaling diseñado para volúmenes de bases de datos.]{#filesystem-types-procfs-journal explanation="Procfs no tiene un diario normal en disco ni desempeña la función de volumen de datos."}
:::

## Descubrir los tipos activos

Muestra los tipos de sistemas de archivos montados con:

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Otras vistas son `df -T` para contabilizar el espacio montado, `lsblk -f` para dispositivos de bloques y firmas de sistemas de archivos detectadas, y `/proc/filesystems` para tipos compatibles o conocidos por el kernel en ejecución. Responden a preguntas distintas; un sistema de archivos sin montar no aparecerá en un listado ordinario de sistemas montados.

:::single-choice{#filesystem-types-findmnt-output} ¿Qué orden muestra directamente destinos montados con su fuente, tipo y opciones en esta lección?

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="Findmnt lee la tabla de montajes y presenta los campos solicitados de los sistemas de archivos montados."}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="Esta orden muestra datos del hardware de bloques, no los tipos y opciones efectivos de los sistemas de archivos montados."}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="Esta orden comunica tipos compatibles con el kernel, no las fuentes y opciones de montaje efectivas."}
:::

Utiliza [Gestionar particiones y sistemas de archivos de Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) sobre almacenamiento desechable para comparar tipos, opciones de montaje y vistas de descubrimiento.

## Resumen

Ahora puedes comparar categorías de sistemas de archivos sin suponer una semántica idéntica.

1. Relaciona VFS con operaciones comunes entre implementaciones.
2. Trata el journaling como ayuda para la coherencia tras fallos, no como copia de seguridad.
3. Compara ext4, XFS y Btrfs según sus operaciones compatibles y la carga de trabajo.
4. Distingue sistemas de archivos locales, de red, de interoperabilidad y virtuales.
5. Utiliza herramientas de montajes y dispositivos de bloques para responder a preguntas de inventario distintas.
