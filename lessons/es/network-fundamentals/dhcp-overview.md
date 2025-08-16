---
title: "Visión general de DHCP"
description: "Aprende sobre DHCP (Dynamic Host Configuration Protocol) en Linux. Comprende cómo DHCP asigna direcciones IP y su proceso de cuatro pasos. ¡Comienza tu viaje en redes Linux!"
keywords: "DHCP, Dynamic Host Configuration Protocol, redes Linux, dirección IP, tutorial DHCP, principiante, guía"
---

## Lesson Content

Un concepto de red importante que aún no hemos revisado es DHCP (Dynamic Host Configuration Protocol).

DHCP asigna direcciones IP, máscaras de subred y puertas de enlace a nuestras máquinas. Por ejemplo, digamos que tienes un teléfono celular y quieres obtener un número de teléfono celular para empezar a hablar con la gente. Tienes que llamar a tu operador de telefonía, y ellos te darán un número. Mientras pagues tus facturas, puedes seguir usando tu teléfono. DHCP es el operador de telefonía en este caso; te da una dirección IP para que puedas hablar con otras direcciones IP. También se te arrienda una dirección IP; estas duran un cierto período de tiempo, luego se renovarán dependiendo de cómo tengas configurados tus ajustes de arrendamiento.

DHCP es excelente por muchas razones: permite que un administrador de red no se preocupe por asignar direcciones IP, y también evita que configuren direcciones IP duplicadas. Cada red física debe tener su propio servidor DHCP para que un host pueda solicitar una dirección IP. En un entorno doméstico regular, el enrutador suele actuar como el servidor DHCP.

La forma en que DHCP obtiene toda la información de tu host dinámico es:

1. DHCP DISCOVER - Este mensaje se transmite para buscar un servidor DHCP.
2. DHCP OFFER - El servidor DHCP en la red responde con un mensaje de oferta. La oferta contiene un paquete con el tiempo de arrendamiento DHCP, la máscara de subred, la dirección IP, etc.
3. DHCP REQUEST - El cliente envía otra transmisión para que todos los servidores DHCP sepan qué oferta aceptó.
4. DHCP ACK - El servidor envía un acuse de recibo.

DHCP es más complejo que esto, pero esta es la esencia.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuáles son los pasos en una solicitud DHCP?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
