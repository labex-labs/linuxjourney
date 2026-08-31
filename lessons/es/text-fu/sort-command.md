---
lesson_id: "sort-command"
course_id: "text-fu"
lang: "es"
order_index: 12
title: "sort"
description: "Aprende a ordenar líneas de texto por valores léxicos, numéricos o de campos seleccionados con sort."
meta_title: "sort - Text-Fu"
meta_description: "Aprende a usar la orden sort de Linux para ordenar archivos de texto. Descubre opciones como la ordenación inversa y numérica y mejora tus habilidades en la línea de órdenes."
meta_keywords: "orden sort Linux, sort -r, sort -n, tutorial Linux, línea de órdenes, Linux para principiantes, guía de sort"
---

La orden `sort` lee líneas completas, las ordena según las reglas de comparación seleccionadas y escribe el resultado en la salida estándar. No modifica un archivo de entrada salvo que elijas explícitamente una operación de salida.

## Ordenar líneas completas

Considera `animals.txt`:

```text
dog
cow
cat
elephant
bird
```

Ordena las líneas en orden ascendente:

```bash
$ sort animals.txt
bird
cat
cow
dog
elephant
```

La ordenación de texto sigue la configuración regional actual, que puede afectar a mayúsculas, acentos y signos de puntuación. Usa una configuración uniforme como `LC_ALL=C` cuando un script requiera una intercalación reproducible basada en bytes:

```bash
$ LC_ALL=C sort animals.txt
```

