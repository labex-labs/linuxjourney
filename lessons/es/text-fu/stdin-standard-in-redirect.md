---
lesson_id: "stdin-standard-in-redirect"
course_id: "text-fu"
lang: "es"
order_index: 2
title: "stdin (Entrada estándar)"
description: "Aprende cómo leen los programas la entrada estándar y cómo conecta Bash ese flujo con un archivo."
meta_title: "stdin (Entrada Estándar) - Text-Fu"
meta_description: "Aprende sobre la redirección de stdin (entrada estándar) en Linux. Comprende cómo usar el operador '<' con archivos y comandos. Explora ejemplos prácticos y mejora tus habilidades de línea de comandos de Linux."
meta_keywords: "stdin, entrada estándar, redirección Linux, operador <, tutorial Linux, línea de comandos, principiante, guía"
---

La entrada estándar, abreviada **stdin**, es el flujo que un programa lee normalmente para recibir datos. En una terminal interactiva, la shell suele conectar stdin con la entrada de la terminal para que un programa pueda leer lo que escribes.

## La entrada estándar y el descriptor de archivo 0

Por convención, los tres flujos estándar utilizan estos números de descriptor de archivo:

- `0`: entrada estándar (`stdin`)
- `1`: salida estándar (`stdout`)
- `2`: error estándar (`stderr`)

Un programa puede decidir si utiliza estos flujos y de qué manera. Una orden diseñada para leer stdin suele esperar la entrada de la terminal cuando no se le proporciona un archivo ni otra fuente de entrada.

:::single-choice{#stdin-descriptor-number} ¿Qué descriptor de archivo representa por convención la entrada estándar?

::option[`0`]{#stdin-fd-zero .correct explanation="La entrada estándar corresponde por convención al descriptor de archivo 0."}
::option[`1`]{#stdin-fd-one explanation="El descriptor de archivo 1 representa por convención la salida estándar, es decir, el flujo de los resultados habituales."}
::option[`2`]{#stdin-fd-two explanation="El descriptor de archivo 2 representa por convención el error estándar, no la entrada estándar."}
:::

## Redirección de un archivo hacia stdin

El operador `<` indica a Bash que abra un archivo para leerlo y lo conecte a stdin de la orden:

```bash
$ cat < peanuts.txt
Hello World
```

La shell se encarga de `< peanuts.txt`; `cat` se limita a leer el descriptor de archivo 0. La ruta no se pasa a `cat` como un operando de archivo normal.

Si el archivo de entrada no existe o no puede abrirse, la shell informa del error de redirección y no inicia la orden con esa entrada.

:::single-choice{#stdin-from-file} ¿Qué orden hace que `sort` lea su entrada estándar desde `names.txt`?

::option[`sort < names.txt`]{#sort-stdin-file .correct explanation="Bash abre `names.txt` para lectura y lo conecta con `sort` mediante el descriptor de archivo 0."}
::option[`sort > names.txt`]{#stdout-to-names explanation="El operador mayor que redirige stdout al archivo y puede truncarlo. No proporciona el archivo como entrada."}
::option[`sort names.txt >`]{#incomplete-sort-output explanation="Esta orden incluye una redirección de salida incompleta. No expresa la conexión de stdin solicitada."}
:::

## Operando de archivo frente a redirección de entrada

Algunas órdenes aceptan tanto un nombre de archivo como stdin, pero los resultados pueden diferir ligeramente. Por ejemplo:

```bash
$ wc -l peanuts.txt
1 peanuts.txt
$ wc -l < peanuts.txt
1
```

Las dos formas cuentan líneas en los mismos datos. En la primera, `wc` conoce el nombre porque lo recibe como argumento. En la segunda solo recibe un flujo mediante stdin, por lo que no dispone de ningún nombre de archivo que mostrar.

:::single-choice{#stdin-not-command-argument} ¿Por qué `wc -l < peanuts.txt` omite normalmente `peanuts.txt` en la salida?

::option[`wc` elimina el nombre del archivo después de contar las líneas.]{#stdin-delete-name explanation="La orden no cambia el nombre ni elimina el archivo de origen. Solo cambia su conexión de entrada."}
::option[El operador `<` oculta todas las palabras que imprime la orden.]{#stdin-hide-words explanation="La redirección de entrada no filtra stdout. El nombre falta porque `wc` nunca lo recibió como argumento."}
::option[Bash proporciona el archivo mediante stdin en vez de como argumento de nombre.]{#stdin-no-filename .correct explanation="La shell consume la redirección y conecta el archivo al descriptor 0, por lo que `wc` no recibe la ruta como operando."}
:::

## Combinación de redirecciones de entrada y salida

Una misma línea puede redirigir más de un flujo:

```bash
$ cat < peanuts.txt > banana.txt
```

La shell realiza dos conexiones independientes:

1. `< peanuts.txt` abre `peanuts.txt` como stdin de `cat`.
2. `> banana.txt` crea o trunca `banana.txt` y lo conecta con stdout de `cat`.

`cat` lee bytes de stdin y los escribe en stdout, por lo que `banana.txt` recibe el contenido del origen. Para copiar un archivo de forma ordinaria, `cp peanuts.txt banana.txt` expresa más directamente la intención; este ejemplo trata sobre las conexiones entre flujos.

:::single-choice{#stdin-and-stdout-files} En `cat < input.txt > output.txt`, ¿qué archivo proporciona stdin y cuál recibe stdout?

::option[`output.txt` proporciona stdin; `input.txt` recibe stdout.]{#stdin-output-stdout-input explanation="Esta opción invierte el significado de los operadores. Las flechas apuntan hacia la orden en la entrada y hacia el archivo en la salida."}
::option[`input.txt` proporciona stdin; `output.txt` recibe stdout.]{#stdin-input-stdout-output .correct explanation="La redirección `<` abre `input.txt` para el descriptor 0 y `>` abre `output.txt` para el descriptor 1."}
::option[Ambos archivos proporcionan stdin y stdout permanece en la terminal.]{#both-stdin explanation="Los dos operadores afectan a flujos estándar diferentes. `>` redirige stdout fuera de la terminal."}
:::

Para practicar la redirección de entrada y salida, prueba estos laboratorios:

1. **[Redirección de entrada y salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practica el control del flujo de datos manipulando stdout, stderr y stdin mediante operadores como `>`, `>>`, `2>` y la orden `tee`.
2. **[Redirección de flujos de datos](https://labex.io/es/labs/linux-data-stream-redirection-17995)** - Manipula los flujos estándar, combina salidas y utiliza `/dev/null` en operaciones más avanzadas.

## Resumen

Ahora puedes conectar mediante la shell la entrada estándar de una orden con un archivo.

1. Reconocer stdin como descriptor de archivo 0.
2. Redirigir un archivo legible con `<`.
3. Distinguir un operando de nombre de archivo de una entrada redirigida.
4. Combinar deliberadamente redirecciones de stdin y stdout.
