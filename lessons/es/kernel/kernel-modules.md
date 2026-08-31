---
lesson_id: "kernel-modules"
course_id: "kernel"
lang: "es"
order_index: 6
title: "Módulos del kernel"
description: "Aprende a inspeccionar, cargar, configurar y retirar de forma segura módulos de Linux específicos de una versión del kernel."
meta_title: "Módulos del kernel - Kernel"
meta_description: "Descubre qué son los módulos del kernel en Linux y cómo amplían su funcionalidad. Esta lección explica cómo usar lsmod y modprobe para listar, cargar y descargar módulos cuando se necesiten."
meta_keywords: "qué son los módulos del kernel, módulos del kernel de Linux, modprobe, lsmod, gestión del kernel, tutorial de Linux, Linux para principiantes, guía de Linux"
---

Un módulo cargable del kernel es código privilegiado que puede ampliar el kernel en ejecución con un controlador, un sistema de archivos, una función de red u otro subsistema. Los módulos evitan tener que integrar todas las funciones opcionales en una sola imagen del kernel, pero cargar uno amplía la superficie de ataque de confianza del kernel.

## Listar e inspeccionar módulos

Lista los módulos cargados actualmente:

```bash
$ lsmod
```

La salida procede del estado del kernel, como `/proc/modules`, e incluye el nombre del módulo, su tamaño y un contador de uso o sus dependencias. Que el contador parezca cero no demuestra por completo que retirarlo sea seguro; un controlador aún puede tener dispositivos activos a su cargo o participar en el estado de un subsistema.

Inspecciona un módulo disponible para el kernel en ejecución con:

```bash
$ modinfo MODULE_NAME
```

`modinfo` puede mostrar el nombre del archivo, los alias, los parámetros, la licencia, la descripción y la información de firma. Trata los metadatos como información descriptiva, no como prueba de que el módulo sea de confianza o compatible con la carga de trabajo.

