---
title: "expand y unexpand"
description: "Aprenda a convertir tabulaciones a espacios con el comando `expand` y espacios a tabulaciones con `unexpand`. Mejore el formato de archivos de texto con este tutorial de Linux."
keywords: "comando expand, comando unexpand, tabulaciones Linux, espacios Linux, formato de texto, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

En nuestra lección sobre el comando `cut`, teníamos nuestro archivo `sample.txt` que contenía una tabulación. Normalmente, las tabulaciones suelen mostrar una diferencia notable, pero algunos archivos de texto no lo muestran lo suficientemente bien. Tener tabulaciones en un archivo de texto puede no proporcionar el espaciado deseado. Para cambiar sus tabulaciones a espacios, use el comando `expand`.

```bash
expand sample.txt
```

El comando anterior imprimirá la salida con cada tabulación convertida en un grupo de espacios. Para guardar esta salida en un archivo, use la redirección de salida como se muestra a continuación.

```bash
expand sample.txt > result.txt
```

Opuesto a `expand`, podemos convertir cada grupo de espacios de nuevo a una tabulación con el comando `unexpand`:

```bash
unexpand -a result.txt
```

## Exercise

¿Qué sucede si solo escribe `expand` sin entrada de archivo?

## Quiz Question

¿Qué comando se utiliza para convertir tabulaciones en espacios?

## Quiz Answer

expand
