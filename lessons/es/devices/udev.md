---
lang: "es"
title: "udev"
description: "Aprende sobre udev, cómo gestiona dinámicamente los archivos de dispositivo de Linux y usa udevadm. Comprende la creación de nodos de dispositivo para principiantes."
keywords: "udev, udevadm, gestión de dispositivos Linux, archivos de dispositivo, tutorial de Linux, Linux para principiantes, reglas de udev, guía de Linux"
---

## Lesson Content

Antiguamente, y de hecho hoy en día si realmente quisieras, crearías nodos de dispositivo usando un comando como:

```bash
mknod /dev/sdb1 b 8 3
```

Este comando creará un nodo de dispositivo `/dev/sdb1` y lo convertirá en un dispositivo de bloque (b) con un número mayor de 8 y un número menor de 3.

Para eliminar un dispositivo, simplemente usarías `rm` para borrar el archivo del dispositivo en el directorio `/dev`.

Por suerte, ya no necesitamos hacer esto gracias a udev. El sistema udev crea y elimina dinámicamente archivos de dispositivo por nosotros, dependiendo de si están conectados o no. Hay un demonio `udevd` que se ejecuta en el sistema y escucha los mensajes del kernel sobre los dispositivos conectados al sistema. `Udevd` analizará esa información y hará coincidir los datos con las reglas especificadas en `/etc/udev/rules.d`. Dependiendo de esas reglas, lo más probable es que cree nodos de dispositivo y enlaces simbólicos para los dispositivos. Puedes escribir tus propias reglas de udev, pero eso está un poco fuera del alcance de esta lección. Afortunadamente, tu sistema ya viene con muchas reglas de udev, por lo que es posible que nunca necesites escribir las tuyas propias.

También puedes ver la base de datos de udev y sysfs usando el comando `udevadm`. Esta herramienta es muy útil, pero a veces puede volverse muy complicada. Un comando simple para ver información de un dispositivo sería:

```bash
udevadm info --query=all --name=/dev/sda
```

## Exercise

Ejecuta el comando `udevadm` proporcionado y revisa la salida.

## Quiz Question

¿Qué añade y elimina dispositivos dinámicamente?

## Quiz Answer

udev
