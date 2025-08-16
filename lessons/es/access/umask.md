---
lang: "es"
title: "Umask"
description: "Aprende a usar el comando `umask` para controlar los permisos de archivo predeterminados en Linux. Comprende los permisos numéricos y gestiona el acceso a nuevos archivos fácilmente."
keywords: "umask, permisos linux, permisos de archivo, comandos linux, linux para principiantes, tutorial linux, permisos predeterminados"
---

## Lesson Content

Cada archivo que se crea viene con un conjunto predeterminado de permisos. Si alguna vez deseas cambiar ese conjunto predeterminado de permisos, puedes hacerlo con el comando `umask`. Este comando utiliza el conjunto de permisos de 3 bits que vemos en los permisos numéricos.

Sin embargo, en lugar de agregar estos permisos, `umask` los quita.

```bash
umask 021
```

En el ejemplo anterior, estamos indicando que queremos que los permisos predeterminados de los nuevos archivos permitan a los usuarios acceso a todo, pero para los grupos, queremos quitarles su permiso de escritura, y para otros, queremos quitarles su permiso de ejecución. El `umask` predeterminado en la mayoría de las distribuciones es `022`, lo que significa acceso completo para el usuario, pero sin acceso de escritura para el grupo y otros usuarios.

Cuando ejecutas el comando `umask`, aplicará ese conjunto predeterminado de permisos a cualquier archivo nuevo que crees. Sin embargo, si quieres que persista, tendrás que modificar tu archivo de inicio (`.profile`), pero eso lo discutiremos en una lección posterior.

## Exercise

1. Create a new file, then note its permissions.
2. Modify the `umask` and then create another new file.
3. Check the permissions once more on the new file. What do you expect to see?

## Quiz Question

¿Qué comando se utiliza para cambiar los permisos de archivo predeterminados?

## Quiz Answer

umask
