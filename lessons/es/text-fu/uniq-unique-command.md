---
title: "uniq (Único)"
description: "Aprende a usar el comando `uniq` de Linux para eliminar líneas duplicadas de archivos de texto. Descubre opciones como -c, -u, -d, y combínalo con `sort` para una limpieza de datos efectiva."
keywords: "comando uniq, Linux uniq, eliminar duplicados, sort uniq, tutorial Linux, procesamiento de texto, Linux para principiantes, guía Linux"
---

## Lesson Content

El comando `uniq` (unique) es otra herramienta útil para analizar texto.

Supongamos que tienes un archivo con muchos duplicados:

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

Obtengamos solo los valores únicos:

```bash
$ uniq -u reading.txt
magazine
```

Obtengamos solo los valores duplicados:

```bash
$ uniq -d reading.txt
book
paper
article
```

**Nota**: `uniq` no detecta líneas duplicadas a menos que sean adyacentes. Por ejemplo:

Supongamos que tienes un archivo con duplicados que no son adyacentes:

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

¿Qué resultado obtendrías si intentaras `uniq -uc`?

## Quiz Question

¿Qué comando usarías para eliminar duplicados en un archivo?

## Quiz Answer

uniq
