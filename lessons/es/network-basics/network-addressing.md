---
index: 4
lang: "es"
title: "Direccionamiento de Red"
meta_title: "Direccionamiento de Red - Fundamentos de Red"
meta_description: "Descubra los fundamentos del direccionamiento de red. Esta guía explica las direcciones MAC, direcciones IP y nombres de host, conceptos clave para entender cómo se comunican los dispositivos en redes Linux."
meta_keywords: "direccionamiento de red, dirección MAC, dirección IP, nombre de host, identificadores de red, redes Linux, fundamentos de red, principiante, tutorial, guía"
---

## Lesson Content

Antes de explorar cómo viajan los paquetes de datos a través de una red, es esencial comprender algo de terminología central. Al igual que una carta física necesita una dirección de destino y de remitente, los paquetes de red requieren información similar para llegar a su objetivo. En redes informáticas, los dispositivos se identifican mediante direcciones MAC (Control de Acceso al Medio) y direcciones IP. Para simplificar las cosas para los humanos, también usamos nombres de host.

### Direcciones MAC

Una dirección MAC es un identificador de hardware único y permanente asignado a una tarjeta de interfaz de red (NIC). Esta dirección se graba en el dispositivo durante la fabricación y no cambia. Cada dispositivo que se conecta a una red, como su computadora o teléfono inteligente, tiene una NIC con una dirección MAC distinta. Esta dirección de hardware es crucial para la comunicación en un segmento de red local. Una dirección MAC de Ethernet típicamente se ve así: `00:C4:B5:45:B2:43`. Los primeros tres bytes de la dirección forman el Identificador Único Organizacional (OUI), que identifica al fabricante. Por ejemplo, Dell utiliza el OUI `00-14-22`, por lo que una NIC de Dell podría tener una dirección MAC como `00-14-22-34-B2-C2`.

### Direcciones IP

Una dirección IP es un identificador lógico para un dispositivo en una red, lo que lo hace accesible a través de diferentes redes, incluido Internet. A diferencia de una dirección MAC, una dirección IP no está ligada al hardware y puede asignarse dinámicamente. Nos centraremos en IPv4 por ahora, donde una dirección se parece a `10.24.12.4`. Las direcciones IP son fundamentales para el lado del software de las redes, ya que permiten el enrutamiento y la comunicación global. Si bien las direcciones IP públicas son únicas en todo Internet, pueden cambiar, y tecnologías como la Traducción de Direcciones de Red (NAT) permiten direcciones privadas no únicas dentro de una red local. Es importante recordar que tanto las direcciones MAC (hardware) como las IP (software) son necesarias para una comunicación de red exitosa.

### Nombres de Host

Aunque las direcciones IP son efectivas para las computadoras, son difíciles de recordar para los humanos. Los nombres de host resuelven este problema al mapear un nombre fácil de usar a una dirección IP. Por ejemplo, es mucho más fácil recordar `mihost.com` que su dirección IP correspondiente, como `192.12.41.4`. Este mapeo es manejado por el Sistema de Nombres de Dominio (DNS), que actúa como la guía telefónica de Internet, traduciendo nombres de host memorables a las direcciones IP numéricas requeridas para el enrutamiento de red.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de los identificadores de red como direcciones MAC, direcciones IP y nombres de host:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones MAC e IP, en un sistema Linux.
2. **[Explorar tipos de direcciones IP y alcanzabilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore diferentes tipos de direcciones IP y pruebe la alcanzabilidad de la red usando `ping` e `ip a`.
3. **[Administrar la resolución de nombres de host locales en Linux](https://labex.io/es/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Aprenda a administrar la resolución de nombres de host locales editando el archivo `/etc/hosts` y probando sus cambios.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con las redes fundamentales de Linux.

## Quiz Question

¿Cuántos bytes tiene una dirección IPv4?

## Quiz Answer

4
