---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "es"
order_index: 13
title: "tr (traducir)"
description: "Aprende a traducir, eliminar y comprimir conjuntos de caracteres de un flujo de entrada estándar."
meta_title: "tr (traducir) - Text-Fu"
meta_description: "Aprende la orden tr de Linux con ejemplos para traducir y eliminar caracteres, comprimir repeticiones, usar clases de caracteres y limpiar texto."
meta_keywords: "orden tr Linux, orden tr, tr -d, tr -s, traducir caracteres, eliminar caracteres, clases de caracteres, procesamiento de texto Linux"
---

La orden `tr`, abreviatura de *translate* (traducir), traduce, elimina o comprime caracteres leídos de la entrada estándar. No acepta operandos normales de archivo de entrada, así que proporciona los datos mediante una tubería o una redirección de entrada.

La sintaxis básica es:

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr` trabaja con conjuntos de caracteres, no con palabras ni expresiones regulares generales. Usa otra herramienta cuando una transformación dependa de una palabra completa, de la estructura de una línea o del contexto circundante.

## Traducir caracteres

Con dos conjuntos, los caracteres de `SET1` se corresponden por posición con los de `SET2`:

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

Aquí, las posiciones del intervalo de minúsculas se corresponden con las del intervalo de mayúsculas. Pon entre comillas las expresiones de conjuntos para que el shell las entregue sin cambios.

También puedes traducir un carácter a otro:

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

Los caracteres que no están en `SET1` pasan sin cambios.

:::single-choice{#tr-map-characters} ¿Qué imprime `printf '%s\n' 'abc123' | tr 'abc' 'ABC'`?

::option[`ABCABC`]{#tr-uppercase-digits explanation="Los dígitos no pertenecen al conjunto de origen, por lo que `tr` no los sustituye por letras."}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="Cada uno de `a`, `b` y `c` se corresponde con el carácter de la misma posición en `ABC`; los dígitos no cambian."}
::option[`abc123ABC`]{#tr-append-set explanation="`tr` traduce los caracteres coincidentes de la entrada. No añade el conjunto de destino al flujo."}
:::

## Eliminar caracteres

Usa `-d` con un conjunto para eliminar cada carácter coincidente:

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

Cada dígito se elimina de forma independiente; `tr` no identifica un token numérico completo.

Las clases de caracteres pueden describir grupos definidos por la configuración regional actual:

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

Eliminar los saltos de línea une las líneas de entrada sin insertar un separador de reemplazo:

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

:::single-choice{#tr-delete-digits} ¿Qué orden elimina todos los dígitos de la entrada estándar y deja sin cambios los demás caracteres?

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="La opción `-d` elimina del flujo de entrada todos los caracteres de la clase de dígitos."}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="La opción `-s` comprime los dígitos repetidos, pero deja un carácter de cada secuencia."}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="La traducción suele necesitar un segundo conjunto. Un conjunto por sí solo no solicita la eliminación."}
:::

## Comprimir caracteres repetidos

Usa `-s SET` para sustituir cada secuencia de un carácter indicado por una sola aparición de ese carácter:

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

Este conjunto contiene un espacio normal, por lo que esa orden no comprime tabulaciones ni saltos de línea.

También puedes comprimir saltos de línea repetidos:

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

:::single-choice{#tr-squeeze-spaces} ¿Qué orden reduce cada secuencia de espacios normales de la entrada estándar a un solo espacio?

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="La opción `-s` comprime los miembros repetidos del conjunto proporcionado, que contiene un espacio normal."}
::option[`tr -d ' '`]{#tr-delete-space explanation="La opción `-d` elimina todos los espacios normales en vez de conservar uno por secuencia."}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="Un conjunto de traducción vacío no es la forma clara y portable de solicitar una compresión. Usa `-s` para caracteres repetidos."}
:::

## Usar clases de caracteres y complementos

En muchas configuraciones regionales, las clases de caracteres expresan la intención con mayor claridad que los intervalos escritos a mano. Entre las clases habituales se encuentran:

- `[:lower:]`: letras minúsculas.
- `[:upper:]`: letras mayúsculas.
- `[:digit:]`: dígitos.
- `[:alpha:]`: letras.
- `[:alnum:]`: letras y dígitos.
- `[:space:]`: caracteres de espacio en blanco.
- `[:punct:]`: caracteres de puntuación.

Por ejemplo, convierte texto en minúsculas a mayúsculas con clases de caracteres:

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

La opción `-c` complementa `SET1`, es decir, representa todos los caracteres que no están en el conjunto. Combínala con `-d` para conservar solo ciertos tipos de caracteres:

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

Esto también elimina el salto de línea porque no es alfanumérico. Añade o conserva separadores de forma deliberada cuando los límites de los registros sean importantes.

:::single-choice{#tr-keep-alphanumeric} ¿Qué hace `tr -cd '[:alnum:]'` con la entrada estándar?

::option[Elimina los caracteres alfanuméricos y conserva todos los demás.]{#tr-delete-alnum explanation="El complemento cambia los caracteres a los que se dirige `-d`. El propio conjunto alfanumérico se conserva."}
::option[Elimina todos los caracteres que no son alfanuméricos.]{#tr-delete-nonalnum .correct explanation="`-c` complementa el conjunto alfanumérico y `-d` elimina el conjunto resultante de caracteres no alfanuméricos."}
::option[Convierte todas las letras y dígitos a mayúsculas.]{#tr-uppercase-alnum explanation="No hay ningún conjunto de traducción de destino, por lo que esta orden no convierte mayúsculas y minúsculas."}
:::

## Construir transformaciones de flujos

Se pueden conectar varios procesos `tr` cuando las transformaciones resulten más claras como etapas separadas:

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

Para una entrada sencilla separada por tabulaciones, traduce los caracteres de tabulación a comas:

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

Como `tr` lee de la entrada estándar, se puede proporcionar un archivo mediante `<`:

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

Redirige la salida estándar a otro archivo si necesitas guardar el resultado. No la redirijas a la ruta de entrada, porque el shell la truncaría antes de que `tr` pudiera leerla.

:::single-choice{#tr-read-file-input} ¿Qué orden hace que `tr` lea `names.txt` como entrada estándar y convierta los caracteres en minúsculas a mayúsculas?

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr` no acepta un nombre de archivo de entrada normal de este modo; el operando adicional hace que la sintaxis no sea válida."}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="Esto lee el archivo correctamente, pero elimina las letras minúsculas en vez de traducirlas."}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="El shell abre `names.txt` en la entrada estándar y `tr` asigna la clase de minúsculas a la de mayúsculas."}
:::

Para practicar transformaciones de flujos carácter por carácter, prueba este laboratorio práctico:

1. **[Orden tr de Linux: traducción de caracteres](https://labex.io/labs/linux-linux-tr-command-character-translating-219198)** - Aprende a usar `tr` para transformar caracteres en flujos de texto. Practicarás la traducción y eliminación de caracteres concretos, las clases de caracteres y la compresión de caracteres repetidos.

## Resumen

Ahora puedes transformar flujos de caracteres mediante operaciones específicas de `tr`.

1. Asigna caracteres entre conjuntos correspondientes.
2. Elimina caracteres seleccionados con `-d`.
3. Comprime caracteres repetidos con `-s`.
4. Usa deliberadamente clases dependientes de la configuración regional y complementos.
5. Proporciona la entrada mediante la entrada estándar, no como un operando de nombre de archivo.
