---
lesson_id: "grep-command"
course_id: "text-fu"
lang: "es"
order_index: 16
title: "grep"
description: "Aprende a seleccionar líneas mediante cadenas fijas o expresiones regulares y a interpretar los resultados de grep."
meta_title: "grep - Text-Fu"
meta_description: "Aprende a usar la potente orden grep de Linux para buscar patrones de texto. Esta guía explica el uso básico, grep -e, grep -c y otras opciones esenciales."
meta_keywords: "orden grep, orden grep -e, grep -c, grep -f, grep -o, ejemplo grep -e, grep Linux, buscar texto, coincidencia de patrones, procesamiento de texto"
---

La orden `grep` selecciona líneas de entrada que coinciden con un patrón. Puede buscar en archivos indicados o en la entrada estándar, imprimir contexto coincidente, contar líneas seleccionadas y comunicar mediante su estado de salida si se encontró una coincidencia.

## Buscar líneas en un archivo

Proporciona un patrón seguido de uno o más archivos de entrada:

```bash
$ grep 'fox' sample.txt
```

De forma predeterminada, `grep` de GNU interpreta el patrón como una expresión regular básica e imprime todas las líneas seleccionadas. Pon los patrones entre comillas para evitar que el shell interprete primero los espacios y metacaracteres.

Usa `-F` cuando el patrón deba tratarse como una cadena fija en vez de como una expresión regular:

```bash
$ grep -F 'price: $5.00' products.txt
```

