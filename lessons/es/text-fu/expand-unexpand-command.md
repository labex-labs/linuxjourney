---
lesson_id: "expand-unexpand-command"
course_id: "text-fu"
lang: "es"
order_index: 10
title: "expand y unexpand"
description: "Aprende cómo las posiciones de tabulación controlan la conversión entre tabulaciones y espacios con expand y unexpand."
meta_title: "expand y unexpand - Text-Fu"
meta_description: "Domina el formato de texto en Linux con nuestra guía sobre las órdenes expand y unexpand. Aprende a convertir tabulaciones en espacios y espacios en tabulaciones para mantener diseños uniformes."
meta_keywords: "orden expand, orden unexpand, tabulaciones Linux, espacios Linux, formato de texto, tutorial Linux, Linux para principiantes, guía Linux"
---

Las tabulaciones almacenan un desplazamiento hasta una posición de tabulación, no una cantidad fija de espacios visibles. Su anchura mostrada depende de la columna actual y de la configuración de las posiciones de tabulación. Las órdenes `expand` y `unexpand` convierten entre caracteres de tabulación y espacios teniendo en cuenta esas posiciones.

## Convertir tabulaciones en espacios

`expand` lee la entrada, sustituye las tabulaciones por los espacios necesarios para llegar a las posiciones de tabulación correspondientes y escribe el resultado en la salida estándar:

```bash
$ expand sample.txt
```

De forma predeterminada, hay una posición de tabulación cada 8 columnas. Por tanto, una tabulación en la columna 1 se expande de forma distinta que una en la columna 6; no siempre se sustituye por ocho espacios.

