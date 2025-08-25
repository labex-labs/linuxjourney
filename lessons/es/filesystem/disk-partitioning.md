---
index: 4
lang: "es"
title: "Particionado de Disco"
meta_title: "Particionado de Disco - El Sistema de Archivos"
meta_description: "Aprende el particionado de discos en Linux usando parted. Entiende cómo particionar, seleccionar, ver y redimensionar discos. ¡Comienza con esta guía amigable para principiantes!"
meta_keywords: "Particionado de disco Linux, comando parted, fdisk, gparted, tutorial Linux, Linux para principiantes, gestión de discos, guía Linux"
---

## Lesson Content

Hagamos algo práctico con los sistemas de archivos trabajando en el proceso en una unidad USB. Si no tienes una, no te preocupes, aún puedes seguir estas próximas dos lecciones.

Primero, necesitaremos particionar nuestro disco. Hay muchas herramientas disponibles para hacer esto:

- fdisk - herramienta básica de particionado de línea de comandos; no soporta GPT
- parted - esta es una herramienta de línea de comandos que soporta particionado MBR y GPT
- gparted - esta es la versión GUI de parted
- gdisk - fdisk, pero no soporta MBR, solo GPT

Usemos parted para nuestro particionado. Digamos que conecto el dispositivo USB y vemos que el nombre del dispositivo es /dev/sdb2.

### Iniciar parted

```bash
sudo parted
```

Entrarás en la herramienta parted; aquí puedes ejecutar comandos para particionar tu dispositivo.

### Seleccionar el dispositivo

```bash
select /dev/sdb2
```

Para seleccionar el dispositivo con el que trabajarás, selecciónalo por su nombre de dispositivo.

### Ver la tabla de particiones actual

```plaintext
(parted) print
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

Aquí verás las particiones disponibles en el dispositivo. Los puntos de **inicio** y **fin** son donde las particiones ocupan espacio en el disco duro; querrás encontrar una buena ubicación de inicio y fin para tus particiones.

### Particionar el dispositivo

```bash
mkpart primary 123 4567
```

Ahora solo elige un punto de inicio y fin y crea la partición; necesitarás especificar el tipo de partición dependiendo de la tabla que usaste.

### Redimensionar una partición

También puedes redimensionar una partición si no tienes espacio.

```bash
resize 2 1245 3456
```

Selecciona el número de partición y luego los puntos de inicio y fin a los que quieres redimensionarla.

Parted es una herramienta muy potente, y debes tener cuidado al particionar tus discos.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del particionado de discos y la gestión de sistemas de archivos en Linux:

1. [Administrar particiones y sistemas de archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845) - En este laboratorio, aprenderás a administrar particiones de disco y sistemas de archivos en Linux. Usarás fdisk para crear una nueva partición, formatearla con ext4, montarla, configurar el montaje persistente en /etc/fstab y crear una partición de intercambio, todo en un disco virtual secundario seguro.

Este laboratorio te ayudará a aplicar los conceptos de particionado de discos y gestión de sistemas de archivos en un escenario real y a ganar confianza con estas habilidades esenciales de administración de Linux.

## Quiz Question

¿Cuál es el comando parted para crear una partición?

## Quiz Answer

mkpart
