---
index: 6
lang: "es"
title: "file"
meta_title: "file - Línea de Comandos"
meta_description: "Aprende el comando file en Linux con ejemplos para identificar archivos de texto, imágenes, scripts, archivos comprimidos, binarios y tipos MIME."
meta_keywords: "comando linux file, comando file, identificar tipo de archivo linux, tipo mime linux, archivo de texto, archivo binario, archivo comprimido"
---

## Lesson Content

En la lección anterior, aprendimos sobre `touch`. Volvamos a eso un momento. ¿Notaste que el nombre del archivo no seguía las convenciones estándar de nombres, como probablemente has visto en otros sistemas operativos como Windows? Normalmente, esperarías que un archivo llamado `banana.jpeg` sea una imagen JPEG.

En Linux, los nombres de archivo no están obligados a representar el contenido del archivo. Puedes crear un archivo llamado `funny.gif` que en realidad no sea un GIF.

Para saber qué tipo de archivo es un archivo, puedes usar el comando `file`. Te mostrará una descripción del contenido del archivo.

```bash
$ file banana.jpg
banana.jpg: JPEG image data
```

### Por qué las extensiones de archivo no son suficientes

Las herramientas de Linux usualmente no requieren una extensión de archivo para decidir qué es un archivo. Un script de shell puede llamarse `backup`, un archivo de texto puede llamarse `README`, y una imagen puede tener la extensión incorrecta. El comando `file` inspecciona el contenido y los metadatos del archivo para hacer una mejor suposición.

```bash
$ file README
README: ASCII text
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable
```

### Comprobando múltiples archivos

Puedes revisar varios archivos a la vez:

```bash
$ file notes.txt image.png archive.tar.gz
notes.txt: ASCII text
image.png: PNG image data
archive.tar.gz: gzip compressed data
```

Los comodines también funcionan:

```bash
$ file *
```

### Mostrar tipos MIME

La opción `-i` imprime información en formato MIME, lo cual es útil cuando trabajas con archivos web o scripts.

```bash
$ file -i index.html
index.html: text/html; charset=us-ascii
```

### Opciones comunes de file

- `-i`: Muestra información del tipo MIME.
- `-b`: Modo breve, omite el nombre del archivo en la salida.
- `-L`: Sigue enlaces simbólicos.
- `-z`: Intenta inspeccionar archivos comprimidos.

Por ejemplo:

```bash
$ file -b notes.txt
ASCII text
```

### Preguntas comunes

**¿El comando file se basa solo en las extensiones?** No. Principalmente inspecciona el contenido del archivo y firmas conocidas.

**¿Puede file equivocarse?** Sí. Hace una suposición educada, especialmente para archivos inusuales o dañados.

**¿Por qué file dice "data"?** El archivo no coincide con un tipo conocido más específico, o puede ser datos binarios sin una firma reconocible.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión sobre la inspección del contenido y propiedades de archivos:

1. **[Comando Linux ls: Listado de Contenido](https://labex.io/es/labs/linux-linux-ls-command-content-listing-219205)** - Aprende el comando `ls` en Linux para listar y analizar eficientemente el contenido de archivos y directorios, lo que a menudo precede o sigue al uso del comando `file` para entender qué hay en tus directorios.
2. **[Comando Linux cat: Concatenación de Archivos](https://labex.io/es/labs/linux-linux-cat-command-file-concatenating-210986)** - Practica ver y manipular archivos de texto, una tarea común después de identificar el tipo de un archivo.
3. **[Comando Linux more: Desplazamiento de Archivos](https://labex.io/es/labs/linux-linux-more-command-file-scrolling-214299)** - Mejora tus habilidades en la línea de comandos para navegar y explorar archivos de texto grandes, basándote en la capacidad de identificar tipos de archivo y luego inspeccionar su contenido.

Estos laboratorios te ayudarán a aplicar los conceptos de inspección de archivos y visualización de contenido en escenarios reales y a ganar confianza en la gestión de archivos en Linux.

## Quiz Question

¿Qué comando puedes usar para encontrar el tipo de archivo de un archivo?

## Quiz Answer

file
