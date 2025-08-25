---
index: 13
lang: "es"
title: "rm (Eliminar)"
meta_title: "rm (Eliminar) - Línea de Comandos"
meta_description: "Aprende a usar el comando `rm` en Linux para eliminar de forma segura archivos y directorios. Comprende opciones como -f, -i, -r y rmdir. ¡Comienza tu viaje en Linux!"
meta_keywords: "comando rm, eliminar archivos Linux, eliminar directorios, tutorial Linux, Linux para principiantes, rmdir, guía Linux"
---

## Lesson Content

Ahora, creo que tenemos demasiados archivos; eliminemos algunos. Para eliminar archivos, puedes usar el comando `rm`. El comando `rm` (remove) se usa para eliminar archivos y directorios.

```bash
rm file1
```

Ten precaución al usar `rm`; no hay una papelera de reciclaje mágica de la que puedas recuperar los archivos eliminados. Una vez que se han ido, se han ido para siempre, así que ten cuidado.

Por fortuna, existen algunas medidas de seguridad, por lo que el usuario promedio no puede simplemente eliminar un montón de archivos importantes. Los archivos protegidos contra escritura te pedirán confirmación antes de eliminarlos. Si un directorio está protegido contra escritura, tampoco se eliminará fácilmente.

Ahora, si no te importa nada de eso, puedes eliminar un montón de archivos.

```bash
rm -f file1
```

La opción `-f` o force le dice a `rm` que elimine todos los archivos, estén protegidos contra escritura o no, sin pedir confirmación al usuario (siempre que tengas los permisos adecuados).

```bash
rm -i file
```

Añadir la bandera `-i`, como muchos de los otros comandos, te dará una pregunta sobre si realmente quieres eliminar los archivos o directorios.

```bash
rm -r directory
```

No puedes simplemente `rm` un directorio por defecto; necesitarás añadir la bandera `-r` (recursiva) para eliminar todos los archivos y cualquier subdirectorio que pueda tener.

Puedes eliminar un directorio con el comando `rmdir`.

```bash
rmdir directory
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la eliminación de archivos y directorios en Linux:

1. **[Comando Linux rm: Eliminación de archivos](https://labex.io/es/labs/linux-linux-rm-command-file-removing-209741)** - Aprende a usar el comando `rm` para eliminar archivos y directorios, incluyendo varias opciones como `-r` e `-i`, y practica la eliminación segura y efectiva de archivos.
2. **[Organización de archivos y directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practica habilidades esenciales de gestión de archivos de Linux, incluyendo el uso de `rm` para limpiar directorios innecesarios, en un desafío práctico.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza en la gestión de archivos y directorios en Linux.

## Quiz Question

¿Cómo eliminas un archivo llamado `myfile`?

## Quiz Answer

rm myfile
