---
index: 4
lang: "es"
title: "Umask"
meta_title: "Umask - Permisos"
meta_description: "Aprende a usar el comando `umask` para controlar los permisos de archivo predeterminados en Linux. Comprende los permisos numéricos y gestiona fácilmente el acceso a nuevos archivos."
meta_keywords: "umask, permisos de linux, permisos de archivos, comandos de linux, linux para principiantes, tutorial de linux, permisos predeterminados"
---

## Lesson Content

Cada archivo que se crea viene con un conjunto predeterminado de permisos. Si alguna vez quieres cambiar ese conjunto predeterminado de permisos, puedes hacerlo con el comando `umask`. Este comando utiliza el conjunto de permisos de 3 bits que vemos en los permisos numéricos.

Sin embargo, en lugar de añadir estos permisos, `umask` los quita.

```bash
umask 021
```

En el ejemplo anterior, estamos indicando que queremos que los permisos predeterminados de los nuevos archivos permitan a los usuarios acceso a todo, pero para los grupos, queremos quitarles el permiso de escritura, y para otros, queremos quitarles el permiso de ejecución. El `umask` predeterminado en la mayoría de las distribuciones es `022`, lo que significa acceso total para el usuario, pero sin acceso de escritura para el grupo y otros usuarios.

Cuando ejecutas el comando `umask`, aplicará ese conjunto predeterminado de permisos a cualquier archivo nuevo que crees. Sin embargo, si quieres que persista, tendrás que modificar tu archivo de inicio (`.profile`), pero eso lo discutiremos en una lección posterior.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los permisos de archivos y cómo se relacionan con la configuración predeterminada:

1. **[Grupo de Usuarios de Linux y Permisos de Archivos](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Practica la creación y gestión de usuarios, explorando las membresías de grupo, entendiendo los permisos de archivos y manipulando la propiedad de los archivos. Este laboratorio proporciona experiencia práctica en la seguridad de un entorno Linux multiusuario, lo cual es crucial para entender cómo `umask` influye en los permisos de los nuevos archivos.

Este laboratorio te ayudará a aplicar los conceptos de permisos de archivos en escenarios reales y a generar confianza en la gestión del acceso en Linux.

## Quiz Question

¿Qué comando se utiliza para cambiar los permisos predeterminados de los archivos?

## Quiz Answer

umask
