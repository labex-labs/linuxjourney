---
lesson_id: "anatomy-of-a-disk"
course_id: "filesystem"
lang: "es"
order_index: 3
title: "Anatomía de un disco"
description: "Aprende cómo los dispositivos de bloques, las tablas de particiones, las particiones y los sistemas de archivos forman capas distintas de almacenamiento."
meta_title: "Anatomía de un disco - El sistema de archivos"
meta_description: "Explora las capas de un disco Linux y comprende las tablas MBR y GPT, las particiones y los sistemas de archivos."
meta_keywords: "disco Linux, particiones Linux, MBR, GPT, tabla de particiones, sistema de archivos"
---

Un dispositivo de almacenamiento se expone como dispositivo de bloques, por ejemplo `/dev/sda` o `/dev/nvme0n1`. Puede contener una tabla de particiones cuyas entradas describen regiones expuestas como dispositivos de bloques hijos. Una partición puede contener un sistema de archivos, una firma de intercambio, un miembro RAID, un contenedor cifrado, un volumen físico de volúmenes lógicos u otro formato de datos.

Estas capas son independientes: no todos los discos tienen una tabla de particiones, no todas las particiones contienen un sistema de archivos y un sistema de archivos puede residir en un volumen lógico o en un dispositivo completo.

## Tablas de particiones y límites

Una tabla de particiones registra posiciones iniciales, longitudes, identificadores de tipo y atributos específicos del esquema. El kernel la lee para crear dispositivos de bloques de particiones como `/dev/sda1` o `/dev/nvme0n1p1`.

En los diseños ordinarios, los límites de las particiones no deben solaparse. El espacio situado fuera de todas las entradas está sin asignar desde la perspectiva de la tabla, aunque todavía puede contener firmas o datos antiguos. Cambiar una tabla no traslada automáticamente el contenido de un sistema de archivos para que coincida con los nuevos límites.

