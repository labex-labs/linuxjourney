---
lesson_id: "umask"
course_id: "permissions"
lang: "es"
order_index: 4
title: "Umask"
description: "Aprende cómo la umask de un proceso limita los bits de permisos solicitados para archivos y directorios nuevos."
meta_title: "Umask - Permisos"
meta_description: "Aprende a usar umask para controlar los permisos de creación en Linux y a calcular los modos resultantes de archivos y directorios nuevos."
meta_keywords: "umask, permisos Linux, permisos de archivos, órdenes Linux, Linux para principiantes, permisos predeterminados"
---

La máscara de creación de archivos de un proceso, o umask, impide que se establezcan determinados bits de permisos cuando ese proceso crea un objeto del sistema de archivos. Es una máscara, no un modo predeterminado completo: la aplicación solicita primero un modo y el kernel elimina los bits prohibidos por la umask.

Conceptualmente:

```text
resulting mode = requested mode AND NOT umask
```

Las listas de control de acceso y el comportamiento de la aplicación pueden añadir más detalles, así que consulta el resultado cuando los permisos exactos sean importantes.

## Consultar y establecer la umask

Ejecuta `umask` sin operandos para mostrar la máscara del shell actual, normalmente en formato octal:

```bash
$ umask
0022
```

Establécela para el shell actual y los procesos que este inicie posteriormente:

```bash
$ umask 027
```

Cada posición octal corresponde a propietario, grupo y otros. Un bit de máscara elimina el permiso solicitado correspondiente: `2` enmascara escritura, `4` enmascara lectura y `1` enmascara ejecución.

:::single-choice{#umask-command-purpose} ¿Qué cambia `umask 027` en el shell actual?

::option[Los permisos de todos los archivos que ya existen.]{#umask-existing-files explanation="Una umask afecta a las solicitudes de creación; no ejecuta retroactivamente `chmod` sobre objetos existentes."}
::option[La máscara que heredarán las órdenes iniciadas posteriormente desde ese shell.]{#umask-current-shell-mask .correct explanation="El shell establece la umask de su proceso y los procesos hijos suelen heredar ese valor."}
::option[Los nombres de propietario y grupo almacenados en archivos nuevos.]{#umask-owner-group explanation="La máscara filtra bits de permisos y no selecciona identidades de propiedad."}
:::

## Calcular los modos de archivos y directorios nuevos

Muchos programas normales solicitan `0666` para archivos normales nuevos, porque crear archivos ejecutables de forma predeterminada sería inseguro. Suelen solicitar `0777` para directorios nuevos, donde el permiso de ejecución es necesario para atravesarlos.

Con la umask `0022`:

```text
regular file: 0666 masked by 0022 -> 0644 (rw-r--r--)
directory:    0777 masked by 0022 -> 0755 (rwxr-xr-x)
```

La umask solo elimina bits solicitados. No puede añadir permiso de ejecución cuando una aplicación no lo ha solicitado. Una aplicación también puede solicitar un modo inicial más restrictivo, lo que produce un resultado más restrictivo.

:::single-choice{#umask-file-mode-022} Si un programa solicita el modo `0666` para un archivo normal y la umask es `0022`, ¿qué modo resulta?

::option[`0666`]{#umask-file-0666 explanation="La máscara `0022` elimina los bits de escritura de grupo y otros solicitados por `0666`."}
::option[`0755`]{#umask-file-0755 explanation="No se solicitaron bits de ejecución para el archivo normal, por lo que la umask no puede añadirlos."}
::option[`0644`]{#umask-file-0644 .correct explanation="Eliminar la escritura de grupo y otros de `0666` deja lectura y escritura para el propietario y solo lectura para grupo y otros."}
:::

:::single-choice{#umask-directory-mode-027} Si un programa solicita `0777` para un directorio y la umask es `0027`, ¿qué modo resulta?

::option[`0777`]{#umask-directory-0777 explanation="La máscara no nula filtra la escritura de grupo solicitada y todos los permisos de otros."}
::option[`0640`]{#umask-directory-0640 explanation="Ese resultado también elimina bits de ejecución que la máscara `0027` no elimina del propietario ni del grupo."}
::option[`0750`]{#umask-directory-0750 .correct explanation="La máscara elimina la escritura de grupo y todos los permisos de otros, dejando `rwxr-x---`."}
:::

## Ámbito y persistencia

Cambiar la umask en un shell no modifica su proceso padre ni otras sesiones. El valor se aplica a las creaciones futuras de ese shell y sus descendientes; los archivos existentes conservan sus modos.

Para hacer persistente un valor preferido, configúralo en el inicio de sesión, shell, PAM, gestor de servicios o aplicación apropiado para tu entorno. La ubicación correcta varía y los servicios pueden establecer su propia umask. No des por hecho que editar un archivo de un shell interactivo controla todos los procesos del sistema.

:::single-choice{#umask-existing-file-effect} ¿Qué le ocurre a un archivo existente cuando estableces una umask nueva?

::option[Su modo actual no cambia.]{#umask-existing-unchanged .correct explanation="Una umask nueva filtra solicitudes de creación posteriores y no modifica modos ya almacenados en objetos del sistema de archivos."}
::option[Su modo se vuelve a calcular a partir de `0666`.]{#umask-existing-recalculated explanation="Los objetos existentes no se recrean ni se pasan automáticamente por la máscara nueva."}
::option[Su propietario pierde inmediatamente los permisos enmascarados.]{#umask-existing-owner-loss explanation="Cambiar la umask de un proceso no es una operación sobre los metadatos de archivos existentes."}
:::

Para practicar, crea archivos y directorios con distintas máscaras en un entorno aislado y compara sus modos mediante `ls -ld`. El laboratorio [Usuarios, grupos y permisos de archivos en Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) ofrece un espacio adecuado.

## Resumen

Ahora puedes predecir cómo una umask limita los permisos recién solicitados.

1. Consulta o establece la máscara del shell actual con `umask`.
2. Elimina los bits enmascarados del modo solicitado por una aplicación.
3. Distingue las solicitudes habituales `0666` para archivos y `0777` para directorios.
4. Trata el ámbito y la persistencia de la umask como específicos del proceso y el entorno.
