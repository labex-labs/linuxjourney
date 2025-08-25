---
index: 3
lang: "es"
title: "Proceso DNS"
meta_title: "Proceso DNS - DNS"
meta_description: "Aprenda cómo funciona DNS paso a paso, desde los servidores raíz hasta el DNS autorizado. Comprenda el proceso de búsqueda de DNS para usuarios principiantes e intermedios."
meta_keywords: "proceso DNS, búsqueda DNS, cómo funciona DNS, tutorial DNS, DNS para principiantes, DNS Linux, TLD, servidores raíz"
---

## Lesson Content

Veamos un ejemplo de cómo su host encuentra un dominio (catzontheinterwebz.com) con DNS. Esencialmente, nos abrimos camino hasta llegar al servidor DNS que conoce ese dominio.

### Servidor DNS Local

Primero, nuestro host pregunta: "¿Dónde está catzontheinterwebz.com?". Nuestro servidor DNS local no lo sabe, así que va y comienza desde la parte superior del embudo para preguntar a los Servidores Raíz. Tenga en cuenta que nuestro host no está haciendo estas solicitudes para encontrar catzontheinterwebz.com directamente; la mayoría de los usuarios hablan con un servidor DNS recursivo proporcionado por sus ISP, y ese servidor se encarga de encontrar la ubicación de catzontheinterwebz.com.

### Servidores Raíz

Hay 13 Servidores Raíz para Internet. Están replicados y distribuidos por todo el mundo para manejar las solicitudes DNS de Internet, por lo que en realidad hay cientos de servidores funcionando. Están controlados por diferentes organizaciones y contienen información sobre los Dominios de Nivel Superior. Los dominios de nivel superior son lo que usted conoce como direcciones .org, .com, .net, etc. Así que el Servidor Raíz no sabe dónde está catzontheinterwebz.com, pero nos dice que preguntemos al Servidor DNS de Dominio de Nivel Superior .com en una dirección IP que nos proporciona.

### Dominio de Nivel Superior

Así que ahora enviamos otra solicitud al servidor de nombres que conoce las direcciones ".com" y le preguntamos si sabe dónde está catzontheinterwebz.com. El TLD no tiene catzontheinterwebz.com en sus archivos de zona, pero sí ve un registro para el servidor de nombres de catzontheinterwebz.com. Así que nos da la dirección IP de ese servidor de nombres y nos dice que busquemos allí.

### Servidor DNS Autorizado

Ahora enviamos una solicitud final al servidor DNS que realmente tiene el registro que queremos. El servidor de nombres ve que tiene un archivo de zona para catzontheinterwebz.com, y hay un registro de recurso para 'www' para este host. Luego nos da la dirección IP de este host, y finalmente podemos ver algunos gatos en Internet.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la resolución y gestión de DNS:

1. **[Consultar Registros DNS en Linux con dig y nslookup](https://labex.io/es/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** - Aprenda a consultar registros DNS como A, PTR y MX, e identifique su servidor DNS predeterminado, esencial para la resolución de problemas de red.
2. **[Configurar un Servidor DNS Autorizado Local en Linux](https://labex.io/es/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** - Obtenga experiencia práctica instalando y configurando un servidor DNS autorizado local, definiendo zonas y probando la resolución DNS.
3. **[Administrar la Resolución de Nombres de Host Local en Linux](https://labex.io/es/labs/linux-manage-local-hostname-resolution-in-linux)** - Practique la administración de la resolución de nombres de host local editando el archivo `/etc/hosts`, una habilidad clave para el desarrollo web y las pruebas de red.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con DNS.

## Quiz Question

¿Cuál es la abreviatura de los servidores de nombres donde se encuentran las direcciones .com, .net, .org, etc.?

## Quiz Answer

TLD
