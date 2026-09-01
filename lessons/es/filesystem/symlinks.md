---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "es"
order_index: 12
title: "Enlaces simbólicos"
description: "Aprende cómo difieren los enlaces simbólicos y duros en la resolución de rutas, la identidad de inodos y el alcance del sistema de archivos."
meta_title: "Enlaces simbólicos - El sistema de archivos"
meta_description: "Aprende a crear e inspeccionar enlaces simbólicos y duros de Linux y comprende sus diferencias de identidad y alcance."
meta_keywords: "enlaces simbólicos Linux, enlaces duros, orden ln, inodos, readlink, recuento de enlaces"
---

Una entrada de directorio da nombre a un inodo. Un enlace duro crea otra entrada de directorio para el mismo inodo, mientras que un enlace simbólico crea un inodo distinto cuyo contenido es una ruta que debe resolverse. Esta diferencia controla la identidad, la duración y el comportamiento entre sistemas de archivos.

## Crear y examinar un enlace simbólico

Crea un enlace simbólico con `ln -s TARGET LINK_NAME`:

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

El enlace simbólico tiene su propio inodo y almacena el texto `myfile`. Cuando un programa sigue `myfilelink`, la resolución de rutas continúa hacia el destino. Muestra el texto almacenado sin seguirlo mediante:

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic} ¿Qué orden crea el enlace simbólico `myfilelink` con el texto de destino `myfile`?

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="La opción `-s` solicita un enlace simbólico, seguida del destino y el nombre del enlace nuevo."}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="Sin `-s`, `ln` solicita un enlace duro al inodo existente."}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="Readlink examina un enlace simbólico y no crea ninguno."}
:::

## Destinos relativos y absolutos

Un destino absoluto comienza en `/`. Un destino relativo se resuelve respecto al directorio que contiene el enlace simbólico, no respecto al directorio actual del shell en el momento en que alguien lo abra posteriormente.

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

Mover toda la jerarquía `tree` conserva esta relación relativa. Mover solo el enlace o el destino puede romperla. Un enlace simbólico puede contener un destino inexistente y entonces se denomina colgante o roto.

