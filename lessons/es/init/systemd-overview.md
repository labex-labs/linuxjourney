---
lesson_id: "systemd-overview"
course_id: "init"
lang: "es"
order_index: 5
title: "Descripción general de systemd"
description: "Aprende cómo systemd carga unidades, resuelve dependencias, activa objetivos y gestiona recursos del sistema y de los usuarios."
meta_title: "Descripción general de systemd - Init"
meta_description: "Aprende los fundamentos del sistema de inicio systemd. Esta guía explica cómo systemd (o system d) usa unidades y objetivos para gestionar el proceso de arranque y los servicios de Linux. Comprende los conceptos esenciales del estándar moderno de inicialización de Linux."
meta_keywords: "systemd, system d, sistema init, unidades systemd, objetivos systemd, proceso de arranque linux, servicios linux, gestión de sistemas, principiante, tutorial"
---

Systemd es el sistema de inicio y gestor de servicios que se ejecuta como PID 1 en muchas distribuciones Linux actuales. El proyecto systemd también proporciona componentes de registro, dispositivos, inicio de sesión, red, hora y otros ámbitos, pero cada distribución puede elegir cuáles implantar.

## Confirmar el gestor en ejecución

Inspecciona el estado activo en lugar de comprobar si existen directorios instalados:

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

`/usr/lib/systemd/` puede existir en un sistema donde otro programa sea el PID 1, y un contenedor puede exponer su propio espacio de nombres de PID. `systemctl` también dispone de modos para el gestor de usuario y para sistemas remotos o contenedores, así que identifica a qué gestor se dirige cada operación.

