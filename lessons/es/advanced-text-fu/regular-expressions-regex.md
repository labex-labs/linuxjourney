---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "es"
order_index: 1
title: "regex (expresiones regulares)"
description: "Aprende cómo las anclas, los conjuntos de caracteres, la repetición y las variantes de regex controlan la coincidencia de patrones de texto."
meta_title: "regex (expresiones regulares) - Text-Fu avanzado"
meta_description: "Domina los fundamentos de las expresiones regulares en Linux. Aprende a buscar patrones con grep mediante sintaxis como ^, $, conjuntos y repeticiones."
meta_keywords: "expresiones regulares Linux, regex, fundamentos Linux, coincidencia de patrones, grep, procesamiento de texto, aprender Linux, tutorial Linux"
---

Las expresiones regulares, abreviadas con frecuencia como **regex**, describen patrones de texto. Herramientas como `grep`, `sed` y `awk` usan regex, pero la sintaxis que admiten puede variar, así que identifica siempre la herramienta y la variante de expresiones regulares.

`grep` de GNU usa expresiones regulares básicas (BRE) de forma predeterminada y expresiones regulares extendidas (ERE) con `-E`. Esta lección presenta primero elementos compartidos por ambas y después señala incorporaciones habituales de ERE.

Usa esta entrada en los ejemplos:

```text
sally sells seashells
by the seashore
```

## Buscar texto literal

La mayoría de los caracteres normales coinciden consigo mismos. El patrón `seashells` selecciona una línea que contenga esa secuencia exacta en cualquier posición:

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

Pon los patrones regex entre comillas para que el shell no los expanda ni divida antes de que los reciba la herramienta de coincidencia. Las regex también difieren de la expansión de rutas del shell: en una regex, `*` repite el átomo anterior; en un patrón glob del shell, `*` es por sí mismo un comodín para una secuencia de caracteres de una ruta.

