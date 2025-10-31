---
index: 14
lang: "es"
title: "uniq (Único)"
meta_title: "uniq (Único) - Text-Fu"
meta_description: "Explora el comando uniq en Linux para filtrar y eliminar líneas adyacentes duplicadas de texto. Aprende a usar la herramienta uniq de Linux con opciones como -c, -u, -d y combínala con sort para un potente procesamiento de texto."
meta_keywords: "comando uniq, uniq Linux, uniq linux, eliminar duplicados, sort uniq, procesamiento de texto, limpieza de datos, tutorial Linux"
---

## Lesson Content

El comando `uniq` (único) es una herramienta esencial para el procesamiento de texto en Linux. Te ayuda a filtrar y gestionar líneas duplicadas dentro de un archivo de texto, pero es importante entender cómo funciona para usarlo eficazmente.

### Eliminación Básica de Duplicados

La función principal del comando `uniq` es eliminar líneas adyacentes duplicadas. Imagina que tienes un archivo llamado `reading.txt` con el siguiente contenido:

```plaintext
book
book
paper
paper
article
article
magazine
```

Para eliminar las líneas repetidas, puedes ejecutar el comando `uniq`:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Como puedes ver, `uniq` muestra una versión del archivo con las líneas adyacentes duplicadas eliminadas.

### Opciones Avanzadas de Filtrado

El comando `uniq` también proporciona varias opciones para un análisis más detallado.

Para contar las ocurrencias de cada línea, usa la bandera `-c` (count/contar):

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

Para mostrar solo las líneas que no se repiten (es decir, que son únicas), usa la bandera `-u` (unique/único):

```bash
$ uniq -u reading.txt
magazine
```

Por el contrario, para mostrar solo las líneas que están duplicadas, usa la bandera `-d` (duplicated/duplicado):

```bash
$ uniq -d reading.txt
book
paper
article
```

### La Importancia de Ordenar (Sort)

Un detalle crítico sobre el comando **uniq linux** es que solo detecta líneas duplicadas si son directamente adyacentes entre sí. Si los duplicados están dispersos por el archivo, `uniq` no los identificará.

Considera esta versión de `reading.txt` donde los duplicados no son adyacentes:

```plaintext
book
paper
book
paper
article
magazine
article
```

Ejecutar `uniq` en este archivo producirá un resultado sorprendente:

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

No se eliminó ninguna línea porque ninguna línea idéntica estaba una al lado de la otra. Para solucionar esto, primero debes ordenar el contenido del archivo. Al canalizar (`pipe`) la salida de `sort` hacia `uniq`, te aseguras de que todas las líneas idénticas se vuelvan adyacentes, permitiendo que `uniq` funcione correctamente. Esta combinación es un patrón poderoso y común en la programación de shell.

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

Este comando primero ordena las líneas alfabéticamente y luego `uniq` filtra los duplicados, dándote una lista limpia de entradas únicas.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del procesamiento de texto con `uniq` y `sort`:

1. **[Comando uniq de Linux: Filtrado de Duplicados](https://labex.io/es/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Aprende a usar el comando `uniq` de Linux en combinación con `sort` para identificar, filtrar y analizar líneas duplicadas en archivos de texto.
2. **[Comando sort de Linux: Ordenación de Texto](https://labex.io/es/labs/linux-linux-sort-command-text-sorting-219196)** - Practica el uso del comando `sort` para organizar líneas de archivos de texto, un paso crucial antes de usar `uniq` eficazmente.
3. **[Conteo de Palabras y Ordenación](https://labex.io/es/labs/linux-word-count-and-sorting-388125)** - Aprende las herramientas esenciales de procesamiento de texto de Linux `wc` (conteo de palabras) y `sort` en este desafío práctico. Aprende a contar líneas, palabras y caracteres, encontrar patrones frecuentes y ordenar datos eficientemente para diversas tareas de análisis de texto.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con el procesamiento de texto y la manipulación de datos en Linux.

## Quiz Question

¿Qué comando usarías para eliminar líneas adyacentes duplicadas en un archivo? Por favor, responde usando solo el nombre del comando en minúsculas en inglés.

## Quiz Answer

uniq
