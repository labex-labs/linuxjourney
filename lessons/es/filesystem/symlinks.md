---
index: 12
lang: "es"
title: "symlinks"
meta_title: "symlinks - El sistema de archivos"
meta_description: "Aprende sobre los symlinks y enlaces duros de Linux, incluyendo cómo crearlos y gestionarlos. Comprende sus diferencias y casos de uso con esta guía para principiantes."
meta_keywords: "Linux symlinks, enlaces duros, comando ln, enlaces simbólicos, sistema de archivos Linux, tutorial Linux, Linux para principiantes"
---

## Lesson Content

Usemos un ejemplo anterior de información de inodo:

```plaintext
pete@icebox:~$ ls -li
140 drwxr-xr-x 2 pete pete 6 Jan 20 20:13 Desktop
141 drwxr-xr-x 2 pete pete 6 Jan 20 20:01 Documents
```

Es posible que hayas notado que hemos estado pasando por alto el tercer campo en el comando `ls`; ese campo es el recuento de enlaces. El recuento de enlaces es el número total de enlaces duros que tiene un archivo. Bueno, eso no significa nada para ti ahora mismo, así que primero hablemos de los enlaces.

### Enlaces simbólicos (Symlinks)

En el sistema operativo Windows, existen cosas conocidas como accesos directos. Los accesos directos son solo alias a otros archivos. Si haces algo al archivo original, podrías romper el acceso directo. En Linux, el equivalente a los accesos directos son los enlaces simbólicos (o enlaces blandos o symlinks). Los symlinks nos permiten enlazar a otro archivo por su nombre de archivo. Otro tipo de enlace que se encuentra en Linux son los enlaces duros; estos son en realidad otro archivo con un enlace a un inodo. Veamos qué quiero decir en la práctica, comenzando con los symlinks.

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

Puedes ver que he creado un enlace simbólico llamado `myfilelink` que apunta a `myfile`. Los enlaces simbólicos se denotan con `->`. Sin embargo, fíjate cómo obtuve un nuevo número de inodo; los symlinks son solo archivos que apuntan a nombres de archivo. Cuando modificas un symlink, el archivo también se modifica. Los números de inodo son únicos para los sistemas de archivos; no puedes tener dos números de inodo iguales en un solo sistema de archivos, lo que significa que no puedes referenciar un archivo en un sistema de archivos diferente por su número de inodo. Sin embargo, si usas symlinks, no usan números de inodo; usan nombres de archivo, por lo que pueden ser referenciados a través de diferentes sistemas de archivos.

### Enlaces duros (Hardlinks)

Veamos un ejemplo de un enlace duro:

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

Un enlace duro simplemente crea otro archivo con un enlace al mismo inodo. Así que si modificara el contenido de `myfile2` o `myhardlink`, el cambio se vería en ambos. Pero si eliminara `myfile2`, el archivo seguiría siendo accesible a través de `myhardlink`. Aquí es donde entra en juego nuestro recuento de enlaces en el comando `ls`. El recuento de enlaces es el número de enlaces duros que tiene un inodo. Cuando eliminas un archivo, ese recuento de enlaces disminuirá. El inodo solo se elimina cuando se han eliminado todos los enlaces duros al inodo. Cuando creas un archivo, su recuento de enlaces es 1 porque es el único archivo que apunta a ese inodo. A diferencia de los symlinks, los enlaces duros no se extienden a través de sistemas de archivos porque los inodos son únicos para el sistema de archivos.

### Creación de un enlace simbólico

```bash
ln -s myfile mylink
```

Para crear un enlace simbólico, usas el comando `ln` con `-s` para simbólico, y especificas un archivo de destino y luego un nombre de enlace.

### Creación de un enlace duro

```bash
ln somefile somelink
```

Similar a la creación de un symlink, excepto que esta vez omites el `-s`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la gestión de archivos, enlaces e inodos:

1. **[Gestionar archivos y directorios en Linux](https://labex.io/es/labs/comptia-manage-files-and-directories-in-linux-590835)** - Practica la creación, copia, movimiento y eliminación de archivos y directorios, y aprende específicamente sobre enlaces simbólicos y duros, y cómo analizar inodos.
2. **[Navegar por el sistema de archivos en Linux](https://labex.io/es/labs/comptia-navigate-the-filesystem-in-linux-590971)** - Domina comandos esenciales como `pwd`, `cd` y `ls` para moverte eficientemente por el sistema de archivos de Linux, una habilidad fundamental para entender dónde residen los archivos y sus inodos.

Estos laboratorios te ayudarán a aplicar los conceptos de gestión de archivos y enlaces en escenarios reales y a construir confianza con el sistema de archivos de Linux.

## Quiz Question

¿Cuál es el comando utilizado para crear un symlink?

## Quiz Answer

ln -s
