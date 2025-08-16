---
lang: "es"
title: "Uso del Disco"
description: "Aprende a verificar el uso del disco y el espacio libre en Linux usando los comandos df y du. Comprende sus diferencias y cuándo usar cada uno. Tutorial de gestión de discos en Linux."
keywords: "comando df, comando du, uso del disco Linux, verificar espacio libre, tutorial Linux, Linux para principiantes, gestión de discos, guía Linux"
---

## Lesson Content

Hay algunas herramientas que puedes usar para ver la utilización de tus discos:

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

El comando `df` te muestra la utilización de tus sistemas de archivos actualmente montados. La bandera `-h` te da un formato legible para humanos. Puedes ver cuál es el dispositivo y cuánta capacidad se usa y está disponible.

Supongamos que tu disco se está llenando y quieres saber qué archivos o directorios están ocupando ese espacio; para eso, puedes usar el comando **du**.

```bash
du -h
```

Esto te muestra el uso del disco del directorio actual en el que te encuentras. Puedes echar un vistazo al directorio raíz con `du -h /`, pero eso puede volverse un poco desordenado.

Ambos comandos son tan similares en sintaxis que puede ser difícil recordar cuál usar. Para verificar cuánto de tu **disco** está **libre**, usa `df`. Para verificar el **uso del disco**, usa `du`.

## Exercise

Observa el uso de tu disco y el espacio libre con `du` y `df`.

## Quiz Question

¿Qué comando se usa para mostrar cuánto espacio libre hay en tu disco?

## Quiz Answer

df
