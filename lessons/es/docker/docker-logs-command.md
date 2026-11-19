---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "es"
order_index: 6
title: "docker logs"
description: "Aprende a leer la salida que Docker recoge de un contenedor y a usarla para elegir el siguiente paso de diagnóstico."
meta_title: "docker logs - Docker"
meta_description: "Lee registros de contenedores activos o terminados, consulta las líneas recientes y distingue un error del programa del estado del contenedor."
meta_keywords: "docker logs, registros de contenedores, diagnóstico de Docker, errores de inicio, últimas líneas"
---

Un contenedor llamado `preview` ha terminado. La lista de contenedores indica su estado y su código de salida. Para averiguar qué comunicó el programa, consulta la salida que Docker recogió de ese contenedor.

## Elegir un contenedor

Indica el nombre del contenedor a `docker logs`. El comando puede leer la salida conservada de un contenedor que se haya detenido y aún exista. En este ejemplo, una tarea breve intentó leer un archivo en `/site/title.txt` antes de terminar.

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

Aquí, `cat` es el programa que intentó leer el archivo. El mensaje indica la ruta que el programa no pudo encontrar dentro del contenedor.

:::single-choice{#docker-logs-command-read-exited} Preview y report usaron la misma imagen. ¿Qué comando lee la salida de preview?

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="El nombre selecciona un contenedor. Report identifica otra ejecución."}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="Esa es la referencia de la imagen. Los registros pertenecen a un contenedor creado a partir de la imagen."}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="Este comando usa el nombre del contenedor cuya salida quieres consultar."}
:::

## Interpretar el mensaje en su contexto

Los registros contienen mensajes que escribió el propio programa. Un mensaje de inicio puede indicar que el programa ya escucha peticiones. Un error puede mostrar qué operación quedó sin completar. En el ejemplo, `preview` señala que falta una ruta dentro del contenedor. Un buen siguiente paso es revisar si el archivo debía estar exactamente en esa ruta. El mensaje te indica por dónde empezar.

:::single-choice{#docker-logs-command-error-boundary} ¿Qué permite afirmar el mensaje del archivo que falta?

::option[El archivo falta en todos los directorios del anfitrión.]{#docker-logs-command-error-host-path explanation="El programa buscó una ruta dentro del contenedor. El mensaje no describe todos los archivos del anfitrión."}
::option[El programa no encontró el archivo indicado dentro de preview.]{#docker-logs-command-error-container-path .correct explanation="El mensaje recoge el resultado de la búsqueda del programa que se ejecutó en preview."}
::option[El navegador del anfitrión usó un puerto sin publicar.]{#docker-logs-command-error-network explanation="El mensaje se refiere a la búsqueda de un archivo. No indica qué puerto usó el navegador."}
:::

## Consultar la salida reciente

Si un contenedor ha producido muchas líneas, usa `--tail` seguido de un número. Docker devuelve como máximo ese número de líneas del final de la salida recogida. Empieza con unas pocas y amplía la consulta si el primer error aparece antes.

```bash
$ docker logs --tail 5 web
```

![Terminal de LabEx con el error de archivo no encontrado de preview y las últimas cinco líneas de web](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

Los dos comandos consultan contenedores distintos. En la ejecución de LabEx, `preview` indica que falta el archivo y `web` comunica que Nginx se ha iniciado.

:::single-choice{#docker-logs-command-tail-choice} Solo quieres ver las dos últimas líneas disponibles de web. ¿Qué comando encaja?

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="Tail 2 solicita hasta dos líneas del final de la salida de este contenedor."}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="Solicita hasta cinco líneas, así que puede mostrar más de dos."}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="Sin un límite, Docker puede devolver todas las líneas disponibles."}
:::

## Qué hacer si la salida está vacía

Docker solo puede mostrar la salida que recogió. Un comando puede ejecutarse sin imprimir mensajes. También es posible que el programa escriba en un archivo que Docker no recoge. Si `docker logs` se ejecuta correctamente y no imprime nada, usa `docker ps -a` para comprobar el estado del contenedor. La falta de registros no aclara por sí sola ese estado.

:::single-choice{#docker-logs-command-empty-result} La tarea cleanup no tiene registros. ¿Cómo puedes saber si sigue en marcha o ya ha terminado?

::option[Pedir a Docker más líneas de cleanup.]{#docker-logs-command-empty-more-lines explanation="Cambiar el límite de líneas no aclara si un programa sin salida ha terminado."}
::option[Buscar la imagen con la que se inició cleanup.]{#docker-logs-command-empty-image explanation="La imagen identifica sus archivos y su configuración iniciales. El estado aparece en la lista de contenedores."}
::option[Consultar el estado de cleanup en la lista completa de contenedores.]{#docker-logs-command-empty-container-state .correct explanation="La lista completa incluye tanto los contenedores activos como aquellos que han terminado y aún existen."}
:::

## Resumen

Ya puedes usar la salida de un contenedor para decidir qué comprobar después.

1. Leer la salida recogida de un contenedor por su nombre, aunque haya terminado.
2. Utilizar el mensaje del programa para localizar el problema que comunica.
3. Limitar la salida con `--tail`.
4. Elegir otra comprobación si los registros dejan una pregunta sin responder.
