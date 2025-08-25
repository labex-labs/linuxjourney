---
index: 2
lang: "es"
title: "tipos de dispositivos"
meta_title: "tipos de dispositivos - Dispositivos"
meta_description: "Aprenda sobre los tipos de dispositivos Linux (carácter, bloque, tubería, socket) y cómo identificarlos usando `ls -l /dev`. Comprenda los números de dispositivo mayor/menor. Tutorial de Linux para principiantes."
meta_keywords: "tipos de dispositivos Linux, ls -l /dev, dispositivo de carácter, dispositivo de bloque, número de dispositivo mayor menor, tutorial de Linux, guía de Linux, principiante"
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

- Permisos
- Propietario
- Grupo
- Número de Dispositivo Mayor
- Número de Dispositivo Menor
- Marca de tiempo
- Nombre del Dispositivo

Recuerde, en el comando `ls`, puede ver el tipo de archivo con el primer bit en cada línea. Los archivos de dispositivo se denotan de la siguiente manera:

- c - character
- b - block
- p - pipe
- s - socket

### Dispositivo de Carácter

Estos dispositivos transfieren datos, pero un carácter a la vez. Verá muchos pseudo dispositivos (`/dev/null`) como dispositivos de carácter. Estos dispositivos no están realmente conectados físicamente a la máquina, pero permiten una mayor funcionalidad al sistema operativo.

### Dispositivo de Bloque

Estos dispositivos transfieren datos, pero en grandes bloques de tamaño fijo. Lo más común es ver dispositivos que utilizan bloques de datos como dispositivos de bloque, como discos duros, sistemas de archivos, etc.

### Dispositivo de Tubería (Pipe)

Las tuberías con nombre permiten que dos o más procesos se comuniquen entre sí. Son similares a los dispositivos de carácter, pero en lugar de enviar la salida a un dispositivo, se envía a otro proceso.

### Dispositivo de Socket

Los dispositivos de socket facilitan la comunicación entre procesos, de forma similar a los dispositivos de tubería, pero pueden comunicarse con muchos procesos a la vez.

### Caracterización de Dispositivos

Los dispositivos se caracterizan utilizando dos números: **número de dispositivo mayor** y **número de dispositivo menor**. Puede ver estos números en el ejemplo de `ls` anterior; están separados por una coma. Por ejemplo, digamos que un dispositivo tenía los números de dispositivo: **8, 0**:

El número de dispositivo mayor representa el controlador de dispositivo que se utiliza, en este caso 8, que a menudo es el número mayor para los dispositivos de bloque sd. El número menor le dice al kernel qué dispositivo único es en esta clase de controlador; en este caso, 0 se usa para representar el primer dispositivo (a).

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de los archivos de dispositivo de Linux y su gestión:

1. **[Gestionar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practique la creación y gestión de particiones de disco y sistemas de archivos, que son dispositivos de bloque fundamentales en Linux.
2. **[Explorar Dispositivos de Hardware en Linux](https://labex.io/es/labs/comptia-explore-hardware-devices-in-linux-590861)** - Aprenda a identificar e inspeccionar varios dispositivos de hardware, entendiendo cómo se representan en el directorio `/dev`.
3. **[Crear y Activar un Archivo de Intercambio en Linux](https://labex.io/es/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Obtenga experiencia práctica en la creación y activación de un archivo de intercambio, que funciona como un dispositivo de memoria virtual.

Estos laboratorios le ayudarán a aplicar los conceptos de interacción y gestión de dispositivos en escenarios reales y a generar confianza con la administración de sistemas Linux.

## Quiz Question

¿Cuál es el símbolo para los dispositivos de carácter en el comando `ls -l`?

## Quiz Answer

c
