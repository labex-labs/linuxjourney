---
index: 2
lang: "es"
title: "Subredes"
meta_title: "Subredes - Subneteo"
meta_description: "Domina los fundamentos de la subred y máscara de subred en Linux. Esta guía explica el subneteo de subredes, prefijos de red y cómo gestionar la segmentación de red en un entorno Linux de subredes."
meta_keywords: "subnet linux, subred linux, máscara de subred linux, subneteo de subredes, subredes, máscara de subred, prefijo de red, redes Linux, dirección IP"
---

## Lesson Content

¿Cómo puedes saber si dos computadoras están en la misma red? La respuesta radica en comprender la subred, abreviatura de sub-red. Una subred es una división lógica de una red IP, que agrupa hosts con direcciones IP similares. Estos hosts suelen estar en proximidad física cercana, lo que permite una transferencia de datos eficiente entre ellos. Piénsalo como enviar correo dentro del mismo código postal; es mucho más rápido y sencillo que enviarlo a un estado diferente.

Para que un host forme parte de una **subred linux**, su dirección IP se divide en dos partes: un prefijo de red y un identificador de host. Por ejemplo, si un host tiene una IP de 192.168.1.8 y otro tiene 192.168.1.9, es probable que compartan el mismo prefijo de red. La parte común identifica la red, mientras que los números únicos (8 y 9) identifican a los hosts individuales.

### Comprensión de la Máscara de Subred de Linux

Una **máscara de subred linux** es lo que determina qué parte de una dirección IP es la porción de red y cuál es la porción de host. Una máscara de subred típica se ve así:

```plaintext
255.255.255.0
```

Para entender esto, necesitamos pensar en binario. Cada número en una dirección IP o máscara de subred es un octeto, que representa 8 bits. En binario, un `1` significa "encendido" y un `0` significa "apagado". Si conviertes el número binario `11111111` a decimal, obtienes 255. Esto significa que un octeto puede variar de 0 (`00000000`) a 255 (`11111111`).

Los `255` en la máscara "enmascaran" la porción de red de la dirección IP. Por lo tanto, con una máscara de `255.255.255.0` y una IP de `192.168.1.8`, la parte `192.168.1` es la red, y `8` es el host. A menudo denotamos una configuración de **subred linux** por su prefijo de red seguido de la máscara de subred, como `192.168.1.0/255.255.255.0`.

### El Propósito de Subnetting Subnets

¿Por qué creamos subredes? La práctica de **subnetting subnets** (subredes de subredes) es crucial para organizar y administrar redes de manera efectiva. Implica dividir una red más grande en segmentos más pequeños y manejables. Esto ofrece varios beneficios clave:

- **Rendimiento Mejorado:** Al segmentar una red, reduces el volumen de tráfico de difusión dentro de cada subred, lo que conduce a menos congestión y un mejor rendimiento general.
- **Seguridad Mejorada:** Las subredes te permiten aislar diferentes partes de tu red. Un host en una subred no puede interactuar directamente con un host en otra sin un enrutador, creando un límite de seguridad. Puedes implementar reglas de acceso en el enrutador para controlar el flujo de tráfico entre subredes.
- **Administración Simplificada:** Dividir una red grande en unidades lógicas más pequeñas facilita la administración, la solución de problemas y la aplicación de políticas de red.

### Conexión de Subredes

¿Qué pasa si necesitas conectarte a hosts en una red diferente, como yahoo.com? Para conectar diferentes subredes, necesitas un dispositivo que esté conectado a más de una subred: un enrutador.

Por ejemplo, un host en `192.168.1.129` en una red con una máscara `255.255.255.0` puede alcanzar cualquier otro host en la red `192.168.1.0`. Para llegar a Internet, debe enviar tráfico a través de su puerta de enlace, que es el enrutador. En muchas redes domésticas, la dirección del enrutador suele ser `.1` de la subred (por ejemplo, `192.168.1.1`). Este enrutador tiene otra conexión a una subred diferente (como la red de tu ISP), lo que permite la comunicación con el resto de Internet.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión del direccionamiento IP y el subnetting:

1. **[Identificar Direcciones MAC e IP en Linux](https://labex.io/es/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - Practica el uso del comando `ip a` para identificar información de direccionamiento de red, incluidas las direcciones IPv4, lo cual es fundamental para comprender las subredes.
2. **[Explorar Tipos de Direcciones IP y Alcanzabilidad en Linux](https://labex.io/es/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - Aprende a explorar diferentes tipos de direcciones IP y a probar la alcanzabilidad de la red, lo que te ayudará a verificar si los hosts están en la misma red.
3. **[Realizar Subnetting IP y Conversión Binaria en la Terminal de Linux](https://labex.io/es/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Domina el subnetting IP y la conversión binaria, aplicando directamente los conceptos de prefijo de red e identificación de host discutidos en la lección.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con el direccionamiento de red y el subnetting.

## Quiz Question

Una subred se define por un prefijo de red y una máscara de subred. ¿Verdadero o Falso? (Por favor, responda con 'True' o 'False'. La respuesta distingue entre mayúsculas y minúsculas y debe estar en inglés.)

## Quiz Answer

True