:::single-choice{#systemd-overview-detection}
¿Qué identifica de la forma más directa a systemd como gestor de inicio del sistema?

::option[Existe un directorio llamado `/usr/lib/systemd`.]{#systemd-overview-directory explanation="Las bibliotecas y los archivos de unidad pueden seguir instalados sin que systemd actúe como PID 1."}
::option[Un usuario ha ejecutado un comando llamado `systemctl`.]{#systemd-overview-command-executed explanation="El binario cliente puede existir aunque no haya disponible un gestor systemd del sistema."}
::option[El PID 1 de la máquina es systemd.]{#systemd-overview-pid-one .correct explanation="El primer proceso en ejecución es una prueba más sólida que los archivos instalados o los nombres de paquetes."}
:::

## Las unidades como objetos gestionados

Una unidad es el modelo con nombre que systemd utiliza para representar un recurso o una actividad. Entre los tipos habituales se encuentran:

- `.service` para procesos y demonios
- `.socket` para la activación mediante sockets
- `.mount` y `.automount` para sistemas de archivos
- `.timer` y `.path` para la activación basada en eventos
- `.target` para agrupación y sincronización
- `.device`, `.swap`, `.slice` y `.scope` para otros recursos gestionados

El estado de una unidad no siempre es «en ejecución». Un montaje puede estar montado, un temporizador esperando, un dispositivo presente y un objetivo activo después de alcanzar sus dependencias.

:::single-choice{#systemd-overview-group-unit}
¿Qué tipo de unidad suele agrupar otras unidades y proporcionar un punto de sincronización?

::option[`.socket`]{#systemd-overview-socket explanation="Las unidades de socket exponen puntos de acceso IPC o de red y pueden activar servicios."}
::option[`.target`]{#systemd-overview-target .correct explanation="Las unidades de objetivo reúnen dependencias y representan hitos del arranque o del funcionamiento."}
::option[`.timer`]{#systemd-overview-timer explanation="Las unidades de temporizador programan activaciones según el calendario o el tiempo monotónico."}
:::

## Rutas de carga y ajustes de las unidades

Las unidades del sistema pueden cargarse desde rutas de la distribución y del administrador como:

- `/usr/lib/systemd/system/` para las unidades proporcionadas por paquetes en muchas distribuciones
- `/run/systemd/system/` para configuraciones generadas durante la ejecución o transitorias
- `/etc/systemd/system/` para configuraciones y ajustes locales persistentes del administrador

Las rutas exactas del proveedor pueden variar. La configuración local de mayor prioridad prevalece sobre los archivos de menor prioridad con el mismo nombre de unidad. Es preferible crear ajustes parciales con `systemctl edit UNIT` en lugar de copiar y modificar un archivo completo del proveedor, para que los cambios de las actualizaciones de paquetes sigan siendo visibles.

:::single-choice{#systemd-overview-local-override}
¿Dónde deberían residir normalmente los ajustes locales persistentes de las unidades del sistema?

::option[Dentro de `/proc/systemd/`.]{#systemd-overview-proc-systemd explanation="Procfs es una interfaz del kernel durante la ejecución, no un lugar para configuraciones persistentes de unidades."}
::option[Bajo `/etc/systemd/system/`.]{#systemd-overview-etc-system .correct explanation="La capa de configuración del administrador tiene prioridad sobre las unidades del proveedor instaladas por paquetes."}
::option[En los bytes de código de arranque del MBR del disco.]{#systemd-overview-mbr-units explanation="Las unidades de servicio son archivos de configuración del espacio de usuario."}
:::

## Dependencias y orden

Systemd construye una transacción a partir de las relaciones de dependencia. `Wants=` y `Requires=` incorporan otras unidades a una transacción con distinta intensidad. `Before=` y `After=` especifican el orden cuando ambas unidades están programadas; por sí solos, no provocan que se inicie otra unidad.

Una línea `After=network.target` no demuestra que la conectividad, el DNS o un punto remoto concreto estén disponibles. Los servicios deben usar la integración adecuada con el estado de red disponible o implementar sus propios mecanismos de reintento y disponibilidad.

:::single-choice{#systemd-overview-after-semantics}
¿Qué especifica por sí solo `After=other.service`?

::option[Una garantía de que el punto de acceso de la aplicación del otro servicio funciona correctamente.]{#systemd-overview-after-health explanation="La finalización del orden y la disponibilidad de la aplicación son conceptos distintos."}
::option[El orden, si ambas unidades forman parte de la transacción.]{#systemd-overview-after-ordering .correct explanation="Se necesita un requisito independiente, como Wants o Requires, para incorporar la otra unidad."}
::option[La habilitación automática de ambas unidades en todos los arranques futuros.]{#systemd-overview-after-enable explanation="La habilitación corresponde a metadatos de instalación y el orden no la implica."}
:::

## Objetivos y transacción de arranque predeterminada

`default.target` suele ser un alias de un objetivo como `multi-user.target` o `graphical.target`. Systemd inicia una transacción para ese objetivo y sus dependencias, lo que permite que tareas no relacionadas avancen a la vez mientras se respeta el orden explícito.

Los objetivos se parecen a los niveles de ejecución solo en términos generales de compatibilidad. Varios objetivos pueden estar activos simultáneamente, pueden crearse objetivos personalizados y que un objetivo esté activo no significa que todos los servicios de la máquina funcionen correctamente.

:::single-choice{#systemd-overview-default-target}
¿Qué selecciona normalmente `default.target`?

::option[El dispositivo de bloques predeterminado que `mkfs` debe borrar.]{#systemd-overview-default-disk explanation="Los objetivos describen la activación de unidades, no la selección destructiva del almacenamiento."}
::option[El único objetivo que puede estar activo.]{#systemd-overview-only-target explanation="Los objetivos son agrupaciones y puede haber muchos activos durante un mismo arranque."}
::option[La transacción de objetivos utilizada para un arranque normal del sistema.]{#systemd-overview-normal-boot .correct explanation="Suele ser un alias del objetivo de arranque multiusuario o gráfico elegido por el administrador."}
:::

## Resumen

Ahora puedes describir systemd en términos de gestores activos, unidades y transacciones.

1. Confirma systemd mediante el PID 1 correspondiente y la conexión con el gestor.
2. Relaciona los tipos de recursos con los sufijos de las unidades.
3. Coloca los ajustes locales por encima de la configuración del proveedor.
4. Distingue la intensidad de las dependencias, el orden y la disponibilidad de la aplicación.
5. Trata los objetivos como agrupaciones e hitos, no como estados mutuamente excluyentes.
