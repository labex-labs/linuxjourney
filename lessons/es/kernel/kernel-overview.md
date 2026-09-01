---
lesson_id: "kernel-overview"
course_id: "kernel"
lang: "es"
order_index: 1
title: "Descripción general del kernel"
description: "Aprende cómo el kernel de Linux media entre el hardware, los recursos, el aislamiento y las solicitudes del espacio de usuario."
meta_title: "Descripción general del kernel - Kernel"
meta_description: "Comienza tu recorrido por Linux con una descripción general del kernel. Comprende su función esencial en la gestión del hardware y el espacio de usuario, un concepto fundamental de linuxjourney.com."
meta_keywords: "kernel de Linux, sistema operativo, hardware, espacio de usuario, linux jorney, linux jorney.com, linux jouney.com, linux journe, descripción general del kernel"
---

Linux es el kernel del sistema operativo: el software privilegiado que gestiona los procesadores, la memoria, los dispositivos, los procesos y las abstracciones comunes de recursos. Un sistema Linux completo también incluye bibliotecas, utilidades, servicios, shells y programas gráficos del espacio de usuario, además de las políticas de la distribución.

## Recursos de hardware

Los procesadores ejecutan instrucciones, la memoria almacena el estado activo y los controladores conectan el almacenamiento, las redes, las pantallas, los dispositivos de entrada y otros periféricos. El hardware expone mecanismos específicos de la arquitectura y del dispositivo, no una única interfaz segura para todas las aplicaciones.

El kernel inicializa y controla estos recursos mediante código de arquitectura y controladores de dispositivos. Gestiona las interrupciones, la coordinación de DMA, los temporizadores y los eventos de administración de energía, a la vez que impone límites de acceso entre las cargas de trabajo.

