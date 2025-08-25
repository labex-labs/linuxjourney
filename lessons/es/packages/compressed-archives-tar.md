---
index: 3
lang: "es"
title: "tar y gzip"
meta_title: "tar y gzip - Paquetes"
meta_description: "Aprende a usar tar y gzip para archivar y comprimir archivos en Linux. Entiende los comandos para crear, extraer y comprimir archivos. ¡Empieza con esta guía para principiantes!"
meta_keywords: "tar, gzip, archivado Linux, compresión de archivos, comando tar, comando gzip, tutorial Linux, Linux para principiantes"
---

## Lesson Content

Antes de entrar en la instalación de paquetes y los diferentes gestores, necesitamos hablar sobre el archivado y la compresión de archivos, porque lo más probable es que te encuentres con ellos cuando busques software en internet.

Probablemente ya sabes lo que es un archivo de ficheros; lo más seguro es que te hayas encontrado con tipos de archivos como .rar y .zip. Estos son archivos de ficheros; contienen muchos ficheros dentro de ellos, pero vienen en este único y ordenado fichero conocido como archivo.

### Comprimir archivos con gzip

gzip es un programa usado para comprimir archivos en Linux; terminan en una extensión .gz.

Para comprimir un archivo:

```bash
gzip mycoolfile
```

Para descomprimir el archivo:

```bash
gunzip mycoolfile.gz
```

### Crear archivos con tar

Desafortunadamente, gzip no puede añadir múltiples archivos en un solo archivo por nosotros. Afortunadamente, tenemos el programa tar que sí lo hace. Cuando creas un archivo usando tar, tendrá una extensión .tar.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - crear
- `v` - indicar al programa que sea detallado y nos muestre lo que está haciendo
- `f` - el nombre del archivo tar debe ir después de esta opción; si estás creando un archivo tar, tendrás que inventar un nombre

### Desempaquetar archivos con tar

Para extraer el contenido de un archivo tar, usa:

```bash
tar xvf mytarfile.tar
```

- `x` - extraer
- `v` - indicar al programa que sea detallado y nos muestre lo que está haciendo
- `f` - el archivo que quieres extraer

### Comprimir/descomprimir archivos con tar y gzip

Muchas veces verás un archivo tar que ha sido comprimido, como: `mycompressedarchive.tar.gz`. Todo lo que necesitas hacer es trabajar de afuera hacia adentro, así que primero elimina la compresión con `gunzip` y luego puedes desempaquetar el archivo tar. Opcionalmente, puedes usar la opción **z** con tar, que simplemente le indica que use la utilidad gzip o gunzip.

Crear un archivo tar comprimido:

```bash
tar czf myfile.tar.gz
```

Descomprimir y desempaquetar:

```bash
tar xzf file.tar
```

Si necesitas ayuda para recordar esto: ¡e**X**trae todos los archivos **Z**ee!

tar es uno de esos comandos que es tan importante y, sin embargo, nunca lo recuerdas realmente. xkcd relevante: `https://xkcd.com/1168`

### Otras utilidades

A lo largo de tu viaje con Linux, te encontrarás con otros tipos de archivo y compresión como: bzip2, compress, zip, unzip, etc. Son un poco menos comunes, pero ten en cuenta que diferentes utilidades requerirán diferentes comandos.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del archivado y la compresión de archivos:

1. **[Empaquetado y Compresión de Archivos](https://labex.io/es/labs/linux-file-packaging-and-compression-385413)** - Aprende técnicas esenciales de compresión y empaquetado de archivos en Linux usando herramientas como tar, gzip y zip.
2. **[Crear y Restaurar una Copia de Seguridad con tar en Linux](https://labex.io/es/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Adquiere experiencia práctica creando y restaurando copias de seguridad del sistema de archivos usando el comando tar.
3. **[Copia de Seguridad del Registro del Sistema](https://labex.io/es/labs/linux-backup-system-log-17989)** - Aprende la habilidad esencial de hacer copias de seguridad de los archivos de registro del sistema usando el comando tar y el formato de fecha.

Estos laboratorios te ayudarán a aplicar los conceptos de archivado y compresión en escenarios reales y a ganar confianza en la gestión de archivos en Linux.

## Quiz Question

¿Qué bandera de tar se usa para crear archivos?

## Quiz Answer

c
