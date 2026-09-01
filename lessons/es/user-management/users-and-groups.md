---
lesson_id: "users-and-groups"
course_id: "user-management"
lang: "es"
order_index: 1
title: "Usuarios y grupos"
description: "Aprende cómo Linux identifica usuarios y grupos y cómo las credenciales de los procesos afectan a las decisiones de acceso."
meta_title: "Usuarios y grupos - Gestión de usuarios"
meta_description: "Comprende la gestión de usuarios y grupos en Linux: UID, GID, credenciales de procesos, el superusuario root y la delegación controlada mediante sudo."
meta_keywords: "usuarios y grupos Linux, fundamentos Linux, sudo, usuario root, UID, GID, gestión de usuarios, tutorial Linux"
---

Linux usa identidades de usuarios y grupos para etiquetar procesos, asignar la propiedad de objetos del sistema de archivos y tomar decisiones de control de acceso. Los nombres legibles ayudan a los administradores, mientras que el kernel trabaja principalmente con identificadores numéricos y credenciales de procesos.

## Identificar usuarios mediante UID

Cada cuenta tiene un identificador numérico de usuario, o **UID**. Los nombres de usuario se corresponden con UID mediante las bases de datos de cuentas del sistema. Los archivos almacenan la propiedad numérica, que las herramientas suelen mostrar como el nombre correspondiente.

Ejecuta `id` para consultar la información de identidad del proceso actual:

```bash
$ id
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
```

Los valores varían según el sistema. Las cuentas humanas de inicio de sesión suelen tener directorios personales como `/home/alice`, pero pueden usar otra ruta o no tener un directorio personal normal. Las cuentas de servicio suelen existir para ejecutar software con una identidad limitada, no para permitir un inicio de sesión interactivo.

