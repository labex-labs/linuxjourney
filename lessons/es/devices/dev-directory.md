---
title: "directorio /dev"
description: "Aprende sobre el directorio /dev en Linux, donde se almacenan los archivos de dispositivo. Comprende los nodos de dispositivo y cómo interactuar con ellos. Explora /dev con ls. Guía para principiantes de Linux."
keywords: "directorio /dev, archivos de dispositivo Linux, nodos de dispositivo, tutorial de Linux, ls /dev, Linux para principiantes, guía de Linux"
---

## Lesson Content

Cuando conectas un dispositivo a tu máquina, generalmente necesita un controlador de dispositivo para funcionar correctamente. Puedes interactuar con los controladores de dispositivo a través de archivos de dispositivo o nodos de dispositivo; estos son archivos especiales que se parecen a los archivos regulares. Dado que estos archivos de dispositivo son como archivos regulares, puedes usar programas como `ls`, `cat`, etc., para interactuar con ellos. Estos archivos de dispositivo generalmente se almacenan en el directorio `/dev`. Adelante, haz un `ls` del directorio `/dev` en tu sistema; verás una gran cantidad de archivos de dispositivo que están en tu sistema.

```bash
ls /dev
```

Algunos de estos dispositivos ya los has usado e interactuado con ellos, como `/dev/null`. Recuerda cuando enviamos la salida a `/dev/null`, el kernel sabe que este dispositivo toma toda nuestra entrada y simplemente la descarta, por lo que no se devuelve nada.

Antiguamente, si querías añadir un dispositivo a tu sistema, añadías el archivo de dispositivo en `/dev` y luego probablemente te olvidabas de él. Bueno, repite eso un par de veces, y puedes ver dónde había un problema. El directorio `/dev` se llenaría de archivos de dispositivo estáticos de dispositivos que hace mucho tiempo actualizaste, dejaste de usar, etc. Los dispositivos también se asignan archivos de dispositivo en el orden en que el kernel los encuentra. Así, si cada vez que reiniciabas tu sistema, los dispositivos podían tener diferentes archivos de dispositivo dependiendo de cuándo fueron descubiertos.

Afortunadamente, ya no usamos ese método. Ahora tenemos algo que usamos para añadir y eliminar dinámicamente los dispositivos que se están utilizando actualmente en el sistema, y lo discutiremos en las próximas lecciones.

## Exercise

Revisa el contenido del directorio `/dev`. ¿Reconoces algún dispositivo familiar?

## Quiz Question

¿Dónde se almacenan los archivos de dispositivo en el sistema?

## Quiz Answer

/dev
