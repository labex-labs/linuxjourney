---
lesson_id: "touch-command"
course_id: "command-line"
lang: "es"
order_index: 5
title: "touch"
description: "Aprende a crear archivos vacíos y gestionar sus marcas de tiempo con la orden `touch`."
meta_title: "touch - Línea de Comandos"
meta_description: "Aprende el comando touch de Linux con ejemplos para crear archivos vacíos, actualizar marcas de tiempo, establecer fechas, usar archivos de referencia y evitar sobrescrituras."
meta_keywords: "comando linux touch, comando touch, crear archivo linux, actualizar marca de tiempo linux, touch -d, touch -r, touch -c"
---

La orden `touch` modifica las marcas de tiempo de los archivos. También se utiliza habitualmente para crear uno o varios archivos vacíos.

Su sintaxis básica es:

```bash
touch [OPTIONS] FILE...
```

## Creación de archivos vacíos

Si el archivo indicado no existe, `touch` lo crea vacío:

```bash
$ touch mysuperduperfile
```

Puedes crear varios archivos con una sola orden enumerando sus nombres:

```bash
$ touch file1.txt file2.txt file3.log
```

Esto resulta útil para crear marcadores de posición, pero `touch` no añade texto a los archivos. Cuando necesites un archivo con contenido, utiliza un editor de texto u otra orden diseñada para escribir datos.

:::single-choice{#create-several-empty-files} ¿Qué orden crea tres archivos vacíos llamados `one`, `two` y `three` si aún no existen?

::option[`touch "one two three"`]{#touch-one-spaced explanation="Las comillas hacen que todo sea un único nombre de archivo con espacios. Esta orden actúa sobre un archivo, no sobre tres."}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir` crea directorios, no archivos normales vacíos. Utiliza `touch` para crear los archivos solicitados."}
::option[`touch one two three`]{#touch-three .correct explanation="`touch` acepta varios operandos de archivo. Crea cada archivo que falte sin añadirle contenido."}
:::

## Actualización de las marcas de tiempo

Los archivos registran varias marcas de tiempo. De forma predeterminada, ejecutar `touch` sobre un archivo existente cambia tanto su hora de acceso como su hora de modificación a la hora actual. El contenido del archivo no se altera.

Puedes comparar la hora de modificación mostrada antes y después de ejecutar la orden:

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

La salida de `ls -l` suele mostrar la hora de modificación, no la de acceso.

:::single-choice{#touch-existing-file} ¿Qué ocurre al ejecutar `touch report.txt` si `report.txt` ya existe?

::option[Se actualizan sus marcas de tiempo sin sustituir el contenido.]{#timestamps-only .correct explanation="De forma predeterminada, `touch` actualiza las horas de acceso y modificación de un archivo existente. No sobrescribe sus datos."}
::option[Se elimina su contenido y el archivo queda vacío.]{#contents-deleted explanation="La creación de un archivo vacío solo ocurre cuando este no existe. Si ya existe, conserva el contenido mientras `touch` actualiza sus marcas de tiempo."}
::option[La orden falla porque el nombre del archivo ya está en uso.]{#existing-error explanation="`touch` está diseñado para actuar tanto sobre archivos existentes como sobre archivos ausentes. Un nombre existente no constituye un error por sí mismo."}
:::

## Control de la marca de tiempo que cambia

Utiliza `-a` para cambiar únicamente la hora de acceso o `-m` para cambiar solo la hora de modificación:

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only} ¿Qué orden actualiza únicamente la hora de modificación de `notes.txt`?

::option[`touch -a notes.txt`]{#access-only explanation="La opción `-a` cambia solo la hora de acceso. No selecciona la hora de modificación solicitada."}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="La opción `-m` limita el cambio a la hora de modificación. La hora de acceso permanece intacta."}
::option[`touch -c notes.txt`]{#no-create explanation="La opción `-c` controla si se crea un archivo ausente. No limita la actualización a una sola marca de tiempo."}
:::

## Establecer o copiar una hora

La opción `-d` acepta una cadena de fecha en vez de utilizar la hora actual:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Para asignar a un archivo las mismas horas de acceso y modificación que otro archivo de referencia, utiliza `-r`:

```bash
$ touch -r file1.txt file2.txt
```

En este caso, `file1.txt` proporciona las marcas de tiempo y `file2.txt` es el archivo que cambia. La opción `-t` ofrece otra forma de indicar una hora mediante un formato numérico compacto.

:::single-choice{#copy-reference-timestamps} ¿Qué orden copia las marcas de tiempo de `source.txt` a `target.txt`?

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="Con `-r`, el operando siguiente es el archivo de referencia y el último operando es el archivo cuyas marcas de tiempo se actualizan."}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="Esta orden invierte las funciones de los archivos. Utilizaría `target.txt` como referencia y actualizaría `source.txt`."}
::option[`touch -d source.txt target.txt`]{#date-source explanation="La opción `-d` espera una cadena de fecha, no un nombre de archivo de referencia. Utiliza `-r` para copiar las marcas de tiempo de otro archivo."}
:::

## Evitar la creación de archivos

Normalmente, `touch` crea un archivo cuando la ruta indicada no existe. Añade `-c` cuando solo quieras actualizarlo si ya existe:

```bash
$ touch -c existing-file.txt
```

Si `existing-file.txt` no existe, esta orden no lo crea. Este comportamiento puede ser útil en scripts que deben actualizar una marca de tiempo sin introducir un archivo nuevo.

:::single-choice{#update-without-creating} ¿Qué orden actualiza `status.log` si existe, pero no lo crea si falta?

::option[`touch -a status.log`]{#touch-access explanation="La opción `-a` selecciona la hora de acceso, pero aún podría crear un archivo ausente. No proporciona el comportamiento solicitado."}
::option[`touch -m status.log`]{#touch-modification explanation="La opción `-m` selecciona la hora de modificación, pero no impide crear un archivo que falte. Para ello se utiliza `-c`."}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="La opción `-c` impide crear un archivo ausente. Si el archivo existe, sus marcas de tiempo sí pueden actualizarse."}
:::

## Resumen

Ahora puedes utilizar `touch` para crear archivos vacíos y controlar sus marcas de tiempo.

1. Crear uno o varios archivos vacíos.
2. Actualizar marcas de tiempo sin cambiar el contenido.
3. Seleccionar la hora de acceso o de modificación.
4. Establecer una hora concreta o copiar la de un archivo de referencia.
5. Evitar la creación de un archivo ausente.
