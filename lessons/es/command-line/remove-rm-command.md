---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "es"
order_index: 13
title: "rm (Eliminar)"
description: "Aprende a eliminar archivos y directorios comprobando los destinos y eligiendo opciones más seguras de `rm`."
meta_title: "rm (Eliminar) - Línea de Comandos"
meta_description: "Aprende el comando Linux rm con ejemplos seguros para eliminar archivos, borrar directorios, usar rm -r, rm -i y evitar errores con rm -rf."
meta_keywords: "comando linux rm, comando rm, rm -r, rm -i, rm -f, rm -rf, eliminar archivos linux, borrar directorio linux, rmdir"
---

La orden `rm` elimina entradas del sistema de archivos. La eliminación desde la línea de comandos normalmente no envía los elementos a la papelera del escritorio y `rm` no incorpora una función para deshacer, así que confirma todos los destinos antes de ejecutarla.

Su sintaxis básica es:

```bash
rm [OPTIONS] FILE...
```

## Eliminación de archivos

Para eliminar un archivo, pasa el nombre del archivo a `rm`.

```bash
$ rm file1
```

Puedes eliminar varios archivos a la vez listándolos uno tras otro.

```bash
$ rm notes.txt old-report.txt draft.md
```

Comprueba la ortografía y la ubicación antes de pulsar Enter. Una copia de seguridad o una versión almacenada en un sistema de control de versiones es un plan de recuperación más fiable que las herramientas de recuperación del sistema de archivos después de eliminar los datos.

