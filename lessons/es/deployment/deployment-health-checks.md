---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "es"
order_index: 4
title: "Comprobaciones de estado"
description: "Aprende a combinar una comprobación del proceso, una del servicio y una petición desde un cliente después del despliegue."
meta_title: "Comprobaciones de estado - Despliegue"
meta_description: "Aprende a combinar una comprobación del proceso, una del servicio y una petición desde un cliente después del despliegue."
meta_keywords: "comprobaciones de estado, punto de acceso de versión, despliegue, DevOps, Linux Journey"
---

Un programa recién iniciado puede estar en ejecución antes de poder atender peticiones. Comprueba el servicio por etapas para saber qué demuestra cada resultado positivo.

## Comprobar el proceso

La lista de contenedores puede confirmar que el programa principal está en marcha. Eso responde a una primera pregunta importante sobre el despliegue. Aún hay que comprobar si el programa terminó de iniciarse y si un navegador puede conectarse.

:::single-choice{#deployment-health-checks-process-scope} El nuevo contenedor aparece como Up. ¿Qué puedes concluir?

::option[Los visitantes reciben la página nueva con seguridad.]{#deployment-health-checks-process-scope-a explanation="El estado del contenedor no indica qué recibe un visitante."}
::option[El programa principal del contenedor está en ejecución en el momento de la comprobación.]{#deployment-health-checks-process-scope-b .correct explanation="Up indica el estado del proceso."}
::option[Todas las dependencias pasaron la comprobación.]{#deployment-health-checks-process-scope-c explanation="No se muestran los resultados de las dependencias."}
:::

## Comprobar un punto de acceso del servicio

Un **punto de acceso** es una dirección con una ruta que atiende el servicio. Usa una ruta que te permita comprobar el comportamiento que te interesa. Para probarlo localmente, parte de una carpeta de prácticas vacía. La redirección escribe el archivo de versión. Deja el servidor de Python en ejecución en este terminal, en la dirección de bucle local, y páralo con Ctrl+C al terminar.

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

Desde otro terminal, solicita el archivo de versión. La opción `-f` de curl trata las respuestas HTTP de error como fallos. `-sS` oculta los mensajes de progreso, pero sigue mostrando los errores.

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

En la práctica deberías obtener `2`. Una petición exitosa al archivo de versión cubre solo una pequeña parte de las pruebas del sitio.

:::single-choice{#deployment-health-checks-endpoint-mismatch} La petición tiene éxito y muestra 1. ¿Qué debes investigar?

::option[Qué versión responde en esa dirección.]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="La conexión funcionó, pero respondió una versión distinta de la prevista."}
::option[Por qué curl no se puede conectar.]{#deployment-health-checks-endpoint-mismatch-b explanation="El valor recibido confirma que hubo conexión y respuesta."}
::option[Si el nombre del servicio incluye un número.]{#deployment-health-checks-endpoint-mismatch-c explanation="El nombre del servicio no indica qué versión devolvió."}
:::

![Punto de acceso de bucle local que devuelve la versión 2 desde el servidor de prácticas de LabEx](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## Comprobar desde donde se conecta el cliente

Si la petición desde el anfitrión del servicio funciona, repite una comprobación segura desde donde suelen conectarse los usuarios. Un balanceador de carga, un proxy o una regla de red pueden cambiar la ruta de acceso. Anota la dirección comprobada y la respuesta recibida. Si el resultado no coincide con la versión esperada, sigue investigando el despliegue.

:::single-choice{#deployment-health-checks-user-path} Una petición local devuelve 2, pero la dirección pública de prueba devuelve 1. ¿Qué conviene comprobar ahora?

::option[Cuántas líneas mostró la petición local.]{#deployment-health-checks-user-path-a explanation="El número de líneas no identifica qué servicio atiende la dirección pública."}
::option[Repetir solo la misma comprobación local.]{#deployment-health-checks-user-path-b explanation="La ruta local ya devolvió la versión 2."}
::option[Qué versión del servicio atiende la ruta pública.]{#deployment-health-checks-user-path-c .correct explanation="Las dos rutas produjeron respuestas distintas."}
:::

## Resumen

Ya puedes explicar qué verificó cada comprobación posterior al despliegue.

1. Confirma que se ejecuta el programa principal.
2. Consulta un punto de acceso que muestre la versión esperada.
3. Verifica por separado la ruta que usan los usuarios.
