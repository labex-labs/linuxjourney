---
index: 1
lang: "es"
title: "Usuarios y Grupos"
meta_title: "Usuarios y Grupos - Gestión de Usuarios"
meta_description: "Aprende sobre usuarios y grupos de Linux, comprende UIDs, GIDs y el usuario root. Descubre cómo usar el comando sudo para permisos elevados. ¡Comienza tu viaje en Linux!"
meta_keywords: "usuarios de Linux, grupos de Linux, comando sudo, usuario root, permisos de Linux, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

En cualquier sistema operativo tradicional, existen usuarios y grupos. Existen únicamente para el acceso y los permisos. Cuando se ejecuta un proceso, este se ejecutará como el propietario de ese proceso, ya sea Jane o Bob. El acceso y la propiedad de los archivos también dependen de los permisos. No querrías que Jane viera los documentos de Bob y viceversa.

Cada usuario tiene su propio directorio personal donde se almacenan sus archivos específicos de usuario. Esto generalmente se encuentra en `/home/username`, pero puede variar en diferentes distribuciones.

El sistema utiliza identificadores de usuario (UID) para gestionar a los usuarios. Los nombres de usuario son la forma amigable de asociar a los usuarios con la identificación, pero el sistema identifica a los usuarios por su UID. El sistema también utiliza grupos para gestionar los permisos. Los grupos son simplemente conjuntos de usuarios con permisos establecidos por ese grupo; el sistema los identifica con su ID de grupo (GID).

En Linux, tendrás usuarios además de los humanos normales que usan el sistema. A veces, estos usuarios son demonios del sistema que ejecutan procesos continuamente para mantener el sistema funcionando. Uno de los usuarios más importantes es `root` o `superuser`. `root` es el usuario más poderoso del sistema; `root` puede acceder a cualquier archivo e iniciar y terminar cualquier proceso. Por esa razón, puede ser peligroso operar como `root` todo el tiempo; podrías eliminar archivos críticos del sistema. Afortunadamente, si se necesita acceso de `root` y un usuario tiene acceso de `root`, puede ejecutar un comando como `root` en su lugar con el comando `sudo`. El comando `sudo` (superuser do) se utiliza para ejecutar un comando con acceso de `root`. Profundizaremos en cómo un usuario recibe acceso de `root` en una lección posterior.

Continúa e intenta ver un archivo protegido como `/etc/shadow`:

```bash
cat /etc/shadow
```

Observa cómo obtienes un error de permiso denegado. Mira los permisos con:

```bash
$ ls -la /etc/shadow

-rw-r----- 1 root shadow 1134 Dec 1 11:45 /etc/shadow
```

Todavía no hemos revisado los permisos, pero lo que está sucediendo aquí es que `root` es el propietario del archivo, y necesitarás acceso de `root` o ser parte del grupo `shadow` para leer el contenido. Ahora ejecuta el comando con `sudo`:

```bash
sudo cat /etc/shadow
```

¡Ahora podrás ver el contenido del archivo!

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los usuarios, grupos y `sudo` de Linux:

1. **[Administrar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/es/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica el ciclo de vida completo de la administración de usuarios, desde la creación y seguridad de nuevas cuentas hasta su modificación y eliminación.
2. **[Administrar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/es/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Adquiere experiencia práctica con las utilidades de línea de comandos principales para la administración de grupos, incluyendo la creación de nuevos grupos, la modificación de membresías de usuarios y la eliminación de grupos.
3. **[Configurar cuentas de usuario y privilegios Sudo en Linux](https://labex.io/es/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprende técnicas esenciales para administrar cuentas de usuario y privilegios `sudo` para mejorar la seguridad de un sistema Linux, incluyendo la concesión de permisos administrativos.

Estos laboratorios te ayudarán a aplicar los conceptos de gestión de usuarios y grupos, y el uso de `sudo`, en escenarios reales y a generar confianza en la administración de sistemas Linux.

## Quiz Question

¿Qué comando usas para ejecutar como `root`?

## Quiz Answer

sudo
