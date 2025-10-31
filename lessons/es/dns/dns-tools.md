---
index: 6
lang: "es"
title: "Herramientas DNS"
meta_title: "Herramientas DNS - DNS"
meta_description: "Explore herramientas DNS esenciales de Linux como nslookup y el potente comando dig. Este tutorial de Linux para principiantes cubre consultas DNS y técnicas de solución de problemas DNS."
meta_keywords: "nslookup, comando dig, herramientas DNS, DNS Linux, solución de problemas DNS, búsqueda de servidor de nombres, tutorial Linux, Linux para principiantes"
---

## Lesson Content

En Linux, hay varias utilidades de línea de comandos disponibles para el diagnóstico de redes. Cuando se trata de problemas del Sistema de Nombres de Dominio (DNS), dos **herramientas DNS** principales destacan: `nslookup` y `dig`. Comprender cómo usarlas es crucial para cualquier **resolución de problemas DNS** en un servidor o cliente **DNS de Linux**.

### Uso de nslookup para consultas DNS básicas

La herramienta `nslookup` (búsqueda de servidor de nombres) es una utilidad clásica para consultar servidores DNS y obtener información de mapeo de nombres de dominio o direcciones IP. Aunque a veces se considera obsoleta en favor de `dig`, sigue siendo una herramienta rápida y sencilla para búsquedas simples.

Para encontrar la dirección IP de un dominio como `www.google.com`, puede ejecutar:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

En esta salida, `Server` y `Address` muestran el servidor DNS que respondió a la consulta. La `Non-authoritative answer` (Respuesta no autoritativa) significa que el servidor proporcionó un resultado en caché en lugar de consultar directamente la fuente autoritativa. `Name` y `Address` muestran la dirección IP resuelta para el dominio.

### Resolución avanzada de problemas DNS con dig

El comando `dig` (domain information groper) es una herramienta potente y flexible para interrogar servidores de nombres DNS. Proporciona información más detallada que `nslookup`, lo que lo convierte en la opción preferida para una **resolución de problemas DNS** seria.

Aquí hay un ejemplo de uso del **comando dig**:

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

La salida de `dig` está organizada en secciones:

- **QUESTION SECTION** (Sección de pregunta): Muestra la consulta que se envió. Aquí, solicitamos un registro `A` (dirección) para `www.google.com`.
- **ANSWER SECTION** (Sección de respuesta): Muestra la respuesta recibida del servidor DNS. En este caso, Google tiene varias direcciones IP asociadas con su dominio.
- **Statistics** (Estadísticas): La sección final proporciona metadatos sobre la consulta, como el tiempo de consulta y el servidor que respondió.

Debido a su salida detallada y flexibilidad, `dig` es una utilidad indispensable para cualquiera que administre o solucione problemas de servicios de red en Linux.

## Exercise

Para adquirir más experiencia con las utilidades de red de Linux, considere probar el siguiente laboratorio práctico:

1. **[Examine Network Interface Settings with ethtool in Linux](https://labex.io/es/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Aprenda a usar el comando `ethtool` para examinar y administrar la configuración de la interfaz de red, incluida la visualización y configuración de la velocidad y dúplex de la interfaz, y el análisis de los modos de enlace para solucionar problemas de red de capa física.

Este laboratorio le ayudará a aplicar los conceptos en escenarios reales y a ganar confianza en la administración de interfaces de red.

## Quiz Question

¿Qué herramienta se utiliza para obtener información detallada sobre los servidores de nombres DNS? Por favor, responda usando solo caracteres ingleses en minúsculas.

## Quiz Answer

dig
