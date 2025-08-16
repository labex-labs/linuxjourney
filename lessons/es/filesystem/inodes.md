---
lang: "es"
title: "Inodes"
description: "Aprende sobre los inodes de Linux, su estructura y cómo gestionan los archivos. Comprende los números de inode y usa `df -i` y `ls -li` para verificar el uso de inodes. ¡Comienza tu viaje en Linux!"
keywords: "inodes de Linux, tutorial de inode, df -i, ls -li, filesystem de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

¿Recuerdas cómo nuestro filesystem se compone de todos nuestros archivos reales y una base de datos que gestiona estos archivos? La base de datos se conoce como la tabla de inodes.

### ¿Qué es un inode?

Un inode (index node) es una entrada en esta tabla, y hay uno por cada archivo. Describe todo sobre el archivo, como:

- File type - regular file, directory, character device, etc.
- Owner
- Group
- Access permissions
- Timestamps - mtime (time of last file modification), ctime (time of last attribute change), atime (time of last access)
- Number of hardlinks to the file
- Size of the file
- Number of blocks allocated to the file
- Pointers to the data blocks of the file - ¡lo más importante!

Básicamente, los inodes almacenan todo sobre el archivo, ¡excepto el filename y el archivo en sí!

### ¿Cuándo se crean los inodes?

Cuando se crea un filesystem, también se asigna espacio para los inodes. Los algoritmos determinan cuánto espacio de inode necesitas, dependiendo del volumen del disco y más. Probablemente en algún momento de tu vida hayas visto errores por problemas de falta de espacio en disco. Lo mismo puede ocurrir con los inodes (aunque es menos común); puedes quedarte sin inodes y, por lo tanto, no poder crear más archivos. Recuerda, el almacenamiento de datos depende tanto de los datos como de la base de datos (inodes).

Para ver cuántos inodes quedan en tu sistema, usa el comando `df -i`.

### Información del Inode

Los inodes se identifican por números. Cuando se crea un archivo, se le asigna un número de inode, y el número se asigna en orden secuencial. Sin embargo, a veces puedes notar que cuando creas un nuevo archivo, obtiene un número de inode que es más bajo que otros. Esto se debe a que una vez que los inodes se eliminan, pueden ser reutilizados por otros archivos. Para ver los números de inode, ejecuta `ls -li`:

```bash
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

El primer campo de este comando lista el número de inode.

También puedes ver información detallada sobre un archivo con `stat`; también te da información sobre el inode.

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

### ¿Cómo localizan los inodes los archivos?

Sabemos que nuestros datos están en algún lugar del disco. Desafortunadamente, probablemente no se almacenaron secuencialmente, por lo que tenemos que usar inodes. Los inodes apuntan a los data blocks reales de tus archivos. En un filesystem típico (no todos funcionan igual), cada inode contiene 15 pointers. Los primeros 12 pointers apuntan directamente a los data blocks. El 13º pointer apunta a un block que contiene pointers a más blocks, el 14º pointer apunta a otro block anidado de pointers, ¡y el 15º pointer apunta de nuevo a otro block de pointers! Confuso, ¡lo sé! La razón por la que esto se hace de esta manera es para mantener la estructura del inode igual para cada inode, pero poder referenciar archivos de diferentes tamaños. Si tuvieras un archivo pequeño, podrías encontrarlo más rápido con los primeros 12 direct pointers; los archivos más grandes se pueden encontrar con los nidos de pointers. De cualquier manera, la estructura del inode es la misma.

## Exercise

Observe some inode numbers for different files. Which ones are usually created first?

## Quiz Question

¿Cómo se ve cuántos inodes quedan en tu sistema?

## Quiz Answer

df -i
