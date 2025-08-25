---
index: 2
lang: "es"
title: "Tipos de Sistemas de Archivos"
meta_title: "Tipos de Sistemas de Archivos - El Sistema de Archivos"
meta_description: "Aprenda sobre los tipos de sistemas de archivos de Linux como ext4, Btrfs y XFS. Comprenda el registro (journaling) y VFS para datos consistentes. Explore los sistemas de archivos comunes de Linux en esta guía para principiantes."
meta_keywords: "tipos de sistemas de archivos Linux, ext4, Btrfs, XFS, journaling, VFS, tutorial Linux, guía para principiantes"
---

## Lesson Content

Existen muchas implementaciones diferentes de sistemas de archivos. Algunos son más rápidos que otros, algunos soportan almacenamiento de mayor capacidad y otros solo funcionan en almacenamiento de menor capacidad. Los diferentes sistemas de archivos tienen diferentes formas de organizar sus datos, y entraremos en detalle sobre qué tipos de sistemas de archivos existen. Dado que hay tantas implementaciones diferentes disponibles, las aplicaciones necesitan una forma de manejar las diferentes operaciones. Por lo tanto, existe algo llamado capa de abstracción del Sistema de Archivos Virtual (VFS). Es una capa entre las aplicaciones y los diferentes tipos de sistemas de archivos, por lo que no importa qué sistema de archivos tenga, sus aplicaciones podrán trabajar con él.

Puede tener muchos sistemas de archivos en sus discos, dependiendo de cómo estén particionados, y lo veremos en una próxima lección.

### Registro (Journaling)

El registro (journaling) viene por defecto en la mayoría de los tipos de sistemas de archivos, pero en caso de que no sea así, debe saber lo que hace. Digamos que está copiando un archivo grande y de repente pierde la energía. Bueno, si está en un sistema de archivos sin registro, el archivo terminaría corrupto y su sistema de archivos sería inconsistente. Luego, cuando vuelva a arrancar, su sistema realizaría una verificación del sistema de archivos para asegurarse de que todo esté bien. Sin embargo, las reparaciones podrían tardar un tiempo dependiendo del tamaño de su sistema de archivos.

Ahora, si estuviera en un sistema con registro, antes de que su máquina comience a copiar el archivo, escribirá lo que va a hacer en un archivo de registro (journal). Cuando realmente copie el archivo, una vez que se complete, el registro marca esa tarea como completa. El sistema de archivos siempre está en un estado consistente debido a esto, por lo que sabrá exactamente dónde se quedó si su máquina se apaga repentinamente. Esto también disminuye el tiempo de arranque porque en lugar de verificar todo el sistema de archivos, solo mira su registro.

### Tipos Comunes de Sistemas de Archivos de Escritorio

- ext4 - Esta es la versión más actual de los sistemas de archivos nativos de Linux. Es compatible con las versiones anteriores ext2 y ext3. Soporta volúmenes de disco de hasta 1 exabyte y tamaños de archivo de hasta 16 terabytes y mucho más. Es la opción estándar para los sistemas de archivos de Linux.
- Btrfs - "Better or Butter FS" es un nuevo sistema de archivos para Linux que viene con instantáneas, copias de seguridad incrementales, aumento de rendimiento y mucho más. Está ampliamente disponible, pero aún no es del todo estable y compatible.
- XFS - Sistema de archivos con registro de alto rendimiento, ideal para un sistema con archivos grandes como un servidor de medios.
- NTFS y FAT - Sistemas de archivos de Windows
- HFS+ - Sistema de archivos de Macintosh

Verifique qué sistemas de archivos hay en su máquina:

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

El comando **df** informa el uso del espacio en disco del sistema de archivos y otros detalles sobre su disco; hablaremos más sobre esta herramienta más adelante.

## Exercise

¡La práctica hace al maestro! Aquí hay un laboratorio práctico para reforzar su comprensión de los sistemas de archivos y particiones de Linux:

1. **[Administrar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practique la creación de una nueva partición, su formato, su montaje y la configuración del montaje persistente, todas habilidades fundamentales relacionadas con la gestión de diferentes implementaciones de sistemas de archivos.

Este laboratorio le ayudará a aplicar los conceptos en escenarios reales y a generar confianza en la gestión del almacenamiento en disco en Linux.

## Quiz Question

¿Cuál es el tipo de sistema de archivos común de Linux?

## Quiz Answer

ext4
