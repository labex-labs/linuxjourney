---
index: 2
lang: "es"
title: "root"
meta_title: "root - Gestión de Usuarios"
meta_description: "Aprende sobre el usuario root de Linux, el comando su y el archivo /etc/sudoers. Comprende el acceso y los permisos de superusuario en Linux con esta guía para principiantes."
meta_keywords: "Linux root, comando su, archivo sudoers, permisos Linux, superusuario, tutorial Linux, guía para principiantes"
---

## Lesson Content

Hemos visto una forma de obtener acceso de superusuario usando el comando `sudo`. También puedes ejecutar comandos como superusuario con el comando `su`. Este comando "sustituirá usuarios" y abrirá un shell de root si no se especifica un nombre de usuario. Puedes usar este comando para sustituir a cualquier usuario siempre que conozcas la contraseña.

```bash
su
```

Existen algunas desventajas al usar este método: es mucho más fácil cometer un error crítico ejecutando todo como root, no tendrás registros de los comandos que usas para cambiar las configuraciones del sistema, etc. Básicamente, si necesitas ejecutar comandos como superusuario, simplemente quédate con `sudo`.

Ahora que sabes qué comandos ejecutar como superusuario, la pregunta es ¿cómo sabes quién tiene acceso para hacerlo? El sistema no permite que cualquier persona ejecute comandos como superusuario, entonces, ¿cómo lo sabe? Existe un archivo llamado `/etc/sudoers`; este archivo lista los usuarios que pueden ejecutar `sudo`. Puedes editar este archivo con el comando **visudo**.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del acceso y los privilegios de superusuario:

1. **[Configurar cuentas de usuario y privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Practica la aplicación de políticas de contraseña, el bloqueo y desbloqueo de cuentas de usuario, la seguridad de la cuenta root y la concesión de permisos administrativos, lo que se relaciona directamente con la gestión del acceso de superusuario.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a generar confianza en la gestión de privilegios de usuario y acceso de superusuario.

## Quiz Question

¿Qué archivo muestra los usuarios que tienen acceso a `sudo`?

## Quiz Answer

/etc/sudoers
