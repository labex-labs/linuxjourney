---
lang: "es"
title: "Network Manager"
description: "Aprenda sobre NetworkManager en Linux, cómo automatiza la configuración de red y use los comandos nm-tool y nmcli. ¡Comience con esta guía para principiantes!"
keywords: "NetworkManager, nm-tool, nmcli, redes Linux, configuración de red, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Por supuesto, si desea que la red de su sistema funcione automáticamente, ya existe algo para ello. La mayoría de las distribuciones utilizan el demonio NetworkManager para configurar sus redes automáticamente.

Notará NetworkManager en forma de un applet en algún lugar de la barra de tareas de su escritorio si está utilizando una GUI. Como puede ver, gestiona el hardware y la información de conexión de su red. Por ejemplo, al iniciar, NetworkManager recopilará información del hardware de red, buscará conexiones (inalámbricas, cableadas, etc.) y luego las activará.

También hay herramientas de línea de comandos para interactuar con NetworkManager:

### nm-tool

`nm-tool` informa el estado de NetworkManager y sus dispositivos.

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

El comando `nmcli` le permite controlar y modificar NetworkManager. Consulte la página man para más detalles.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuál es el comando para ver la información de NetworkManager?

## Quiz Answer

nm-tool
