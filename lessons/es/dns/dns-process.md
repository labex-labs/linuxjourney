---
title: "Proceso DNS"
description: "Aprenda cómo funciona DNS paso a paso, desde los servidores raíz hasta el DNS autoritativo. Comprenda el proceso de búsqueda de DNS para usuarios principiantes e intermedios."
keywords: "proceso DNS, búsqueda DNS, cómo funciona DNS, tutorial DNS, DNS para principiantes, DNS en Linux, TLD, servidores raíz"
---

## Lesson Content

Veamos un ejemplo de cómo su host encuentra un dominio (catzontheinterwebz.com) con DNS. Esencialmente, nos abrimos paso hasta llegar al servidor DNS que conoce ese dominio.

### Local DNS Server

Primero, nuestro host pregunta: "¿Dónde está catzontheinterwebz.com?" Nuestro servidor DNS local no lo sabe, así que va y comienza desde la parte superior del embudo para preguntar a los Root Servers. Tenga en cuenta que nuestro host no está haciendo estas solicitudes para encontrar catzontheinterwebz.com directamente; la mayoría de los usuarios hablan con un servidor DNS recursivo proporcionado por sus ISP, y ese servidor se encarga de encontrar la ubicación de catzontheinterwebz.com.

### Root Servers

Hay 13 Root Servers para Internet. Están replicados y distribuidos por todo el mundo para manejar las solicitudes DNS de Internet, por lo que en realidad hay cientos de servidores funcionando. Son controlados por diferentes organizaciones y contienen información sobre Top-Level Domains. Los Top-level domains son lo que usted conoce como direcciones .org, .com, .net, etc. Así que el Root Server no sabe dónde está catzontheinterwebz.com, pero nos dice que preguntemos al DNS Server del Top-Level Domain .com en una dirección IP que nos proporciona.

### Top-Level Domain

Así que ahora enviamos otra solicitud al name server que conoce las direcciones ".com" y le preguntamos si sabe dónde está catzontheinterwebz.com. El TLD no tiene catzontheinterwebz.com en sus zone files, pero sí ve un registro para el name server de catzontheinterwebz.com. Así que nos da la dirección IP de ese name server y nos dice que busquemos allí.

### Authoritative DNS Server

Ahora enviamos una solicitud final al DNS server que realmente tiene el registro que queremos. El name server ve que tiene un zone file para catzontheinterwebz.com, y hay un resource record para 'www' para este host. Luego nos da la dirección IP de este host, y finalmente podemos ver algunos gatos en Internet.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cuál es la abreviatura de los nameservers donde se encuentran las direcciones .com, .net, .org, etc.?

## Quiz Answer

TLD
