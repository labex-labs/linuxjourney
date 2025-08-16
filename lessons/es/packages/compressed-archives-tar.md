---
title: "tar y gzip"
description: "Aprende a usar tar y gzip para archivar y comprimir archivos en Linux. Comprende los comandos para crear, extraer y comprimir archivos. ¡Empieza con esta guía para principiantes!"
keywords: "tar, gzip, archivado Linux, compresión de archivos, comando tar, comando gzip, tutorial Linux, Linux para principiantes"
---

## Lesson Content

Antes de entrar en la instalación de paquetes y los diferentes gestores, necesitamos hablar sobre el archivado y la compresión de archivos, porque lo más probable es que te encuentres con ellos cuando busques software en internet.

Probablemente ya sepas qué es un archivo; lo más seguro es que te hayas encontrado con tipos de archivo como .rar y .zip. Estos son archivos de ficheros; contienen muchos ficheros dentro de ellos, pero vienen en un único fichero muy ordenado conocido como archivo.

### Compressing files with gzip

gzip es un programa utilizado para comprimir archivos en Linux; terminan en una extensión .gz.

Para comprimir un archivo:

```bash
gzip mycoolfile
```

Para descomprimir el archivo:

```bash
gunzip mycoolfile.gz
```

### Creating archives with tar

Desafortunadamente, gzip no puede añadir múltiples archivos en un solo archivo por nosotros. Afortunadamente, tenemos el programa tar que sí lo hace. Cuando creas un archivo usando tar, tendrá una extensión .tar.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - create
- `v` - tell the program to be verbose and let us see what it's doing
- `f` - the filename of the tar file has to come after this option; if you are creating a tar file, you'll have to come up with a name

### Unpacking archives with tar

Para extraer el contenido de un archivo tar, usa:

```bash
tar xvf mytarfile.tar
```

- `x` - extract
- `v` - tell the program to be verbose and let us see what it's doing
- `f` - the file you want to extract

### Compressing/uncompressing archives with tar and gzip

Muchas veces verás un archivo tar que ha sido comprimido, como: `mycompressedarchive.tar.gz`. Todo lo que necesitas hacer es trabajar de afuera hacia adentro, así que primero elimina la compresión con `gunzip` y luego puedes desempaquetar el archivo tar. O puedes usar alternativamente la opción **z** con tar, que simplemente le dice que use la utilidad gzip o gunzip.

Crear un archivo tar comprimido:

```bash
tar czf myfile.tar.gz
```

Descomprimir y desempaquetar:

```bash
tar xzf file.tar
```

Si necesitas ayuda para recordar esto: e**X**trae todos los **Z**ee **F**iles!

tar es uno de esos comandos que es tan importante y, sin embargo, nunca lo recuerdas realmente. xkcd relevante: <https://xkcd.com/1168/>

### Other Utilities

A lo largo de tu viaje con Linux, te encontrarás con otros tipos de archivo y compresión como: bzip2, compress, zip, unzip, etc. Son un poco menos comunes, pero ten en cuenta que diferentes utilidades requerirán diferentes comandos.

## Exercise

Familiarízate con la documentación de tar y mira las otras opciones disponibles en la página man.

## Quiz Question

¿Qué bandera de tar se usa para crear archivos?

## Quiz Answer

c
