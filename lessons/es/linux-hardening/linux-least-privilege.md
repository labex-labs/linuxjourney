---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "es"
order_index: 3
title: "Principio de mínimo privilegio"
description: "Aprende a elegir los permisos de archivos y de administración que requiere una tarea concreta de un servicio."
meta_title: "Principio de mínimo privilegio - Endurecimiento de Linux"
meta_description: "Aprende a elegir los permisos de archivos y de administración que requiere una tarea concreta de un servicio."
meta_keywords: "mínimo privilegio, endurecimiento de Linux, ciberseguridad, Linux Journey"
---

El **mínimo privilegio** consiste en dar a una cuenta solo el acceso que necesita para su trabajo. Empieza por enumerar las acciones. Quizá la cuenta deba leer un archivo, escribir en otro y no tenga ninguna tarea de administración.

## Ajustar los permisos a la tarea

Un proceso que atiende peticiones web necesita leer `index.html`. La cuenta de despliegue actualiza el archivo. Cada tarea puede tener permisos distintos. El proceso web puede leer la página y la cuenta de despliegue puede modificarla.

:::single-choice{#linux-least-privilege-read-only-page} ¿Qué permiso sobre la página necesita el proceso web en este ejemplo?

::option[Permiso de lectura.]{#linux-least-privilege-read-only-page-a .correct explanation="Para servir el archivo, el proceso necesita leer su contenido."}
::option[Permiso de escritura.]{#linux-least-privilege-read-only-page-b explanation="La cuenta de despliegue es la que modifica la página."}
::option[Permiso para administrar otros servicios.]{#linux-least-privilege-read-only-page-c explanation="Esas tareas quedan fuera del cometido del proceso web."}
:::

## Comprobar la ruta completa

Los permisos del archivo son solo una parte de la comprobación. Linux también exige permiso para atravesar los directorios que llevan al archivo. En un directorio, el permiso de ejecución permite al programa atravesarlo si conoce el nombre de la entrada que busca. Si el proceso no puede atravesar un directorio de la ruta, tampoco podrá acceder al archivo aunque tenga permiso de lectura.

:::single-choice{#linux-least-privilege-path-boundary} Según los permisos de index.html, el proceso puede leerlo, pero no puede acceder al directorio que lo contiene. ¿Qué debes revisar?

::option[Si la página ocupa más espacio.]{#linux-least-privilege-path-boundary-a explanation="El tamaño no concede acceso al directorio."}
::option[Si se debe permitir que todo el mundo modifique la página.]{#linux-least-privilege-path-boundary-c explanation="El permiso de escritura no resuelve la falta de acceso a la ruta."}
::option[El permiso del proceso para atravesar el directorio.]{#linux-least-privilege-path-boundary-b .correct explanation="El proceso necesita acceso tanto al archivo como a los directorios de la ruta."}
:::

## Limitar las acciones administrativas

Las herramientas administrativas como `sudo` pueden permitir que un usuario autorizado realice tareas concretas de mantenimiento. Define la acción, quién tiene autorización para realizarla y cómo comprobarás el nuevo acceso. Verifica que el mantenimiento autorizado siga funcionando y que la misma política siga impidiendo otras acciones administrativas ajenas a la tarea.

:::single-choice{#linux-least-privilege-policy-test} Un rol de mantenimiento debe consultar el estado del servicio. ¿Qué plan comprueba mejor los permisos previstos?

::option[Comprobar que ahora funciona cualquier comando administrativo.]{#linux-least-privilege-policy-test-a explanation="Esos permisos adicionales superarían lo requerido para la tarea documentada."}
::option[Comprobar que el rol puede consultar el estado y que los cambios privilegiados ajenos a la tarea siguen restringidos.]{#linux-least-privilege-policy-test-c .correct explanation="Así verificas el acceso necesario y el límite previsto."}
::option[Comprobar solo que existe el nombre de usuario.]{#linux-least-privilege-policy-test-b explanation="La existencia de una cuenta no demuestra qué permisos tiene."}
:::

## Resumen

Ya puedes determinar el acceso mínimo que necesita una tarea.

1. Distingue entre las acciones de lectura, escritura y administración.
2. Comprueba el acceso a través de los directorios de la ruta.
3. Verifica las acciones permitidas y las restringidas para cada rol.
