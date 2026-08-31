---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "es"
order_index: 6
title: "Herramientas de gestión de usuarios"
description: "Aprende a crear, modificar, proteger, verificar y eliminar cuentas locales mediante opciones explícitas."
meta_title: "Herramientas de gestión de usuarios - Gestión de usuarios"
meta_description: "Domina la gestión de usuarios de Linux con useradd, usermod, passwd y userdel para crear, modificar, proteger y eliminar cuentas locales."
meta_keywords: "gestión de usuarios Linux, useradd, usermod, userdel, passwd, cuentas Linux, administrar usuarios Linux"
---

Las distribuciones de Linux suelen proporcionar herramientas de cuentas de la suite de utilidades shadow, pero los valores predeterminados y las interfaces de nivel superior varían. Antes de cambiar una cuenta local, confirma que no se gestione centralmente, revisa el manual local de la orden y mantén una vía de recuperación.

Las órdenes de esta lección modifican el estado de autenticación y propiedad. Practica únicamente en un entorno desechable autorizado, no en un host de producción.

## Revisar los valores predeterminados de creación

`useradd` crea una cuenta local mediante las opciones de la orden y los valores predeterminados del sitio. Consulta los valores compilados y configurados con:

```bash
$ useradd -D
```

Archivos como `/etc/default/useradd`, `/etc/login.defs` y el contenido de plantilla pueden influir en el comportamiento, pero sus funciones varían según la distribución. Puede existir una orden `adduser` de nivel superior, aunque su interfaz no está estandarizada en todos los sistemas Linux.

## Crear explícitamente una cuenta local

En un entorno controlado, especifica las propiedades importantes en vez de confiar en valores predeterminados desconocidos:

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m` solicita crear el directorio personal.
- `-s /bin/bash` elige el shell de inicio después de confirmar que la ruta está permitida e instalada.
- `-c` proporciona el campo GECOS/comentario.

La cuenta nueva no suele poder autenticarse mediante una contraseña local utilizable hasta que se establezca una, pero el estado inicial exacto de la contraseña y del bloqueo depende de las herramientas y la política locales. Verifica los registros en vez de darlo por hecho:

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home}
¿Qué opción de `useradd` solicita explícitamente crear el directorio personal de la cuenta nueva?

::option[`-M`]{#user-tools-no-home-option explanation="La `-M` mayúscula indica explícitamente a las implementaciones habituales de `useradd` que no creen el directorio personal."}
::option[`-s`]{#user-tools-shell-option explanation="La opción `-s` elige un shell de inicio de sesión y no crea por sí sola un directorio personal."}
::option[`-m`]{#user-tools-home-option .correct explanation="La opción `-m` minúscula solicita que `useradd` cree y rellene el directorio personal según los valores predeterminados locales."}
:::

## Establecer o cambiar una contraseña

Un usuario normal cambia de forma interactiva su propia contraseña local con:

```bash
$ passwd
```

Un administrador autorizado puede establecer la contraseña de otra cuenta local con:

```bash
$ sudo passwd bob
```

Introduce las contraseñas únicamente en la solicitud protegida, no en argumentos de órdenes, el historial del shell, notas de la lección o conversaciones. La política PAM puede rechazar contraseñas débiles o reutilizadas. Las cuentas gestionadas mediante directorios pueden requerir otra herramienta.

:::single-choice{#user-tools-change-own-password}
¿Qué orden permite normalmente al usuario actual cambiar su propia contraseña mediante una solicitud interactiva?

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd` crea un registro de cuenta y no es la orden interactiva normal para cambiar contraseñas."}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel` elimina una cuenta local y no está relacionado con cambiar la contraseña del usuario que lo ejecuta."}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="Sin un operando de nombre de usuario, `passwd` actúa sobre la contraseña local del usuario que lo invoca, según la política PAM."}
:::

## Modificar propiedades y grupos de una cuenta

`usermod` cambia campos de cuentas locales. Algunos ejemplos:

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

Antes de mover el directorio personal, verifica el destino, la propiedad, el espacio disponible, los procesos activos, los montajes y los servicios. Para los grupos complementarios, `-aG` significa añadir a la lista actual. Usar `-G` sin `-a` sustituye toda la lista de grupos complementarios y puede eliminar acceso de forma inesperada.

Los cambios de grupos suelen afectar a las sesiones de inicio nuevas, no a los procesos que ya se ejecutan con el conjunto de credenciales anterior.