:::single-choice{#symlinks-relative-resolution} ¿Desde dónde se resuelve el destino relativo de un enlace simbólico?

::option[Desde el directorio personal del usuario que lo creó.]{#symlinks-creator-home explanation="La identidad del creador no se convierte en una base permanente de resolución."}
::option[Desde el directorio actual del primer shell que lo muestra.]{#symlinks-listing-shell explanation="El contexto del listado no reescribe la relación de destino almacenada."}
::option[Desde el directorio que contiene el enlace simbólico.]{#symlinks-containing-directory .correct explanation="El recorrido de la ruta sustituye el texto relativo almacenado en la ubicación del enlace."}
:::

## Crear un enlace duro

Crea otro nombre para un archivo normal existente sin `-s`:

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

Ambos nombres se corresponden con el mismo sistema de archivos y número de inodo. El recuento de enlaces pasa a ser 2. Ningún nombre es intrínsecamente el «original»; cambiar el contenido mediante uno modifica el objeto compartido, y eliminar un nombre deja el otro.

Los enlaces duros no pueden cruzar límites de sistemas de archivos porque un número de inodo solo tiene significado dentro del suyo. Linux también impide normalmente que los usuarios creen enlaces duros a directorios y puede restringir enlaces a archivos que no poseen para evitar ciclos y problemas de seguridad.

:::single-choice{#symlinks-hard-link-inode} ¿Qué comparten dos enlaces duros a un archivo normal?

::option[Únicamente nombres parecidos, pero datos de archivo distintos.]{#symlinks-separate-data explanation="Eso describiría copias independientes, no enlaces duros."}
::option[Una ruta almacenada dentro de un inodo de enlace simbólico distinto.]{#symlinks-stored-path explanation="El texto de una ruta es el mecanismo que define un enlace simbólico."}
::option[El mismo inodo y contenido de archivo.]{#symlinks-same-inode .correct explanation="Cada entrada de directorio da nombre al mismo objeto del sistema de archivos."}
:::

## Duración y eliminación

Eliminar un enlace simbólico elimina ese objeto de enlace, no su destino:

```bash
$ rm -- myfilelink
```

Eliminar el nombre de un enlace duro reduce el recuento de enlaces del inodo compartido. El sistema de archivos solo puede recuperar el objeto cuando el recuento llega a cero y ningún descriptor abierto ni otra referencia del sistema de archivos lo mantiene vivo.

Evita una barra final al eliminar un enlace simbólico a un directorio, porque la resolución de rutas con barra final puede seguir la semántica de directorios según la orden. Examina con `ls -ld -- LINK` y elimina deliberadamente el nombre del enlace.

:::single-choice{#symlinks-remove-symbolic} ¿Qué ocurre normalmente al eliminar el propio enlace simbólico?

::option[Se eliminan el inodo y el nombre del enlace mientras permanece el destino.]{#symlinks-remove-link-only .correct explanation="Desenlazar el enlace simbólico no actúa sobre el objeto indicado por el texto de destino almacenado."}
::option[Se eliminan automáticamente el destino y todos sus enlaces duros.]{#symlinks-remove-target explanation="El enlace simbólico es un objeto independiente y no posee su destino."}
::option[El destino se copia dentro del enlace antes de eliminarlo.]{#symlinks-copy-target explanation="La eliminación no conserva el contenido del destino dentro del enlace."}
:::

## Seguir enlaces de forma segura

Los enlaces simbólicos pueden desviar un programa privilegiado fuera de un directorio esperado o cambiar entre la validación y el uso. Los programas seguros deben evitar carreras de comprobar y después abrir, y utilizar interfaces relativas a directorios, que no sigan enlaces o que restrinjan la resolución según el lenguaje y el sistema operativo.

Para una inspección habitual:

- `ls -ld ENLACE` muestra el propio enlace.
- `readlink LINK` imprime el texto de destino almacenado.
- `stat LINK` suele comunicar los metadatos del enlace, mientras que `stat -L LINK` lo sigue en GNU coreutils.
- `find -L` sigue enlaces y puede encontrar ciclos; utilízalo solo deliberadamente.

Los permisos mostrados como `lrwxrwxrwx` no son una concesión general de acceso. El acceso se decide mediante el recorrido de directorios, la política de seguimiento y los permisos del destino; la propiedad del enlace también importa para algunas reglas de directorios protegidos.

:::single-choice{#symlinks-readlink-output} ¿Qué imprime de forma predeterminada `readlink LINK`?

::option[El texto de ruta almacenado en el enlace simbólico.]{#symlinks-readlink-target-text .correct explanation="Examina el objeto de enlace sin leer el contenido del archivo de destino."}
::option[Todo el contenido en bytes del archivo normal de destino.]{#symlinks-readlink-file-content explanation="Utiliza una orden de lectura después de resolver deliberadamente el destino para obtener su contenido."}
::option[Todos los enlaces duros del sistema de archivos.]{#symlinks-readlink-all-hard explanation="Descubrir enlaces duros exige búsquedas que conozcan los inodos y no guarda relación con el texto de destino del enlace simbólico."}
:::

Utiliza [Gestionar archivos y directorios en Linux](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835) para practicar con enlaces en archivos desechables y comparar números de inodo.

## Resumen

Ahora puedes elegir y examinar el tipo correcto de enlace del sistema de archivos.

1. Utiliza `ln -s DESTINO ENLACE` para un enlace simbólico basado en rutas.
2. Resuelve los destinos relativos desde el directorio que contiene el enlace.
3. Utiliza `ln EXISTING LINK` para otro nombre de inodo en el mismo sistema de archivos.
4. Distingue desenlazar un enlace simbólico de desenlazar uno duro.
5. Evita seguir enlaces de forma insegura en operaciones privilegiadas o recursivas.
