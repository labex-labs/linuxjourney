---
index: 6
lang: "es"
title: "lsusb, lspci, lssci"
meta_title: "lsusb, lspci, lssci - Dispositivos"
meta_description: "Descubra cómo listar e inspeccionar hardware USB, PCI y SCSI en su sistema Linux. Esta guía cubre los comandos lsusb, lspci y lssci, incluyendo opciones como lsusb -t para ver árboles de dispositivos."
meta_keywords: "lsusb, lspci, lssci, lsusb -t, listar dispositivos usb, listar dispositivos pci, listar dispositivos scsi, hardware linux, información de dispositivos"
---

## Lesson Content

Al igual que usas el comando `ls` para listar archivos, Linux proporciona herramientas similares para listar dispositivos de hardware. Estos comandos son esenciales para identificar el hardware conectado a tu sistema.

### Listar Dispositivos USB con lsusb

Para ver todos los dispositivos USB conectados a tu sistema, puedes usar el comando `lsusb`. Este comando escanea los concentradores (hubs) USB e informa sobre los dispositivos que encuentra, como cámaras web, teclados y unidades externas.

```bash
lsusb
```

Para una vista más estructurada, puedes usar el comando `lsusb -t`. Esta opción muestra los dispositivos USB en una estructura de árbol, lo cual es útil para comprender cómo los dispositivos están conectados físicamente a los controladores y concentradores USB.

### Listar Dispositivos PCI con lspci

El comando `lspci` se utiliza para listar todos los dispositivos PCI (Peripheral Component Interconnect). Estos son típicamente componentes internos conectados a la placa base, como tarjetas gráficas, adaptadores de red y tarjetas de sonido. Este comando proporciona una visión rápida del hardware central de tu sistema.

```bash
lspci
```

### Listar Dispositivos SCSI y SATA con lssci

Para los dispositivos de almacenamiento, el comando `lssci` es particularmente útil. Lista todos los dispositivos SCSI y SATA conectados, que comúnmente incluyen discos duros, SSD y unidades ópticas (CD/DVD/Blu-ray). Mientras que otros comandos pueden mostrar el controlador de almacenamiento, `lssci` proporciona información directa sobre los dispositivos de almacenamiento en sí, convirtiéndolo en una herramienta valiosa para administradores de sistemas y usuarios que gestionan el almacenamiento.

```bash
lssci
```

## Exercise

Para reforzar tu comprensión sobre la exploración de dispositivos de hardware en Linux, prueba el siguiente laboratorio práctico:

1. **[Explorar Dispositivos de Hardware en Linux](https://labex.io/es/labs/comptia-explore-hardware-devices-in-linux-590861)** - En este laboratorio, aprenderás las habilidades esenciales para explorar, identificar e inspeccionar dispositivos de hardware dentro de un entorno Linux. Obtendrás experiencia práctica con potentes utilidades de línea de comandos para comprender cómo el sistema operativo interactúa con los componentes físicos.

Este laboratorio te ayudará a aplicar estos conceptos en un escenario del mundo real y a ganar confianza en la gestión de la información de los dispositivos.

## Quiz Question

What command is used to view a list of connected USB devices? (Please answer in lowercase English characters only.)

## Quiz Answer

lsusb
