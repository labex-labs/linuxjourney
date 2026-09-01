---
lesson_id: "cut-command"
course_id: "text-fu"
lang: "es"
order_index: 6
title: "cut"
description: "Aprende a seleccionar posiciones de caracteres o campos delimitados de cada línea con `cut`."
meta_title: "cortar - Text-Fu"
meta_description: "Aprenda a usar el comando Linux `cut` para extraer secciones específicas de texto de archivos. Esta guía cubre el corte por carácter y campo (`cut f`), incluido cómo cortar f con delimitadores personalizados. Perfecto para dominar el procesamiento de texto en Linux."
meta_keywords: "comando cut, procesamiento de texto Linux, extraer texto, cut f, cómo usar cut f, tutorial Linux, ejemplos de cut, guía Linux, corte por campo"
---

La orden `cut` selecciona posiciones de caracteres o campos concretos de cada línea de entrada. Funciona mejor con texto de estructura coherente cuyos delimitadores y posiciones de campo se conocen.

Crea un pequeño archivo separado por tabuladores para los ejemplos. `printf` interpreta `\t` como una tabulación literal y `\n` como un salto de línea:

```bash
$ printf 'name\trole\nalice\tadmin\nbob\tviewer\n' > team.tsv
```

## Selección de posiciones de caracteres

Utiliza `-c LIST` para seleccionar posiciones de cada línea. Las posiciones empiezan en 1:

```bash
$ cut -c 1 team.tsv
n
a
b
```

La lista puede contener posiciones individuales e intervalos:

```bash
$ cut -c 1-4 team.tsv
name
alic
bob
$ cut -c 1,3 team.tsv
nm
ai
bb
```

Los espacios, tabuladores y signos de puntuación también ocupan posiciones. `cut` procesa cada línea de forma independiente.

