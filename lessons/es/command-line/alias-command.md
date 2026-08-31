---
lesson_id: "alias-command"
course_id: "command-line"
lang: "es"
order_index: 18
title: "alias"
description: "Aprende a crear, inspeccionar, guardar, omitir y eliminar alias de órdenes en Bash."
meta_title: "alias - Línea de Comandos"
meta_description: "Aprende el comando alias en Linux con ejemplos para crear alias temporales, guardar alias en .bashrc, listar alias y eliminarlos con unalias."
meta_keywords: "comando alias linux, comando alias, alias bash, alias .bashrc, comando unalias, atajo de comando linux, alias de shell"
---

Un alias indica a una shell interactiva que sustituya una palabra de orden por otra cadena antes de ejecutar la línea. Puede abreviar una orden frecuente o proporcionar un conjunto de opciones preferido.

## Creación de un alias en la shell actual

Para crear un alias temporal que dure solo durante tu sesión actual de terminal, simplemente especifica un nombre y asígnale la cadena del comando.

Por ejemplo, crea un alias llamado `ll` para `ls -la`:

```bash
$ alias ll='ls -la'
```

Después de esta definición, introducir `ll` como orden se expande a `ls -la`. Las comillas mantienen unida la sustitución al definir el alias.

Los alias son adecuados para sustituciones sencillas del prefijo de una orden. Utiliza una función de shell cuando necesites procesar argumentos de una forma más estructurada.

:::single-choice{#define-ll-alias}
¿Qué orden de Bash define `ll` como alias de `ls -la` en la shell actual?

::option[`alias ll = 'ls -la'`]{#alias-spaces explanation="Los espacios alrededor de `=` dividen la definición en varias palabras, por lo que Bash no recibe una asignación de alias válida."}
::option[`alias ll='ls -la'`]{#alias-ll .correct explanation="Esta orden utiliza la forma obligatoria `NAME=REPLACEMENT` y entrecomilla la sustitución que contiene un espacio."}
::option[`unalias ll='ls -la'`]{#unalias-definition explanation="`unalias` elimina nombres de alias existentes. No crea una sustitución."}
:::

## Carga de un alias en futuras sesiones de Bash

Un alias definido en el prompt pertenece a la shell actual y desaparece cuando esta termina. Las sesiones interactivas de Bash que no son de inicio de sesión suelen leer `~/.bashrc`, por lo que ese archivo es el lugar habitual para los alias personales:

```bash
alias ll='ls -la'
```

Después de editar el archivo, inicia una nueva sesión interactiva de Bash o vuelve a cargarlo en la shell actual:

```bash
$ source ~/.bashrc
```

El comportamiento de inicio puede variar según la shell, el modo de inicio de sesión y la configuración de la distribución. Un usuario de Zsh, por ejemplo, utilizaría normalmente la configuración de Zsh en vez del archivo `.bashrc` de Bash.

:::single-choice{#persist-bash-alias}
¿Dónde debe definirse normalmente un alias personal para que lo carguen las futuras sesiones interactivas de Bash que no sean de inicio de sesión?

::option[En el archivo `~/.bashrc` del usuario.]{#bashrc-alias .correct explanation="Las sesiones interactivas de Bash que no son de inicio de sesión suelen leer `~/.bashrc`, por lo que es el lugar convencional para los alias personales."}
::option[En el archivo ejecutable utilizado por la orden con alias.]{#edit-executable explanation="Modificar un ejecutable instalado no está relacionado con la expansión de alias y puede dañar archivos gestionados por el sistema."}
::option[En el historial de desplazamiento de la terminal actual.]{#terminal-scrollback explanation="El historial de desplazamiento solo conserva texto mostrado. Bash no lo ejecuta como configuración de inicio."}
:::

## Inspección de alias y resolución de nombres

Ejecuta `alias` sin argumentos para listar los alias en tu shell actual.

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Usa `type NAME` para ver qué se ejecutará cuando ingreses un comando:

```bash
$ type ll
ll is aliased to 'ls -la'
```

:::single-choice{#inspect-command-alias}
¿Qué orden muestra si Bash resuelve actualmente `ll` como alias, función, orden integrada o ejecutable?

::option[`file ll`]{#file-ll explanation="`file` clasifica una ruta del sistema de archivos. Un alias existe en el estado de la shell y no tiene por qué corresponder a un archivo llamado `ll`."}
::option[`type ll`]{#type-ll .correct explanation="La orden integrada `type` informa de cómo resuelve la sesión actual de Bash el nombre `ll`."}
::option[`whatis ll`]{#whatis-ll explanation="`whatis` consulta descripciones de páginas del manual. Los alias personales normalmente no tienen ninguna entrada en esa base de datos."}
:::

## Omisión y eliminación de un alias

Para omitir un alias en una sola línea, antepón una barra invertida al nombre de la orden o colócalo después de la orden integrada `command` de Bash:

```bash
$ \ls
$ command ls
```

Esto resulta útil cuando necesitas el comportamiento normal de la orden subyacente. Mantén los alias breves y previsibles, y evita ocultar comportamientos sorprendentes o destructivos tras nombres conocidos.

:::single-choice{#bypass-ls-alias}
La sesión actual de Bash tiene un alias llamado `ls`. ¿Qué orden omite ese alias en una sola invocación?

::option[`alias ls`]{#show-ls-alias explanation="Esta orden muestra la definición del alias `ls`. No invoca la orden subyacente."}
::option[`command ls`]{#command-ls .correct explanation="Como `command` es la palabra de orden, Bash no expande el `ls` siguiente como alias y aplica la resolución normal de órdenes."}
::option[`source ls`]{#source-ls explanation="`source` lee un archivo como código de shell en la sesión actual. No es una forma segura ni apropiada de omitir un alias."}
:::

Elimina un alias de la shell actual con `unalias`:

```bash
$ unalias ll
```

Si la definición permanece en `~/.bashrc`, una shell futura puede volver a crearla. Elimina o modifica también esa línea de configuración cuando quieras retirar el alias de forma permanente.

:::single-choice{#remove-current-alias}
¿Qué orden elimina el alias `ll` de la sesión actual de Bash?

::option[`unalias ll`]{#unalias-ll .correct explanation="`unalias` elimina el alias indicado de la tabla de alias de la shell actual."}
::option[`alias ll=''`]{#empty-ll explanation="Esta orden sustituye el alias por una expansión vacía, pero no elimina su definición."}
::option[`command ll`]{#command-ll explanation="`command` puede omitir la expansión de alias en esa línea, pero no elimina el alias del estado de la shell."}
:::

## Resumen

Ahora puedes personalizar Bash con alias sencillos que se pueden inspeccionar.

1. Definir un alias temporal con las comillas correctas.
2. Cargar alias personales desde `~/.bashrc` en sesiones futuras.
3. Inspeccionar alias y la resolución de órdenes.
4. Omitir un alias durante una sola invocación.
5. Eliminar las definiciones activa y guardada cuando sea necesario.
