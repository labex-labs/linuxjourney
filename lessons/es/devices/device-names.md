---
lesson_id: "device-names"
course_id: "devices"
lang: "es"
order_index: 3
title: "Nombres de dispositivos"
description: "Aprende cómo Linux nombra los dispositivos de almacenamiento, las particiones, los dispositivos lógicos y los enlaces persistentes más habituales."
meta_title: "Nombres de dispositivos - Dispositivos"
meta_description: "Explora los nombres habituales de discos, particiones, dispositivos lógicos y seudodispositivos de Linux."
meta_keywords: "nombres de dispositivos Linux, sda, NVMe, particiones Linux, enlaces persistentes, /dev/disk"
---

Los nombres de dispositivos de Linux reflejan el subsistema y el controlador del kernel que presentan una interfaz, no siempre el conector físico impreso en el hardware. Aprende los patrones habituales, pero descubre la correspondencia real del sistema actual antes de modificar el almacenamiento.

## Nombres de discos de la capa SCSI

Los discos presentados mediante la capa de discos SCSI suelen utilizar nombres `sd`. Esto incluye muchos discos SCSI, SATA, de almacenamiento USB y virtuales:

- `/dev/sda`: un disco completo
- `/dev/sdb`: otro disco completo
- `/dev/sda3`: la partición 3 de `/dev/sda`
- `/dev/sdb1`: la partición 1 de `/dev/sdb`

Las letras reflejan la enumeración, no una identidad duradera. Añadir un controlador, cambiar el orden del firmware o conectar un dispositivo puede modificar qué disco recibe una letra determinada.

:::single-choice{#device-names-sdb-first-partition}
Según el patrón de nombres `sd`, ¿qué ruta designa la partición 1 de `/dev/sdb`?

::option[`/dev/sda2`]{#device-names-sda-two explanation="Esta ruta designa la partición 2 del disco que actualmente se llama `/dev/sda`."}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="El separador `p` se utiliza en patrones cuyo nombre base ya termina en un dígito, no en los nombres `sd` ordinarios."}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="En los discos `sd`, el número de partición se añade directamente al nombre del disco completo."}
:::

## Nombres que terminan en dígitos

Algunos nombres de dispositivos completos ya contienen dígitos, por lo que los nombres de sus particiones utilizan `p` como separador:

- `/dev/nvme0n1`: el espacio de nombres NVMe 1 del controlador 0
- `/dev/nvme0n1p2`: la partición 2 de ese espacio de nombres
- `/dev/mmcblk0`: un dispositivo de bloques MMC
- `/dev/mmcblk0p1`: la partición 1 de ese dispositivo

Los dispositivos NVMe no suelen llamarse `/dev/sdX`; utilizan la convención de nombres del subsistema NVMe.

:::single-choice{#device-names-nvme-partition}
¿Qué ruta designa la partición 2 de `/dev/nvme0n1`?

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="Los nombres de particiones NVMe insertan `p` antes del número de partición."}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="Sin un separador, los dígitos finales serían ambiguos respecto al número del espacio de nombres."}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="Esa es una partición de un disco de la capa `sd` y no designa el espacio de nombres NVMe indicado."}
:::

## Dispositivos de bloques lógicos y virtuales

Linux también crea dispositivos de bloques que no se corresponden uno a uno con un disco físico:

- `/dev/dm-N` para dispositivos del mapeador de dispositivos, a menudo acompañados de enlaces descriptivos bajo `/dev/mapper/`
- `/dev/mdN` para matrices RAID por software de Linux
- `/dev/loopN` para archivos normales conectados como dispositivos de bloques de bucle

Las particiones, las capas de cifrado, RAID, los volúmenes lógicos y los sistemas de archivos forman una pila. Utiliza herramientas como `lsblk` para ver las relaciones entre padres e hijos en vez de deducir la pila únicamente por el nombre.

