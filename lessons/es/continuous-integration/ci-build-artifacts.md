---
lesson_id: "ci-build-artifacts"
course_id: "continuous-integration"
lang: "es"
order_index: 6
title: "Artefactos de compilación"
description: "Aprende a relacionar un archivo generado por CI con su ejecución y con la revisión de origen."
meta_title: "Artefactos de compilación - Integración continua"
meta_description: "Aprende a relacionar un archivo generado por CI con su ejecución y con la revisión de origen."
meta_keywords: "artefactos de compilación, revisión de origen, integración continua, DevOps, Linux Journey"
---

Un **artefacto de compilación** es un archivo o un conjunto de archivos que se conserva después de una ejecución para usarlo más adelante. Por ejemplo, puede ser un informe de pruebas o un archivo comprimido del sitio. Si registras la ejecución y la revisión junto al artefacto, quien lo revise podrá identificar el código fuente que lo produjo.

## Empaquetar un directorio de salida

Usa la carpeta de prácticas donde `dist` contiene la página generada. Este ejemplo crea un archivo comprimido que reúne todo el contenido del directorio. Si en la carpeta actual ya hay un archivo comprimido con el mismo nombre, lo sustituye.

```bash
$ tar -czf site.tar.gz -C dist .
$ tar -tzf site.tar.gz
```

En el primer comando, `-c` crea el archivo, `-z` lo comprime y `-f` indica el nombre del archivo de salida. Con `-C dist .`, tar empieza en `dist`. El segundo comando usa `-t` para enumerar el contenido del archivo. Busca `./index.html` antes de compartirlo.

:::single-choice{#ci-build-artifacts-inspect-archive} ¿Qué comando permite comprobar que la página quedó incluida?

::option[Listar el contenido con tar -tzf site.tar.gz.]{#ci-build-artifacts-inspect-archive-b .correct explanation="La lista muestra si index.html está dentro."}
::option[Crear otra vez el archivo comprimido.]{#ci-build-artifacts-inspect-archive-a explanation="Volver a generarlo no te muestra qué archivos se empaquetaron."}
::option[Leer solo el nombre del archivo.]{#ci-build-artifacts-inspect-archive-c explanation="El nombre del archivo comprimido no indica qué contiene."}
:::

![Listado de tar que muestra index.html dentro de site.tar.gz](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-build-artifacts/archive-contents.png)

## Relacionar un artefacto con una ejecución

Un flujo puede subir el archivo comprimido cuando esté listo. En la página de la ejecución aparece la revisión que se compiló. Dos artefactos llamados `site.tar.gz` pueden ser distintos si provienen de revisiones diferentes. Para elegir qué archivo descargar, ten en cuenta tanto la ejecución como la revisión.

:::single-choice{#ci-build-artifacts-choose-run} Las ejecuciones 41 y 42 contienen site.tar.gz. ¿Cuál identifica el paquete de la revisión que comprobaste?

::option[La primera descarga con el nombre site.tar.gz.]{#ci-build-artifacts-choose-run-b explanation="El nombre no indica de qué código fuente proviene."}
::option[La última ejecución exitosa, sea cual sea su revisión.]{#ci-build-artifacts-choose-run-c explanation="Una ejecución posterior puede haber usado otros archivos fuente. Busca la revisión que quieres utilizar."}
::option[La ejecución cuya revisión coincide con la que comprobaste.]{#ci-build-artifacts-choose-run-a .correct explanation="Varias ejecuciones pueden usar el mismo nombre de archivo."}
:::

## Distinguir un archivo comprimido de una imagen de contenedor

Un archivo comprimido del sitio contiene archivos que puedes extraer. Una imagen de contenedor incluye el sistema de archivos y los ajustes que Docker usa para iniciar un contenedor. Un flujo puede publicar una imagen en un registro. Si vas a ejecutar esa imagen, anota su referencia junto con la revisión de origen.

:::single-choice{#ci-build-artifacts-deployable-type} La siguiente etapa debe iniciar un contenedor a partir de una imagen de un registro. ¿A qué resultado debe hacer referencia?

::option[A un informe de pruebas descargado de la ejecución.]{#ci-build-artifacts-deployable-type-a explanation="El informe describe resultados y no proporciona un sistema de archivos de contenedor."}
::option[A la referencia de la imagen de contenedor publicada.]{#ci-build-artifacts-deployable-type-c .correct explanation="Docker puede usar la referencia para obtener la imagen preparada."}
::option[Al nombre del archivo comprimido del sitio.]{#ci-build-artifacts-deployable-type-b explanation="El archivo contiene los de la página y no identifica una imagen del registro."}
:::

## Resumen

Ya puedes identificar un artefacto de compilación y rastrear su origen.

1. Empaqueta los archivos generados y revisa el contenido del archivo.
2. Comprueba qué ejecución y qué revisión de origen lo produjeron.
3. Elige un artefacto de archivo o una imagen de contenedor según lo que necesite la siguiente etapa.
