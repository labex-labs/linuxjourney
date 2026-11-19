---
lesson_id: "compose-volumes"
course_id: "docker-compose"
lang: "es"
order_index: 4
title: "Volúmenes"
description: "Aprende por qué un volumen con nombre conserva los archivos cuando se reemplaza un contenedor."
meta_title: "Volúmenes - Docker Compose"
meta_description: "Aprende por qué un volumen con nombre conserva los archivos cuando se reemplaza un contenedor."
meta_keywords: "volúmenes con nombre, almacenamiento persistente, Docker Compose, DevOps, Linux Journey"
---

Un contenedor puede escribir archivos en su propia capa de escritura. Si eliminas el contenedor, Docker elimina también esa capa. Un **volumen con nombre** es un espacio de almacenamiento que Docker administra por separado. Puedes montarlo en un contenedor que reemplace al anterior.

## Definir un volumen para la práctica

Guarda este ejemplo por separado como `compose.volume.yaml` en la carpeta de prácticas. El archivo monta el almacenamiento llamado `notes` en la ruta `/data` del contenedor de herramientas. La sección `volumes`, al final, declara el volumen con nombre.

```yaml
services:
  toolbox:
    image: busybox:1.36
    volumes:
      - notes:/data
volumes:
  notes:
```

La definición del servicio indica en qué ruta del contenedor se monta el volumen. La declaración de nivel superior indica que Compose debe administrar el volumen junto con el proyecto.

:::single-choice{#compose-volumes-attached-path} ¿Qué ruta usa el volumen con nombre dentro del contenedor de herramientas?

::option[/notes.]{#compose-volumes-attached-path-b explanation="Notes es el nombre del volumen. La ruta de montaje dentro del contenedor está a la derecha de los dos puntos."}
::option[/data.]{#compose-volumes-attached-path-a .correct explanation="La parte derecha de notes:/data indica la ruta dentro del contenedor."}
::option[Todas las rutas del contenedor.]{#compose-volumes-attached-path-c explanation="El volumen solo está montado en el directorio configurado."}
:::

## Escribir y leer desde dos contenedores distintos

La opción `-f` selecciona el archivo alternativo y `-p` le da un nombre de proyecto distinto. El comando `run --rm` crea un contenedor para una sola ejecución y lo elimina cuando termina. Ejecuta los comandos en la carpeta de prácticas. El primero sobrescribe el archivo de prueba en `/data/note.txt`.

```bash
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox sh -c 'echo ready > /data/note.txt'
$ docker compose -p journey-volume -f compose.volume.yaml run --rm toolbox cat /data/note.txt
```

El segundo contenedor debería mostrar `ready`. Monta el mismo volumen que el primero.

:::single-choice{#compose-volumes-persistence} ¿Por qué el segundo contenedor puede leer el archivo aunque se haya eliminado el primero?

::option[Los dos montaron el mismo volumen con nombre.]{#compose-volumes-persistence-b .correct explanation="El archivo se escribió en un almacenamiento independiente, montado en /data."}
::option[Los dos conservaron la capa de escritura del primer contenedor.]{#compose-volumes-persistence-a explanation="La capa del primer contenedor se eliminó junto con él."}
::option[BusyBox añadió el archivo a su imagen automáticamente.]{#compose-volumes-persistence-c explanation="La imagen original no cambia al ejecutar un contenedor."}
:::

![Dos contenedores de herramientas distintos escriben y leen un mismo archivo en un volumen con nombre](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-volumes/persisted-note.png)

## Decidir qué datos se conservan

Un archivo como `/tmp/note.txt`, fuera del directorio montado, se queda en el contenedor salvo que esa ruta tenga otro almacenamiento montado. Comprueba las rutas antes de dar por hecho que el archivo se conservará. Si eliminas el volumen, puedes perder sus datos. Una copia de seguridad guarda los datos por separado y te permite restaurarlos si se pierde el volumen.

:::single-choice{#compose-volumes-inside-mount} ¿A qué archivo podrá acceder el próximo contenedor de herramientas a través de este volumen?

::option[A /tmp/note.txt de la capa de escritura del primer contenedor.]{#compose-volumes-inside-mount-a explanation="Esta ruta queda fuera del directorio montado."}
::option[A un archivo guardado en otro volumen con nombre.]{#compose-volumes-inside-mount-b explanation="Para verlo, el contenedor nuevo tendría que montar ese otro volumen."}
::option[A /data/note.txt, que escribió el primer contenedor.]{#compose-volumes-inside-mount-c .correct explanation="El montaje en /data da acceso al mismo archivo guardado desde los dos contenedores."}
:::

## Resumen

Ya puedes explicar por qué un archivo puede seguir disponible después de eliminar el contenedor que lo escribió.

1. Identifica el nombre del volumen y la ruta de montaje.
2. Lee el archivo desde otro contenedor para comprobar que se conserva.
3. Distingue entre eliminar el volumen y reemplazar el contenedor.
