---
lesson_id: "boot-process-kernel"
course_id: "boot-system"
lang: "es"
order_index: 4
title: "Proceso de arranque: kernel"
description: "Aprende cómo el kernel inicializa el hardware, ejecuta el espacio de usuario inicial de initramfs, alcanza la raíz real e inicia el PID 1."
meta_title: "Proceso de arranque: kernel - Arrancar el sistema"
meta_description: "Aprende cómo el kernel de Linux utiliza initramfs para preparar la raíz real y ejecutar el primer proceso del espacio de usuario."
meta_keywords: "arranque del kernel, initramfs, initrd, sistema de archivos raíz, PID 1, Linux"
---

Después de que el control alcance el kernel de Linux, este inicializa la gestión de memoria, la planificación, las interrupciones, los controladores integrados, los marcos de seguridad y otros subsistemas esenciales. Analiza la línea de órdenes y se prepara para iniciar el primer proceso del espacio de usuario.

## Por qué existe el espacio de usuario inicial

A veces se puede montar un sistema de archivos raíz sencillo mediante controladores integrados en el kernel. Los sistemas más complejos necesitan módulos y herramientas antes de alcanzar la raíz real. Algunos ejemplos son:

- módulos del controlador de almacenamiento o del sistema de archivos
- desbloqueo de una raíz cifrada
- ensamblaje de LVM o RAID
- configuración de red para una raíz de red
- descubrimiento de dispositivos y resolución de identificadores persistentes

Un initramfs empaqueta estos componentes en un entorno de espacio de usuario inicial que se proporciona junto con el kernel.

:::single-choice{#boot-kernel-initramfs-purpose} ¿Qué problema resuelve habitualmente un initramfs?

::option[Proporciona herramientas y módulos iniciales necesarios antes de que esté disponible la raíz real.]{#boot-kernel-early-tools .correct explanation="El espacio de usuario inicial puede descubrir y ensamblar almacenamiento al que el kernel no puede acceder solo con su soporte integrado."}
::option[Almacena permanentemente en firmware el directorio personal de cada usuario.]{#boot-kernel-home-firmware explanation="El archivo es un elemento de arranque, no almacenamiento permanente de datos de usuarios."}
::option[Sustituye el kernel de Linux después del primer inicio de sesión.]{#boot-kernel-replace-kernel explanation="El kernel permanece activo mientras se ejecuta el código de initramfs en el espacio de usuario."}
:::

## Initramfs e initrd heredado

Un initramfs moderno suele ser uno o varios archivos cpio, a menudo comprimidos, que el kernel desempaqueta en su sistema de archivos raíz inicial. El kernel ejecuta un programa `/init` inicial desde ese entorno.

Un initrd heredado es conceptualmente una imagen de sistema de archivos cargada en un dispositivo de bloques respaldado por RAM y montada. Los términos suelen utilizarse con poca precisión en nombres de archivo y órdenes del cargador, así que examina las herramientas reales en vez de deducir el formato solo por la palabra.

El initramfs debe corresponder al kernel y al diseño de arranque. La ausencia de módulos, identificadores de dispositivos obsoletos o la omisión de herramientas criptográficas y de LVM pueden hacer que un kernel recién instalado no arranque aunque su imagen sea válida.

:::single-choice{#boot-kernel-initramfs-format} ¿Cómo se presenta habitualmente un initramfs moderno al kernel?

::option[Únicamente como un repositorio interactivo de paquetes mediante HTTP.]{#boot-kernel-http-repository explanation="El acceso a red puede configurarse en el espacio de usuario inicial, pero no define el formato de initramfs."}
::option[Como un archivo basado en cpio que se desempaqueta en la raíz inicial.]{#boot-kernel-cpio-archive .correct explanation="El kernel expande el archivo y ejecuta su programa inicial del espacio de usuario."}
::option[Como la cabecera de respaldo GPT del disco.]{#boot-kernel-gpt-header explanation="La redundancia de la tabla de particiones es independiente del archivo de espacio de usuario inicial."}
:::

## Alcanzar la raíz real

El espacio de usuario inicial interpreta parámetros como `root=`, espera los dispositivos necesarios, activa las capas de almacenamiento y monta el sistema de archivos raíz previsto. Después utiliza una operación de cambio de raíz para convertir ese sistema en el nuevo `/` y liberar el entorno inicial temporal cuando sea posible.

La solicitud inicial `ro` de la línea de órdenes puede facilitar comprobaciones de coherencia y un inicio controlado, pero la secuencia exacta depende de la distribución. Las comprobaciones de sistemas de archivos son operaciones del espacio de usuario, y el initramfs o el sistema init posterior puede volver a montar la raíz en lectura y escritura cuando la política lo permita.

:::single-choice{#boot-kernel-root-switch} ¿Qué ocurre después de que el espacio de usuario inicial monte correctamente la raíz real prevista?

::option[Se vuelve a crear la tabla de particiones de todos los discos.]{#boot-kernel-recreate-tables explanation="Cambiar la raíz no vuelve a particionar el almacenamiento."}
::option[El kernel termina y el firmware reanuda la planificación normal de procesos.]{#boot-kernel-firmware-schedules explanation="El kernel de Linux sigue siendo responsable de los procesos y el hardware después de la transferencia."}
::option[El arranque cambia la vista raíz a ese sistema de archivos y continúa el inicio del espacio de usuario.]{#boot-kernel-switch-root .correct explanation="La raíz inicial temporal transfiere el control a la jerarquía raíz del sistema instalado."}
:::

## Iniciar el PID 1

El kernel ejecuta el programa init configurado, normalmente alcanzado mediante una ruta como `/sbin/init` o seleccionado con `init=`. Ese proceso recibe el PID 1 y se hace responsable del entorno principal de servicios del espacio de usuario.

Si no se puede ejecutar un programa init utilizable, el kernel no puede continuar hacia un sistema normal de usuario y suele comunicar un fallo de arranque o panic. Depura la primera capa que falle: kernel y línea de órdenes, contenido de initramfs, descubrimiento de la raíz, montaje de la raíz o ejecución del PID 1.

:::single-choice{#boot-kernel-pid-one} ¿Cuál es la última gran transferencia del kernel en esta etapa simplificada del arranque?

::option[Ejecutar el primer programa del espacio de usuario como PID 1.]{#boot-kernel-exec-init .correct explanation="El PID 1 inicia después los servicios y el estado configurado del sistema."}
::option[Convertir `/proc` en una base de datos persistente de paquetes.]{#boot-kernel-proc-package explanation="Procfs sigue siendo una interfaz del kernel durante la ejecución."}
::option[Asignar el mismo PID a todos los procesos posteriores.]{#boot-kernel-same-pid explanation="Cada proceso activo recibe su propio PID dentro de un espacio de nombres."}
:::

## Resumen

Ahora puedes seguir el arranque del kernel a través del espacio de usuario inicial hasta el PID 1.

1. Separa la inicialización integrada del kernel de los módulos iniciales cargables.
2. Relaciona initramfs con una raíz temporal basada en cpio y `/init`.
3. Sigue el ensamblaje del almacenamiento y el cambio a la raíz real.
4. Identifica la ejecución del PID 1 como la transferencia al espacio de usuario.
