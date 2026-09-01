---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "es"
order_index: 4
title: "Instalación del kernel"
description: "Aprende a instalar, arrancar, validar y conservar un kernel de la distribución con una alternativa probada."
meta_title: "Instalación del kernel - Kernel"
meta_description: "Aprende a instalar y gestionar kernels de Linux. Descubre las versiones del kernel y utiliza `uname -r` y comandos apt. Comienza tu recorrido por el kernel de Linux."
meta_keywords: "kernel de Linux, instalar kernel, uname -r, apt dist-upgrade, gestión de kernel, tutorial de Linux, Linux para principiantes, guía de Linux"
---

Las distribuciones empaquetan los kernels junto con los módulos, la integración con initramfs, las actualizaciones del cargador de arranque, las firmas y la política de soporte. Utiliza ese flujo gestionado salvo que estés desarrollando o probando deliberadamente un kernel personalizado y puedas recuperar la máquina.

## Kernels en ejecución e instalados

Muestra la versión del kernel que se está ejecutando actualmente:

```bash
$ uname -r
6.8.0-00-generic
```

Esto no lista todos los kernels instalados y no cambia inmediatamente cuando se instala un paquete más reciente. El sistema debe arrancar la imagen nueva antes de que `uname -r` informe de ella. Consulta los paquetes instalados y las entradas de arranque con las herramientas propias de la distribución.

