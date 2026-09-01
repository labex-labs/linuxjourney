---
lesson_id: "uniq-unique-command"
course_id: "text-fu"
lang: "es"
order_index: 14
title: "uniq (único)"
description: "Aprende a agrupar, contar o filtrar grupos adyacentes de líneas iguales con uniq."
meta_title: "uniq (único) - Text-Fu"
meta_description: "Explora la orden uniq de Linux para filtrar líneas duplicadas adyacentes. Aprende a usar opciones como -c, -u y -d, y a combinar uniq con sort."
meta_keywords: "orden uniq, uniq Linux, eliminar duplicados, sort uniq, procesamiento de texto, limpieza de datos, tutorial Linux"
---

La orden `uniq` compara cada línea de entrada con la línea anterior. Puede agrupar, contar o seleccionar grupos de líneas iguales adyacentes, pero no busca duplicados separados por todo el archivo.

## Agrupar líneas duplicadas adyacentes

Supón que `reading.txt` contiene valores agrupados:

```plaintext
book
book
paper
paper
article
article
magazine
```

Ejecuta `uniq` sin opciones de filtrado para imprimir una línea representativa de cada grupo adyacente:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

El archivo de entrada no cambia porque el resultado se envía a la salida estándar.

:::single-choice{#uniq-collapse-adjacent} ¿Qué hace `uniq reading.txt` de forma predeterminada?

::option[Ordena el archivo completo y después elimina todos los valores repetidos.]{#uniq-auto-sort explanation="`uniq` conserva el orden de entrada y no ordena. Las copias separadas siguen siendo grupos diferentes."}
::option[Imprime una línea de cada grupo adyacente de líneas iguales.]{#uniq-one-per-group .correct explanation="De forma predeterminada, `uniq` reduce cada secuencia de líneas iguales consecutivas a una línea de salida."}
::option[Elimina las líneas duplicadas directamente de `reading.txt`.]{#uniq-edit-file explanation="La orden escribe el texto filtrado en la salida estándar de forma predeterminada y no edita el archivo de entrada."}
:::

## Contar grupos adyacentes

Usa `-c` para anteponer a cada grupo de salida su cantidad de líneas de entrada consecutivas:

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Estas cantidades representan longitudes de secuencias, no totales globales, salvo que antes se hayan colocado juntas todas las líneas iguales.

:::single-choice{#uniq-count-groups} ¿Qué representa la cantidad de `uniq -c`?

::option[La cantidad de caracteres de cada línea de entrada.]{#uniq-character-count explanation="Contar caracteres no es el propósito de `uniq -c`; herramientas como `wc` calculan totales de caracteres y bytes."}
::option[La cantidad de líneas iguales consecutivas de cada grupo.]{#uniq-consecutive-count .correct explanation="`-c` antepone a cada grupo adyacente agrupado la cantidad de líneas que contenía."}
::option[La cantidad total de líneas coincidentes en cualquier parte del archivo.]{#uniq-global-count explanation="Las líneas iguales separadas forman grupos distintos, salvo que primero se ordenen o agrupen los datos."}
:::

## Seleccionar grupos únicos o repetidos

Usa `-u` para imprimir solo los grupos que contienen exactamente una línea:

```bash
$ uniq -u reading.txt
magazine
```

Usa `-d` para imprimir una línea representativa de cada grupo adyacente que contenga más de una línea:

```bash
$ uniq -d reading.txt
book
paper
article
```

`uniq -D` de GNU imprime todas las líneas de los grupos repetidos, mientras que `-d` en minúscula imprime una vez el valor de cada grupo repetido.

:::single-choice{#uniq-only-singletons} ¿Qué orden imprime únicamente los grupos adyacentes que aparecen exactamente una vez?

::option[`uniq -c reading.txt`]{#uniq-count-reading explanation="Esto imprime todos los grupos con una cantidad, incluidos los repetidos y los de una sola línea."}
::option[`uniq -d reading.txt`]{#uniq-duplicate-reading explanation="`-d` en minúscula imprime una línea por cada grupo repetido, la selección contraria."}
::option[`uniq -u reading.txt`]{#uniq-single-reading .correct explanation="La opción `-u` selecciona los grupos cuya secuencia adyacente tiene una longitud exacta de uno."}
:::

:::single-choice{#uniq-one-per-duplicate-group} ¿Qué orden imprime una línea por cada grupo adyacente que aparece más de una vez?

::option[`uniq -d reading.txt`]{#uniq-duplicate-groups .correct explanation="La opción `-d` selecciona grupos adyacentes repetidos y emite una línea representativa por grupo."}
::option[`uniq -D reading.txt`]{#uniq-all-duplicate-lines explanation="`-D` en mayúscula de GNU imprime todas las líneas que pertenecen a grupos repetidos, no solo una representativa."}
::option[`uniq -u reading.txt`]{#uniq-unique-groups explanation="La opción `-u` selecciona grupos de una sola línea, no grupos repetidos."}
:::

## Agrupar duplicados separados

Si las líneas iguales están separadas, forman grupos diferentes:

```plaintext
book
paper
book
paper
article
magazine
article
```

Ejecutar `uniq` sobre este archivo produce un resultado que puede sorprender:

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

No se agrupa ninguna línea porque los valores vecinos son distintos. Ordena primero cuando sea aceptable cambiar el orden y quieras reunir líneas completas iguales:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Usa una configuración regional y una política de comparación uniformes en ambos pasos. `sort -u reading.txt` también puede ordenar y conservar una línea por cada clave de ordenación igual en una sola orden.

:::single-choice{#uniq-separated-duplicates} Hay líneas iguales dispersas por `reading.txt` y el orden de salida puede cambiar. ¿Qué tubería produce una copia ordenada de cada línea completa distinta?

::option[`sort reading.txt | uniq`]{#sort-then-uniq .correct explanation="La ordenación reúne líneas completas iguales y después `uniq` reduce cada grupo adyacente a una línea."}
::option[`uniq reading.txt | sort`]{#uniq-before-sort explanation="`uniq` se ejecuta antes de que las líneas iguales separadas queden juntas, por lo que la ordenación posterior puede dejar líneas de salida duplicadas."}
::option[`uniq -c reading.txt | head`]{#uniq-count-head explanation="Esto cuenta los grupos adyacentes existentes y luego limita la salida. No agrupa globalmente los duplicados separados."}
:::

`uniq` lee de la entrada estándar cuando no se indica un archivo de entrada, por eso encaja de forma natural después de `sort`. Opciones de GNU como `-i` pueden ignorar las mayúsculas, mientras que `-f`, `-s` y `-w` pueden omitir o limitar regiones de comparación; úsalas solo cuando la igualdad deba definirse mediante una parte de cada línea.

Para practicar cómo agrupar, contar y filtrar duplicados, prueba estos laboratorios prácticos:

1. **[Orden uniq de Linux: filtrado de duplicados](https://labex.io/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Aprende a usar `uniq` junto con `sort` para identificar, filtrar y analizar líneas duplicadas en archivos de texto.
2. **[Orden sort de Linux: ordenación de texto](https://labex.io/labs/linux-linux-sort-command-text-sorting-219196)** - Practica el uso de `sort` para organizar líneas de archivos de texto, un paso crucial para usar `uniq` de manera eficaz.
3. **[Recuento de palabras y ordenación](https://labex.io/labs/linux-word-count-and-sorting-388125)** - Aprende las herramientas esenciales `wc` y `sort` en este desafío práctico: cuenta líneas, palabras y caracteres, encuentra patrones frecuentes y ordena datos de forma eficiente.

## Resumen

Ahora puedes analizar grupos adyacentes de líneas iguales con `uniq`.

1. Reduce cada grupo duplicado adyacente a una línea.
2. Cuenta apariciones consecutivas con `-c`.
3. Selecciona grupos de una sola línea con `-u`.
4. Selecciona grupos repetidos con `-d` o con `-D` de GNU.
5. Ordena primero cuando sea necesario agrupar duplicados separados.
