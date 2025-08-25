---
index: 5
lang: "es"
title: "/etc/group"
meta_title: "/etc/group - Gestión de Usuarios"
meta_description: "Aprenda sobre el archivo /etc/group en Linux, entendiendo la gestión de grupos, GID y permisos de usuario. Tutorial esencial del archivo de grupo de Linux para principiantes."
meta_keywords: "/etc/group, grupos de Linux, gestión de grupos, GID, permisos de Linux, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Otro archivo utilizado en la gestión de usuarios es el archivo `/etc/group`. Este archivo permite diferentes grupos con diferentes permisos.

```bash
$ cat /etc/group

root:*:0:pete
```

Muy similar al archivo `/etc/passwd`, los campos de `/etc/group` son los siguientes:

1. Nombre del grupo
2. Contraseña del grupo: no es necesario establecer una contraseña de grupo; usar un privilegio elevado como `sudo` es estándar. Se colocará un asterisco (`*`) como valor predeterminado.
3. ID de grupo (GID)
4. Lista de usuarios: puede especificar manualmente los usuarios que desea en un grupo específico

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de usuarios y grupos de Linux:

1. **[Administrar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practique el ciclo de vida completo de la administración de usuarios, desde la creación y seguridad de nuevas cuentas hasta su modificación y eliminación.
2. **[Administrar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Obtenga experiencia práctica con las utilidades de línea de comandos principales para la administración de grupos, incluyendo `groupadd`, `usermod` y `groupdel`.
3. **[Agregar nuevo usuario y grupo](https://labex.io/es/labs/linux-add-new-user-and-group-17987)** - Simule la adición de nuevos miembros del equipo a un entorno de servidor creando nuevas cuentas de usuario, configurando grupos personalizados y gestionando las membresías de grupo.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la gestión de usuarios y grupos de Linux.

## Quiz Question

¿Cuál es el GID de root?

## Quiz Answer

0
