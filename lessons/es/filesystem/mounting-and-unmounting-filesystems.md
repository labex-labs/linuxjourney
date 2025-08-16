---
title: "mount y umount"
description: "Aprenda a usar los comandos mount y umount de Linux para administrar sistemas de archivos. Comprenda el montaje, desmontaje de dispositivos y UUID para principiantes."
keywords: "Linux mount, umount command, mount filesystem, Linux UUID, Linux para principiantes, tutorial de Linux, punto de montaje, guía de Linux"
---

## Lesson Content

Antes de poder ver el contenido de su sistema de archivos, deberá montarlo. Para hacer eso, necesitaré la ubicación del dispositivo, el tipo de sistema de archivos y un punto de montaje. El punto de montaje es un directorio en el sistema donde se adjuntará el sistema de archivos. Entonces, básicamente queremos montar nuestro dispositivo en un punto de montaje.

Primero, cree el punto de montaje; en nuestro caso, **mkdir /mydrive**.

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

¡Tan simple como eso! Ahora, cuando vamos a /mydrive, podemos ver el contenido de nuestro sistema de archivos. El **-t** especifica el tipo de sistema de archivos, luego tenemos la ubicación del dispositivo, y luego el punto de montaje.

Para desmontar un dispositivo de un punto de montaje:

```bash
sudo umount /mydrive
```

o

```bash
sudo umount /dev/sdb2
```

Recuerde que el kernel nombra los dispositivos en el orden en que los encuentra. ¿Qué pasa si el nombre de nuestro dispositivo cambia por alguna razón después de montarlo? Bueno, afortunadamente, puede usar el ID universalmente único (UUID) de un dispositivo en lugar de un nombre.

Para ver los UUID en su sistema para dispositivos de bloque:

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

Podemos ver los nombres de nuestros dispositivos, sus tipos de sistema de archivos correspondientes y sus UUID. Ahora, cuando queremos montar algo, podemos usar:

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

La mayoría de las veces, no necesitará montar dispositivos a través de sus UUID; es mucho más fácil usar el nombre del dispositivo, y a menudo el sistema operativo sabrá cómo montar dispositivos comunes como las unidades USB. Sin embargo, si necesita montar automáticamente un sistema de archivos al inicio, como si agregara un disco duro secundario, querrá usar el UUID, y lo veremos en la próxima lección.

## Exercise

Examine la página del manual para `mount` y `umount` y vea qué otras opciones puede usar.

## Quiz Question

¿Qué comando se utiliza para adjuntar un sistema de archivos?

## Quiz Answer

mount
