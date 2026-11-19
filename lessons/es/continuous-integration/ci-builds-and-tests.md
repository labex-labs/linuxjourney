---
lesson_id: "ci-builds-and-tests"
course_id: "continuous-integration"
lang: "es"
order_index: 4
title: "Compilación y pruebas"
description: "Aprende a distinguir la preparación, la compilación y las pruebas con una pequeña comprobación local de una página."
meta_title: "Compilación y pruebas - Integración continua"
meta_description: "Aprende a distinguir la preparación, la compilación y las pruebas con una pequeña comprobación local de una página."
meta_keywords: "compilación, pruebas, código de salida, integración continua, DevOps, Linux Journey"
---

Es más fácil interpretar un fallo si cada etapa tiene una función clara. La **preparación** deja disponibles los archivos de entrada y las herramientas. La **compilación** genera una salida. Una **prueba** comprueba si los archivos fuente o el resultado cumplen una condición.

## Preparar el archivo de entrada

Escribe una página de ejemplo en una carpeta de prácticas vacía. La redirección sobrescribe `index.html` si ya existe, así que usa una carpeta de prácticas nueva.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
```

En un trabajo de CI, el checkout proporcionaría la página. Algunos proyectos también instalan dependencias, es decir, las bibliotecas o herramientas que necesitan para compilar o ejecutar sus pruebas.

:::single-choice{#ci-builds-and-tests-prepare-input} La página no está disponible antes de ejecutar el comando que la copia. ¿Qué etapa debes investigar primero?

::option[La descarga del artefacto en un trabajo posterior.]{#ci-builds-and-tests-prepare-input-a explanation="Se necesita el archivo de entrada antes de generar el resultado."}
::option[La preparación.]{#ci-builds-and-tests-prepare-input-b .correct explanation="El archivo de entrada debería estar disponible en este trabajo."}
::option[El tiempo de respuesta en producción.]{#ci-builds-and-tests-prepare-input-c explanation="El caso se refiere a archivos del ejecutor."}
:::

## Generar la salida

Copia la página a la carpeta que contendrá el sitio terminado.

```bash
$ mkdir -p dist
$ cp index.html dist/index.html
```

La opción `-p` permite que `mkdir` termine bien aunque la carpeta ya exista. La copia crea un archivo independiente en el directorio de salida. Las pruebas posteriores pueden examinar ese archivo.

:::single-choice{#ci-builds-and-tests-build-product} ¿Qué archivo está listo para empaquetar después de copiarlo correctamente?

::option[dist/index.html.]{#ci-builds-and-tests-build-product-a .correct explanation="La compilación dejó una copia en el directorio de salida."}
::option[La página desplegada en el sitio público.]{#ci-builds-and-tests-build-product-b explanation="Copiar el archivo localmente no pone en marcha un servicio."}
::option[Un registro del estado del flujo.]{#ci-builds-and-tests-build-product-c explanation="En este ejemplo, la compilación genera una página. El ejecutor registra por separado el estado de la comprobación."}
:::

## Probar la página

Ejecuta esta comprobación justo después de generar el archivo. La opción `-F` busca el texto literal y `-q` evita que se impriman las coincidencias. El intérprete guarda el código de salida del último comando en `$?`. Cero significa que encontró el texto. Uno indica que no hubo ninguna línea coincidente.

```bash
$ grep -Fq '<h1>Welcome</h1>' dist/index.html
$ echo "$?"
```

Deberías obtener `0`. La prueba buscó el texto exacto en el archivo generado. No evaluó los colores, la apariencia en el navegador ni el tiempo de respuesta.

:::single-choice{#ci-builds-and-tests-test-scope} La prueba pasa. ¿Qué puedes concluir?

::option[Se puede acceder a la página desde Internet.]{#ci-builds-and-tests-test-scope-a explanation="La comprobación leyó un archivo de salida local."}
::option[La página se ve bien en todos los navegadores compatibles.]{#ci-builds-and-tests-test-scope-b explanation="En esta prueba no se usó ningún navegador."}
::option[El archivo generado contiene el texto esperado del encabezado.]{#ci-builds-and-tests-test-scope-c .correct explanation="Esa es la condición que comprobó el comando grep."}
:::

![Comprobación local del encabezado en LabEx que termina con código de salida cero](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-builds-and-tests/heading-check.png)

## Resumen

Ya puedes interpretar qué demuestra cada etapa de una comprobación sencilla de CI.

1. Prepara el archivo de entrada antes de compilar.
2. Identifica qué archivo genera la compilación.
3. Interpreta el código de salida y la condición exacta que comprobó la prueba.
