---
lang: "es"
title: "Análisis de Paquetes"
description: "Aprenda los conceptos básicos del análisis de paquetes usando tcpdump. Comprenda el tráfico de red, capture datos e interprete la salida con esta guía de Linux para principiantes."
keywords: "tcpdump, análisis de paquetes, análisis de red, redes Linux, tutorial para principiantes, Wireshark, comandos Linux, tráfico de red"
---

## Lesson Content

El tema del análisis de paquetes podría llenar un curso completo por sí solo, y hay muchos libros escritos solo sobre análisis de paquetes. Sin embargo, hoy solo aprenderemos lo básico. Hay dos analizadores de paquetes extremadamente populares: Wireshark y tcpdump. Estas herramientas escanean sus interfaces de red, capturan la actividad de los paquetes, los analizan y nos muestran la información. Nos permiten adentrarnos en los detalles del análisis de red y profundizar en los aspectos de bajo nivel. Usaremos tcpdump ya que tiene una interfaz más simple; sin embargo, si fuera a incorporar el análisis de paquetes a su conjunto de herramientas, le recomendaría investigar Wireshark.

### Install tcpdump

```bash
sudo apt install tcpdump
```

### Capture packet data on an interface

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
```

Notará muchas cosas sucediendo cuando ejecuta una captura de paquetes. Bueno, eso es de esperar; hay mucha actividad de red ocurriendo en segundo plano. En mi ejemplo anterior, he tomado solo un fragmento de mi captura, específicamente el momento en que decidí hacer ping a <www.google.com>.

### Understanding the output

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- El primer campo es una marca de tiempo de la actividad de red.
- IP: Esto contiene la información del protocolo.
- A continuación, verá la dirección de origen y destino: `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: Este es el número de secuencia inicial y final del paquete TCP.
- `length`: Longitud en bytes.

Como puede ver en nuestra salida de tcpdump, ¡estamos enviando un paquete ICMP echo request a <www.google.com> y recibiendo un paquete ICMP echo reply a cambio! Además, tenga en cuenta que diferentes paquetes mostrarán información diferente; consulte la página man para ver cuáles son.

### Writing tcpdump output to a file

```bash
sudo tcpdump -w /some/file
```

Algunas reflexiones finales: solo hemos arañado la superficie del tema del análisis de paquetes. Hay mucho que se puede analizar, y ni siquiera hemos tocado la posibilidad de profundizar aún más con la salida Hex y ASCII. Hay muchos recursos en línea para ayudarle a aprender más sobre los analizadores de paquetes, ¡y le insto a que los encuentre!

## Exercise

Descargue e instale la herramienta Wireshark y juegue con la interfaz.

## Quiz Question

¿Cuál es la bandera para capturar una interfaz específica con tcpdump?

## Quiz Answer

-i
