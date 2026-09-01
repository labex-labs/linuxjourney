---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "es"
order_index: 2
title: "Modificar permisos"
description: "Aprende a cambiar los bits de permisos de Linux con modos simbólicos y octales de chmod."
meta_title: "Modificar permisos - Permisos"
meta_description: "Aprende a cambiar permisos en Linux con chmod. Esta guía explica los métodos simbólico y octal para gestionar de forma segura el acceso a archivos y directorios."
meta_keywords: "cambiar permisos Linux, cómo cambiar permisos Linux, chmod, permisos de archivos, seguridad Linux, permisos simbólicos, permisos octales"
---

La orden `chmod` cambia los bits de modo de archivos y directorios. Normalmente, solo el propietario del archivo o un proceso con los privilegios necesarios puede realizar este cambio. Consulta el modo actual con `ls -l` antes y después de ejecutar `chmod`.

## Usar el modo simbólico

Un modo simbólico indica qué clase de permisos se va a cambiar, cómo se modificará y qué permisos intervienen.

- `u` selecciona la clase del propietario.
- `g` selecciona la clase del grupo.
- `o` selecciona la clase de otros.
- `a` selecciona las tres clases.
- `+` añade permisos, `-` los elimina y `=` establece exactamente la clase seleccionada.

Por ejemplo, añade permiso de ejecución para el propietario:

```bash
$ chmod u+x myfile
```

Elimina el permiso de escritura del grupo:

```bash
$ chmod g-w myfile
```

Añade permiso de escritura para el propietario y el grupo:

```bash
$ chmod ug+w myfile
```

Se pueden separar varias cláusulas mediante comas. Esta orden establece lectura y escritura para el propietario, solo lectura para el grupo y ningún permiso para otros:

```bash
$ chmod u=rw,g=r,o= myfile
```

Si se omite la clase, como en `chmod +x myfile`, la umask del proceso afecta a las clases que cambian. Indicar explícitamente la clase facilita revisar el resultado deseado.

:::single-choice{#modifying-permissions-remove-group-write} ¿Qué modo simbólico elimina el permiso de escritura del grupo sin cambiar sus demás bits?

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="Esto elimina el permiso de escritura de la clase del propietario, no de la del grupo."}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="`g` selecciona la clase del grupo, `-` elimina un bit y `w` identifica el permiso de escritura."}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="El operador `=` sustituye la clase seleccionada por permiso exclusivo de escritura en vez de eliminarlo."}
:::

## Usar el modo octal

Un modo octal establece cada triplete de permisos básicos mediante un dígito. Suma estos valores dentro de cada clase:

- `4` para lectura.
- `2` para escritura.
- `1` para ejecución.
- `0` para ningún permiso.

Los tres dígitos de la derecha representan propietario, grupo y otros, en ese orden. Por ejemplo:

```bash
$ chmod 755 myfile
```

El modo `755` se descompone así:

- El `7` del propietario es `4 + 2 + 1`, o `rwx`.
- El `5` del grupo es `4 + 1`, o `r-x`.
- El `5` de otros es `4 + 1`, o `r-x`.

A diferencia de las operaciones simbólicas con `+` o `-`, un modo octal proporciona todo el conjunto de permisos normales. Una lección posterior explica el dígito inicial opcional de los bits de modo especiales.

:::single-choice{#modifying-permissions-octal-read-value} ¿Qué valor octal representa el permiso de lectura?

::option[`1`]{#modifying-permissions-value-one explanation="El valor `1` representa el permiso de ejecución."}
::option[`2`]{#modifying-permissions-value-two explanation="El valor `2` representa el permiso de escritura."}
::option[`4`]{#modifying-permissions-value-four .correct explanation="El permiso de lectura aporta el valor octal `4` al dígito de una clase."}
:::

:::single-choice{#modifying-permissions-mode-640} ¿Qué permisos normales establece `chmod 640 report`?

::option[Lectura para el propietario, escritura para el grupo y ejecución para otros.]{#modifying-permissions-640-separated explanation="Los dígitos octales son sumas para cada clase, no columnas separadas de lectura, escritura y ejecución."}
::option[Lectura y ejecución para el propietario, escritura para el grupo y ninguno para otros.]{#modifying-permissions-640-wrong-sums explanation="El valor `6` del propietario es lectura más escritura, mientras que el valor `4` del grupo es lectura."}
::option[Lectura y escritura para el propietario, lectura para el grupo y ninguno para otros.]{#modifying-permissions-640-correct .correct explanation="Los dígitos se convierten en propietario `6` (`rw-`), grupo `4` (`r--`) y otros `0` (`---`)."}
:::

## Aplicar cambios de forma segura

Concede únicamente el acceso que necesiten los usuarios y servicios. Evita `chmod 777` como atajo para resolver problemas, ya que concede lectura, escritura y ejecución a todas las clases, lo que suele aumentar el riesgo sin solucionar la propiedad, el recorrido de directorios, las ACL o la política del servicio.

Los cambios recursivos requieren especial cuidado. Previsualiza el árbol de destino, ten en cuenta los enlaces simbólicos y los sistemas de archivos montados y prueba con un ámbito pequeño antes de usar `chmod -R`. Después del cambio, verifica el modo resultante en vez de dar por hecho que la orden afectó a los objetos deseados.

:::single-choice{#modifying-permissions-least-privilege} ¿Por qué `chmod 777` suele ser una mala solución general para un problema de acceso?

::option[Elimina todos los permisos del propietario.]{#modifying-permissions-777-removes explanation="Cada `7` concede lectura, escritura y ejecución; no elimina los permisos del propietario."}
::option[Concede todos los permisos básicos a propietario, grupo y otros.]{#modifying-permissions-777-grants-all .correct explanation="Las tres clases reciben `rwx`, lo que suele superar el acceso realmente necesario."}
::option[Modifica únicamente la propiedad de grupo del archivo.]{#modifying-permissions-777-group explanation="`chmod` cambia bits de modo; la propiedad de grupo se cambia con una herramienta como `chgrp` o `chown`."}
:::

Para practicar en un entorno aislado, usa el laboratorio [Usuarios, grupos y permisos de archivos en Linux](https://labex.io/labs/linux-linux-user-group-and-file-permissions-18002) y consulta cada modo antes y después de cambiarlo.

## Resumen

Ahora puedes cambiar los bits de modo normales de Linux mediante expresiones `chmod` deliberadas.

1. Usa el modo simbólico para añadir, eliminar o asignar permisos concretos.
2. Construye dígitos octales con lectura `4`, escritura `2` y ejecución `1`.
3. Lee las clases octales en el orden propietario, grupo y otros.
4. Verifica los cambios y aplica el mínimo privilegio necesario.
