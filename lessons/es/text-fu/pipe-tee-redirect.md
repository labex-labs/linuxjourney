---
lesson_id: "pipe-tee-redirect"
course_id: "text-fu"
lang: "es"
order_index: 4
title: "tubería y tee"
description: "Aprende cómo conectan órdenes las tuberías y cómo `tee` guarda un flujo mientras lo transmite."
meta_title: "tubería y tee - Text-Fu"
meta_description: "Explore el potente comando pipe y tee en Linux. Aprenda a encadenar comandos con la combinación pipe tee de Linux y redirigir la salida tanto a la pantalla como a un archivo. Esta guía cubre cómo usar pipe a tee para un flujo de datos avanzado en la línea de comandos."
meta_keywords: "comando pipe y tee en linux, pipe tee linux, pipe a tee, tubería linux, comando tee, stdout, stdin, redirección de línea de comandos, tutorial linux"
---

Las tuberías conectan órdenes pequeñas para que los datos fluyan entre ellas sin necesidad de un archivo intermedio. La orden `tee` puede copiar una parte de ese flujo en un archivo y continuar transmitiéndolo.

## Conexión de órdenes con |

Comencemos con un comando que produce mucha salida:

```bash
$ ls -la /etc
```

La lista de elementos es probablemente demasiado larga para caber en tu pantalla, lo que dificulta su lectura. Si bien podrías redirigir esta salida a un archivo, un método más eficiente es enviarla directamente a otro comando, como `less`, para una visualización fácil.

```bash
$ ls -la /etc | less
```

El operador de tubería `|` conecta stdout de la orden de la izquierda con stdin de la orden de la derecha. La shell inicia las órdenes de la tubería y prepara la conexión; pueden trabajar al mismo tiempo, de modo que `less` empiece a leer antes de que `ls` haya producido toda la lista.

