---
index: 4
lang: "es"
title: "/etc/shadow"
meta_title: "/etc/shadow - Gestión de Usuarios"
meta_description: "Explore el archivo /etc/shadow en Linux, un componente crítico para la autenticación de usuarios. Aprenda a verlo con 'cat /etc/shadow' y comprenda la estructura del archivo etc shadow, que almacena contraseñas cifradas e información de políticas."
meta_keywords: "etc shadow, archivo etc/shadow en linux, cat /etc/shadow, etc shadow en linux, /etc/shadow, autenticación de usuarios, seguridad de contraseñas, administración de sistemas Linux"
---

## Lesson Content

El archivo `/etc/shadow` es un componente crítico en los sistemas Linux para almacenar información sensible de autenticación de usuarios. A diferencia del archivo `/etc/passwd`, que es legible por el mundo, este requiere privilegios de superusuario para acceder, proporcionando una ubicación segura para los datos de las contraseñas.

### El Rol del Archivo etc/shadow en Linux

El propósito principal del **archivo etc/shadow en Linux** es almacenar contraseñas de usuario cifradas y políticas de envejecimiento de contraseñas. Al separar estos datos sensibles de la información general del usuario en `/etc/passwd`, el sistema mejora la seguridad. Si un usuario sin privilegios pudiera leer los hashes de las contraseñas, podría intentar descifrarlos sin conexión.

### Visualización del Archivo con cat /etc/shadow

Para inspeccionar el contenido de este archivo, debe usar un comando con privilegios de superusuario, como `sudo`. El comando `cat /etc/shadow` se usa comúnmente para este propósito.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

El formato de salida del **archivo etc shadow** es una serie de campos separados por dos puntos, donde cada línea representa un único usuario.

### Comprensión de la Estructura del Archivo

Cada línea en `/etc/shadow` contiene nueve campos, separados por dos puntos:

1. **Nombre de usuario**: El nombre de inicio de sesión del usuario.
2. **Contraseña cifrada**: La contraseña del usuario hasheada. Un asterisco (`*`) o un signo de exclamación (`!`) aquí significa que la cuenta está bloqueada.
3. **Fecha del último cambio de contraseña**: El número de días desde el 1 de enero de 1970 en que se cambió la contraseña por última vez. Un valor de `0` fuerza un cambio de contraseña en el próximo inicio de sesión.
4. **Antigüedad mínima de la contraseña**: El número mínimo de días que deben transcurrir antes de que el usuario pueda volver a cambiar su contraseña.
5. **Antigüedad máxima de la contraseña**: El número máximo de días que la contraseña es válida. Después de este período, el usuario debe cambiarla.
6. **Período de advertencia de contraseña**: El número de días antes de que expire la contraseña en los que el usuario recibirá un mensaje de advertencia.
7. **Período de inactividad de la contraseña**: El número de días después de que expira una contraseña en los que la cuenta se deshabilita.
8. **Fecha de caducidad de la cuenta**: Una fecha absoluta, expresada en días desde el 1 de enero de 1970, en la que se deshabilitará la cuenta de usuario.
9. **Campo reservado**: Este campo está reservado para uso futuro.

Aunque el archivo `/etc/shadow` es fundamental, la mayoría de las distribuciones modernas lo complementan con otros mecanismos de autenticación, como los Módulos de Autenticación Conectables (PAM), que ofrecen esquemas de autenticación más flexibles y avanzados.

## Exercise

¡La práctica hace la perfección! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la autenticación de usuarios y la gestión de contraseñas en Linux:

1. **[Administrar Cuentas de Usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practique el ciclo de vida completo de la administración de usuarios, desde la creación y aseguramiento de nuevas cuentas con `useradd` y `passwd` hasta su modificación y eliminación.
2. **[Configurar Cuentas de Usuario y Privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas esenciales para administrar cuentas de usuario y privilegios sudo, incluida la aplicación de políticas de contraseñas y la protección de cuentas.

Estos laboratorios le ayudarán a aplicar los conceptos de gestión de usuarios y contraseñas en escenarios reales y a ganar confianza con la administración de sistemas Linux.

## Quiz Question

No questions, move along!
