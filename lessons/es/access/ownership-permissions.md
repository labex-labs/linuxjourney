---
lang: "es"
title: "Permisos de Propiedad"
description: "Aprende a cambiar la propiedad de archivos en Linux usando los comandos chown y chgrp. Comprende los permisos de usuario y grupo con este tutorial de Linux para principiantes."
keywords: "chown, chgrp, propiedad de archivos Linux, permisos Linux, comandos Linux, Linux para principiantes, tutorial Linux, guía Linux"
---

## Lesson Content

Además de modificar los permisos de los archivos, también puedes modificar la propiedad de grupo y usuario del archivo.

### Modify user ownership

```bash
sudo chown patty myfile
```

Este comando establecerá el propietario de `myfile` en `patty`.

### Modify group ownership

```bash
sudo chgrp whales myfile
```

Este comando establecerá el grupo de `myfile` en `whales`.

### Modify both user and group ownership at the same time

Si añades dos puntos y el nombre del grupo después del usuario, puedes establecer tanto el usuario como el grupo al mismo tiempo.

```bash
sudo chown patty:whales myfile
```

## Exercise

Modifica el grupo y el usuario de algunos archivos de prueba. Después, echa un vistazo a los permisos con `ls -l`.

## Quiz Question

¿Qué comando utilizas para cambiar la propiedad del usuario?

## Quiz Answer

chown
