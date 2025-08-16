---
title: "Symlinks"
description: "Aprende sobre los symlinks y hard links de Linux, incluyendo cómo crearlos y gestionarlos. Comprende sus diferencias y casos de uso con esta guía para principiantes."
keywords: "Linux symlinks, hard links, comando ln, enlaces simbólicos, sistema de archivos Linux, tutorial de Linux, Linux para principiantes"
---

## Lesson Content

Usemos un ejemplo anterior de información de inodo:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Es posible que hayas notado que hemos estado pasando por alto el tercer campo en el comando `ls`; ese campo es el conteo de enlaces (link count). El conteo de enlaces es el número total de hard links que tiene un archivo. Bueno, eso no significa nada para ti ahora mismo, así que primero hablemos de los enlaces.

### Symlinks

En el sistema operativo Windows, existen los accesos directos (shortcuts). Los accesos directos son solo alias a otros archivos. Si haces algo con el archivo original, podrías romper el acceso directo. En Linux, el equivalente a los accesos directos son los enlaces simbólicos (symbolic links o soft links o symlinks). Los symlinks nos permiten enlazar a otro archivo por su nombre de archivo. Otro tipo de enlace que se encuentra en Linux son los hard links; estos son en realidad otro archivo con un enlace a un inodo. Veamos qué quiero decir en la práctica, comenzando con los symlinks.

```bash
pete@icebox:~/Desktop$ echo 'myfile' > myfile
pete@icebox:~/Desktop$ echo 'myfile2' > myfile2
pete@icebox:~/Desktop$ echo 'myfile3' > myfile3

pete@icebox:~/Desktop$ ln -s myfile myfilelink
pete@icebox:~/Desktop$ ls -li
total 12
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
```

Puedes ver que he creado un enlace simbólico llamado `myfilelink` que apunta a `myfile`. Los enlaces simbólicos se denotan con `->`. Sin embargo, fíjate cómo obtuve un nuevo número de inodo; los symlinks son solo archivos que apuntan a nombres de archivo. Cuando modificas un symlink, el archivo también se modifica. Los números de inodo son únicos para los filesystems; no puedes tener dos números de inodo iguales en un solo filesystem, lo que significa que no puedes referenciar un archivo en un filesystem diferente por su número de inodo. Sin embargo, si usas symlinks, no usan números de inodo; usan nombres de archivo, por lo que pueden ser referenciados a través de diferentes filesystems.

### Hardlinks

Veamos un ejemplo de un hardlink:

```bash
pete@icebox:~/Desktop$ ln myfile2 myhardlink
pete@icebox:~/Desktop$ ls -li
total 16
  151 -rw-rw-r-- 1 pete pete 7 Jan 21 21:36 myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myfile2
93402 -rw-rw-r-- 1 pete pete 8 Jan 21 21:36 myfile3
93403 lrwxrwxrwx 1 pete pete 6 Jan 21 21:39 myfilelink -> myfile
93401 -rw-rw-r-- 2 pete pete 8 Jan 21 21:36 myhardlink
```

Un hardlink simplemente crea otro archivo con un enlace al mismo inodo. Así que si modificara el contenido de `myfile2` o `myhardlink`, el cambio se vería en ambos. Pero si eliminara `myfile2`, el archivo seguiría siendo accesible a través de `myhardlink`. Aquí es donde entra en juego nuestro conteo de enlaces en el comando `ls`. El conteo de enlaces es el número de hardlinks que tiene un inodo. Cuando eliminas un archivo, disminuirá ese conteo de enlaces. El inodo solo se elimina cuando todos los hardlinks al inodo han sido eliminados. Cuando creas un archivo, su conteo de enlaces es 1 porque es el único archivo que apunta a ese inodo. A diferencia de los symlinks, los hardlinks no abarcan filesystems porque los inodos son únicos para el filesystem.

### Creating a symlink

```bash
ln -s myfile mylink
```

Para crear un enlace simbólico, usas el comando `ln` con `-s` para simbólico, y especificas un archivo de destino y luego un nombre de enlace.

### Creating a hardlink

```bash
ln somefile somelink
```

Similar a la creación de un symlink, excepto que esta vez omites el `-s`.

## Exercise

Experimenta creando symlinks y hardlinks. Elimina un par y ve qué sucede.

## Quiz Question

¿Cuál es el comando utilizado para crear un symlink?

## Quiz Answer

ln -s
