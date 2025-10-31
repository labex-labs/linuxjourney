---
index: 4
lang: "es"
title: "Gestor de Red"
meta_title: "Gestor de Red - Configuración de Red"
meta_description: "Descubra el rol del demonio NetworkManager en la gestión moderna de redes Linux. Aprenda cómo esta herramienta automatiza la configuración de red y cómo interactuar con ella usando nm-tool y la potente utilidad de línea de comandos nmcli."
meta_keywords: "NetworkManager, nm-tool, nmcli, gestor de red linux, networkmanager linux, gestor red linux, gestión de red linux, configuración de red, redes Linux"
---

## Lesson Content

Para que la red de un sistema se configure automáticamente, normalmente ya existe un servicio implementado. La mayoría de las distribuciones modernas de Linux utilizan el demonio NetworkManager para este propósito, convirtiéndolo en una piedra angular de la **gestión de redes de Linux**.

### ¿Qué es Network Manager en Linux?

Si está utilizando una interfaz gráfica de usuario (GUI), probablemente notará el servicio **Network Manager Linux** como un applet en la barra de tareas de su escritorio. Esta herramienta administra su hardware de red y la información de conexión. Por ejemplo, al iniciarse, NetworkManager recopila información sobre el hardware de red, busca conexiones disponibles (como redes inalámbricas o cableadas) y luego las activa para conectarlo a Internet.

### Interacción desde la Línea de Comandos

Aunque el applet de la GUI es conveniente, también existen potentes herramientas de línea de comandos para interactuar con el servicio **networkmanager linux**. Estas son esenciales para la administración de servidores y la creación de scripts.

### Uso de nm-tool

El comando `nm-tool` informa sobre el estado actual de NetworkManager y una lista de sus dispositivos administrados. Tenga en cuenta que `nm-tool` se considera obsoleto en muchos sistemas modernos en favor de `nmcli`.

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

### La Herramienta Moderna nmcli

El comando `nmcli` es la principal utilidad de línea de comandos para controlar y modificar el **Network Manager de Linux**. Le permite ver el estado, administrar conexiones y configurar dispositivos de red directamente desde la terminal. Para obtener una lista completa de sus capacidades, consulte su página de manual (`man nmcli`).

## Exercise

¡La práctica hace al maestro! Si bien NetworkManager automatiza gran parte de la configuración de red, comprender los comandos y conceptos subyacentes que administra es crucial para la solución de problemas y la administración avanzada. Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la identificación y gestión de redes en Linux:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones MAC e IP, en un sistema Linux.
2. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a configurar direcciones IP estáticas y dinámicas, establecer puertas de enlace predeterminadas y verificar configuraciones de red utilizando el comando `ip` y `dhclient`.
3. **[Explorar la interacción de la capa de red con ping y arp en Linux](https://labex.io/es/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - Use `ping` y `arp` para comprender cómo interactúan las capas de red y de enlace de datos, observando ARP en acción y cómo las puertas de enlace predeterminadas manejan el tráfico.

Estos laboratorios le ayudarán a aplicar los conceptos de identificación y configuración de red en escenarios reales y a ganar confianza con los fundamentos de redes de Linux.

## Quiz Question

¿Cuál es el comando para ver un resumen del estado y los dispositivos de NetworkManager como se muestra en la lección? Por favor, responda usando solo el nombre del comando en inglés en minúsculas.

## Quiz Answer

nm-tool
