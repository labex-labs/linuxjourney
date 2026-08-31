---
lesson_id: "stderr-standard-error-redirect"
course_id: "text-fu"
lang: "es"
order_index: 3
title: "stderr (Error estándar)"
description: "Aprende a redirigir el error estándar por separado o a combinarlo con la salida estándar en Bash."
meta_title: "stderr (Error Estándar) - Text-Fu"
meta_description: "Aprenda a gestionar el error estándar en Linux. Esta guía cubre la redirección de stderr, el descriptor de archivo stderr (2) y cómo redirigir stderr a un archivo o /dev/null usando 2>, 2>&1 y &>."
meta_keywords: "stderr, error estándar linux, descriptor de archivo stderr, archivo stderr, error estándar linux, redirigir stderr, 2>, 2>&1, &>, /dev/null, manejo de errores bash"
---

Los programas suelen escribir sus resultados normales en la salida estándar y los diagnósticos en un flujo independiente llamado error estándar o **stderr**. Mantener separados ambos flujos permite guardar datos útiles sin mezclarlos con mensajes de error.

## Separación de la salida normal y los errores

```bash
$ ls /fake/directory > peanuts.txt
ls: cannot access '/fake/directory': No such file or directory
```

El operador `>` solo redirige stdout. El diagnóstico se escribe en stderr, que sigue conectado a la terminal. Mientras tanto, la shell crea o trunca `peanuts.txt` para stdout aunque `ls` no produzca ningún resultado normal.

Los flujos estándar utilizan por convención estos descriptores de archivo:

- `0`: stdin (entrada estándar)
- `1`: stdout (salida estándar)
- `2`: stderr (error estándar)

