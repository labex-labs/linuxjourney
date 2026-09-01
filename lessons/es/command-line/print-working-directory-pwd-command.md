---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "es"
order_index: 2
title: "pwd (Imprimir directorio de trabajo)"
description: "Aprende a usar `pwd` para identificar tu ubicación actual en el sistema de archivos de Linux."
meta_title: "pwd (Imprimir Directorio de Trabajo) - Línea de Comandos"
meta_description: "Aprende el comando pwd de Linux, qué significa imprimir el directorio de trabajo y cómo las rutas absolutas muestran tu ubicación actual en el sistema de archivos."
meta_keywords: "comando pwd, linux pwd, imprimir directorio de trabajo, directorio actual linux, ruta absoluta, sistema de archivos linux, árbol de directorios"
---

En Linux, los archivos y directorios están organizados en una jerarquía llamada sistema de archivos. Antes de poder moverte con confianza, necesitas saber dónde estás. El comando `pwd` responde a esa pregunta imprimiendo tu directorio de trabajo actual.

## El árbol de directorios en Linux

Todo el sistema de archivos comienza desde un único directorio de nivel superior llamado directorio raíz, representado por una barra diagonal (`/`). Desde la raíz, el árbol de directorios se ramifica en subdirectorios, que pueden contener archivos y más subdirectorios.

Aquí hay un ejemplo simplificado de cómo se ve esta estructura:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

:::single-choice{#identify-root-subdirectories} En el árbol anterior, ¿qué relación tienen `home` y `etc` con `/`?

::option[Son subdirectorios que parten de `/`.]{#root-subdirectories .correct explanation="Ambos directorios aparecen justo debajo de `/` en el árbol. El sistema de archivos se ramifica en subdirectorios desde su raíz."}
::option[Son archivos almacenados dentro del directorio `bin`.]{#files-inside-bin explanation="El árbol sitúa `home` y `etc` al mismo nivel que `bin`, no dentro de él. En este ejemplo son directorios, no archivos."}
::option[Son nombres alternativos del directorio raíz.]{#alternate-root-names explanation="Linux tiene una sola raíz del sistema de archivos, representada por `/`. `home` y `etc` son directorios situados bajo ella."}
:::

## Cómo entender las rutas de archivos

La ubicación de cualquier archivo o directorio se describe mediante su ruta. Una ruta es una secuencia de directorios que conduce desde un punto de inicio hasta un destino específico.

Por ejemplo, si tienes una carpeta llamada `pete` dentro de `/home`, y una carpeta `Movies` dentro de `pete`, la ruta completa es:

```plaintext
/home/pete/Movies
```

Una ruta que comienza con `/` es una ruta absoluta porque empieza en el directorio raíz. Una ruta como `Movies` es relativa porque depende de tu ubicación actual.

:::single-choice{#recognize-absolute-path} ¿Qué hace que `/home/pete/Movies` sea una ruta absoluta?

::option[Contiene varios nombres de directorio separados por `/`.]{#contains-directories explanation="Tanto las rutas absolutas como las relativas pueden contener varios nombres. El tipo de ruta lo determina su punto de partida, no la cantidad de nombres."}
::option[Termina en un directorio llamado `Movies`.]{#ends-with-movies explanation="El nombre del destino no determina si una ruta es absoluta. Una ruta absoluta se reconoce por su punto de partida en la raíz."}
::option[Comienza en la raíz con una `/` inicial.]{#starts-at-root .correct explanation="Una ruta absoluta comienza en el directorio raíz. La `/` inicial muestra ese punto de partida."}
:::

## ¿Qué significa PWD en Linux?

La forma completa de `pwd` es "print working directory" (imprimir directorio de trabajo). Tu directorio de trabajo es el directorio donde tu shell se encuentra actualmente. Los comandos que usan rutas relativas parten desde esta ubicación.

:::single-choice{#expand-pwd-name} ¿Qué significa `pwd`?

::option[Print working directory]{#print-working-directory .correct explanation="El nombre describe exactamente lo que hace la orden: imprime el directorio de trabajo actual de la shell."}
::option[Present working directory]{#present-working-directory explanation="En una conversación se puede hablar de la ubicación presente, pero esa no es la expansión de `pwd`."}
::option[Print whole directory]{#print-whole-directory explanation="`pwd` muestra la ruta del directorio actual. No imprime todo el contenido del directorio."}
:::

## Uso de la orden pwd

Para encontrar tu directorio actual, escribe `pwd` y presiona Enter.

```bash
$ pwd
/home/pete
```

La salida es una ruta absoluta. En este ejemplo, el shell está actualmente en el directorio personal del usuario `pete`.

La salida exacta puede ser diferente en tu sistema porque quizá cambien el nombre de usuario, el directorio personal o la ubicación actual. La orden `pwd` solo muestra información; no modifica el directorio de trabajo. En cambio, `cd` cambia el directorio donde se encuentra la shell.

:::single-choice{#check-location-without-changing-it} ¿Qué acción comprueba el directorio actual sin cambiarlo?

::option[Ejecutar `cd` y leer el directorio al que se desplaza.]{#run-cd explanation="La orden `cd` cambia el directorio de trabajo. Por tanto, no cumple el requisito de consultar la ubicación sin modificarla."}
::option[Introducir `/home/pete` y utilizar la ruta como una orden.]{#run-path explanation="Una ruta absoluta identifica una ubicación, pero la ruta por sí sola no es la orden que informa del directorio actual."}
::option[Ejecutar `pwd` y leer la ruta absoluta que imprime.]{#run-pwd .correct explanation="`pwd` informa de la ubicación actual de la shell sin desplazarse. Puedes usarlo con seguridad siempre que necesites confirmar dónde estás."}
:::

## Por qué `pwd` es útil

Usa `pwd` cuando:

- Estás siguiendo instrucciones y necesitas confirmar tu ubicación.
- Un comando falló porque una ruta de archivo era incorrecta.
- Te moviste por varios directorios y perdiste la pista de dónde estás.
- Quieres copiar la ruta del directorio actual en otro comando.

Por ejemplo:

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

Esto te dice que `app.py` y `README.md` están ubicados en `/home/pete/projects`.

Para reforzar tu comprensión de la navegación por el sistema de archivos de Linux y de cómo identificar tu ubicación actual, prueba estos laboratorios prácticos:

1. **[Comando pwd de Linux: Mostrar Directorio](https://labex.io/es/labs/linux-linux-pwd-command-directory-displaying-209734)** - Este laboratorio ofrece una visión enfocada y uso práctico del comando `pwd`, alineado directamente con la introducción de la lección para encontrar tu directorio actual.
2. **[Navegación de Directorios en Linux](https://labex.io/es/labs/linux-directory-navigation-387844)** - Pon a prueba tus habilidades básicas en la línea de comandos de Linux navegando por varios directorios, solidificando tu comprensión de rutas y la estructura del sistema de archivos.
3. **[Comando cd de Linux: Cambiar Directorio](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Aprende a navegar eficientemente tu sistema de archivos usando el comando `cd`, entendiendo diferentes técnicas para cambiar de directorio y explorar la estructura de archivos.

## Resumen

Ahora puedes utilizar `pwd` para identificar tu ubicación actual en el sistema de archivos de Linux.

1. Reconocer la raíz del árbol de directorios.
2. Distinguir una ruta absoluta de una ruta relativa.
3. Explicar qué significa `pwd` y qué información muestra.
4. Consultar el directorio de trabajo sin cambiarlo.
