---
lesson_id: "simple-http-server"
course_id: "network-sharing"
lang: "es"
order_index: 3
title: "Servidor HTTP sencillo"
description: "Aprende a exponer temporalmente un directorio controlado mediante el servidor HTTP de Python."
meta_title: "Servidor HTTP sencillo - Network Sharing"
meta_description: "Aprende a configurar rápidamente un servidor HTTP sencillo en Linux mediante el módulo http.server de Python. Esta guía explica cómo crear un servidor web simple para compartir archivos en tu red."
meta_keywords: "servidor http sencillo linux, servidor http simple linux, servidor web linux sencillo, python http.server, qué es python simplehttpserver, intercambio de archivos, servidor de red"
---

El módulo `http.server` de Python puede servir archivos estáticos para una prueba breve o una transferencia de confianza. No es un servidor web de producción y no proporciona autenticación, autorización, TLS, limitación de frecuencia ni un tratamiento reforzado del tráfico hostil.

## Preparar un directorio compartido

Crea un directorio dedicado que solo contenga archivos destinados a exponerse. Revisa los archivos ocultos, los enlaces simbólicos, los permisos y los metadatos sensibles antes de iniciarlo. Evita servir un directorio personal, la raíz de un repositorio, un directorio de credenciales o una ruta del sistema.

Utiliza `--directory` para que la raíz compartida sea explícita:

```bash
$ python3 -m http.server 8000 --directory /srv/temporary-share
```

Cuando no hay un archivo de índice, el módulo normalmente genera un listado del directorio. Cualquier persona que pueda llegar al listener puede enumerar y descargar el contenido servido.

:::single-choice{#http-server-directory-option}
¿Por qué debes utilizar `--directory /srv/temporary-share`?

::option[Cifra automáticamente todas las respuestas HTTP.]{#http-server-directory-tls explanation="La opción de directorio no añade TLS."}
::option[Crea una cuenta para cada persona que descarga.]{#http-server-directory-accounts explanation="El módulo básico no proporciona autenticación de usuarios."}
::option[Hace explícita la raíz de documentos prevista.]{#http-server-explicit-root .correct explanation="Una raíz explícita y revisada reduce la posibilidad de exponer archivos de un directorio de trabajo accidental."}
:::

## Controlar la dirección de escucha

Vincula a loopback cuando solo deba conectarse el mismo host:

```bash
$ python3 -m http.server 8000 --bind 127.0.0.1 --directory /srv/temporary-share
```

Para compartir en una red de confianza, vincula deliberadamente a una dirección de interfaz apropiada y confirma la política del cortafuegos. Ejecutarlo sin una vinculación restrictiva suele escuchar en todas las interfaces disponibles, lo que puede exponer el directorio más allá de la red prevista.

:::single-choice{#http-server-loopback-bind}
¿Quién puede llegar normalmente a un servidor vinculado a `127.0.0.1`?

::option[Los clientes del mismo host.]{#http-server-local-clients .correct explanation="La vinculación a loopback es apropiada para pruebas locales o para utilizarse detrás de un túnel configurado deliberadamente."}
::option[Cualquier host de Internet público.]{#http-server-public explanation="Loopback es local al mismo espacio de nombres de red y no es una interfaz pública."}
::option[Únicamente los dispositivos conectados mediante Bluetooth.]{#http-server-bluetooth explanation="La dirección no está relacionada con el transporte Bluetooth."}
:::

## Probar el acceso

Desde el host que sirve los archivos, solicita un archivo conocido e inspecciona la respuesta:

```bash
$ curl -f http://127.0.0.1:8000/example.txt
```

Para una prueba remota autorizada, utiliza la dirección de la interfaz seleccionada en lugar de loopback. Confirma tanto que el archivo previsto sea accesible como que uno situado fuera de la raíz de documentos no lo sea. Que el navegador funcione no demuestra por sí solo que la exposición o la confidencialidad sean apropiadas.

:::single-choice{#http-server-default-port-command}
¿Qué puerto se selecciona explícitamente en `python3 -m http.server 8000`?

::option[22]{#http-server-port-22 explanation="El puerto 22 suele asociarse con SSH y no se selecciona aquí."}
::option[8000]{#http-server-port-8000 .correct explanation="El operando posicional del puerto indica al módulo dónde escuchar."}
::option[443]{#http-server-port-443 explanation="El comando no configura HTTPS en el puerto 443."}
:::

## Detener y limpiar

Ejecuta el servicio temporal en una terminal supervisada y detenlo con `Ctrl-C` cuando termine la transferencia. Comprueba que el listener haya desaparecido:

```bash
$ ss -ltn 'sport = :8000'
```

Elimina las copias temporales según la política de tratamiento de datos y revierte cualquier regla temporal del cortafuegos. Para una distribución persistente, autenticada o expuesta a Internet, utiliza un servidor mantenido y configurado con control de acceso y TLS.

:::single-choice{#http-server-completion-check}
¿Qué debe ocurrir después de completar la transferencia temporal?

::option[Detener el servidor y comprobar que el puerto ya no esté a la escucha.]{#http-server-stop-verify .correct explanation="La comprobación confirma que el servicio de red temporal terminó realmente."}
::option[Dejar el listener en ejecución por si alguien lo necesita más adelante.]{#http-server-leave-running explanation="La exposición innecesaria debe eliminarse cuando termina la finalidad autorizada."}
::option[Copiar más archivos privados en la raíz de documentos.]{#http-server-add-private explanation="Solo el contenido que se comparte deliberadamente debe estar en el directorio servido."}
:::

## Resumen

Ahora puedes ejecutar un servidor HTTP temporal de Python con una exposición limitada.

1. Sirve únicamente un directorio dedicado y revisado.
2. Vincula a la dirección apropiada más restrictiva.
3. Prueba el acceso previsto y los límites no deseados.
4. Detén el listener y elimina después el acceso temporal.
