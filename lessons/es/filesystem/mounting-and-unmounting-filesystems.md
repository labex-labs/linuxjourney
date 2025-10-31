---
index: 6
lang: "es"
title: "montar y desmontar"
meta_title: "mount y umount - El Sistema de Archivos"
meta_description: "Aprenda a usar los comandos mount y umount en Linux para adjuntar y separar sistemas de archivos. Esta guía cubre el montaje de dispositivos, el proceso de sudo umount para un desmontaje seguro en Linux y el uso de UUIDs."
meta_keywords: "mount, umount, sudo umount, umount linux, desmontar linux, debian umount, montar sistema de archivos, desmontar dispositivo, Linux UUID, punto de montaje"
---

## Lesson Content

Antes de poder acceder a los archivos de un dispositivo de almacenamiento, primero debe montar su sistema de archivos en un directorio de su sistema. Este proceso implica una ubicación del dispositivo, un tipo de sistema de archivos y un punto de montaje. El punto de montaje es simplemente un directorio existente donde se adjuntará el sistema de archivos.

### Cómo Montar un Sistema de Archivos

Primero, necesita crear un punto de montaje. Creemos un directorio para este propósito:

```bash
sudo mkdir /mydrive
```

Con el punto de montaje listo, puede usar el comando `mount` para adjuntar su dispositivo. La bandera `-t` especifica el tipo de sistema de archivos.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

¡Así de simple! Ahora, si navega al directorio `/mydrive`, verá el contenido del sistema de archivos de su dispositivo.

### Cómo Desmontar un Sistema de Archivos en Linux

Cuando haya terminado con un dispositivo, debe desmontarlo para asegurarse de que todos los datos se escriban de forma segura y el sistema de archivos se separe limpiamente. El comando estándar para esta operación en Linux es `umount`. Para realizar un `linux unmount`, puede especificar el punto de montaje o el nombre del dispositivo.

Usando el punto de montaje:

```bash
sudo umount /mydrive
```

Alternativamente, usando el nombre del dispositivo:

```bash
sudo umount /dev/sdb2
```

Es una buena práctica usar `sudo umount` para asegurar que tiene los permisos necesarios para separar el sistema de archivos. Este comando es universal en las distribuciones de Linux, por lo que la misma sintaxis se aplica si está en Ubuntu, Fedora o realizando un `debian umount`. Tenga en cuenta que no puede `umount` un dispositivo si está actualmente en uso (por ejemplo, si un archivo está abierto o su directorio de trabajo actual está en el dispositivo).

### Uso de UUIDs para un Montaje Estable

El kernel nombra los dispositivos en el orden en que los descubre, lo que significa que un nombre de dispositivo como `/dev/sdb2` podría cambiar entre reinicios. Para evitar problemas, puede usar la identificación única universal (UUID) de un dispositivo, que permanece constante.

Para ver los UUIDs de sus dispositivos de bloque, use el comando `blkid`:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Esta salida muestra los nombres de los dispositivos, sus tipos de sistema de archivos y sus UUIDs correspondientes. Luego puede montar un dispositivo usando su UUID:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

Aunque no siempre necesitará montar dispositivos a través de sus UUIDs, es el método recomendado para montar sistemas de archivos automáticamente al inicio, como un disco duro secundario. Cubriremos ese proceso en la próxima lección.

## Exercise

¡La práctica hace al maestro! Aquí hay un laboratorio práctico para reforzar su comprensión de la gestión de sistemas de archivos de Linux:

- **[Administrar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - En este laboratorio, aprenderá a administrar particiones de disco y sistemas de archivos en Linux. Usará fdisk para crear una nueva partición, formatearla con ext4, montarla, configurar el montaje persistente en /etc/fstab y crear una partición swap, todo en un disco virtual secundario seguro.

Este laboratorio le ayudará a aplicar los conceptos de montaje y desmontaje en escenarios reales y a ganar confianza con la gestión de sistemas de archivos.

## Quiz Question

¿Qué comando se utiliza para adjuntar un sistema de archivos? (Por favor, use una sola palabra en inglés en minúsculas para su respuesta.)

## Quiz Answer

mount
