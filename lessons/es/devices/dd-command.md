---
lesson_id: "dd-command"
course_id: "devices"
lang: "es"
order_index: 7
title: "dd"
description: "Aprende cómo `dd` copia flujos de bloques y cómo evitar errores destructivos de entrada, salida y tamaño."
meta_title: "dd - Dispositivos"
meta_description: "Aprende a usar dd en Linux para copiar datos y crear imágenes de disco con seguridad mediante if, of, bs y count."
meta_keywords: "orden dd, dd Linux, copiar datos, imagen de disco, copia de seguridad, if, of, bs"
---

`dd` copia datos de un flujo de entrada a uno de salida y aplica los tamaños de bloque y las conversiones solicitados. No comprende los sistemas de archivos, los límites de las particiones ni si un destino contiene datos valiosos. Esto lo hace útil para imágenes y dispositivos sin procesar, e inmediatamente destructivo cuando el destino es incorrecto.

## Entrada, salida y tamaño de bloque

Una orden tiene esta forma general:

```bash
$ dd if=input.img of=output.img bs=4M status=progress
```

- `if=` selecciona la entrada; sin él, `dd` lee la entrada estándar.
- `of=` selecciona la salida; sin él, `dd` escribe en la salida estándar.
- `bs=` establece el tamaño de los bloques de entrada y salida para una copia ordinaria.
- `status=progress` solicita a GNU `dd` que comunique periódicamente el progreso de la transferencia.

`dd` copia bloques, no necesariamente un byte cada vez. Un `bs` mayor puede reducir la sobrecarga de las llamadas al sistema, pero el valor óptimo depende de los dispositivos, la alineación, la caché y la carga de trabajo. No cambia los datos lógicos copiados.

