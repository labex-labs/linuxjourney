---
index: 4
lang: "es"
title: "Particionamiento de Discos"
meta_title: "Particionamiento de Discos - El Sistema de Archivos"
meta_description: "Aprenda el particionamiento de discos en Linux con el comando parted. Esta guía cubre cómo ver particiones con `sudo parted -l`, crearlas y redimensionarlas. También presenta gparted, una alternativa gráfica popular."
meta_keywords: "Particionamiento de discos Linux, comando parted, sudo parted -l, gparted, alternativa gparted windows, fdisk, gestión de discos, crear partición, redimensionar partición, guía Linux"
---

## Lesson Content

Esta lección proporciona una guía práctica para administrar sistemas de archivos particionando un disco, como una unidad USB. Si no tienes una unidad de repuesto, aún puedes seguir el proceso para comprender los conceptos.

Primero, necesitaremos particionar nuestro disco. Hay muchas herramientas disponibles para esta tarea:

- **fdisk**: Una herramienta básica de particionamiento por línea de comandos; no admite GPT.
- **parted**: Una potente herramienta de línea de comandos que admite el particionamiento MBR y GPT.
- **gparted**: La versión gráfica de `parted`. Para los usuarios que prefieren una interfaz visual, `gparted` es una herramienta intuitiva, a menudo considerada una excelente `gparted windows alternative`.
- **gdisk**: Similar a `fdisk`, pero solo admite GPT.

Usaremos `parted` para nuestros ejemplos.

### Listar Particiones Existentes

Antes de realizar cambios, es crucial identificar su disco y su diseño actual. Una forma rápida de hacerlo es con el comando `sudo parted -l`, que enumera las tablas de particiones de todos los dispositivos de bloque conectados.

```bash
sudo parted -l
```

Este comando le ayuda a encontrar el nombre de dispositivo correcto, como `/dev/sdb`, antes de comenzar a modificarlo.

### Iniciar el Modo Interactivo

Para comenzar a realizar cambios, inicie `parted` en modo interactivo. Supongamos que su dispositivo de destino es `/dev/sdb`.

```bash
sudo parted
```

Ingresará al shell de la herramienta `parted`, donde puede ejecutar comandos para administrar las particiones de su dispositivo.

### Seleccionar un Dispositivo

Una vez dentro del shell de `parted`, debe seleccionar el disco que desea modificar. Tenga mucho cuidado de elegir el correcto para evitar la pérdida de datos.

```bash
select /dev/sdb
```

### Ver la Tabla de Particiones

Use el comando `print` para mostrar la tabla de particiones del disco seleccionado.

```plaintext
(parted) print
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sdb: 10.7GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Disk Flags:

Number  Start   End     Size    Type      File system  Flags
 1      1049kB  10.7GB  10.7GB  primary   ext4         boot
```

Esta salida muestra las particiones disponibles en el dispositivo. Las columnas **Start** (Inicio) y **End** (Fin) indican dónde se encuentra cada partición en el disco.

### Crear una Partición

El comando `mkpart` crea una nueva partición. Debe especificar el tipo de partición (ejemplo: `primary`), un tipo de sistema de archivos opcional, y los puntos de inicio y fin.

```bash
mkpart primary ext4 1MB 5000MB
```

Este comando crea una partición primaria formateada con ext4, que comienza en 1MB y termina en 5000MB.

### Redimensionar una Partición

También puede cambiar el tamaño de una partición existente con el comando `resize`. Necesitará el número de partición y los nuevos puntos de inicio y fin.

```bash
resize 1 1MB 8000MB
```

Este comando redimensiona la partición número 1 para que termine en la marca de 8000MB.

`parted` es una herramienta muy potente. Siempre revise dos veces sus comandos antes de ejecutarlos para prevenir la pérdida accidental de datos.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del particionamiento de discos y la administración de sistemas de archivos en Linux:

1. [Administrar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845) - En este laboratorio, aprenderá a administrar particiones de disco y sistemas de archivos en Linux. Usará fdisk para crear una nueva partición, formatearla con ext4, montarla, configurar el montaje persistente en /etc/fstab y crear una partición swap, todo en un disco virtual secundario seguro.

Este laboratorio le ayudará a aplicar los conceptos de particionamiento de discos y administración de sistemas de archivos en un escenario real y a ganar confianza con estas habilidades esenciales de administración de Linux.

## Quiz Question

What is the `parted` command to make a partition? (Please answer in English, paying attention to case sensitivity).

## Quiz Answer

mkpart
