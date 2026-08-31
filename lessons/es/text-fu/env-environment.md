---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "es"
order_index: 5
title: "env (Entorno)"
description: "Aprende cómo expande, exporta, inspecciona y sustituye temporalmente Bash las variables de entorno."
meta_title: "env (Entorno) - Text-Fu"
meta_description: "Explora qué hace el comando env en Linux. Esta guía explica cómo ver y usar variables de entorno de Linux como PATH, HOME y USER con el comando env de Linux."
meta_keywords: "env, env linux, env comando linux, qué hace env en linux, variables de entorno, variable PATH, variables de shell"
---

Cada proceso tiene un entorno: una colección de cadenas de nombre y valor heredadas de su proceso padre. Las shells utilizan variables de entorno para transmitir a los programas que inician configuraciones como el idioma o las rutas de búsqueda de ejecutables.

## Expansión de valores de variables en Bash

Bash expande `$NAME` o `${NAME}` al valor de una variable antes de ejecutar una orden. Entrecomilla la expansión para conservar el valor como un único argumento:

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

Algunas variables de entorno habituales son:

- `HOME`: Ruta del directorio personal del usuario actual.
- `USER`: Nombre de usuario proporcionado por el entorno de inicio de sesión en muchos sistemas.
- `PWD`: Directorio de trabajo actual de la shell.
- `PATH`: Directorios en los que se buscan nombres de órdenes.

Los valores dependen del entorno del proceso actual; no son constantes universales. Una variable no definida se expande a una cadena vacía, salvo que se active un comportamiento más estricto de la shell.

:::single-choice{#env-print-home-value}
¿Qué orden de Bash muestra el valor de `HOME` y lo conserva como un único argumento?

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="Las comillas simples impiden la expansión de parámetros, por lo que se muestran los caracteres literales `$HOME`."}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="Bash expande `$HOME` dentro de las comillas dobles y `printf` recibe el valor completo como un único argumento."}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="Sin el signo de dólar ni otra sintaxis de parámetros, `HOME` es texto ordinario, no una expansión de variable."}
:::

## Inspección del entorno actual

Ejecuta `env` sin operandos para mostrar el entorno heredado por ese proceso `env`:

```bash
$ env
```

La salida contiene registros `NAME=value`, por ejemplo:

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

Las variables de entorno pueden contener credenciales, tokens, rutas internas u otros datos sensibles. No pegues toda la salida de `env` en incidencias o registros públicos sin revisarla y ocultar los datos necesarios.

