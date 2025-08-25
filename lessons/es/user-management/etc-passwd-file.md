---
index: 3
lang: "es"
title: "/etc/passwd"
meta_title: "/etc/passwd - Gestión de usuarios"
meta_description: "Aprende sobre el archivo /etc/passwd en Linux, comprende los campos de información del usuario y cómo funcionan los UID. Explora este archivo de configuración esencial."
meta_keywords: "/etc/passwd, usuarios de Linux, ID de usuario, UID, tutorial de Linux, principiante, guía, comandos de Linux"
---

## Lesson Content

Recuerda que los nombres de usuario no son realmente identificaciones para los usuarios. El sistema utiliza un ID de usuario (UID) para identificar a un usuario. Para saber qué usuarios están asignados a qué ID, consulta el archivo `/etc/passwd`.

```bash
cat /etc/passwd
```

Este archivo te muestra una lista de usuarios e información detallada sobre ellos. Por ejemplo, la primera línea de este archivo probablemente se vea así:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Cada línea muestra información de un usuario; lo más común es que veas al usuario root como la primera línea. Hay muchos campos separados por dos puntos que te dan información adicional sobre el usuario. Veámoslos todos:

1. **Nombre de usuario**
2. **Contraseña del usuario** - La contraseña no se almacena realmente en este archivo; generalmente se almacena en el archivo `/etc/shadow`. Hablaremos más sobre `/etc/shadow` en la próxima lección, pero por ahora, debes saber que contiene contraseñas de usuario cifradas. Puedes ver muchos símbolos diferentes en este campo: si ves una "x", significa que la contraseña se almacena en el archivo `/etc/shadow`; un "*" significa que el usuario no tiene acceso de inicio de sesión; y si hay un campo en blanco, significa que el usuario no tiene contraseña.
3. **El ID de usuario** - Como puedes ver, root tiene el UID de 0.
4. **El ID de grupo**
5. **Campo GECOS** - Se utiliza para dejar comentarios generales sobre el usuario o la cuenta, como su nombre real o número de teléfono. Está delimitado por comas.
6. **Directorio de inicio del usuario**
7. **Shell del usuario** - Probablemente verás que muchos usuarios tienen bash como su shell predeterminado.

Normalmente, en la página de configuración de un usuario, esperarías ver solo usuarios humanos. Sin embargo, notarás que `/etc/passwd` contiene otros usuarios. Recuerda que los usuarios solo están en el sistema para ejecutar procesos con diferentes permisos. A veces queremos ejecutar procesos con permisos predeterminados. Por ejemplo, el usuario `daemon` se utiliza para procesos demonio.

Además, cabe señalar que puedes editar el archivo `/etc/passwd` manualmente si deseas agregar usuarios y modificar información con la herramienta `vipw`. Sin embargo, es mejor dejar este tipo de cosas a las herramientas que discutiremos en una lección posterior, como `useradd` y `userdel`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de las cuentas de usuario de Linux y su gestión:

1. **[Administrar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica el ciclo de vida completo de la administración de usuarios, desde la creación y seguridad de nuevas cuentas hasta su modificación y eliminación.
2. **[Administrar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Adquiere experiencia práctica con las utilidades de línea de comandos principales para la administración de grupos, incluida la creación de nuevos grupos y la modificación de membresías de usuarios.
3. **[Configurar cuentas de usuario y privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprende técnicas esenciales para administrar cuentas de usuario y privilegios sudo para mejorar la seguridad de un sistema Linux.

Estos laboratorios te ayudarán a aplicar los conceptos de ID de usuario y administración de cuentas en escenarios reales y a generar confianza con la administración de usuarios de Linux.

## Quiz Question

Si un usuario no tiene acceso de inicio de sesión, ¿cómo se indica eso en `/etc/passwd`?

## Quiz Answer

-