:::single-choice{#pipe-stream-connection} En `ls -la /etc | less`, ¿qué flujos conecta `|` de forma predeterminada?

::option[Stdin de `ls` con stdout de `less`.]{#pipe-reversed-streams explanation="Esta opción invierte tanto el productor como el consumidor. Los datos fluyen desde la salida de la orden izquierda hacia la entrada de la derecha."}
::option[Stderr de `ls` con los dos flujos de `less`.]{#pipe-stderr-both explanation="Una tubería normal no conecta stderr de la orden izquierda ni apunta a los dos flujos de la orden derecha."}
::option[Stdout de `ls` con stdin de `less`.]{#pipe-stdout-stdin .correct explanation="Una tubería estándar conecta el descriptor de archivo 1 de la orden izquierda con el descriptor 0 de la derecha."}
:::

## Mantenimiento de stderr por separado

Una tubería normal solo transporta stdout. Stderr de la orden izquierda conserva su destino anterior, que suele ser la terminal:

```bash
$ find /etc -name "*.conf" | less
```

Las rutas coincidentes atraviesan la tubería, mientras que los diagnósticos de permisos pueden seguir apareciendo directamente en la terminal. Redirige stderr por separado si necesitas otro comportamiento:

```bash
$ find /etc -name "*.conf" 2> find-errors.log | less
```

:::single-choice{#pipe-left-stderr} En `find /etc -name "*.conf" | less`, ¿adónde va normalmente stderr de `find` si no hay otra redirección?

::option[A `less` por la misma tubería que stdout.]{#pipe-errors-to-less explanation="La tubería ordinaria solo conecta stdout. Stderr no se combina automáticamente con él."}
::option[A un archivo llamado `stderr` en el directorio actual.]{#pipe-errors-to-file explanation="No existe ninguna redirección a un archivo de errores, por lo que la shell no crea tal archivo."}
::option[A su destino actual, normalmente la terminal.]{#pipe-errors-terminal .correct explanation="Como el descriptor 2 no cambia, los diagnósticos suelen seguir conectados a la terminal."}
:::

## Copia de un flujo con tee

¿Qué pasa si quieres ver la salida en tu pantalla _y_ guardarla en un archivo simultáneamente? Aquí es donde entra en juego el comando `tee`. El `comando pipe and tee en linux` es una combinación clásica para registrar y monitorear.

```bash
$ ls | tee listing.txt
```

`tee` lee stdin, escribe una copia en cada archivo indicado y también envía los mismos datos a stdout. De forma predeterminada, crea o trunca el archivo, igual que `>`.

:::single-choice{#tee-display-and-save} ¿Qué orden muestra la salida de `generate-report` y también sustituye `report.txt` por esa misma salida?

::option[`generate-report > report.txt`]{#redirect-report-only explanation="Una redirección de salida sencilla escribe el archivo, pero no conserva una copia del flujo hacia la terminal."}
::option[`generate-report | tee report.txt`]{#tee-report .correct explanation="`tee` copia stdin en `report.txt` y en su stdout, que en esta tubería sigue conectado a la terminal."}
::option[`tee generate-report | report.txt`]{#tee-operands-reversed explanation="Esta orden trata `generate-report` como archivo de destino e intenta ejecutar `report.txt` como orden. El productor debe estar a la izquierda."}
:::

Utiliza `-a` para añadir contenido en vez de sustituir el archivo:

```bash
$ date | tee -a activity.log
```

:::single-choice{#tee-append-log} ¿Qué orden muestra la fecha actual y la añade a `activity.log`?

::option[`date | tee -a activity.log`]{#tee-append-activity .correct explanation="La opción `-a` hace que `tee` añada datos al archivo mientras continúa copiando la entrada a stdout."}
::option[`date | tee activity.log`]{#tee-replace-activity explanation="Sin `-a`, `tee` sustituye el archivo existente en vez de conservar sus entradas anteriores."}
::option[`date > activity.log`]{#redirect-replace-activity explanation="Esta orden sustituye el archivo y no envía ninguna copia a la terminal. No cumple ni el requisito de añadir ni el de mostrar."}
:::

## Conservación de un resultado intermedio

Puedes crear flujos de trabajo aún más avanzados encadenando estos comandos. Un patrón común es usar `pipe to tee` en medio de una cadena de comandos más larga. Esto te permite guardar un resultado intermedio mientras continúas procesando los datos.

Por ejemplo, puedes usar la combinación `linux pipe tee` para ver y guardar la salida antes de un filtrado adicional:

```bash
$ ls -la /etc | tee etc-listing.txt | grep "conf"
```

Este comando hace tres cosas:

1. Lista el contenido del directorio `/etc`.
2. Envía esa salida por tubería a `tee`, que guarda una copia en `etc-listing.txt` y también la pasa adelante.
3. La salida de `tee` se envía luego por tubería a `grep`, que filtra las líneas que contienen "conf".

El archivo contiene los datos anteriores al filtrado de `grep`. Si quieres guardar únicamente las líneas filtradas, coloca `tee` después de `grep`.

:::single-choice{#tee-before-filter-result} ¿Qué contiene `all.txt` cuando `produce | tee all.txt | grep error` termina correctamente?

::option[Únicamente las líneas que coinciden con `grep`.]{#tee-filtered-only explanation="`tee` se ejecuta antes que `grep`, por lo que escribe la entrada sin filtrar, no el conjunto de coincidencias posterior."}
::option[Únicamente stderr de `produce`.]{#tee-producer-stderr explanation="Una tubería normal transporta stdout de `produce`. Stderr no constituye la entrada de `tee`."}
::option[Toda la salida estándar producida antes del filtrado.]{#tee-complete-intermediate .correct explanation="`tee` guarda cada byte que recibe y después transmite ese mismo flujo a `grep` para filtrarlo."}
:::

Para practicar las tuberías y la copia de flujos, prueba estos laboratorios:

1. **[Redirección de Entrada y Salida en Linux](https://labex.io/es/labs/comptia-redirecting-input-and-output-in-linux-590840)** - Practica el control del flujo de datos desde comandos manipulando la salida estándar (stdout), el error estándar (stderr) y la entrada estándar (stdin) usando operadores como `>`, `>>`, `2>` y el comando `tee`.
2. **[Control de Secuencia y Tubería en Linux](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Aprende a controlar las secuencias de ejecución de comandos, utilizar tuberías (pipelines) y aprovechar herramientas potentes de procesamiento de texto como `cut`, `grep`, `wc`, `sort` y `uniq`.
3. **[Redirección de Flujo de Datos](https://labex.io/es/labs/linux-data-stream-redirection-17995)** - Aprende el arte de la redirección de flujos en Linux, incluida la manipulación de flujos de entrada, salida y error estándar, la combinación de salidas y el uso de `/dev/null`.

## Resumen

Ahora puedes conectar órdenes y conservar puntos concretos de un flujo de datos.

1. Canalizar stdout de una orden hacia stdin de otra.
2. Redirigir stderr por separado cuando sea necesario.
3. Copiar la entrada en un archivo y en stdout con `tee`.
4. Añadir contenido con `tee -a` en vez de sustituir un archivo.
5. Colocar deliberadamente `tee` antes o después de un filtro.