:::single-choice{#remove-one-file}
Después de confirmar el destino, ¿qué orden elimina el archivo `old-report.txt`?

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm` elimina la entrada del archivo indicado. Normalmente la operación no lo envía a una papelera."}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir` actúa sobre directorios vacíos, no sobre archivos normales. No es la orden apropiada para este destino."}
::option[`mv old-report.txt`]{#mv-report explanation="`mv` necesita un destino y cambia una ruta en vez de eliminarla. Esta orden incompleta no realiza la eliminación solicitada."}
:::

## Previsualización de destinos con comodines

Los comodines del shell te permiten coincidir con varios archivos. Por ejemplo, esto elimina todos los archivos `.tmp` en el directorio actual:

```bash
$ rm *.tmp
```

Antes de usar `rm` con un comodín, es más seguro previsualizar la coincidencia con `ls`.

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

Recuerda que el shell expande `*.tmp` antes de que `rm` se ejecute. Si el patrón coincide con más archivos de los esperados, `rm` recibirá todos ellos.

:::single-choice{#preview-removal-pattern}
Planeas eliminar `*.tmp`. ¿Qué orden muestra primero las rutas no ocultas seleccionadas por el patrón sin borrarlas?

::option[`rm -v *.tmp`]{#verbose-remove explanation="El modo detallado informa de las eliminaciones mientras ocurren. Sigue borrando los archivos coincidentes y no es una previsualización de solo lectura."}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="Las comillas impiden expandir el comodín, por lo que se busca un nombre literal que contenga `*` en vez de previsualizar los destinos previstos."}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="La shell expande `*.tmp` para `ls`, lo que permite examinar el mismo conjunto de coincidencias no ocultas antes de eliminarlas."}
:::

## Solicitud de confirmación

Para un enfoque más seguro, usa la opción `-i`. Te pregunta antes de eliminar cada archivo.

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

La opción `-I` es una protección menos intrusiva de GNU `rm`: pregunta una vez cuando la orden eliminaría más de tres archivos o actuaría de forma recursiva.

:::single-choice{#confirm-each-removal}
¿Qué orden solicita confirmación antes de eliminar cada archivo indicado?

::option[`rm -i important.txt`]{#interactive-important .correct explanation="La opción `-i` pregunta antes de cada eliminación, lo que permite rechazar la operación."}
::option[`rm -f important.txt`]{#force-important explanation="La opción `-f` suprime los prompts e ignora un operando ausente. Elimina confirmaciones en vez de añadirlas."}
::option[`rm -v important.txt`]{#verbose-important explanation="La opción `-v` informa de lo que se ha eliminado, pero no pide aprobación previamente."}
:::

## Ignorar archivos ausentes con -f

La opción `-f` significa "force" (forzar). Ignora archivos inexistentes y no solicita confirmación.

```bash
$ rm -f old-cache.txt
```

Esto puede hacer que la limpieza de un script sea idempotente cuando un archivo generado quizá ya no exista. Como elimina la confirmación, no añadas `-f` solo para silenciar un error que no comprendes.

## Eliminación de directorios

Por defecto, `rm` no puede eliminar un directorio.

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

Para eliminar un directorio y todo su contenido, usa `-r` o `-R` para eliminación recursiva.

```bash
$ rm -r old-project
```

Para un directorio vacío, `rmdir` es una alternativa más limitada:

```bash
$ rmdir empty-directory
```

`rmdir` falla si el directorio no está vacío, lo que protege su contenido frente a una eliminación recursiva.

:::single-choice{#remove-empty-directory-only}
¿Qué orden elimina `old-cache/` únicamente si el directorio está vacío?

::option[`rm -r old-cache/`]{#recursive-cache explanation="`rm` recursivo elimina el directorio y su contenido. No impone la condición de que esté vacío."}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir` solo tiene éxito con un directorio vacío, por lo que no elimina recursivamente los archivos que contenga."}
::option[`rm -f old-cache/`]{#force-cache explanation="La opción `-f` no hace que un `rm` sin `-r` elimine directorios. Además, suprime protecciones en vez de comprobar que estén vacíos."}
:::

## Comprobación de una eliminación recursiva

La eliminación recursiva puede borrar un árbol completo. Combinar `-r` con `-f` también suprime los prompts, por lo que `rm -rf` exige validar el destino con especial cuidado. Antes de cualquier eliminación recursiva, comprueba:

- ¿Estás en el directorio que crees? Usa `pwd`.
- ¿Tu comodín se expandió correctamente? Previsualiza con `ls`.
- ¿La ruta es absoluta o relativa? `/tmp/cache` y `tmp/cache` son muy diferentes.
- ¿Hay un espacio accidental? `rm -rf old-project` y `rm -rf old project` apuntan a rutas diferentes.

Utiliza `--` antes de un destino que pueda comenzar con un guion para evitar que se interprete como una opción:

```bash
$ rm -- -old-name
```

No recurras a `sudo` simplemente porque `rm` informe de un error de permisos. Comprueba primero el destino y determina por qué tu cuenta no puede modificar el directorio que lo contiene. Una eliminación recursiva con privilegios puede dañar el sistema operativo o los datos de otros usuarios.

Utiliza `-v` cuando quieras que `rm` informe de cada eliminación realizada:

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree}
Después de verificar el destino completo, ¿qué orden elimina `old-project/` y todo su contenido sin suprimir los prompts normales?

::option[`rm old-project/`]{#plain-rm-project explanation="Un `rm` sin opciones no desciende por un directorio. No puede eliminar un árbol que contenga elementos."}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="La opción `-r` elimina recursivamente el árbol del directorio. A diferencia de `-rf`, esta forma no añade `-f` para suprimir los prompts."}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir` exige que el directorio esté vacío. Falla mientras el proyecto contenga elementos."}
:::

Para practicar la eliminación en un entorno controlado, prueba estos laboratorios:

1. **[Orden rm de Linux: eliminación de archivos](https://labex.io/es/labs/linux-linux-rm-command-file-removing-209741)** - Aprende a utilizar la orden `rm` para eliminar archivos y directorios, incluidas opciones como `-r` e `-i`, y practica una eliminación segura y eficaz.
2. **[Organización de archivos y directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practica habilidades esenciales de administración de archivos en Linux, incluido el uso de `rm` para limpiar directorios innecesarios, mediante un ejercicio práctico.

## Resumen

Ahora puedes eliminar elementos del sistema de archivos tratando cada destino como irreversible.

1. Confirmar las rutas de archivo antes de eliminarlas.
2. Previsualizar las expansiones de comodines con una orden de solo lectura.
3. Solicitar confirmación con `-i` o `-I`.
4. Preferir `rmdir` cuando el directorio deba estar vacío.
5. Validar el destino completo antes de una eliminación recursiva.
