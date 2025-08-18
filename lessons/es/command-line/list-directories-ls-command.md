---
index: 4
lang: "es"
title: "ls (Listar Directorios)"
meta_title: "ls (Listar Directorios) - Command Line"
meta_description: "Aprende a usar el comando 'ls' en Linux para listar el contenido de directorios, ver archivos ocultos y entender los detalles de los archivos. ¡Mejora tus habilidades en la línea de comandos de Linux!"
meta_keywords: "comando ls, listar directorios, tutorial de Linux, archivos ocultos, comandos de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Ahora que sabemos cómo movernos por el sistema, ¿cómo averiguamos qué tenemos disponible? En este momento, es como si nos moviéramos en la oscuridad. Bueno, podemos usar el maravilloso comando `ls` para listar el contenido del directorio. El comando `ls` listará directorios y archivos en el directorio actual por defecto; sin embargo, puedes especificar qué ruta quieres listar los directorios.

```bash
ls
ls /home/pete
```

`ls` es una herramienta bastante útil; también te muestra información detallada sobre los archivos y directorios que estás viendo.

Además, ten en cuenta que no todos los archivos de un directorio serán visibles. Los nombres de archivo que comienzan con `.` están ocultos. Sin embargo, puedes verlos con el comando `ls` y pasarle la bandera `-a` (`a` de all).

```bash
ls -a
```

También hay otra bandera útil de `ls`, `-l` de long. Esto muestra una lista detallada de archivos en formato largo. Esto te mostrará información detallada, comenzando por la izquierda: permisos de archivo, número de enlaces, nombre del propietario, grupo del propietario, tamaño del archivo, marca de tiempo de la última modificación y nombre del archivo/directorio.

```bash
ls -l
```

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

Los comandos tienen lo que se llaman banderas (o argumentos u opciones, como quieras llamarlos) para añadir más funcionalidad. Mira cómo añadimos `-a` y `-l`; bueno, puedes añadirlos ambos juntos con `-la`. El orden de las banderas determina el orden en que van. La mayoría de las veces, esto no importa mucho, así que también puedes hacer `ls -al` y seguiría funcionando.

```bash
ls -la
```

## Exercise

Ejecuta `ls` con diferentes banderas y observa la salida que recibes.

## Quiz Question

¿Qué comando usarías para ver los archivos ocultos?

## Quiz Answer

ls -a
