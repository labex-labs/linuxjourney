---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "es"
order_index: 5
title: "Setuid"
description: "Aprende cómo el bit de modo set-user-ID afecta a los programas ejecutables y por qué requiere una revisión cuidadosa de seguridad."
meta_title: "Setuid - Permisos"
meta_description: "Aprende cómo funciona setuid (SUID) en Linux, cómo reconocerlo y modificarlo y por qué los ejecutables con privilegios requieren una revisión de seguridad."
meta_keywords: "setuid Linux, SUID, permisos Linux, chmod, orden passwd, seguridad Linux, tutorial Linux"
---

Algunos programas necesitan un acceso estrictamente controlado que sus usuarios no tienen normalmente. En un archivo normal ejecutable, el bit set-user-ID puede hacer que un proceso nuevo reciba como ID de usuario efectivo el del propietario del archivo. El programa puede realizar entonces operaciones autorizadas para esa identidad y conservar al mismo tiempo información sobre quien lo invocó.

Setuid no es una instrucción general para «ejecutar como root». Su efecto depende del propietario del ejecutable, el sistema operativo, el sistema de archivos y sus opciones de montaje y la forma en que el programa gestiona sus credenciales.

## Reconocer setuid

En sistemas que usan un ejecutable `passwd` con setuid, un listado largo puede parecerse a este:

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

La `s` minúscula en la posición de ejecución del propietario significa que están establecidos tanto setuid como la ejecución del propietario. Si setuid está presente pero no lo está la ejecución del propietario, `ls -l` muestra una `S` mayúscula en esa posición.

No des por hecho que todas las distribuciones tienen el mismo modo o diseño de autenticación. Consulta el sistema real en vez de confiar en el ejemplo.

:::single-choice{#setuid-lowercase-s} ¿Qué indica una `s` minúscula en la posición de ejecución del propietario?

::option[Setuid está establecido, pero falta la ejecución del propietario.]{#setuid-s-without-execute explanation="Esa combinación se muestra con una `S` mayúscula, no con una `s` minúscula."}
::option[El archivo tiene el bit sticky y ejecución de grupo.]{#setuid-sticky-group explanation="El bit sticky aparece en la posición de ejecución de otros, mientras que setuid aparece en la del propietario."}
::option[Setuid y la ejecución del propietario están establecidos.]{#setuid-s-with-execute .correct explanation="La `s` minúscula representa el bit setuid junto con el bit normal de ejecución del propietario."}
:::

## Comprender el cambio de credenciales

Cuando el kernel respeta setuid durante la ejecución, el proceso nuevo suele recibir un ID de usuario efectivo basado en el propietario del ejecutable. En un programa propiedad de root, esto puede proporcionar acceso autorizado para root, pero solo mientras se ejecuta el programa y únicamente mediante las operaciones que realiza su código.

Este mecanismo puede permitir que un programa cuidadosamente escrito valide una solicitud y realice un cambio restringido en un estado protegido. Por ejemplo, una utilidad local para cambiar contraseñas puede necesitar acceso controlado a datos de autenticación que los usuarios normales no pueden editar directamente. Las implementaciones modernas también dependen de PAM, bloqueo de archivos, políticas y otras protecciones; setuid por sí solo no explica todo el flujo.

:::single-choice{#setuid-effective-identity} Cuando se respeta un ejecutable setuid, ¿qué identidad se obtiene principalmente del propietario del archivo?

::option[El nombre de inicio de sesión almacenado en `/etc/passwd`.]{#setuid-login-name explanation="Ejecutar un archivo no reescribe el registro de la cuenta ni el nombre de inicio de sesión de quien lo invoca."}
::option[El ID de usuario efectivo del proceso.]{#setuid-effective-user .correct explanation="El mecanismo set-user-ID de ejecución cambia la identidad de usuario efectiva empleada en muchas comprobaciones de autorización."}
::option[El grupo propietario de todos los archivos abiertos.]{#setuid-opened-file-group explanation="Setuid afecta a las credenciales del proceso, no a los metadatos de propiedad de archivos no relacionados."}
:::

## Establecer y eliminar el bit

Establece setuid simbólicamente con:

```bash
$ sudo chmod u+s myfile
```

En notación octal, setuid aporta `4` en un dígito inicial de bits especiales:

```bash
$ sudo chmod 4755 myfile
```

Aquí, el `4` inicial establece setuid y `755` establece los bits normales de propietario, grupo y otros. Elimina setuid sin cambiar el resto del modo mediante `chmod u-s myfile`.

:::single-choice{#setuid-octal-value} ¿Qué valor octal inicial representa el bit especial setuid?

::option[`4`]{#setuid-octal-four .correct explanation="Setuid aporta el valor `4` en el dígito inicial de bits especiales."}
::option[`1`]{#setuid-octal-one explanation="Un `1` inicial representa el bit sticky."}
::option[`2`]{#setuid-octal-two explanation="Un `2` inicial representa el bit setgid."}
:::

## Tratar setuid como sensible para la seguridad

Un fallo en un programa setuid con privilegios puede convertirse en una vía de escalada de privilegios. Estos programas deben validar la entrada, controlar el entorno y las rutas en las que confían, evitar comportamientos inseguros de subprocesos, minimizar el código con privilegios y abandonarlos tan pronto como sea posible.

Linux no suele respetar setuid en scripts interpretados porque hacerlo de forma segura plantea problemas de carreras y del intérprete. Los sistemas de archivos montados con `nosuid` también suprimen los efectos setuid y setgid. Prefiere mecanismos más limitados, como operaciones mediadas por servicios, políticas `sudo` de ámbito reducido o capacidades, cuando se adapten al requisito.

Nunca añadas setuid a un shell, intérprete o programa copiado arbitrario como experimento en un sistema compartido. Audita los archivos setuid existentes y practica únicamente en un entorno aislado y desechable.

:::single-choice{#setuid-nosuid-mount} ¿Cuál es el propósito de montar un sistema de archivos con `nosuid`?

::option[Eliminar todos los bits de ejecución almacenados en los archivos del sistema de archivos.]{#setuid-nosuid-remove-execute explanation="La opción no reescribe los bits normales de ejecución de los metadatos."}
::option[Suprimir los efectos de ejecución setuid y setgid en ese sistema de archivos.]{#setuid-nosuid-suppress .correct explanation="La opción de montaje `nosuid` impide que esos bits especiales concedan su comportamiento normal de cambio de credenciales durante la ejecución."}
::option[Hacer que todos los archivos del sistema de archivos pertenezcan a root.]{#setuid-nosuid-root-owner explanation="Montar con `nosuid` no cambia los campos de usuario ni grupo propietarios."}
:::

## Resumen

Ahora puedes reconocer setuid y explicar sus implicaciones de credenciales y seguridad.

1. Localiza `s` o `S` en la posición de ejecución del propietario.
2. Relaciona la ejecución setuid con la identidad de usuario efectiva del propietario del ejecutable.
3. Establece o elimina el bit mediante modos `chmod` simbólicos u octales.
4. Trata todo ejecutable con privilegios como código sensible para la seguridad.
