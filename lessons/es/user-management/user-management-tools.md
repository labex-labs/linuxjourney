---
index: 6
lang: "es"
title: "Herramientas de Gestión de Usuarios"
meta_title: "Herramientas de Gestión de Usuarios - Gestión de Usuarios"
meta_description: "Aprenda la gestión de usuarios de Linux: agregue, elimine y cambie contraseñas con los comandos useradd, userdel y passwd. ¡Comience con esta guía para principiantes!"
meta_keywords: "gestión de usuarios de Linux, adduser, userdel, passwd, tutorial de Linux, Linux para principiantes, cuentas de usuario, comandos de Linux"
---

## Lesson Content

La mayoría de los entornos empresariales utilizan sistemas de gestión para administrar usuarios, cuentas y contraseñas. Sin embargo, en una computadora de una sola máquina, existen comandos útiles para ejecutar y administrar usuarios.

### Añadir Usuarios

Puede usar el comando `adduser` o `useradd`. El comando `adduser` contiene características más útiles, como la creación de un directorio de inicio y más. Hay archivos de configuración para agregar nuevos usuarios que se pueden personalizar según lo que desee asignar a un usuario predeterminado.

```bash
sudo useradd bob
```

Verá que el comando anterior crea una entrada en `/etc/passwd` para bob, configura grupos predeterminados y agrega una entrada al archivo `/etc/shadow`.

### Eliminar Usuarios

Para eliminar un usuario, puede usar el comando `userdel`.

```bash
sudo userdel bob
```

Esto básicamente hace todo lo posible para deshacer los cambios de archivo realizados por `useradd`.

### Cambiar Contraseñas

```bash
passwd bob
```

Esto le permitirá cambiar su propia contraseña o la de otro usuario (si es root).

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de usuarios y cuentas en Linux:

1. **[Administrar Cuentas de Usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practique el ciclo de vida completo de la administración de usuarios, desde la creación y seguridad de nuevas cuentas hasta su modificación y eliminación.
2. **[Administrar Grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Obtenga experiencia práctica con las utilidades de línea de comandos principales para la administración de grupos, incluyendo la adición, modificación y eliminación de grupos.
3. **[Configurar Cuentas de Usuario y Privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas esenciales para administrar cuentas de usuario y privilegios sudo para mejorar la seguridad de un sistema Linux.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la gestión de usuarios y grupos de Linux.

## Quiz Question

¿Qué comando se utiliza para cambiar una contraseña?

## Quiz Answer

passwd
