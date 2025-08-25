---
index: 4
lang: "es"
title: "Direccionamiento de Red"
meta_title: "Direccionamiento de Red - Conceptos Básicos de Redes"
meta_description: "Aprende los conceptos básicos del direccionamiento de red: direcciones MAC vs. IP y nombres de host. Comprende cómo se comunican los dispositivos en una red. ¡Comienza tu viaje en redes Linux!"
meta_keywords: "direccionamiento de red, dirección MAC, dirección IP, nombre de host, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

Antes de sumergirnos en cómo se mueve un paquete a través de una red, debemos familiarizarnos con cierta terminología. Cuando envías una carta, debes saber a quién se envía y de dónde viene. Los paquetes necesitan la misma información. Nuestros hosts y otros hosts se identifican utilizando direcciones MAC (Media Access Control) y direcciones IP. Para facilitarnos las cosas a los humanos, usamos nombres de host para identificar un host.

### Direcciones MAC

Una dirección MAC es un identificador único utilizado como dirección de hardware. Esta dirección nunca cambiará. Cuando quieres acceder a Internet, tu máquina necesita tener un dispositivo llamado tarjeta de interfaz de red. Este adaptador de red tiene su propia dirección de hardware que se utiliza para identificar tu máquina. Una dirección MAC para un dispositivo Ethernet se ve algo así: `00:C4:B5:45:B2:43`. Las direcciones MAC se asignan a los adaptadores de red cuando se fabrican. Cada fabricante tiene un Identificador Único de Organización (OUI) para identificarlos como el fabricante. Este OUI se denota por los primeros 3 bytes de la dirección MAC. Por ejemplo, Dell tiene `00-14-22`, por lo que un adaptador de red de Dell podría tener una dirección MAC como: `00-14-22-34-B2-C2`.

### Direcciones IP

Una dirección IP se utiliza para identificar un dispositivo en una red. Son independientes del hardware y pueden variar en sintaxis dependiendo de si estás usando IPv4 o IPv6 (más sobre esto más adelante). Por ahora, asumiremos que estás usando IPv4, por lo que una dirección IP típica se vería así: `10.24.12.4`. Las direcciones IP se utilizan con el lado del software de la red. Cada vez que un sistema se conecta a Internet, debe tener una dirección IP. También pueden cambiar si tu red cambia y son únicas para todo Internet (esto no siempre es así una vez que aprendemos sobre NAT).

Recuerda, se necesita tanto software como hardware para mover paquetes a través de las redes, por lo que tenemos dos identificadores para cada uno: MAC (hardware) e IP (software).

### Nombres de host

Una última forma de identificar tus máquinas es a través de los nombres de host. Los nombres de host toman tu dirección IP y te permiten vincular esa dirección a un nombre legible por humanos. En lugar de recordar `192.12.41.4`, simplemente puedes recordar `myhost.com`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los identificadores de red como las direcciones MAC, las direcciones IP y los nombres de host:

1. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - Practica el uso del comando `ip a` para identificar información de direccionamiento de red, incluyendo direcciones MAC e IP, en un sistema Linux.
2. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Explora diferentes tipos de direcciones IP y prueba la accesibilidad de la red usando `ping` e `ip a`.
3. **[Administrar la resolución de nombres de host locales en Linux](https://labex.io/es/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - Aprende a administrar la resolución de nombres de host locales editando el archivo `/etc/hosts` y probando tus cambios.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con los fundamentos de las redes en Linux.

## Quiz Question

¿Cuántos bytes tiene una dirección IPv4?

## Quiz Answer

4
