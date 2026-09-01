---
lesson_id: "history-command"
course_id: "command-line"
lang: "es"
order_index: 9
title: "history"
description: "Aprende a inspeccionar, buscar, reutilizar y gestionar el historial de órdenes en Bash."
meta_title: "history - Línea de Comandos"
meta_description: "Aprende el comando history de Linux con ejemplos para ver el historial de comandos, volver a ejecutar comandos, búsqueda inversa, eliminar entradas y limpiar la terminal."
meta_keywords: "comando history linux, historial bash, history -c, history -d, history -w, Ctrl-R, historial de comandos, comando clear"
---

Las shells interactivas pueden conservar un registro de las órdenes que introduces. Esta lección se centra en Bash, donde la orden integrada `history` muestra y gestiona ese registro. Otras shells pueden utilizar atajos, archivos o configuraciones diferentes.

## Visualización del historial de Bash

Para ver la lista de comandos que has usado, escribe `history`.

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Cada línea tiene un número de historial seguido por el comando.

:::single-choice{#show-command-history} ¿Qué orden de Bash muestra la lista numerada del historial actual?

::option[`clear`]{#clear-display explanation="`clear` renueva el área visible de la terminal. No muestra las órdenes anteriores."}
::option[`history -w`]{#write-history explanation="`history -w` escribe la lista actual en el archivo de historial. Su finalidad es guardarla, no mostrarla."}
::option[`history`]{#show-history .correct explanation="La orden integrada `history` imprime las órdenes de la lista actual, normalmente acompañadas de sus números de historial."}
:::

## Reutilización de órdenes anteriores

El shell ofrece varios atajos para facilitar la reejecución de comandos.

- **`Up Arrow`**: recupera órdenes anteriores para revisarlas o editarlas.
- **`!!`**: Expande y ejecuta la orden más reciente.
- **Ejecutar por número**: Usa `!102` para ejecutar el comando número 102 de tu historial.
- **Ejecutar por prefijo**: Usa `!cat` para ejecutar el comando más reciente que comenzó con `cat`.

Las expansiones del historial que empiezan por `!` pueden ejecutar una orden en cuanto pulses Enter. Si existe alguna duda, inspecciona primero la coincidencia, sobre todo antes de añadir privilegios elevados o actuar sobre archivos importantes.

:::single-choice{#repeat-most-recent-command} ¿Qué expansión del historial de Bash repite la orden ejecutada más recientemente?

::option[`!102`]{#event-number explanation="Esta expansión selecciona la orden con el número de historial 102. Esa entrada no tiene por qué ser la más reciente."}
::option[`!cat`]{#event-prefix explanation="Esta expansión selecciona la orden más reciente cuyo texto empiece por `cat`. No significa la orden más reciente de cualquier tipo."}
::option[`!!`]{#previous-event .correct explanation="En Bash, `!!` se expande a la orden anterior y la ejecuta al enviar la línea."}
:::

## Búsqueda interactiva en el historial

Uno de los atajos más poderosos del historial es `Ctrl-R`. Esto inicia una búsqueda inversa. Después de presionar `Ctrl-R`, comienza a escribir cualquier parte del comando que buscas, y el shell mostrará la coincidencia más reciente. Puedes presionar `Ctrl-R` repetidamente para recorrer coincidencias más antiguas. Una vez que encuentres el comando que quieres, solo presiona Enter para ejecutarlo.

Si quieres editar el comando encontrado antes de ejecutarlo, presiona la tecla de flecha derecha o izquierda en lugar de Enter.

:::single-choice{#search-before-executing} Recuerdas una parte de una orden anterior de Bash y quieres encontrarla de forma interactiva. ¿Qué debes pulsar primero?

::option[`Ctrl+D`]{#end-input explanation="`Ctrl+D` señala el fin de la entrada en muchos contextos de terminal y puede cerrar una shell inactiva. No inicia una búsqueda en el historial."}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C` suele interrumpir o cancelar la operación actual. No busca en el historial de órdenes."}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R` inicia una búsqueda incremental inversa en el historial. Escribir más caracteres reduce las coincidencias."}
:::

## Gestión de la lista del historial

Más allá de solo ver tu historial, también puedes gestionarlo directamente.

- **Borrar la lista de historial actual**: `history -c` elimina todas las entradas de la lista de historial en memoria.
- **Guardar el historial en un archivo**: `history -w` guarda el historial de la sesión actual en tu archivo de historial, usualmente `~/.bash_history`.
- **Eliminar una entrada específica**: `history -d <offset>` elimina un comando por su número de historial.

Ejemplos:

```bash
$ history -d 101
$ history -w
```

Vaciar la lista en memoria no garantiza por sí solo que las órdenes anteriores hayan desaparecido de todos los archivos, copias de seguridad u otras shells activas. El comportamiento también depende de la configuración de Bash y del momento en que las sesiones leen o escriben sus archivos.

:::single-choice{#save-current-history-list} ¿Qué orden escribe la lista actual del historial de Bash en su archivo configurado?

::option[`history -c`]{#clear-current-list explanation="La opción `-c` vacía la lista en memoria. No solicita guardar la lista actual."}
::option[`history -d 101`]{#delete-one-entry explanation="La opción `-d` elimina una entrada seleccionada del historial. No guarda la lista completa."}
::option[`history -w`]{#write-current-list .correct explanation="La opción `-w` escribe la lista actual del historial en el archivo configurado."}
:::

## Limpieza de la pantalla y autocompletado de nombres

A medida que tu ventana de terminal se llena, puede que quieras limpiarla. Usa el comando `clear` para borrar tu pantalla y comenzar con una pantalla limpia.

```bash
$ clear
```

Esto no borra la lista del historial de Bash. Según la terminal, el contenido anterior también puede seguir disponible al desplazarte hacia arriba.

El autocompletado con Tab evita volver a escribir. Empieza una orden o un nombre de archivo o directorio y pulsa Tab. Bash puede completar una coincidencia inequívoca o mostrar las posibilidades si existe más de una.

Las líneas de órdenes pueden guardarse en el historial, así que no introduzcas contraseñas, tokens ni otros secretos directamente en ellas cuando exista un método de entrada más seguro.

:::single-choice{#distinguish-clear-from-history-clear} Quieres renovar la terminal visible sin eliminar el historial de órdenes en memoria. ¿Qué orden debes ejecutar?

::option[`clear`]{#clear-visible-area .correct explanation="`clear` renueva el área visible de la terminal y deja intacta la lista del historial de Bash en memoria."}
::option[`history -c`]{#clear-memory explanation="Esta orden elimina las entradas de la lista actual en memoria. Modifica el historial en vez de limitarse a renovar la pantalla."}
::option[`history -d 1`]{#delete-first-entry explanation="Esta orden pide a Bash que elimine una entrada concreta del historial. No limpia el área visible de la terminal."}
:::

## Resumen

Ahora puedes encontrar y reutilizar órdenes de Bash mientras gestionas deliberadamente el historial.

1. Mostrar la lista numerada del historial actual.
2. Recuperar o expandir con cuidado una orden anterior.
3. Buscar interactivamente en el historial con `Ctrl+R`.
4. Eliminar, vaciar o escribir entradas del historial.
5. Distinguir el historial de órdenes de la pantalla de la terminal.
