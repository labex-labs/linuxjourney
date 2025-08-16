---
title: "tipos de dispositivos"
description: "Aprende sobre los tipos de dispositivos Linux (character, block, pipe, socket) y cómo identificarlos usando `ls -l /dev`. Comprende los números de dispositivo mayor/menor. Tutorial de Linux para principiantes."
keywords: "tipos de dispositivos Linux, ls -l /dev, dispositivo de carácter, dispositivo de bloque, número de dispositivo mayor menor, tutorial de Linux, guía de Linux, principiante"
---

## Lesson Content

Antes de hablar sobre cómo se gestionan los dispositivos, echemos un vistazo a algunos dispositivos.

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

Las columnas son las siguientes de izquierda a derecha:

- Permissions
- Owner
- Group
- Major Device Number
- Minor Device Number
- Timestamp
- Device Name

Recuerda, en el comando `ls`, puedes ver el tipo de archivo con el primer bit en cada línea. Los archivos de dispositivo se denotan de la siguiente manera:

- c - character
- b - block
- p - pipe
- s - socket

### Character Device

Estos dispositivos transfieren datos, pero un carácter a la vez. Verás muchos pseudo dispositivos (`/dev/null`) como character devices. Estos dispositivos no están realmente conectados físicamente a la máquina, pero permiten una mayor funcionalidad al sistema operativo.

### Block Device

Estos dispositivos transfieren datos, pero en bloques grandes de tamaño fijo. Lo más común es que veas dispositivos que utilizan bloques de datos como block devices, como discos duros, sistemas de archivos, etc.

### Pipe Device

Las named pipes permiten que dos o más procesos se comuniquen entre sí. Son similares a los character devices, pero en lugar de enviar la salida a un dispositivo, se envía a otro proceso.

### Socket Device

Los socket devices facilitan la comunicación entre procesos, de forma similar a los pipe devices, pero pueden comunicarse con muchos procesos a la vez.

### Device Characterization

Los dispositivos se caracterizan utilizando dos números: **major device number** y **minor device number**. Puedes ver estos números en el ejemplo de `ls` anterior; están separados por una coma. Por ejemplo, digamos que un dispositivo tenía los números de dispositivo: **8, 0**:

El major device number representa el device driver que se utiliza, en este caso 8, que a menudo es el número mayor para los sd block devices. El minor number le dice al kernel qué dispositivo único es en esta clase de driver; en este caso, 0 se usa para representar el primer dispositivo (a).

## Exercise

Mira tu directorio `/dev` y averigua qué tipos de dispositivos puedes ver.

## Quiz Question

¿Cuál es el símbolo para los character devices en el comando `ls -l`?

## Quiz Answer

c