:::single-choice{#kernel-installation-uname-release} ¿Qué muestra `uname -r`?

::option[La cadena de versión del kernel que se está ejecutando actualmente.]{#kernel-installation-running-release .correct explanation="Informa del estado activo del kernel, no solo de la imagen más reciente almacenada en el disco."}
::option[Todos los paquetes de kernel disponibles en todos los repositorios.]{#kernel-installation-all-packages explanation="El inventario del repositorio corresponde al gestor de paquetes."}
::option[La versión del firmware de todos los dispositivos conectados.]{#kernel-installation-device-firmware explanation="La versión del kernel y el inventario del firmware de los dispositivos son datos distintos."}
:::

## Preferir el paquete de seguimiento de la distribución

Instala o conserva el paquete de seguimiento o metapaquete de kernel compatible de la distribución para seguir recibiendo futuras actualizaciones de seguridad. Los nombres de los paquetes dependen de la versión, la arquitectura, la clase de hardware y la variante del kernel. Por ejemplo, Ubuntu suele ofrecer `linux-generic`, pero los sistemas en la nube, de baja latencia, HWE, OEM, de tiempo real y específicos de una arquitectura utilizan otros paquetes.

No conviertas directamente una cadena de versión de `uname -r` en un operando de `apt install` suponiendo que será válido. Consulta la documentación actual de la distribución e inspecciona los candidatos con el gestor de paquetes antes de instalar.

:::single-choice{#kernel-installation-meta-package} ¿Por qué resulta útil un metapaquete de kernel compatible?

::option[Garantiza que nunca sea necesario reiniciar.]{#kernel-installation-no-reboot explanation="Un kernel recién instalado solo se activa después de arrancarlo, salvo el alcance limitado de mecanismos especializados de parcheo en vivo."}
::option[Convierte todos los controladores externos al árbol en código integrado.]{#kernel-installation-convert-drivers explanation="Los módulos externos siguen necesitando compilaciones y firmas compatibles."}
::option[Sigue la secuencia de actualizaciones del kernel prevista por la distribución.]{#kernel-installation-update-tracking .correct explanation="Las dependencias trasladan el sistema a paquetes de imágenes y módulos compatibles más recientes a medida que se publican actualizaciones."}
:::

## Comprobaciones previas al cambio

Antes de una transacción del kernel:

1. Confirma los repositorios compatibles, las firmas de los paquetes, el ciclo de vida de la versión y la variante de kernel prevista.
2. Asegúrate de que `/boot` o la partición del sistema EFI tenga espacio suficiente.
3. Conserva al menos un kernel instalado cuyo funcionamiento esté comprobado y una entrada de arranque que se pueda seleccionar.
4. Comprueba el acceso mediante consola, administración remota y medios de rescate, así como las vías de recuperación del cifrado y de reversión.
5. Comprueba los módulos externos al árbol, los controladores de almacenamiento y red, las firmas de Secure Boot, la hibernación y la compatibilidad con la virtualización.

La transacción de paquetes debe generar un initramfs correspondiente y actualizar las entradas de arranque mediante los mecanismos de la distribución. Lee todos los errores; que un paquete figure como instalado no basta si falló la generación del initramfs o del cargador.

:::single-choice{#kernel-installation-initramfs-error} ¿Por qué un error al generar el initramfs impide considerar que la operación tuvo éxito?

::option[La generación del initramfs cambia la contraseña del shell del usuario.]{#kernel-installation-initramfs-password explanation="El flujo del archivo de arranque no está relacionado con los secretos de autenticación de las cuentas."}
::option[El kernel nuevo puede carecer de los módulos o herramientas iniciales necesarios para llegar al almacenamiento raíz.]{#kernel-installation-missing-early-tools .correct explanation="Una imagen puede estar instalada mientras falta o está obsoleto el artefacto del espacio de usuario inicial que necesita."}
::option[El error demuestra que el kernel que estaba en ejecución ya se ha detenido.]{#kernel-installation-current-stopped explanation="Los mecanismos de los paquetes se ejecutan mientras el kernel anterior puede seguir activo."}
:::

## Arrancar y validar

Programa un reinicio controlado teniendo en cuenta a las partes interesadas y las cargas de trabajo activas. Asegúrate de que la consola permita seleccionar la entrada anterior si falla la predeterminada. Después del arranque:

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

Utiliza herramientas equivalentes en sistemas que no usen systemd. Valida el almacenamiento, los sistemas de archivos, la red, los gráficos, los dispositivos de entrada, los módulos de seguridad, los módulos externos, los contenedores, las máquinas virtuales y la salud de las aplicaciones. Un indicador de inicio de sesión no constituye por sí solo una validación completa.

:::single-choice{#kernel-installation-activation} ¿Cuándo se convierte un paquete de kernel ordinario recién instalado en el kernel en ejecución?

::option[En cuanto se escribe `uname -r`.]{#kernel-installation-uname-activates explanation="Uname es de solo lectura y no puede cambiar de kernel."}
::option[Después de que la máquina arranca esa imagen del kernel.]{#kernel-installation-after-boot .correct explanation="Instalar archivos no sustituye el kernel que ya se está ejecutando en memoria."}
::option[Cuando se descarga el archivo del paquete, antes de instalarlo.]{#kernel-installation-download-activates explanation="Un archivo descargado no afecta a la ejecución activa."}
:::

## Eliminar kernels antiguos

Usa el flujo de limpieza compatible del gestor de paquetes solo después de que el kernel nuevo haya superado la validación. Nunca elimines el kernel en ejecución, la única alternativa cuyo funcionamiento esté comprobado ni los paquetes que necesite el paquete de seguimiento activo. Revisa la propuesta exacta de eliminación y las entradas de arranque resultantes.

Eliminar archivos manualmente de `/boot` deja incoherentes los estados de los paquetes y del cargador. Si ya se ha agotado el espacio, crea un plan de recuperación antes de modificar archivos en lugar de borrar imágenes arbitrarias.

:::single-choice{#kernel-installation-old-kernel-removal} ¿Qué kernel debe permanecer instalado durante la validación inicial de uno nuevo?

::option[Únicamente el kernel nuevo que aún no se ha probado.]{#kernel-installation-only-new explanation="Eliminar todas las alternativas antes de probar convierte un problema de compatibilidad en un incidente de recuperación."}
::option[Ningún archivo de kernel bajo la ruta de arranque.]{#kernel-installation-no-kernels explanation="La máquina necesita un artefacto de kernel que se pueda cargar para arrancar Linux."}
::option[Una alternativa de funcionamiento comprobado que se pueda seleccionar mediante el cargador de arranque.]{#kernel-installation-known-good-fallback .correct explanation="La alternativa proporciona una vía de recuperación cuando el kernel nuevo falla con el hardware o las cargas de trabajo."}
:::

El laboratorio [Personalizar el menú de arranque de GRUB2](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859) proporciona un entorno seguro para la recuperación en el que comprender varias entradas.

## Resumen

Ahora puedes tratar una actualización del kernel como un cambio en la cadena de arranque y la compatibilidad.

1. Distingue la versión en ejecución de las imágenes instaladas.
2. Sigue las actualizaciones compatibles mediante el paquete correcto de la distribución.
3. Comprueba previamente el almacenamiento, el initramfs, las firmas, los módulos y el acceso de recuperación.
4. Arranca y valida el comportamiento del hardware y las aplicaciones.
5. Conserva una alternativa de funcionamiento comprobado hasta demostrar que el kernel nuevo funciona.
