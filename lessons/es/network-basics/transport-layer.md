---
index: 6
lang: "es"
title: "Capa de Transporte"
meta_title: "Capa de Transporte - Fundamentos de Red"
meta_description: "Explore la Capa de Transporte en redes Linux. Esta lección cubre protocolos clave como TCP y UDP, la función de los puertos de red, segmentación de datos y el handshake TCP para transferencia fiable."
meta_keywords: "Capa de Transporte Linux, TCP, UDP, handshake TCP, puertos de red, segmentación de datos, redes Linux, protocolos de red, transferencia de datos fiable"
---

## Lesson Content

La capa de transporte es una parte fundamental de la red de Linux responsable de la comunicación de extremo a extremo y la transferencia fiable de datos entre aplicaciones en diferentes hosts. Prepara los datos para su transporte a través de la red de una manera estructurada y manejable.

### Segmentación de Datos

Una de las funciones principales de la capa de transporte es la segmentación de datos. Descompone grandes cantidades de datos en fragmentos más pequeños y manejables llamados segmentos. Este proceso hace que la transferencia de datos sea más eficiente y resiliente. Si se pierde o corrompe un segmento durante la transmisión, solo ese pequeño trozo necesita ser reenviado, no todo el conjunto de datos. Una vez que los segmentos llegan a su destino, la capa de transporte los vuelve a ensamblar en el orden correcto.

### Comprensión de los Puertos de Red

Mientras que las direcciones IP identifican el host correcto en una red, no especifican qué aplicación o servicio debe recibir los datos. Aquí es donde entran en juego los puertos de red. Servicios como HTTP (tráfico web) o SMTP (correo electrónico) escuchan en puertos específicos y bien conocidos. Por ejemplo, HTTP utiliza típicamente el puerto 80. La capa de transporte adjunta números de puerto de origen y destino a cada segmento, asegurando que los datos se entreguen al proceso correcto en el host receptor.

### Protocolos Centrales de Transporte TCP y UDP

Hay dos protocolos de transporte principales utilizados en las redes modernas: TCP (Protocolo de Control de Transmisión) y UDP (Protocolo de Datagramas de Usuario). Cubriremos brevemente UDP y luego nos centraremos en TCP, ya que es el más utilizado para la comunicación fiable.

### UDP (Protocolo de Datagramas de Usuario)

UDP es un protocolo sin conexión que ofrece un método rápido pero no fiable para transportar datos. No garantiza que todos los segmentos lleguen o que lleguen en el orden correcto. Aunque esto pueda parecer una desventaja, UDP es muy eficaz para aplicaciones donde la velocidad es más crítica que la precisión perfecta, como la transmisión de video en vivo o los juegos en línea. Perder algunos fotogramas de video es a menudo una compensación aceptable para una transmisión más fluida y rápida.

### TCP (Protocolo de Control de Transmisión)

TCP proporciona un flujo de datos fiable y orientado a la conexión. Antes de que se intercambien datos, TCP establece una conexión formal entre los dos hosts para asegurar que ambos estén listos para comunicarse.

### El Handshake TCP

Para establecer una conexión, TCP utiliza un proceso llamado handshake de tres vías:

1. **SYN**: El cliente envía un segmento SYN (sincronizar) al servidor para iniciar una conexión.
2. **SYN-ACK**: El servidor responde con un segmento SYN-ACK (sincronizar-confirmar) para acusar recibo de la solicitud del cliente.
3. **ACK**: El cliente envía un segmento ACK (confirmar) de vuelta al servidor, confirmando que la conexión está establecida.

Una vez completado el handshake, los datos pueden intercambiarse de forma fiable. TCP utiliza números de secuencia para rastrear cada segmento, lo que permite al host receptor volver a ensamblarlos en el orden correcto y solicitar la retransmisión de cualquier segmento faltante. En nuestro ejemplo de correo electrónico, la capa de transporte adjuntaría el puerto de destino para SMTP (puerto 25) y un puerto de origen del host cliente a cada segmento.

## Exercise

Si bien no hay laboratorios específicos para este tema, recomendamos explorar la ruta de aprendizaje integral de Linux [Linux Learning Path](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

What is a reliable transport protocol? (Your answer should be in English and is case-sensitive).

## Quiz Answer

TCP
