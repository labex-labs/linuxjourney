---
lesson_id: "find-command"
course_id: "command-line"
lang: "es"
order_index: 14
title: "find"
description: "Aprende a buscar en árboles de directorios por nombre, tipo, tamaño y fecha, y a actuar sobre coincidencias verificadas."
meta_title: "find - Línea de Comandos"
meta_description: "Aprende el comando find de Linux con ejemplos para buscar por nombre, tipo, tamaño, tiempo de modificación y ejecutar acciones sobre archivos coincidentes."
meta_keywords: "comando linux find, comando find, encontrar archivos linux, find por nombre, find por tipo, find por tamaño, find mtime, find exec"
---

Con innumerables archivos en un sistema, puede ser difícil localizar uno específico. El comando `find` busca en árboles de directorios usando criterios como nombre, tipo, tamaño y tiempo de modificación.

## Elección del lugar donde buscar

La sintaxis básica es:

```bash
find [PATH] [EXPRESSION]
```

Especificas el directorio donde buscar y los criterios de lo que buscas.

Por ejemplo, para buscar un archivo llamado `puppies.jpg` dentro del directorio `/home` y todos sus subdirectorios, usarías:

```bash
$ find /home -name puppies.jpg
```

Las búsquedas son recursivas por defecto, así que `find /home` busca dentro de `/home` y sus subdirectorios.

Utiliza `.` como ruta inicial cuando quieras buscar en el árbol del directorio actual.

