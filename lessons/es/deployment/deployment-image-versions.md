---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "es"
order_index: 2
title: "Versiones de imágenes"
description: "Aprende a distinguir entre la etiqueta y el resumen criptográfico de una imagen y a comparar las imágenes exactas que usan dos entornos."
meta_title: "Versiones de imágenes - Despliegue"
meta_description: "Aprende a distinguir entre la etiqueta y el resumen criptográfico de una imagen y a comparar las imágenes exactas que usan dos entornos."
meta_keywords: "versiones de imágenes, etiquetas, digest, despliegue, DevOps, Linux Journey"
---

Una etiqueta como `site:2` facilita la lectura de una referencia de imagen. Al subir una imagen nueva, quien la publica puede reasignar la etiqueta. Para identificar el contenido exacto de la imagen, registra su **resumen criptográfico** (digest), un valor calculado a partir del contenido al que apunta la referencia.

## Leer una etiqueta

Imagina que un registro muestra estas entradas en dos días distintos. Los resúmenes que aparecen abreviados son ilustrativos y no sirven para descargar una imagen.

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

La misma etiqueta ahora apunta a un contenido distinto. Un equipo que descargó la imagen el lunes puede seguir usando la versión anterior.

:::single-choice{#deployment-image-versions-moving-tag} Los dos entornos muestran la etiqueta site:2. ¿Qué permite saber qué imagen descargó realmente cada uno?

::option[Solo la etiqueta que comparten.]{#deployment-image-versions-moving-tag-b explanation="En el ejemplo, dos imágenes distintas usan la misma etiqueta."}
::option[El número de contenedores que tiene cada equipo.]{#deployment-image-versions-moving-tag-c explanation="Esa cifra no identifica las imágenes."}
::option[Los resúmenes criptográficos que se registraron.]{#deployment-image-versions-moving-tag-a .correct explanation="Una etiqueta puede reasignarse. El resumen identifica el contenido elegido en el momento de la descarga."}
:::

## Leer una referencia con resumen criptográfico

Una referencia de imagen puede incluir una `@` seguida del resumen criptográfico completo. Con esa referencia, solicitas al registro el objeto exacto. Usa el resumen completo que figure en el registro de imágenes o en el registro de compilación. Los valores abreviados pueden ayudar en ejemplos. Para descargar la imagen, necesitas el valor completo.

:::single-choice{#deployment-image-versions-fixed-reference} ¿Qué referencia selecciona un objeto concreto del registro?

::option[El nombre de la imagen sin etiqueta.]{#deployment-image-versions-fixed-reference-a explanation="Docker aplica una etiqueta predeterminada, que puede reasignarse."}
::option[El nombre de la imagen seguido de su resumen criptográfico completo.]{#deployment-image-versions-fixed-reference-c .correct explanation="El resumen corresponde a un contenido exacto."}
::option[Un comentario con el día de la compilación.]{#deployment-image-versions-fixed-reference-b explanation="El registro no puede recuperar un objeto a partir de un comentario."}
:::

## Comparar imágenes de la misma plataforma

El nombre de una imagen puede apuntar a una lista de compilaciones para distintos tipos de máquina o a una imagen para una plataforma concreta. Para comparar qué ejecutan dos equipos, anota la plataforma de cada uno y compara las referencias de imagen que corresponden a esas plataformas. Conserva la referencia original completa en el registro de la versión.

:::single-choice{#deployment-image-versions-compare-platform} Una versión admite arm64 y amd64. ¿Qué comparación resulta útil al comprobar dos equipos amd64?

::option[Comparar las referencias de imagen amd64 que eligió cada equipo.]{#deployment-image-versions-compare-platform-b .correct explanation="Así comparas el contenido destinado a la misma plataforma."}
::option[Comparar objetos de imagen de arquitecturas distintas.]{#deployment-image-versions-compare-platform-a explanation="Esos objetos corresponden a plataformas diferentes."}
::option[Comparar los nombres de los equipos.]{#deployment-image-versions-compare-platform-c explanation="Los nombres sirven para identificar los equipos. No indican qué contenido se desplegó."}
:::

## Resumen

Ya puedes identificar la imagen exacta que se usó, aunque la etiqueta se reasigne.

1. Explica por qué una etiqueta puede apuntar a contenidos distintos.
2. Reconoce una referencia con el resumen criptográfico completo.
3. Compara las imágenes que corresponden a la misma plataforma.
