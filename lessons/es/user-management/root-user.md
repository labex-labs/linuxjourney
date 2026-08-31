---
lesson_id: "root-user"
course_id: "user-management"
lang: "es"
order_index: 2
title: "root"
description: "Aprende cómo su, sudo y la política sudoers proporcionan acceso controlado a identidades con privilegios."
meta_title: "root - Gestión de usuarios"
meta_description: "Explora el papel del usuario root en Linux, las diferencias entre su y sudo y cómo la política sudoers controla el acceso administrativo."
meta_keywords: "usuario root Linux, su, sudo, sudoers, visudo, superusuario, gestión de usuarios, permisos Linux"
---

La cuenta tradicionalmente llamada `root` tiene el UID 0 y una amplia autoridad dentro de su contexto de seguridad. Usa una cuenta sin privilegios para el trabajo rutinario y elévalos solo para un propósito administrativo concreto que comprendas.

## Iniciar un shell como otro usuario con su

`su`, de *substitute user* (sustituir usuario), inicia un shell o una orden con la identidad de otra cuenta. Sin un nombre de usuario, el destino predeterminado es root:

```bash
$ su
```

La autenticación está controlada por PAM y por la política local. Un sistema puede solicitar la contraseña de la cuenta de destino, restringir quién puede usar `su` o mantener bloqueada la contraseña de root. No des por hecho que conocer una contraseña es la única condición.

`su` sin más cambia la identidad y conserva una mayor parte del entorno actual. `su - USER`, también escrito como `su --login USER`, inicia un shell de inicio de sesión y configura un entorno más parecido a una sesión nueva de la cuenta de destino:

```bash
$ su - operator
```

Sal del subshell cuando termines el trabajo específico de esa cuenta.

