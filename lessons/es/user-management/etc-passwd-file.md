---
lang: "es"
title: "/etc/passwd"
meta_description: "Aprende sobre el archivo /etc/passwd en Linux, comprende los campos de información del usuario y cómo funcionan los UID. Explora este archivo de configuración esencial."
meta_keywords: "/etc/passwd, usuarios de Linux, ID de usuario, UID, tutorial de Linux, principiante, guía, comandos de Linux"
---

## Lesson Content

Recuerda que los nombres de usuario no son realmente identificaciones para los usuarios. El sistema utiliza un ID de usuario (UID) para identificar a un usuario. Para saber qué usuarios están mapeados a qué ID, consulta el archivo `/etc/passwd`.

```bash
cat /etc/passwd
```

Este archivo te muestra una lista de usuarios e información detallada sobre ellos. Por ejemplo, la primera línea de este archivo probablemente se vea así:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Cada línea muestra información de usuario para un usuario; lo más común es que veas al usuario root como la primera línea. Hay muchos campos separados por dos puntos que te dan información adicional sobre el usuario. Veámoslos todos:

1. **Nombre de usuario**
2. **Contraseña del usuario** - La contraseña no se almacena realmente en este archivo; generalmente se almacena en el archivo `/etc/shadow`. Hablaremos más sobre `/etc/shadow` en la próxima lección, pero por ahora, debes saber que contiene contraseñas de usuario cifradas. Puedes ver muchos símbolos diferentes en este campo: si ves una "x", significa que la contraseña se almacena en el archivo `/etc/shadow`; un "\*" significa que el usuario no tiene acceso de inicio de sesión; y si hay un campo en blanco, significa que el usuario no tiene contraseña.
3. **El ID de usuario** - Como puedes ver, root tiene el UID de 0.
4. **El ID de grupo**
5. **Campo GECOS** - Se utiliza para dejar comentarios generales sobre el usuario o la cuenta, como su nombre real o número de teléfono. Está delimitado por comas.
6. **Directorio de inicio del usuario**
7. **Shell del usuario** - Probablemente verás que muchos usuarios tienen bash como shell predeterminado.

Normalmente, en la página de configuración de un usuario, esperarías ver solo usuarios humanos. Sin embargo, notarás que `/etc/passwd` contiene otros usuarios. Recuerda que los usuarios solo están en el sistema para ejecutar procesos con diferentes permisos. A veces queremos ejecutar procesos con permisos predeterminados. Por ejemplo, el usuario `daemon` se utiliza para procesos daemon.

Además, cabe señalar que puedes editar el archivo `/etc/passwd` manualmente si deseas agregar usuarios y modificar información con la herramienta `vipw`. Sin embargo, este tipo de cosas es mejor dejarlas a las herramientas que discutiremos en una lección posterior, como `useradd` y `userdel`.

## Exercise

Look at your `/etc/passwd` file, take a look at some of the users, and note the access they have.

## Quiz Question

Si un usuario no tiene acceso de inicio de sesión, ¿cómo se denota eso en `/etc/passwd`?

## Quiz Answer

-
