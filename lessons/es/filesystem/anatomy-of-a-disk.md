---
index: 3
lang: "es"
title: "Anatomía de un Disco"
meta_title: "Anatomía de un Disco - El Sistema de Archivos"
meta_description: "Aprenda sobre el particionamiento de discos Linux, MBR vs. GPT y la estructura del sistema de archivos. Comprenda las particiones, tablas y cómo organizar los datos. ¡Comience con esta guía para principiantes!"
meta_keywords: "particionamiento de disco Linux, MBR, GPT, estructura del sistema de archivos, particiones Linux, principiante, tutorial, guía"
---

## Lesson Content

Los discos duros pueden subdividirse en particiones, creando esencialmente múltiples dispositivos de bloque. Recordemos ejemplos como `/dev/sda1` y `/dev/sda2`. `/dev/sda` es el disco completo, pero `/dev/sda1` es la primera partición de ese disco. Las particiones son extremadamente útiles para separar datos, y si necesita un determinado sistema de archivos, puede crear fácilmente una partición en lugar de hacer que todo el disco sea de un solo tipo de sistema de archivos.

### Tabla de Particiones

Cada disco tendrá una tabla de particiones. Esta tabla le dice al sistema cómo está particionado el disco. Esta tabla le indica dónde comienzan y terminan las particiones, qué particiones son arrancables, qué sectores del disco están asignados a qué partición, etc. Se utilizan dos esquemas principales de tabla de particiones: Master Boot Record (MBR) y GUID Partition Table (GPT).

### Partición

Los discos están compuestos por particiones que nos ayudan a organizar nuestros datos. Puede tener múltiples particiones en un disco, y no pueden superponerse entre sí. Si hay espacio que no está asignado a una partición, se conoce como espacio libre. Los tipos de particiones dependen de su tabla de particiones. Dentro de una partición, puede tener un sistema de archivos o dedicar una partición a otras cosas como swap (pronto llegaremos a eso).

_MBR_

- Tabla de particiones tradicional, se usaba como estándar
- Puede tener particiones primarias, extendidas y lógicas
- MBR tiene un límite de cuatro particiones primarias
- Se pueden crear particiones adicionales convirtiendo una partición primaria en una partición extendida (solo puede haber una partición extendida en un disco). Luego, dentro de la partición extendida, se añaden particiones lógicas. Las particiones lógicas se usan como cualquier otra partición. Tonto, lo sé.
- Soporta discos de hasta 2 terabytes

_GPT_

- GUID Partition Table (GPT) se está convirtiendo en el nuevo estándar para el particionamiento de discos
- Tiene un solo tipo de partición, y se pueden hacer muchas de ellas
- Cada partición tiene un ID globalmente único (GUID)
- Se usa principalmente junto con el arranque basado en UEFI (entraremos en detalles en otro curso)

### Estructura del Sistema de Archivos

Sabemos por nuestra lección anterior que un sistema de archivos es una colección organizada de archivos y directorios. En su forma más simple, se compone de una base de datos para administrar archivos y los archivos en sí; sin embargo, vamos a entrar en un poco más de detalle.

- Boot block - Esto se encuentra en los primeros sectores del sistema de archivos, y realmente no es utilizado por el sistema de archivos. Más bien, contiene información utilizada para arrancar el sistema operativo. El sistema operativo solo necesita un boot block. Si tiene varias particiones, tendrán boot blocks, pero muchos de ellos no se utilizan.
- Super block - Este es un solo bloque que viene después del boot block, y contiene información sobre el sistema de archivos, como el tamaño de la tabla de inodos, el tamaño de los bloques lógicos y el tamaño del sistema de archivos.
- Inode table - Piense en esto como la base de datos que administra nuestros archivos (tenemos una lección completa sobre inodos, así que no se preocupe). Cada archivo o directorio tiene una entrada única en la tabla de inodos, y tiene diversa información sobre el archivo.
- Data blocks - Estos son los datos reales de los archivos y directorios.

Echemos un vistazo a las diferentes tablas de particiones. A continuación se muestra un ejemplo de una partición que utiliza la tabla de particiones MBR (msdos). Puede ver las particiones primarias, extendidas y lógicas en la máquina.

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

Este ejemplo es GPT, usando solo un ID único para las particiones.

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

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del particionamiento de discos y los sistemas de archivos:

1. **[Administrar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practique la creación de nuevas particiones, formateándolas con sistemas de archivos como ext4, montándolas y configurando el montaje persistente en `/etc/fstab`.

Este laboratorio le ayudará a aplicar los conceptos de administración de discos en escenarios reales y a generar confianza con el almacenamiento de Linux.

## Quiz Question

¿Qué tipo de partición se utiliza para crear más de 4 particiones en el esquema de particionamiento MBR?

## Quiz Answer

extended
