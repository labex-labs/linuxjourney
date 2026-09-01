---
lesson_id: "inodes"
course_id: "filesystem"
lang: "es"
order_index: 11
title: "Inodos"
description: "Aprende cómo los números de inodo conectan los nombres de directorio con los metadatos y los datos de los objetos del sistema de archivos."
meta_title: "Inodos - El sistema de archivos"
meta_description: "Aprende cómo los inodos de Linux relacionan nombres, metadatos y datos, y cómo examinar números y capacidad de inodos."
meta_keywords: "inodos Linux, número de inodo, sistema de archivos, df -i, ls -li, stat, enlaces duros"
---

En los sistemas de archivos Unix basados en inodos, un directorio asocia el nombre de cada entrada con un número de inodo. El inodo representa el objeto del sistema de archivos y registra los metadatos necesarios para localizar e interpretar sus datos. Por tanto, la ruta no se almacena como identidad principal propia del objeto.

## Metadatos almacenados con un inodo

Entre los metadatos habituales asociados a un inodo se encuentran:

- tipo de objeto y modo de permisos
- propiedad de usuario y grupo
- tamaño lógico y contabilidad de bloques asignados
- número de enlaces duros
- marcas de tiempo de acceso, modificación y cambio de estado
- referencias a los datos del archivo o a estructuras de extensiones específicas del sistema de archivos

El inodo no suele almacenar el nombre de la entrada del directorio. Un sistema de archivos también puede almacenar atributos ampliados, listas de control de acceso, hora de creación, datos en línea u otra información mediante estructuras específicas del formato.

`ctime` es la hora de cambio de estado del inodo, no necesariamente la hora de creación del archivo. Una marca independiente de nacimiento o creación es opcional y puede no estar disponible.

