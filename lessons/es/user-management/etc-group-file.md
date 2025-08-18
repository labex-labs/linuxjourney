---
index: 5
lang: "es"
title: "/etc/group"
meta_title: "/etc/group - Gestión de Usuarios"
meta_description: "Aprende sobre el archivo /etc/group en Linux, entendiendo la gestión de grupos, GID y permisos de usuario. Tutorial esencial del archivo de grupo de Linux para principiantes."
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
2. Contraseña del grupo: no es necesario establecer una contraseña de grupo; usar un privilegio elevado como `sudo` es lo estándar. Se colocará un asterisco (`*`) como valor predeterminado.
3. Group ID (GID)
4. Lista de usuarios: puedes especificar manualmente los usuarios que deseas en un grupo específico

## Exercise

Run the command `groups`. What do you see?

## Quiz Question

¿Cuál es el GID de root?

## Quiz Answer

0
