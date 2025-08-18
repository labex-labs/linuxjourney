---
index: 6
lang: "es"
title: "Herramientas de gestión de usuarios"
meta_title: "Herramientas de gestión de usuarios - Gestión de Usuarios"
meta_description: "Aprende la gestión de usuarios en Linux: añadir, eliminar y cambiar contraseñas con los comandos useradd, userdel y passwd. ¡Empieza con esta guía para principiantes!"
meta_keywords: "gestión de usuarios Linux, adduser, userdel, passwd, tutorial Linux, Linux para principiantes, cuentas de usuario, comandos Linux"
---

## Lesson Content

La mayoría de los entornos empresariales utilizan sistemas de gestión para administrar usuarios, cuentas y contraseñas. Sin embargo, en una máquina individual, existen comandos útiles para gestionar usuarios.

### Adding Users

Puedes usar el comando `adduser` o `useradd`. El comando `adduser` contiene características más útiles, como la creación de un directorio de inicio y más. Hay archivos de configuración para añadir nuevos usuarios que se pueden personalizar según lo que quieras asignar a un usuario predeterminado.

```bash
sudo useradd bob
```

Verás que el comando anterior crea una entrada en `/etc/passwd` para bob, configura grupos predeterminados y añade una entrada al archivo `/etc/shadow`.

### Removing Users

Para eliminar un usuario, puedes usar el comando `userdel`.

```bash
sudo userdel bob
```

Esto básicamente hace todo lo posible para deshacer los cambios de archivo realizados por `useradd`.

### Changing Passwords

```bash
passwd bob
```

Esto te permitirá cambiar tu propia contraseña o la de otro usuario (si eres root).

## Exercise

Crea un nuevo usuario, luego cambia su contraseña e inicia sesión como el nuevo usuario.

## Quiz Question

¿Qué comando se utiliza para cambiar una contraseña?

## Quiz Answer

passwd
