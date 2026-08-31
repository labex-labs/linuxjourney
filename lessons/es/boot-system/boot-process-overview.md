---
lesson_id: "boot-process-overview"
course_id: "boot-system"
lang: "es"
order_index: 1
title: "Visión general del proceso de arranque"
description: "Aprende las principales transferencias desde el firmware de la plataforma, pasando por el kernel, hasta el primer proceso del espacio de usuario."
meta_title: "Visión general del proceso de arranque - Arrancar el sistema"
meta_description: "Comprende las principales etapas del arranque de Linux: firmware, cargador, kernel, espacio de usuario inicial y PID 1."
meta_keywords: "proceso de arranque Linux, BIOS, UEFI, gestor de arranque, kernel, initramfs, PID 1"
---

El arranque es una cadena de confianza y transferencias de control que transforma el reinicio de la plataforma en un entorno de espacio de usuario en ejecución. Una ruta habitual en un PC puede resumirse como firmware, gestor o cargador de arranque, kernel con espacio de usuario inicial opcional y sistema init con PID 1. Las arquitecturas, máquinas virtuales, sistemas embebidos y contenedores pueden utilizar rutas distintas.

## Inicialización del firmware

El firmware de la plataforma inicializa suficiente estado de CPU, memoria y dispositivos para elegir un destino de arranque. Los PC tradicionales utilizan convenciones de BIOS; los actuales suelen utilizar UEFI. Los ajustes del firmware, el orden de arranque, la verificación de la plataforma y la política de Secure Boot pueden determinar qué ejecutable de la etapa siguiente está autorizado a ejecutarse.

El firmware no comprende necesariamente el sistema de archivos raíz de Linux instalado. Localiza una ruta de arranque conforme a su interfaz; por ejemplo, código de arranque BIOS en un disco seleccionado o una entrada de arranque UEFI que apunte a un ejecutable EFI en una partición del sistema EFI.

:::single-choice{#boot-overview-first-stage}
¿Qué componente comienza la inicialización de la plataforma después del reinicio en un PC típico?

::option[El shell interactivo del usuario.]{#boot-overview-shell explanation="Un shell se inicia mucho más tarde mediante servicios del espacio de usuario o el proceso de inicio de sesión."}
::option[El firmware de la plataforma, como BIOS o UEFI.]{#boot-overview-firmware .correct explanation="El firmware establece el estado inicial del hardware y selecciona el siguiente destino de arranque antes de que se ejecute Linux."}
::option[La utilidad de reparación del sistema de archivos.]{#boot-overview-fsck explanation="Un comprobador puede participar posteriormente según la política de arranque, pero no es la etapa inicial de firmware."}
:::

## Cargador o gestor de arranque

Un cargador como GRUB puede presentar entradas, cargar en memoria un kernel de Linux seleccionado y el sistema de archivos inicial en RAM, construir la línea de órdenes del kernel y transferirle el control. UEFI también puede cargar directamente un kernel compilado como ejecutable EFI, por lo que un cargador independiente con varias etapas es habitual, pero no universal.

Los elementos seleccionados deben concordar: la versión del kernel, el contenido de initramfs, el identificador de la raíz, las firmas de seguridad y las opciones de la línea de órdenes influyen en que la siguiente transferencia tenga éxito.

:::single-choice{#boot-overview-loader-role}
¿Cuál es una responsabilidad habitual de un cargador de arranque de Linux?

::option[Cargar un kernel seleccionado y pasarle su línea de órdenes.]{#boot-overview-load-kernel .correct explanation="El cargador prepara la imagen y los parámetros del kernel, a menudo junto con un initramfs."}
::option[Crear desde cero todas las cuentas de usuario en cada arranque.]{#boot-overview-create-users explanation="Las bases de datos persistentes de cuentas son configuración del espacio de usuario y el cargador no las vuelve a crear."}
::option[Planificar todos los procesos de aplicaciones después de iniciar sesión.]{#boot-overview-schedule-apps explanation="La planificación de CPU corresponde al kernel en ejecución."}
:::

## Kernel y espacio de usuario inicial

El kernel se descomprime o reubica según sea necesario, inicializa subsistemas esenciales, analiza su línea de órdenes y descubre el hardware disponible. Un initramfs puede proporcionar módulos y herramientas iniciales necesarios para descubrir almacenamiento, RAID, cifrado, LVM, redes u otros trabajos requeridos para ensamblar el sistema de archivos raíz real.

Cuando la raíz prevista está disponible, el espacio de usuario inicial cambia a ella y el kernel ejecuta el primer programa de usuario configurado. Detalles como quién comprueba los sistemas de archivos o los vuelve a montar en modo de lectura y escritura pertenecen al diseño de arranque de la distribución, no a una secuencia universal.

:::single-choice{#boot-overview-initramfs-purpose}
¿Por qué puede utilizar un sistema un initramfs?

::option[Para conservar permanentemente en firmware la sesión de escritorio de cada usuario.]{#boot-overview-desktop-firmware explanation="Un initramfs es una imagen de sistema de archivos para el arranque, no almacenamiento de sesiones en firmware."}
::option[Para proporcionar herramientas y controladores iniciales necesarios para alcanzar el sistema de archivos raíz real.]{#boot-overview-early-root-tools .correct explanation="El espacio de usuario inicial puede ensamblar almacenamiento raíz cifrado, lógico, de red o dependiente de controladores."}
::option[Para sustituir el planificador de procesos del kernel después de iniciar sesión.]{#boot-overview-replace-scheduler explanation="El kernel conserva la responsabilidad de planificación durante todo el funcionamiento."}
:::

## PID 1 y disponibilidad del sistema

El primer proceso del espacio de usuario recibe el PID 1. En muchas distribuciones es systemd; otros sistemas utilizan sysvinit, OpenRC, runit, BusyBox init o un programa especializado. El PID 1 establece el entorno de servicios del espacio de usuario, recolecta procesos hijos huérfanos y se ocupa del apagado.

Alcanzar el PID 1 no significa que el sistema esté completamente listo. Los servicios pueden seguir iniciándose, el almacenamiento montándose, la configuración de red pendiente y un inicio de sesión gráfico o de consola es solo uno de los posibles estados de destino.

:::single-choice{#boot-overview-final-stage}
¿Qué comienza la etapa principal de inicialización del espacio de usuario?

::option[La creación del MBR protector del disco en cada arranque.]{#boot-overview-create-mbr explanation="Crear tablas de particiones no es una etapa recurrente normal del arranque."}
::option[La eliminación de todos los parámetros de la línea de órdenes del kernel.]{#boot-overview-delete-command-line explanation="El kernel analiza y expone su línea de órdenes en vez de exigir que se elimine."}
::option[La ejecución del programa init con PID 1.]{#boot-overview-pid-one .correct explanation="Después de preparar la raíz, el primer proceso de usuario inicia o supervisa los servicios necesarios para el estado configurado del sistema."}
:::

El laboratorio [Personalizar el menú de arranque de GRUB2](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) muestra una ruta de configuración del cargador. Aplica cambios únicamente en un sistema de laboratorio con capacidad de recuperación.

## Resumen

Ahora puedes seguir las principales transferencias del arranque de Linux sin tratarlas como detalles universales de implementación.

1. Empieza por la inicialización del firmware y la selección del destino.
2. Relaciona el cargador con la selección del kernel, initramfs y la línea de órdenes.
3. Utiliza el espacio de usuario inicial para comprender el ensamblaje complejo de la raíz.
4. Trata el PID 1 como el comienzo de la inicialización de servicios, no como prueba de disponibilidad.
