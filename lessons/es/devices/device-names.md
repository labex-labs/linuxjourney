---
index: 3
lang: "es"
title: "Nombres de Dispositivos"
meta_title: "Nombres de Dispositivos - Dispositivos"
meta_description: "Aprenda los nombres de dispositivos Linux como los dispositivos SCSI (sd), pseudo y PATA (hd). Entienda /dev/sda, /dev/null y más en esta guía para principiantes."
meta_keywords: "nombres de dispositivos Linux, /dev, dispositivos SCSI, pseudo dispositivos, dispositivos PATA, tutorial de Linux, Linux para principiantes, archivos de dispositivo"
---

## Lesson Content

Aquí están los nombres de dispositivos más comunes que encontrará:

### SCSI Devices

Si tiene algún tipo de almacenamiento masivo en su máquina, lo más probable es que esté utilizando el protocolo SCSI (pronunciado "scuzzy"). SCSI significa Small Computer System Interface; es un protocolo utilizado para permitir la comunicación entre discos, impresoras, escáneres y otros periféricos y su sistema. Es posible que haya oído hablar de los dispositivos SCSI, que en realidad no se utilizan en los sistemas modernos; sin embargo, nuestros sistemas Linux corresponden los discos SCSI con las unidades de disco duro en `/dev`. Se representan con un prefijo de `sd` (SCSI disk):

Archivos de dispositivo SCSI comunes:

- `/dev/sda` - Primer disco duro
- `/dev/sdb` - Segundo disco duro
- `/dev/sda3` - Tercera partición en el primer disco duro

### Pseudo Devices

Como discutimos anteriormente, los pseudo dispositivos no están realmente conectados físicamente a su sistema. La mayoría de los pseudo dispositivos comunes son dispositivos de caracteres:

- `/dev/zero` - acepta y descarta toda la entrada, produce un flujo continuo de bytes NULL (valor cero)
- `/dev/null` - acepta y descarta toda la entrada, no produce salida
- `/dev/random` - produce números aleatorios

### PATA Devices

A veces, en sistemas más antiguos, puede ver discos duros a los que se hace referencia con un prefijo `hd`:

- `/dev/hda` - Primer disco duro
- `/dev/hdd2` - Segunda partición en el cuarto disco duro

## Exercise

Escriba en los pseudo dispositivos y vea qué sucede. ¡Tenga cuidado de no escribir sus discos en esos dispositivos!

## Quiz Question

¿Cuál sería comúnmente el nombre del dispositivo para la primera partición en el segundo disco SCSI?

## Quiz Answer

sdb1
