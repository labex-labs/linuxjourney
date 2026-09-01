---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "es"
order_index: 1
title: "stdout (Salida estándar)"
description: "Aprende cómo fluye la salida estándar hacia la terminal y cómo Bash la redirige a archivos."
meta_title: "stdout (Salida Estándar) - Text-Fu"
meta_description: "Comienza tu viaje para aprender Linux dominando la salida estándar (stdout) y la redirección de E/S. Esta lección cubre cómo redirigir la salida de comandos a archivos usando los operadores > y >>, una habilidad fundamental para cualquier usuario de Linux."
meta_keywords: "Linux, aprender linux, stdout, redirección E/S, salida estándar, redirigir salida, bash, scripting shell, comandos Linux, tutorial Linux"
---

Los programas se comunican mediante flujos de entrada y salida. La salida estándar, abreviada **stdout**, es el flujo que un programa utiliza normalmente para sus resultados habituales. En una terminal, la shell conecta inicialmente este flujo con la pantalla.

## Escritura en la salida estándar

La orden `echo` escribe sus argumentos en stdout:

```bash
$ echo Hello World
Hello World
```

Stdout es el descriptor de archivo `1`, un número que resulta útil al redirigir más de un flujo. Los programas también pueden disponer de entrada estándar o stdin y de error estándar o stderr; las próximas lecciones examinan esos flujos.

:::single-choice{#stdout-default-destination} Sin redirección, ¿adónde envía normalmente `echo Hello World` su salida habitual en una terminal interactiva?

::option[A un archivo llamado `stdout` en el directorio actual.]{#stdout-file explanation="La salida estándar es un flujo, no un archivo llamado `stdout` que se cree automáticamente. Solo se utiliza un archivo si rediriges la salida hacia él."}
::option[A la terminal a través de la salida estándar.]{#stdout-terminal .correct explanation="La shell suele conectar la salida estándar de una orden con la terminal, por lo que allí aparece el resultado de `echo`."}
::option[Al flujo de entrada estándar de la orden.]{#stdout-to-stdin explanation="La entrada estándar transporta datos hacia un programa. `echo` envía su resultado habitual hacia fuera mediante stdout."}
:::

## Sustitución de un archivo con >

Bash interpreta `>` como un operador de redirección de salida. Abre el archivo de destino y conecta con él la salida estándar de la orden:

```bash
$ echo Hello World > peanuts.txt
```

El texto deja de aparecer en la terminal porque stdout se dirige a `peanuts.txt`. Si el archivo no existe, la shell lo crea. Si ya existe, lo trunca antes de que la orden escriba, por lo que se pierde el contenido anterior.

Utiliza `cat` para inspeccionar el resultado:

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file} `notes.txt` ya contiene texto. ¿Qué hace `echo new > notes.txt`?

::option[Sustituye el contenido del archivo por `new`.]{#stdout-replace-existing .correct explanation="La shell trunca el destino existente al usar `>` y dirige la salida de `echo` al archivo ya vacío."}
::option[Añade `new` después del texto existente.]{#stdout-add-existing explanation="Para añadir contenido se necesita `>>`. Un solo `>` no conserva el contenido anterior del destino."}
::option[Muestra `new` sin modificar el archivo.]{#stdout-display-only explanation="La redirección envía stdout a `notes.txt`, por lo que la salida normal no permanece en la terminal."}
:::

Como la shell abre el destino antes de ejecutar la orden, comprueba la ruta antes de pulsar Enter. Un archivo existente mal escrito o no deseado puede quedar truncado aunque la orden falle después.

## Adición a un archivo con >>

Utiliza `>>` cuando quieras añadir la nueva salida estándar después del contenido existente de un archivo:

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

Al igual que `>`, `>>` crea el destino si no existe. La diferencia está en cómo abre un archivo existente: `>>` añade contenido en vez de truncarlo.

:::single-choice{#stdout-append-file} ¿Qué orden añade `Finished` al final de `status.log` sin borrar su contenido actual?

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="Un solo `>` trunca el destino existente antes de escribir. Borraría el contenido anterior del registro."}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`echo` produce el texto y `>>` añade esa salida estándar al archivo de destino."}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="Esta orden pide a `cat` que lea un archivo llamado `Finished`. No produce el texto solicitado como salida estándar."}
:::

## La redirección pertenece a la shell

La shell reconoce `>` y `>>`, elimina estos operadores de los argumentos que se pasan al programa, abre el archivo y prepara la conexión del flujo. La orden se limita a escribir en stdout como siempre.

Por ello, la misma sintaxis de redirección funciona con muchas órdenes:

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role} ¿Quién interpreta normalmente `>` en `pwd > current-directory.txt`?

::option[La orden `pwd` después de recibir `>` como argumento.]{#stdout-pwd-redirection explanation="La shell consume la sintaxis de redirección, por lo que normalmente `pwd` no recibe `>` ni el destino como argumentos ordinarios."}
::option[La shell Bash antes de iniciar `pwd`.]{#stdout-bash-redirection .correct explanation="Bash abre el destino y conecta el descriptor de archivo 1 antes de ejecutar la orden."}
::option[La terminal después de que `pwd` muestre la ruta en pantalla.]{#stdout-terminal-redirection explanation="El flujo se redirige antes de escribir la salida, por lo que la terminal nunca recibe esa salida estándar."}
:::

Para practicar la redirección de flujos estándar, prueba este laboratorio:

1. **[Redirección de entrada y salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practica el control del flujo de datos de las órdenes manipulando stdout, stderr y stdin mediante operadores como `>`, `>>`, `2>` y la orden `tee`.

## Resumen

Ahora puedes redirigir la salida estándar de una orden sin confundir la sustitución con la adición de contenido.

1. Reconocer stdout como el flujo de los resultados habituales de una orden.
2. Sustituir el contenido de un archivo con `>`.
3. Conservar el contenido existente y añadir datos con `>>`.
4. Comprobar un destino antes de que la shell lo abra.
