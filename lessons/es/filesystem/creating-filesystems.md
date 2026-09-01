---
lesson_id: "creating-filesystems"
course_id: "filesystem"
lang: "es"
order_index: 5
title: "Crear sistemas de archivos"
description: "Aprende a verificar el destino de un dispositivo de bloques y crear un sistema de archivos con herramientas específicas del formato."
meta_title: "Crear sistemas de archivos - El sistema de archivos"
meta_description: "Aprende a verificar un dispositivo y crear un sistema de archivos Linux con mkfs y herramientas específicas del formato."
meta_keywords: "mkfs, crear sistema de archivos, ext4, particiones Linux, formatear disco Linux"
---

Crear un sistema de archivos escribe estructuras nuevas de asignación y metadatos en un dispositivo de bloques. Es un paso de inicialización destructivo, no un simple cambio de etiqueta. Utiliza solo almacenamiento desechable para practicar y conserva una copia de seguridad probada antes de dar formato a un dispositivo que haya contenido datos valiosos.

## Comprender `mkfs`

`mkfs` suele ser una interfaz que delega en un programa específico del sistema de archivos, como `mkfs.ext4`, `mkfs.xfs` o `mkfs.btrfs`. Una orden genérica tiene esta forma:

```bash
$ sudo mkfs -t ext4 /dev/VERIFIED-PARTITION
```

El marcador de posición solo debe sustituirse después de verificar el destino. La sintaxis equivalente específica del formato suele ser:

```bash
$ sudo mkfs.ext4 /dev/VERIFIED-PARTITION
```

Las opciones compatibles, los valores predeterminados, los conjuntos de funciones y las preguntas antes de sobrescribir difieren entre implementaciones. Lee el manual local del formateador exacto en vez de suponer que todos los programas subyacentes de `mkfs` se comportan igual.

:::single-choice{#creating-filesystems-mkfs-role} ¿Qué solicita `mkfs -t ext4 TARGET`?

::option[Montar un sistema de archivos existente sin modificarlo.]{#creating-filesystems-mount-existing explanation="Montar es una operación independiente; mkfs inicializa metadatos en el dispositivo."}
::option[Crear estructuras de un sistema de archivos ext4 en el destino.]{#creating-filesystems-create-ext4 .correct explanation="La interfaz selecciona la implementación de formateo ext4 para el dispositivo de bloques indicado."}
::option[Mostrar todos los sistemas de archivos montados en ese momento.]{#creating-filesystems-list-mounted explanation="Las herramientas como `findmnt` realizan el inventario de montajes de solo lectura."}
:::

## Verificar todas las capas de almacenamiento

Antes de dar formato, identifica el destino por modelo, número de serie, tamaño, topología, enlace persistente y función prevista:

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
$ findmnt --real
$ sudo wipefs --no-act /dev/VERIFIED-PARTITION
```

`wipefs --no-act` comunica las firmas reconocidas sin borrarlas. Comprueba también el uso como intercambio, LVM, RAID, cifrado, máquina virtual, contenedor o aplicación. Un dispositivo puede estar activo aunque `MOUNTPOINTS` esté vacío.

Desmonta o desactiva cada capa pertinente mediante su propia herramienta. Vuelve a comprobar la identidad inmediatamente antes de usar el formateador porque los nombres de enumeración pueden cambiar.

:::single-choice{#creating-filesystems-wipefs-no-act} ¿Qué proporciona `wipefs --no-act TARGET` en este flujo de trabajo?

::option[Un informe de solo lectura de las firmas reconocidas.]{#creating-filesystems-signature-report .correct explanation="El modo no-act ayuda a revelar firmas de sistemas de archivos, tablas de particiones, RAID u otros formatos sin eliminarlas."}
::option[Un sistema de archivos vacío nuevo y listo para montar.]{#creating-filesystems-wipefs-formats explanation="Examinar firmas no inicializa un sistema de archivos nuevo."}
::option[Una garantía de que ningún proceso utiliza el destino.]{#creating-filesystems-wipefs-no-users explanation="El uso debe comprobarse por separado en los montajes y en toda la pila de almacenamiento."}
:::

## Seleccionar deliberadamente el sistema de archivos

Elige un tipo compatible con la distribución, el entorno de arranque, las herramientas de copia de seguridad y reparación y la carga de trabajo. Considera los límites necesarios, las instantáneas, las sumas de comprobación, las cuotas, las capas de cifrado, la ampliación o reducción y el acceso multiplataforma.

No elijas un formato solo porque sea popular. Por ejemplo, ext4, XFS y Btrfs tienen funciones operativas y procedimientos de recuperación distintos. Un dispositivo extraíble para interoperabilidad puede necesitar otro formato con una semántica de permisos Unix diferente.

:::single-choice{#creating-filesystems-type-choice} ¿Cuál es una base sólida para seleccionar un tipo de sistema de archivos?

::option[El nombre que sea más corto de escribir.]{#creating-filesystems-shortest-name explanation="La longitud de la orden no dice nada sobre la durabilidad, las funciones o la compatibilidad."}
::option[La promesa de que nunca podrá producirse un fallo de almacenamiento.]{#creating-filesystems-no-failure explanation="Ningún sistema de archivos elimina los fallos de hardware ni la necesidad de copias de seguridad."}
::option[Las necesidades de la carga junto con herramientas compatibles de copia de seguridad, arranque y recuperación.]{#creating-filesystems-supported-workflow .correct explanation="El formato debe satisfacer tanto los requisitos técnicos como la capacidad del entorno para operarlo y recuperarlo."}
:::

## Etiquetas, UUID y verificación

Los formateadores suelen generar un UUID del sistema de archivos y a menudo permiten establecer una etiqueta legible. Utiliza etiquetas suficientemente únicas para el entorno y asegúrate de que los sistemas de archivos clonados no conserven identificadores conflictivos cuando se monten juntos.

Después de crearlo correctamente, examínalo sin montarlo:

```bash
$ lsblk -f /dev/VERIFIED-PARTITION
$ sudo blkid /dev/VERIFIED-PARTITION
```

Registra el UUID para la configuración posterior del montaje. Crear un sistema de archivos no lo monta, no crea directorios de aplicaciones, no restaura copias de seguridad ni lo hace persistente entre arranques.

:::single-choice{#creating-filesystems-after-mkfs} ¿Qué sigue siendo un paso independiente después de crear un sistema de archivos?

::option[Montarlo en el directorio previsto.]{#creating-filesystems-mount-separate .correct explanation="Dar formato escribe las estructuras del sistema de archivos, mientras que montar lo une al árbol visible de directorios."}
::option[Asignar cualquier capacidad al dispositivo de bloques.]{#creating-filesystems-capacity explanation="La partición o el dispositivo lógico subyacente ya proporciona la capacidad a la que se da formato."}
::option[Crear desde cero el directorio `/dev` del kernel.]{#creating-filesystems-create-dev explanation="La gestión de nodos de dispositivo es independiente del formateo de un destino."}
:::

Utiliza [Gestionar particiones y sistemas de archivos de Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) únicamente en el disco secundario desechable del laboratorio.

## Resumen

Ahora puedes describir la creación de un sistema de archivos como una operación destructiva verificada.

1. Trata `mkfs` como una interfaz que delega en herramientas específicas del formato.
2. Verifica la identidad persistente, las firmas y todos los consumidores activos.
3. Selecciona un sistema de archivos según los requisitos de compatibilidad y recuperación.
4. Examina el tipo, la etiqueta y el UUID generados antes de montar.
