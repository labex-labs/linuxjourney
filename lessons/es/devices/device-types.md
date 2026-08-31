---
lesson_id: "device-types"
course_id: "devices"
lang: "es"
order_index: 2
title: "Tipos de dispositivos"
description: "Aprende a distinguir los nodos de dispositivos de caracteres y de bloques de las tuberías, los sockets y los objetos normales del sistema de archivos."
meta_title: "Tipos de dispositivos - Dispositivos"
meta_description: "Explora los dispositivos de caracteres y bloques, las tuberías, los sockets y los números mayor y menor de Linux."
meta_keywords: "tipos de dispositivos Linux, nodo de dispositivo, dispositivo de caracteres, dispositivo de bloques, números mayor y menor"
---

El primer carácter del modo que muestra `ls -l` identifica el tipo de objeto del sistema de archivos. Bajo `/dev`, los archivos especiales de caracteres y de bloques son nodos de dispositivo. También pueden aparecer nodos de tuberías y sockets de dominio Unix, pero son objetos de comunicación entre procesos, no nodos de dispositivos de hardware.

```text
$ ls -l /dev/null /dev/sda /run/systemd/journal/dev-log /tmp/example-fifo
crw-rw-rw- 1 root root 1, 3 ... /dev/null
brw-rw---- 1 root disk 8, 0 ... /dev/sda
srw-rw-rw- 1 root root      ... /run/systemd/journal/dev-log
prw------- 1 user user      ... /tmp/example-fifo
```

Las entradas y los permisos varían según el sistema; el ejemplo solo ilustra los caracteres de tipo.

## Nodos de dispositivos de caracteres

Una `c` identifica un dispositivo de caracteres. Suele exponer una interfaz orientada a flujos o específica del dispositivo en vez de bloques de almacenamiento de tamaño fijo direccionables. Algunos ejemplos son las terminales y seudodispositivos como `/dev/null`.

«Carácter» no exige que cada llamada al sistema transfiera exactamente un carácter. Las aplicaciones pueden leer o escribir búferes, mientras que el controlador define el bloqueo, el encuadre y el comportamiento de control.

