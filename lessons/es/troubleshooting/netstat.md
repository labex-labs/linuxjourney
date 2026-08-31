---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "es"
order_index: 4
title: "netstat"
description: "Aprende a inspeccionar sockets, listeners, colas y estados TCP de Linux con ss."
meta_title: "netstat - Resolución de problemas"
meta_description: "Domina netstat y ss en Linux para analizar conexiones de red, puertos, sockets y estados como SYN-SENT y CLOSE-WAIT."
meta_keywords: "netstat Linux, netstat, orden netstat, syn_sent netstat, netstat close_wait, conexiones de red, redes Linux, análisis de red, tutorial Linux"
---

La herramienta antigua `netstat` muestra sockets, rutas y estadísticas de interfaces. En Linux moderno, `ss` es la herramienta preferida para inspeccionar sockets porque expone con eficiencia su estado en el kernel y se mantiene junto con iproute2.

## Enumerar sockets a la escucha

Muestra numéricamente los sockets TCP y UDP a la escucha, incluidos los procesos propietarios cuando esté permitido:

```bash
$ sudo ss -lntup
```

`-l` selecciona listeners, `-n` evita la resolución de nombres, `-t` y `-u` seleccionan TCP y UDP, y `-p` solicita datos de procesos. UDP no usa conexiones, por lo que sus sockets vinculados sin conexión no tienen negociaciones `LISTEN` como TCP.

:::single-choice{#netstat-ss-numeric}
¿Por qué se utiliza `-n` al diagnosticar sockets?

::option[Crea un nuevo espacio de nombres de red.]{#netstat-new-namespace explanation="La opción controla la resolución de nombres en la salida."}
::option[Evita buscar nombres para las direcciones y los puertos.]{#netstat-numeric-output .correct explanation="La salida numérica evita confundir una asignación de nombre de servicio con la identidad observada del protocolo."}
::option[Cierra todos los sockets que no están a la escucha.]{#netstat-close-sockets explanation="La inspección no termina sockets."}
:::

## Puertos, extremos y servicios

Un extremo de socket local combina una dirección, un protocolo de transporte y un puerto. Una conexión TCP se distingue por el protocolo y las direcciones y puertos de origen y destino. `/etc/services` asigna nombres convencionales a números, pero no demuestra qué proceso posee un puerto en ese momento ni qué protocolo de aplicación utiliza.

:::single-choice{#netstat-services-file-limit}
¿Qué establece una entrada de `/etc/services` como `https 443/tcp`?

::option[Que un servidor HTTPS en buen estado está a la escucha en ese momento.]{#netstat-healthy-listener explanation="Una base de datos estática de nombres no demuestra el estado de ejecución."}
::option[La asignación convencional de un nombre de servicio a ese puerto.]{#netstat-conventional-name .correct explanation="La propiedad del socket y el comportamiento real del protocolo requieren inspección y pruebas en ejecución."}
::option[Que todo el tráfico del puerto 443 está cifrado correctamente.]{#netstat-all-encrypted explanation="Un número de puerto no puede validar el comportamiento de TLS."}
:::

## Leer los estados TCP

Algunos estados habituales son:

- `SYN-SENT`: el extremo local envió una solicitud de conexión y espera que avance.
- `ESTAB`: la conexión TCP está establecida.
- `CLOSE-WAIT`: el par cerró su lado emisor, pero la aplicación local no ha cerrado su socket.
- `TIME-WAIT`: el extremo que cerró activamente espera para que caduquen los segmentos retrasados y el intercambio final pueda manejarse de forma segura.

Una población grande o creciente de `CLOSE-WAIT` suele apuntar al comportamiento de limpieza de la aplicación local. `TIME-WAIT` es un estado normal del protocolo; su cantidad y el impacto sobre los recursos determinan si supone un problema operativo.

:::single-choice{#netstat-close-wait-owner}
¿Qué lado todavía debe cerrar un socket en `CLOSE-WAIT`?

::option[Todos los routers de Internet.]{#netstat-all-routers-close explanation="Los routers no son propietarios del socket del extremo."}
::option[El servidor DNS autoritativo.]{#netstat-dns-close explanation="El servicio de nombres no guarda relación con el cierre TCP local."}
::option[La aplicación local.]{#netstat-local-close .correct explanation="TCP recibió el FIN del par y espera a que el proceso local cierre su lado."}
:::

## Interpretar las colas

El significado de `Recv-Q` y `Send-Q` depende del estado y el protocolo. En sockets TCP establecidos pueden indicar datos en espera de recepción por la aplicación o de confirmación de transmisión. En sockets a la escucha, los campos de cola describen el estado de la acumulación de conexiones, no bytes de carga útil de la aplicación de la misma manera.

Una sola instantánea no permite confirmar una fuga o un cuello de botella. Toma muestras a lo largo del tiempo y correlaciónalas con el comportamiento del proceso, la latencia de la aplicación, las retransmisiones y los límites de recursos.

:::single-choice{#netstat-queue-snapshot}
¿Por qué una sola instantánea de una cola de sockets grande no basta para diagnosticar?

::option[Linux nunca almacena datos en colas de sockets.]{#netstat-no-queues explanation="La red del kernel depende de colas de envío y recepción."}
::option[Cada valor de cola es un permiso del sistema de archivos.]{#netstat-queue-permission explanation="Los campos describen el estado de la red."}
::option[El impacto de la cola requiere conocer el estado, la tendencia y el contexto de la carga.]{#netstat-queue-context .correct explanation="Una ráfaga transitoria difiere de un cuello de botella sostenido en la aplicación o la red."}
:::

## Filtrar una investigación

Limita la salida al protocolo, estado, extremo o proceso investigado:

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

Un listener demuestra que el transporte local está preparado, no que sea accesible de forma remota ni que la aplicación funcione correctamente. Continúa con pruebas de ruta, cortafuegos, paquetes, TLS y aplicación adecuadas para el síntoma.

:::single-choice{#netstat-listener-limit}
¿Qué no demuestra un listener TCP en el puerto 443?

::option[Que un socket local aceptó las operaciones bind y listen.]{#netstat-listen-local explanation="Ese es precisamente el estado local que se muestra."}
::option[Que los clientes remotos pueden completar una solicitud HTTPS válida.]{#netstat-not-remote-proof .correct explanation="La política de la ruta, TLS y el comportamiento de la aplicación siguen sin probarse."}
::option[Que TCP tiene un campo de puerto numérico.]{#netstat-port-field explanation="La salida del listener incluye uno directamente."}
:::

## Resumen

Ahora puedes utilizar `ss` para inspeccionar el estado de los sockets sin confundir los puertos con las aplicaciones.

1. Enumera listeners numéricamente con el contexto de sus procesos.
2. Distingue los nombres de servicio convencionales de la propiedad en ejecución.
3. Interpreta los estados de cierre TCP desde la perspectiva del extremo local.
4. Toma muestras de las colas a lo largo del tiempo y con el contexto de la carga.
5. Verifica el comportamiento remoto de la aplicación más allá del listener local.
