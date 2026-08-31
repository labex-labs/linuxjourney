---
lesson_id: "boot-process-bios"
course_id: "boot-system"
lang: "es"
order_index: 2
title: "Proceso de arranque: BIOS"
description: "Aprende cómo el BIOS heredado y el firmware UEFI moderno localizan y autorizan la siguiente etapa del arranque."
meta_title: "Proceso de arranque: BIOS - Arrancar el sistema"
meta_description: "Aprende cómo BIOS y UEFI localizan la siguiente etapa del arranque mediante sectores de arranque o ejecutables EFI."
meta_keywords: "arranque Linux, BIOS, MBR, UEFI, ESP, Secure Boot, gestor de arranque"
---

El firmware se ejecuta antes que el kernel de Linux. En el hardware de tipo PC, las dos interfaces principales son el BIOS heredado y UEFI. Utilizan modelos distintos para descubrir el arranque, por lo que «el BIOS lee el cargador de arranque» solo describe una de las rutas.

## Arranque con BIOS heredado

Después de la inicialización inicial de la plataforma y de seleccionar un dispositivo de arranque, un BIOS heredado suele leer el primer sector de 512 bytes del disco elegido y transfiere el control a su código de arranque si el sector contiene la firma esperada.

En un diseño MBR, ese sector contiene una región pequeña de código de arranque, cuatro entradas de particiones y una firma. El código es demasiado pequeño para un cargador con muchas funciones, así que suele localizar otra etapa en otro lugar del disco o en un sistema de archivos.

Es posible arrancar mediante BIOS desde un disco GPT, pero el MBR protector por sí solo no proporciona las etapas posteriores del cargador. GRUB suele utilizar una pequeña partición de arranque BIOS en GPT para insertar código esencial. La disposición exacta corresponde al cargador instalado.

:::single-choice{#boot-bios-legacy-first-sector}
¿Qué carga primero normalmente el BIOS heredado desde el disco de arranque seleccionado?

::option[El sector de arranque inicial que contiene una pequeña cantidad de código.]{#boot-bios-boot-sector .correct explanation="La ruta de disco heredada del firmware transfiere el control al código del primer sector del disco seleccionado."}
::option[Todo el sistema de archivos raíz de Linux en la memoria del firmware.]{#boot-bios-entire-root explanation="El sector de la primera etapa es diminuto y el software posterior localiza el kernel y el almacenamiento raíz."}
::option[Toda la configuración de servicios de usuario bajo `/etc`.]{#boot-bios-etc-config explanation="El firmware no analiza toda la configuración de servicios del sistema instalado."}
:::

## Arranque UEFI

El firmware UEFI puede comprender un sistema de archivos definido en una partición del sistema EFI, o ESP, y cargar archivos ejecutables EFI. Las entradas de arranque del firmware almacenadas en variables no volátiles suelen identificar un disco, una partición y la ruta de un ejecutable. Puede utilizarse una ruta alternativa normalizada para medios extraíbles o situaciones de recuperación.

La ESP contiene aplicaciones de arranque y archivos auxiliares, no «toda la información de inicio». Las imágenes del kernel, los archivos initramfs y la configuración del cargador pueden residir allí o en otro lugar según el diseño. GPT es habitual en los sistemas UEFI, aunque la interfaz del firmware y el esquema de tabla de particiones siguen siendo capas distintas.

:::single-choice{#boot-bios-uefi-esp}
¿Qué suele cargar UEFI desde una partición del sistema EFI?

::option[Un ejecutable EFI seleccionado mediante una entrada de arranque del firmware.]{#boot-bios-efi-executable .correct explanation="La gestión de arranque UEFI dirige el firmware a un archivo ejecutable de una partición del sistema compatible."}
::option[Un script de shell POSIX desde cualquier directorio personal ext4.]{#boot-bios-shell-script explanation="El firmware carga formatos ejecutables definidos desde rutas de arranque compatibles, no ejecuta un shell de usuario normal."}
::option[Una partición extendida MBR que contiene cuentas de usuario.]{#boot-bios-extended-users explanation="Los datos de cuentas no guardan relación con el descubrimiento de ejecutables UEFI."}
:::

## Secure Boot y confianza

Con Secure Boot habilitado, UEFI verifica las firmas de la cadena de arranque conforme a las claves inscritas y a la política de la plataforma. Una distribución Linux puede utilizar un shim firmado, un cargador de arranque, un kernel y una política de módulos del kernel para ampliar esta cadena.

Secure Boot no cifra el disco ni demuestra que todos los programas del espacio de usuario sean seguros. Ayuda a impedir que se acepte código anterior al arranque no autorizado según la política de confianza configurada.

:::single-choice{#boot-bios-secure-boot-purpose}
¿Qué aplica principalmente UEFI Secure Boot?

::option[El cifrado automático de todos los archivos de todos los discos.]{#boot-bios-secure-encryption explanation="La confidencialidad del disco exige un sistema de cifrado independiente."}
::option[La autorización mediante firmas de los ejecutables de la cadena de arranque.]{#boot-bios-secure-signatures .correct explanation="El firmware y los componentes verificados posteriores aceptan código conforme a las claves inscritas y a la política."}
::option[La ausencia garantizada de vulnerabilidades en el software firmado.]{#boot-bios-secure-no-vulnerabilities explanation="Una firma válida demuestra autorización e integridad, no que el código carezca de defectos."}
:::

## Entrar en la configuración del firmware

Las teclas de configuración del firmware varían según el fabricante y el modelo; suelen incluir Supr, Escape o una tecla de función durante el inicio. Consulta la documentación del dispositivo en vez de realizar cambios al azar. Algunos sistemas UEFI también ofrecen al sistema operativo una solicitud para reiniciar en la configuración del firmware.

Registra los valores existentes y las claves de recuperación antes de cambiar Secure Boot, el modo del controlador de almacenamiento, TPM, la virtualización o el orden de arranque. Un cambio en el firmware puede hacer temporalmente inaccesibles los volúmenes cifrados o el sistema operativo instalado.

:::single-choice{#boot-bios-setup-key}
¿Por qué no existe una tecla universal para entrar en la configuración del firmware?

::option[Porque Linux asigna una tecla aleatoria nueva después de cada arranque.]{#boot-bios-random-key explanation="El sistema operativo no define aleatoriamente la tecla inicial del firmware."}
::option[Porque el fabricante del sistema elige la tecla y el momento.]{#boot-bios-vendor-key .correct explanation="Las interfaces de firmware difieren entre modelos, por lo que se necesita la documentación oficial del dispositivo."}
::option[Porque solo se puede entrar en la configuración eliminando el cargador.]{#boot-bios-delete-loader explanation="La configuración del firmware es independiente de destruir los archivos de arranque instalados."}
:::

## Resumen

Ahora puedes distinguir los modelos de descubrimiento del arranque mediante BIOS heredado y UEFI.

1. Relaciona el BIOS heredado con el código del primer sector y las etapas posteriores del cargador.
2. Relaciona las entradas UEFI con ejecutables EFI en una ESP.
3. Trata GPT, la interfaz del firmware y el diseño del cargador como elecciones independientes.
4. Cambia los ajustes de confianza y almacenamiento del firmware únicamente con una vía de recuperación.