:::single-choice{#dd-command-output-operand}
¿Qué operando selecciona el destino en el que escribe `dd`?

::option[`if=`]{#dd-command-input-file explanation="`if` identifica la fuente de entrada."}
::option[`of=`]{#dd-command-output-file .correct explanation="`of` designa el flujo o archivo de salida que recibe los datos copiados."}
::option[`bs=`]{#dd-command-block-size explanation="`bs` elige el tamaño del bloque de transferencia, no una ruta."}
:::

## Limitar la copia

`count=` limita el número de bloques de entrada procesados. Para un archivo de entrada normal:

```bash
$ dd if=source.img of=prefix.img bs=1M count=2 status=progress
```

Esto solicita dos bloques de entrada de hasta 1 MiB cada uno, por lo que copia como máximo 2 MiB. Las lecturas cortas pueden complicar la multiplicación sencilla en flujos como las tuberías; GNU `dd` ofrece `iflag=fullblock` cuando se necesitan bloques de entrada completos. Distingue las unidades binarias y la sintaxis de los sufijos conforme a la implementación local.

:::single-choice{#dd-command-count-result}
Para un archivo normal, ¿qué cantidad máxima solicita `bs=1M count=2`?

::option[1 MiB.]{#dd-command-one-mib explanation="Eso correspondería a un bloque del tamaño seleccionado."}
::option[2 MiB.]{#dd-command-two-mib .correct explanation="Dos bloques de entrada multiplicados por 1 MiB por bloque dan un máximo de 2 MiB."}
::option[2 GiB.]{#dd-command-two-gib explanation="En GNU `dd`, el sufijo `M` indica bloques del tamaño de un mebibyte, no gibibytes."}
:::

## Escribir una imagen en un dispositivo de bloques

Una restauración sin procesar puede tener este aspecto:

```bash
$ sudo dd if=backup.img of=/dev/sdX bs=4M status=progress conv=fsync
```

`/dev/sdX` es deliberadamente un marcador de posición, no una orden que se deba copiar. Antes de sustituirlo:

1. Conserva una copia de seguridad probada de todos los datos valiosos.
2. Identifica el destino por modelo, número de serie, tamaño, transporte y enlace persistente mediante `lsblk`, `udevadm` o herramientas equivalentes.
3. Confirma que ninguna partición del destino esté montada, se utilice como intercambio, forme parte de RAID o LVM, o esté abierta por otro servicio.
4. Vuelve a comprobar el dispositivo después de cualquier desconexión, reinicio o cambio de topología.
5. Asegúrate de que la imagen quepa y de que realmente pretendas escribir en todo el dispositivo.

El dispositivo de salida se sobrescribe desde el principio. Invertir `if` y `of`, seleccionar el disco del sistema o utilizar un disco completo cuando se pretendía usar una partición puede destruir datos sin pedir confirmación.

:::single-choice{#dd-command-target-verification}
¿Cuál es la razón más importante para verificar el modelo, el número de serie, el tamaño y el uso activo antes de escribir en un dispositivo sin procesar?

::option[Las letras de los dispositivos pueden cambiar y `dd` sobrescribe el destino seleccionado sin comprender su contenido.]{#dd-command-target-can-change .correct explanation="Comprobar la identidad y el uso reduce el riesgo de destruir otro disco o una pila de almacenamiento activa."}
::option[`dd` se niega a escribir si la etiqueta del sistema de archivos no coincide con la imagen.]{#dd-command-label-check explanation="La herramienta no realiza esa comprobación de seguridad basada en el sistema de archivos."}
::option[Los dispositivos de bloques no pueden abrirse mientras exista alguna copia de seguridad.]{#dd-command-backup-prevents-open explanation="Una copia de seguridad no impide técnicamente las escrituras; permite recuperarse si se mantiene y se ha probado."}
:::

## Crear una imagen coherente

Leer un dispositivo de bloques activo mientras cambia su sistema de archivos puede producir una imagen internamente incoherente. Prefiere un sistema de archivos desmontado, una instantánea coherente con la aplicación o un flujo documentado de inmovilización e instantáneas. Las bases de datos y las máquinas virtuales pueden exigir sus propios procedimientos de pausa.

Una imagen sin procesar copia bloques, incluidos los metadatos del sistema de archivos y las regiones sin usar, por lo que puede ser mucho mayor que una copia de seguridad basada en archivos y puede reproducir identificadores que deban cambiarse antes de montar un clon junto al original.

:::single-choice{#dd-command-live-filesystem-image}
¿Por qué puede ser poco fiable crear una imagen de un sistema de archivos montado que está cambiando?

::option[Los sistemas de archivos montados nunca permiten leer el dispositivo de bloques.]{#dd-command-mounted-no-read explanation="Las lecturas sin procesar pueden ser posibles, por lo que la coherencia debe planificarse en vez de darse por supuesta."}
::option[Pueden leerse bloques distintos correspondientes a momentos diferentes del estado del sistema de archivos.]{#dd-command-inconsistent-moments .correct explanation="Las modificaciones simultáneas pueden hacer que la imagen de bloques recopilada no represente un único instante coherente."}
::option[`dd` convierte automáticamente el sistema de archivos en un archivo tar.]{#dd-command-converts-tar explanation="La herramienta copia datos sin procesar y no crea un archivo que comprenda el sistema de archivos."}
:::

## Finalización y verificación

Que la orden termine sin un error de E/S no demuestra que se eligieran la fuente y el destino pretendidos ni que la imagen sea utilizable. Registra las identidades y los tamaños exactos, asegúrate de que la salida almacenada en búfer haya llegado al soporte, compara una lectura posterior limitada adecuadamente o hashes criptográficos y prueba la recuperación conforme al plan de copias de seguridad.

No anuncies pasadas de sobrescritura con `dd` como un borrado seguro garantizado para SSD, capas de traducción flash, almacenamiento de aprovisionamiento fino, instantáneas o sectores reasignados. Utiliza la sanitización compatible con el dispositivo y la plataforma junto con una política explícita de destrucción de datos.

:::single-choice{#dd-command-success-meaning}
¿Qué no demuestra por sí solo un estado de salida cero de `dd`?

::option[Que la orden analizó todos los operandos proporcionados.]{#dd-command-parsed-operands explanation="Los operandos no válidos suelen provocar un error, no una finalización correcta."}
::option[Que el operador seleccionó la fuente y el destino pretendidos.]{#dd-command-does-not-prove-intent .correct explanation="La herramienta puede copiar correctamente al destino equivocado porque no puede deducir la intención del operador."}
::option[Que el proceso alcanzó su vía normal de terminación.]{#dd-command-normal-exit explanation="Un estado cero sí indica éxito al nivel de la orden, aunque no la corrección semántica de los destinos elegidos."}
:::

Practica únicamente con archivos normales o discos virtuales desechables antes de tocar hardware sin procesar. Los conceptos de particiones y sistemas de archivos de [Gestionar particiones y sistemas de archivos de Linux](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) proporcionan contexto esencial.

## Resumen

Ahora puedes razonar sobre `dd` como una herramienta de copia de bloques sin conocimiento de la intención.

1. Distingue `if`, `of`, `bs` y `count`.
2. Verifica la identidad persistente del destino y todos sus consumidores activos.
3. Crea imágenes a partir de un estado de almacenamiento coherente.
4. Vacía los búferes, verifica y prueba la recuperación después de una copia.
5. Trata toda salida a un dispositivo sin procesar como potencialmente destructiva.