:::single-choice{#root-su-login-shell}
¿Qué orden solicita un shell de inicio de sesión como el usuario `operator`?

::option[`su - operator`]{#root-su-login-operator .correct explanation="El guion solicita el comportamiento de un shell de inicio de sesión y un entorno orientado al usuario `operator`."}
::option[`su operator`]{#root-su-preserve-environment explanation="Esto cambia a la identidad de destino, pero no solicita la inicialización completa de inicio de sesión presentada aquí."}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l` enumera órdenes permitidas por la política; no inicia el shell de sesión solicitado."}
:::

## Ejecutar una orden concreta con sudo

`sudo COMMAND` solicita autorización según una política para ejecutar una orden como un usuario de destino, normalmente root de forma predeterminada. Usa `-u USER` para solicitar otro destino:

```bash
$ sudo -u postgres id
```

Esto no significa que la solicitud vaya a permitirse. La política de sudo controla el usuario que la invoca, el host, la identidad de destino, la orden y otras condiciones. La autenticación puede usar la contraseña del usuario que la invoca, otro mecanismo o no mostrar ninguna solicitud, según la configuración.

Cuando sea práctico, prefiere una orden administrativa de ámbito reducido a un shell con privilegios de larga duración. Un ámbito menor reduce la probabilidad de que órdenes accidentales se ejecuten con autoridad elevada.

:::single-choice{#root-sudo-target-user}
¿Qué solicita `sudo -u postgres id`?

::option[Cambiar permanentemente el nombre de la cuenta actual a `postgres`.]{#root-sudo-rename explanation="`sudo` ejecuta una orden con credenciales de destino; no cambia el nombre de los registros de cuentas."}
::option[Ejecutar `id` con `postgres` como usuario de destino, sujeto a la política.]{#root-sudo-postgres-id .correct explanation="La opción `-u` selecciona la identidad de destino y la política sudoers decide si se permite la solicitud."}
::option[Enumerar todos los usuarios cuyo UID es mayor que el del usuario actual.]{#root-sudo-list-uids explanation="La orden `id` muestra información de identidad de su proceso; esta sintaxis no enumera UID de cuentas."}
:::

## Evitar shells con privilegios persistentes

Órdenes como `su -`, `sudo -s` o `sudo -i` pueden crear un shell con privilegios cuando la política lo permite. Todas las órdenes posteriores de ese shell pueden conservar un impacto elevado hasta que salgas. Los errores de rutas, los scripts no revisados y las expansiones del shell se vuelven más peligrosos.

El comportamiento de auditoría depende de la configuración. `sudo` suele registrar las invocaciones, pero un único inicio registrado de un shell no proporciona automáticamente un registro completo de todas las órdenes escritas dentro de él. El historial del shell, la auditoría del sistema y el registro de entrada y salida de sudo son mecanismos separados con políticas propias.

:::single-choice{#root-persistent-shell-risk}
¿Por qué un shell root de larga duración es más arriesgado que elevar una orden conocida cada vez?

::option[Los shells root eliminan automáticamente todas las órdenes de todos los sistemas de auditoría.]{#root-shell-no-audit explanation="El registro varía según la configuración; no es correcto afirmar que todos los registros de auditoría se borran automáticamente."}
::option[El shell desactiva las rutas del sistema de archivos con más de un componente.]{#root-shell-path-limit explanation="Los privilegios no imponen esta restricción de rutas; el problema es la autoridad aplicada a operaciones normales."}
::option[Las órdenes posteriores pueden conservar un impacto elevado hasta que se cierre el shell.]{#root-shell-elevated-scope .correct explanation="Una identidad con privilegios persistente amplía el intervalo durante el cual un error o una orden no fiable puede modificar recursos protegidos."}
:::

## Revisar la autorización de sudo

Ejecuta `sudo -l` para mostrar lo que la cuenta actual puede solicitar según la política activa:

```bash
$ sudo -l
```

Revisa las rutas de las órdenes, los usuarios de destino permitidos y las restricciones de argumentos. Una regla que parezca amplia no debe interpretarse como permiso para realizar trabajo no relacionado.

:::single-choice{#root-list-sudo-rules}
¿Qué orden enumera los privilegios sudo disponibles para el usuario que la invoca actualmente?

::option[`sudo -i`]{#root-sudo-login explanation="Esto solicita un shell de inicio de sesión de destino y puede ampliar el ámbito de privilegios; no es una lista de solo lectura de la política."}
::option[`sudo -l`]{#root-sudo-list .correct explanation="La opción `-l` minúscula pide a sudo que enumere las órdenes permitidas por su política actual."}
::option[`su -l`]{#root-su-login-default explanation="Esto invoca el comportamiento de shell de inicio de sesión de `su` en vez de enumerar la autorización de sudo."}
:::

## Editar la política sudoers de forma segura

La política sudo predeterminada suele leer `/etc/sudoers` y puede incluir archivos de `/etc/sudoers.d/`. También son posibles otros orígenes de políticas. La sintaxis controla mucho más que una simple lista de usuarios y grupos.

Usa `visudo` para cambiar la política, ya que bloquea el archivo y valida la sintaxis antes de instalarlo:

```bash
$ sudo visudo
```

Para un archivo adicional, indica su ruta exacta:

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

No edites sudoers con una redirección normal ni con un flujo de editor sin validación. Un error de sintaxis o permisos puede eliminar el acceso administrativo. Mantén disponible otra vía de recuperación verificada cuando cambies autorizaciones remotas.

:::single-choice{#root-edit-sudoers-safely}
¿Qué herramienta debe usarse para editar y comprobar la sintaxis de la política sudoers principal?

::option[`cat`]{#root-cat-sudoers explanation="`cat` puede mostrar texto legible, pero no edita, bloquea ni valida de forma segura la sintaxis de sudoers."}
::option[`visudo`]{#root-visudo .correct explanation="`visudo` proporciona bloqueo y validación de sintaxis diseñados para cambiar la política sudoers."}
::option[`echo` con `>`]{#root-echo-sudoers explanation="La redirección del shell puede truncar la política inmediatamente y no ofrece validación de la sintaxis sudoers."}
:::

Para practicar la administración delegada en un entorno controlado, prueba este laboratorio práctico:

1. **[Configurar cuentas de usuario y privilegios sudo en Linux](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Practica políticas de contraseñas, bloqueo y desbloqueo de cuentas, protección de root y concesión de permisos administrativos.

## Resumen

Ahora puedes distinguir el cambio de identidad de la delegación de órdenes controlada por políticas.

1. Usa `su - USER` solo cuando quieras un shell de inicio de sesión del destino.
2. Solicita un destino sudo concreto con `-u USER`.
3. Minimiza el tiempo que pasas en un shell con privilegios.
4. Revisa las reglas sudo efectivas con `sudo -l`.
5. Edita la política sudoers únicamente mediante `visudo`.
