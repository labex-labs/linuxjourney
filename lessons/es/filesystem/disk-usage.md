---
lesson_id: "disk-usage"
course_id: "filesystem"
lang: "es"
order_index: 9
title: "Uso del disco"
description: "Aprende cómo `df` y `du` miden vistas distintas del consumo de bloques e inodos de un sistema de archivos."
meta_title: "Uso del disco - El sistema de archivos"
meta_description: "Aprende a comprobar el uso del disco en Linux con df y du, incluidos el espacio libre y los inodos."
meta_keywords: "orden df, orden du, uso de disco Linux, espacio libre, df -i, inodos"
---

La capacidad de un sistema de archivos tiene al menos dos límites: los bloques de datos y los objetos de metadatos como los inodos. `df` comunica la asignación desde la perspectiva del sistema de archivos, mientras que `du` recorre las rutas alcanzables y suma el uso atribuido a ellas. Los valores responden a preguntas distintas y no tienen por qué coincidir.

## Capacidad del sistema de archivos con `df`

Muestra el tipo de sistema de archivos montado y cifras de bloques legibles con:

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4  6.2G  2.3G  3.6G  40% /
```

`Size`, `Used` y `Avail` proceden de la contabilidad del sistema de archivos. El espacio disponible puede ser menor que el total menos el utilizado debido a bloques reservados, metadatos, políticas de asignación, cuotas o redondeos. Ejecuta `df` sobre una ruta para obtener el sistema de archivos que la contiene:

```bash
$ df -hT /var/log
```

:::single-choice{#disk-usage-df-scope}
¿Qué comunica principalmente `df`?

::option[El contenido en bytes de cada archivo de un directorio.]{#disk-usage-df-file-content explanation="La contabilidad del árbol de directorios corresponde a herramientas como `du`."}
::option[La capacidad, el uso y el espacio disponible a nivel del sistema de archivos.]{#disk-usage-df-filesystem .correct explanation="Df consulta estadísticas de asignación de sistemas de archivos montados en vez de recorrer todas las rutas."}
::option[Únicamente el tamaño físico impreso en la etiqueta de un disco.]{#disk-usage-df-physical-label explanation="Sus cifras describen la contabilidad del sistema de archivos, no solo la capacidad anunciada del hardware."}
:::

## Capacidad de inodos

Los sistemas de archivos que asignan objetos semejantes a inodos pueden agotarlos aunque queden bloques:

```bash
$ df -i /var
```

Una gran cantidad de archivos pequeños puede consumir los inodos disponibles. Eliminar un archivo grande libera muchos bloques, pero por lo general un solo inodo; eliminar muchos archivos pequeños innecesarios puede aliviar la presión de inodos. Algunos sistemas de archivos asignan metadatos dinámicamente y comunican estos conceptos de otra forma.

:::single-choice{#disk-usage-inode-exhaustion}
¿Qué puede ocurrir cuando un sistema de archivos tiene bloques libres, pero no inodos libres?

::option[Todos los archivos existentes duplican automáticamente su tamaño.]{#disk-usage-inode-double explanation="Agotar los inodos impide asignar metadatos nuevos y no amplía el contenido existente."}
::option[Puede fallar la creación de otro archivo.]{#disk-usage-inode-create-fail .correct explanation="Un objeto nuevo del sistema de archivos necesita metadatos aunque quede espacio para datos."}
::option[El sistema de archivos se convierte en intercambio.]{#disk-usage-inode-swap explanation="Agotar un recurso no cambia el tipo del sistema de archivos."}
:::

## Uso de rutas con `du`

Resume el espacio asignado alcanzable bajo un directorio:

```bash
$ du -sh /var/log
```

Compara los hijos inmediatos sin salir de un sistema de archivos:

```bash
$ sudo du -xhd1 /var | sort -h
```

Las opciones de GNU mostradas significan salida legible, profundidad máxima uno y un solo sistema de archivos. Los permisos pueden ocultar subárboles y producir un total incompleto. `du` también puede contar los archivos con enlaces duros una sola vez de forma predeterminada, distinguir el tamaño aparente de los bloques asignados y tratar de forma distinta los archivos dispersos según las opciones.

:::single-choice{#disk-usage-du-purpose}
¿Qué orden resume el uso asignado bajo `/var/log`?

::option[`df -i /var/log`]{#disk-usage-df-inodes explanation="Esta orden comunica estadísticas de inodos del sistema de archivos que contiene la ruta."}
::option[`du -sh /var/log`]{#disk-usage-du-summary .correct explanation="Du recorre el árbol indicado y `-s` emite un único resumen en unidades legibles."}
::option[`mount -a /var/log`]{#disk-usage-mount-a explanation="Montar no guarda relación con un resumen de solo lectura del uso de un directorio."}
:::

## Por qué difieren `df` y `du`

Entre las causas habituales se encuentran:

- un proceso mantiene abierto un archivo eliminado, por lo que sus bloques siguen asignados, pero no existe una ruta para `du`
- los metadatos del sistema de archivos, el espacio reservado, los diarios, reflinks, instantáneas o la compresión influyen en la contabilidad
- hay otro sistema de archivos montado dentro del árbol recorrido
- los permisos impiden que `du` lea algunos directorios
- los archivos dispersos tienen tamaños aparentes y asignados distintos

Para archivos eliminados pero abiertos, examina los procesos autorizados con una herramienta como `lsof +L1`; reinicia o señala el servicio responsable mediante su procedimiento normal en vez de truncar descriptores desconocidos.

:::single-choice{#disk-usage-deleted-open-file}
¿Por qué puede mostrar `df` espacio en uso que `du`, basado en rutas, no encuentra?

::option[Porque `df` siempre multiplica por dos el tamaño de todos los archivos.]{#disk-usage-df-doubles explanation="No existe una regla universal de duplicación."}
::option[Porque un archivo eliminado puede seguir abierto y asignado a un proceso en ejecución.]{#disk-usage-open-deleted .correct explanation="La entrada del directorio desapareció, pero el sistema de archivos conserva los bloques hasta que se cierra la última referencia abierta."}
::option[Porque `du` elimina automáticamente los archivos después de contarlos.]{#disk-usage-du-deletes explanation="Du es una herramienta de contabilidad y no elimina los archivos recorridos."}
:::

## Investigar sin empeorar el incidente

Empieza por el sistema de archivos lleno que comunica `df`, identifica su destino de montaje con `findmnt` y después limita las búsquedas de `du` al mismo sistema. Ten en cuenta las instantáneas, las capas de contenedores, los registros, las cachés de paquetes y la política de retención de la aplicación. No elimines archivos solo porque sean grandes; determina primero su propietario, copia de seguridad, requisitos normativos y comportamiento del servicio.

:::single-choice{#disk-usage-safe-investigation}
¿Cuál es la respuesta más segura al encontrar un archivo grande?

::option[Eliminarlo inmediatamente mientras el servicio escribe en él.]{#disk-usage-delete-immediately explanation="Esto puede perder datos necesarios y quizá no libere espacio si el archivo sigue abierto."}
::option[Ejecutar `mkfs` en el dispositivo que lo contiene.]{#disk-usage-mkfs-device explanation="Dar formato destruiría el sistema de archivos en vez de resolver el crecimiento de un archivo."}
::option[Identificar su propietario y su función de retención antes de modificarlo.]{#disk-usage-review-large-file .correct explanation="El tamaño por sí solo no demuestra que el archivo sea desechable ni seguro truncarlo."}
:::

## Resumen

Ahora puedes conciliar informes de espacio del sistema de archivos y basados en rutas.

1. Utiliza `df` para la capacidad de bloques de sistemas de archivos montados.
2. Utiliza `df -i` para la presión de inodos cuando sea compatible.
3. Utiliza recorridos limitados de `du` para atribuir el uso de rutas alcanzables.
4. Investiga archivos eliminados pero abiertos y diferencias de contabilidad específicas del sistema de archivos.
5. Aplica las políticas de propiedad y retención antes de eliminar datos.
