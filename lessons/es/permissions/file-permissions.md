---
index: 1
lang: "es"
title: "Permisos de Archivos"
meta_title: "Permisos de Archivos - Permisos"
meta_description: "Aprende los permisos de archivos de Linux: comprende los bits rwx, los permisos de usuario, grupo y otros. Domina la salida de `ls -l` para principiantes. ¡Comienza tu viaje en Linux!"
meta_keywords: "permisos de archivos de Linux, comando ls -l, permisos rwx, tutorial de Linux, modos de archivo, Linux para principiantes, guía de Linux"
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

Así que en el ejemplo anterior, vemos que el usuario pete tiene permisos de lectura, escritura y ejecución sobre el archivo. El grupo penguins tiene permisos de lectura y ejecución. Y finalmente, los otros usuarios (todos los demás) tienen permisos de lectura y ejecución.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los permisos de archivos, usuarios y grupos de Linux:

1. **[Grupo de Usuarios de Linux y Permisos de Archivos](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprende conceptos esenciales de gestión de usuarios y grupos de Linux, incluyendo la creación de usuarios, la exploración de membresías de grupo, la comprensión de los permisos de archivos y la manipulación de la propiedad de los archivos.
2. **[Añadir Nuevo Usuario y Grupo](https://labex.io/es/labs/linux-add-new-user-and-group-17987)** - Practica la creación de nuevas cuentas de usuario, la configuración de grupos personalizados y la gestión de membresías de grupo, simulando tareas de administración de sistemas del mundo real.
3. **[Encontrar un Archivo](https://labex.io/es/labs/linux-find-a-file-17993)** - Aplica tus conocimientos sobre permisos de archivos encontrando un archivo específico y configurando su autoridad de acceso, asegurándote de que eres el único usuario autorizado.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza en la gestión de permisos y usuarios en Linux.

## Quiz Question

¿Qué bit de permiso se utiliza para ejecutable?

## Quiz Answer

x
