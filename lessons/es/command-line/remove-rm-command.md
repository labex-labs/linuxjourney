---
index: 13
lang: "es"
title: "rm (Eliminar)"
meta_title: "rm (Eliminar) - Command Line"
meta_description: "Aprende a usar el comando `rm` en Linux para eliminar de forma segura archivos y directorios. Comprende opciones como -f, -i, -r y rmdir. ¡Comienza tu viaje en Linux!"
meta_keywords: "comando rm, eliminar archivos Linux, eliminar directorios, tutorial Linux, Linux para principiantes, rmdir, guía Linux"
---

## Lesson Content

Ahora, creo que tenemos demasiados archivos; eliminemos algunos. Para eliminar archivos, puedes usar el comando `rm`. El comando `rm` (remove) se usa para eliminar archivos y directorios.

```bash
rm file1
```

Ten precaución al usar `rm`; no hay una papelera de reciclaje mágica de la que puedas recuperar los archivos eliminados. Una vez que se han ido, se han ido para siempre, así que ten cuidado.

Afortunadamente, existen algunas medidas de seguridad, por lo que el usuario promedio no puede simplemente eliminar un montón de archivos importantes. Los archivos protegidos contra escritura te pedirán confirmación antes de eliminarlos. Si un directorio está protegido contra escritura, tampoco se eliminará fácilmente.

Ahora, si no te importa nada de eso, puedes eliminar un montón de archivos.

```bash
rm -f file1
```

La opción `-f` o force le dice a `rm` que elimine todos los archivos, ya sean de solo lectura o no, sin pedir confirmación al usuario (siempre que tengas los permisos adecuados).

```bash
rm -i file
```

Agregar la bandera `-i`, como muchos de los otros comandos, te dará una solicitud sobre si realmente deseas eliminar los archivos o directorios.

```bash
rm -r directory
```

No puedes simplemente `rm` un directorio por defecto; necesitarás agregar la bandera `-r` (recursive) para eliminar todos los archivos y cualquier subdirectorio que pueda tener.

Puedes eliminar un directorio con el comando `rmdir`.

```bash
rmdir directory
```

## Exercise

1. Create a file called `-file` (don't forget the dash!).
2. Remove that file.

## Quiz Question

¿Cómo se elimina un archivo llamado `myfile`?

## Quiz Answer
