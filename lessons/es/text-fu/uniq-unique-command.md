---
index: 14
lang: "es"
title: "uniq (Único)"
meta_title: "uniq (Único) - Text-Fu"
meta_description: "Aprende a usar el comando `uniq` de Linux para eliminar líneas duplicadas de archivos de texto. Descubre opciones como -c, -u, -d, y combínalo con `sort` para una limpieza de datos efectiva."
meta_keywords: "comando uniq, Linux uniq, eliminar duplicados, sort uniq, tutorial Linux, procesamiento de texto, Linux para principiantes, guía Linux"
---

## Lesson Content

El comando `uniq` (único) es otra herramienta útil para analizar texto.

Digamos que tienes un archivo con muchos duplicados:

```plaintext
reading.txt
book
book
paper
paper
article
article
magazine
```

Y quieres eliminar los duplicados; bueno, puedes usar el comando `uniq`:

```bash
$ uniq reading.txt
book
paper
article
magazine
```

Obtengamos el recuento de cuántas ocurrencias de una línea:

```bash
$ uniq -c reading.txt
2 book
2 paper
2 article
1 magazine
```

Obtengamos solo valores únicos:

```bash
$ uniq -u reading.txt
magazine
```

Obtengamos solo valores duplicados:

```bash
$ uniq -d reading.txt
book
paper
article
```

**Nota**: `uniq` no detecta líneas duplicadas a menos que sean adyacentes. Por ejemplo:

Digamos que tienes un archivo con duplicados que no son adyacentes:

```plaintext
reading.txt
book
paper
book
paper
article
magazine
article
```

```bash
$ uniq reading.txt
reading.txt
book
paper
book
paper
article
magazine
article
```

El resultado devuelto por `uniq` contendrá todas las entradas, a diferencia del primer ejemplo.

Para superar esta limitación de `uniq`, podemos usar `sort` en combinación con `uniq`:

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del procesamiento de texto con `uniq` y `sort`:

1. **[Comando uniq de Linux: Filtrado de Duplicados](https://labex.io/es/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - Aprende a usar el comando `uniq` de Linux en combinación con `sort` para identificar, filtrar y analizar líneas duplicadas en archivos de texto.
2. **[Comando sort de Linux: Ordenación de Texto](https://labex.io/es/labs/linux-linux-sort-command-text-sorting-219196)** - Practica el uso del comando `sort` para organizar líneas de archivos de texto, un paso crucial antes de usar `uniq` de manera efectiva.
3. **[Conteo y Ordenación de Palabras](https://labex.io/es/labs/linux-word-count-and-sorting-388125)** - Aprende las herramientas esenciales de procesamiento de texto de Linux `wc` (conteo de palabras) y `sort` en este desafío práctico. Aprende a contar líneas, palabras y caracteres, encontrar patrones frecuentes y ordenar datos de manera eficiente para diversas tareas de análisis de texto.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con el procesamiento de texto y la manipulación de datos en Linux.

## Quiz Question

¿Qué comando usarías para eliminar duplicados en un archivo?

## Quiz Answer

uniq
