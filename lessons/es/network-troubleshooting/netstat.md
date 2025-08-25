---
index: 4
lang: "es"
title: "netstat"
meta_title: "netstat - Solución de problemas"
meta_description: "Aprende el comando netstat para el análisis de redes en Linux. Comprende las conexiones de red, puertos y sockets con esta guía para principiantes."
meta_keywords: "netstat, comando netstat, redes Linux, conexiones de red, tutorial Linux, principiante, guía"
---

## Lesson Content

### Puertos Conocidos

Hemos hablado de la transmisión de datos a través de puertos en nuestra máquina; veamos algunos puertos conocidos.

Puedes obtener una lista de puertos conocidos consultando el archivo **/etc/services**:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

La primera columna es el nombre del servicio, luego el número de puerto y el protocolo de capa de transporte que utiliza.

### netstat

Una herramienta extremadamente útil para obtener información detallada sobre tu red es **netstat**. Netstat muestra diversa información relacionada con la red, como conexiones de red, tablas de enrutamiento, información sobre interfaces de red y más; es la navaja suiza de las herramientas de red. Nos centraremos principalmente en una característica que tiene netstat, y es el estado de las conexiones de red. Antes de ver un ejemplo, hablemos primero de sockets y puertos. Un socket es una interfaz que permite a los programas enviar y recibir datos, mientras que un puerto se utiliza para identificar qué aplicación debe enviar o recibir datos. La dirección del socket es la combinación de la dirección IP y el puerto. Cada conexión entre un host y un destino requiere un socket único. Por ejemplo, HTTP es un servicio que se ejecuta en el puerto 80; sin embargo, podemos tener muchas conexiones HTTP, y para mantener cada conexión, se crea un socket por conexión.

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

El comando `netstat -a` muestra los sockets de escucha y no escucha para las conexiones de red; la bandera `-t` muestra solo las conexiones TCP.

Las columnas son las siguientes de izquierda a derecha:

- **Proto**: Protocolo utilizado, TCP o UDP.
- **Recv-Q**: Datos en cola para ser recibidos.
- **Send-Q**: Datos en cola para ser enviados.
- **Local Address**: Host conectado localmente.
- **Foreign Address**: Host conectado remotamente.
- **State**: El estado del socket.

Consulta la página del manual para obtener una lista de los estados de los sockets, pero aquí hay algunos:

- **LISTENING**: El socket está escuchando conexiones entrantes. Recuerda, cuando hacemos una conexión TCP, nuestro destino debe estar escuchando para que podamos conectarnos.
- **SYN_SENT**: El socket está intentando activamente establecer una conexión.
- **ESTABLISHED**: El socket tiene una conexión establecida.
- **CLOSE_WAIT**: El host remoto se ha cerrado y estamos esperando que el socket se cierre.
- **TIME_WAIT**: El socket está esperando después del cierre para manejar paquetes que aún están en la red.

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión de la configuración de la interfaz de red:

1. **[Examinar la configuración de la interfaz de red con ethtool en Linux](https://labex.io/es/labs/linux-examine-network-interface-settings-with-ethtool-in-linux-592759)** - Aprende a usar el comando `ethtool` para examinar y administrar la configuración de la interfaz de red, incluyendo la visualización y configuración de la velocidad y el dúplex de la interfaz, y el análisis de los modos de enlace para solucionar problemas de red de la capa física.

Este laboratorio te ayudará a aplicar los conceptos en escenarios reales y a desarrollar confianza en la gestión de interfaces de red.

## Quiz Question

¿Qué puerto se utiliza para HTTPS?

## Quiz Answer

443
