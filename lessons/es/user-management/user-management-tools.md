---
index: 6
lang: "es"
title: "Herramientas de Gestión de Usuarios"
meta_title: "Herramientas de Gestión de Usuarios - Administración de Usuarios"
meta_description: "Domine la gestión de usuarios de Linux con herramientas esenciales de línea de comandos. Esta guía cubre el uso de useradd, userdel y passwd para administrar cuentas en Linux, ideal para principiantes."
meta_keywords: "gestión de usuarios linux, la herramienta de línea de comandos para administrar cuentas en linux, useradd, userdel, passwd, cuentas linux, administrar usuarios linux"
---

## Lesson Content

Aunque muchos entornos empresariales dependen de sistemas dedicados para la gestión de identidades, comprender los fundamentos de la **gestión de usuarios de Linux** directamente en una sola máquina es una habilidad crucial. Varias utilidades sirven como **la herramienta de línea de comandos para gestionar cuentas en Linux**, permitiendo una administración eficiente desde la terminal.

### Añadir Usuarios

Para crear un nuevo usuario, puede utilizar el comando `useradd`. Es una utilidad de bajo nivel que crea una nueva cuenta de usuario basándose en los valores predeterminados que se encuentran en `/etc/default/useradd`. Aunque algunos sistemas también ofrecen `adduser`, un script más interactivo y fácil de usar, `useradd` es el estándar universal.

```bash
sudo useradd bob
```

La ejecución de este comando añade una entrada para el usuario "bob" en el archivo `/etc/passwd`, configura las membresías de grupo predeterminadas y crea una entrada correspondiente en el archivo `/etc/shadow` para almacenar la información de la contraseña de forma segura.

### Eliminar Usuarios

Para eliminar una cuenta de usuario, puede utilizar el comando `userdel`. Este comando revierte efectivamente los cambios realizados por `useradd` al eliminar las entradas del usuario de los archivos de cuentas del sistema.

```bash
sudo userdel bob
```

Por defecto, este comando puede no eliminar el directorio personal del usuario. Puede usar la bandera `-r` (`userdel -r bob`) para asegurar que el directorio personal y el buzón de correo también se eliminen.

### Cambiar Contraseñas

El comando `passwd` se utiliza para establecer o cambiar la contraseña de un usuario. Un usuario normal puede ejecutar este comando para cambiar su propia contraseña. El usuario root puede ejecutarlo para cambiar la contraseña de cualquier usuario.

```bash
passwd bob
```

Cuando lo ejecuta un administrador, el sistema solicitará una nueva contraseña para el usuario especificado sin preguntar por la anterior. Esta es una tarea fundamental en la **gestión de usuarios de Linux**.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión de usuarios y cuentas en Linux:

1. **[Gestionar Cuentas de Usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practique el ciclo de vida completo de la administración de usuarios, desde la creación y protección de nuevas cuentas hasta su modificación y eliminación.
2. **[Gestionar Grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Obtenga experiencia práctica con las utilidades de línea de comandos principales para la administración de grupos, incluida la adición, modificación y eliminación de grupos.
3. **[Configurar Cuentas de Usuario y Privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprenda técnicas esenciales para gestionar cuentas de usuario y privilegios sudo para mejorar la seguridad de un sistema Linux.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la gestión de usuarios y grupos de Linux.

## Quiz Question

¿Qué comando se utiliza para cambiar una contraseña? Por favor, responda solo con el nombre del comando en letras minúsculas en inglés.

## Quiz Answer

passwd
