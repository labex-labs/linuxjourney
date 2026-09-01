---
lesson_id: "join-split-command"
course_id: "text-fu"
lang: "es"
order_index: 11
title: "join y split"
description: "Aprende a unir dos archivos de texto ordenados mediante una clave y a dividir un archivo en fragmentos con nombre."
meta_title: "join y split - Text-Fu"
meta_description: "Domina el uso de las órdenes join y split de Linux. Aprende a unir archivos mediante campos comunes y a dividir archivos grandes en partes más pequeñas."
meta_keywords: "unir archivos Linux, orden join Linux, orden split Linux, manipulación de archivos, línea de órdenes, procesamiento de texto"
---

Las órdenes `join` y `split` resuelven problemas distintos de procesamiento de archivos. `join` combina registros relacionados de dos entradas de texto ordenadas, mientras que `split` divide una entrada en una secuencia de archivos más pequeños.

## Unir dos archivos por su primer campo

De forma predeterminada, `join` compara el primer campo separado por espacios en blanco de exactamente dos archivos de entrada. Considera estos archivos ya ordenados:

`people.txt`:

```text
1 John
2 Jane
3 Mary
```

`surnames.txt`:

```text
1 Doe
2 Doe
3 Sue
```

Une los registros cuyos campos clave sean iguales:

```bash
$ join people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

La salida contiene una vez la clave compartida, seguida de los campos restantes del primer y del segundo archivo. `join` procesa dos archivos a la vez; no acepta tres operandos de archivo normales como una unión relacional de tres vías.

:::single-choice{#join-default-key} Sin opciones de campo, ¿qué registros combina `join first.txt second.txt`?

::option[Las líneas cuyos primeros campos separados por espacios en blanco son iguales.]{#join-first-fields .correct explanation="El comportamiento predeterminado de `join` compara el campo 1 de cada una de las dos entradas ordenadas."}
::option[Las líneas que ocupan el mismo número de línea físico.]{#join-line-numbers explanation="La coincidencia se basa en los valores de los campos clave, no simplemente en la posición de los registros."}
::option[Cada línea del primer archivo con cada línea del segundo.]{#join-all-pairs explanation="`join` emite registros para claves coincidentes, no un producto cartesiano sin restricciones de todas las líneas."}
:::

## Ordenar las claves de unión

Cada entrada debe estar ordenada por su campo de unión con reglas de comparación compatibles. Para el campo 1 predeterminado, prepara copias con `sort -k 1,1`:

```bash
$ LC_ALL=C sort -k 1,1 people-raw.txt > people.txt
$ LC_ALL=C sort -k 1,1 surnames-raw.txt > surnames.txt
$ LC_ALL=C join people.txt surnames.txt
```

Usar la misma configuración regional para ordenar y unir mantiene uniformes las reglas de intercalación. No redirijas una ordenación a la misma ruta de su entrada, porque el shell truncaría primero ese archivo.

:::single-choice{#join-sort-requirement} ¿Qué preparación suele requerir `join` para producir coincidencias fiables?

::option[Ambos archivos deben contener exactamente la misma cantidad de líneas físicas.]{#join-equal-line-count explanation="Las longitudes de entrada pueden diferir. Las coincidencias de claves, no la igualdad del número de líneas, determinan la salida unida."}
::option[Ambos archivos deben tener nombres que queden juntos al ordenarlos alfabéticamente.]{#join-filename-order explanation="Es necesario ordenar las claves del contenido; la relación léxica entre los nombres de archivo no importa."}
::option[Ambos archivos deben estar ordenados por sus respectivos campos de unión con un orden compatible.]{#join-sorted-keys .correct explanation="`join` avanza por claves ordenadas, por lo que cada entrada debe usar un orden coherente con la comparación que realiza."}
:::

## Seleccionar campos de unión diferentes

Usa `-1 FIELD` para la clave del primer archivo y `-2 FIELD` para la del segundo. Supón que la primera entrada contiene:

```text
John 1
Jane 2
Mary 3
```

La segunda contiene:

```text
1 Doe
2 Doe
3 Sue
```

Después de ordenar el primer archivo por el campo 2 y el segundo por el campo 1, ejecuta:

```bash
$ join -1 2 -2 1 people.txt surnames.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

Usa `-t CHARACTER` cuando un único carácter que no sea un espacio en blanco, como `:`, separe los campos. Opciones como `-a 1` o `-a 2` pueden incluir líneas sin pareja de una entrada; la salida predeterminada solo contiene claves coincidentes.

