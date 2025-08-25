---
index: 11
lang: "es"
title: "Inodos"
meta_title: "Inodos - El sistema de archivos"
meta_description: "Aprende sobre los inodos de Linux, su estructura y cómo gestionan los archivos. Comprende los números de inodo y usa `df -i` y `ls -li` para verificar el uso de inodos. ¡Comienza tu viaje en Linux!"
meta_keywords: "inodos de Linux, tutorial de inodos, df -i, ls -li, sistema de archivos de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

¿Recuerdas cómo nuestro sistema de archivos se compone de todos nuestros archivos reales y una base de datos que gestiona estos archivos? La base de datos se conoce como tabla de inodos.

### ¿Qué es un inodo?

Un inodo (nodo índice) es una entrada en esta tabla, y hay uno por cada archivo. Describe todo sobre el archivo, como:

- Tipo de archivo: archivo regular, directorio, dispositivo de caracteres, etc.
- Propietario
- Grupo
- Permisos de acceso
- Marcas de tiempo: mtime (hora de la última modificación del archivo), ctime (hora del último cambio de atributo), atime (hora del último acceso)
- Número de enlaces duros al archivo
- Tamaño del archivo
- Número de bloques asignados al archivo
- Punteros a los bloques de datos del archivo, ¡lo más importante!

Básicamente, los inodos almacenan todo sobre el archivo, ¡excepto el nombre del archivo y el archivo en sí!

### ¿Cuándo se crean los inodos?

Cuando se crea un sistema de archivos, también se asigna espacio para los inodos. Los algoritmos determinan cuánto espacio de inodos necesitas dependiendo del volumen del disco y más. Probablemente en algún momento de tu vida hayas visto errores por problemas de falta de espacio en disco. Lo mismo puede ocurrir también con los inodos (aunque es menos común); puedes quedarte sin inodos y, por lo tanto, no poder crear más archivos. Recuerda, el almacenamiento de datos depende tanto de los datos como de la base de datos (inodos).

Para ver cuántos inodos quedan en tu sistema, usa el comando `df -i`.

### Información del inodo

Los inodos se identifican por números. Cuando se crea un archivo, se le asigna un número de inodo, y el número se asigna en orden secuencial. Sin embargo, a veces puedes notar que cuando creas un nuevo archivo, obtiene un número de inodo que es más bajo que otros. Esto se debe a que una vez que los inodos se eliminan, pueden ser reutilizados por otros archivos. Para ver los números de inodo, ejecuta `ls -li`:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

El primer campo de este comando lista el número de inodo.

También puedes ver información detallada sobre un archivo con `stat`; también te da información sobre el inodo.

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

### ¿Cómo localizan los inodos los archivos?

Sabemos que nuestros datos están en algún lugar del disco. Desafortunadamente, probablemente no se almacenaron secuencialmente, por lo que tenemos que usar inodos. Los inodos apuntan a los bloques de datos reales de tus archivos. En un sistema de archivos típico (no todos funcionan igual), cada inodo contiene 15 punteros. Los primeros 12 punteros apuntan directamente a los bloques de datos. El puntero número 13 apunta a un bloque que contiene punteros a más bloques, el puntero número 14 apunta a otro bloque anidado de punteros, ¡y el puntero número 15 apunta de nuevo a otro bloque de punteros! Confuso, ¡lo sé! La razón por la que se hace de esta manera es para mantener la estructura del inodo igual para cada inodo, pero poder referenciar archivos de diferentes tamaños. Si tuvieras un archivo pequeño, podrías encontrarlo más rápido con los primeros 12 punteros directos; los archivos más grandes se pueden encontrar con los nidos de punteros. De cualquier manera, la estructura del inodo es la misma.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del sistema de archivos de Linux y la gestión de archivos:

1. **[Gestionar archivos y directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Practica la creación, eliminación, copia y movimiento de archivos y directorios, y explora la creación de enlaces simbólicos y duros mientras analizas los inodos.
2. **[Navegar por el sistema de archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Aprende las habilidades fundamentales para navegar por el sistema de archivos de Linux usando comandos esenciales de shell como `pwd`, `cd` y `ls`.
3. **[Encontrar archivos y comandos en Linux](https://labex.io/es/labs/comptia-find-files-and-commands-in-linux-590834)** - Domina las técnicas esenciales para localizar archivos y comandos en Linux usando `find`, `locate`, `whereis`, `which` y `type`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con la gestión del sistema de archivos de Linux.

## Quiz Question

¿Cómo ves cuántos inodos quedan en tu sistema?

## Quiz Answer

df -i
