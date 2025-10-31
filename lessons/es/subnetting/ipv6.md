---
index: 7
lang: "es"
title: "IPv6"
meta_title: "IPv6 - Subnetting"
meta_description: "Guía para principiantes sobre el protocolo IPv6. Aprenda por qué se creó IPv6, cómo difiere de IPv4 y comprenda los conceptos básicos de su esquema de direccionamiento para redes Linux modernas."
meta_keywords: "IPv6, IPv4, dirección IP, redes Linux, protocolos de red, protocolo de internet, agotamiento de direcciones, principiante, tutorial, guía"
---

## Lesson Content

Cada dispositivo que se conecta a Internet, desde su servidor hasta su teléfono inteligente, requiere una dirección IP única para comunicarse. La versión más utilizada, IPv4, proporciona un número finito de direcciones, un límite al que nos acercamos rápidamente en nuestro mundo cada vez más conectado. Este problema se conoce como agotamiento de direcciones IPv4.

### ¿Qué es IPv6?

Para resolver este problema, el Grupo de Trabajo de Ingeniería de Internet (IETF) desarrolló una nueva versión del Protocolo de Internet: IPv6. El propósito principal de IPv6 es expandir drásticamente el grupo disponible de direcciones IP, asegurando que Internet pueda seguir creciendo y dar cabida a miles de millones de nuevos dispositivos. También incluye otras mejoras en el protocolo de red.

### IPv4 vs IPv6

Aunque IPv6 se creó para abordar las limitaciones de IPv4, su adopción ha sido gradual. No está destinado a reemplazar inmediatamente a IPv4. En cambio, los dos protocolos de red están diseñados para coexistir y complementarse. Muchas redes hoy en día funcionan en modo "pila dual" (dual-stack), soportando IPv4 e IPv6 simultáneamente. Si está familiarizado con IPv4, los conceptos centrales de IPv6 serán fáciles de captar.

### Entendiendo las Direcciones IPv6

La diferencia más significativa que notará es el formato de la dirección. Una dirección IPv4 es un número de 32 bits que generalmente se escribe como cuatro números decimales separados por puntos (ejemplo: `192.168.1.1`). En contraste, una dirección IPv6 es un número de 128 bits escrito en hexadecimal y separado por dos puntos.

Así es como se ve una dirección IPv6 típica:

```plaintext
2dde:1235:1256:3:200:f8ed:fe23:59cf
```

Este formato más largo permite un número mucho mayor de direcciones IP únicas, asegurando el futuro de la conectividad a Internet.

## Exercise

Para dominar los conceptos de IPv6, la práctica es esencial. Aquí hay algunos laboratorios prácticos para reforzar su comprensión del direccionamiento IPv6 y su interacción con IPv4 en un entorno Linux:

1. **[Configurar y Verificar Direcciones IPv6 en Linux](https://labex.io/es/labs/comptia-configure-and-verify-ipv6-addresses-in-linux-592858)** - Practique la asignación de direcciones IPv6 estáticas y pruebe la conectividad usando los comandos `ip` y `ping6`.
2. **[Realizar Consultas DNS IPv6 en Linux](https://labex.io/es/labs/comptia-perform-ipv6-dns-lookups-in-linux-592862)** - Aprenda a consultar registros AAAA y verifique la resolución DNS IPv6 usando `dig`, `nslookup` y `ping6`.
3. **[Configurar un Túnel 6to4 de IPv4 a IPv6 en Linux](https://labex.io/es/labs/comptia-configure-an-ipv4-to-ipv6-6to4-tunnel-in-linux-592867)** - Obtenga experiencia práctica configurando un túnel 6to4 para habilitar la conectividad IPv6 sobre una red IPv4 existente.

Estos laboratorios le ayudarán a aplicar los conceptos de IPv6 en escenarios reales y a ganar confianza con la configuración y solución de problemas de red.

## Quiz Question

What is the name of the IP protocol designed to increase the number of available addresses for hosts on the Internet? Please answer in English using the protocol's common name, paying attention to capitalization.

## Quiz Answer

IPv6
