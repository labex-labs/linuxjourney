---
lesson_id: "file-permissions"
course_id: "permissions"
lang: "es"
order_index: 1
title: "Permisos de archivos"
description: "Aprende a leer los tipos de archivos de Linux y los bits de permisos de propietario, grupo y otros."
meta_title: "Permisos de archivos - Permisos"
meta_description: "Aprende los permisos de archivos de Linux, incluidos los bits rwx de propietario, grupo y otros. Domina la salida de ls -l y los modos de archivo."
meta_keywords: "permisos de archivos, permisos Linux, permisos rwx, orden ls -l, modos de archivo, guía Linux"
---

Linux representa muchos recursos mediante interfaces similares a archivos, y cada objeto del sistema de archivos tiene metadatos que controlan el acceso. Leer esos metadatos es una base para trabajar de forma segura con archivos y directorios.

## Leer un listado largo

Usa `ls -l` para mostrar un listado largo:

```bash
$ ls -ld Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 Desktop/
```

El primer campo, `drwxr-xr-x`, combina un carácter de tipo de archivo con nueve caracteres de permisos. El listado también identifica a `pete` como propietario y a `penguins` como grupo asociado al directorio.

El carácter inicial describe el tipo de objeto. Algunos valores habituales son:

- `-` para un archivo normal.
- `d` para un directorio.
- `l` para un enlace simbólico.

También existen otros tipos de archivos especiales. Los nueve caracteres restantes son los permisos de acceso:

```text
d | rwx | r-x | r-x
```

:::single-choice{#file-permissions-type-character}
En `drwxr-xr-x`, ¿qué indica la `d` inicial?

::option[El objeto es un enlace simbólico.]{#file-permissions-type-link explanation="Un enlace simbólico suele mostrarse con `l` en la posición del tipo de archivo."}
::option[El objeto es un directorio.]{#file-permissions-type-directory .correct explanation="El primer carácter indica el tipo de archivo y `d` identifica un directorio."}
::option[El propietario tiene permiso para eliminar.]{#file-permissions-type-delete explanation="Las cadenas de modo de Linux no usan `d` como permiso de eliminación; la primera posición describe el tipo de objeto."}
:::

## Comprender `r`, `w` y `x`

Cada triplete de permisos usa estos caracteres:

- `r` concede permiso de lectura.
- `w` concede permiso de escritura.
- `x` concede permiso de ejecución.
- `-` significa que el permiso no está presente.

Para un archivo normal, la lectura permite acceder a su contenido, la escritura permite modificarlo y la ejecución permite que el kernel intente ejecutarlo como programa. La ejecución aún puede fallar si el formato del archivo, la línea de intérprete, las opciones de montaje u otro control de seguridad no lo permiten.

En un directorio, los significados se refieren a sus entradas:

- La lectura permite enumerar los nombres del directorio.
- La escritura permite crear o eliminar entradas, normalmente junto con el permiso de ejecución.
- La ejecución, también llamada permiso de búsqueda, permite atravesar el directorio y acceder a las entradas por su nombre.

La eliminación de un archivo se rige principalmente por los permisos de su directorio padre, no por el bit de escritura del propio archivo.

:::single-choice{#file-permissions-directory-execute}
¿Qué permite principalmente el permiso de ejecución sobre un directorio?

::option[Ejecutar todos los archivos normales almacenados en el directorio.]{#file-permissions-directory-run-files explanation="El bit de ejecución de un directorio no concede permiso de ejecución a todos los archivos que contiene."}
::option[Cambiar el contenido de todos los archivos del directorio.]{#file-permissions-directory-edit-files explanation="La escritura del contenido depende de los permisos de cada archivo y de otros controles de acceso."}
::option[Atravesar el directorio y acceder a las entradas por su nombre.]{#file-permissions-directory-search .correct explanation="El permiso de ejecución o búsqueda de un directorio permite atravesarlo dentro de una ruta."}
:::

## Clases de propietario, grupo y otros

Los nueve caracteres de modo forman tres tripletes en un orden fijo:

1. **Propietario**: permisos usados cuando el ID de usuario efectivo del proceso coincide con el propietario del archivo.
2. **Grupo**: permisos usados cuando un ID de grupo aplicable del proceso coincide con el grupo del archivo.
3. **Otros**: permisos usados cuando ninguna de las clases anteriores coincide.

El kernel selecciona una clase aplicable; no combina los tres tripletes para encontrar el resultado más permisivo. Otros mecanismos, como las listas de control de acceso, las opciones de montaje, las capacidades o los controles de acceso obligatorios, pueden afectar aún más a la decisión final.

En el ejemplo, el triplete del propietario es `rwx`, mientras que los de grupo y otros son `r-x`. El propietario puede leer, escribir y buscar en el directorio. Las clases de grupo y otros pueden leerlo y recorrerlo, pero no crear ni eliminar entradas mediante los bits de modo normales del directorio.

:::single-choice{#file-permissions-triplet-order}
Después del carácter de tipo de archivo, ¿en qué orden aparecen los tres tripletes de permisos?

::option[Grupo, propietario y otros.]{#file-permissions-order-group-first explanation="El triplete del grupo es el segundo, no el primero."}
::option[Otros, grupo y propietario.]{#file-permissions-order-other-first explanation="El triplete de otros es el último y el de propietario es el primero."}
::option[Propietario, grupo y otros.]{#file-permissions-order-owner-first .correct explanation="Los nueve caracteres de permisos siempre muestran los tripletes de propietario, grupo y otros en ese orden."}
:::

:::single-choice{#file-permissions-example-group}
¿Qué permisos normales tiene la clase de grupo en `drwxr-xr-x`?

::option[Lectura y escritura.]{#file-permissions-group-read-write explanation="El triplete del grupo es `r-x`, por lo que su posición de escritura contiene `-`."}
::option[Escritura y ejecución.]{#file-permissions-group-write-execute explanation="El triplete del grupo contiene `r`, no `w`, en su primera posición."}
::option[Lectura y ejecución.]{#file-permissions-group-read-execute .correct explanation="El triplete central es `r-x`, que concede lectura y ejecución, pero no escritura."}
:::

Para reforzar estos conceptos en un entorno aislado, prueba el laboratorio [Usuarios, grupos y permisos de archivos en Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002). Permite practicar la lectura de modos y el cambio de propiedad y permisos.

## Resumen

Ahora puedes interpretar el campo básico de permisos de un listado largo de Linux.

1. Separa el carácter de tipo de archivo de los nueve bits de permisos.
2. Lee `r`, `w` y `x` según si el objeto es un archivo o un directorio.
3. Divide el modo en tripletes de propietario, grupo y otros.
4. Relaciona los tripletes con el propietario y el grupo mostrados por `ls -l`.
