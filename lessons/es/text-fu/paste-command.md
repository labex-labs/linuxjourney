---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "es"
order_index: 7
title: "paste"
description: "Aprende a combinar líneas correspondientes o a serializar líneas con delimitadores configurables mediante `paste`."
meta_title: "paste - Text-Fu"
meta_description: "Aprende a usar el comando paste de Linux para fusionar líneas de archivos. Descubre delimitadores y combina archivos con este tutorial esencial del comando de Linux."
meta_keywords: "comando paste de Linux, tutorial del comando paste, fusionar líneas de archivos, comandos de Linux, Linux para principiantes, guía de Linux"
---

La orden `paste` combina líneas en forma de columnas. De manera predeterminada, toma una línea de cada archivo de entrada, las une con una tabulación y repite el proceso hasta que todas las entradas llegan al final.

## Combinación de archivos en paralelo

Crea dos archivos pequeños:

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

Pasa ambos archivos a `paste`:

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

El espacio visible entre columnas es una tabulación. A diferencia de `cat`, que escribe un archivo completo después de otro, `paste` combina las líneas correspondientes.

:::single-choice{#paste-corresponding-lines} `first.txt` contiene `A` y después `B`, mientras que `second.txt` contiene `1` y después `2`. ¿Qué produce `paste first.txt second.txt` de forma predeterminada?

::option[`A`, `B`, `1` y `2` en cuatro líneas consecutivas.]{#paste-concatenated-files explanation="Esto se parece a escribir los archivos uno detrás de otro. `paste` combina en cambio las líneas correspondientes."}
::option[`A`, `B`, `1` y `2` en una sola línea sin separadores.]{#paste-one-line-no-separator explanation="La serialización en una sola línea necesita `-s` y el separador predeterminado es una tabulación, no la ausencia de separador."}
::option[`A` junto con `1` y después `B` junto con `2`, separados por tabulaciones.]{#paste-parallel-result .correct explanation="El modo paralelo predeterminado toma una línea de cada archivo para cada línea de salida y separa los campos con una tabulación."}
:::

## Elección de un delimitador

Utiliza `-d LIST` para sustituir la tabulación predeterminada. Para usar dos puntos:

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

Entrecomilla los delimitadores que tengan significado para la shell. `paste` puede recorrer varios caracteres delimitadores si la lista contiene más de uno, pero un único carácter es la opción más sencilla al construir dos columnas.

:::single-choice{#paste-colon-delimiter} ¿Qué orden une con dos puntos las líneas correspondientes de `names.txt` y `roles.txt`?

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="La opción `-d` sustituye la tabulación predeterminada por los dos puntos proporcionados entre cada par de campos."}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="La opción `-s` selecciona el modo serial y `:` se trataría como otra ruta de entrada, no como delimitador."}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="Sin `-d`, todos los operandos se tratan como archivos de entrada. Esta orden intentaría abrir un archivo llamado `:`."}
:::

## Serialización de las líneas de un archivo

La opción `-s` procesa cada archivo de entrada en serie y une sus líneas en una sola línea de salida. Crea un archivo con una palabra por línea:

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

Combina `-s` con `-d` para elegir el separador:

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

Si proporcionas varios archivos con `-s`, cada uno se convierte en su propia línea de salida.

:::single-choice{#paste-serialize-with-spaces} ¿Qué orden une todas las líneas de `words.txt` en una única línea separada por espacios?

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="En el modo paralelo predeterminado, un único archivo sigue produciendo una línea de salida por línea de entrada. El delimitador no tiene campos de archivos diferentes que unir."}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="Esta orden serializa dos archivos por separado con la tabulación predeterminada y produce dos líneas de salida, no el resultado solicitado."}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s` serializa las líneas del archivo y `-d ' '` utiliza un espacio entre ellas."}
:::

## Tratamiento de entradas con longitudes distintas

Cuando los archivos de entrada paralelos tienen cantidades de líneas distintas, `paste` continúa hasta terminar el archivo más largo. Los valores ausentes del archivo más corto se convierten en campos vacíos:

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files} ¿Qué ocurre cuando un archivo pasado a `paste` en modo paralelo termina antes que otro?

::option[`paste` utiliza campos vacíos para ese archivo hasta que termina la entrada más larga.]{#paste-empty-fields .correct explanation="El modo paralelo continúa hasta agotar todos los archivos y representa con campos vacíos las líneas ausentes de las entradas más cortas."}
::option[`paste` se detiene de inmediato y descarta las líneas restantes.]{#paste-stop-shortest explanation="`paste` continúa hasta finalizar la entrada más larga, por lo que no descarta las líneas restantes solo porque haya terminado otro archivo."}
::option[`paste` repite el archivo más corto desde el principio.]{#paste-repeat-shorter explanation="La orden no repite los registros de entrada. Una entrada agotada aporta campos vacíos."}
:::

## Lectura de una entrada desde stdin

Utiliza `-` como operando de archivo para leer esa posición desde stdin:

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand} En `producer | paste names.txt -`, ¿qué significa el operando `-`?

::option[Escribir el resultado combinado en stderr.]{#paste-write-stderr explanation="Aquí el guion identifica una fuente de entrada. No redirige ningún flujo de salida."}
::option[Eliminar los delimitadores entre las dos columnas.]{#paste-remove-delimiter explanation="El delimitador se selecciona con `-d`. El guion no cambia el separador."}
::option[Leer esa columna de entrada desde stdin.]{#paste-read-stdin .correct explanation="El guion indica a `paste` que utilice su entrada estándar en esa posición de operando."}
:::

Para practicar la combinación de datos orientados a líneas, prueba este laboratorio:

1. **[Procesamiento sencillo de texto](https://labex.io/es/labs/linux-simple-text-processing-18004)** - Utiliza órdenes como `tr`, `col`, `join` y `paste` para manipular y analizar datos de texto.

## Resumen

Ahora puedes combinar entradas orientadas a líneas con una alineación y unos delimitadores previsibles.

1. Combinar las líneas correspondientes de varios archivos.
2. Sustituir la tabulación predeterminada con `-d`.
3. Serializar las líneas de un archivo con `-s`.
4. Interpretar los campos vacíos de entradas más cortas.
5. Utilizar `-` cuando una entrada proceda de stdin.
