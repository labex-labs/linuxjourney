---
lang: "es"
title: "Anatomía de un Disco"
meta_title: "Anatomía de un Disco - El Filesystem"
meta_description: "Aprenda sobre el particionamiento de discos en Linux, MBR vs. GPT y la estructura del sistema de archivos. Comprenda las particiones, las tablas y cómo organizar los datos. ¡Comience con esta guía para principiantes!"
meta_keywords: "particionamiento de disco Linux, MBR, GPT, estructura del sistema de archivos, particiones Linux, principiante, tutorial, guía"
---

## Lesson Content

Los discos duros pueden subdividirse en particiones, creando esencialmente múltiples dispositivos de bloque. Recuerde ejemplos como `/dev/sda1` y `/dev/sda2`. `/dev/sda` es el disco completo, pero `/dev/sda1` es la primera partición de ese disco. Las particiones son extremadamente útiles para separar datos, y si necesita un determinado filesystem, puede crear fácilmente una partición en lugar de hacer que todo el disco sea de un solo tipo de filesystem.

### Partition Table

Cada disco tendrá una partition table. Esta tabla le dice al sistema cómo está particionado el disco. Esta tabla le indica dónde comienzan y terminan las particiones, qué particiones son bootable, qué sectores del disco están asignados a qué partición, etc. Se utilizan dos esquemas principales de partition table: Master Boot Record (MBR) y GUID Partition Table (GPT).

### Partition

Los discos están compuestos por particiones que nos ayudan a organizar nuestros datos. Puede tener múltiples particiones en un disco, y no pueden superponerse entre sí. Si hay espacio que no está asignado a una partición, se conoce como free space. Los tipos de particiones dependen de su partition table. Dentro de una partición, puede tener un filesystem o dedicar una partición a otras cosas como swap (lo veremos pronto).

_MBR_

- Partition table tradicional, se usaba como estándar
- Puede tener primary, extended y logical partitions
- MBR tiene un límite de cuatro primary partitions
- Se pueden crear particiones adicionales convirtiendo una primary partition en una extended partition (solo puede haber una extended partition en un disco). Luego, dentro de la extended partition, se añaden logical partitions. Las logical partitions se usan como cualquier otra partición. Es tonto, lo sé.
- Soporta discos de hasta 2 terabytes

_GPT_

- GUID Partition Table (GPT) se está convirtiendo en el nuevo estándar para el particionamiento de discos
- Tiene un solo tipo de partición, y se pueden crear muchas de ellas
- Cada partición tiene un Globally Unique ID (GUID)
- Se usa principalmente en conjunto con el arranque basado en UEFI (entraremos en detalles en otro curso)

### Filesystem Structure

Sabemos por nuestra lección anterior que un filesystem es una colección organizada de files y directories. En su forma más simple, se compone de una database para gestionar files y los files en sí mismos; sin embargo, vamos a entrar en un poco más de detalle.

- Boot block - Esto se encuentra en los primeros sectores del filesystem, y realmente no es utilizado por el filesystem. Más bien, contiene información utilizada para arrancar el operating system. El operating system solo necesita un boot block. Si tiene múltiples particiones, tendrán boot blocks, pero muchos de ellos no se utilizan.
- Super block - Este es un single block que viene después del boot block, y contiene información sobre el filesystem, como el size de la inode table, size de los logical blocks, y el size del filesystem.
- Inode table - Piense en esto como la database que gestiona nuestros files (tenemos una lección completa sobre inodes, así que no se preocupe). Cada file o directory tiene una unique entry en la inode table, y tiene diversa información sobre el file.
- Data blocks - Esta es la actual data para los files y directories.

Echemos un vistazo a las diferentes partition tables. A continuación se muestra un ejemplo de una partición que utiliza la tabla de particiones MBR (msdos). Puede ver las primary, extended y logical partitions en la máquina.

```plaintext
pete@icebox:~$ sudo parted -l
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

Este ejemplo es GPT, usando solo un unique ID para las particiones.

```plaintext
Model: Thumb Drive (scsi)
Disk /dev/sdb: 4041MB
Sector size (logical/physical): 512B/512B
Partition Table: gpt

Number  Start   End     Size     File system  Name        Flags
 1      17.4kB  1000MB  1000MB                first
 2      1000MB  4040MB  3040MB                second
```

## Exercise

Ejecute **parted -l** en su máquina y evalúe sus resultados.

## Quiz Question

¿Qué tipo de partición se utiliza para crear más de 4 particiones en el esquema de particionamiento MBR?

## Quiz Answer

extended
