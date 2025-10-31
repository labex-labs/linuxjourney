---
index: 3
lang: "es"
title: "/etc/passwd"
meta_title: "/etc/passwd - Gestión de Usuarios"
meta_description: "Guía completa sobre el archivo /etc/passwd en Linux. Aprenda a interpretar campos de datos de usuario, entender UIDs y vea ejemplos como root:x:0:0:root:/root:/bin/bash."
meta_keywords: "/etc/passwd, /etc/passwd en linux, root:x:0:0:root:/root:/bin/bash, ID de usuario, UID, gestión de usuarios, tutorial Linux"
---

## Lesson Content

En Linux, los nombres de usuario son etiquetas legibles por humanos, pero el sistema identifica a los usuarios con un ID de Usuario (UID) único. El mapeo entre nombres de usuario y UIDs se almacena en el archivo `/etc/passwd`, un componente crítico para la gestión de usuarios.

Para ver su contenido, puedes usar un comando simple:

```bash
cat /etc/passwd
```

Este archivo muestra una lista de todos los usuarios del sistema e información detallada sobre ellos. Cada línea representa una única cuenta de usuario.

### Desglosando los Campos de /etc/passwd

A una línea típica en este archivo, a menudo la primera, se ve así:

```plaintext
root:x:0:0:root:/root:/bin/bash
```

Esta entrada para el usuario `root` contiene siete campos separados por dos puntos (`:`). Comprender la estructura de `/etc/passwd` en Linux es clave para administrar usuarios. Analicemos cada campo:

1. **Nombre de Usuario**: El nombre de inicio de sesión del usuario (ej. `root`).
2. **Contraseña**: Un marcador de posición para la contraseña cifrada del usuario. La contraseña real no se almacena aquí por razones de seguridad.
    - Una `x` indica que la contraseña cifrada está en el archivo `/etc/shadow`.
    - Un `*` (asterisco) significa que la cuenta está bloqueada y no se puede usar para iniciar sesión.
    - Un campo en blanco significa que el usuario no tiene contraseña.
3. **ID de Usuario (UID)**: El identificador numérico único para el usuario. El usuario `root` siempre tiene un UID de `0`.
4. **ID de Grupo (GID)**: El identificador numérico del grupo principal del usuario.
5. **Campo GECOS**: Un campo de comentarios que tradicionalmente contiene información adicional como el nombre completo del usuario, número de teléfono o ubicación de la oficina. Está delimitado por comas.
6. **Directorio Principal**: La ruta absoluta al directorio principal del usuario (ej. `/root`).
7. **Shell Predeterminado**: El intérprete de línea de comandos predeterminado del usuario, que se ejecuta al iniciar sesión (ej. `/bin/bash`).

### Usuarios del Sistema y Cuentas Especiales

Cuando inspeccionas el archivo `/etc/passwd`, notarás muchas cuentas que no pertenecen a usuarios humanos. Estas son cuentas de sistema utilizadas para ejecutar servicios o procesos específicos con permisos limitados, lo que mejora la seguridad del sistema. Por ejemplo, el usuario `daemon` se utiliza para ejecutar procesos de demonio en segundo plano.

### Edición del Archivo /etc/passwd

Aunque técnicamente puedes editar el archivo `/etc/passwd` directamente usando un editor de texto o el comando `vipw`, esto es fuertemente desaconsejado. Las ediciones manuales pueden introducir fácilmente errores de sintaxis, lo que podría bloquearte el acceso al sistema o causar inestabilidad.

Siempre es más seguro y confiable utilizar utilidades de línea de comandos dedicadas como `useradd`, `usermod` y `userdel` para administrar cuentas de usuario. Estas herramientas están diseñadas para modificar el archivo correctamente y manejar todas las configuraciones relacionadas.

## Exercise

Para solidificar tu conocimiento, prueba estos laboratorios prácticos. Te ayudarán a aplicar los conceptos de IDs de usuario y gestión de cuentas en escenarios del mundo real y a ganar confianza con la administración de usuarios de Linux.

1. **[Administrar Cuentas de Usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica el ciclo de vida completo de la administración de usuarios, desde la creación y aseguramiento de nuevas cuentas hasta la modificación y eliminación de las mismas.
2. **[Administrar Grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Adquiere experiencia práctica con utilidades de línea de comandos esenciales para la administración de grupos, incluida la creación de nuevos grupos y la modificación de las membresías de los usuarios.
3. **[Configurar Cuentas de Usuario y Privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprende técnicas esenciales para administrar cuentas de usuario y privilegios sudo para mejorar la seguridad de un sistema Linux.

## Quiz Question

Si una cuenta de usuario está bloqueada y no se puede utilizar para iniciar sesión, ¿cómo se indica esto en el campo de contraseña del archivo `/etc/passwd`? Por favor, responde usando solo el carácter requerido.

## Quiz Answer

`*`