:::single-choice{#sort-lines-ascending}
¿Qué hace `sort animals.txt` sin una opción de clave o numérica?

::option[Ordena líneas de entrada completas según la configuración regional actual.]{#sort-locale-lines .correct explanation="De forma predeterminada, `sort` compara líneas completas mediante las reglas de intercalación de la configuración regional activa."}
::option[Ordena las palabras dentro de cada línea, pero mantiene fijo el orden de las líneas.]{#sort-words-within-lines explanation="`sort` trata cada línea como un registro. No reorganiza las palabras dentro de una línea."}
::option[Reescribe automáticamente `animals.txt` en el mismo archivo.]{#sort-auto-rewrite explanation="El resultado ordenado se envía de forma predeterminada a la salida estándar y el archivo de entrada no cambia."}
:::

## Invertir el resultado

Añade `-r` para invertir el resultado de la comparación:

```bash
$ sort -r animals.txt
elephant
dog
cow
cat
bird
```

:::single-choice{#sort-reverse-order}
¿Qué orden clasifica `animals.txt` en orden inverso?

::option[`sort -n animals.txt`]{#sort-numeric-animals explanation="La opción `-n` solicita una comparación numérica. No significa orden inverso."}
::option[`sort -u animals.txt`]{#sort-unique-animals explanation="La opción `-u` suprime claves duplicadas. No invierte la salida."}
::option[`sort -r animals.txt`]{#sort-reverse-animals .correct explanation="La opción `-r` invierte el orden elegido por las demás reglas de comparación."}
:::

## Comparar números

El orden léxico compara caracteres, por lo que `10` suele aparecer antes que `2`. Usa `-n` para una comparación numérica normal:

```bash
$ printf '10\n2\n30\n' | sort -n
2
10
30
```

Combina opciones cuando sea necesario. `sort -nr scores.txt` compara numéricamente y coloca primero los valores mayores.

:::single-choice{#sort-numbers-descending}
¿Qué orden clasifica las líneas numéricas de `scores.txt` de mayor a menor?

::option[`sort -n scores.txt`]{#sort-numeric-ascending explanation="Se selecciona la comparación numérica, pero la dirección predeterminada coloca primero los valores menores."}
::option[`sort -nr scores.txt`]{#sort-numeric-reverse .correct explanation="`-n` selecciona la comparación numérica y `-r` la invierte, lo que produce un orden numérico descendente."}
::option[`sort -r scores.txt`]{#sort-lexical-reverse explanation="Esto invierte la intercalación textual, pero no solicita una comparación numérica, por lo que valores como `10` y `2` pueden ordenarse de forma inesperada."}
:::

## Ordenar por un campo

Usa `-k START[,END]` para elegir una clave. De forma predeterminada, los campos se separan mediante secuencias de espacios en blanco. Para registros separados por dos puntos, usa `-t ':'`:

```bash
$ printf 'alice:30\nbob:8\ncarol:20\n' | sort -t ':' -k 2,2n
bob:8
carol:20
alice:30
```

Aquí, `-t ':'` selecciona el delimitador, `-k 2,2` limita la clave al campo 2 y la `n` adjunta compara esa clave numéricamente. Sin el `,2` final, una clave que comienza en el campo 2 suele continuar hasta el final de la línea.

:::single-choice{#sort-second-colon-field}
¿Qué orden clasifica `users.txt` numéricamente solo por su segundo campo separado por dos puntos?

::option[`sort -n -k 1,1 users.txt`]{#sort-first-blank-field explanation="Esto usa campos separados por espacios en blanco y selecciona el campo 1, no el segundo campo separado por dos puntos."}
::option[`cut -d ':' -f 2 users.txt`]{#cut-second-user-field explanation="`cut` extrae el campo 2, pero no ordena los registros originales por esa clave."}
::option[`sort -t ':' -k 2,2n users.txt`]{#sort-colon-field-two .correct explanation="Los dos puntos establecen los límites de los campos, `2,2` restringe la clave al campo 2 y `n` aplica una comparación numérica a esa clave."}
:::

## Eliminar duplicados y guardar la salida

Usa `-u` para generar una línea por cada clave de comparación igual:

```bash
$ sort -u names.txt
```

Esto ordena y elimina duplicados según las reglas de comparación seleccionadas. Si solo quieres eliminar duplicados adyacentes de datos ya ordenados, la orden `uniq`, que se explica más adelante, puede hacerlo.

Para escribir el resultado en un archivo, una redirección normal sirve cuando el destino difiere de la entrada:

```bash
$ sort names.txt > names-sorted.txt
```

No ejecutes `sort names.txt > names.txt`; el shell trunca la entrada antes de que `sort` la lea. En GNU, `sort -o names.txt names.txt` gestiona su propia salida de forma segura cuando quieres usar deliberadamente la misma ruta:

```bash
$ sort -o names.txt names.txt
```

Conserva una copia de seguridad o escribe y comprueba un resultado separado cuando los datos originales sean importantes.

:::single-choice{#sort-safe-same-file}
En GNU/Linux, ¿qué orden pide a `sort` que escriba de forma segura el resultado ordenado en `names.txt` sin que una redirección del shell lo trunque primero?

::option[`sort -o names.txt names.txt`]{#sort-output-same-file .correct explanation="`sort` de GNU gestiona la salida de `-o` después de leer según sea necesario, por lo que el shell no trunca previamente la entrada mediante `>`."}
::option[`sort names.txt > names.txt`]{#sort-redirection-same-file explanation="El shell trunca `names.txt` antes de iniciar `sort`, por lo que la orden puede perder la entrada."}
::option[`sort -u names.txt`]{#sort-unique-stdout explanation="Esto escribe líneas únicas y ordenadas en la salida estándar y no modifica el archivo de entrada."}
:::

Para practicar la ordenación y el análisis de datos orientados a líneas, prueba estos laboratorios prácticos:

1. **[Orden sort de Linux: ordenación de texto](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** - Este laboratorio ofrece una introducción directa a `sort` para practicar distintas formas de ordenar líneas de archivos de texto, incluidos los órdenes ascendente y descendente.
2. **[Recuento de palabras y ordenación](https://labex.io/labs/linux-word-count-and-sorting-388125)** - En este desafío aplicarás tus conocimientos de ordenación junto con el recuento de palabras para analizar datos de texto, encontrar patrones frecuentes y ordenar datos de manera eficiente.

## Resumen

Ahora puedes elegir reglas de comparación y destinos para el texto ordenado.

1. Ordena líneas completas con una configuración regional explícita cuando la reproducibilidad sea importante.
2. Invierte los resultados con `-r`.
3. Compara valores numéricos con `-n`.
4. Selecciona una clave de campo acotada con `-t` y `-k`.
5. Elimina duplicados o guarda la salida sin truncar la entrada.