:::single-choice{#env-list-exported-values}
¿Qué orden muestra el entorno visible para un proceso recién iniciado?

::option[`env`]{#env-print-all .correct explanation="Sin una orden ni asignaciones, `env` muestra el entorno de nombres y valores que ha recibido."}
::option[`alias`]{#env-alias-list explanation="`alias` enumera definiciones de alias, que forman parte del estado de la shell y no de los registros de entorno exportados."}
::option[`history`]{#env-history-list explanation="`history` muestra las líneas de órdenes recordadas por la shell. No enumera variables exportadas."}
:::

## Búsqueda de órdenes mediante PATH

`PATH` es una lista de directorios separados por dos puntos que Bash recorre cuando el nombre de una orden no contiene ninguna barra:

```bash
$ printf '%s\n' "$PATH"
```

El orden importa: Bash utiliza la primera orden adecuada que encuentra según sus reglas de resolución. Utiliza `type -a NAME` para inspeccionar cómo resuelve la shell actual un nombre.

Para añadir `/opt/coolapp/bin` a la shell actual y a sus futuros procesos hijo sin perder la ruta existente:

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

No sustituyas accidentalmente `PATH` por un único directorio nuevo ni añadas directorios no fiables con permisos de escritura. Cualquiera de esos errores puede impedir encontrar órdenes normales o hacer que se ejecute un programa inesperado.

:::single-choice{#env-prepend-path-directory}
¿Qué orden añade `/opt/coolapp/bin` antes del `PATH` existente para el proceso actual de Bash y sus futuros hijos?

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="Esta orden descarta todos los directorios de búsqueda existentes, lo que puede dificultar encontrar órdenes normales."}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="Esta orden antepone el directorio nuevo, conserva el valor anterior y exporta el resultado a los procesos hijo."}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="Las comillas simples conservan el texto literal `$PATH` y la asignación no se exporta a futuros procesos hijo."}
:::

## Exportación de una variable a procesos hijo

Las variables de Bash no forman parte automáticamente del entorno entregado a los procesos hijo. Marca un nombre para exportarlo con `export`:

```bash
$ export TEST=test
```

El proceso actual de Bash tiene ahora una variable llamada `TEST`, y las órdenes que inicie heredarán `TEST=test`. Un proceso hijo no puede utilizar este mecanismo para modificar el entorno de su padre.

```bash
$ printenv TEST
test
```

La asignación suele durar hasta que elimines la variable o termine la shell. No modifica el entorno de todo el sistema.

:::single-choice{#env-export-inheritance}
¿Cuál es el efecto principal de `export TEST=test` en Bash?

::option[Escribe `TEST` en la configuración del sistema de todos los usuarios.]{#env-system-wide explanation="La asignación afecta a la shell actual y a la herencia de sus hijos, no a todos los usuarios ni al sistema operativo completo."}
::option[Marca `TEST=test` para que lo hereden los futuros procesos hijo.]{#env-child-inheritance .correct explanation="`export` añade la variable de la shell al entorno que Bash pasa a las órdenes que inicia."}
::option[Cambia el entorno de procesos que ya están en ejecución.]{#env-existing-processes explanation="Los procesos existentes conservan sus propios entornos. La exportación afecta a los procesos que se inicien después."}
:::

## Asignación de un valor para una sola orden

Coloca asignaciones antes de una orden para proporcionar valores únicamente a su entorno:

```bash
$ LANG=C sort names.txt
```

El valor de `LANG` de la shell actual no cambia de forma permanente. La utilidad `env` ofrece otra forma explícita:

```bash
$ env LANG=C sort names.txt
```

Utiliza `env -i COMMAND` para iniciar una orden con un entorno inicialmente vacío y añade después las asignaciones necesarias. Muchos programas dependen de valores del entorno, así que usa esta opción deliberadamente.

:::single-choice{#env-one-command-value}
¿Qué orden ejecuta `sort names.txt` con `LANG=C` sin cambiar de forma permanente el valor de `LANG` de la shell actual?

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env` añade la asignación al entorno de la orden que inicia, mientras que la shell padre conserva su valor anterior."}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="Esta orden exporta `LANG=C` en la shell actual y deja el valor cambiado después de que termine `sort`."}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="Esta orden comienza con un entorno vacío, pero no establece el valor `LANG=C` solicitado."}
:::

## Carga de valores personales en futuras sesiones

Para volver a crear una variable exportada en futuras sesiones interactivas de Bash, coloca una línea `export` adecuada en el archivo de inicio que esas sesiones lean; para sesiones interactivas de Bash que no son de inicio, suele ser `~/.bashrc`:

```bash
export TEST=test
```

Zsh suele utilizar `~/.zshrc`, mientras que Fish emplea otra sintaxis y configuración. Las shells de inicio de sesión y las no interactivas pueden leer archivos diferentes, así que identifica la shell y el tipo de sesión en vez de suponer que un único archivo configura todos los procesos.

Para practicar la herencia del entorno y la configuración de la shell, prueba estos laboratorios:

1. **[Administrar el entorno y la configuración de la shell en Linux](https://labex.io/es/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - Practica la creación y gestión de variables locales y de entorno, su herencia y su persistencia mediante `.bashrc`.
2. **[Variables de entorno en Linux](https://labex.io/es/labs/linux-environment-variables-in-linux-385274)** - Aprende a crear, modificar y gestionar variables de entorno y comprende su papel en la configuración del sistema.

## Resumen

Ahora puedes inspeccionar y controlar el entorno que Bash transmite a los procesos hijo.

1. Expandir valores de variables con comillas deliberadas.
2. Revisar valores exportados sin exponer secretos.
3. Conservar y ordenar los directorios de órdenes en `PATH`.
4. Exportar una variable de la shell a futuros procesos hijo.
5. Sustituir un valor para una sola orden sin cambiar la shell padre.
