---
index: 4
lang: "es"
title: "/etc/shadow"
meta_title: "/etc/shadow - Gestión de Usuarios"
meta_description: "Aprende sobre el archivo /etc/shadow en Linux, sus campos y cómo asegura las contraseñas de los usuarios. Comprende la autenticación de Linux para principiantes."
meta_keywords: "/etc/shadow, seguridad de Linux, autenticación de usuario, gestión de contraseñas, tutorial de Linux, guía para principiantes"
---

## Lesson Content

El archivo `/etc/shadow` se utiliza para almacenar información sobre la autenticación de usuarios. Requiere permisos de lectura de superusuario.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

Notarás que se parece mucho al contenido de `/etc/passwd`; sin embargo, en el campo de la contraseña, verás una contraseña cifrada. Los campos están separados por dos puntos de la siguiente manera:

1. Nombre de usuario
2. Contraseña cifrada
3. Fecha del último cambio de contraseña - expresada como el número de días desde el 1 de enero de 1970. Si hay un 0, significa que el usuario debe cambiar su contraseña la próxima vez que inicie sesión.
4. Edad mínima de la contraseña - Días que un usuario tendrá que esperar antes de poder cambiar su contraseña de nuevo.
5. Edad máxima de la contraseña - Número máximo de días antes de que un usuario tenga que cambiar su contraseña.
6. Período de advertencia de la contraseña - Número de días antes de que una contraseña vaya a caducar.
7. Período de inactividad de la contraseña - Número de días después de que una contraseña haya caducado para permitir el inicio de sesión con su contraseña.
8. Fecha de caducidad de la cuenta - Fecha en la que un usuario no podrá iniciar sesión.
9. Campo reservado para uso futuro.

En la mayoría de las distribuciones actuales, la autenticación de usuarios no se basa solo en el archivo `/etc/shadow`; existen otros mecanismos, como PAM (Módulos de Autenticación Conectables), que reemplazan la autenticación.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la autenticación de usuarios y la gestión de contraseñas en Linux:

1. **[Administrar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica el ciclo de vida completo de la administración de usuarios, desde la creación y seguridad de nuevas cuentas con `useradd` y `passwd` hasta su modificación y eliminación.
2. **[Configurar cuentas de usuario y privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprende técnicas esenciales para administrar cuentas de usuario y privilegios sudo, incluyendo la aplicación de políticas de contraseña y la seguridad de las cuentas.

Estos laboratorios te ayudarán a aplicar los conceptos de gestión de usuarios y contraseñas en escenarios reales y a desarrollar confianza con la administración de sistemas Linux.

## Quiz Question

No hay preguntas, ¡sigue adelante!

## Quiz Answer