:::single-choice{#users-uid-purpose} ¿Qué identificador usa principalmente el kernel para representar la identidad de un usuario?

::option[La ruta de un directorio personal]{#users-home-path explanation="Una ruta personal forma parte de la configuración de la cuenta y puede variar o no existir; no es el identificador de usuario del kernel."}
::option[Un UID numérico]{#users-numeric-uid .correct explanation="Las bases de datos de cuentas asocian nombres con UID numéricos, que se usan en las credenciales de procesos y registros de propiedad."}
::option[El número de una ventana de terminal]{#users-terminal-number explanation="Los dispositivos y las sesiones de terminal son independientes de las identidades numéricas de usuarios."}
:::

## Organizar el acceso mediante grupos

Un grupo tiene un identificador numérico de grupo, o **GID**. Una cuenta suele tener un grupo principal y puede pertenecer a grupos complementarios. La pertenencia a grupos permite conceder acceso a un conjunto de usuarios sin asignar permisos cuenta por cuenta.

Consulta las pertenencias con:

```bash
$ id alice
$ groups alice
```

Estas órdenes muestran información de identidad configurada o resuelta. Los servicios de directorio y las cachés pueden intervenir, por lo que leer directamente `/etc/group` no siempre muestra toda la pertenencia efectiva.

:::single-choice{#users-primary-supplementary-groups} ¿Cómo puede participar normalmente una cuenta de Linux en grupos?

::option[Puede pertenecer exactamente a un grupo durante toda su existencia.]{#users-single-group explanation="Los procesos de Linux pueden llevar un grupo principal y una lista de grupos complementarios."}
::option[Pertenece a todos los grupos cuyos archivos puede leer.]{#users-readable-groups explanation="La lectura de archivos depende de permisos y credenciales; no crea automáticamente una pertenencia al grupo."}
::option[Tiene un grupo principal y puede tener grupos complementarios.]{#users-group-memberships .correct explanation="El GID principal forma parte del registro de la cuenta, mientras que las pertenencias complementarias proporcionan identidades de grupo adicionales."}
:::

## Comprender las credenciales de los procesos

Un proceso tiene credenciales como UID y GID reales y efectivos, además de grupos complementarios. Las credenciales efectivas son fundamentales para muchas comprobaciones de permisos. Un proceso iniciado por un usuario suele heredar las credenciales de su proceso padre, pero ciertos mecanismos controlados pueden cambiarlas.

Esto es más preciso que afirmar que un proceso siempre se ejecuta únicamente «como el usuario que lo inició». Los ejecutables con set-user-ID, los gestores de servicios, los contenedores, los espacios de nombres y las llamadas al sistema que cambian privilegios pueden afectar a las identidades visibles o efectivas en un contexto concreto.

:::single-choice{#users-process-access-identity} ¿Qué información se tiene en cuenta habitualmente cuando el kernel compara un proceso con los permisos de un archivo?

::option[El UID efectivo, el GID efectivo y los grupos complementarios del proceso.]{#users-effective-credentials .correct explanation="Estas credenciales se comparan con los datos de propiedad y permisos durante las comprobaciones normales de acceso discrecional."}
::option[El tema de colores de la terminal que inició el proceso.]{#users-terminal-theme explanation="Las preferencias de visualización no intervienen en las comprobaciones de permisos del sistema de archivos."}
::option[La longitud del nombre de usuario de la cuenta.]{#users-username-length explanation="El kernel trabaja con credenciales numéricas; la longitud del nombre de usuario no concede acceso."}
:::

## Reconocer la identidad root

La cuenta tradicionalmente llamada `root` tiene el UID 0. Muchos mecanismos de permisos de Linux tratan el UID 0 de forma especial y le otorgan amplio poder administrativo. Linux moderno también puede dividir privilegios mediante capacidades, espacios de nombres, controles de acceso obligatorios y aislamiento de servicios, por lo que «poder ilimitado en todos los contextos» es una simplificación excesiva.

El trabajo rutinario debe realizarse con una cuenta sin privilegios. La autoridad administrativa aumenta el impacto de los errores en rutas, las órdenes no fiables y el software comprometido.

:::single-choice{#users-root-uid} ¿Qué UID numérico identifica tradicionalmente la cuenta root?

::option[`0`]{#users-uid-zero .correct explanation="Linux y los sistemas tipo Unix reservan tradicionalmente el UID 0 para la identidad del superusuario."}
::option[`1000`]{#users-uid-thousand explanation="Muchas distribuciones asignan un valor cercano a 1000 a la primera cuenta humana normal, pero no es el UID de root."}
::option[`1`]{#users-uid-one explanation="El UID 1 puede pertenecer a una cuenta del sistema y no es la identidad tradicional del superusuario."}
:::

## Usar sudo bajo una política

`sudo` consulta su política configurada para saber si el usuario que lo invoca puede ejecutar una orden como un usuario de destino. El destino predeterminado suele ser root, pero una política o `-u USER` puede seleccionar otra cuenta. Las solicitudes de autenticación y el registro también dependen de la configuración.

Muestra las órdenes que la cuenta actual puede ejecutar:

```bash
$ sudo -l
```

Usa una orden administrativa permitida solo cuando la tarea lo requiera y comprendas sus efectos. No uses `sudo` simplemente para silenciar un error de permisos ni muestres bases de datos de hashes de contraseñas como `/etc/shadow` como ejercicio casual.

:::single-choice{#users-sudo-policy} ¿Qué hace `sudo` antes de ejecutar una orden solicitada?

::option[Consulta la política configurada para permitir el uso de la identidad de destino solicitada.]{#users-sudo-policy-check .correct explanation="`sudo` autoriza según una política y, cuando se permite, establece las credenciales de destino configuradas."}
::option[Siempre concede a todos los usuarios locales acceso root sin restricciones.]{#users-sudo-always-root explanation="La autorización está controlada por una política; los usuarios u órdenes denegados no reciben acceso root general."}
::option[Cambia permanentemente a 0 el UID de la cuenta que lo invoca.]{#users-sudo-permanent-uid explanation="`sudo` ejecuta una orden con credenciales de destino; no reescribe permanentemente la identidad de la cuenta que lo invoca."}
:::

Para practicar la administración de cuentas y grupos en un entorno controlado, prueba estos laboratorios prácticos:

1. **[Gestionar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica todo el ciclo de administración de usuarios, desde crear y proteger cuentas nuevas hasta modificarlas y eliminarlas.
2. **[Gestionar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Practica las utilidades principales de administración de grupos, incluida la creación, modificación de pertenencias y eliminación.
3. **[Configurar cuentas de usuario y privilegios sudo en Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprende técnicas esenciales para gestionar cuentas y privilegios de `sudo` y mejorar la seguridad del sistema.

## Resumen

Ahora puedes describir cómo Linux representa identidades y delega órdenes administrativas.

1. Identifica cuentas mediante UID y grupos mediante GID.
2. Distingue la pertenencia a grupos principal y complementarios.
3. Relaciona las credenciales de procesos con las comprobaciones de acceso.
4. Reconoce el UID 0 como la identidad root tradicional.
5. Trata `sudo` como una herramienta de delegación controlada por políticas.
