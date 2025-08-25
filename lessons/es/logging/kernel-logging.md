---
index: 4
lang: "es"
title: "Registro del Kernel"
meta_title: "Registro del Kernel - Registro"
meta_description: "Aprenda sobre el registro del kernel de Linux con dmesg y kern.log. Comprenda los mensajes de arranque y los problemas de hardware. Explore los registros del kernel para obtener información del sistema."
meta_keywords: "dmesg, kern.log, registro de Linux, mensajes del kernel, registro de arranque, tutorial de Linux, guía para principiantes"
---

## Lesson Content

### /var/log/dmesg

Al arrancar, su sistema registra información sobre el búfer circular del kernel. Esto nos muestra información sobre los controladores de hardware, la información del kernel y el estado durante el arranque, entre otras cosas. Este archivo de registro se puede encontrar en `/var/log/dmesg` y se restablece en cada arranque. Puede que ahora no le vea ninguna utilidad, pero si alguna vez tuviera problemas con algo durante el arranque o un problema de hardware, `dmesg` es el mejor lugar para buscar. También puede ver este registro usando el comando `dmesg`.

### /var/log/kern.log

Otro registro que puede usar para ver la información del kernel es el archivo `/var/log/kern.log`. Este registra la información y los eventos del kernel en su sistema; también registra la salida de `dmesg`.

## Exercise

¡La práctica hace al maestro! Aquí tiene algunos laboratorios prácticos para reforzar su comprensión de la gestión de usuarios y grupos de Linux:

1. **[Administrar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practique el ciclo de vida completo de la administración de usuarios, desde la creación y seguridad de nuevas cuentas hasta su modificación y eliminación.
2. **[Administrar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Obtenga experiencia práctica con las utilidades de línea de comandos principales para la administración de grupos, incluida la creación de nuevos grupos, la modificación de membresías de usuarios y la eliminación de grupos.
3. **[Configurar cuentas de usuario y privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas esenciales para administrar cuentas de usuario y privilegios sudo para mejorar la seguridad de un sistema Linux, incluida la aplicación de políticas de contraseña y la concesión de permisos administrativos.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la gestión de usuarios y grupos en Linux.

## Quiz Question

¿Qué comando se puede usar para ver los mensajes de arranque del kernel?

## Quiz Answer

dmesg
