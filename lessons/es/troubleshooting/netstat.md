---
index: 4
lang: "es"
title: "netstat"
meta_title: "netstat - Solución de problemas"
meta_description: "Domina el comando netstat de Linux para analizar conexiones de red, puertos y sockets. Esta guía cubre estados comunes como SYN_SENT y netstat close_wait para una solución de problemas efectiva."
meta_keywords: "netstat linux, netstat, comando netstat, netstat syn_sent, netstat close_wait, conexiones de red, redes linux, análisis de red, tutorial linux"
---

## Lesson Content

### Puertos Bien Conocidos

Hemos discutido cómo se transmiten los datos a través de puertos en nuestra máquina. Echemos un vistazo a algunos puertos comunes y bien conocidos. Puede encontrar una lista de estos puertos en el archivo **/etc/services**:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

La primera columna muestra el nombre del servicio, seguido de su número de puerto asignado y el protocolo de capa de transporte que utiliza.

### Introducción a netstat en Linux

Una herramienta extremadamente útil para recopilar información detallada de la red es **netstat**. El comando `linux netstat` muestra una amplia gama de datos relacionados con la red, incluidas conexiones de red activas, tablas de enrutamiento y estadísticas de interfaz. A menudo se le llama la navaja suiza de las herramientas de red.

Esta lección se centrará en usar `netstat` para verificar el estado de las conexiones de red. Antes de sumergirnos en un ejemplo, aclaremos la diferencia entre sockets y puertos. Un **puerto** es un identificador numérico utilizado para dirigir los datos a una aplicación específica. Un **socket** es un punto final para la comunicación, que permite a los programas enviar y recibir datos. La dirección del socket es la combinación única de una dirección IP y un número de puerto. Cada conexión entre un host y un destino requiere un socket único. Por ejemplo, aunque el servicio HTTP se ejecuta en el puerto 80, pueden existir múltiples conexiones HTTP simultáneamente, y se crea un socket único para cada una.

Examinemos la salida de `netstat -at`:

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

El comando `netstat -a` muestra todos los sockets en escucha y no en escucha, mientras que el indicador `-t` filtra la salida para mostrar solo las conexiones TCP.

Las columnas son las siguientes:

- **Proto**: El protocolo utilizado (ej. TCP o UDP).
- **Recv-Q**: La cola de datos esperando ser recibidos.
- **Send-Q**: La cola de datos esperando ser enviados.
- **Local Address**: La dirección del host local.
- **Foreign Address**: La dirección del host remoto.
- **State**: El estado actual del socket.

### Comprensión de los Estados de Conexión

La columna **State** (Estado) proporciona información crucial sobre el estado de una conexión. Aquí hay algunos estados comunes que encontrará:

- **LISTENING**: El socket está esperando conexiones entrantes. Para que se realice una conexión TCP, el destino debe estar escuchando.
- **SYN_SENT**: Cuando se utiliza `netstat`, un estado `SYN_SENT` indica que el socket está intentando activamente establecer una conexión.
- **ESTABLISHED**: El socket tiene una conexión completamente establecida.
- **CLOSE_WAIT**: El estado `netstat close_wait` significa que el host remoto se ha desconectado y el sistema local está esperando que la aplicación cierre el socket.
- **TIME_WAIT**: El socket está esperando después de cerrarse para manejar cualquier paquete que aún pueda estar en la red.

Puede ver una lista completa de los estados de socket en la página de manual de `netstat`.

## Exercise

¡La práctica hace al maestro! Aquí hay un laboratorio práctico para reforzar su comprensión de la configuración de la interfaz de red:

1. **[Examinar la configuración de la interfaz de red con ethtool en Linux](https://labex.io/es/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Aprenda a usar el comando `ethtool` para examinar y administrar la configuración de la interfaz de red, incluida la visualización y configuración de la velocidad y dúplex de la interfaz, y el análisis de los modos de enlace para solucionar problemas de red de capa física.

Este laboratorio le ayudará a aplicar los conceptos en escenarios reales y a ganar confianza en la administración de interfaces de red.

## Quiz Question

¿Qué puerto se utiliza para HTTPS?

## Quiz Answer

443
