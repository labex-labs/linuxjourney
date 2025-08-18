---
index: 3
lang: "es"
title: "dhclient"
meta_title: "dhclient - Configuración de Red"
meta_description: "Aprenda sobre dhclient, cómo obtiene direcciones IP usando DHCP y gestiona las concesiones de red. Comprenda los archivos dhclient.conf y dhclient.leases. Guía para principiantes de Linux."
meta_keywords: "dhclient, DHCP, redes Linux, dirección IP, configuración de red, tutorial de Linux, guía para principiantes"
---

## Lesson Content

Hemos hablado de DHCP antes, y la mayoría de las veces nunca necesitará configurar estáticamente sus direcciones IP, máscaras de subred, etc. En su lugar, ¡usará DHCP! El `dhclient` se inicia al arrancar y obtiene una lista de interfaces de red del archivo `dhclient.conf`. Para cada interfaz listada, intenta configurar la interfaz usando el protocolo DHCP.

En el archivo `dhclient.leases`, `dhclient` mantiene un registro de una lista de concesiones a través de los reinicios del sistema. Después de leer `dhclient.conf`, se lee el archivo `dhclient.leases` para informarle qué concesiones ya ha asignado.

### Para obtener una IP nueva

```bash
sudo dhclient
```

## Exercise

No hay ejercicios para esta lección.

## Quiz Question

¿Qué intenta asignar direcciones IP con el protocolo DHCP?

## Quiz Answer

dhclient
