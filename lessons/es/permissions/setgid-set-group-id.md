---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "es"
order_index: 6
title: "Setgid"
description: "Aprende cómo set-group-ID afecta a las credenciales de ejecutables y a la herencia de grupos en directorios compartidos."
meta_title: "Setgid - Permisos"
meta_description: "Aprende cómo funciona setgid (SGID) en Linux sobre ejecutables y directorios, cómo reconocerlo y modificarlo y cómo usarlo en árboles compartidos."
meta_keywords: "setgid Linux, SGID, Set Group ID, permisos Linux, chmod g+s, seguridad Linux, tutorial Linux"
---

El bit set-group-ID, llamado habitualmente setgid o SGID, tiene dos usos importantes. En un archivo normal ejecutable, puede cambiar el ID de grupo efectivo del proceso nuevo. En un directorio, hace que las entradas nuevas hereden el grupo del directorio, lo que resulta especialmente útil para árboles colaborativos.

## Setgid en archivos ejecutables

Un listado largo puede mostrar setgid en la posición de ejecución del grupo:

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

La `s` minúscula significa que están establecidos tanto setgid como la ejecución del grupo. La `S` mayúscula significa que setgid está establecido, pero falta la ejecución del grupo.

Cuando el kernel respeta este bit durante la ejecución, el proceso recibe un ID de grupo efectivo basado en el grupo propietario del ejecutable. Controles como un montaje `nosuid` pueden suprimir el comportamiento, y no debe considerarse una garantía universal para todos los tipos de archivo y entornos.

:::single-choice{#setgid-executable-effect}
Cuando se respeta setgid en un ejecutable, ¿qué credencial procede del grupo propietario del ejecutable?

::option[El ID de grupo efectivo del proceso.]{#setgid-effective-group .correct explanation="La ejecución set-group-ID establece el grupo propietario del ejecutable como identidad de grupo efectiva del proceso."}
::option[El ID de usuario real del proceso.]{#setgid-real-user explanation="El bit se refiere a la credencial de grupo, no a la identidad de usuario real de quien lo invoca."}
::option[El propietario de todos los archivos que abre el proceso.]{#setgid-opened-owner explanation="Las credenciales de ejecución no reescriben los metadatos de propiedad de los archivos abiertos."}
:::

## Setgid en directorios

Setgid tiene otro propósito en un directorio. Los archivos y subdirectorios nuevos suelen heredar el grupo del directorio en vez del grupo predeterminado de quien los crea. En Linux, los subdirectorios nuevos también heredan el bit setgid, lo que ayuda a mantener un grupo uniforme en un árbol de proyecto compartido.

Setgid no concede por sí solo permiso de escritura al grupo. El modo del directorio, la umask del proceso, el modo de creación solicitado, las ACL predeterminadas y otros controles siguen determinando el acceso.

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance}
¿Qué hace normalmente que un archivo nuevo herede setgid en `/srv/project`?

::option[El usuario propietario del directorio.]{#setgid-inherit-user explanation="Setgid de directorio afecta a la herencia de grupo, no al usuario propietario de la entrada nueva."}
::option[El modo de permisos completo del directorio.]{#setgid-inherit-mode explanation="Los permisos de creación todavía se calculan a partir del modo solicitado, la umask y las ACL existentes."}
::option[El grupo propietario del directorio.]{#setgid-inherit-group .correct explanation="Una entrada nueva suele recibir el grupo del directorio setgid, lo que mantiene una propiedad compartida uniforme."}
:::

## Establecer y eliminar setgid

Establece el bit simbólicamente con:

```bash
$ sudo chmod g+s myfile
```

Establécelo junto con los bits de modo normales mediante un `2` octal inicial:

```bash
$ sudo chmod 2755 myfile
```

Elimina únicamente el bit especial con `chmod g-s myfile`.

:::single-choice{#setgid-octal-value}
¿Qué valor aporta setgid al dígito octal inicial de bits especiales?

::option[`4`]{#setgid-value-four explanation="El valor `4` representa setuid en el dígito de bits especiales."}
::option[`1`]{#setgid-value-one explanation="El valor `1` representa el bit sticky."}
::option[`2`]{#setgid-value-two .correct explanation="Setgid aporta `2`, como en el modo `2755`."}
:::

## Usar directorios compartidos de forma segura

Para un directorio colaborativo, combina el grupo propietario deseado, setgid y unos bits de acceso cuidadosamente elegidos. Prueba la creación con usuarios representativos y consulta los resultados mediante `ls -ld`. No hagas que un árbol permita escritura a todo el mundo simplemente para resolver problemas de uso compartido por grupo; un grupo dedicado, una umask o ACL predeterminada adecuada y un directorio setgid suelen proporcionar un control más claro.

:::single-choice{#setgid-directory-write-access}
¿Establecer setgid por sí solo permite a los miembros del grupo crear archivos en un directorio?

::option[Sí; setgid siempre añade lectura, escritura y ejecución al grupo.]{#setgid-adds-rwx explanation="El bit especial no modifica automáticamente los tres bits normales de permisos del grupo."}
::option[Sí; setgid desactiva todas las comprobaciones para los miembros del grupo.]{#setgid-disables-checks explanation="Las comprobaciones discrecionales normales y los controles de seguridad adicionales siguen aplicándose."}
::option[No; los permisos aplicables de escritura y búsqueda también deben permitir la creación.]{#setgid-no-automatic-write .correct explanation="Setgid controla la herencia de grupo, mientras que los permisos normales y otros controles de acceso rigen la escritura en el directorio."}
:::

## Resumen

Ahora puedes distinguir los significados de setgid en ejecutables y directorios.

1. Reconoce setgid en la posición de ejecución del grupo.
2. Relaciona setgid en un ejecutable con el ID de grupo efectivo.
3. Usa setgid en directorios para conservar la propiedad de grupo en árboles compartidos.
4. Establece o elimina el bit sin confundirlo con el permiso normal de escritura.