:::single-choice{#kernel-modules-lsmod-purpose}
¿Qué muestra `lsmod`?

::option[Todos los paquetes de módulos disponibles en repositorios remotos.]{#kernel-modules-repository-list explanation="Para consultar el inventario de los repositorios se necesita el gestor de paquetes."}
::option[Únicamente los controladores compilados directamente en la imagen del kernel.]{#kernel-modules-builtins explanation="Las funciones integradas no son módulos cargables y normalmente no aparecen en lsmod."}
::option[Los módulos cargados actualmente en el kernel en ejecución.]{#kernel-modules-loaded-list .correct explanation="El listado refleja el estado activo de los módulos y la información sobre dependencias o uso."}
:::

## Cargar con `modprobe`

Carga un módulo por su nombre:

```bash
$ sudo modprobe MODULE_NAME
```

`modprobe` consulta los índices de dependencias, los alias y la configuración del kernel en ejecución bajo `/lib/modules/$(uname -r)/`. Carga las dependencias necesarias y pasa los parámetros configurados. En cambio, `insmod` inserta directamente un único archivo de módulo indicado y no proporciona el mismo flujo de resolución de dependencias.

Antes de cargarlo, confirma la procedencia del módulo, la política de firmas, la compatibilidad con la versión del kernel, los parámetros, la asociación esperada con el hardware y el procedimiento de reversión. Secure Boot o el bloqueo del kernel pueden rechazar módulos sin firmar; forzar código incompatible puede provocar un fallo o comprometer el sistema.

:::single-choice{#kernel-modules-modprobe-dependencies}
¿Por qué suele preferirse `modprobe` frente al uso directo de `insmod`?

::option[Ejecuta el módulo por completo en el espacio de usuario sin privilegios.]{#kernel-modules-modprobe-userspace explanation="El módulo insertado se ejecuta como código privilegiado del kernel."}
::option[Garantiza que todos los módulos de terceros estén firmados y sean seguros.]{#kernel-modules-modprobe-guarantee explanation="La aplicación de firmas depende de la política, y una firma válida no demuestra que no haya defectos."}
::option[Resuelve los alias, las dependencias y la configuración de los módulos.]{#kernel-modules-modprobe-resolves .correct explanation="Modprobe utiliza el árbol de módulos indexado de la versión exacta en ejecución."}
:::

## Parámetros de módulos y carga durante el arranque

La política persistente de parámetros y alias debe residir en un archivo `.conf` bajo `/etc/modprobe.d/`:

```text
options example_module mode=careful
```

Esta línea afecta a la forma en que modprobe carga el módulo; por sí sola, no solicita que se cargue durante el arranque. Una lista sencilla de carga durante el arranque suele residir bajo `/etc/modules-load.d/`:

```text
example_module
```

Los alias de hardware suelen provocar la carga automática sin una lista explícita. Para los módulos que se necesitan durante las primeras fases del arranque, actualiza el initramfs mediante el proceso documentado de la distribución después de cambiar la configuración.

:::single-choice{#kernel-modules-options-versus-load}
¿Qué hace una línea `options` de `/etc/modprobe.d/`?

::option[Garantiza por sí sola que el módulo se cargue en todos los arranques.]{#kernel-modules-options-autoload explanation="Las solicitudes de carga durante el arranque utilizan otro mecanismo, como la configuración de modules-load o los alias de dispositivos."}
::option[Establece los parámetros que se utilizan al cargar el módulo indicado.]{#kernel-modules-options-parameters .correct explanation="Modprobe aplica los argumentos clave-valor configurados durante la inserción."}
::option[Compila el módulo para todas las versiones instaladas del kernel.]{#kernel-modules-options-compiles explanation="La configuración no compila módulos binarios."}
:::

## Listas negras y sus límites

Una configuración de modprobe puede contener:

```text
blacklist example_module
```

La inclusión en una lista negra normalmente impide la carga automática mediante los alias del módulo. No descarga un módulo ya cargado, no lo elimina de un initramfs ni impide necesariamente que se cargue explícitamente por su nombre exacto o como dependencia. El refuerzo de la seguridad requiere una combinación específica para la amenaza de disponibilidad de módulos, aplicación de firmas, contenido del initramfs, parámetros de arranque y políticas.

:::single-choice{#kernel-modules-blacklist-effect}
¿Qué impide principalmente una línea básica `blacklist` de modprobe?

::option[La carga automática mediante los alias del módulo.]{#kernel-modules-blacklist-aliases .correct explanation="La directiva no constituye una prohibición universal de todas las vías por las que el código puede estar ya cargado o llegar a cargarse."}
::option[La ejecución de todos los programas del espacio de usuario que tengan un nombre parecido.]{#kernel-modules-blacklist-user-programs explanation="La configuración de modprobe se aplica a la resolución de módulos del kernel."}
::option[Todo el código del kernel integrado en la imagen.]{#kernel-modules-blacklist-builtins explanation="La funcionalidad integrada no puede descargarse ni bloquearse como módulo."}
:::

## Retirar un módulo de forma segura

Solicita la retirada con:

```bash
$ sudo modprobe -r MODULE_NAME
```

Modprobe puede retirar las dependencias que hayan dejado de usarse cuando corresponda. El kernel rechaza la retirada cuando el seguimiento ordinario de referencias indica que el módulo está ocupado, pero no confíes en ello como única comprobación de seguridad. Detén los servicios, desmonta los sistemas de archivos, desconecta los dispositivos, deja inactiva la red y confirma que haya otro controlador o una vía de recuperación antes de retirar código que preste servicio a hardware activo.

Nunca fuerces la descarga de un módulo en un sistema que necesites conservar. Los errores durante la retirada o la actividad pendiente pueden bloquear el kernel o dañar datos.

:::single-choice{#kernel-modules-remove-command}
¿Qué comando solicita la retirada por nombre de un módulo teniendo en cuenta las dependencias?

::option[`lsmod -r MODULE_NAME`]{#kernel-modules-lsmod-remove explanation="Lsmod es una herramienta de listado de solo lectura y no retira módulos."}
::option[`uname -r MODULE_NAME`]{#kernel-modules-uname-remove explanation="Uname informa sobre el kernel y no gestiona módulos."}
::option[`modprobe -r MODULE_NAME`]{#kernel-modules-modprobe-remove .correct explanation="El modo de retirada tiene en cuenta las relaciones de dependencia indexadas alrededor del módulo solicitado."}
:::

Utiliza [Gestionar módulos del kernel en Linux](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865) para practicar con módulos que el laboratorio haya designado como seguros.

## Resumen

Ahora puedes gestionar módulos teniendo en cuenta el riesgo que implican en el nivel del kernel.

1. Usa `lsmod` para consultar el estado activo y `modinfo` para los metadatos disponibles.
2. Usa `modprobe` para cargar teniendo en cuenta los alias y las dependencias.
3. Distingue los parámetros de modprobe de las solicitudes de carga durante el arranque.
4. Trata las listas negras como una política limitada, no como un bloqueo absoluto.
5. Deja inactivos todos los consumidores antes de ejecutar `modprobe -r`.
