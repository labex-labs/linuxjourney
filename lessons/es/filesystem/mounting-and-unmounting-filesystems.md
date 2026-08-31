---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "es"
order_index: 6
title: "mount y umount"
description: "Aprende a conectar, examinar y desconectar de forma segura sistemas de archivos mediante fuentes y puntos de montaje verificados."
meta_title: "mount y umount - El sistema de archivos"
meta_description: "Aprende a montar y desmontar sistemas de archivos Linux con mount y umount mediante dispositivos y UUID verificados."
meta_keywords: "mount, umount, montar sistema de archivos, desmontar dispositivo, UUID Linux, punto de montaje"
---

Montar conecta un sistema de archivos con un directorio del espacio de nombres visible. La fuente puede ser un dispositivo de bloques, una exportación de red, un sistema de archivos virtual, una fuente de montaje enlazado u otro objeto específico de una implementación. El directorio de destino se llama punto de montaje.

## Preparar y examinar un punto de montaje

Crea un directorio con un nombre deliberado cuando la política local lo requiera:

```bash
$ sudo mkdir -p /mnt/mydrive
```

Examínalo antes de montar:

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

Montar sobre un directorio no vacío oculta sus entradas existentes tras el sistema de archivos nuevo hasta que se desmonta; no las elimina. Esto puede confundir a las aplicaciones y consumir espacio en disco de forma invisible, así que utiliza un punto de montaje vacío y dedicado.