:::single-choice{#inodes-name-location} ¿Dónde se asocia normalmente el componente de ruta de un archivo normal con su número de inodo?

::option[En el planificador de procesos.]{#inodes-scheduler-name explanation="El estado de planificación de CPU no implementa la búsqueda de rutas del sistema de archivos."}
::option[En una entrada de directorio.]{#inodes-directory-entry .correct explanation="Un directorio asocia un nombre con un número de inodo dentro de ese sistema de archivos."}
::option[En la tabla de particiones del disco.]{#inodes-partition-name explanation="Una tabla de particiones delimita regiones de almacenamiento, no nombres de archivos individuales."}
:::

## Números de inodo y alcance del sistema de archivos

Muestra los números de inodo con:

```bash
$ ls -li
```

El primer campo es el número de inodo. Examina un objeto con más detalle mediante:

```bash
$ stat path
```

Un número de inodo solo es único dentro de un sistema de archivos en un momento determinado. El mismo número puede existir en otro sistema y puede reutilizarse después de liberar un inodo. Para identificar un objeto de forma sólida, utiliza tanto la identidad del sistema de archivos como el número de inodo, no solo este último.

:::single-choice{#inodes-number-scope} ¿En qué ámbito identifica un objeto un número de inodo?

::option[En todos los sistemas Linux del mundo para siempre.]{#inodes-global-forever explanation="La asignación de inodos es local a cada sistema de archivos y los identificadores pueden reutilizarse."}
::option[En un sistema de archivos y en un momento determinados.]{#inodes-one-filesystem .correct explanation="Otros sistemas de archivos pueden utilizar el mismo número y los inodos liberados pueden reutilizarse después."}
::option[Únicamente en el proceso de shell que creó el archivo.]{#inodes-shell-scope explanation="El sistema de archivos, no un shell, mantiene la identidad del inodo."}
:::

## Enlaces duros y referencias abiertas

Varias entradas de directorio pueden referirse al mismo inodo; son enlaces duros. Crear otro enlace duro incrementa el número de enlaces del objeto. Eliminar un nombre reduce ese número sin borrar los datos mientras quede otro enlace.

Incluso después de eliminar la última entrada de directorio, un archivo abierto permanece asignado hasta que se cierre la última referencia del proceso. Su número de enlaces puede ser cero mientras un descriptor siga accediendo a él. Esto explica por qué eliminar un registro grande abierto quizá no reduzca inmediatamente el uso que muestra `df`.

:::single-choice{#inodes-unlinked-open-file} ¿Cuándo se liberan normalmente los recursos de un archivo desenlazado?

::option[Inmediatamente después de eliminar cualquier nombre de enlace duro.]{#inodes-one-link-removed explanation="Otros enlaces duros o referencias abiertas pueden mantener vivo el objeto."}
::option[Únicamente cuando se vuelve a dar formato a todo el sistema de archivos.]{#inodes-reformat-only explanation="Las operaciones normales de desenlace y cierre recuperan inodos y bloques sin uso."}
::option[Cuando su número de enlaces es cero y se cierra la última referencia abierta.]{#inodes-zero-links-no-opens .correct explanation="Los nombres de directorio y los descriptores de archivos de procesos son referencias independientes al inodo."}
:::

## Capacidad de inodos

En sistemas de archivos con un conjunto de inodos finito o comunicado, millones de archivos pequeños pueden agotar la capacidad de metadatos antes de llenar los bloques de datos. Examina la contabilidad de inodos de los sistemas montados con:

```bash
$ df -i
```

Si no quedan inodos libres, crear otro archivo puede fallar aunque `df -h` comunique bloques disponibles. Las estrategias de asignación difieren: algunos sistemas preasignan estructuras de inodos al crearse, mientras que otros gestionan metadatos dinámicamente y pueden comunicar la capacidad de otra forma.

:::single-choice{#inodes-df-i-purpose} ¿Qué comunica `df -i` cuando el sistema de archivos ofrece contabilidad de inodos?

::option[El contenido de todos los archivos ordenado por inodo.]{#inodes-df-i-content explanation="Df comunica estadísticas agregadas y no lee el contenido de los archivos."}
::option[La capacidad de inodos utilizada y disponible.]{#inodes-df-i-capacity .correct explanation="La vista de inodos ayuda a diagnosticar el agotamiento de objetos de metadatos independientemente de los bloques de datos."}
::option[La revisión del firmware del disco.]{#inodes-df-i-firmware explanation="El inventario del firmware no guarda relación con el uso de inodos."}
:::

## Correspondencia de datos específica del sistema de archivos

No supongas que cada inodo tiene exactamente 12 punteros directos y tres indirectos. Es una descripción útil de algunos diseños clásicos, pero ext4 moderno puede utilizar extensiones, y XFS, Btrfs y otros sistemas emplean estructuras diferentes. Los datos en línea y las extensiones comprimidas o de copia al escribir modifican aún más la relación.

Utiliza herramientas de diagnóstico específicas del sistema de archivos únicamente en modos de solo lectura o documentados cuando importe la correspondencia interna. Para la administración habitual, `stat`, `find -inum`, `df -i` y las herramientas que comprenden enlaces ofrecen abstracciones más seguras.

:::single-choice{#inodes-layout-portability} ¿Por qué no debes suponer un único diseño fijo de punteros para todos los inodos?

::option[Porque los inodos nunca se refieren de ninguna forma a los datos de archivos.]{#inodes-no-data-reference explanation="El sistema de archivos debe asociar el objeto con su contenido, aunque el mecanismo varíe."}
::option[Porque las implementaciones utilizan estructuras distintas de extensiones, árboles y datos en línea.]{#inodes-format-specific-layout .correct explanation="La correspondencia en disco entre un inodo y su contenido forma parte del formato de cada sistema de archivos."}
::option[Porque el propietario de cada archivo elige por separado el diseño de su inodo.]{#inodes-owner-layout explanation="La implementación y el formato del sistema de archivos determinan la estructura de metadatos."}
:::

Utiliza [Gestionar archivos y directorios en Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835) para comparar números de inodo y recuentos de enlaces en archivos desechables.

## Resumen

Ahora puedes relacionar rutas, inodos, enlaces y capacidad del sistema de archivos.

1. Trata las entradas de directorio como asociaciones de nombres con números de inodo.
2. Lee metadatos y marcas de tiempo sin confundir ctime con la creación.
3. Limita los números de inodo a un sistema de archivos y un momento.
4. Ten en cuenta los enlaces duros y los descriptores de archivo abiertos.
5. Utiliza modelos específicos de cada sistema en vez de un diseño universal de punteros.
