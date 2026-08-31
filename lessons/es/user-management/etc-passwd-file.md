---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "es"
order_index: 3
title: "/etc/passwd"
description: "Aprende a leer registros passwd locales y a distinguirlos de la vista completa de cuentas proporcionada por NSS."
meta_title: "/etc/passwd - Gestión de usuarios"
meta_description: "Guía del archivo /etc/passwd en Linux. Aprende a interpretar sus siete campos, los UID y GID y registros como root:x:0:0:root:/root:/bin/bash."
meta_keywords: "/etc/passwd, /etc/passwd Linux, root:x:0:0:root:/root:/bin/bash, ID de usuario, UID, gestión de usuarios, tutorial Linux"
---

`/etc/passwd` almacena registros de cuentas locales en un formato de texto separado por dos puntos. Asocia nombres de inicio de sesión con UID numéricos y registra un GID principal, un campo descriptivo, una ruta personal y un programa de inicio de sesión.

## Registros locales frente a cuentas resueltas

Muestra el archivo local con una orden de solo lectura:

```bash
$ cat /etc/passwd
```

Esto no representa necesariamente todas las cuentas conocidas por el sistema. Name Service Switch (NSS) puede resolver cuentas desde archivos, servicios de directorio, bases de datos del sistema u otros orígenes configurados. Usa `getent` para consultar la base de datos passwd resuelta:

```bash
$ getent passwd
$ getent passwd root
```

La primera orden puede revelar nombres y metadatos de cuentas, así que revisa la salida antes de compartirla públicamente.

