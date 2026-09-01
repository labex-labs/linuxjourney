---
lesson_id: "sysfs"
course_id: "devices"
lang: "es"
order_index: 4
title: "sysfs"
description: "Aprende cómo sysfs expone el modelo actual de dispositivos, controladores, buses y clases del kernel de Linux bajo `/sys`."
meta_title: "sysfs - Dispositivos"
meta_description: "Explora sysfs y el directorio virtual /sys de Linux, que expone información de dispositivos y objetos del kernel."
meta_keywords: "sysfs, /sys Linux, sistema de archivos virtual, dispositivos Linux, controladores Linux, /dev"
---

`sysfs` es un sistema de archivos virtual que normalmente se monta en `/sys`. Representa objetos del kernel y sus relaciones mediante directorios, enlaces simbólicos y pequeños archivos de atributos. Las herramientas y los gestores de descubrimiento de dispositivos lo utilizan para comprender el modelo actual de dispositivos del kernel.

## Recorrer el modelo de dispositivos

Entre las vistas importantes del nivel superior se encuentran:

- `/sys/devices/`: la jerarquía de dispositivos físicos y lógicos
- `/sys/class/`: dispositivos agrupados por clase funcional, como bloques o red
- `/sys/bus/`: buses, sus dispositivos y controladores
- `/sys/block/`: una vista práctica de los dispositivos de bloques
- `/sys/dev/`: enlaces indexados por los números mayor y menor de dispositivos de caracteres o bloques

Muchas entradas situadas fuera de `/sys/devices` son enlaces simbólicos hacia la jerarquía canónica. Resuelve un enlace con `readlink -f` cuando necesites la ruta real del padre:

```bash
$ readlink -f /sys/class/block/sda
```

El nombre del ejemplo puede no existir en sistemas que utilicen otras interfaces de almacenamiento.

:::single-choice{#sysfs-canonical-device-tree} ¿Qué subárbol de sysfs contiene la jerarquía principal de dispositivos del kernel?

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="Sysfs no es un repositorio de secretos de autenticación de usuarios."}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="El subárbol devices representa la topología padre-hijo de los dispositivos; las vistas de clases y buses enlazan con él."}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="Las herramientas de paquetes de la distribución, no esta ruta de sysfs, mantienen el estado de los paquetes instalados."}
:::

## Leer atributos

Los archivos de atributos exponen valores o controles individuales. En un dispositivo de bloques, algunos ejemplos pueden ser:

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev` comunica los números mayor y menor del dispositivo. `ro` comunica el indicador de solo lectura del dispositivo de bloques. En los dispositivos de bloques de Linux, `size` se expresa convencionalmente en sectores de 512 bytes, con independencia del tamaño de sector físico del dispositivo. Consulta siempre la documentación de la ABI del kernel para conocer las unidades y el significado de un atributo concreto.

:::single-choice{#sysfs-dev-attribute} ¿Qué contiene normalmente el atributo `dev` de sysfs de un dispositivo de bloques?

::option[Todos los archivos almacenados en ese momento en el dispositivo.]{#sysfs-file-list explanation="El árbol de directorios de un sistema de archivos no está incrustado en este pequeño atributo de dispositivo."}
::option[El nombre del paquete que instaló el hardware.]{#sysfs-package-name explanation="El hardware no se instala como un paquete identificado por el atributo `dev`."}
::option[Sus números mayor y menor de dispositivo.]{#sysfs-major-minor .correct explanation="El atributo conecta el objeto de sysfs con la identidad del dispositivo de bloques correspondiente."}
:::

## Relacionar `/sys` y `/dev`

`/dev` contiene nodos que las aplicaciones abren para realizar E/S con dispositivos. `/sys` expone relaciones entre objetos, propiedades, estado y determinados controles. Un nodo de bloques como `/dev/sda` puede corresponderse con `/sys/dev/block/8:0`, que se resuelve al objeto de sysfs pertinente.

Las dos interfaces se complementan. Ninguna contiene por sí sola un inventario completo de todos los datos del hardware, y un dispositivo puede desaparecer mientras se examina.

:::single-choice{#sysfs-versus-dev} ¿Qué afirmación distingue correctamente `/sys` de `/dev`?

::option[`/sys` almacena documentos de usuarios y `/dev` almacena archivos de paquetes.]{#sysfs-dev-user-files explanation="Ninguno de los dos directorios cumple esas funciones de almacenamiento de datos ordinarios."}
::option[`/sys` expone atributos de objetos del kernel y `/dev` proporciona nodos de dispositivo para E/S.]{#sysfs-dev-distinction .correct explanation="Sysfs modela objetos y controles, mientras que los nodos de dispositivo encaminan operaciones hacia controladores de caracteres o de bloques."}
::option[Ambos son listas estáticas creadas una sola vez durante la instalación.]{#sysfs-dev-static explanation="Su estado visible cambia cuando aparecen o desaparecen dispositivos y objetos del kernel."}
:::

## Escribir atributos de forma segura

Algunos atributos de sysfs permiten escrituras que pueden cambiar el estado de energía, la vinculación de controladores, el comportamiento de las colas, la autorización de dispositivos, los LED u otros controles activos. Una escritura de texto correcta puede tener efectos inmediatos en el hardware o en los servicios; no equivale a editar un archivo de configuración persistente.

Lee la ABI documentada y el valor actual, identifica cómo debe hacerse persistente el ajuste y realiza pruebas únicamente en un sistema autorizado. Nunca cambies recursivamente permisos ni escribas valores adivinados por todo `/sys`.

:::single-choice{#sysfs-write-risk} ¿Por qué puede ser importante para el funcionamiento escribir en un atributo de sysfs?

::option[Porque cada escritura crea una copia de seguridad ordinaria en disco.]{#sysfs-backup-copy explanation="Sysfs es virtual y no proporciona copias de seguridad automáticas de los cambios de control."}
::option[Porque sysfs ignora todas las escrituras incluso cuando un atributo permite escribir.]{#sysfs-ignore-writes explanation="Los atributos que permiten escrituras existen precisamente para aceptar valores de control compatibles."}
::option[Porque la escritura puede invocar un control activo del kernel o de un controlador.]{#sysfs-live-control .correct explanation="Los atributos que permiten escrituras son interfaces activas y pueden modificar inmediatamente el comportamiento del dispositivo."}
:::

Utiliza [Explorar dispositivos de hardware en Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para recorrer sysfs en modo de solo lectura y relacionarlo con nodos de dispositivo.

## Resumen

Ahora puedes utilizar sysfs como una vista estructurada de los objetos activos del kernel.

1. Recorre las vistas de dispositivos, clases, buses, bloques y números de dispositivo.
2. Lee un atributo documentado cada vez y utiliza las unidades correctas.
3. Relaciona los objetos de sysfs con los nodos de `/dev`.
4. Trata los atributos que permiten escrituras como interfaces de control activas.
