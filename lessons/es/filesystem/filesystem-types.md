---
lang: "es"
title: "Tipos de Sistemas de Archivos"
meta_description: "Aprende sobre los tipos de sistemas de archivos de Linux como ext4, Btrfs y XFS. Comprende el journaling y VFS para datos consistentes. Explora los sistemas de archivos comunes de Linux en esta guía para principiantes."
meta_keywords: "tipos de sistemas de archivos de Linux, ext4, Btrfs, XFS, journaling, VFS, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Existen muchas implementaciones de sistemas de archivos diferentes. Algunos son más rápidos que otros, algunos soportan almacenamiento de mayor capacidad y otros solo funcionan en almacenamiento de menor capacidad. Los diferentes sistemas de archivos tienen distintas formas de organizar sus datos, y entraremos en detalle sobre qué tipos de sistemas de archivos existen. Dado que hay tantas implementaciones diferentes disponibles, las aplicaciones necesitan una forma de manejar las distintas operaciones. Por lo tanto, existe algo llamado capa de abstracción del Sistema de Archivos Virtual (VFS). Es una capa entre las aplicaciones y los diferentes tipos de sistemas de archivos, de modo que, sin importar qué sistema de archivos tengas, tus aplicaciones podrán trabajar con él.

Puedes tener muchos sistemas de archivos en tus discos, dependiendo de cómo estén particionados, y lo veremos en una próxima lección.

### Journaling

El journaling viene por defecto en la mayoría de los tipos de sistemas de archivos, pero en caso de que no sea así, debes saber qué hace. Digamos que estás copiando un archivo grande y de repente pierdes la energía. Bueno, si estás en un sistema de archivos sin journaling, el archivo terminaría corrupto y tu sistema de archivos sería inconsistente. Luego, cuando vuelvas a arrancar, tu sistema realizaría una verificación del sistema de archivos para asegurarse de que todo esté bien. Sin embargo, las reparaciones podrían tardar un tiempo dependiendo del tamaño de tu sistema de archivos.

Ahora, si estuvieras en un sistema con journaling, antes de que tu máquina comience a copiar el archivo, escribirá lo que vas a hacer en un archivo de registro (journal). Cuando realmente copias el archivo, una vez que se completa, el journal marca esa tarea como completa. El sistema de archivos siempre está en un estado consistente debido a esto, por lo que sabrá exactamente dónde te quedaste si tu máquina se apaga repentinamente. Esto también disminuye el tiempo de arranque porque en lugar de verificar todo el sistema de archivos, solo mira tu journal.

### Common Desktop Filesystem Types

- ext4 - Esta es la versión más actual de los sistemas de archivos nativos de Linux. Es compatible con las versiones anteriores ext2 y ext3. Soporta volúmenes de disco de hasta 1 exabyte y tamaños de archivo de hasta 16 terabytes y mucho más. Es la opción estándar para los sistemas de archivos de Linux.
- Btrfs - "Better or Butter FS" es un nuevo sistema de archivos para Linux que viene con snapshots, copias de seguridad incrementales, aumento de rendimiento y mucho más. Está ampliamente disponible, pero aún no es del todo estable y compatible.
- XFS - Sistema de archivos con journaling de alto rendimiento, ideal para un sistema con archivos grandes como un servidor de medios.
- NTFS and FAT - Windows filesystems
- HFS+ - Macintosh filesystem

Check out what filesystems are on your machine:

```plaintext
pete@icebox:~$ df -T
Filesystem     Type     1K-blocks    Used Available Use% Mounted on
/dev/sda1      ext4       6461592 2402708   3707604  40% /
udev           devtmpfs    501356       4    501352   1% /dev
tmpfs          tmpfs       102544    1068    101476   2% /run
/dev/sda6      xfs       13752320  460112  13292208   4% /home
```

The **df** command reports file system disk space usage and other details about your disk; we will talk more about this tool later.

## Exercise

Haz una pequeña investigación en línea sobre los otros tipos de sistemas de archivos: ReiserFS, ZFS, JFS y otros que puedas encontrar.

## Quiz Question

¿Cuál es el tipo de sistema de archivos común de Linux?

## Quiz Answer

ext4
