---
lesson_id: "swap-space"
course_id: "filesystem"
lang: "es"
order_index: 8
title: "Intercambio"
description: "Aprende cómo Linux utiliza, inicializa, activa, dimensiona y desactiva de forma segura el espacio de intercambio."
meta_title: "Intercambio - El sistema de archivos"
meta_description: "Aprende cómo funciona el intercambio de Linux y cómo examinar, crear, activar, dimensionar y desactivar áreas swap."
meta_keywords: "swap Linux, intercambio, mkswap, swapon, swapoff, /etc/fstab, memoria virtual"
---

Linux puede trasladar determinadas páginas de memoria anónima entre la RAM y el almacenamiento respaldado por intercambio. Esto permite conservar memoria inactiva y liberar RAM para cargas activas y la caché del sistema de archivos, pero el almacenamiento es mucho más lento que la RAM. El intercambio es una herramienta de capacidad y gestión de memoria, no un sustituto de suficiente memoria ni un límite de memoria para aplicaciones.

## Participación del intercambio en la gestión de memoria

El kernel puede utilizar intercambio antes de agotar por completo la RAM, según la carga, la presión de memoria, los cgroups y ajustes como swappiness. Las páginas limpias respaldadas por archivos suelen poder descartarse y volver a leerse desde sus archivos, mientras que las páginas anónimas necesitan intercambio o deben permanecer en RAM.

Un intercambio intenso y sostenido puede provocar una latencia grave o thrashing. Diagnostica la demanda de memoria, los conjuntos de trabajo, la presión y los límites de las aplicaciones en vez de tratar una zona de intercambio mayor como solución universal de rendimiento.

