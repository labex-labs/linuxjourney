---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "es"
order_index: 5
title: "Proceso de arranque: init"
description: "Aprende cómo el PID 1 inicializa el espacio de usuario, supervisa servicios, recolecta hijos y coordina el apagado."
meta_title: "Proceso de arranque: init - Arrancar el sistema"
meta_description: "Aprende la función del PID 1 y compara sistemas init de Linux como System V, Upstart, systemd, OpenRC y runit."
meta_keywords: "init Linux, PID 1, systemd, System V init, Upstart, OpenRC, runit"
---

El kernel inicia el primer proceso del espacio de usuario como PID 1 dentro de un espacio de nombres de PID. En un sistema Linux completo, este proceso init establece el entorno de servicios. En un contenedor, el PID 1 puede ser un pequeño envoltorio de init o la propia aplicación, pero sigue teniendo responsabilidades especiales de señalización y recolección de procesos hijos.

## Responsabilidades del PID 1

Un sistema init suele:

- iniciar y supervisar servicios, inicios de sesión, montajes y otras unidades de trabajo
- ordenar el trabajo según las dependencias y el estado de destino configurado
- adoptar y recolectar procesos hijos huérfanos
- responder a fallos de servicios conforme a una política
- coordinar el apagado y el reinicio ordenados

El límite exacto varía. La gestión de dispositivos, las redes, los registros y las tareas programadas pueden ser programas independientes supervisados por init en vez de código integrado en el PID 1.

:::single-choice{#boot-init-pid-one-role} ¿Qué responsabilidad es especial para el PID 1 en su espacio de nombres de PID?

::option[Compilar todas las aplicaciones desde el código fuente en cada arranque.]{#boot-init-compile-apps explanation="El inicio normal de servicios utiliza programas instalados en vez de volver a compilar todo el software."}
::option[Definir el tamaño físico de los sectores del disco.]{#boot-init-sector-size explanation="El hardware de almacenamiento y los controladores exponen la geometría de sectores antes de que init gestione servicios."}
::option[Adoptar y recolectar procesos hijos huérfanos.]{#boot-init-reap-orphans .correct explanation="El PID 1 es el padre final y debe recopilar el estado de terminación para que no se acumulen registros zombis."}
:::

## System V init y niveles de ejecución

El sysvinit tradicional utiliza configuración como `/etc/inittab` y scripts de inicio y apagado específicos de cada nivel de ejecución. Un nivel representa un modo de funcionamiento, pero el significado de los niveles numerados puede variar según la distribución. El orden de los scripts se basa en convenciones y las herramientas de la distribución pueden ampliarlo o paralelizarlo.

No deduzcas el sistema init activo de un equipo solo porque exista `/etc/init.d/`; pueden quedar scripts de compatibilidad en sistemas cuyo PID 1 sea otra implementación.

:::single-choice{#boot-init-sysv-runlevel} ¿Qué representa un nivel de ejecución de System V?

::option[Un número de versión del kernel seleccionado por el cargador.]{#boot-init-runlevel-kernel explanation="Seleccionar el kernel corresponde al cargador y no se codifica mediante un nivel de init."}
::option[Un modo de funcionamiento configurado asociado con acciones sobre servicios.]{#boot-init-runlevel-mode .correct explanation="Los diseños SysV asocian niveles con conjuntos y órdenes de scripts de inicio o apagado."}
::option[El porcentaje actual de uso de inodos de un sistema de archivos.]{#boot-init-runlevel-inodes explanation="La capacidad de metadatos no guarda relación con los modos de funcionamiento de servicios."}
:::

## Sistemas basados en sucesos y dependencias

Upstart introdujo un modelo de trabajos dirigido por sucesos y fue utilizado por versiones antiguas de Ubuntu y algunos otros sistemas. Actualmente tiene sobre todo interés histórico o para operar sistemas heredados.

systemd se utiliza ampliamente en las distribuciones actuales de propósito general. Modela servicios, sockets, montajes, temporizadores, dispositivos, destinos y otros recursos como unidades. Las dependencias declarativas y los mecanismos de activación permiten que el trabajo independiente avance en paralelo y a la vez preservan el orden necesario.

Otros diseños activos de init y supervisión son OpenRC, runit, s6 y BusyBox init. «Más reciente» no es una regla útil de compatibilidad; identifica qué ejecuta el sistema real y utiliza su documentación.

:::single-choice{#boot-init-systemd-unit-model} ¿Cómo representa systemd recursos gestionados como servicios y montajes?

::option[Como entradas de particiones principales MBR.]{#boot-init-systemd-partitions explanation="Los metadatos de particiones no guardan relación con las unidades del gestor de servicios."}
::option[Únicamente como enlaces duros al ejecutable del PID 1.]{#boot-init-systemd-hard-links explanation="Las unidades son objetos de configuración y ejecución, no simples alias de inodos."}
::option[Como unidades con dependencias y relaciones de activación.]{#boot-init-systemd-units .correct explanation="Los tipos de unidades proporcionan un modelo compartido de orden, estado y supervisión."}
:::

## Identificar el init en ejecución

Examina el PID 1 en vez de adivinarlo por los archivos instalados:

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

Los permisos, los contenedores y los espacios de nombres influyen en lo que ves. Una orden ejecutada dentro de un contenedor comunica el PID 1 de ese espacio, no necesariamente el init del anfitrión. Después de identificarlo, utiliza sus herramientas nativas de estado y registros en vez de mezclar órdenes de otra familia de init.

:::single-choice{#boot-init-detect-running} ¿Por qué es mejor examinar el PID 1 que comprobar si existe un directorio de scripts heredado?

::option[Porque el PID 1 tiene siempre el mismo nombre de ejecutable en todos los sistemas Linux.]{#boot-init-same-name explanation="Systemd, sysvinit, BusyBox, los programas init de contenedores y otros pueden ocupar el PID 1."}
::option[Porque pueden existir archivos de compatibilidad aunque se ejecute otra implementación de init.]{#boot-init-compatibility-files .correct explanation="El ejecutable activo con PID 1 es una prueba más sólida del sistema init en uso."}
::option[Porque los directorios heredados se eliminan automáticamente en cada arranque.]{#boot-init-directories-deleted explanation="Los archivos de compatibilidad instalados pueden persistir entre arranques."}
:::

## Resumen

Ahora puedes explicar init como una función, no como una implementación obligatoria.

1. Relaciona el PID 1 con la inicialización de servicios, la recolección y el apagado.
2. Reconoce los niveles de System V como modos de funcionamiento definidos por la distribución.
3. Relaciona los recursos y dependencias de systemd con unidades.
4. Examina el PID 1 activo en el espacio de nombres pertinente antes de elegir herramientas.
