---
lang: "es"
title: "paste"
meta_description: "Aprende a usar el comando paste de Linux para fusionar líneas de archivos. Descubre delimitadores y combina archivos con este tutorial esencial del comando Linux."
meta_keywords: "comando paste de Linux, tutorial del comando paste, fusionar líneas de archivos, comandos de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

El comando `paste` es similar al comando `cat`; fusiona líneas en un archivo. Creemos un nuevo archivo con el siguiente contenido:

```
sample2.txt
The
quick
brown
fox
```

Combinemos todas estas líneas en una sola línea:

```bash
paste -s sample2.txt
```

El delimitador predeterminado para `paste` es TAB, por lo que ahora hay una línea con TABs separando cada palabra.

Cambiemos este delimitador (`-d`) a algo un poco más legible:

```bash
paste -d ' ' -s sample2.txt
```

Ahora todo debería estar en una línea delimitada por espacios.

## Exercise

Intenta pegar varios archivos juntos. ¿Qué sucede?

## Quiz Question

¿Qué bandera usas con `paste` para que todo vaya en una sola línea?

## Quiz Answer

-s