:::single-choice{#search-current-tree} ¿Qué orden busca en el directorio actual y sus descendientes elementos llamados `notes.txt`?

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="El punto selecciona el directorio actual como ruta inicial y `-name` comprueba el nombre base de cada elemento."}
::option[`find / -name notes.txt`]{#find-root-notes explanation="Una ruta inicial `/` busca desde la raíz del sistema de archivos, un ámbito mucho más amplio que el árbol del directorio actual."}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find` espera las rutas iniciales antes de la expresión. Este orden no representa la búsqueda solicitada."}
:::

## Coincidencia por nombre y tipo

La prueba `-name` acepta un nombre base exacto o un patrón al estilo de la shell. Entrecomilla los patrones con comodines para que la shell actual los entregue sin modificar a `find`:

```bash
$ find . -name "*.txt"
```

Sin comillas, la shell podría expandir `*.txt` en el directorio actual antes de que se inicie `find`. Utiliza `-iname` en lugar de `-name` si la coincidencia no debe distinguir mayúsculas y minúsculas.

```bash
$ find /home -type d -name MyFolder
```

En este comando, establecemos el tipo a `d` para directorio y buscamos un elemento llamado `MyFolder`. Para buscar específicamente archivos regulares, usarías `-type f`.

:::single-choice{#find-text-regular-files} ¿Qué orden encuentra archivos normales cuyos nombres terminan en `.txt` bajo el directorio actual?

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f` selecciona archivos normales y `find` evalúa el patrón de `-name` entrecomillado para cada elemento."}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="El patrón está entrecomillado correctamente, pero `-type d` selecciona directorios en vez de archivos normales."}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="La shell actual puede expandir el comodín sin comillas antes de ejecutar `find`, lo que cambia la expresión prevista."}
:::

## Coincidencia por tamaño y fecha de modificación

Puedes buscar por tamaño de archivo:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

La `M` mayúscula representa unidades de 1 048 576 bytes y la `k` minúscula, unidades de 1024 bytes. `find` redondea los tamaños hacia arriba según la unidad elegida antes de comparar el número, por lo que los límites se basan en esas unidades.

También puedes buscar por tiempo de modificación:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime` mide periodos completos de 24 horas desde la modificación. `-mtime -7` selecciona un valor inferior a 7 y `-mtime +30`, uno superior a 30; estas pruebas no se basan en los límites de los días del calendario.

:::single-choice{#find-recent-regular-files} ¿Qué orden encuentra bajo `.` archivos normales cuya antigüedad de modificación es inferior a siete periodos completos de 24 horas?

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f` selecciona archivos normales y `-mtime -7` selecciona antigüedades inferiores a siete periodos completos de 24 horas."}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="El signo más selecciona antigüedades superiores a siete unidades. Busca archivos más antiguos, no recientes."}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="La prueba de tiempo busca elementos recientes, pero `-type d` restringe los resultados a directorios en vez de archivos normales."}
:::

## Mostrar coincidencias y actuar sobre ellas

Por defecto, `find` imprime las rutas coincidentes. Puedes agregar acciones como `-print`, `-delete` o `-exec`.

Imprimir coincidencias explícitamente:

```bash
$ find . -name "*.log" -print
```

Ejecutar `ls -l` en cada coincidencia:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

En la forma con `\;`, `{}` se sustituye por una ruta coincidente en cada invocación. El punto y coma termina la acción `-exec` y se escapa para que la shell se lo entregue a `find`.

Antes de usar una acción destructiva como `-delete` o una orden `-exec` que modifique archivos, ejecuta las mismas pruebas con `-print` y revisa todos los resultados. Una ruta inicial más limitada y `-maxdepth N` también pueden restringir la búsqueda.

:::single-choice{#verify-before-delete} Estás preparando una orden `find` que más adelante podría eliminar archivos `.log` antiguos. ¿Qué debes hacer primero?

::option[Añadir `-delete` de inmediato y comprobar qué archivos desaparecen.]{#delete-first explanation="Eliminar no es una previsualización segura y no tiene una función incorporada para deshacer. Comprueba todas las coincidencias antes de añadir la acción."}
::option[Ejecutar las mismas pruebas con `-print` y revisar cada coincidencia.]{#print-first .correct explanation="Una lista de solo lectura verifica la ruta inicial y las pruebas antes de introducir una acción destructiva."}
::option[Buscar desde `/` para que la orden no omita ningún archivo de registro.]{#root-first explanation="Comenzar en `/` amplía el ámbito y puede incluir rutas ajenas o protegidas. Utiliza el punto de partida apropiado más limitado."}
:::

:::single-choice{#run-ls-for-each-match} En `find . -name "*.log" -exec ls -l {} \;`, ¿qué representa `{}`?

::option[La ruta coincidente actual que se pasa a `ls -l`.]{#match-placeholder .correct explanation="En esta forma de `-exec`, `find` sustituye `{}` por la coincidencia actual antes de invocar `ls -l`."}
::option[El directorio donde se inició la orden `find`.]{#starting-placeholder explanation="El directorio inicial es el punto situado cerca del principio de la orden. Las llaves cumplen otra función dentro de `-exec`."}
::option[El punto y coma que termina la expresión `-exec`.]{#terminator-placeholder explanation="El punto y coma escapado termina la acción `-exec`. Las llaves son el marcador de posición de la ruta."}
:::

Los mensajes de permiso denegado suelen indicar que la cuenta actual no puede recorrer parte del árbol. Prefiere una ruta inicial pertinente y más limitada; no añadas privilegios elevados hasta comprender y querer el acceso adicional.

Para practicar la creación de expresiones de búsqueda, prueba estos laboratorios:

1. **[Orden find de Linux: búsqueda de archivos](https://labex.io/es/labs/linux-linux-find-command-file-searching-219191)** - Este laboratorio presenta la orden `find`, una herramienta versátil para buscar y localizar archivos y directorios según distintos criterios. Practicarás cómo localizar archivos concretos con `find`.
2. **[Descubrir recursos críticos del sistema](https://labex.io/es/labs/linux-discover-critical-system-resources-388032)** - Aprende órdenes esenciales de Linux para localizar archivos y ejecutables, incluida `find`. Practicarás cómo recorrer con eficiencia el sistema de archivos y descubrir recursos críticos del sistema.

## Resumen

Ahora puedes construir expresiones de `find` bien delimitadas y verificar los resultados antes de actuar.

1. Elegir la ruta inicial útil más limitada.
2. Entrecomillar patrones de nombre y combinarlos con pruebas de tipo.
3. Filtrar por tamaño o por periodos completos de modificación de 24 horas.
4. Limitar la profundidad de recursión cuando convenga.
5. Mostrar y revisar las coincidencias antes de realizar acciones destructivas.
