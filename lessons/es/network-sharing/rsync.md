---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "es"
order_index: 2
title: "rsync"
description: "Aprende a previsualizar, ejecutar y comprobar una sincronización segura de directorios, local o mediante SSH, con rsync."
meta_title: "rsync - Network Sharing"
meta_description: "Descubre cómo utilizar el potente comando rsync de Linux para sincronizar archivos de forma eficiente, transferir datos remotamente y realizar copias fiables. Esta guía explica sus comandos y opciones esenciales."
meta_keywords: "rsync, rsync linux, sincronización de archivos, copia de datos, sincronización remota, comando rsync, transferencia de archivos linux, tutorial rsync"
---

`rsync` reconcilia archivos y árboles de directorios evitando transferir innecesariamente datos que no han cambiado. Su eficiencia no hace seguras todas las invocaciones: la sintaxis del origen, las barras finales, los metadatos, las exclusiones y la política de eliminación determinan el resultado.

## Interpretar el origen y el destino

Sincroniza localmente el contenido de `source/` dentro de `destination/`:

```bash
$ rsync -a -- source/ destination/
```

La barra final de `source/` significa «copia el contenido de este directorio». Sin ella, `rsync -a source destination/` crea o actualiza `destination/source`. Previsualiza siempre las rutas resultantes cuando cambies la colocación de la barra.

:::single-choice{#rsync-source-trailing-slash}
¿Qué significa la barra final de `rsync -a source/ destination/`?

::option[Eliminar el origen después de una transferencia satisfactoria.]{#rsync-delete-source explanation="Eliminar el origen requiere otra opción y una política explícitas."}
::option[Copiar el contenido de `source` dentro del destino.]{#rsync-copy-contents .correct explanation="Quitar la barra del origen cambia la disposición de nivel superior en el destino."}
::option[Interpretar el destino como un recurso compartido remoto de Windows.]{#rsync-windows-share explanation="La barra controla el contenido de los directorios, no el tipo de transporte."}
:::

## Comprender el modo de archivo

El modo de archivo, `-a`, equivale a un conjunto de opciones recursivas y de conservación de metadatos que suele resumirse como `-rlptgoD`. Conserva enlaces simbólicos, permisos, horas de modificación, grupos, propietarios y archivos de dispositivos o especiales cuando los permisos y la plataforma lo permiten.

El modo de archivo no incluye la conservación de enlaces duros, ACL ni atributos extendidos; normalmente requieren `-H`, `-A` y `-X`. Tampoco crea versiones históricas por sí solo.

:::single-choice{#rsync-archive-limit}
¿Qué metadato no incluye `-a` por sí solo?

::option[Las relaciones entre enlaces duros.]{#rsync-hard-links .correct explanation="Conservar los enlaces duros requiere la opción independiente `-H`."}
::option[El recorrido recursivo de directorios.]{#rsync-archive-recursion explanation="El modo de archivo incluye el recorrido recursivo."}
::option[Las horas de modificación.]{#rsync-archive-times explanation="El modo de archivo incluye la conservación de horas."}
:::

## Previsualizar una transferencia

Utiliza una simulación con cambios detallados antes de una sincronización importante:

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

Una simulación predice las acciones según el análisis actual; no puede garantizar que los archivos no cambien antes del comando real. Guarda y revisa el comando exacto y ejecútalo sin `--dry-run` solo después de confirmar ambos puntos finales.

:::single-choice{#rsync-dry-run-purpose}
¿Qué proporciona `--dry-run --itemize-changes`?

::option[Una instantánea permanente conservada en otro dispositivo.]{#rsync-dry-backup explanation="Una simulación no crea ninguna copia de datos ni conservación independiente."}
::option[Una garantía de que los archivos de origen no podrán cambiar posteriormente.]{#rsync-dry-lock explanation="La previsualización no bloquea el árbol de origen."}
::option[Una previsualización de los cambios que rsync planea actualmente.]{#rsync-dry-preview .correct explanation="La salida detallada de la simulación expone las decisiones de rutas y metadatos antes de modificarlos."}
:::

## Sincronizar mediante SSH

Envía datos a un host remoto u obtenlos de él mediante el operando remoto habitual:

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

Rsync moderno suele utilizar SSH para esta forma, pero confirma el shell remoto configurado, la clave del host, los privilegios de la cuenta y la disponibilidad de rsync remoto. La compresión con `-z` puede ayudar con datos comprimibles en un enlace limitado, pero puede desperdiciar CPU con datos ya comprimidos.

:::single-choice{#rsync-pull-direction}
¿Qué orden de operandos obtiene datos remotos en un directorio local?

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="Este orden envía el contenido local al destino remoto."}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="Esto no expresa la sintaxis de ruta remota mostrada y añade una opción destructiva no relacionada."}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="El árbol remoto es el origen y el árbol local es el destino."}
:::

## Tratar la eliminación como destructiva

`--delete` elimina las entradas del destino que no existen en el origen dentro del ámbito sincronizado. Por tanto, invertir los puntos finales, usar una barra incorrecta o definir una exclusión errónea puede borrar datos válidos. Previsualiza contra un destino de prueba, asegúrate de disponer de copias recuperables, revisa el estado de montaje y considera límites máximos de eliminaciones antes de autorizarlo.

Después de la ejecución real, inspecciona el estado de salida y los registros, compara la cantidad esperada de archivos y los metadatos, y prueba contenido representativo o una restauración. La sincronización mediante rsync por sí sola replica eliminaciones o daños no deseados y no constituye una estrategia completa de copias de seguridad.

:::single-choice{#rsync-delete-effect}
¿Qué puede hacer `--delete` durante la sincronización?

::option[Cifrar todos los archivos transferidos mediante la clave del host SSH.]{#rsync-delete-encrypt explanation="La política de eliminación no está relacionada con el cifrado de archivos."}
::option[Impedir todos los cambios en el sistema de archivos de destino.]{#rsync-delete-readonly explanation="Autoriza explícitamente cambios adicionales en el destino."}
::option[Eliminar entradas del destino que no existen en el ámbito de origen seleccionado.]{#rsync-delete-destination .correct explanation="La opción hace que el contenido del destino refleje el origen y exige una previsualización revisada y un plan de recuperación."}
:::

## Resumen

Ahora puedes previsualizar y comprobar una operación `rsync` sin ocultar sus casos destructivos.

1. Utiliza barras finales para expresar la disposición prevista de los directorios.
2. Añade las opciones de metadatos que no cubra el modo de archivo cuando sean necesarias.
3. Revisa la salida detallada de la simulación antes de sincronizar realmente.
4. Comprueba la identidad SSH y la dirección de los puntos finales.
5. Trata la eliminación y la conservación de copias como políticas explícitas.
