---
index: 5
lang: "es"
title: "Setuid"
meta_title: "Setuid - Permisos"
meta_description: "Aprende sobre los permisos Linux Setuid (SUID), cómo funcionan y cómo modificarlos. Comprende SUID para un acceso seguro a archivos en Linux."
meta_keywords: "Linux Setuid, SUID, permisos Linux, chmod, comando passwd, seguridad Linux, Linux para principiantes, tutorial Linux"
---

## Lesson Content

Hay muchos casos en los que los usuarios normales necesitan acceso elevado para realizar tareas. El administrador del sistema no siempre puede estar presente para introducir una contraseña de root cada vez que un usuario necesita acceso a un archivo protegido, por lo que existen bits de permisos de archivo especiales para permitir este comportamiento. El Set User ID (SUID) permite a un usuario ejecutar un programa como el propietario del archivo del programa en lugar de como ellos mismos.

Veamos un ejemplo:

Digamos que quiero cambiar mi contraseña, ¿sencillo verdad? Simplemente uso el comando `passwd`:

```bash
passwd
```

¿Qué está haciendo el comando `passwd`? Está modificando un par de archivos, pero lo más importante es que está modificando el archivo `/etc/shadow`. Echemos un vistazo a ese archivo por un segundo:

```bash
$ ls -l /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Oh, espera un minuto, ¿este archivo es propiedad de root? ¿Cómo es posible que podamos modificar un archivo propiedad de root?

Veamos otro conjunto de permisos, esta vez del comando que ejecutamos:

```bash
$ ls -l /usr/bin/passwd

-rwsr-xr-x 1 root root 47032 Dec 1 11:45 /usr/bin/passwd
```

Notarás un nuevo bit de permiso aquí **s**. Este bit de permiso es el SUID. Cuando un archivo tiene este permiso establecido, permite a los usuarios que iniciaron el programa obtener el permiso del propietario del archivo, así como el permiso de ejecución, en este caso root. Así que, esencialmente, mientras un usuario está ejecutando el comando `passwd`, lo está ejecutando como root.

Es por eso que podemos acceder a un archivo protegido como `/etc/shadow` cuando ejecutamos el comando `passwd`. Ahora, si eliminas ese bit, verás que no podrás modificar `/etc/shadow` y, por lo tanto, cambiar tu contraseña.

### Modificación de SUID

Al igual que los permisos regulares, hay dos formas de modificar los permisos SUID.

_Forma simbólica:_

```bash
sudo chmod u+s myfile
```

_Forma numérica:_

```bash
sudo chmod 4755 myfile
```

Como puedes ver, el SUID se denota con un 4 y se antepone al conjunto de permisos. Puedes ver el SUID denotado como una **S** mayúscula. Esto significa que sigue haciendo lo mismo, pero no tiene permisos de ejecución.

## Exercise

¡La práctica hace al maestro! Comprender cómo funcionan los permisos de archivo, los grupos de usuarios y los bits especiales como SUID es crucial para administrar y proteger los sistemas Linux. La experiencia práctica solidificará tus conocimientos.

Aquí tienes un laboratorio práctico para reforzar tu comprensión de los permisos de archivo y la gestión de usuarios:

1. **[Grupos de usuarios y permisos de archivos de Linux](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Practica la creación y gestión de usuarios y grupos, la comprensión de los permisos de archivo y la manipulación de la propiedad de los archivos. Este laboratorio proporciona el conocimiento fundamental necesario para comprender cómo SUID aprovecha estos conceptos para un acceso elevado.

Este laboratorio te ayudará a aplicar los conceptos en un escenario real y a generar confianza con la gestión de usuarios y archivos de Linux.

## Quiz Question

¿Qué número representa el SUID?

## Quiz Answer

4