:::single-choice{#grep-fixed-string}
¿Qué orden busca en `products.txt` el texto literal `price: $5.00` sin tratar los caracteres del patrón como sintaxis de expresiones regulares?

::option[`grep -F 'price: $5.00' products.txt`]{#grep-fixed-price .correct explanation="`-F` selecciona la coincidencia de cadenas fijas y las comillas simples protegen el signo de dólar de la expansión del shell."}
::option[`grep -E 'price: $5.00' products.txt`]{#grep-extended-price explanation="`-E` activa expresiones regulares extendidas, donde `$` y `.` tienen significados especiales en vez de ser literales."}
::option[`grep -v 'price: $5.00' products.txt`]{#grep-invert-price explanation="`-v` selecciona líneas que no coinciden y sigue usando de forma predeterminada la interpretación como expresión regular."}
:::

## Seleccionar la sintaxis del patrón

`grep` de GNU ofrece tres modos de patrón habituales:

- Predeterminado: expresiones regulares básicas.
- `-E`: expresiones regulares extendidas, con operadores como `|`, `+` y `?` sin barras invertidas.
- `-F`: cadenas fijas sin operadores de expresiones regulares.

Anclas como `^` y `$` coinciden con el principio y el final de una línea. Para encontrar en una lista de texto nombres de archivo que terminen con el sufijo literal `.txt`:

```bash
$ grep -E '\.txt$' filenames.txt
```

La barra invertida hace que el punto sea literal; un `.` sin escapar en una expresión regular coincide con cualquier carácter individual.

:::single-choice{#grep-literal-txt-suffix}
¿Qué expresión regular extendida coincide con líneas que terminan con el sufijo literal `.txt`?

::option[`'.txt$'`]{#grep-anychar-txt explanation="El punto no está escapado, por lo que coincide con cualquier carácter anterior a `txt`, no específicamente con un punto literal."}
::option[`'\.txt$'`]{#grep-dot-txt-end .correct explanation="`\.` coincide con un punto literal y `$` ancla la coincidencia al final de la línea."}
::option[`'^.txt'`]{#grep-start-anychar-txt explanation="Esto ancla al principio y sigue usando un punto sin escapar, por lo que expresa una coincidencia diferente."}
:::

## Proporcionar patrones de forma segura

Usa `-e PATTERN` para proporcionar un patrón explícitamente. Resulta especialmente útil cuando el patrón comienza por `-`, porque las comillas por sí solas no detienen el análisis de opciones:

```bash
$ grep -e '-v' settings.conf
```

Puedes repetir `-e` para seleccionar líneas que coincidan con cualquiera de los patrones proporcionados. Usa `-f patterns.txt` para leer un patrón por línea desde un archivo.

:::single-choice{#grep-hyphen-pattern}
¿Qué orden busca el patrón `-v` en `settings.conf` en vez de interpretarlo como una opción?

::option[`grep '-v' settings.conf`]{#grep-quoted-v explanation="Las comillas protegen los caracteres de la expansión del shell, pero `grep` aún puede interpretar el argumento resultante `-v` como su opción para invertir coincidencias."}
::option[`grep -v settings.conf`]{#grep-invert-settings explanation="Esto activa la coincidencia invertida y no proporciona `settings.conf` como patrón y entrada del modo solicitado."}
::option[`grep -e '-v' settings.conf`]{#grep-explicit-v .correct explanation="La opción `-e` declara que el argumento siguiente es un patrón aunque comience por un guion."}
:::

## Controlar la salida seleccionada

- `-i`: ignora las diferencias entre mayúsculas y minúsculas.
- `-n`: antepone números de línea a las líneas seleccionadas.
- `-v`: selecciona las líneas que no coinciden.
- `-c`: imprime la cantidad de líneas seleccionadas de cada archivo de entrada.
- `-o`: imprime solo cada parte coincidente no vacía en lugar de la línea seleccionada completa.

Por ejemplo, cuenta líneas que contengan `fox` sin distinguir entre mayúsculas y minúsculas:

```bash
$ grep -ic 'fox' sample.txt
```

`-c` cuenta líneas seleccionadas, no la cantidad total de coincidencias dentro de ellas. Una línea que contiene `fox fox` aporta uno al recuento. Cuando necesites específicamente apariciones no superpuestas con `grep` de GNU, una posible tubería es `grep -o PATTERN | wc -l`.

:::single-choice{#grep-count-lines}
`data.txt` tiene una línea que contiene `error error` y dos líneas sin coincidencias. ¿Qué muestra `grep -c 'error' data.txt`?

::option[`2`, porque la palabra aparece dos veces en una línea.]{#grep-count-occurrences explanation="`-c` cuenta líneas seleccionadas, no coincidencias individuales dentro de una línea."}
::option[`1`, porque coincide exactamente una línea.]{#grep-count-one-line .correct explanation="La única línea se selecciona una vez aunque el patrón aparezca dos veces en ella."}
::option[`3`, porque el archivo contiene tres líneas en total.]{#grep-count-total-lines explanation="Solo las líneas seleccionadas contribuyen a `grep -c`; las que no coinciden quedan excluidas."}
:::

## Filtrar la entrada estándar y buscar en directorios

Cuando no se indica ningún archivo de entrada, `grep` lee de la entrada estándar y encaja de forma natural en una tubería:

```bash
$ env | grep '^USER='
```

Usa `-r` para buscar recursivamente en archivos legibles dentro de un directorio:

```bash
$ grep -r 'listen_port' config/
```

Los diagnósticos, como errores de permisos, se envían a la salida de error estándar y no forman parte de la entrada en la que se buscan coincidencias. Limita la ruta de búsqueda y comprende los permisos en vez de elevar el acceso inmediatamente.

:::single-choice{#grep-pipeline-input}
En `generate-report | grep 'failed'`, ¿qué entrada examina `grep`?

::option[Un archivo llamado `generate-report` en el directorio actual.]{#grep-report-file explanation="La palabra de la izquierda se ejecuta como una orden y no se entrega a `grep` como operando de archivo."}
::option[El flujo de salida estándar producido por `generate-report`.]{#grep-report-stdout .correct explanation="La tubería conecta la salida estándar del productor con la entrada estándar de `grep`."}
::option[El flujo de error estándar producido por `generate-report`.]{#grep-report-stderr explanation="Una tubería normal transporta la salida estándar. El error estándar permanece separado salvo que se redirija explícitamente."}
:::

## Interpretar el estado de salida

En búsquedas normales, `grep` de GNU devuelve el estado `0` cuando se selecciona al menos una línea, `1` cuando no se selecciona ninguna y `2` cuando se produce un error. Esto permite que los scripts comprueben una coincidencia sin tratar «sin coincidencias» como la misma situación que un archivo ilegible o un patrón no válido.

Opciones como `-q` suprimen la salida normal y se detienen tras encontrar una coincidencia, lo que resulta útil para comprobaciones condicionales. No deduzcas el éxito únicamente de una pantalla vacía: `-q`, una redirección, la ausencia de coincidencias y un error pueden producir poca o ninguna salida estándar, pero sus estados son distintos.

Para practicar búsquedas con cadenas fijas y expresiones regulares, prueba estos laboratorios prácticos:

1. **[Buscar texto con grep en Linux](https://labex.io/labs/comptia-search-text-with-grep-in-linux-590841)** - Practica búsquedas básicas, números de línea, anclas y expresiones regulares básicas y extendidas para crear coincidencias de patrones complejas con `grep`.
2. **[Orden grep de Linux: búsqueda de patrones](https://labex.io/labs/linux-linux-grep-command-pattern-searching-219192)** - Aprende a usar `grep` para buscar patrones en archivos de texto y explora expresiones regulares para definir búsquedas complejas.
3. **[Aguja en el pajar](https://labex.io/labs/linux-needle-in-the-haystack-388109)** - Usa `grep` para buscar patrones concretos, contar apariciones, extraer valores únicos y combinar varios criterios de búsqueda en archivos de registro.

## Resumen

Ahora puedes buscar texto orientado a líneas y distinguir las coincidencias de los errores.

1. Elige entre coincidencias básicas, extendidas o de cadenas fijas.
2. Pon los patrones entre comillas y usa `-e` si comienzan por un guion.
3. Cuenta líneas seleccionadas sin confundirlas con apariciones.
4. Filtra la entrada estándar o busca recursivamente en un directorio limitado.
5. Interpreta los estados de salida de coincidencia, ausencia de coincidencia y error.
