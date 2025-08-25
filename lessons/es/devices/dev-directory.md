---
index: 1
lang: "es"
title: "Directorio /dev"
meta_title: "/dev directory - Dispositivos"
meta_description: "Aprende sobre el directorio /dev en Linux, donde se almacenan los archivos de dispositivo. Comprende los nodos de dispositivo y cómo interactuar con ellos. Explora /dev con ls. Guía para principiantes de Linux."
meta_keywords: "directorio /dev, archivos de dispositivo Linux, nodos de dispositivo, tutorial Linux, ls /dev, Linux para principiantes, guía Linux"
---

## Lesson Content

Cuando conectas un dispositivo a tu máquina, generalmente necesita un controlador de dispositivo para funcionar correctamente. Puedes interactuar con los controladores de dispositivo a través de archivos de dispositivo o nodos de dispositivo; estos son archivos especiales que se parecen a los archivos regulares. Dado que estos archivos de dispositivo son como archivos regulares, puedes usar programas como `ls`, `cat`, etc., para interactuar con ellos. Estos archivos de dispositivo generalmente se almacenan en el directorio `/dev`. Adelante, ejecuta `ls` en el directorio `/dev` de tu sistema; verás una gran cantidad de archivos de dispositivo que están en tu sistema.

```bash
ls /dev
```

Algunos de estos dispositivos ya los has usado e interactuado con ellos, como `/dev/null`. Recuerda que cuando enviamos la salida a `/dev/null`, el kernel sabe que este dispositivo toma toda nuestra entrada y simplemente la descarta, por lo que no se devuelve nada.

Antiguamente, si querías añadir un dispositivo a tu sistema, añadías el archivo de dispositivo en `/dev` y luego probablemente te olvidabas de él. Bueno, repite eso un par de veces, y puedes ver dónde había un problema. El directorio `/dev` se llenaría de archivos de dispositivo estáticos de dispositivos que hace mucho tiempo que actualizaste, dejaste de usar, etc. Los dispositivos también se asignan a archivos de dispositivo en el orden en que el kernel los encuentra. Así, si cada vez que reiniciabas tu sistema, los dispositivos podían tener diferentes archivos de dispositivo dependiendo de cuándo fueron descubiertos.

Afortunadamente, ya no usamos ese método. Ahora tenemos algo que usamos para añadir y eliminar dinámicamente los dispositivos que se están utilizando actualmente en el sistema, y lo discutiremos en las próximas lecciones.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los dispositivos de hardware y su interacción con el sistema Linux:

1. **[Explorar dispositivos de hardware en Linux](https://labex.io/es/labs/comptia-explore-hardware-devices-in-linux-590861)** - En este laboratorio, aprenderás las habilidades esenciales para explorar, identificar e inspeccionar dispositivos de hardware dentro de un entorno Linux. Obtendrás experiencia práctica con potentes utilidades de línea de comandos para comprender cómo el sistema operativo interactúa con los componentes físicos.

Este laboratorio te ayudará a aplicar los conceptos de interacción con dispositivos en escenarios reales y a generar confianza en la gestión de hardware en Linux.

## Quiz Question

¿Dónde se almacenan los archivos de dispositivo en el sistema?

## Quiz Answer

/dev
