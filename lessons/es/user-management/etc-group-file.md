---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "es"
order_index: 5
title: "/etc/group"
description: "Aprende cómo los registros de grupos locales asocian nombres con GID y enumeran miembros complementarios."
meta_title: "/etc/group - Gestión de usuarios"
meta_description: "Explora el archivo /etc/group de Linux. Aprende a interpretar sus cuatro campos, los GID, las listas de miembros y la pertenencia mediante grupos principales."
meta_keywords: "/etc/group, /etc/group Linux, archivo /etc/group Linux, getent group, gestión de grupos, GID, permisos Linux, grupos Linux"
---

`/etc/group` almacena registros de grupos locales. Asocia nombres de grupos con GID numéricos y enumera miembros explícitos, lo que permite compartir el control de acceso entre varias cuentas.

## Grupos locales frente a grupos resueltos

El archivo es solo uno de los posibles orígenes de grupos. NSS puede resolverlos desde archivos locales, servicios de directorio u otras bases de datos configuradas. Muestra los registros locales con:

```bash
$ cat /etc/group
```

Consulta la base de datos de grupos resuelta con `getent`:

```bash
$ getent group
$ getent group developers
```

Las listas de grupos pueden revelar nombres internos de cuentas y funciones, así que revisa la salida antes de compartirla.