:::single-choice{#anatomy-disk-partition-table-role} ¿Qué indica al sistema operativo dónde comienzan y terminan las particiones del disco?

::option[El directorio de trabajo actual del shell.]{#anatomy-disk-shell-directory explanation="Una ruta del shell no interviene en los límites de las particiones en disco."}
::option[La tabla de particiones del disco.]{#anatomy-disk-table-boundaries .correct explanation="Las entradas de particiones describen regiones que el kernel puede exponer como dispositivos de bloques hijos."}
::option[El grupo principal de la cuenta de usuario.]{#anatomy-disk-user-group explanation="Las credenciales de las cuentas no definen la geometría ni el diseño de las particiones."}
:::

## Particionado MBR

El esquema heredado DOS/MBR almacena su tabla principal en el primer sector lógico. Tiene cuatro entradas principales. Una entrada puede describir una partición extendida que actúa como contenedor de una serie enlazada de particiones lógicas, lo que permite más de cuatro regiones utilizables.

Con direcciones de sector de 32 bits y sectores lógicos de 512 bytes, MBR alcanza el límite citado habitualmente de unos 2 TiB. La capacidad de direccionamiento exacta depende del tamaño del sector y de la compatibilidad de las herramientas. MBR tampoco tiene las copias redundantes de cabecera y tabla ni los GUID por partición de GPT.

:::single-choice{#anatomy-disk-mbr-more-than-four} ¿Qué elemento de MBR permite disponer de más de cuatro particiones utilizables?

::option[Una partición de diario que contiene más entradas principales.]{#anatomy-disk-mbr-journal explanation="El journaling del sistema de archivos no guarda relación con la tabla MBR de cuatro entradas."}
::option[Una partición extendida que contiene particiones lógicas.]{#anatomy-disk-mbr-extended .correct explanation="Una entrada principal puede definir un contenedor extendido dentro del cual se enlazan particiones lógicas."}
::option[Un superbloque del sistema de archivos que vuelve a numerar las entradas.]{#anatomy-disk-mbr-superblock explanation="Los metadatos de un sistema de archivos no amplían la tabla de particiones del disco."}
:::

## Particionado GPT

La tabla de particiones GUID, o GPT, utiliza direcciones de bloques lógicos de 64 bits y suele almacenar una cabecera y una matriz de entradas principales cerca del principio, además de copias de respaldo cerca del final del disco. Un MBR protector ayuda a evitar que el software antiguo que solo comprende MBR trate el disco como vacío.

Cada entrada GPT incluye un GUID de tipo de partición y un GUID de partición único; por tanto, GPT no tiene un único tipo de partición. El número de entradas disponibles lo determinan la tabla asignada y las herramientas, y suele ser muy superior a cuatro sin utilizar particiones extendidas ni lógicas.

GPT se utiliza normalmente en discos de arranque UEFI, pero el particionado y el modo de arranque del firmware son conceptos distintos. Un sistema UEFI también necesita archivos de arranque apropiados y una partición del sistema EFI; GPT por sí solo no hace que un disco sea arrancable.

:::single-choice{#anatomy-disk-gpt-identifiers} ¿Qué identificadores incluye una entrada de partición GPT?

::option[Un GUID de tipo y un GUID de partición único.]{#anatomy-disk-gpt-guids .correct explanation="El tipo describe el uso previsto, mientras que el GUID único identifica esa entrada de partición concreta."}
::option[Únicamente un tipo universal compartido por todas las particiones GPT.]{#anatomy-disk-gpt-one-type explanation="GPT define numerosos GUID de tipo para distintos usos de particiones."}
::option[El UID y el GID de inicio de sesión del usuario que la creó.]{#anatomy-disk-gpt-user-ids explanation="Los identificadores de cuentas del sistema de archivos no son campos de identidad de particiones GPT."}
:::

## Las estructuras del sistema de archivos dependen del formato

Después de particionar, una herramienta de creación de sistemas de archivos escribe las estructuras definidas por ese sistema. Muchos formatos tienen conceptos como superbloques, metadatos de asignación, registros de directorios y extensiones o bloques de datos, pero su diseño, redundancia y terminología difieren.

Por ejemplo, los sistemas de archivos ext utilizan inodos y grupos de bloques, mientras que otros organizan los metadatos mediante árboles o estructuras de asignación diferentes. No apliques a todos los sistemas de archivos un diagrama simplificado de «bloque de arranque, un superbloque, tabla de inodos y bloques de datos».

:::single-choice{#anatomy-disk-filesystem-layer} ¿Crear una partición crea automáticamente un sistema de archivos dentro de ella?

::option[No; darle formato u otro uso explícito es un paso independiente.]{#anatomy-disk-partition-not-filesystem .correct explanation="La tabla de particiones solo define una región de bloques; su contenido permanece independiente."}
::option[Sí; todas las particiones se formatean automáticamente como ext4.]{#anatomy-disk-auto-ext4 explanation="Las herramientas de particionado no crean universalmente un sistema de archivos ext4."}
::option[Sí; las entradas GPT son directorios montados.]{#anatomy-disk-gpt-mounted explanation="Una entrada de partición describe almacenamiento y no es un punto de montaje de un sistema de archivos."}
:::

## Examinar el diseño actual

Utiliza vistas de solo lectura antes de cualquier modificación:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,PTTYPE,PARTTYPE,FSTYPE,MOUNTPOINTS
$ sudo parted --list
```

`PTTYPE` describe el esquema de tabla de particiones detectado, `PARTTYPE` un identificador de tipo de partición y `FSTYPE` una firma de contenido detectada. La detección es una prueba, no una garantía de que el contenido esté sano o sea seguro montarlo.

Los nombres de dispositivos pueden cambiar y las firmas obsoletas pueden confundir la detección. Confirma el modelo, el número de serie, el tamaño, el transporte, los enlaces persistentes, los montajes activos, el intercambio, RAID, LVM, el cifrado y las copias de seguridad antes de abrir cualquier herramienta de particionado en modo de escritura.

:::single-choice{#anatomy-disk-lsblk-fields} ¿Qué campo de `lsblk` distingue el contenido detectado del sistema de archivos del esquema de la tabla de particiones?

::option[`FSTYPE`]{#anatomy-disk-fstype .correct explanation="`FSTYPE` comunica un sistema de archivos detectado u otra firma de contenido reconocida, mientras que `PTTYPE` comunica el esquema de la tabla."}
::option[`NAME`]{#anatomy-disk-name-field explanation="`NAME` etiqueta la entrada de dispositivo de bloques del kernel y no identifica específicamente el formato del contenido."}
::option[`SIZE`]{#anatomy-disk-size-field explanation="El tamaño comunica la capacidad, no el tipo de sistema de archivos."}
:::

Utiliza [Gestionar particiones y sistemas de archivos de Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) únicamente sobre almacenamiento desechable para practicar estas capas.

## Resumen

Ahora puedes separar los metadatos del diseño del disco de los formatos de datos almacenados en él.

1. Identifica los dispositivos completos y sus dispositivos de particiones hijos.
2. Relaciona las particiones extendidas MBR con el límite heredado de cuatro entradas.
3. Relaciona GPT con tablas redundantes y GUID por partición.
4. Trata la creación del sistema de archivos como algo independiente de crear la partición.
5. Examina todas las capas de almacenamiento y consumidores activos antes de realizar cambios.
