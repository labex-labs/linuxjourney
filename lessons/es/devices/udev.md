---
index: 5
lang: "es"
title: "udev"
meta_title: "udev - Dispositivos"
meta_description: "Aprende sobre udev, cómo gestiona dinámicamente los archivos de dispositivos Linux y usa udevadm. Comprende la creación de nodos de dispositivo para principiantes."
meta_keywords: "udev, udevadm, gestión de dispositivos Linux, archivos de dispositivos, tutorial de Linux, Linux para principiantes, reglas de udev, guía de Linux"
---

## Lesson Content

Antiguamente, y de hecho hoy en día si realmente quisieras, crearías nodos de dispositivo usando un comando como:

```bash
mknod /dev/sdb1 b 8 3
```

Este comando creará un nodo de dispositivo `/dev/sdb1` y lo convertirá en un dispositivo de bloque (b) con un número mayor de 8 y un número menor de 3.

Para eliminar un dispositivo, simplemente harías un **rm** del archivo del dispositivo en el directorio `/dev`.

Afortunadamente, ya no necesitamos hacer esto gracias a udev. El sistema udev crea y elimina dinámicamente archivos de dispositivo por nosotros, dependiendo de si están conectados o no. Hay un demonio `udevd` que se ejecuta en el sistema y escucha los mensajes del kernel sobre los dispositivos conectados al sistema. `Udevd` analizará esa información y hará coincidir los datos con las reglas especificadas en `/etc/udev/rules.d`. Dependiendo de esas reglas, lo más probable es que cree nodos de dispositivo y enlaces simbólicos para los dispositivos. Puedes escribir tus propias reglas de udev, pero eso está un poco fuera del alcance de esta lección. Afortunadamente, tu sistema ya viene con muchas reglas de udev, por lo que es posible que nunca necesites escribir las tuyas propias.

También puedes ver la base de datos de udev y sysfs usando el comando **udevadm**. Esta herramienta es muy útil, pero a veces puede volverse muy complicada. Un comando simple para ver información de un dispositivo sería:

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la interacción con el hardware y la gestión de dispositivos en Linux:

1. **[Explorar dispositivos de hardware en Linux](https://labex.io/es/labs/comptia-explore-hardware-devices-in-linux-590861)** - En este laboratorio, aprenderás las habilidades esenciales para explorar, identificar e inspeccionar dispositivos de hardware dentro de un entorno Linux. Obtendrás experiencia práctica con potentes utilidades de línea de comandos para comprender cómo el sistema operativo interactúa con los componentes físicos, lo cual es crucial para entender los nodos de dispositivo y el papel de udev.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a desarrollar confianza en la gestión de hardware de Linux.

## Quiz Question

¿Qué añade y elimina dispositivos dinámicamente?

## Quiz Answer

udev
