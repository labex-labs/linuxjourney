---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "es"
order_index: 4
title: "Particionado de discos"
description: "Aprende un flujo de trabajo basado en la verificación para examinar, crear y redimensionar límites de particiones con `parted`."
meta_title: "Particionado de discos - El sistema de archivos"
meta_description: "Aprende a examinar, crear y redimensionar particiones Linux con parted mediante un flujo seguro basado en la verificación."
meta_keywords: "particionado de discos Linux, parted, fdisk, gparted, crear partición, redimensionar partición"
---

Editar particiones cambia el mapa que define los límites del almacenamiento. Un dispositivo, inicio o final incorrecto puede hacer inaccesibles los datos existentes o sobrescribir metadatos esenciales. Practica únicamente en un disco virtual desechable y conserva una copia de seguridad probada por separado antes de modificar almacenamiento valioso.

## Elegir una herramienta

Entre las herramientas habituales se encuentran:

- `fdisk`, un editor de particiones para terminal de util-linux compatible con MBR y GPT
- `parted`, un editor para terminal y scripts compatible con GPT, MBR y otros formatos de tabla
- `gdisk`, un editor interactivo centrado en GPT
- GParted, una interfaz gráfica para particiones y sistemas de archivos

La compatibilidad de las herramientas evoluciona, así que utiliza el manual local y la documentación de la distribución. Una interfaz gráfica no hace seguras las operaciones destructivas; sigue cambiando los mismos metadatos del disco.