:::single-choice{#passwd-query-resolved-database}
¿Qué orden consulta la base de datos passwd resuelta por NSS en vez de leer únicamente el archivo local?

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="Esto muestra únicamente el archivo local y no incluye cuentas proporcionadas exclusivamente por otros orígenes NSS."}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="El archivo shadow contiene datos locales protegidos de contraseñas y caducidad y no debe mostrarse con este fin."}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent` consulta mediante NSS los orígenes configurados de la base de datos passwd."}
:::

## Leer los siete campos

Un registro local suele tener este aspecto:

```text
root:x:0:0:root:/root:/bin/bash
```

Los siete campos separados por dos puntos son:

1. **Nombre de inicio de sesión**: el nombre legible de la cuenta, como `root`.
2. **Campo de contraseña**: normalmente `x` en un sistema con contraseñas shadow, lo que indica que los datos protegidos se almacenan por separado.
3. **UID**: la identidad numérica del usuario. El UID 0 recibe el tratamiento tradicional de superusuario.
4. **GID principal**: el identificador numérico del grupo principal de la cuenta.
5. **GECOS/comentario**: información descriptiva de la cuenta, a menudo separada internamente por comas.
6. **Directorio personal**: la ruta configurada como directorio personal de la cuenta; puede no existir en disco.
7. **Shell/programa de inicio de sesión**: el programa solicitado para las sesiones de inicio de sesión correspondientes, como `/bin/bash` o un programa que impide el inicio de sesión.

El kernel no exige que los UID sean únicos en registros mal formados o duplicados deliberadamente, pero las cuentas que comparten un UID son indistinguibles para muchas decisiones de propiedad y permisos. Los administradores deben mantener normalmente los UID de las cuentas únicos.

:::single-choice{#passwd-uid-field}
En `root:x:0:0:root:/root:/bin/bash`, ¿qué campo contiene el UID?

::option[El segundo campo, `x`]{#passwd-second-password explanation="El segundo campo es el marcador de contraseña, no la identidad numérica del usuario."}
::option[El cuarto campo, el segundo `0`]{#passwd-fourth-gid explanation="El campo 4 es el GID principal, no el UID."}
::option[El tercer campo, el primer `0`]{#passwd-third-uid .correct explanation="El campo 3 es el UID, por lo que el primer cero identifica este registro con el UID 0."}
:::

:::single-choice{#passwd-primary-gid-field}
¿Qué campo de un registro passwd almacena el GID principal de la cuenta?

::option[El campo 5]{#passwd-gecos-five explanation="El quinto campo es GECOS o comentario."}
::option[El campo 4]{#passwd-gid-four .correct explanation="El cuarto campo separado por dos puntos identifica numéricamente el grupo principal."}
::option[El campo 7]{#passwd-shell-seven explanation="El séptimo campo especifica el shell o programa de inicio de sesión."}
:::

## Interpretar el marcador de contraseña

En los sistemas habituales con contraseñas shadow, `x` en el campo 2 dirige las herramientas compatibles con contraseñas a los datos protegidos de `/etc/shadow`. Valores como `*` o `!` no son hashes de contraseña válidos y suelen impedir la autenticación mediante una contraseña Unix a través de esa entrada.

Esto no demuestra que la cuenta no pueda autenticarse por ningún método. Las claves SSH, los certificados, los tokens o los mecanismos específicos de un servicio pueden ser independientes. Del mismo modo, un campo de contraseña vacío tiene un comportamiento sensible para la seguridad que depende de la pila de autenticación; no lo crees ni lo «corrijas» manualmente.

:::single-choice{#passwd-x-placeholder}
¿Qué significa habitualmente `x` en el campo 2 de un registro local de `/etc/passwd`?

::option[La cuenta no tiene garantizado ningún método de autenticación.]{#passwd-no-auth-guarantee explanation="El marcador no describe todos los métodos de autenticación posibles ni significa por sí mismo que la cuenta no pueda usarse."}
::option[Se ha eliminado el directorio personal de la cuenta.]{#passwd-home-deleted explanation="La información del directorio personal se almacena en el campo 6 y no está relacionada con el marcador `x`."}
::option[Los datos protegidos de la contraseña se guardan en la base de datos shadow.]{#passwd-shadow-placeholder .correct explanation="El registro passwd público contiene un marcador, mientras que el hash y los campos de caducidad residen en datos shadow protegidos."}
:::

## Reconocer cuentas de servicio

Muchos registros representan servicios en vez de personas. Las identidades de servicio separadas ayudan a limitar los archivos y procesos a la autoridad necesaria para un daemon. Sus rutas personales pueden ser inusuales o inexistentes, y su programa de inicio de sesión puede ser `/usr/sbin/nologin`, `/bin/false` u otro programa restringido.

No deduzcas el propósito de una cuenta únicamente por su intervalo de UID sin consultar la política de la distribución. Los intervalos de asignación varían y las cuentas gestionadas centralmente pueden seguir convenciones distintas.

:::single-choice{#passwd-nologin-shell}
¿Cuál es un propósito habitual de un programa de inicio de sesión como `/usr/sbin/nologin` en el campo 7?

::option[Eliminar los archivos de la cuenta cada vez que se detiene un servicio.]{#passwd-nologin-delete explanation="El programa de inicio de sesión no elimina automáticamente datos propiedad de la cuenta ni gestiona archivos al detener servicios."}
::option[Impedir un shell interactivo normal mediante rutas de inicio de sesión que respetan el campo.]{#passwd-nologin-purpose .correct explanation="Un programa que impide iniciar sesión se usa habitualmente para cuentas de servicio que no deben recibir un shell interactivo mediante un inicio de sesión normal."}
::option[Conceder a la cuenta los mismos privilegios que al UID 0.]{#passwd-nologin-root explanation="Restringir el inicio de sesión interactivo no eleva la cuenta ni cambia su UID numérico."}
:::

## Modificar registros de cuentas de forma segura

Prefiere herramientas de gestión de cuentas como `useradd`, `usermod` y `userdel`, ya que coordinan registros relacionados y aplican los valores predeterminados del sistema. Su comportamiento exacto puede configurarse por distribución, así que revisa las opciones antes de cambiar una cuenta.

Si una base de datos passwd local necesita realmente una reparación manual, usa `vipw` en vez de un editor normal. Aplica un bloqueo destinado a evitar ediciones simultáneas. Valida las bases de datos con herramientas como `pwck` y mantén una sesión de recuperación antes de cambiar archivos de autenticación de forma remota.

Para practicar los registros de usuarios y grupos en un entorno controlado, prueba estos laboratorios prácticos:

1. **[Gestionar cuentas de usuario de Linux con useradd, usermod y userdel](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - Practica todo el ciclo de administración de usuarios, desde crear y proteger cuentas hasta modificarlas y eliminarlas.
2. **[Gestionar grupos de Linux con groupadd, usermod y groupdel](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - Practica las utilidades principales para crear grupos y modificar pertenencias de usuarios.

## Resumen

Ahora puedes interpretar registros passwd locales sin confundirlos con la base de datos de identidades completa.

1. Consulta cuentas resueltas por NSS con `getent passwd`.
2. Lee los siete campos de passwd separados por dos puntos.
3. Localiza los campos UID y GID principal.
4. Interpreta los marcadores de contraseña sin exagerar el estado de inicio de sesión.
5. Usa herramientas de cuentas o `vipw` en vez de un editor normal.
