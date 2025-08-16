---
title: "root"
description: "Aprende sobre el usuario root de Linux, el comando su y el archivo /etc/sudoers. Comprende el acceso y los permisos de superusuario en Linux con esta guía para principiantes."
keywords: "Linux root, comando su, archivo sudoers, permisos de Linux, superusuario, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Hemos visto una forma de obtener acceso de superusuario usando el comando `sudo`. También puedes ejecutar comandos como superusuario con el comando `su`. Este comando "sustituirá usuarios" y abrirá un shell de root si no se especifica un nombre de usuario. Puedes usar este comando para sustituir a cualquier usuario siempre que conozcas la contraseña.

```bash
su
```

Existen algunas desventajas al usar este método: es mucho más fácil cometer un error crítico ejecutando todo como root, no tendrás registros de los comandos que usas para cambiar las configuraciones del sistema, etc. Básicamente, si necesitas ejecutar comandos como superusuario, simplemente quédate con `sudo`.

Ahora que sabes qué comandos ejecutar como superusuario, la pregunta es ¿cómo sabes quién tiene acceso para hacerlo? El sistema no permite que cualquier persona ejecute comandos como superusuario, entonces, ¿cómo lo sabe? Existe un archivo llamado `/etc/sudoers`; este archivo lista los usuarios que pueden ejecutar `sudo`. Puedes editar este archivo con el comando **visudo**.

## Exercise

Open up the `/etc/sudoers` file and see what superuser permissions other users on the machine have.

## Quiz Question

¿Qué archivo muestra los usuarios que tienen acceso a `sudo`?

## Quiz Answer

/etc/sudoers