:::single-choice{#group-query-resolved-database} ¿Qué orden consulta la base de datos de grupos resuelta por NSS?

::option[`getent group`]{#group-getent-all .correct explanation="`getent` consulta los orígenes NSS configurados para los registros de grupos."}
::option[`cat /etc/group`]{#group-cat-local explanation="Esto solo lee el archivo local de grupos y puede omitir los proporcionados por otros orígenes."}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups` espera nombres de usuarios y muestra sus pertenencias; no trata la ruta de la base de datos local como una consulta NSS."}
:::

## Leer los cuatro campos

Un registro local tiene cuatro campos separados por dos puntos:

```text
developers:x:1500:alice,bob
```

1. **Nombre del grupo**: `developers`.
2. **Campo de contraseña**: normalmente `x`, `*` u otro marcador; los datos protegidos de contraseñas de grupos pueden almacenarse en `/etc/gshadow`.
3. **GID**: la identidad numérica del grupo, `1500` en este caso.
4. **Lista de miembros**: nombres de miembros explícitos separados por comas, aquí `alice` y `bob`.

Las contraseñas de grupos son una función heredada que usan herramientas como `newgrp` en algunas configuraciones. No son el mecanismo normal para conceder autorización sudo y no deben introducirse mediante ediciones manuales de campos.

:::single-choice{#group-gid-field} En `developers:x:1500:alice,bob`, ¿qué campo contiene el GID?

::option[El segundo campo, `x`]{#group-second-password explanation="El campo 2 es el marcador de contraseña del grupo, no la identidad numérica."}
::option[El cuarto campo, `alice,bob`]{#group-fourth-members explanation="El campo 4 enumera nombres de miembros explícitos, no el GID."}
::option[El tercer campo, `1500`]{#group-third-gid .correct explanation="El tercer campo separado por dos puntos es el identificador numérico del grupo."}
:::

:::single-choice{#group-explicit-member-field} ¿Cómo se representan los nombres de miembros explícitos en un registro de grupo local?

::option[Como una lista separada por comas en el campo 4.]{#group-members-field-four .correct explanation="El último campo contiene nombres de miembros complementarios explícitos separados por comas."}
::option[Como una lista separada por espacios en el campo 2.]{#group-members-field-two explanation="El campo 2 está reservado para datos relacionados con contraseñas o un marcador, no para la lista de miembros."}
::option[Como UID numéricos incorporados al nombre del grupo.]{#group-members-in-name explanation="El nombre del grupo y los nombres de miembros son campos separados; las entradas normales de miembros son nombres de inicio de sesión, no dígitos UID incorporados."}
:::

## Tener en cuenta la pertenencia al grupo principal

La lista de miembros de `/etc/group` no suele repetir a los usuarios cuyo registro passwd indica ese GID como grupo principal. Por tanto, un usuario puede ser miembro aunque su nombre no aparezca en el campo 4.

Por ejemplo, si el registro passwd de Alice tiene el GID principal 1500, pertenece a `developers` aunque el registro local del grupo termine con un campo de miembros vacío:

```text
developers:x:1500:
```

Por eso, analizar únicamente el campo 4 produce una vista incompleta de las pertenencias.

:::single-choice{#group-primary-membership-visibility} El registro passwd de Alice usa el GID 1500 como GID principal, pero su nombre no aparece en el campo 4 del grupo 1500. ¿Es miembro de ese grupo?

::option[No, todas las pertenencias deben aparecer en el campo 4 de `/etc/group`.]{#group-field-four-only explanation="Esto ignora la pertenencia mediante el GID principal y contabilizaría menos miembros de los reales."}
::option[Sí, la pertenencia principal procede del campo GID del registro passwd.]{#group-primary-from-passwd .correct explanation="La lista explícita del archivo de grupos se usa principalmente para pertenencias complementarias; la principal se registra con la cuenta."}
::option[Solo si el campo de contraseña del grupo contiene su nombre de usuario.]{#group-password-member explanation="El campo de contraseña no está relacionado con la declaración de la pertenencia principal."}
:::

## Consultar los grupos de un usuario

Usa `id USER` o `groups USER` para obtener una vista resuelta de la cuenta:

```bash
$ id alice
$ groups alice
```

Para el proceso actual, `id` sin argumentos muestra los grupos presentes realmente en sus credenciales. Una pertenencia complementaria recién configurada no suele aparecer en una sesión de inicio ya activa; inicia una sesión autenticada nueva o usa deliberadamente un mecanismo configurado como `newgrp` cuando corresponda.

:::single-choice{#group-current-process-credentials} ¿Qué orden muestra el UID, el GID principal y los grupos complementarios del proceso actual?

::option[`id`]{#group-current-id .correct explanation="Sin un operando de usuario, `id` muestra las credenciales de identidad del proceso actual."}
::option[`cat /etc/group`]{#group-current-cat explanation="El archivo local enumera registros, pero no muestra qué grupos resueltos están activos en el proceso actual."}
::option[`getent passwd`]{#group-current-passwd explanation="Esto consulta registros de cuentas y no muestra específicamente la lista de grupos complementarios del proceso actual."}
:::

## Cambiar grupos locales de forma segura

Usa herramientas como `groupadd`, `groupmod`, `groupdel`, `gpasswd` y `usermod` en vez de editar los registros con un editor de propósito general. Ten especial cuidado con:

- `usermod -aG GROUP USER`, que añade una pertenencia complementaria.
- `usermod -G ...`, que sustituye la lista de grupos complementarios cuando se omite `-a`.

Si es inevitable reparar manualmente la base de datos local, usa `vigr` para bloquearla y `grpck` para validarla. Mantén una vía de recuperación antes de realizar cambios remotos de identidad.

Para practicar la gestión de grupos locales en un entorno controlado, prueba estos laboratorios prácticos:

1. **[Gestionar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica todo el ciclo de administración de usuarios, desde crear y proteger cuentas hasta modificarlas y eliminarlas.
2. **[Gestionar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Practica utilidades principales de administración de grupos como `groupadd`, `usermod` y `groupdel`.
3. **[Añadir un usuario y grupo nuevos](https://labex.io/labs/linux-add-new-user-and-group-17987)** - Simula la incorporación de miembros a un servidor mediante cuentas, grupos personalizados y pertenencias.

## Resumen

Ahora puedes interpretar registros de grupos locales y resolver la pertenencia completa con mayor precisión.

1. Consulta los orígenes de grupos configurados con `getent group`.
2. Lee los cuatro campos de grupo separados por dos puntos.
3. Localiza el GID numérico y la lista de miembros explícitos.
4. Incluye la pertenencia principal de los registros passwd.
5. Consulta las credenciales activas antes de confiar en una pertenencia recién cambiada.
