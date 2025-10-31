---
index: 2
lang: "es"
title: "Tabla de Enrutamiento"
meta_title: "Tabla de Enrutamiento - Enrutamiento"
meta_description: "Una guía para entender la tabla de enrutamiento de Linux. Aprenda a interpretar la salida del comando route, incluyendo destino, puerta de enlace, genmask e interfaz eth0. Domine los conceptos básicos de su tabla de rutas de Linux."
meta_keywords: "tabla de enrutamiento linux, tabla de rutas linux, genmask, eth0, comando route, enrutamiento de red, enrutamiento IP, destino, puerta de enlace, máscara de subred, redes linux"
---

## Lesson Content

La **tabla de enrutamiento de Linux** contiene las reglas que determinan a dónde se envían los paquetes de red. Cada vez que su sistema necesita enviar un paquete a una dirección IP, consulta esta tabla para encontrar la ruta apropiada. Para ver la **tabla de rutas de Linux** de su máquina, puede usar el comando `route`.

```plaintext
pete@icebox:~$ sudo route -n
Tabla de enrutamiento IP del kernel
Destino     Puerta de enlace Genmask         Flags Métrica Ref    Uso Interfaz
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Entendiendo las Columnas

La salida del comando `route` se organiza en varias columnas, cada una proporcionando información específica sobre una ruta de red.

### Destino

La columna Destino especifica una red o un host. La entrada `192.168.224.0` dirige todos los paquetes destinados a esa red específica. Si el destino de un paquete está dentro de esta red (por ejemplo, de 192.168.224.5 a 192.168.224.7), se envía directamente a través de la interfaz especificada, como `eth0`.

El destino `0.0.0.0` es la ruta predeterminada. Si la tabla de enrutamiento no tiene una entrada más específica para el destino de un paquete, utiliza esta ruta.

### Puerta de enlace (Gateway)

La columna Puerta de enlace muestra el enrutador al que se envían los paquetes. Si un paquete no está en la misma red local, se reenvía a esta dirección de puerta de enlace. Para la ruta predeterminada, esta es la dirección IP del enrutador que conecta su red local con otras redes, como Internet.

### Genmask

El `genmask`, o máscara de generación, es la máscara de subred para la red de destino. Se utiliza junto con la IP de destino para determinar si un paquete pertenece a esa red. Por ejemplo, un `genmask` de `255.255.255.0` significa que los primeros tres octetos de la dirección IP deben coincidir con los primeros tres octetos del destino.

### Flags (Indicadores)

Estos indicadores proporcionan información adicional sobre la ruta:

- **U**: Indica que la ruta está activa y en funcionamiento.
- **G**: Significa que la ruta es hacia una puerta de enlace (enrutador).
- **UG**: Significa que la ruta está activa y apunta a una puerta de enlace.

### Iface (Interfaz)

Esta columna indica la interfaz de red, como `eth0`, a través de la cual se enviarán los paquetes para esta ruta. `eth0` generalmente representa el primer adaptador Ethernet en su sistema.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del enrutamiento de red y el direccionamiento IP:

1. **[Identificar Direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practique el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas direcciones IP e interfaces de red, que son componentes clave de una tabla de enrutamiento.
2. **[Administrar el Direccionamiento IP en Linux](https://labex.io/es/labs/comptia-manage-ip-addressing-in-linux-592736)** - Aprenda a administrar el direccionamiento IP, configurar IPs estáticas, establecer puertas de enlace predeterminadas y verificar configuraciones de red, lo que se relaciona directamente con las entradas que se encuentran en una tabla de enrutamiento.
3. **[Explorar Tipos de Direcciones IP y Alcanzabilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Explore el direccionamiento IP y la alcanzabilidad de la red usando `ping` e `ip a`, lo que le ayudará a comprender cómo interactúan los diferentes tipos de IP y cómo se determina la alcanzabilidad de la red, lo cual se refleja en las decisiones de enrutamiento.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la configuración y solución de problemas de red.

## Quiz Question

Si no se encuentra un destino en la tabla de enrutamiento, ¿a dónde se envían los paquetes? Por favor, responda con una sola palabra en inglés, prestando atención a la capitalización.

## Quiz Answer

Gateway
