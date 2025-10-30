---
index: 3
lang: "es"
title: "Permisos de Propiedad"
meta_title: "Permisos de Propiedad - Permisos"
meta_description: "Aprende a cambiar la propiedad de archivos en Linux usando los comandos chown y chgrp. Comprende los permisos de usuario y grupo con este tutorial de Linux para principiantes."
meta_keywords: "chown, chgrp, propiedad de archivos Linux, permisos Linux, comandos Linux, Linux para principiantes, tutorial Linux, guía Linux"
---

## Lesson Content

Además de modificar los permisos de los archivos, también puedes modificar la propiedad de grupo y usuario del archivo.

### Modificar la propiedad del usuario

```bash
sudo chown patty myfile
```

Este comando establecerá el propietario de `myfile` en `patty`.

### Modificar la propiedad del grupo

```bash
sudo chgrp whales myfile
```

Este comando establecerá el grupo de `myfile` en `whales`.

### Modificar la propiedad de usuario y grupo al mismo tiempo

Si añades dos puntos y el nombre del grupo después del usuario, puedes establecer tanto el usuario como el grupo al mismo tiempo.

```bash
sudo chown patty:whales myfile
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la propiedad y los permisos de los archivos:

1. **[Grupo de usuarios de Linux y permisos de archivos](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprende conceptos esenciales de gestión de usuarios y grupos de Linux, incluyendo la comprensión de los permisos de archivos y la manipulación de la propiedad de los archivos. Este laboratorio proporciona experiencia práctica en la seguridad de un entorno Linux multiusuario.
2. **[Añadir nuevo usuario y grupo](https://labex.io/es/labs/linux-add-new-user-and-group-17987)** - En este desafío, simularás la adición de nuevos miembros del equipo a un entorno de servidor creando nuevas cuentas de usuario, configurando grupos personalizados y gestionando las membresías de grupo. Esto pondrá a prueba tus habilidades en la administración de usuarios y grupos de Linux.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a generar confianza en la gestión de la propiedad y los permisos de los archivos en Linux.

## Quiz Question

¿Qué comando utilizas para cambiar la propiedad del usuario?

## Quiz Answer

chown
