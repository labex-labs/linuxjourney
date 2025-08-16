---
lang: "es"
title: "Registro de Autenticación"
description: "Aprende sobre el registro de autenticación de Linux con /var/log/auth.log. Comprende los inicios de sesión de usuarios y soluciona problemas de acceso con esta guía esencial."
keywords: "autenticación Linux, auth.log, registro Linux, inicio de sesión de usuario, seguridad Linux, principiante, tutorial, guía"
---

## Lesson Content

La autenticación de registros puede ser muy útil si tienes problemas para iniciar sesión.

### /var/log/auth.log

Este archivo contiene registros de autorización del sistema, como inicios de sesión de usuarios y los métodos de autenticación utilizados.

Fragmento de ejemplo:

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

Realiza algunos intentos de inicio de sesión fallidos y luego uno exitoso. Después, examina tu archivo `/var/log/auth.log` para ver qué ocurrió.

## Quiz Question

¿Qué archivo de registro se utiliza para la autenticación de usuarios?

## Quiz Answer

auth.log
