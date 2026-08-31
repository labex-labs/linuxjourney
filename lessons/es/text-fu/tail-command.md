---
lesson_id: "tail-command"
course_id: "text-fu"
lang: "es"
order_index: 9
title: "tail"
description: "Aprende a ver el final de una entrada y a seguir archivos a medida que se añade contenido nuevo."
meta_title: "tail - Text-Fu"
meta_description: "Una guía de Linux para principiantes sobre la orden tail. Aprende a usar tail para ver el final de los archivos y supervisar registros en tiempo real con la opción tail -f."
meta_keywords: "orden tail, Linux tail, tail -f, ver registros, supervisar registros, tutorial Linux, Linux para principiantes, guía Linux, supervisión de archivos"
---

La orden `tail` muestra el final de un archivo o flujo de entrada. También puede permanecer activa y mostrar los datos que se añaden a un archivo, lo que resulta útil para observar registros.

## Mostrar las últimas diez líneas

Sin una opción de cantidad, `tail` imprime las últimas 10 líneas de cada archivo indicado:

```bash
$ tail application.log
```

Si el archivo contiene menos de 10 líneas, se imprimen todas las disponibles. El archivo en sí no se modifica.

:::single-choice{#tail-default-lines}
¿Qué muestra `tail application.log` de forma predeterminada?

::option[Hasta las 10 primeras líneas del archivo.]{#tail-first-ten explanation="`head` selecciona el principio de un archivo. `tail` trabaja desde el final."}
::option[Todas las líneas añadidas después de iniciar la orden.]{#tail-follow-only explanation="El seguimiento continuo requiere `-f` o una opción relacionada. `tail` sin opciones imprime una instantánea y termina."}
::option[Hasta las 10 últimas líneas del archivo.]{#tail-last-ten .correct explanation="Sin una opción de cantidad, `tail` selecciona las diez últimas líneas, o todas si hay menos."}
:::

## Elegir una cantidad de líneas o bytes

Usa `-n NUMBER` para seleccionar otra cantidad de líneas finales:

```bash
$ tail -n 20 application.log
```

Usa `-c NUMBER` cuando necesites los bytes finales:

```bash
$ tail -c 100 payload.bin
```

El modo de bytes puede comenzar en mitad de una línea de texto o de un carácter codificado, por lo que el modo de líneas suele ser más claro para texto.

:::single-choice{#tail-twenty-lines}
¿Qué orden muestra las 20 últimas líneas de `application.log`?

::option[`tail -n 20 application.log`]{#tail-twenty-end .correct explanation="La opción `-n` selecciona una cantidad de líneas y `tail` las toma desde el final."}
::option[`head -n 20 application.log`]{#head-twenty-start explanation="Esto selecciona 20 líneas desde el principio, no desde el final."}
::option[`tail -c 20 application.log`]{#tail-twenty-bytes explanation="La opción `-c` selecciona los 20 bytes finales, que no equivalen a 20 líneas."}
:::

## Comenzar en una línea concreta

Una cantidad precedida por `+` cambia el significado: `tail -n +N` comienza en la línea N e imprime hasta el final.

```bash
$ tail -n +5 report.txt
```

Esto omite las cuatro primeras líneas y comienza en la línea 5. Resulta útil para eliminar de un flujo una cantidad conocida de líneas de cabecera.

:::single-choice{#tail-start-line-five}
¿Qué orden imprime `report.txt` a partir de la línea 5?

::option[`tail -n +5 report.txt`]{#tail-from-five .correct explanation="La cantidad `+5` indica a `tail` que comience en la línea 5 y continúe hasta el final."}
::option[`tail -n 5 report.txt`]{#tail-final-five explanation="Sin el signo más, esto selecciona las cinco últimas líneas, independientemente de sus números de línea absolutos."}
::option[`head -n +5 report.txt`]{#head-plus-five explanation="Esta no es la forma de `tail` para comenzar en una línea. Usa `tail -n +5` para el intervalo solicitado."}
:::

## Seguir los datos añadidos

Con `-f`, `tail` imprime el final inicial y permanece activa, mostrando los datos a medida que se añaden:

```bash
$ tail -f application.log
```

Pulsa `Ctrl+C` para interrumpir `tail` y volver al shell. Seguir un archivo solo muestra contenido nuevo; no garantiza que la aplicación que produce el registro funcione correctamente ni que todos los eventos relevantes usen ese archivo.

:::single-choice{#tail-follow-file}
¿Qué orden muestra el final actual de `application.log` y continúa esperando contenido añadido?

::option[`tail -f application.log`]{#tail-follow-app .correct explanation="La opción `-f` mantiene `tail` activa y muestra los datos añadidos al archivo."}
::option[`tail -n 0 application.log`]{#tail-zero-lines explanation="Esto no imprime ninguna línea al principio y termina porque no incluye una opción de seguimiento."}
::option[`less application.log`]{#less-log explanation="`less` permite navegar de forma interactiva, pero esta forma no permanece en un modo de seguimiento como el de `tail`."}
:::

## Seguir por nombre un registro rotado

La rotación de registros puede cambiar el nombre del archivo antiguo y crear uno nuevo en la ruta original. En GNU, `tail -F` equivale a seguir por nombre y reintentar, por lo que puede volver a abrir un archivo que se haya sustituido o que falte temporalmente:

```bash
$ tail -F application.log
```

Usa `-f` cuando quieras seguir el archivo abierto actualmente y `-F` cuando esperes que un registro identificado por su nombre rote. Estos son comportamientos de GNU; otras implementaciones pueden diferir.

:::single-choice{#tail-follow-rotated-name}
En GNU/Linux, ¿qué opción es más adecuada para seguir `application.log` durante una rotación habitual que cambia el nombre y vuelve a crear el archivo?

::option[`-n`]{#tail-rotation-lines explanation="La opción `-n` cambia la cantidad de líneas mostradas. No vuelve a intentar abrir una ruta sustituida."}
::option[`-c`]{#tail-rotation-bytes explanation="La opción `-c` cambia la unidad de selección a bytes. No proporciona un seguimiento compatible con la rotación."}
::option[`-F`]{#tail-follow-name .correct explanation="En GNU, `-F` sigue por nombre y reintenta, lo que permite que `tail` vuelva a abrir un registro sustituido o ausente temporalmente."}
:::

Cuando no se indica ningún archivo, `tail` lee de la entrada estándar, por lo que puede seleccionar el final de la salida de una orden. Varios archivos indicados reciben cabeceras identificativas de forma predeterminada, como ocurre con `head`.

Para practicar cómo ver y seguir el final de los archivos, prueba estos laboratorios prácticos:

1. **[Orden tail de Linux: mostrar el final de un archivo](https://labex.io/labs/linux-linux-tail-command-file-end-display-214303)** - Aprende a usar la orden `tail` de Linux para ver y supervisar el final de archivos de texto, incluida la opción `-f` para actualizaciones en tiempo real.
2. **[Visualización de archivos de registro y configuración en Linux](https://labex.io/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practica el uso de `tail` (junto con `cat` y `more`) para ver y recorrer eficazmente archivos de registro y configuración, algo fundamental para supervisar el sistema.
3. **[Detección rápida de amenazas](https://labex.io/labs/linux-rapid-threat-detection-387930)** - Aplica tus conocimientos de `tail` para extraer y analizar rápidamente entradas recientes de registros, simulando una detección rápida de amenazas en un contexto de ciberseguridad.

## Resumen

Ahora puedes inspeccionar el final de los archivos y observar el contenido recién añadido con `tail`.

1. Muestra las diez últimas líneas de forma predeterminada.
2. Selecciona explícitamente una cantidad de líneas o bytes.
3. Comienza la salida en una línea numerada con `-n +N`.
4. Sigue el contenido añadido con `-f` y detén la orden con `Ctrl+C`.
5. Usa `-F` de GNU cuando un registro identificado por su nombre pueda rotar.
