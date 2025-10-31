---
index: 11
lang: "es"
title: "Inodos"
meta_title: "Inodos - El Sistema de Archivos"
meta_description: "Explore el concepto del inodo de Linux. Aprenda qué es un i-nodo, cómo los inodos en Linux gestionan los metadatos de archivos y cómo verificar el uso de inodos con `df -i` y `ls -li`."
meta_keywords: "inodo linux, inodo en linux, i nodo, inodo, inodo linux, número de inodo, sistema de archivos, df -i, ls -li, stat"
---

## Lesson Content

Recuerda que nuestro sistema de archivos se compone de todos nuestros archivos reales y una base de datos que los administra. Esta base de datos se conoce como la tabla de inodos, una parte fundamental de cómo funciona el `inode in linux`.

### ¿Qué es un Inodo de Linux

Un inodo (abreviatura de nodo índice) es una entrada en esta tabla. Cada archivo y directorio tiene su propio `inode`. Describe todo sobre el archivo, como:

- Tipo de archivo (ej. archivo regular, directorio, dispositivo de caracteres)
- Propietario
- Grupo
- Permisos de acceso
- Marcas de tiempo: mtime (última modificación), ctime (último cambio de atributo), atime (último acceso)
- Número de enlaces duros al archivo
- Tamaño del archivo
- Número de bloques asignados al archivo
- Punteros a los bloques de datos del archivo (¡lo más importante!)

Esencialmente, un `i node` almacena todos los metadatos sobre el archivo, excepto su nombre y el contenido real.

### Creación y Asignación de Inodos

Cuando se crea un sistema de archivos, también se asigna espacio para los inodos. Los algoritmos determinan cuánto espacio de `inode` necesitas según el volumen del disco y otros factores. Probablemente hayas visto errores de falta de espacio en disco antes. Lo mismo puede suceder con los inodos, aunque es menos común. Si te quedas sin inodos, no puedes crear nuevos archivos. El almacenamiento de datos depende tanto de los bloques de datos como de la base de datos (la tabla de `inode`).

Para ver cuántos inodos quedan en tu sistema, usa el comando `df -i`. Esta es una comprobación crucial para los administradores de sistemas que gestionan una gran cantidad de archivos pequeños.

### Visualización de Información del Inodo

Cada `linux inode` se identifica mediante un número único. Cuando se crea un archivo, se le asigna un número de inodo, a menudo de forma secuencial. Sin embargo, podrías notar que un nuevo archivo obtiene un número de inodo menor que los más antiguos. Esto sucede porque los números de inodo eliminados pueden reutilizarse para nuevos archivos. Para ver los números de inodo, ejecuta `ls -li`:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

El primer campo en la salida de este comando es el número de inodo. También puedes ver información detallada sobre el `i node` de un archivo con el comando `stat`:

```bash
pete@icebox:~$ stat ~/Desktop/
  File: ‘/home/pete/Desktop/’
  Size: 6               Blocks: 0          IO Block: 4096   directory
Device: 806h/2054d      Inode: 140         Links: 2
Access: (0755/drwxr-xr-x)  Uid: ( 1000/   pete)   Gid: ( 1000/   pete)
Access: 2016-01-20 20:13:50.647435982 -0800
Modify: 2016-01-20 20:13:06.191675843 -0800
Change: 2016-01-20 20:13:06.191675843 -0800
 Birth: -
```

### Cómo un I-Node Apunta a los Datos

Sabemos que nuestros datos se almacenan en el disco, pero es probable que no estén en un bloque continuo. Aquí es donde la estructura `inode linux` se vuelve esencial. Los inodos apuntan a los bloques de datos reales de tus archivos. En un sistema de archivos típico (aunque las implementaciones varían), cada inodo contiene 15 punteros. Los primeros 12 punteros apuntan directamente a bloques de datos. El puntero 13 apunta a un bloque que contiene más punteros. Los punteros 14 y 15 apuntan a bloques anidados más profundos de punteros. Esto puede parecer confuso, pero esta estructura permite que el `i node` mantenga un tamaño fijo mientras puede hacer referencia a archivos de tamaños variables. Los archivos pequeños se pueden acceder rápidamente usando los punteros directos, mientras que los archivos más grandes se localizan a través de los punteros anidados.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del sistema de archivos y la gestión de archivos en Linux:

1. **[Administrar Archivos y Directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Practica la creación, eliminación, copia y movimiento de archivos y directorios, y explora la creación de enlaces simbólicos y duros mientras analizas los inodos.
2. **[Navegar por el Sistema de Archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Aprende las habilidades fundamentales para navegar por el sistema de archivos de Linux usando comandos esenciales de shell como `pwd`, `cd` y `ls`.
3. **[Encontrar Archivos y Comandos en Linux](https://labex.io/es/labs/comptia-find-files-and-commands-in-linux-590834)** - Domina las técnicas esenciales para localizar archivos y comandos en Linux usando `find`, `locate`, `whereis`, `which` y `type`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la gestión del sistema de archivos de Linux.

## Quiz Question

¿Cómo ves cuántos inodos quedan en tu sistema? (Por favor, responde en inglés, prestando atención a las mayúsculas y minúsculas.)

## Quiz Answer

df -i