:::single-choice{#kernel-overview-hardware-manager} ¿Qué capa coordina normalmente los controladores de dispositivos y las interrupciones de hardware en Linux?

::option[El archivo de historial del shell de cada usuario.]{#kernel-overview-shell-history explanation="El historial registra comandos y no gestiona la ejecución del hardware."}
::option[El índice del repositorio de paquetes.]{#kernel-overview-repository-index explanation="Los metadatos del repositorio describen paquetes de software, no eventos activos del hardware."}
::option[El kernel.]{#kernel-overview-kernel-layer .correct explanation="El código privilegiado del kernel conecta los eventos de hardware y las operaciones de los controladores con interfaces controladas del sistema."}
:::

## Responsabilidades del kernel

Entre sus principales responsabilidades se encuentran:

- programar los hilos ejecutables en las CPU
- crear y aislar espacios de direcciones virtuales
- aplicar credenciales de procesos, permisos y políticas de seguridad
- proporcionar sistemas de archivos, redes, IPC e interfaces de dispositivos
- gestionar señales, temporizadores y el ciclo de vida de los procesos
- asignar, contabilizar y recuperar recursos

Linux suele describirse como un kernel monolítico porque los servicios esenciales y muchos controladores se ejecutan en un único espacio de direcciones privilegiado del kernel. También es modular: los componentes compatibles pueden cargarse y descargarse como módulos del kernel. Un error en código privilegiado del kernel puede comprometer todo el sistema, por lo que las actualizaciones del kernel y la procedencia de los módulos son esenciales para la seguridad.

:::single-choice{#kernel-overview-scheduler-role} ¿Qué gestiona el planificador del kernel?

::option[Qué página de documentación leerá un usuario a continuación.]{#kernel-overview-documentation explanation="La navegación del aprendizaje queda fuera de la planificación del kernel."}
::option[Qué hilos ejecutables reciben tiempo de ejecución de CPU.]{#kernel-overview-thread-scheduling .correct explanation="El planificador selecciona contextos de ejecución según la política, la prioridad, la afinidad y la disponibilidad de CPU."}
::option[En qué clave de firma de un repositorio debe confiar un administrador.]{#kernel-overview-repository-key explanation="La configuración de confianza pertenece a la política de gestión de paquetes."}
:::

## Espacio de usuario

El espacio de usuario contiene los procesos ordinarios: el sistema de inicio y los servicios, las herramientas de línea de comandos, los entornos de ejecución de lenguajes, las bases de datos, los shells y las aplicaciones de escritorio. Los privilegios del hardware impiden que estos programas ejecuten directamente muchas instrucciones delicadas o accedan a memoria arbitraria del kernel.

Los procesos solicitan trabajo al kernel mediante llamadas al sistema e interactúan con interfaces expuestas como descriptores de archivo, sockets, nodos de dispositivo, procfs, sysfs, netlink y asignaciones de memoria. Las bibliotecas suelen envolver estas interfaces en API de mayor nivel.

El usuario root del espacio de usuario dispone de amplias autorizaciones según la política, pero normalmente sigue ejecutándose en el modo de usuario del procesador. La identidad del usuario y el modo de privilegio de la CPU son conceptos independientes.

:::single-choice{#kernel-overview-root-user-mode} ¿Ejecuta una aplicación normal propiedad de root todas sus instrucciones en modo kernel?

::option[Sí; el UID 0 cambia permanentemente todas las instrucciones al anillo 0.]{#kernel-overview-root-ring-zero explanation="Un proceso root ordinario sigue siendo un proceso del espacio de usuario."}
::option[Sí; las aplicaciones de root se convierten automáticamente en módulos cargables del kernel.]{#kernel-overview-root-module explanation="El UID de propietario no transforma un ejecutable de usuario en código del kernel."}
::option[No; normalmente se ejecuta en modo de usuario y entra en el kernel mediante interfaces controladas.]{#kernel-overview-root-userspace .correct explanation="Las credenciales de root afectan a la autorización, mientras que el modo del procesador solo cambia al entrar y ejecutar código del kernel."}
:::

## Límites y abstracciones

El kernel presenta procesos virtuales, archivos, sockets y espacios de direcciones en lugar de exponer directamente la maquinaria física en bruto. Estas abstracciones favorecen el aislamiento y la portabilidad, pero por sí solas no constituyen límites de seguridad perfectos. Los espacios de nombres, cgroups, capacidades, módulos de seguridad, seccomp y la virtualización añaden controles especializados.

Al diagnosticar un problema, pregunta qué capa es responsable del comportamiento: la aplicación, la biblioteca, la interfaz de llamadas al sistema, el sistema de archivos, el controlador, el subsistema del kernel, el firmware o el hardware. Las pruebas procedentes de la capa equivocada pueden conducir a soluciones incorrectas.

:::single-choice{#kernel-overview-system-call-boundary} ¿Qué es una llamada al sistema?

::option[Una solicitud controlada del espacio de usuario para obtener un servicio del kernel.]{#kernel-overview-controlled-request .correct explanation="El procesador entra en modo kernel mediante una interfaz definida, donde el kernel valida y realiza la operación."}
::option[Un comando directo que elude todos los controles de acceso.]{#kernel-overview-bypass-checks explanation="Las llamadas al sistema son precisamente el lugar donde se realizan muchas comprobaciones de validación y autorización."}
::option[Un archivo de paquete que contiene un controlador de dispositivo.]{#kernel-overview-package-archive explanation="Los paquetes pueden proporcionar software, pero una llamada al sistema es una interfaz de ejecución."}
:::

Utiliza [Gestionar módulos del kernel en Linux](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865) para observar una parte modular del kernel en un entorno controlado.

## Resumen

Ahora puedes situar el kernel entre los recursos físicos y los procesos aislados del espacio de usuario.

1. Relaciona los controladores y el código de arquitectura con el control del hardware.
2. Identifica las responsabilidades de planificación, memoria, seguridad, sistemas de archivos y redes.
3. Trata las credenciales de root y el modo kernel del procesador como conceptos distintos.
4. Sitúa la interacción entre el usuario y el kernel en interfaces controladas durante la ejecución.