:::single-choice{#disk-partitioning-fdisk-gpt} ¿Qué afirmación sobre el `fdisk` actual de Linux es correcta?

::option[Admite tablas de particiones MBR y GPT.]{#disk-partitioning-fdisk-supports-gpt .correct explanation="El fdisk actual de util-linux puede editar diseños DOS/MBR y GPT, entre otros."}
::option[Solo puede editar GPT y nunca MBR.]{#disk-partitioning-fdisk-only-gpt explanation="`gdisk`, centrado en GPT, se aproxima más a esa descripción; fdisk admite varios tipos de etiquetas."}
::option[Crea sistemas de archivos, pero no puede editar entradas de particiones.]{#disk-partitioning-fdisk-filesystem-only explanation="Su finalidad principal es mostrar y editar tablas de particiones."}
:::

## Identificar y detener el uso del destino

Comienza con un inventario de solo lectura:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

Confirma el dispositivo completo mediante su identidad persistente, modelo, número de serie, tamaño, transporte y topología, no solo por `/dev/sdX`. Después identifica todos sus consumidores: sistemas de archivos montados, intercambio, LVM, RAID, cifrado, contenedores, máquinas virtuales, bases de datos y descriptores de archivo abiertos.

Desmonta o desactiva todas las capas pertinentes mediante sus procedimientos documentados. No edites la tabla de particiones del disco del sistema en ejecución solo porque la herramienta se abra correctamente. Registra la tabla existente en un formato restaurable y confirma que la copia de seguridad reside en otro dominio de fallo.

:::single-choice{#disk-partitioning-target-identity} ¿Por qué un nombre de dispositivo como `/dev/sdb` no basta como única comprobación del destino?

::option[Porque Linux nunca expone discos completos bajo `/dev`.]{#disk-partitioning-no-whole-disks explanation="Los discos completos suelen tener nodos de bloques bajo `/dev`."}
::option[Porque los nombres de enumeración pueden cambiar al modificarse los dispositivos o la topología.]{#disk-partitioning-enumeration-changes .correct explanation="La letra se asigna según el orden de descubrimiento y puede referirse a otro disco en una sesión posterior."}
::option[Porque las herramientas de particionado solo aceptan UUID de sistemas de archivos como operandos.]{#disk-partitioning-only-uuid explanation="Los editores suelen operar sobre la ruta de un dispositivo de bloques completo después de verificar su identidad."}
:::

## Examinar un dispositivo con `parted`

Abre el dispositivo completo verificado explícitamente:

```bash
$ sudo parted /dev/VERIFIED-DISK
```

Después selecciona unidades de visualización coherentes y muestra la tabla:

```text
(parted) unit MiB
(parted) print free
```

`print free` muestra las entradas actuales y las regiones sin asignar. Las órdenes de Parted pueden actualizar los metadatos del disco inmediatamente en vez de esperar a una operación final de «guardar», así que trata el prompt interactivo como acceso de escritura activo.

:::single-choice{#disk-partitioning-print-free} ¿Qué ayuda a mostrar `print free` en `parted`?

::option[Archivos que pueden eliminarse para reducir de forma segura cualquier sistema de archivos.]{#disk-partitioning-free-files explanation="Parted lee el diseño de las particiones, no la asignación de archivos del sistema de archivos."}
::option[Todas las copias de seguridad almacenadas en sistemas remotos.]{#disk-partitioning-remote-backups explanation="El inventario de copias remotas está fuera del alcance de un editor de particiones."}
::option[Las entradas de particiones existentes y las regiones sin asignar.]{#disk-partitioning-free-regions .correct explanation="La vista ayuda a elegir límites a partir de la tabla actual y de los huecos restantes."}
:::

## Crear una entrada de partición

La sintaxis exacta de `mkpart` depende del tipo de tabla. Un ejemplo GPT en unidades MiB tiene este aspecto:

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

Esto crea una entrada de partición con un nombre, un tipo de contenido sugerido, un inicio y un final. **No** crea un sistema de archivos ext4. Dar formato es un paso destructivo independiente que se realiza únicamente después de que el kernel reconozca la nueva partición pretendida y se verifique su identidad.

Utiliza la alineación recomendada por la herramienta y comprende si los extremos son inclusivos y cómo se redondean. Examina el resultado con `print` y `lsblk`; no supongas que un límite decimal solicitado se registró exactamente.

:::single-choice{#disk-partitioning-mkpart-effect} ¿Qué crea `mkpart` de `parted`?

::option[Un sistema de archivos ext4 montado que contiene un directorio personal.]{#disk-partitioning-mounted-filesystem explanation="Dar formato y montar son operaciones independientes posteriores a la creación de la partición."}
::option[Una copia de seguridad completa del contenido anterior de la partición.]{#disk-partitioning-automatic-backup explanation="Los editores de particiones no crean automáticamente una copia de recuperación."}
::option[Una entrada en la tabla de particiones, sin dar formato a un sistema de archivos.]{#disk-partitioning-entry-only .correct explanation="El argumento del tipo de sistema de archivos influye en los metadatos de la partición, pero no ejecuta `mkfs`."}
:::

## Redimensionar límites y contenido

`resizepart NUMBER END` mueve únicamente el límite final de una partición. No redimensiona el sistema de archivos ni otra estructura almacenada dentro.

El orden es fundamental:

- Para ampliar, aumenta primero la partición o el dispositivo lógico que contiene los datos y después amplía el sistema de archivos con su herramienta compatible.
- Para reducir, verifica que el sistema de archivos admita la reducción, redúcelo primero respetando sus requisitos de funcionamiento en línea o sin conexión y después reduce el límite del contenedor sin cruzar el nuevo final.

Algunos sistemas de archivos no pueden reducirse. El cifrado, LVM, RAID y los diseños anidados añaden más capas ordenadas. El kernel también puede negarse a volver a leer una tabla modificada mientras los dispositivos estén ocupados, lo que exige un reinicio controlado antes de poder utilizar el nuevo diseño.

:::single-choice{#disk-partitioning-shrink-order} Cuando un sistema de archivos admite la reducción, ¿qué orden evita cortar datos activos?

::option[Reducir primero la partición y después averiguar si cabe el sistema de archivos.]{#disk-partitioning-shrink-partition-first explanation="Acortar primero el contenedor puede truncar estructuras y datos del sistema de archivos."}
::option[Reducir primero el sistema de archivos y después el límite de la partición que lo contiene.]{#disk-partitioning-shrink-filesystem-first .correct explanation="El contenido debe caber dentro del intervalo menor antes de acortar el dispositivo de bloques exterior."}
::option[Eliminar la tabla de particiones y dejar que el sistema de archivos la vuelva a crear.]{#disk-partitioning-delete-table explanation="Un sistema de archivos no reconstruye una tabla de particiones segura como parte de una reducción normal."}
:::

Utiliza [Gestionar particiones y sistemas de archivos de Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) en su disco virtual secundario designado; no lo sustituyas por un disco del equipo anfitrión.

## Resumen

Ahora puedes describir la edición de particiones como una operación destructiva sobre capas de almacenamiento.

1. Selecciona una herramienta compatible con la tabla y el flujo de trabajo reales.
2. Verifica la identidad persistente del disco y desactiva todos sus consumidores.
3. Examina unidades, entradas y regiones libres antes de escribir.
4. Recuerda que `mkpart` no crea un sistema de archivos.
5. Redimensiona el contenido interior y los límites exteriores en el orden seguro.
