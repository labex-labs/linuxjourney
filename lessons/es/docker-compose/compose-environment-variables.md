---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "es"
order_index: 5
title: "Variables de entorno"
description: "Aprende a distinguir entre un valor que Compose inserta en el archivo y uno que pasa a un contenedor."
meta_title: "Variables de entorno - Docker Compose"
meta_description: "Aprende a distinguir entre un valor que Compose inserta en el archivo y uno que pasa a un contenedor."
meta_keywords: "variables de entorno, interpolación, Docker Compose, DevOps, Linux Journey"
---

Una variable de entorno es un valor con nombre que un programa puede leer. Compose puede usar variables de dos maneras: para insertar un valor al leer el archivo o para pasar valores a un programa dentro del contenedor.

## Insertar un valor en el archivo

Guarda el ejemplo como `compose.env.yaml` en la carpeta de prácticas. La expresión `${PAGE_MODE:-demo}` indica que se usa el valor de `PAGE_MODE` si la variable está definida y no está vacía. En caso contrario, se usa `demo`.

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose resuelve la expresión antes de crear el contenedor. A esto se le llama **interpolación**. En otros archivos puedes encontrar la misma técnica para elegir el puerto del anfitrión o la etiqueta de una imagen.

:::single-choice{#compose-environment-variables-interpolate-default} Si PAGE_MODE no está definida, ¿qué valor aparece en la configuración procesada?

::option[La expresión tal como aparece en el archivo.]{#compose-environment-variables-interpolate-default-a explanation="Compose resuelve la expresión cuando lee el archivo."}
::option[Un nombre de contenedor generado automáticamente.]{#compose-environment-variables-interpolate-default-c explanation="El nombre del contenedor y el valor de la variable se configuran por separado."}
::option[Demo, el valor que sigue al operador de valor predeterminado.]{#compose-environment-variables-interpolate-default-b .correct explanation="La expresión indica que demo es el valor que se usa por defecto."}
:::

## Consultar el valor resuelto

Al asignar una variable antes de un comando, el valor se aplica solo a esa ejecución. Usa esta forma para ver cómo cambia la configuración con otro valor. El comando `config` muestra los ajustes resueltos sin crear ningún contenedor.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

Busca `PAGE_MODE: review` en las variables de entorno del servicio. El valor `review` solo sirve para el ejemplo. Evita incluir secretos en los archivos de ejemplo o en la salida de los comandos.

:::single-choice{#compose-environment-variables-config-scope} La configuración procesada muestra review. ¿Qué ha ocurrido hasta ahora?

::option[Ya se ha iniciado un servicio con ese valor.]{#compose-environment-variables-config-scope-b explanation="Mostrar la configuración e iniciar un contenedor son operaciones distintas."}
::option[Compose ha insertado el valor al leer la configuración.]{#compose-environment-variables-config-scope-a .correct explanation="El comando config muestra los ajustes resueltos antes de iniciar un servicio."}
::option[Todos los contenedores existentes usan el valor.]{#compose-environment-variables-config-scope-c explanation="Esta ejecución no cambia los contenedores en marcha."}
:::

## Pasar un valor al contenedor

La sección `environment` pasa el valor resuelto a un contenedor nuevo. Usa `printenv` para que el programa dentro del contenedor temporal muestre ese valor.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

Deberías ver `review`. La interpolación eligió el valor y la entrada de entorno lo pasó al contenedor. Una variable que solo se usa para elegir un puerto del anfitrión no pasa automáticamente al entorno del programa.

:::single-choice{#compose-environment-variables-actual-value} ¿Cómo puedes comprobar qué valor recibe el programa del contenedor de herramientas?

::option[Mostrar PAGE_MODE desde el contenedor.]{#compose-environment-variables-actual-value-c .correct explanation="El entorno del propio programa permite comprobar qué valor recibió."}
::option[Leer solo el valor predeterminado del archivo original.]{#compose-environment-variables-actual-value-a explanation="Otro valor puede sustituir el valor predeterminado del archivo."}
::option[Buscar la dirección IP del contenedor de herramientas.]{#compose-environment-variables-actual-value-b explanation="La dirección no revela la configuración del programa."}
:::

## Resumen

Ya puedes distinguir los dos usos de las variables de entorno.

1. Lee una expresión con valor predeterminado en un archivo de Compose.
2. Revisa la configuración resuelta antes de iniciar un contenedor.
3. Comprueba un valor en el entorno del programa que se ejecuta.
