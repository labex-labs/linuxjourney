---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "es"
order_index: 3
title: "Permisos de propiedad"
description: "Aprende a consultar y cambiar el usuario y el grupo propietarios de objetos del sistema de archivos de Linux."
meta_title: "Permisos de propiedad - Permisos"
meta_description: "Domina la propiedad de archivos de Linux con las órdenes chown y chgrp. Aprende a cambiar el usuario y el grupo propietarios de forma segura."
meta_keywords: "chown, chgrp, propiedad de archivos Linux, cambiar propietario archivo, cambiar grupo archivo, permisos Linux, órdenes Linux"
---

Cada objeto del sistema de archivos de Linux registra un usuario propietario y un grupo propietario. Estas identidades determinan qué triplete de permisos de propietario o grupo se aplica, pero no conceden por sí mismas un permiso concreto. Consulta la propiedad y el modo con `ls -l`.

## Cambiar el usuario propietario

Usa `chown`, abreviatura de *change owner*, para asignar otro usuario propietario:

```bash
$ sudo chown patty myfile
```

Esto cambia a `patty` el usuario propietario de `myfile` y deja su grupo sin cambios. Modificar el usuario propietario de un archivo suele requerir los privilegios correspondientes, aunque seas su propietario actual. Esta restricción impide transferir archivos para eludir cuotas u otros controles basados en la propiedad.

:::single-choice{#ownership-permissions-change-user} ¿Qué orden cambia el usuario propietario de `myfile` a `patty` y deja su grupo sin cambios?

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="Un nombre de usuario sin grupo como operando de propiedad de `chown` cambia el usuario propietario y conserva el grupo."}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp` cambia el grupo propietario, no el usuario propietario."}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod` cambia bits de modo y no acepta un nombre de usuario como nuevo propietario."}
:::

## Cambiar el grupo propietario

Usa `chgrp` para asignar otro grupo propietario:

```bash
$ chgrp whales myfile
```

En los sistemas habituales, un propietario sin privilegios solo puede cambiar el grupo de un archivo a otro al que pertenezca. Los procesos con privilegios pueden realizar cambios más amplios. La forma equivalente de `chown` comienza con dos puntos:

```bash
$ chown :whales myfile
```

Después, los bits de modo del grupo se aplican cuando el kernel selecciona esa clase; cambiar el grupo no añade automáticamente bits de lectura, escritura o ejecución.

:::single-choice{#ownership-permissions-change-group} ¿Qué cambia `chgrp whales myfile`?

::option[El usuario propietario registrado para `myfile`.]{#ownership-permissions-group-not-user explanation="El usuario propietario se cambia con `chown`, no con `chgrp`."}
::option[Los miembros enumerados en el grupo `whales`.]{#ownership-permissions-group-members explanation="La orden cambia metadatos del archivo; no edita la base de datos de pertenencias a grupos del sistema."}
::option[El grupo propietario registrado para `myfile`.]{#ownership-permissions-group-owner .correct explanation="`chgrp` asigna el grupo indicado como propietario de grupo del objeto del sistema de archivos."}
:::

## Cambiar conjuntamente usuario y grupo

Proporciona `USER:GROUP` a `chown` para actualizar ambos campos en una operación:

```bash
$ sudo chown patty:whales myfile
```

La orden asigna `patty` como usuario propietario y `whales` como grupo propietario. Verifica el resultado en vez de dar por hecho que ha funcionado:

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both} ¿Qué especificación de propiedad asigna el usuario `patty` y el grupo `whales` en una orden `chown`?

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="Los dos puntos separan los nombres de usuario y grupo en la especificación conjunta de propiedad."}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="La barra no es el separador presentado para un operando de usuario y grupo de `chown`."}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="El signo más no se usa para combinar los dos campos de propiedad de `chown`."}
:::

## Tratar con cuidado los cambios recursivos

La opción `-R` cambia la propiedad recursivamente, pero una orden recursiva amplia puede atravesar árboles inesperados o afectar a datos de servicios. Confirma el destino exacto, comprende el comportamiento de tu implementación con enlaces simbólicos, previsualiza el árbol y verifica una muestra pequeña antes de cambiar una jerarquía grande. No copies órdenes de propiedad con privilegios de ejemplos a sistemas reales sin revisar su alcance.

:::single-choice{#ownership-permissions-mode-separate} Después de cambiar el grupo propietario de un archivo, ¿qué ocurre con sus bits normales de permisos de grupo?

::option[Siempre pasan automáticamente a lectura y escritura.]{#ownership-permissions-mode-read-write explanation="`chgrp` no selecciona automáticamente un modo de grupo fijo."}
::option[Se copian del triplete de permisos del propietario.]{#ownership-permissions-mode-copied explanation="Los tripletes de propietario y grupo siguen siendo independientes cuando cambia la propiedad."}
::option[Permanecen como estaban salvo que otra operación los cambie.]{#ownership-permissions-mode-unchanged .correct explanation="Los campos de propiedad y los bits de modo son metadatos separados; cambiar el grupo no concede por sí mismo bits nuevos al grupo."}
:::

Para practicar en un entorno aislado, el laboratorio [Usuarios, grupos y permisos de archivos en Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) explica cómo consultar y modificar la propiedad junto con los modos de archivo.

## Resumen

Ahora puedes distinguir los metadatos de propiedad de los bits de permisos y cambiarlos deliberadamente.

1. Usa `chown USER FILE` para cambiar el usuario propietario.
2. Usa `chgrp GROUP FILE` o `chown :GROUP FILE` para cambiar el grupo propietario.
3. Usa `chown USER:GROUP FILE` para establecer ambos campos.
4. Verifica los resultados y limita con cuidado los cambios recursivos.
