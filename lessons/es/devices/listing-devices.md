---
lesson_id: "listing-devices"
course_id: "devices"
lang: "es"
order_index: 6
title: "lsusb, lspci, lsscsi"
description: "Aprende a examinar la topología USB, las funciones PCI, los dispositivos de la capa SCSI y sus controladores activos."
meta_title: "lsusb, lspci, lsscsi - Dispositivos"
meta_description: "Descubre cómo mostrar e inspeccionar hardware USB, PCI y SCSI en Linux mediante lsusb, lspci y lsscsi."
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, dispositivos USB, dispositivos PCI, dispositivos SCSI, hardware Linux"
---

Linux ofrece herramientas de inventario específicas para buses y subsistemas. Cada orden muestra una vista distinta, así que combina sus identificadores, topología, controladores, rutas de sysfs y registros en vez de esperar una lista completa del hardware en una sola herramienta.

## Examinar dispositivos USB

`lsusb` muestra los dispositivos visibles mediante el subsistema USB:

```bash
$ lsusb
```

La salida suele incluir los números de bus y dispositivo, un par de identificadores de fabricante y producto, y una descripción procedente de la base de datos local de identificadores USB. La dirección numérica de bus y dispositivo puede cambiar tras volver a conectarlo o reiniciar, y no debe tratarse como una identidad persistente.

Muestra las relaciones entre controladores, concentradores, puertos, interfaces, controladores del kernel y velocidades con:

```bash
$ lsusb -t
```

Existe una salida detallada de descriptores, pero algunos datos necesitan acceso de lectura elevado. No concedas permisos amplios sobre dispositivos USB solo para que una orden de inspección muestre menos avisos.

:::single-choice{#listing-devices-usb-tree} ¿Qué orden muestra los dispositivos USB como un árbol de topología?

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="Esta orden muestra funciones PCI e información de controladores del kernel, no la topología USB."}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="Esta no es la orden de árbol USB presentada."}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="La opción de árbol muestra los dispositivos bajo controladores y concentradores, con las relaciones de puertos e interfaces."}
:::

## Examinar funciones PCI

`lspci` muestra las funciones descubiertas en buses PCI y PCI Express:

```bash
$ lspci
```

Los dispositivos PCIe internos y externos pueden incluir controladores de gráficos, red, almacenamiento, USB, audio y puentes. Muestra el controlador del kernel utilizado y los módulos candidatos con:

```bash
$ lspci -k
```

Que un controlador PCI aparezca en la lista no demuestra que todos los dispositivos situados tras él estén inicializados o funcionen correctamente. Al resolver problemas, comprueba la vinculación del controlador y los registros del kernel.

:::single-choice{#listing-devices-pci-driver} ¿Qué orden añade información del controlador del kernel a un listado PCI?

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="La opción `-k` muestra el controlador activo del kernel y los módulos capaces de manejar cada dispositivo PCI."}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="Esta orden describe la jerarquía USB y los controladores de interfaces."}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="Esta orden comunica campos de dispositivos de bloques y sistemas de archivos, no la vinculación de controladores PCI."}
:::

## Examinar dispositivos de la capa SCSI

`lsscsi` muestra los dispositivos representados mediante la capa intermedia SCSI de Linux:

```bash
$ lsscsi
```

Puede incluir dispositivos SCSI nativos y discos SATA, de almacenamiento USB o virtuales presentados mediante capas compatibles con SCSI. Los espacios de nombres NVMe suelen pertenecer a otro subsistema y `lsscsi` no los incluye en un inventario completo.

Para ver una jerarquía orientada al almacenamiento que incluya muchos tipos de dispositivos de bloques, utiliza también `lsblk`:

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope} ¿Qué muestra principalmente `lsscsi`?

::option[Exclusivamente todos los espacios de nombres y controladores NVMe.]{#listing-devices-only-nvme explanation="NVMe utiliza su propio subsistema y sus propias herramientas, aunque algunas vistas de bloques relacionadas pueden aparecer en otros lugares."}
::option[Únicamente archivos cuyos nombres terminan en `.scsi`.]{#listing-devices-scsi-extension explanation="La orden consulta interfaces de dispositivos del kernel, no extensiones de nombres de archivo."}
::option[Dispositivos representados mediante la capa intermedia SCSI de Linux.]{#listing-devices-scsi-mid-layer .correct explanation="La orden comunica hosts, destinos y unidades lógicas SCSI, y los nodos de dispositivo correspondientes cuando están disponibles."}
:::

## Interpretar los resultados del inventario

Las descripciones suelen proceder de bases de datos locales de identificadores y pueden ser genéricas u obsoletas. Un dispositivo mostrado puede carecer de un controlador funcional, y un entorno virtualizado puede presentar hardware emulado o paravirtual. Relaciona los resultados con `udevadm info`, sysfs, `lsblk`, herramientas de red y `journalctl -k` o `dmesg`, según los permisos y el problema investigado.

Las utilidades pueden distribuirse por separado, normalmente en paquetes como `usbutils`, `pciutils` y `lsscsi`. Si falta una orden, utiliza el gestor de paquetes de la distribución en vez de descargar sustitutos desconocidos.

:::single-choice{#listing-devices-listed-not-working} ¿Ver un dispositivo en `lspci` demuestra que su controlador está activo y funciona correctamente?

::option[No; examina también la vinculación del controlador y los mensajes pertinentes del kernel.]{#listing-devices-needs-correlation .correct explanation="La enumeración demuestra que una función PCI es visible, no que la inicialización de nivel superior haya terminado correctamente."}
::option[Sí; la enumeración PCI realiza una prueba funcional completa.]{#listing-devices-complete-test explanation="El listado no ejercita todas las funciones del hardware ni valida el comportamiento de los servicios."}
::option[Sí; `lspci` instala automáticamente un controlador apropiado.]{#listing-devices-installs-driver explanation="La orden es una herramienta de inventario y no instala paquetes de controladores."}
:::

Utiliza [Explorar dispositivos de hardware en Linux](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861) para comparar estas vistas de subsistemas en un equipo controlado.

## Resumen

Ahora puedes seleccionar una orden de inventario para el subsistema de dispositivos correspondiente.

1. Utiliza `lsusb` y `lsusb -t` para la identidad y la topología USB.
2. Utiliza `lspci -k` para las funciones PCI y la vinculación de controladores.
3. Utiliza `lsscsi` para dispositivos de la capa SCSI y `lsblk` para la topología de bloques.
4. Relaciona la enumeración con controladores, sysfs y mensajes del kernel.
