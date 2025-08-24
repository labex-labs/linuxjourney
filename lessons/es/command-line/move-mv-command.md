---
index: 11
lang: "es"
title: "mv (Mover)"
meta_title: "mv (Mover) - Línea de Comandos"
meta_description: "Aprende a usar el comando Linux mv para mover y renombrar archivos/directorios. Comprende sus opciones y evita sobrescrituras. ¡Comienza tu viaje en Linux!"
meta_keywords: "comando mv, Linux mv, mover archivos Linux, renombrar archivos Linux, tutorial Linux, principiante, guía Linux"
---

## Lesson Content

Se utiliza para mover archivos y también para renombrarlos. Bastante similar al comando `cp` en cuanto a banderas y funcionalidad.

Puedes renombrar archivos así:

```bash
mv oldfile newfile
```

O puedes mover un archivo a un directorio diferente:

```bash
mv file2 /home/pete/Documents
```

Y mover más de un archivo:

```bash
mv file_1 file_2 /somedirectory
```

También puedes renombrar directorios:

```bash
mv directory1 directory2
```

Al igual que `cp`, si usas `mv` para un archivo o directorio, sobrescribirá cualquier cosa en el mismo directorio. Por lo tanto, puedes usar la bandera `-i` para que te pregunte antes de sobrescribir algo.

```bash
mv -i directory1 directory2
```

Supongamos que querías usar `mv` para sobrescribir el archivo anterior. También puedes hacer una copia de seguridad de ese archivo, y simplemente renombrará la versión antigua con un `~`.

```bash
mv -b directory1 directory2
```

## Exercise

Renombra un archivo y luego muévelo a un directorio diferente.

Para practicar con el comando `mv`, prueba este laboratorio interactivo:

- [Linux mv Command: File Moving and Renaming](https://labex.io/es/labs/linux-linux-mv-command-file-moving-and-renaming-209743)

## Quiz Question

¿Cómo renombras un archivo llamado `cat` a `dog`?

## Quiz Answer

mv cat dog