:::single-choice{#regex-versus-shell-star} ¿Qué hace `*` en una expresión regular como `ab*`?

::option[Coincide con cualquier nombre de archivo del directorio actual.]{#regex-shell-glob explanation="Eso describe la expansión de rutas del shell en el contexto de una orden, no el significado de `*` dentro de una regex."}
::option[Repite la `b` anterior cero o más veces.]{#regex-repeat-b .correct explanation="Un cuantificador regex se aplica al átomo inmediatamente anterior, por lo que `ab*` coincide con `a`, `ab`, `abb`, etc."}
::option[Repite la cadena completa `ab` exactamente dos veces.]{#regex-repeat-ab-twice explanation="El asterisco solo se aplica al átomo anterior y permite cero o más repeticiones, no exactamente dos repeticiones de la cadena completa."}
:::

## Anclar una coincidencia

Fuera de una expresión entre corchetes, `^` al principio de un patrón ancla la coincidencia al principio de una línea:

```plaintext
^by
```

El ancla `$` coincide con el final de una línea:

```plaintext
seashore$
```

Combina ambas anclas cuando toda la línea deba ajustarse al patrón:

```text
^by the seashore$
```

:::single-choice{#regex-complete-line} ¿Qué patrón coincide únicamente con una línea cuyo texto completo es `by the seashore`?

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="El circunflejo exige que la coincidencia comience al principio y el signo de dólar que termine con la línea."}
::option[`by the seashore`]{#regex-unanchored-line explanation="Sin anclas, esta secuencia puede coincidir dentro de una línea más larga con texto adicional antes o después."}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="El ancla final no puede preceder al texto que debe coincidir ni el ancla inicial seguirlo en este patrón."}
:::

## Coincidir con un carácter

El punto coincide con un carácter en el modo normal de expresiones regulares orientadas a líneas:

```plaintext
b.
```

Esto coincide con `by`, pero también podría coincidir con `ba` o `b7`. No coincide con una `b` aislada porque exige un carácter después. Para buscar un punto literal, escápalo como `\.` o colócalo en una expresión entre corchetes adecuada.

:::single-choice{#regex-dot-character} ¿Con qué cadena no coincide el patrón de línea completa `^b.$`?

::option[`by`]{#regex-dot-by explanation="El punto coincide con `y`, por lo que la línea de dos caracteres satisface el patrón."}
::option[`b`]{#regex-dot-b .correct explanation="El punto exige un carácter después de `b`, pero esta cadena termina inmediatamente."}
::option[`b7`]{#regex-dot-b7 explanation="El punto coincide con el dígito `7`, por lo que esta línea de dos caracteres satisface el patrón."}
:::

## Usar expresiones entre corchetes

Una expresión entre corchetes coincide con un carácter de un conjunto especificado:

```plaintext
s[ae]lls
```

Esto coincide con `sells` o `salls` en esa posición.

Cuando `^` es el primer carácter después de `[`, niega el conjunto:

```plaintext
s[^e]lls
```

Esto coincide con `salls`, pero no con `sells`, porque el carácter posterior a la primera `s` no puede ser `e`.

:::single-choice{#regex-negated-bracket} ¿Con qué coincide `[^e]`?

::option[Exactamente un carácter distinto de `e`.]{#regex-not-e .correct explanation="Un circunflejo inicial dentro de los corchetes complementa el conjunto indicado, mientras que la expresión sigue consumiendo un carácter."}
::option[El principio de una línea seguido de `e`.]{#regex-caret-e-anchor explanation="Dentro de una expresión entre corchetes, un circunflejo inicial niega el conjunto en vez de anclar una línea."}
::option[Cero o más apariciones de la letra `e`.]{#regex-repeat-e explanation="La repetición requeriría un cuantificador como `*`; esta expresión coincide con un carácter que no sea `e`."}
:::

Los intervalos pueden describir caracteres entre dos extremos:

```plaintext
d[a-c]g
```

Esto puede coincidir con `dag`, `dbg` o `dcg`. El comportamiento de los intervalos puede depender de la intercalación de la configuración regional. Las clases de caracteres como `[[:lower:]]`, `[[:upper:]]` y `[[:digit:]]` suelen expresar la intención con mayor claridad.

## Repetir y combinar patrones

Tanto en BRE como en ERE, `*` significa cero o más repeticiones del átomo anterior:

```text
seashells*
```

Esto coincide con `seashell` seguido de cero o más caracteres `s` adicionales. En el modo ERE con `grep -E`, los operadores habituales incluyen:

- `+`: una o más repeticiones.
- `?`: cero o una repetición.
- `|`: la expresión de la izquierda o la de la derecha.
- `(...)`: agrupa expresiones.

Por ejemplo:

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

Esto selecciona líneas completas iguales a `cat`, `cats`, `dog` o `dogs`. En el modo BRE, estos operadores tienen reglas de escape diferentes, así que no copies un patrón entre variantes sin comprobarlo.

:::single-choice{#regex-extended-alternation} ¿Qué orden activa la sintaxis de expresiones regulares extendidas para el patrón `^(cat|dog)s?$`?

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F` trata todos los operadores regex como texto literal, por lo que desactiva la agrupación, la alternancia y la repetición opcional."}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E` selecciona expresiones regulares extendidas, lo que activa la agrupación, la alternancia y la `s` opcional mostradas."}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="`grep` usa BRE de forma predeterminada, donde estos caracteres sin escapar de agrupación y alternancia no tienen el significado ERE previsto."}
:::

Para practicar la selección mediante regex con herramientas de texto de Linux, prueba estos laboratorios prácticos:

1. **[Buscar texto con grep en Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** - Aprende a buscar texto en archivos con `grep`, mostrar números de línea, usar anclas como `^` y `$` y aprovechar expresiones regulares básicas y extendidas.
2. **[Procesamiento de texto y expresiones regulares](https://labex.io/labs/linux-text-processing-and-regular-expressions-18003)** - Aprende a usar las herramientas `grep`, `sed` y `awk`, así como expresiones regulares para manipular texto y buscar patrones de forma eficiente.
3. **[Extracción de correos y números](https://labex.io/labs/linux-extracting-mails-and-numbers-17991)** - Usa `grep` y expresiones regulares para extraer direcciones de correo electrónico y números de un archivo.

## Resumen

Ahora puedes leer y construir expresiones regulares fundamentales orientadas a líneas.

1. Distingue los operadores regex de los comodines de rutas del shell.
2. Ancla coincidencias al principio o al final de una línea.
3. Coincide con un carácter mediante un punto o una expresión entre corchetes.
4. Niega conjuntos y usa clases de caracteres dependientes de la configuración regional.
5. Elige deliberadamente la sintaxis BRE o ERE.