:::single-choice{#expand-default-tab-stops}
Con la configuración predeterminada, ¿cómo sustituye `expand` un carácter de tabulación?

::option[Inserta suficientes espacios para llegar a la siguiente posición de tabulación predeterminada.]{#expand-next-stop .correct explanation="`expand` conserva la alineación de las posiciones de tabulación calculando los espacios necesarios desde la columna actual."}
::option[Siempre inserta exactamente ocho espacios.]{#expand-eight-spaces explanation="Las posiciones predeterminadas están separadas por ocho columnas, pero la cantidad de espacios depende de la columna actual."}
::option[Elimina la tabulación sin añadir ningún carácter.]{#expand-remove-tab explanation="La orden sustituye la tabulación por espacios para que el texto posterior permanezca alineado en la posición seleccionada."}
:::

## Elegir las posiciones de tabulación

Usa `-t NUMBER` para colocar posiciones de tabulación cada cantidad especificada de columnas. Para posiciones cada cuatro columnas:

```bash
$ expand -t 4 sample.txt
```

`expand` de GNU también acepta una lista separada por comas de posiciones de tabulación explícitas. Usa `-i` cuando solo deban convertirse las tabulaciones anteriores al primer carácter que no sea un espacio en blanco de cada línea.

:::single-choice{#expand-four-column-stops}
¿Qué orden convierte tabulaciones usando posiciones cada cuatro columnas?

::option[`expand -i 4 sample.txt`]{#expand-initial-four explanation="La opción `-i` limita la conversión a las tabulaciones iniciales y no toma `4` como intervalo entre posiciones."}
::option[`unexpand -t 4 sample.txt`]{#unexpand-tabs-four explanation="`unexpand` convierte espacios apropiados en tabulaciones, la dirección contraria a la operación solicitada."}
::option[`expand -t 4 sample.txt`]{#expand-tabs-four .correct explanation="La opción `-t` establece el intervalo entre posiciones de tabulación y `4` solicita una cada cuatro columnas."}
:::

## Guardar la salida convertida de forma segura

`expand` no edita su archivo de entrada. Redirige la salida estándar a una ruta distinta cuando quieras guardar el texto convertido:

```bash
$ expand sample.txt > result.txt
```

No uses `expand sample.txt > sample.txt`. El shell trunca el destino antes de que `expand` pueda leerlo, por lo que los datos de origen pueden perderse. Después de comprobar un resultado escrito por separado, puedes sustituir deliberadamente el original mediante una operación apropiada de gestión de archivos.

:::single-choice{#expand-safe-output-file}
¿Qué orden guarda el texto expandido sin truncar `sample.txt` antes de leerlo?

::option[`expand sample.txt > sample.txt`]{#expand-same-file explanation="El shell abre y trunca `sample.txt` para la salida antes de iniciar `expand`, lo que puede borrar la entrada."}
::option[`expand sample.txt > result.txt`]{#expand-separate-result .correct explanation="Las rutas de entrada y salida son distintas, por lo que el shell puede crear `result.txt` sin destruir el origen."}
::option[`> sample.txt expand result.txt`]{#expand-leading-redirection explanation="Esto también trunca `sample.txt` y no expresa una conversión segura desde el archivo original."}
:::

## Convertir espacios en tabulaciones

`unexpand` sustituye los espacios que cumplen los requisitos por tabulaciones y conserva la alineación en las posiciones seleccionadas. De forma predeterminada, `unexpand` de GNU solo convierte los espacios en blanco iniciales anteriores al primer carácter que no sea un espacio en blanco de una línea:

```bash
$ unexpand result.txt
```

Usa `-a` para tener en cuenta los espacios apropiados de toda la línea:

```bash
$ unexpand -a result.txt
```

Esto no se limita a sustituir cada grupo de ocho espacios. La conversión depende de las posiciones de las columnas y de las posiciones de tabulación, igual que con `expand`. Usa `-t 4` u otra especificación de posiciones cuando el archivo siga una convención diferente.

:::single-choice{#unexpand-default-scope}
Sin `-a`, ¿qué espacios suele tener en cuenta `unexpand` de GNU para la conversión?

::option[Todos los grupos de espacios de cualquier parte del archivo.]{#unexpand-every-group explanation="Para tener en cuenta los espacios de toda la línea se necesita `-a`, y la conversión sigue dependiendo de las posiciones de tabulación."}
::option[Solo los espacios que aparecen después de la última palabra.]{#unexpand-trailing-blanks explanation="El alcance predeterminado se refiere a los espacios iniciales, no específicamente a los espacios en blanco finales."}
::option[Solo los espacios iniciales anteriores al primer carácter que no sea un espacio en blanco.]{#unexpand-initial-blanks .correct explanation="El comportamiento predeterminado de `unexpand` de GNU se limita al espacio en blanco inicial de cada línea."}
:::

:::single-choice{#unexpand-all-blanks}
¿Qué opción indica a `unexpand` de GNU que también tenga en cuenta los espacios posteriores al primer carácter que no sea un espacio en blanco?

::option[`-i`]{#unexpand-initial-option explanation="Para `expand`, `-i` limita el trabajo a las tabulaciones iniciales. No es la opción de todos los espacios para `unexpand`."}
::option[`-a`]{#unexpand-all-option .correct explanation="La opción `-a` permite convertir los espacios apropiados de toda línea de entrada."}
::option[`-t`]{#unexpand-tab-list-option explanation="La opción `-t` establece posiciones de tabulación. Aunque en GNU puede implicar una conversión más amplia, `-a` solicita explícitamente todos los espacios."}
:::

Ambas órdenes leen de la entrada estándar cuando no se indica ningún archivo, por lo que pueden usarse en tuberías. Recuerda que convertir a espacios y volver a convertir puede no reconstruir la elección original de tabulaciones y espacios, aunque la alineación mostrada no cambie.

## Resumen

Ahora puedes convertir tabulaciones y espacios mientras conservas la alineación de las posiciones de tabulación.

1. Expande las tabulaciones hasta la siguiente posición configurada.
2. Establece posiciones de tabulación personalizadas con `-t`.
3. Guarda la salida en otro archivo antes de sustituir una entrada.
4. Convierte de forma predeterminada los espacios iniciales con `unexpand`.
5. Usa `-a` cuando deban tenerse en cuenta los espacios de toda la línea.
