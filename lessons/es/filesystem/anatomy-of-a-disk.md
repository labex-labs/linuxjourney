---
index: 3
lang: "es"
title: "Anatomía de un Disco"
meta_title: "Anatomía de un Disco - El Sistema de Archivos"
meta_description: "Explora la anatomía de un disco en Linux. Esta guía explica qué componente de un disco le indica al sistema operativo cómo está particionado, cubriendo tablas de partición MBR y GPT, diferentes tipos de particiones de Linux y cómo se organizan."
meta_keywords: "disco en linux, particiones linux, tipos de particiones linux, qué componente de un disco le dice al SO cómo está particionado el disco, qué contiene información sobre cómo se organizan las particiones del disco duro, MBR, GPT, tabla de particiones, sistema de archivos"
---

## Lesson Content

Un disco duro en Linux se puede subdividir en particiones, que funcionan como dispositivos de bloque individuales. Quizás recuerdes ejemplos como /dev/sda1 y /dev/sda2. Aquí, /dev/sda representa el disco completo, mientras que /dev/sda1 es la primera partición de ese disco. Las particiones son increíblemente útiles para separar datos. Si necesitas un sistema de archivos específico para una porción de tu almacenamiento, puedes crear una nueva partición para ello en lugar de formatear todo el disco.

### La Tabla de Particiones

Entonces, ¿qué componente de un disco le dice al sistema operativo cómo está particionado el disco? La respuesta es la **tabla de particiones**. Este componente crucial contiene información sobre cómo se organizan las particiones del disco duro. La tabla de particiones especifica dónde comienza y termina cada partición, qué particiones son arrancables y qué sectores del disco se asignan a cada partición. Hay dos esquemas principales de tabla de particiones: Master Boot Record (MBR) y GUID Partition Table (GPT).

### Entendiendo las Particiones de Linux

Los discos están compuestos de particiones que nos ayudan a organizar nuestros datos. Puedes tener múltiples particiones en un solo disco, pero no pueden superponerse. Cualquier espacio en el disco no asignado a una partición se conoce como espacio libre. Los tipos de particiones de Linux disponibles dependen del esquema de tabla de particiones que utilices. Dentro de una partición, puedes crear un sistema de archivos o dedicarla a otros propósitos, como el espacio de intercambio (swap).

### Particiones MBR

El Master Boot Record (MBR) es el estándar tradicional de tabla de particiones.

- Admite particiones primarias, extendidas y lógicas.
- MBR tiene un límite de cuatro particiones primarias.
- Para crear más particiones, una partición primaria debe designarse como partición extendida (solo se permite una por disco). Dentro de esta partición extendida, puedes crear múltiples particiones lógicas, que funcionan como cualquier otra partición.
- Admite discos de hasta 2 terabytes de tamaño.

### Particiones GPT

La GUID Partition Table (GPT) es el estándar moderno para el particionamiento de discos.

- Solo tiene un tipo de partición y puedes crear una gran cantidad de ellas.
- A cada partición se le asigna un Identificador Único Global (GUID).
- GPT se usa comúnmente con sistemas de arranque basados en UEFI.

### Estructura del Sistema de Archivos

Como aprendimos anteriormente, un sistema de archivos es una colección organizada de archivos y directorios. En esencia, consta de una base de datos para administrar archivos y los archivos en sí. Exploremos su estructura con más detalle.

- **Bloque de arranque (Boot block)**: Ubicado en los primeros sectores de un sistema de archivos, este bloque no es utilizado por el sistema de archivos en sí. En cambio, contiene información utilizada para arrancar el sistema operativo. Solo se necesita un bloque de arranque por sistema operativo. Aunque otras particiones pueden tener bloques de arranque, a menudo no se utilizan.
- **Superbloque (Superblock)**: Es un único bloque que sigue al bloque de arranque y contiene metadatos sobre el sistema de archivos, como el tamaño de la tabla de inodos, el tamaño de los bloques lógicos y el tamaño total del sistema de archivos.
- **Tabla de inodos (Inode table)**: Esta es la base de datos que administra archivos y directorios. Cada archivo o directorio tiene una entrada única en la tabla de inodos, que almacena varios atributos sobre él. Cubriremos los inodos en una lección dedicada.
- **Bloques de datos (Data blocks)**: Aquí es donde se almacena el contenido real de tus archivos y directorios.

A continuación se muestra un ejemplo de un disco que utiliza la tabla de particiones MBR (etiquetada como `msdos`). Puedes ver las particiones primaria, extendida y lógica.

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

Este segundo ejemplo muestra una tabla de particiones GPT, que utiliza identificadores únicos para sus particiones.

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

Para reforzar tu comprensión del particionamiento de discos y los sistemas de archivos, te recomendamos este laboratorio práctico:

1. **[Administrar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practica la creación de nuevas particiones, formateándolas con sistemas de archivos como ext4, montándolas y configurando el montaje persistente en /etc/fstab.

Este laboratorio te ayudará a aplicar conceptos de administración de discos en escenarios del mundo real y a ganar confianza con el almacenamiento de Linux.

## Quiz Question

¿Qué tipo de partición se utiliza para crear más de 4 particiones en el esquema de particionamiento MBR? (Por favor, responde en una sola palabra en inglés en minúsculas.)

## Quiz Answer

extended