:::single-choice{#stderr-not-in-stdout-file}
¿Por qué el error de `ls /missing > results.txt` permanece normalmente en la terminal?

::option[`>` redirige stdout, mientras que el diagnóstico se escribe en stderr.]{#stderr-separate-stream .correct explanation="Un `>` sencillo solo cambia el descriptor de archivo 1. El descriptor 2 conserva como destino la terminal."}
::option[`ls` espera a que se cierre el archivo antes de mostrar cualquier error.]{#stderr-waits-for-close explanation="El problema no es el momento de la escritura. Los mensajes normales y los diagnósticos utilizan flujos de salida distintos."}
::option[`results.txt` puede guardar texto normal, pero no diagnósticos.]{#stderr-file-capability explanation="Un archivo normal puede almacenar cualquiera de los dos flujos. La línea de órdenes simplemente no redirigió stderr hacia él."}
:::

## Redirección de stderr con 2>

Para redirigir `stderr` a un archivo, usas el descriptor de archivo `2` seguido del operador `>`. Este comando enviará cualquier mensaje de error al **archivo stderr** especificado.

```bash
$ ls /fake/directory 2> errors.txt
```

La shell crea o trunca `errors.txt` y lo conecta al descriptor 2. Stdout conserva su destino anterior. Utiliza `2>> errors.txt` cuando quieras añadir la salida de error.

:::single-choice{#stderr-to-error-file}
¿Qué orden sustituye `errors.log` con los diagnósticos de `find /restricted` y deja stdout en su destino actual?

::option[`find /restricted > errors.log`]{#stdout-errors-log explanation="Un `>` sencillo redirige el descriptor 1, por lo que captura resultados normales, no específicamente los diagnósticos."}
::option[`find /restricted < errors.log`]{#stdin-errors-log explanation="El operador menor que proporciona el archivo como stdin. No captura ninguno de los flujos de salida."}
::option[`find /restricted 2> errors.log`]{#stderr-errors-log .correct explanation="El `2` inicial selecciona stderr y `>` crea o trunca el destino de ese flujo."}
:::

## Combinación de stdout y stderr

¿Qué pasa si quieres capturar tanto la salida normal como los mensajes de error en el mismo archivo? Puedes lograr esto redirigiendo ambas secuencias.

```bash
$ ls /fake/directory /etc/passwd > combined.txt 2>&1
```

Analicemos esto:

1. `> combined.txt` redirige `stdout` (descriptor de archivo 1) al archivo `combined.txt`.
2. `2>&1` redirige `stderr` (descriptor de archivo 2) a la misma ubicación a la que apunta actualmente `stdout` (descriptor de archivo 1).

El orden es importante. `2>&1` envía `stderr` al destino actual de `stdout`. En este caso, `stdout` apunta a un archivo, por lo que `stderr` también se envía a ese archivo.

Invertir el orden cambia el resultado:

```bash
$ ls /fake/directory /etc/passwd 2>&1 > regular.txt
```

Aquí stderr duplica primero el destino original de stdout, la terminal. Después stdout se mueve a `regular.txt`, por lo que ambos flujos terminan en lugares diferentes.

:::single-choice{#stderr-combine-order}
¿Qué redirección de Bash envía stdout y stderr de `command` a `all.log`?

::option[`command 2>&1 > all.log`]{#stderr-before-stdout explanation="Esta orden conecta primero stderr con el destino anterior de stdout y después redirige únicamente stdout al archivo. Los flujos quedan separados."}
::option[`command 2> all.log > /dev/null`]{#stderr-file-stdout-null explanation="Esta orden envía stderr a `all.log`, pero descarta stdout. No combina ambos flujos en el archivo."}
::option[`command > all.log 2>&1`]{#stdout-then-stderr .correct explanation="Stdout se dirige primero al archivo y stderr duplica después ese destino actual de stdout."}
:::

Una forma más moderna y corta de redirigir tanto `stdout` como `stderr` es usando `&>`.

```bash
$ ls /fake/directory /etc/passwd &> combined.txt
```

Utiliza `&>>` para añadir ambos flujos en Bash. Conviene reconocer la forma explícita `> archivo 2>&1` porque también aparece en scripts y documentación.

:::single-choice{#stderr-bash-short-form}
¿Qué orden de Bash añade stdout y stderr de `build` a `build.log`?

::option[`build &> build.log`]{#replace-both-build explanation="En Bash, `&>` redirige ambos flujos, pero sustituye el archivo existente en vez de añadir contenido."}
::option[`build 2>> build.log`]{#append-errors-build explanation="Esta orden solo añade stderr. Stdout conserva su destino anterior."}
::option[`build &>> build.log`]{#append-both-build .correct explanation="En Bash, `&>>` añade los descriptores de archivo 1 y 2 al mismo destino."}
:::

## Descartar deliberadamente un flujo

A veces, es posible que desees ejecutar un comando e ignorar por completo cualquier mensaje de error potencial. Para hacer esto, puedes redirigir `stderr` a un archivo especial llamado `/dev/null`, que descarta cualquier dato escrito en él.

```bash
$ ls /fake/directory 2> /dev/null
```

Esto no hace que la orden tenga éxito ni cambia su estado de salida; solo oculta el flujo de diagnósticos. Durante la resolución de problemas, conserva o muestra stderr en vez de descartar la información que necesitas.

:::single-choice{#stderr-dev-null-effect}
¿Qué cambia `check-data 2> /dev/null`?

::option[Descarta stdout y convierte todos los errores en éxitos.]{#discard-stdout-success explanation="El descriptor 2 es stderr, no stdout, y la redirección no reescribe el estado de salida del programa."}
::option[Descarta stderr, pero no fuerza un estado de salida satisfactorio.]{#discard-stderr-only .correct explanation="La redirección cambia el destino de los diagnósticos. El propio programa sigue determinando si finaliza con éxito o con un fallo."}
::option[Guarda stderr en un archivo oculto llamado `/dev/null`.]{#save-dev-null explanation="`/dev/null` descarta los datos escritos; no es un archivo de almacenamiento que pueda recuperarse después."}
:::

Para practicar la gestión de los tres flujos estándar, prueba este laboratorio:

1. **[Redirección de Entrada y Salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - En este laboratorio, aprenderás a redirigir la entrada y la salida en el shell de Linux. Practicarás el control del flujo de datos desde los comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como >, >>, 2>, y el comando tee.

## Resumen

Ahora puedes mantener separados los diagnósticos o combinarlos con la salida normal de una orden.

1. Reconocer stderr como descriptor de archivo 2.
2. Sustituir o ampliar un registro de errores con `2>` o `2>>`.
3. Aplicar varias redirecciones de izquierda a derecha.
4. Combinar los dos flujos de salida con una sintaxis deliberada.
5. Descartar diagnósticos solo cuando resulte aceptable perderlos.
