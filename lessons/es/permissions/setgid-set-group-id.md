---
index: 6
lang: "es"
title: "Setgid"
meta_title: "Setgid - Permisos"
meta_description: "Aprende sobre los permisos SGID (Set Group ID) de Linux, cómo funcionan y cómo modificarlos. Comprende este concepto crucial de seguridad de Linux."
meta_keywords: "Linux SGID, Set Group ID, permisos de Linux, chmod g+s, seguridad de Linux, Linux para principiantes, tutorial de Linux"
---

## Lesson Content

Similar to the set user ID permission bit, there is a set group ID (SGID) permission bit. This bit allows a program to run as if it were a member of that group.

Let's look at one example:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

We can now see that the permission bit is in the group permission set.

### Modificación de SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

The numerical representation for SGID is 2.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los permisos de usuario, grupo y archivo de Linux:

1. **[Permisos de usuario, grupo y archivo de Linux](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprende conceptos esenciales de gestión de usuarios y grupos de Linux, incluyendo la creación y gestión de usuarios, la exploración de membresías de grupo, la comprensión de los permisos de archivo y la manipulación de la propiedad de los archivos.
2. **[Añadir nuevo usuario y grupo](https://labex.io/es/labs/linux-add-new-user-and-group-17987)** - Practica la creación de nuevas cuentas de usuario, la configuración de grupos personalizados y la gestión de membresías de grupo, simulando tareas de administración de sistemas del mundo real.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con los permisos de Linux y la gestión de usuarios.

## Quiz Question

¿Qué número representa el SGID?

## Quiz Answer

2
