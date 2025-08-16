---
lang: "es"
title: "/etc/shadow"
description: "Aprende sobre el archivo /etc/shadow en Linux, sus campos y cómo protege las contraseñas de los usuarios. Comprende la autenticación de Linux para principiantes."
keywords: "/etc/shadow, seguridad de Linux, autenticación de usuario, gestión de contraseñas, tutorial de Linux, guía para principiantes"
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

En la mayoría de las distribuciones actuales, la autenticación de usuarios no se basa únicamente en el archivo `/etc/shadow`; existen otros mecanismos, como PAM (Pluggable Authentication Modules), que reemplazan la autenticación.

## Exercise

Take a look at the `/etc/shadow` file.

## Quiz Question

¡No hay preguntas, sigamos!

## Quiz Answer
