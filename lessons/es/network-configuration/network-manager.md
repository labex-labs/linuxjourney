---
index: 4
lang: "es"
title: "Network Manager"
meta_title: "Network Manager - Configuración de red"
meta_description: "Aprenda sobre NetworkManager en Linux, cómo automatiza la configuración de red y use los comandos nm-tool y nmcli. ¡Comience con esta guía para principiantes!"
meta_keywords: "NetworkManager, nm-tool, nmcli, redes Linux, configuración de red, tutorial Linux, guía para principiantes"
---

## Lesson Content

Por supuesto, si desea que la red de su sistema funcione automáticamente, ya existe algo para ello. La mayoría de las distribuciones utilizan el demonio NetworkManager para configurar sus redes automáticamente.

Notará NetworkManager en forma de un applet en algún lugar de la barra de tareas de su escritorio si está utilizando una GUI. Como puede ver, gestiona el hardware de su red y la información de conexión. Por ejemplo, al iniciar, NetworkManager recopilará información del hardware de red, buscará conexiones (inalámbricas, cableadas, etc.) y luego las activará.

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

¡La práctica hace al maestro! Si bien NetworkManager automatiza gran parte de la configuración de red, comprender los comandos y conceptos subyacentes que gestiona es crucial para la resolución de problemas y la administración avanzada. Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la identificación y gestión de redes en Linux:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones MAC e IP, en un sistema Linux.
2. **[Gestionar el direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a configurar direcciones IP estáticas y dinámicas, establecer puertas de enlace predeterminadas y verificar configuraciones de red usando el comando `ip` y `dhclient`.
3. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` y `arp` para comprender cómo interactúan las capas de red y de enlace de datos, observando ARP en acción y cómo las puertas de enlace predeterminadas manejan el tráfico.

Estos laboratorios le ayudarán a aplicar los conceptos de identificación y configuración de red en escenarios reales y a generar confianza con los fundamentos de redes de Linux.

## Quiz Question

¿Cuál es el comando para ver la información de NetworkManager?

## Quiz Answer

nm-tool
