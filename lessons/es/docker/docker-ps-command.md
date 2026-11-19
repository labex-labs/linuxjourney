---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "es"
order_index: 4
title: "docker ps"
description: "Aprende a listar los contenedores de Docker y a distinguir cuáles están en ejecución y cuáles han terminado."
meta_title: "docker ps - Docker"
meta_description: "Interpreta la salida de docker ps, localiza contenedores detenidos con docker ps -a y lee sus nombres y códigos de salida."
meta_keywords: "docker ps, listar contenedores Docker, contenedores detenidos, docker ps -a, estado, códigos de salida"
---

¿Sigue en marcha el servidor web que iniciaste en Docker? Compruébalo con `docker ps`. Una imagen de Docker reúne el programa y los archivos que necesita. Un contenedor es una instancia creada a partir de esa imagen. El comando muestra la lista de contenedores en el momento de la consulta.

## Listar contenedores en ejecución

De forma predeterminada, `docker ps` lista los contenedores en ejecución. Los ejemplos muestran unas cuantas columnas de un entorno Docker preparado. Puedes leer la salida sin configurar Docker. Si usas una terminal, escribe el comando que aparece después del prompt `$`.

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

Si Docker solo imprime los encabezados de las columnas, la lista de contenedores en ejecución está vacía. En ese mismo entorno todavía puede haber contenedores detenidos.

:::single-choice{#docker-ps-running-list} Docker imprime solo los encabezados de las columnas al ejecutar `docker ps`. ¿Qué puedes deducir?

::option[No hay imágenes disponibles para iniciar contenedores.]{#docker-ps-running-list-images explanation="El comando lista contenedores. Puede haber imágenes aunque no haya contenedores en ejecución."}
::option[No hay contenedores en la lista de los que están en ejecución.]{#docker-ps-running-list-empty .correct explanation="La lista predeterminada muestra los contenedores en marcha. Todavía puede haber contenedores detenidos."}
::option[No hay contenedores detenidos que inspeccionar.]{#docker-ps-running-list-stopped explanation="La selección predeterminada no incluye los contenedores detenidos. La lista vacía no indica si los hay."}
:::

## Leer nombres y estados

Busca primero el contenedor en la columna `NAMES`. Las dos filas muestran la misma imagen, `nginx:alpine`, en la columna `IMAGE`. Localiza `web` en la última columna y lee `STATUS` en esa misma fila. `Up 4 minutes` indica que ese contenedor lleva unos cuatro minutos en ejecución.

:::single-choice{#docker-ps-name-column} ¿Qué fila corresponde a un contenedor que lleva unos 30 segundos en ejecución?

::option[La fila cuyo nombre es `demo`.]{#docker-ps-name-demo .correct explanation="Busca Up 30 seconds en STATUS. En esa misma fila, NAMES muestra demo."}
::option[La fila cuyo nombre es `web`.]{#docker-ps-name-web explanation="La fila de web muestra Up 4 minutes. Los dos contenedores usan la misma imagen y se iniciaron en momentos distintos."}
::option[Las dos filas con la imagen `nginx:alpine`.]{#docker-ps-name-image-reference explanation="Cada fila muestra su propio estado. Compartir una imagen no implica haberse iniciado a la vez."}
:::

## Incluir contenedores que han terminado

Si no aparece un contenedor que esperabas ver, prueba con `docker ps -a`. La opción `-a` es la abreviatura de `--all`. Incluye los contenedores detenidos que todavía existen. Este ejemplo añade una tarea preparada llamada `preview`.

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

Un contenedor ejecuta un programa principal, como un servidor web o un script. `Exited` indica que ese programa se ha detenido. El número entre paréntesis es su **código de salida**, el resultado que comunicó al terminar. Cero suele indicar éxito y un código distinto de cero suele indicar un error. La tarea `report` muestra `Exited (0)`, un resultado normal para una tarea completada correctamente.

![Terminal de LabEx con contenedores activos y terminados, report con código 0 y preview con código 1](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

La captura de LabEx muestra únicamente los nombres y estados de los cuatro contenedores de ejemplo. Los tiempos transcurridos dependen de cuándo ejecutes el comando.

:::single-choice{#docker-ps-exit-code-reading} ¿Qué fila investigarías por un posible error a partir del código de salida?

::option[`report`, porque ha terminado.]{#docker-ps-exit-code-report explanation="Una tarea breve puede terminar al completar su trabajo. El código cero suele indicar que comunicó un resultado correcto."}
::option[`demo`, porque es el contenedor en ejecución más reciente.]{#docker-ps-exit-code-demo explanation="Up indica cuánto tiempo lleva ejecutándose el programa. Esta fila no tiene código de salida."}
::option[`preview`, porque terminó con el código 1.]{#docker-ps-exit-code-preview .correct explanation="Preview muestra Exited (1). Conviene investigar ese fallo, aunque el estado por sí solo no indica la causa."}
:::

## Elegir la próxima comprobación

El código de salida orienta la búsqueda. Para saber si `preview` imprimió un error, escribe su nombre después de `docker logs`. El comando muestra la salida que Docker recogió de ese contenedor.

```bash
$ docker logs preview
```

Si el servidor web está en marcha, quizá también quieras saber si un visitante puede abrir la página. Ábrela desde el equipo que necesita acceder. `Up` describe el programa dentro del contenedor. Una solicitud correcta en el navegador confirma que se puede acceder a la página desde el equipo que has usado.

:::single-choice{#docker-ps-check-visitor-access} La página se abre en el equipo que ejecuta Docker. Otra persona necesita abrirla desde su equipo. ¿Qué prueba permite saber si puede hacerlo?

::option[Abrir la página desde el equipo de esa persona.]{#docker-ps-next-check-visitor-browser .correct explanation="Esa solicitud comprueba la conexión que usará realmente."}
::option[Volver a ejecutar `docker ps` en el equipo con Docker.]{#docker-ps-next-check-status-again explanation="La lista permite saber si web sigue en marcha. Para verificar el acceso desde el otro equipo, hace falta una solicitud desde allí."}
::option[Abrir la página otra vez en el equipo con Docker.]{#docker-ps-next-check-host-browser explanation="Eso repite la prueba desde el primer equipo. La conexión desde el otro podría comportarse de otra manera."}
:::

## Resumen

Ya puedes usar la lista de contenedores para localizar uno, leer su estado y decidir qué comprobar después.

1. Usar `docker ps` para listar los contenedores en marcha.
2. Buscar un contenedor por su nombre y leer su estado.
3. Usar `docker ps -a` para incluir los contenedores terminados.
4. Usar los registros o una solicitud del navegador cuando el estado no aporta información suficiente.
