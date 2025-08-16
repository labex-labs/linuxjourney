---
lang: "es"
title: "Permisos de Archivos"
description: "Aprenda los permisos de archivos de Linux: comprenda los bits rwx, los permisos de usuario, grupo y otros. Domine la salida de `ls -l` para principiantes. ¡Comience su viaje en Linux!"
keywords: "permisos de archivo Linux, comando ls -l, permisos rwx, tutorial Linux, modos de archivo, Linux para principiantes, guía Linux"
---

## Lesson Content

Como aprendimos anteriormente, los archivos tienen diferentes permisos o modos de archivo. Veamos un ejemplo:

```bash
$ ls -l Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 .
```

Hay cuatro partes en los permisos de un archivo. La primera parte es el tipo de archivo, que se denota por el primer carácter en los permisos. En nuestro caso, como estamos viendo un directorio, muestra **d** para el tipo de archivo. Lo más común es que vea un **-** para un archivo regular.

Las siguientes tres partes del modo de archivo son los permisos reales. Los permisos se agrupan en 3 bits cada uno. Los primeros 3 bits son permisos de usuario, luego permisos de grupo y luego otros permisos. He añadido la barra vertical para facilitar la diferenciación.

```plaintext
d | rwx | r-x | r-x
```

Cada carácter representa un permiso diferente:

- r: legible
- w: escribible
- x: ejecutable (básicamente un programa ejecutable)
- -: vacío

Así que, en el ejemplo anterior, vemos que el usuario pete tiene permisos de lectura, escritura y ejecución sobre el archivo. El grupo penguins tiene permisos de lectura y ejecución. Y finalmente, los otros usuarios (todos los demás) tienen permisos de lectura y ejecución.

## Exercise

Use el comando `ls -l` en varios archivos y recite sus permisos, usuario y grupo.

## Quiz Question

¿Qué bit de permiso se utiliza para ejecutable?

## Quiz Answer

x