:::single-choice{#user-tools-append-group}
¿Qué orden añade `bob` al grupo complementario `developers` sin sustituir sus demás pertenencias complementarias?

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="Sin `-a`, `-G` sustituye la lista de grupos complementarios y puede eliminar pertenencias existentes."}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="La opción `-a` añade el grupo indicado por `-G` y conserva las demás pertenencias complementarias."}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel` elimina una definición de grupo y no añade una pertenencia de usuario."}
:::

## Bloquear una contraseña local

Un administrador puede bloquear el hash de la contraseña local con `passwd -l USER` y consultar su estado con `passwd -S USER`. El desbloqueo se realiza mediante `passwd -u USER` solo después de revisar el motivo del bloqueo y si permanece un hash válido.

Bloquear una contraseña no detiene necesariamente claves SSH, tokens, tareas programadas, procesos ya activos ni autenticación específica de servicios. Para desactivar una cuenta de forma integral, define la amenaza y las vías de acceso y aplica después una política coordinada que puede incluir caducidad de la cuenta, shell de inicio, acceso a servicios, claves y finalización de sesiones.

:::single-choice{#user-tools-password-lock-scope}
¿Qué bloquea principalmente `passwd -l bob`?

::option[Todas las vías posibles de autenticación y ejecución de la cuenta.]{#user-tools-lock-everything explanation="Las claves, los tokens, las tareas, los servicios y las sesiones existentes pueden requerir controles separados."}
::option[Todos los archivos que actualmente pertenecen al UID de Bob.]{#user-tools-lock-files explanation="El estado de la contraseña no cambia la propiedad del sistema de archivos ni hace inaccesibles automáticamente los datos propios."}
::option[El hash de la contraseña Unix local usado por la autenticación mediante contraseña.]{#user-tools-lock-local-password .correct explanation="La orden antepone un marcador al hash local o lo desactiva de otro modo, impidiendo la verificación normal a través de esa vía."}
:::

## Eliminar deliberadamente una cuenta local

`userdel bob` sin más elimina los registros de la cuenta local, pero suele conservar el directorio personal. `userdel -r bob` también intenta eliminar el directorio personal y el buzón de correo, por lo que es una operación destructiva.

Antes de cualquier eliminación:

1. Confirma la cuenta exacta con `getent passwd bob` e `id bob`.
2. Identifica procesos activos, tareas programadas, servicios, claves y accesos delegados.
3. Haz un inventario de los archivos propiedad del UID en los sistemas de archivos previstos.
4. Decide si los datos deben transferirse, archivarse, conservarse o eliminarse de forma segura.
5. Confirma que el UID no se reasignará mientras queden archivos huérfanos.

`userdel -r` no garantiza eliminar archivos fuera de las ubicaciones configuradas del directorio personal y el correo. Eliminar una cuenta también puede dejar propiedades numéricas en archivos, permisos de bases de datos, identidades de aplicaciones y registros de directorios remotos.

:::single-choice{#user-tools-userdel-r-scope}
¿Qué eliminación adicional solicita normalmente `userdel -r bob` con respecto a `userdel bob` sin más?

::option[Todos los archivos con el UID de Bob en todos los sistemas de archivos montados.]{#user-tools-delete-all-owned explanation="La herramienta no descubre y borra universalmente todos los archivos propiedad del UID en todo el almacenamiento."}
::option[Todas las cuentas remotas cuyo nombre de usuario también sea `bob`.]{#user-tools-delete-remote explanation="`userdel` actúa sobre las bases de datos locales correspondientes y no elimina identidades ajenas de servicios de directorio."}
::option[El directorio personal y el buzón local de Bob, además de los registros de la cuenta.]{#user-tools-delete-home-mail .correct explanation="La opción de eliminación recursiva apunta al directorio personal y al buzón configurados, pero no a todos los objetos que Bob pueda poseer en otros lugares."}
:::

Para practicar el ciclo de vida de las cuentas en un entorno aislado, prueba estos laboratorios prácticos:

1. **[Gestionar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica todo el ciclo de administración, desde crear y proteger cuentas hasta modificarlas y eliminarlas.
2. **[Gestionar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Practica las utilidades principales para añadir, modificar y eliminar grupos.
3. **[Configurar cuentas de usuario y privilegios sudo en Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Aprende técnicas esenciales para gestionar cuentas y privilegios sudo y mejorar la seguridad del sistema.

## Resumen

Ahora puedes gestionar cuentas locales con un ámbito explícito y verificación.

1. Revisa los valores predeterminados de `useradd` antes de crear una cuenta.
2. Solicita explícitamente la configuración del directorio personal, shell y metadatos.
3. Cambia contraseñas únicamente mediante solicitudes protegidas.
4. Añade grupos complementarios sin sustituir la lista existente.
5. Haz un inventario de las dependencias de identidad antes de una eliminación destructiva.
