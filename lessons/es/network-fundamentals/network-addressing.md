---
lang: "es"
title: "Direccionamiento de Red"
description: "Aprende los conceptos básicos del direccionamiento de red: direcciones MAC vs. IP y nombres de host. Comprende cómo se comunican los dispositivos en una red. ¡Comienza tu viaje en redes Linux!"
keywords: "direccionamiento de red, dirección MAC, dirección IP, nombre de host, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

Antes de sumergirnos en cómo se mueve un paquete a través de una red, debemos familiarizarnos con cierta terminología. Cuando envías una carta, debes saber a quién se envía y de dónde viene. Los paquetes necesitan la misma información. Nuestros hosts y otros hosts se identifican usando direcciones MAC (Media Access Control) y direcciones IP. Para facilitarnos las cosas a los humanos, usamos nombres de host para identificar un host.

### MAC Addresses

Una dirección MAC es un identificador único utilizado como dirección de hardware. Esta dirección nunca cambiará. Cuando quieres acceder a Internet, tu máquina necesita tener un dispositivo llamado tarjeta de interfaz de red. Este adaptador de red tiene su propia dirección de hardware que se utiliza para identificar tu máquina. Una dirección MAC para un dispositivo Ethernet se ve algo así: `00:C4:B5:45:B2:43`. Las direcciones MAC se asignan a los adaptadores de red cuando se fabrican. Cada fabricante tiene un Identificador Único Organizacional (OUI) para identificarlos como el fabricante. Este OUI se denota por los primeros 3 bytes de la dirección MAC. Por ejemplo, Dell tiene `00-14-22`, por lo que un adaptador de red de Dell podría tener una dirección MAC como: `00-14-22-34-B2-C2`.

### IP Addresses

Una dirección IP se utiliza para identificar un dispositivo en una red. Son independientes del hardware y pueden variar en sintaxis dependiendo de si estás usando IPv4 o IPv6 (más sobre esto más adelante). Por ahora, asumiremos que estás usando IPv4, por lo que una dirección IP típica se vería así: `10.24.12.4`. Las direcciones IP se utilizan con el lado del software de la red. Cada vez que un sistema está conectado a Internet, debe tener una dirección IP. También pueden cambiar si tu red cambia y son únicas para todo Internet (esto no siempre es así una vez que aprendemos sobre NAT).

Recuerda, se necesita tanto software como hardware para mover paquetes a través de redes, por lo que tenemos dos identificadores para cada uno: MAC (hardware) e IP (software).

### Hostnames

Otra forma de identificar tus máquinas es a través de los nombres de host. Los nombres de host toman tu dirección IP y te permiten vincular esa dirección a un nombre legible por humanos. En lugar de recordar `192.12.41.4`, puedes simplemente recordar `myhost.com`.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuántos bytes tiene una dirección IPv4?

## Quiz Answer

4
