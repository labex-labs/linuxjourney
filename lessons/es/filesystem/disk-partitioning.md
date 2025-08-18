---
lang: "es"
title: "Particionado de Discos"
meta_description: "Aprende el particionado de discos en Linux usando parted. Entiende cómo particionar, seleccionar, ver y redimensionar discos. ¡Empieza con esta guía para principiantes!"
meta_keywords: "particionado de disco Linux, comando parted, fdisk, gparted, tutorial Linux, Linux para principiantes, gestión de discos, guía Linux"
---

## Lesson Content

Hagamos algunas cosas prácticas con los sistemas de archivos trabajando a través del proceso en una unidad USB. Si no tienes una, no te preocupes, aún puedes seguir estas próximas lecciones.

Primero, necesitaremos particionar nuestro disco. Hay muchas herramientas disponibles para hacer esto:

- fdisk - herramienta básica de particionado de línea de comandos; no soporta GPT
- parted - esta es una herramienta de línea de comandos que soporta particionado MBR y GPT
- gparted - esta es la versión GUI de parted
- gdisk - fdisk, pero no soporta MBR, solo GPT

Usemos parted para hacer nuestro particionado. Digamos que conecto el dispositivo USB y vemos que el nombre del dispositivo es /dev/sdb2.

### Launch parted

```bash
sudo parted
```

Entrarás en la herramienta parted; aquí puedes ejecutar comandos para particionar tu dispositivo.

### Select the device

```bash
select /dev/sdb2
```

Para seleccionar el dispositivo con el que trabajarás, selecciónalo por su nombre de dispositivo.

### View current partition table

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

Aquí verás las particiones disponibles en el dispositivo. Los puntos **start** y **end** son donde las particiones ocupan espacio en el disco duro; querrás encontrar una buena ubicación de inicio y fin para tus particiones.

### Partition the device

```bash
mkpart primary 123 4567
```

Ahora solo elige un punto de inicio y fin y haz la partición; necesitarás especificar el tipo de partición dependiendo de la tabla que usaste.

### Resize a partition

También puedes redimensionar una partición si no tienes espacio.

```bash
resize 2 1245 3456
```

Selecciona el número de partición y luego los puntos de inicio y fin a los que quieres redimensionarla.

Parted es una herramienta muy potente, y debes tener cuidado al particionar tus discos.

## Exercise

Particiona una unidad USB con la mitad de la unidad como ext4 y la otra mitad como espacio libre.

## Quiz Question

¿Cuál es el comando parted para crear una partición?

## Quiz Answer

mkpart