:::single-choice{#cut-first-character} ¿Qué orden muestra el primer carácter de cada línea de `names.txt`?

::option[`cut -c 1 names.txt`]{#cut-character-one .correct explanation="La opción `-c` selecciona posiciones de caracteres y la posición 1 es el primer carácter de cada línea."}
::option[`cut -f 1 names.txt`]{#cut-field-one explanation="La opción `-f` selecciona el primer campo delimitado por tabuladores, que puede contener más de un carácter."}
::option[`cut -d 1 names.txt`]{#cut-delimiter-one explanation="La opción `-d` especifica un delimitador de campos y debe acompañarse de una selección de campos. No selecciona una posición de carácter."}
:::

## Selección de campos delimitados por tabuladores

Utiliza `-f LIST` para seleccionar campos. El delimitador predeterminado es una tabulación:

```bash
$ cut -f 2 team.tsv
role
admin
viewer
```

Al igual que en la selección de caracteres, una lista puede incluir valores como `1`, `1,3`, `2-4`, `-3` o `2-`.

:::single-choice{#cut-second-tab-field} ¿Qué orden muestra el segundo campo delimitado por tabuladores de cada línea de `team.tsv`?

::option[`cut -c 2 team.tsv`]{#cut-second-character explanation="Esta orden selecciona la segunda posición de carácter de cada línea, no el segundo campo separado por tabuladores."}
::option[`cut -f 2 team.tsv`]{#cut-second-field .correct explanation="Sin `-d`, el modo de campos utiliza una tabulación como delimitador y `-f 2` selecciona el segundo campo."}
::option[`cut -d 2 team.tsv`]{#cut-delimiter-two explanation="Esta orden intenta utilizar `2` como delimitador, pero no proporciona una lista de campos. No selecciona el campo 2."}
:::

## Elección de un delimitador personalizado

Utiliza `-d CHARACTER` junto con `-f` cuando los campos empleen un delimitador distinto de la tabulación. Este ejemplo crea datos separados por punto y coma:

```bash
$ printf 'alice;admin\nbob;viewer\n' > team.txt
$ cut -d ';' -f 1 team.txt
alice
bob
```

El delimitador de esta forma es un único carácter. Entrecomilla `;` porque un punto y coma sin comillas tiene un significado de control en la shell.

:::single-choice{#cut-semicolon-role-field} ¿Qué orden muestra el segundo campo delimitado por punto y coma de `team.txt`?

::option[`cut -d ':' -f 2 team.txt`]{#cut-colon-second explanation="Esta orden selecciona campos separados por dos puntos, pero el archivo utiliza puntos y comas."}
::option[`cut -d ';' -f 2 team.txt`]{#cut-semicolon-second .correct explanation="El punto y coma entrecomillado establece el delimitador y `-f 2` selecciona el segundo campo de cada línea."}
::option[`cut -c 2 -f ';' team.txt`]{#cut-mixed-options explanation="Esta orden mezcla la selección de caracteres con un argumento de campo no válido. El delimitador debe seguir a `-d` y el número de campo a `-f`."}
:::

## Tratamiento de líneas sin delimitador

En el modo de campos, `cut` suele mostrar sin cambios una línea que no contiene el delimitador. Añade `-s` para suprimir esas líneas:

```bash
$ printf 'alice;admin\nheader\nbob;viewer\n' | cut -s -d ';' -f 2
admin
viewer
```

Esto no valida un archivo CSV general. Un CSV puede contener delimitadores entre comillas, saltos de línea incrustados y reglas de escape que una separación por un solo carácter no comprende; utiliza una herramienta compatible con CSV para esos datos.

:::single-choice{#cut-suppress-undelimited} ¿Qué hace `-s` en `cut -d ':' -f 1`?

::option[Ordena los campos seleccionados antes de mostrarlos.]{#cut-s-sort explanation="`cut` no ordena la entrada y `-s` no está relacionado con el orden."}
::option[Trata varios delimitadores consecutivos como un único separador.]{#cut-s-squeeze explanation="`cut` no utiliza `-s` para comprimir delimitadores. Los campos vacíos siguen ocupando posiciones significativas."}
::option[Suprime las líneas que no contienen el delimitador seleccionado.]{#cut-s-suppress .correct explanation="En el modo de campos, `-s` impide que las líneas sin delimitador se transmitan sin cambios."}
:::

## Lectura desde stdin

Cuando no se indica ningún archivo, o se utiliza `-` como operando de entrada, `cut` lee stdin. Esto lo convierte en una etapa natural de una tubería:

```bash
$ printf 'red:1\nblue:2\n' | cut -d ':' -f 1
red
blue
```

:::single-choice{#cut-pipeline-input} En `generate-data | cut -d ':' -f 1`, ¿de dónde lee `cut` la entrada?

::option[De stdout de `generate-data` a través de la tubería.]{#cut-pipe-stdin .correct explanation="La tubería conecta stdout del productor con stdin de `cut` y no se indica ningún archivo de entrada independiente."}
::option[De un archivo cuyo nombre literal es `generate-data`.]{#cut-pipe-file explanation="`generate-data` se ejecuta como orden izquierda de la tubería. No se pasa a `cut` como nombre de archivo."}
::option[Del flujo de error estándar de `cut`.]{#cut-pipe-stderr explanation="Una tubería normal alimenta la entrada estándar con stdout de la orden anterior, no con stderr de `cut`."}
:::

Para practicar la selección por posición y por campo, prueba estos laboratorios:

1. **[Orden cut de Linux: cortar texto](https://labex.io/es/labs/linux-linux-cut-command-text-cutting-219187)** - Practica la extracción de columnas o campos concretos de archivos de texto.
2. **[Control de secuencia y tuberías](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Utiliza tuberías y herramientas como `cut`, `grep`, `wc`, `sort` y `uniq` para procesar texto.

## Resumen

Ahora puedes seleccionar posiciones previsibles de texto orientado a líneas con `cut`.

1. Seleccionar posiciones de caracteres individuales o intervalos.
2. Extraer campos delimitados por tabuladores con `-f`.
3. Proporcionar un delimitador de un carácter con `-d`.
4. Suprimir líneas sin delimitador cuando sea apropiado.
5. Leer texto estructurado desde archivos o stdin.
