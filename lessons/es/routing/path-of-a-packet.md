---
index: 3
lang: "es"
title: "Ruta de un Paquete"
meta_title: "Ruta de un Paquete - Enrutamiento"
meta_description: "Explore la ruta completa de un paquete de datos que viaja dentro de una red local y a través de Internet. Aprenda cómo funcionan juntos las direcciones IP, direcciones MAC, ARP y tablas de enrutamiento para asegurar una comunicación de red exitosa en Linux."
meta_keywords: "ruta de paquete, comunicación de red, ARP, dirección IP, dirección MAC, tabla de enrutamiento, puerta de enlace predeterminada, redes Linux, viaje de paquete"
---

## Lesson Content

Comprender cómo viajan los datos a través de una red es fundamental para el networking. Este viaje, a menudo denominado **ruta del paquete**, implica un esfuerzo coordinado entre diferentes protocolos y hardware. Trazaremos la **ruta del paquete** en dos escenarios comunes: comunicación dentro de una red local y comunicación con una red externa.

### Ruta del Paquete Dentro de una Red Local

Cuando un dispositivo envía un paquete a otro dispositivo en la misma red local, el proceso es relativamente sencillo.

1. Primero, el host de envío comprueba si la dirección IP de destino está en la misma subred comparándola con su propia dirección IP y máscara de subred.
2. Para enviar un paquete, el host necesita cuatro piezas clave de información: una IP de origen, una IP de destino, una dirección MAC de origen y una dirección MAC de destino. Inicialmente, el host no conoce la dirección MAC del host de destino.
3. El host utiliza el Protocolo de Resolución de Direcciones (ARP) para encontrar la información faltante. Transmite una solicitud ARP en la red local, preguntando qué dispositivo tiene la dirección IP objetivo. El dispositivo correspondiente responde con su dirección MAC.
4. Con la dirección MAC de destino ya conocida, el paquete está completamente direccionado y puede enviarse directamente al host de destino en la red local.

### Ruta del Paquete a una Red Externa

Cuando un paquete está destinado a un dispositivo fuera de la red local, el proceso involucra routers para reenviar el paquete.

1. El host de envío determina que la dirección IP de destino no está en su red local. Dado que las transmisiones ARP se limitan a la red local, el host no puede descubrir directamente la dirección MAC del destino final.
2. El host consulta su tabla de enrutamiento. Como no hay una ruta específica para la IP externa, utiliza la ruta predeterminada, que apunta a la puerta de enlace predeterminada (un router). El paquete se prepara con las direcciones IP de origen y destino originales. Sin embargo, la dirección MAC de destino se establece en la dirección MAC de la puerta de enlace predeterminada. Si se desconoce la MAC de la puerta de enlace, el host utiliza ARP para encontrarla.
3. Una vez que el paquete llega al router, este examina la dirección IP de destino y consulta su propia tabla de enrutamiento para determinar el siguiente salto en la **ruta del paquete**. Luego, el router reescribe las direcciones MAC del paquete: la MAC de origen se convierte en la MAC del router y la MAC de destino se convierte en la MAC del siguiente salto. Este proceso se repite en cada router a lo largo del camino.
4. Cuando el paquete finalmente llega al router conectado a la red local de destino, ese router utiliza ARP para encontrar la dirección MAC del host final y entrega el paquete.
5. A lo largo de todo este viaje, las direcciones IP de origen y destino en la cabecera del paquete permanecen sin cambios. Solo las direcciones MAC se actualizan en cada salto.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión básica de archivos y directorios en Linux:

1. **[Operaciones Básicas de Archivos en Linux](https://labex.io/es/labs/linux-basic-file-operations-in-linux-18001)** - Practique la navegación por el sistema de archivos, la gestión de archivos y directorios, y el uso de atajos de línea de comandos en un entorno Linux real.
2. **[Operaciones de Archivos y Directorios](https://labex.io/es/labs/linux-file-and-directory-operations-17997)** - Aprenda a navegar por la estructura de directorios, administrar archivos y carpetas, y utilizar herramientas potentes de línea de comandos como `ls`, `cd`, `mkdir`, `cp`, `mv` y `rm`.
3. **[Organización de Archivos y Directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practique habilidades esenciales de gestión de archivos de Linux utilizando los comandos `cp`, `mv` y `rm` para organizar una estructura de proyecto, mover archivos y limpiar directorios innecesarios.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con las interacciones del sistema de archivos de Linux.

## Quiz Question

¿Qué protocolo se utiliza para encontrar la dirección MAC de un host en la red local, dada su dirección IP? Por favor, responda con el acrónimo de tres letras en mayúsculas.

## Quiz Answer

ARP
