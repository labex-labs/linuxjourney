---
index: 1
lang: "es"
title: "¿Qué es DNS?"
meta_title: "¿Qué es DNS? - DNS"
meta_description: "Aprende qué es DNS y cómo traduce nombres de dominio a direcciones IP. Comprende este concepto central de Internet con nuestra guía de Linux para principiantes."
meta_keywords: "DNS, Sistema de Nombres de Dominio, dirección IP, nombre de host, redes Linux, principiante, tutorial, guía"
---

## Lesson Content

Imagina que cada vez que quisieras buscar algo en Google tuvieras que escribir `http://192.78.12.4` en lugar de `www.google.com`. Bueno, sin DNS ("Domain Name System"), eso es exactamente lo que pasaría. Las redes de bajo nivel solo entienden la dirección IP sin procesar para identificar un host. DNS nos permite a los humanos llevar un registro de sitios web y hosts por nombre en lugar de una dirección IP. Es como una lista de contactos para Internet. Si conoces el nombre de alguien pero no sabes su número de teléfono, simplemente puedes buscarlo en tu lista de contactos.

DNS es fundamentalmente una base de datos distribuida de nombres de host a direcciones IP. Nosotros gestionamos nuestra base de datos para que la gente sepa cómo llegar a nuestro sitio/dominio, y en otro lugar otra persona está gestionando su base de datos para que otros puedan llegar a su dominio. Estos dominios pueden entonces comunicarse entre sí y construir una lista de contactos masiva de Internet.

En este curso, repasaremos algunos conceptos básicos de DNS, pero ten en cuenta que DNS es un tema exhaustivo, y si realmente quieres profundizar en él, necesitarás investigar más.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de DNS y la resolución de nombres de host:

1. **[Consultar registros DNS en Linux con dig y nslookup](https://labex.io/es/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - Aprende a usar herramientas esenciales de Linux como `dig` y `nslookup` para consultar varios tipos de registros DNS, lo que te ayudará a comprender cómo se resuelven los nombres de host en direcciones IP.
2. **[Administrar la resolución local de nombres de host en Linux](https://labex.io/es/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - Practica la edición del archivo `/etc/hosts` para administrar la resolución local de nombres de host, una habilidad fundamental para controlar cómo tu sistema Linux resuelve nombres sin depender de servidores DNS externos.
3. **[Configurar un servidor DNS autoritativo local en Linux](https://labex.io/es/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - Adquiere experiencia práctica configurando tu propio servidor DNS autoritativo local usando `bind9`, lo que te permitirá profundizar en cómo se gestionan las zonas y los registros DNS.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con DNS y la resolución de nombres de host en un entorno Linux.

## Quiz Question

Verdadero o falso: ¿DNS nos ayuda a encontrar direcciones MAC para nombres de host?

## Quiz Answer

False