:::single-choice{#join-different-fields} ¿Qué opciones unen el campo 2 del primer archivo con el campo 1 del segundo?

::option[`-1 1 -2 2`]{#join-fields-reversed explanation="Esto selecciona el campo 1 de la primera entrada y el campo 2 de la segunda, lo contrario de la correspondencia solicitada."}
::option[`-1 2 -2 1`]{#join-fields-two-one .correct explanation="`-1 2` elige el campo 2 del primer archivo y `-2 1` elige el campo 1 del segundo."}
::option[`-f 2 -d 1`]{#join-cut-style-options explanation="Se parecen a opciones de campo y delimitador de otras herramientas de texto. No son los selectores de campo de `join`."}
:::

## Dividir por cantidad de líneas

`split` escribe porciones consecutivas de una entrada en archivos de salida separados. No es la operación inversa de una unión basada en claves.

```bash
$ split large.txt
```

El comportamiento predeterminado de GNU escribe hasta 1000 líneas por archivo de salida y usa el prefijo `x`, lo que produce nombres como `xaa`, `xab` y `xac`.

Usa `-l NUMBER` para elegir una cantidad de líneas y añade un último operando para elegir el prefijo de salida:

```bash
$ split -l 500 large.txt part-
```

Esto produce `part-aa`, `part-ab` y así sucesivamente, con un máximo de 500 líneas en cada fragmento.

:::single-choice{#split-lines-with-prefix} ¿Qué orden divide `large.txt` en fragmentos de un máximo de 500 líneas cuyos nombres comienzan por `part-`?

::option[`split -b 500 large.txt part-`]{#split-five-hundred-bytes explanation="La opción `-b` selecciona bytes, por lo que en un texto normal estos fragmentos serían mucho menores que 500 líneas."}
::option[`split -l 500 large.txt part-`]{#split-five-hundred-lines .correct explanation="`-l 500` establece la cantidad máxima de líneas y el último operando proporciona el prefijo del nombre de salida."}
::option[`join -l 500 large.txt part-`]{#join-split-lines explanation="`join` combina registros con claves de dos archivos. No divide una entrada en fragmentos."}
:::

## Dividir por tamaño

Usa `-b SIZE` para dividir la entrada por tamaño en bytes. En este contexto, los sufijos de GNU como `K`, `M` y `G` representan potencias de 1024:

```bash
$ split -b 10M archive.bin chunk-
```

Esto solicita fragmentos de 10 mebibytes, salvo un posible fragmento final más pequeño. `split` no crea un manifiesto del archivo ni metadatos de reconstrucción; conserva el orden de los sufijos y concatena los fragmentos en orden cuando corresponda reconstruirlo.

:::single-choice{#split-ten-mebibytes} ¿Qué orden divide `archive.bin` en fragmentos de 10 MiB con el prefijo `chunk-`?

::option[`split -l 10M archive.bin chunk-`]{#split-lines-ten-m explanation="La opción `-l` espera una cantidad de líneas, no un sufijo de tamaño en bytes para fragmentos binarios."}
::option[`join -b 10M archive.bin chunk-`]{#join-bytes explanation="`join` no divide entradas binarias ni admite esta operación de tamaño de fragmento."}
::option[`split -b 10M archive.bin chunk-`]{#split-ten-mib .correct explanation="La opción `-b` selecciona el tamaño del fragmento, `10M` solicita 10×1024×1024 bytes y `chunk-` es el prefijo de salida."}
:::

Para practicar uniones mediante claves y el procesamiento de datos estructurados, prueba estos laboratorios prácticos:

1. **[Orden join de Linux: unión de archivos](https://labex.io/labs/linux-linux-join-command-file-joining-219193)** - Este laboratorio ofrece una introducción práctica directa a `join`, para que practiques la combinación de líneas de dos archivos de texto ordenados mediante un campo común, tal como se explica en la lección.
2. **[Procesamiento de datos de empleados](https://labex.io/labs/linux-processing-employees-data-388132)** - Aplica tus conocimientos de `join` y otras potentes utilidades de la línea de órdenes de Linux, como `awk`, para combinar y procesar datos de varias fuentes en un caso de análisis de datos realista.

## Resumen

Ahora puedes combinar registros ordenados o dividir una entrada en fragmentos ordenados.

1. Une exactamente dos archivos mediante campos clave iguales.
2. Ordena ambas entradas de forma coherente por sus claves de unión.
3. Selecciona campos clave no predeterminados con `-1` y `-2`.
4. Divide por cantidad de líneas con `-l`.
5. Divide por tamaño en bytes con `-b` y un prefijo claro.