:::single-choice{#mount-umount-nonempty-target}
¿Qué ocurre con los archivos existentes de un directorio cuando se monta otro sistema de archivos en él?

::option[Se copian automáticamente al sistema de archivos nuevo.]{#mount-umount-copied-files explanation="Montar cambia la conexión del espacio de nombres y no migra el contenido del directorio."}
::option[El kernel los elimina permanentemente.]{#mount-umount-erased-files explanation="Los archivos suelen reaparecer después de desmontar porque estaban ocultos, no eliminados."}
::option[El montaje los oculta hasta que se desconecta.]{#mount-umount-hidden-files .correct explanation="El directorio subyacente permanece, pero la resolución de rutas entra en el sistema de archivos montado."}
:::

## Montar un sistema de archivos verificado

Después de confirmar la identidad de la fuente, el tipo detectado y el contenido esperado, monta explícitamente:

```bash
$ sudo mount -t ext4 /dev/VERIFIED-PARTITION /mnt/mydrive
```

La opción `-t` indica la implementación del sistema de archivos. Mount suele poder detectar el tipo, pero un tipo explícito y opciones revisadas aclaran la intención. Para contenido extraíble o que no sea de confianza, considera opciones restrictivas como `ro`, `nosuid`, `nodev` y `noexec` cuando correspondan a la carga; cada una tiene limitaciones y no debe tratarse como un entorno aislado completo.

Verifica lo que está montado realmente:

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

Los montajes se limitan a espacios de nombres. Un montaje creado en un contenedor o en el espacio privado de un servicio puede no aparecer en la vista de otro proceso.

:::single-choice{#mount-umount-mount-role}
¿Qué hace la orden `mount` en el flujo de trabajo mostrado?

::option[Crea un sistema de archivos nuevo y borra la fuente.]{#mount-umount-format-source explanation="Crear un sistema de archivos es una operación destructiva independiente realizada con `mkfs`."}
::option[Conecta una fuente de sistema de archivos con un directorio de un espacio de nombres de montajes.]{#mount-umount-attach-filesystem .correct explanation="La resolución de rutas bajo el destino entra entonces en el sistema de archivos conectado."}
::option[Cambia los límites de las particiones del disco.]{#mount-umount-change-partitions explanation="Editar la tabla de particiones es independiente de montar en un espacio de nombres."}
:::

## Utilizar UUID de sistemas de archivos

Los nombres de enumeración como `/dev/sdb2` pueden cambiar. Descubre identificadores de sistemas de archivos con:

```bash
$ lsblk -f
$ sudo blkid
```

Después monta un sistema de archivos verificado mediante su UUID:

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

Un UUID identifica el sistema de archivos, no necesariamente el disco físico. Darle otro formato lo cambia, mientras que clonarlo puede duplicarlo. Verifica la unicidad antes de conectar el original y el clon al mismo sistema.

:::single-choice{#mount-umount-uuid-benefit}
¿Por qué suele ser preferible un UUID del sistema de archivos a `/dev/sdX` para una configuración persistente?

::option[Porque evita que fallen los dispositivos de almacenamiento.]{#mount-umount-uuid-no-failure explanation="Un identificador no proporciona redundancia, reparación de integridad ni copias de seguridad."}
::option[Porque garantiza que los sistemas de archivos clonados tengan identificadores distintos.]{#mount-umount-uuid-clone-unique explanation="Un clon a nivel de bloques puede copiar el UUID y provocar una colisión."}
::option[Porque está vinculado a la identidad del sistema de archivos y no al orden de enumeración actual.]{#mount-umount-uuid-identity .correct explanation="La ruta del dispositivo de bloques puede cambiar mientras los metadatos del sistema de archivos conservan su UUID."}
:::

## Desmontar de forma segura

Desconecta mediante el punto de montaje exacto:

```bash
$ sudo umount /mnt/mydrive
```

La orden se escribe `umount`, sin la primera `n`. Un desmontaje correcto desconecta el sistema de archivos después de que el kernel complete las escrituras pendientes necesarias y las referencias lo permitan. Confirma después con `findmnt` antes de desconectar el almacenamiento.

Un desmontaje correcto no siempre es la última operación necesaria para retirar con seguridad un medio extraíble. Las pilas de almacenamiento de escritorio pueden ofrecer una acción de expulsión o apagado que vacíe las cachés del dispositivo y desactive un dispositivo USB. Sigue el flujo de trabajo de la plataforma y el hardware.

:::single-choice{#mount-umount-command-name}
¿Qué orden desconecta `/mnt/mydrive`?

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount` desconecta el sistema de archivos montado en el destino indicado."}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="El nombre de la orden estándar omite la primera `n`."}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="Mkfs crea estructuras de sistemas de archivos y no debe utilizarse para desconectar."}
:::

## Diagnosticar un sistema de archivos ocupado

El desmontaje falla cuando el espacio de nombres todavía contiene referencias activas, como archivos abiertos, el directorio de trabajo de un proceso, montajes anidados, intercambio u otras capas de almacenamiento. Investiga en vez de forzarlo de inmediato:

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

Saca los shells del árbol, detén limpiamente la aplicación responsable y desmonta los montajes hijos antes que el padre. Las opciones de desmontaje diferido y forzoso tienen una semántica especializada y pueden dejar referencias activas o arriesgar datos; utilízalas únicamente con un razonamiento de recuperación documentado.

:::single-choice{#mount-umount-busy-cause}
¿Qué condición puede hacer que `umount` comunique que un sistema de archivos está ocupado?

::option[Que el nombre del directorio del punto de montaje contenga letras minúsculas.]{#mount-umount-lowercase explanation="El uso de mayúsculas o minúsculas en la ruta no crea por sí solo una referencia activa al sistema de archivos."}
::option[Que un proceso tenga su directorio de trabajo actual dentro del montaje.]{#mount-umount-cwd-busy .correct explanation="El proceso conserva una referencia al sistema de archivos montado, lo que impide la desconexión ordinaria."}
::option[Que el UUID sea más largo que el nombre del dispositivo.]{#mount-umount-uuid-length explanation="La longitud de la cadena del identificador no guarda relación con las comprobaciones de ocupación."}
:::

Utiliza [Gestionar particiones y sistemas de archivos de Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) para practicar con el almacenamiento desechable designado.

## Resumen

Ahora puedes conectar y desconectar sistemas de archivos con un alcance verificable.

1. Utiliza un punto de montaje vacío y dedicado.
2. Verifica la fuente, el tipo, las opciones y el montaje resultante.
3. Prefiere un identificador único del sistema de archivos para referencias persistentes.
4. Desmonta por destino y confirma la desconexión antes de retirar el dispositivo.
5. Diagnostica las referencias activas en vez de forzar un desmontaje ocupado.