:::single-choice{#device-names-device-mapper-link}
¿Qué ubicación suele proporcionar enlaces descriptivos para los dispositivos del mapeador de dispositivos?

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="Los usuarios del mapeador de dispositivos, como LVM y el cifrado de discos, suelen exponer enlaces con nombre en este directorio."}
::option[`/dev/null/`]{#device-names-null-directory explanation="`/dev/null` es un dispositivo de caracteres, no un directorio de dispositivos de bloques mapeados."}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="Esta no es la ruta habitual de los enlaces con nombre del mapeador de dispositivos."}
:::

## Enlaces persistentes de almacenamiento

La gestión de dispositivos en el espacio de usuario crea enlaces bajo `/dev/disk/`, normalmente agrupados como:

- `by-id` para identificadores de hardware o transporte
- `by-uuid` para UUID de sistemas de archivos
- `by-label` para etiquetas de sistemas de archivos
- `by-partuuid` para UUID de tablas de particiones
- `by-path` para rutas dependientes de la topología

Elige un identificador que corresponda a aquello que deba permanecer estable. Un UUID de sistema de archivos identifica un sistema de archivos, no necesariamente el disco físico que hay debajo. Clonar un sistema de archivos puede duplicar su UUID, así que comprueba la unicidad antes de depender de él.

:::single-choice{#device-names-persistent-config}
¿Por qué los enlaces de `/dev/disk/by-id/` suelen ser preferibles a `/dev/sdX` en una configuración específica de un dispositivo?

::option[Porque convierten automáticamente en reversibles las escrituras destructivas.]{#device-names-by-id-reversible explanation="Un nombre estable no proporciona instantáneas, copias de seguridad ni protección contra escritura."}
::option[Porque convierten un dispositivo de bloques en un archivo normal.]{#device-names-by-id-regular explanation="La entrada es un enlace simbólico que sigue resolviéndose a un nodo de dispositivo de bloques."}
::option[Porque se derivan de la identidad del dispositivo y no del orden de enumeración actual.]{#device-names-by-id-stable .correct explanation="El destino del enlace puede cambiar mientras el enlace basado en la identidad permanece asociado al mismo dispositivo reconocido."}
:::

## Nombres de seudodispositivos

Nombres como `/dev/null`, `/dev/zero` y `/dev/urandom` describen seudodispositivos del kernel, no almacenamiento físico. `/dev/null` descarta las escrituras y devuelve fin de archivo en las lecturas; `/dev/zero` proporciona bytes con valor cero; `/dev/urandom` proporciona bytes del generador de números aleatorios del kernel.

:::single-choice{#device-names-zero-read}
¿Qué produce la lectura de `/dev/zero`?

::option[Una lista de dispositivos de almacenamiento sin utilizar.]{#device-names-zero-storage-list explanation="Es un dispositivo de caracteres que produce bytes, no una orden de descubrimiento."}
::option[Un flujo de bytes con valor cero.]{#device-names-zero-bytes .correct explanation="El seudodispositivo zero devuelve bytes nulos en las lecturas solicitadas."}
::option[El fin de archivo inmediato, como al leer `/dev/null`.]{#device-names-zero-eof explanation="`/dev/zero` continúa produciendo bytes, mientras que las lecturas de `/dev/null` devuelven el fin de archivo."}
:::

Utiliza [Explorar dispositivos de hardware en Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para comparar nombres, enlaces persistentes y relaciones de `lsblk` antes de intentar trabajar con particiones.

## Resumen

Ahora puedes descifrar nombres habituales de almacenamiento en Linux sin tratarlos como una identidad permanente.

1. Interpreta `sdXNUMBER` como una partición de un disco `sd`.
2. Utiliza `pNUMBER` cuando el nombre del dispositivo completo ya termine en un dígito.
3. Reconoce dispositivos lógicos como el mapeador de dispositivos, RAID y los dispositivos de bucle.
4. Prefiere enlaces persistentes elegidos para la identidad que necesites.
5. Distingue los nombres de almacenamiento de los seudodispositivos del kernel.