:::single-choice{#device-types-character-marker}
¿Qué primer carácter del modo identifica un nodo de dispositivo de caracteres?

::option[`b`]{#device-types-marker-block explanation="El marcador `b` identifica un nodo de dispositivo de bloques."}
::option[`p`]{#device-types-marker-pipe explanation="El marcador `p` identifica una FIFO o tubería con nombre."}
::option[`c`]{#device-types-marker-character .correct explanation="Los archivos especiales de caracteres muestran `c` al principio del modo de un listado largo."}
:::

## Nodos de dispositivos de bloques

Una `b` identifica un dispositivo de bloques. Los dispositivos de bloques proporcionan almacenamiento direccionable en bloques mediante la capa de bloques del kernel y pueden admitir operaciones como E/S con búfer, particionado y sistemas de archivos. Los discos, las particiones y los volúmenes lógicos suelen tener nodos de bloques.

Un nodo de bloques no es un sistema de archivos montado. Representa un dispositivo de almacenamiento o una región lógica; se puede crear un sistema de archivos en él y montarlo por separado. Escribir datos sin procesar en el nodo de bloques equivocado puede destruir tablas de particiones, sistemas de archivos o datos de usuarios.

:::single-choice{#device-types-block-marker}
¿Qué indica el primer carácter de modo `b`?

::option[Un trabajo del shell en segundo plano.]{#device-types-background-job explanation="El estado de los trabajos del shell no se codifica como un carácter de tipo del sistema de archivos."}
::option[Una interfaz de dispositivo de bloques.]{#device-types-block-device .correct explanation="Los archivos especiales de bloques exponen almacenamiento direccionable mediante el subsistema de bloques del kernel."}
::option[Un enlace simbólico roto.]{#device-types-broken-link explanation="Los enlaces simbólicos utilizan `l`, exista o no su destino en ese momento."}
:::

## FIFO y nodos de socket

Una `p` identifica una FIFO, también llamada tubería con nombre. Proporciona un flujo de bytes con nombre mediante el cual pueden comunicarse los procesos. Los datos no se almacenan de forma persistente en el nodo FIFO después de ser consumidos.

Una `s` identifica un nodo de socket de dominio Unix. Da nombre a un extremo de socket local y puede admitir comunicación orientada a conexiones o mediante datagramas, transferencia de descriptores y funciones de credenciales del par. Los sockets de red que utilizan direcciones de Internet no tienen necesariamente nodos en el sistema de archivos.

Ni una FIFO ni un nodo de socket Unix utilizan números mayor y menor de dispositivo para seleccionar un controlador de hardware.

:::single-choice{#device-types-pipe-socket-distinction}
¿Qué afirmación distingue correctamente estos tipos de objetos de comunicación entre procesos?

::option[`p` marca una partición de disco y `s` marca almacenamiento de estado sólido.]{#device-types-storage-letters explanation="Las particiones suelen ser dispositivos de bloques y las letras no codifican la tecnología de almacenamiento."}
::option[`p` marca una FIFO y `s` marca un nodo de socket de dominio Unix.]{#device-types-p-and-s .correct explanation="Son tipos distintos de objetos del sistema de archivos utilizados para la comunicación local entre procesos."}
::option[Ambos tipos identifican controladores de bloques del kernel mediante números mayores.]{#device-types-ipc-major explanation="Los nodos FIFO y de socket no son nodos de dispositivos de caracteres ni de bloques."}
:::

## Números mayor y menor de dispositivo

Los nodos de dispositivos de caracteres y de bloques almacenan un número de dispositivo dividido en componentes mayor y menor. En un listado largo sustituyen la columna habitual del tamaño del archivo:

```text
brw-rw---- 1 root disk 8, 0 ... /dev/sda
```

El par indica al kernel la interfaz de dispositivo registrada y la instancia a las que se dirige el nodo. Un número mayor se asocia con un controlador o una clase de dispositivo, mientras que el controlador interpreta el número menor. No codifiques supuestos como «el número menor cero siempre significa la primera unidad»; las correspondencias dependen del subsistema y de las interfaces del kernel.

Muestra explícitamente el tipo y los números de dispositivo con:

```bash
$ stat -c 'type=%F major=%t minor=%T path=%n' /dev/null
```

GNU `stat` muestra los valores `%t` y `%T` en hexadecimal.

:::single-choice{#device-types-major-minor-scope}
¿Qué objetos utilizan números mayor y menor para identificar una interfaz de dispositivo del kernel?

::option[Todos los archivos normales y directorios.]{#device-types-all-files explanation="Los archivos normales utilizan el tamaño y los metadatos del sistema de archivos, no un par mayor/menor de nodo de dispositivo."}
::option[Únicamente los enlaces simbólicos cuyo destino no existe.]{#device-types-broken-symlinks explanation="Los enlaces simbólicos almacenan texto de ruta y no se convierten en nodos de dispositivo cuando falta el destino."}
::option[Los nodos de dispositivos de caracteres y de bloques.]{#device-types-device-number-nodes .correct explanation="Los metadatos especiales de sus inodos contienen el número de dispositivo que se encamina a una interfaz del controlador."}
:::

## Resumen

Ahora puedes interpretar tipos especiales del sistema de archivos sin tratar todos ellos como dispositivos de hardware.

1. Interpreta `c` como nodo de dispositivo de caracteres y `b` como nodo de dispositivo de bloques.
2. Interpreta `p` como FIFO y `s` como nodo de socket de dominio Unix.
3. Asocia los números mayor y menor únicamente con nodos de dispositivo.
4. Trata el acceso directo a dispositivos de bloques como potencialmente destructivo.
