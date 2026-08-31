---
lesson_id: "dev-directory"
course_id: "devices"
lang: "es"
order_index: 1
title: "Directorio /dev"
description: "Aprende cómo Linux expone interfaces de dispositivos y seudodispositivos mediante nodos bajo `/dev`."
meta_title: "Directorio /dev - Dispositivos"
meta_description: "Descubre el propósito del directorio /dev de Linux, sus nodos de dispositivo y las interfaces de hardware que representan."
meta_keywords: "directorio /dev Linux, archivos de dispositivo, nodos de dispositivo, dispositivos Linux, ls /dev"
---

Linux expone muchas interfaces de dispositivos del kernel mediante objetos especiales del sistema de archivos llamados nodos de dispositivo. Normalmente aparecen bajo `/dev`, junto con enlaces simbólicos útiles y puntos de comunicación. Abrir un nodo de dispositivo conecta una aplicación con un controlador del kernel, no con bytes almacenados en un archivo ordinario.

## Explorar `/dev`

Muestra el directorio sin seguir los enlaces ni leer los dispositivos:

```bash
$ ls -l /dev
```

Las entradas pueden representar almacenamiento físico, terminales, interfaces de entrada, dispositivos lógicos o seudodispositivos proporcionados por el kernel. No todos los componentes de hardware necesitan un nodo visible para el usuario y un dispositivo puede estar representado mediante varios enlaces o interfaces.

El primer carácter de un listado largo identifica el tipo de objeto del sistema de archivos. Los nodos de dispositivos de caracteres y de bloques aparecen como `c` y `b`; lecciones posteriores examinan estos tipos y sus números mayor y menor.

:::single-choice{#dev-directory-device-node-purpose}
¿Qué ocurre cuando un programa abre un nodo de dispositivo bajo `/dev`?

::option[Siempre lee un archivo ordinario del disco que contiene una copia del hardware.]{#dev-directory-ordinary-copy explanation="Un nodo de dispositivo es un objeto especial y no almacena una copia de los datos del dispositivo como un archivo normal."}
::option[Accede a una interfaz implementada por un controlador del kernel.]{#dev-directory-kernel-interface .correct explanation="Las operaciones con nodos se encaminan mediante la identidad de dispositivo del nodo hacia el comportamiento del controlador del kernel."}
::option[Recompila el código fuente del controlador de ese dispositivo.]{#dev-directory-recompile-driver explanation="Abrir una interfaz no invoca un compilador ni vuelve a compilar módulos del kernel."}
:::

## Seudodispositivos

Algunos nodos proporcionan servicios del kernel sin corresponder a hardware físico. `/dev/null` acepta y descarta los datos escritos:

```bash
$ command > /dev/null
```

Otros ejemplos conocidos son `/dev/zero`, que produce bytes con valor cero, y `/dev/urandom`, que proporciona bytes aleatorios mediante el subsistema de aleatoriedad del kernel. Cada uno tiene una semántica específica; no deduzcas su comportamiento únicamente del nombre.

:::single-choice{#dev-directory-null-behavior}
¿Qué hace `/dev/null` con los datos que se escriben en él?

::option[Los almacena hasta el siguiente reinicio.]{#dev-directory-null-temporary-storage explanation="El dispositivo nulo es un sumidero y no actúa como almacenamiento temporal."}
::option[Los envía a todas las terminales con una sesión abierta.]{#dev-directory-null-broadcast explanation="La difusión a terminales no guarda relación con el seudodispositivo nulo."}
::option[Los descarta.]{#dev-directory-null-discards .correct explanation="El dispositivo nulo acepta escrituras sin conservar su contenido."}
:::

## Gestión dinámica de dispositivos

En los sistemas Linux modernos, `devtmpfs`, respaldado por el kernel, puede crear los nodos de dispositivo básicos a medida que aparecen los dispositivos. Un gestor de dispositivos en el espacio de usuario, como `udev`, procesa sucesos, aplica permisos y propiedad, y crea enlaces simbólicos útiles o nombres basados en políticas. Las responsabilidades exactas varían según el sistema.

Los enlaces estables, como las entradas bajo `/dev/disk/by-id/` o `/dev/disk/by-uuid/`, pueden ser más seguros en la configuración que los nombres basados en el orden de detección, como `/dev/sda`, que pueden cambiar al modificarse la topología del hardware o el orden de descubrimiento.

:::single-choice{#dev-directory-persistent-link}
¿Por qué puede preferir un administrador `/dev/disk/by-id/...` a `/dev/sda` en una configuración?

::option[Porque el enlace basado en un identificador depende menos del orden de detección de dispositivos.]{#dev-directory-stable-identifier .correct explanation="Los enlaces persistentes se derivan de propiedades del dispositivo en vez de una letra asignada por el orden de enumeración."}
::option[Porque el enlace crea automáticamente una copia de seguridad de todos los bloques del dispositivo.]{#dev-directory-link-backup explanation="Un enlace simbólico designa el mismo dispositivo y no crea datos de respaldo."}
::option[Porque el enlace evita todos los permisos del dispositivo de destino.]{#dev-directory-link-permissions explanation="Abrir mediante un enlace simbólico sigue alcanzando el dispositivo de destino y sus controles de acceso."}
:::

## Interactuar de forma segura

Las herramientas estándar pueden abrir nodos de dispositivo, pero eso no convierte las lecturas y escrituras arbitrarias en operaciones seguras. Leer puede exponer entradas o almacenamiento confidenciales; escribir en un disco, una terminal o una interfaz de firmware puede corromper datos o molestar a los usuarios. Por esa razón, los permisos, grupos, ACL, capacidades y servicios intermediarios restringen el acceso a los nodos.

Utiliza primero herramientas de descubrimiento de solo lectura, confirma el nodo exacto y la identidad del dispositivo, y sigue la documentación específica del dispositivo. Nunca experimentes redirigiendo datos a una entrada desconocida de `/dev` en un sistema que te importe.

:::single-choice{#dev-directory-direct-write-risk}
¿Por qué debes evitar escribir datos arbitrarios en un nodo de dispositivo desconocido?

::option[Porque se garantiza que todos los nodos de dispositivo son archivos de texto inofensivos.]{#dev-directory-harmless-text explanation="Los nodos de dispositivo no son precisamente archivos de texto ordinarios."}
::option[Porque la operación puede afectar directamente al hardware, al almacenamiento o a otra interfaz del kernel.]{#dev-directory-write-impact .correct explanation="Las escrituras en dispositivos invocan operaciones definidas por el controlador y pueden tener efectos destructivos o perturbadores."}
::option[Porque Linux convierte todas las escrituras en dispositivos en listados de solo lectura.]{#dev-directory-write-listing explanation="El controlador decide la semántica de escritura; el kernel no convierte universalmente las escrituras en listados."}
:::

Utiliza [Explorar dispositivos de hardware en Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para realizar una inspección de solo lectura en un entorno controlado.

## Resumen

Ahora puedes describir `/dev` como un conjunto de interfaces activas orientadas al kernel.

1. Distingue los nodos de dispositivo de los archivos ordinarios.
2. Reconoce seudodispositivos como `/dev/null`.
3. Relaciona los nodos dinámicos y los enlaces persistentes con la gestión de dispositivos.
4. Trata el acceso directo a dispositivos como algo específico de cada interfaz y potencialmente destructivo.
