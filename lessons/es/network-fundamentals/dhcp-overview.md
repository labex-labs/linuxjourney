---
index: 9
lang: "es"
title: "Descripción general de DHCP"
meta_title: "Descripción general de DHCP - Conceptos básicos de red"
meta_description: "Aprende sobre DHCP (Dynamic Host Configuration Protocol) en Linux. Comprende cómo DHCP asigna direcciones IP y su proceso de cuatro pasos. ¡Comienza tu viaje en redes Linux!"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, redes Linux, dirección IP, tutorial DHCP, principiante, guía"
---

## Lesson Content

Un concepto de red importante que aún no hemos revisado es DHCP (Dynamic Host Configuration Protocol).

DHCP asigna direcciones IP, máscaras de subred y puertas de enlace a nuestras máquinas. Por ejemplo, digamos que tienes un teléfono celular y quieres obtener un número de teléfono celular para empezar a hablar con la gente. Tienes que llamar a tu operador de telefonía, y ellos te darán un número. Mientras pagues tus facturas, puedes seguir usando tu teléfono. DHCP es el operador de telefonía en este caso; te da una dirección IP para que puedas hablar con otras direcciones IP. También se te arrienda una dirección IP; estas duran un cierto período de tiempo, luego se renovarán dependiendo de cómo tengas configurados tus ajustes de arrendamiento.

DHCP es excelente por muchas razones: permite que un administrador de red no se preocupe por asignar direcciones IP, y también evita que configuren direcciones IP duplicadas. Cada red física debe tener su propio servidor DHCP para que un host pueda solicitar una dirección IP. En un entorno doméstico regular, el enrutador suele actuar como servidor DHCP.

La forma en que DHCP obtiene toda la información de tu host dinámico es:

1. DHCP DISCOVER - Este mensaje se difunde para buscar un servidor DHCP.
2. DHCP OFFER - El servidor DHCP en la red responde con un mensaje de oferta. La oferta contiene un paquete con el tiempo de arrendamiento DHCP, máscara de subred, dirección IP, etc.
3. DHCP REQUEST - El cliente envía otra difusión para que todos los servidores DHCP sepan qué oferta aceptó.
4. DHCP ACK - El servidor envía un acuse de recibo.

DHCP es más complejo que esto, pero esta es la esencia.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del direccionamiento IP dinámico y la configuración de red:

1. **[Administrar el direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Practica el uso del comando `ip` para inspeccionar interfaces y, específicamente, usa `dhclient` para obtener una dirección IP dinámica, aplicando directamente tus conocimientos de DHCP.
2. **[Identificar direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Aprende a usar el comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones IP asignadas por DHCP, e inspeccionar interfaces de red.
3. **[Explorar tipos de direcciones IP y accesibilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explora el direccionamiento IP y la accesibilidad de la red usando `ping` e `ip a`, lo que te ayudará a comprender cómo funcionan las IP asignadas dinámicamente dentro de una red.

Estos laboratorios te ayudarán a aplicar los conceptos de asignación dinámica de IP y configuración de red en escenarios reales y a generar confianza con las redes Linux.

## Quiz Question

¿Cuáles son los pasos en una solicitud DHCP?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