:::single-choice{#swap-space-anonymous-pages} ¿Qué memoria es una candidata principal para almacenarse en el intercambio?

::option[Todos los archivos ejecutables instalados bajo `/usr`.]{#swap-space-installed-files explanation="Los archivos instalados permanecen en sus sistemas de archivos; las páginas limpias mapeadas pueden volver a leerse desde allí."}
::option[Las páginas inactivas de memoria anónima.]{#swap-space-anonymous-memory .correct explanation="Las páginas anónimas carecen de un archivo de respaldo ordinario desde el cual puedan volver a leerse sin más."}
::option[Las entradas de la tabla de particiones del disco.]{#swap-space-partition-table explanation="Los metadatos de particiones permanecen en el dispositivo de bloques y no son memoria de procesos trasladada desde la RAM."}
:::

## Examinar el intercambio activo

Utiliza primero órdenes de solo lectura:

```bash
$ swapon --show
$ cat /proc/swaps
$ free -h
```

Muestran las áreas de intercambio activas configuradas y cifras agregadas de memoria. Un valor «used» distinto de cero no constituye automáticamente un problema; relaciónalo con las tasas de entrada y salida del intercambio, la presión de memoria, la latencia y el comportamiento de la carga.

:::single-choice{#swap-space-show-active} ¿Qué orden muestra las áreas de intercambio activas en una vista estructurada?

::option[`swapon --show`]{#swap-space-swapon-show .correct explanation="El modo show comunica los archivos o dispositivos de intercambio activos y, cuando están disponibles, su tamaño, uso y prioridad."}
::option[`mkswap --all`]{#swap-space-mkswap-all explanation="Mkswap inicializa firmas de intercambio y no es la orden de listado activo de solo lectura."}
::option[`mkfs -t swap`]{#swap-space-mkfs-swap explanation="La herramienta estándar de inicialización es `mkswap`, y dar formato no es una consulta de estado."}
:::

## Inicializar y activar un dispositivo de intercambio

`mkswap` escribe una firma de intercambio y destruye los metadatos utilizables anteriores del destino. Practica únicamente con un destino desechable y verificado:

```bash
$ sudo mkswap /dev/VERIFIED-SWAP-TARGET
$ sudo swapon /dev/VERIFIED-SWAP-TARGET
```

Antes de `mkswap`, verifica el modelo, el número de serie, el tamaño, la identidad persistente, las firmas existentes, los montajes, RAID, LVM, el cifrado y las copias de seguridad igual que antes de `mkfs`. Tras activarlo, confirma la fuente exacta mediante `swapon --show`.

Para hacerlo persistente, utiliza el UUID del intercambio en `/etc/fstab` con un tipo y opciones apropiados para la política local:

```text
UUID=VERIFIED-SWAP-UUID none swap sw 0 0
```

:::single-choice{#swap-space-enable-command} ¿Qué orden activa un área de intercambio inicializada?

::option[`swapon`]{#swap-space-command-swapon .correct explanation="Swapon añade un dispositivo o archivo swap válido al conjunto activo de intercambio del kernel."}
::option[`mkswap`]{#swap-space-command-mkswap explanation="Mkswap inicializa la firma, pero no activa el área por sí mismo."}
::option[`mount`]{#swap-space-command-mount explanation="El intercambio se activa mediante su subsistema en vez de montarse como un sistema de archivos de directorios."}
:::

## Archivos de intercambio y otros soportes

Un archivo de intercambio puede proporcionar capacidad flexible sin volver a particionar, pero los requisitos para crearlo dependen del sistema de archivos. Debe tener permisos restrictivos, una asignación adecuada sin huecos incompatibles ni comportamiento de copia al escribir, una firma de intercambio y activación. Sigue la documentación del sistema de archivos y de la distribución en vez de copiar en todas partes una receta genérica con `fallocate`.

Los dispositivos de RAM comprimida como zram pueden ofrecer otro nivel de intercambio con diferentes compromisos entre CPU y capacidad. El intercambio cifrado puede proteger las páginas en reposo, mientras que la hibernación exige una configuración de reanudación y almacenamiento adecuado suficiente. Estos objetivos influyen en el tamaño y el diseño.

No existe una regla universal que exija que el intercambio sea el doble de la RAM. Dimensiónalo según los picos de la carga, el comportamiento deseado ante fallos, las necesidades de hibernación, la latencia y resistencia del almacenamiento, el diseño de volcados y la supervisión operativa.

:::single-choice{#swap-space-sizing-rule} ¿Cuál es la mejor base para dimensionar el intercambio?

::option[Siempre exactamente el doble de la RAM instalada.]{#swap-space-twice-ram explanation="Esa regla histórica no resulta apropiada para todas las cargas ni tamaños de memoria modernos."}
::option[Las necesidades medidas de la carga, los objetivos de hibernación y la política ante fallos.]{#swap-space-sizing-requirements .correct explanation="La finalidad del sistema y el comportamiento de memoria observado importan más que un multiplicador fijo de la RAM."}
::option[Siempre cero cuando el sistema tenga una SSD.]{#swap-space-zero-ssd explanation="El tipo de almacenamiento por sí solo no determina los requisitos de presión de memoria o hibernación."}
:::

## Desactivar el intercambio de forma segura

Desactiva un área concreta y verificada con:

```bash
$ sudo swapoff /dev/VERIFIED-SWAP-TARGET
```

El kernel debe trasladar a otro lugar sus páginas residentes en el intercambio. Si la RAM y las demás áreas swap no pueden albergarlas, la operación puede fallar o crear una presión de memoria peligrosa. Detén o limita primero las cargas, supervisa la memoria, elimina la entrada persistente de fstab solo después de verificar el destino correcto y confirma la desactivación con `swapon --show` antes de reutilizar el almacenamiento.

:::single-choice{#swap-space-swapoff-capacity} ¿Por qué puede fallar `swapoff` o poner en peligro un sistema con mucha carga?

::option[Porque swapoff siempre vuelve a dar formato a todos los módulos de RAM.]{#swap-space-formats-ram explanation="Cambia la configuración de intercambio activa y no da formato al hardware de memoria física."}
::option[Porque las páginas de esa área necesitan capacidad en RAM o en otro intercambio.]{#swap-space-pages-need-capacity .correct explanation="La desactivación exige trasladar páginas activas del intercambio mientras el sistema continúa funcionando."}
::option[Porque un área de intercambio inactiva debe permanecer montada en `/swap`.]{#swap-space-mounted-path explanation="Las áreas de intercambio no son sistemas de archivos montados en directorios."}
:::

Utiliza [Crear y activar un archivo swap en Linux](https://labex.io/labs/comptia-create-and-activate-a-swap-file-in-linux-590858) en un entorno controlado para practicar los permisos, la activación y la persistencia.

## Resumen

Ahora puedes tratar el intercambio como un recurso explícito de gestión de memoria.

1. Relaciona el intercambio principalmente con memoria anónima bajo presión.
2. Examina el intercambio activo y la carga antes de cambiar la capacidad.
3. Inicializa únicamente un destino desechable verificado y actívalo después con `swapon`.
4. Dimensiona y protege el intercambio según la carga y los requisitos de hibernación.
5. Garantiza capacidad de traslado antes de utilizar `swapoff`.
