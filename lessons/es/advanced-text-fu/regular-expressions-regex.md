---
index: 1
lang: "es"
title: "regex (Expresiones Regulares)"
meta_title: "regex (Expresiones Regulares) - Dominio Avanzado de Texto"
meta_description: "Domina los fundamentos de Linux con nuestra guía de expresiones regulares (regex). Aprende el emparejamiento de patrones con grep, usando sintaxis como ^, $, y []. Es una de las mejores formas de aprender manipulación de texto en Linux y avanzar tus habilidades."
meta_keywords: "expresiones regulares linux, regex, fundamentos de linux, emparejamiento de patrones, grep, procesamiento de texto, aprender linux, tutorial linux, forma más rápida linux avanzado"
---

## Lesson Content

Las expresiones regulares, a menudo abreviadas como regex, son una herramienta poderosa para la selección de texto basada en patrones. Comprenderlas es fundamental para dominar la manipulación de texto en Linux. Si bien hay muchas aplicaciones para aprender Linux, profundizar en conceptos centrales como `regular expression linux` es la forma más rápida de alcanzar un dominio avanzado en Linux. Utilizan notaciones especiales, algunas de las cuales son similares a los comodines como `*`.

Exploremos algunos de los operadores de regex más comunes, que son casi universales en todos los lenguajes de programación. Usaremos el siguiente texto como nuestro ejemplo:

```plaintext
sally sells seashells
by the seashore
```

### Anclaje al Inicio de una Línea

El símbolo de circunflejo `^` coincide con el comienzo de una línea. Asegura que tu patrón aparezca solo al principio.

```plaintext
^by
```

Este patrón coincidiría con la línea "by the seashore" pero no con "sally sells seashells".

### Anclaje al Final de una Línea

El símbolo de dólar `$` coincide con el final de una línea. Es el homólogo del ancla `^`.

```plaintext
seashore$
```

Este patrón coincidiría con la línea "by the seashore" porque termina con "seashore".

### Coincidencia de Cualquier Carácter Único

El punto `.` es un comodín que coincide con cualquier carácter único.

```plaintext
b.
```

En nuestro ejemplo, esto coincidiría con "by".

### Uso de Corchetes para Conjuntos de Caracteres

Los corchetes `[]` le permiten especificar un conjunto de caracteres para hacer coincidir. Esto proporciona más control que el comodín `.`.

```plaintext
s[ae]lls
```

Esto coincidiría con "sells" y también coincidiría con "salls".

También puede usar corchetes para especificar lo que _no_ debe coincidir. Cuando el circunflejo `^` es el primer carácter dentro de los corchetes, niega el conjunto, haciendo coincidir cualquier carácter _excepto_ los enumerados.

```plaintext
s[^e]lls
```

Esto coincidiría con "salls" pero no con "sells".

Finalmente, los corchetes admiten rangos para definir eficientemente un gran conjunto de caracteres.

```plaintext
d[a-c]g
```

Este patrón coincidirá con "dag", "dbg" y "dcg". Tenga en cuenta que los rangos distinguen entre mayúsculas y minúsculas. Por ejemplo, `[a-c]` no coincidirá con `A`, `B` o `C`.

Aprender estos operadores es una de las mejores maneras de aprender la eficiencia de la línea de comandos de Linux.

## Exercise

Ponga su conocimiento en práctica. Aquí hay algunos laboratorios prácticos para reforzar su comprensión de las expresiones regulares y la coincidencia de patrones:

1. **[Buscar Texto con grep en Linux](https://labex.io/es/labs/comptia-search-text-with-grep-in-linux-590841)** - En este laboratorio, aprenderá a buscar texto en archivos en un sistema Linux usando el comando `grep`. Realizará búsquedas básicas, mostrará números de línea, usará anclas como `^` y `$` para hacer coincidir posiciones de línea, y aprovechará las expresiones regulares básicas y extendidas para la coincidencia de patrones complejos.
2. **[Procesamiento de Texto y Expresiones Regulares](https://labex.io/es/labs/linux-text-processing-and-regular-expressions-18003)** - Aprenda las potentes herramientas de procesamiento de texto grep, sed y awk. Aprenda a usar expresiones regulares para una manipulación de texto eficiente y coincidencia de patrones en Linux.
3. **[Extraer Correos y Números](https://labex.io/es/labs/linux-extracting-mails-and-numbers-17991)** - En este desafío, aprenderá a usar grep y expresiones regulares para extraer direcciones de correo electrónico y números de un archivo, demostrando habilidades esenciales de procesamiento de texto en Linux.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con las expresiones regulares y el procesamiento de texto.

## Quiz Question

¿Qué expresión regular usaría para hacer coincidir cualquier carácter único?

## Quiz Answer

.
