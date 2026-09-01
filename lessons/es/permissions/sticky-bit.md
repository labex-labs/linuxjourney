---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "es"
order_index: 8
title: "El bit sticky"
description: "Aprende cómo el bit sticky protege las entradas de directorios compartidos con escritura, como /tmp."
meta_title: "El bit sticky - Permisos"
meta_description: "Descubre cómo el bit sticky protege archivos en directorios compartidos como /tmp, cómo reconocerlo y cómo establecerlo mediante chmod."
meta_keywords: "bit sticky, sticky bit Linux, permisos Unix, chmod +t, directorio /tmp, permisos de archivos, seguridad Linux"
---

Un directorio con permiso de escritura permite normalmente que un usuario autorizado elimine o cambie el nombre de sus entradas, aunque no sea propietario de los archivos. El bit sticky añade una restricción de propiedad que hace más seguros los directorios compartidos con escritura.

## Cómo restringe el bit sticky la eliminación

Cuando un directorio tiene establecido el bit sticky, Linux suele permitir eliminar o cambiar el nombre de una entrada únicamente a un proceso con privilegios suficientes, al propietario del directorio o al propietario de la entrada. Los permisos normales de escritura y búsqueda del directorio siguen siendo necesarios.

La restricción afecta a las entradas del directorio. No impide que el propietario de un archivo edite su contenido si sus permisos permiten la operación, ni convierte el directorio en privado.

:::single-choice{#sticky-bit-removal-rule} En un directorio compartido con sticky, ¿qué usuario normal puede eliminar normalmente una entrada concreta?

::option[Cualquier usuario que pueda enumerar el directorio.]{#sticky-bit-any-reader explanation="El permiso de lectura del directorio puede revelar nombres, pero no evita la restricción de propiedad del bit sticky."}
::option[El propietario de la entrada, con el acceso necesario al directorio.]{#sticky-bit-entry-owner .correct explanation="El propietario de la entrada es una de las identidades que suele permitir la regla de un directorio sticky."}
::option[Únicamente un miembro del grupo de la entrada.]{#sticky-bit-entry-group explanation="La pertenencia al grupo por sí sola no es la excepción de propiedad definida por el bit sticky."}
:::

## Reconocer el bit en `/tmp`

El directorio temporal del sistema es un ejemplo habitual:

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

La `t` minúscula final ocupa la posición de ejecución de otros. Significa que están presentes tanto el bit sticky como el permiso de ejecución de otros. Una `T` mayúscula indica que sticky está establecido, pero falta la ejecución de otros.

Como `/tmp` suele permitir escritura y búsqueda a todo el mundo, varios usuarios pueden crear entradas en él. El bit sticky impide que un usuario normal elimine las entradas de otro simplemente porque el directorio permite escritura a todos. Las aplicaciones aún deben crear objetos temporales de forma segura, porque los nombres predecibles, los enlaces inseguros y los modos débiles de archivo plantean riesgos distintos.

:::single-choice{#sticky-bit-lowercase-t} ¿Qué indica una `t` minúscula al final del modo de un directorio?

::option[Sticky y la ejecución de otros están establecidos.]{#sticky-bit-t-with-execute .correct explanation="La `t` minúscula combina el bit especial sticky con el bit normal de ejecución de otros."}
::option[Sticky está establecido, pero falta la ejecución de otros.]{#sticky-bit-t-without-execute explanation="Esa combinación se muestra con una `T` mayúscula."}
::option[Setgid y la ejecución de grupo están establecidos.]{#sticky-bit-setgid-position explanation="Setgid aparece en la posición de ejecución del grupo, no en la posición final de otros."}
:::

## Establecer y eliminar el bit sticky

Establece el bit simbólicamente:

```bash
$ chmod +t shared-directory
```

En un dígito octal inicial de bits especiales, sticky aporta `1`:

```bash
$ chmod 1777 shared-directory
```

El `1` inicial establece sticky y `777` proporciona el modo normal. Este modo solo es apropiado cuando el directorio se comparte intencionadamente entre todos los usuarios locales. Para un directorio de equipo pueden ser preferibles permisos de grupo más restringidos. Elimina únicamente el bit sticky con `chmod -t shared-directory`.

:::single-choice{#sticky-bit-octal-value} ¿Qué valor octal inicial representa el bit sticky?

::option[`2`]{#sticky-bit-value-two explanation="Un `2` inicial representa setgid."}
::option[`1`]{#sticky-bit-value-one .correct explanation="El bit sticky aporta `1` al dígito inicial de bits especiales."}
::option[`4`]{#sticky-bit-value-four explanation="Un `4` inicial representa setuid."}
:::

## Verificar toda la política del directorio

Sticky no concede acceso de escritura ni búsqueda; solo restringe la eliminación y el cambio de nombre después de que los permisos normales permitan modificar el directorio. Verifica conjuntamente el propietario, el grupo, el modo normal, las ACL y el contexto de montaje del directorio. Prueba con cuentas sin privilegios en un entorno aislado en vez de modificar `/tmp` en un sistema operativo.

:::single-choice{#sticky-bit-access-scope} ¿Añadir el bit sticky hace que un directorio sin permiso de escritura pase a permitirla a otros usuarios?

::option[Sí; sticky añade automáticamente escritura a todas las clases.]{#sticky-bit-adds-write explanation="El bit especial no reescribe los bits de escritura de propietario, grupo u otros."}
::option[Sí; sticky desactiva el triplete de permisos de otros del directorio.]{#sticky-bit-disables-other explanation="El triplete de otros sigue participando en las comprobaciones normales de acceso."}
::option[No; los permisos normales de escritura y búsqueda siguen controlando el acceso.]{#sticky-bit-no-write-grant .correct explanation="Sticky restringe ciertas operaciones de eliminación y cambio de nombre, pero no añade permisos normales que falten."}
:::

Para practicar, crea un directorio compartido desechable, establece un modo normal adecuado y el bit sticky y prueba después la eliminación de entradas con dos usuarios sin privilegios. El laboratorio [Eliminar y mover archivos](https://labex.io/labs/linux-delete-and-move-files-7777) permite reforzar las operaciones subyacentes de cambio de nombre y eliminación.

## Resumen

Ahora puedes explicar y verificar el bit sticky en directorios compartidos.

1. Relaciona sticky con las restricciones de propiedad sobre eliminación y cambio de nombre.
2. Reconoce `t` minúscula y `T` mayúscula en un listado largo.
3. Establece el bit simbólicamente o con el valor octal inicial `1`.
4. Evalúa sticky junto con los permisos normales del directorio.
