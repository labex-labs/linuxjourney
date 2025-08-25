---
index: 9
lang: "es"
title: "Uso del Disco"
meta_title: "Uso del Disco - El Sistema de Archivos"
meta_description: "Aprende a verificar el uso del disco y el espacio libre en Linux usando los comandos df y du. Comprende sus diferencias y cuándo usar cada uno. Tutorial de gestión de discos en Linux."
meta_keywords: "comando df, comando du, uso del disco Linux, verificar espacio libre, tutorial Linux, Linux para principiantes, gestión de discos, guía Linux"
---

## Lesson Content

Hay algunas herramientas que puedes usar para ver la utilización de tus discos:

```bash
pete@icebox:~$ df -h
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

El comando `df` te muestra la utilización de tus sistemas de archivos actualmente montados. La bandera `-h` te da un formato legible para humanos. Puedes ver cuál es el dispositivo y cuánta capacidad está usada y disponible.

Digamos que tu disco se está llenando y quieres saber qué archivos o directorios están ocupando ese espacio; para eso, puedes usar el comando **du**.

```bash
du -h
```

Esto te muestra el uso del disco del directorio actual en el que te encuentras. Puedes echar un vistazo al directorio raíz con `du -h /`, pero eso puede volverse un poco desordenado.

Ambos comandos son tan similares en sintaxis que puede ser difícil recordar cuál usar. Para verificar cuánto **espacio libre** hay en tu **disco**, usa `df`. Para verificar el **uso del disco**, usa `du`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión y utilización del espacio en disco en Linux:

1. **[Administrar particiones y sistemas de archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practica la creación, el formato y el montaje de sistemas de archivos, que son las estructuras subyacentes reportadas por `df` y `du`.
2. **[Crear y activar un archivo de intercambio en Linux](https://labex.io/es/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Aprende a administrar la memoria virtual en disco, un aspecto crítico de la gestión de recursos del sistema que impacta el espacio en disco.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza en la gestión de recursos de disco.

## Quiz Question

¿Qué comando se usa para mostrar cuánto espacio libre hay en tu disco?

## Quiz Answer

df
