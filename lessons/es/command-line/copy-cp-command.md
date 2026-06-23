---
index: 10
lang: "es"
title: "cp (Copiar)"
meta_title: "cp (Copiar) - Línea de Comandos"
meta_description: "Aprende el comando cp de Linux con ejemplos para copiar archivos, directorios, múltiples archivos, comodines, copias de seguridad y opciones como cp -r, cp -i y cp -p."
meta_keywords: "comando linux cp, comando cp, copiar archivos linux, cp -r, cp -i, cp -p, cp -a, cp -u, copia recursiva, comodines linux"
---

## Lesson Content

El comando `cp` es la herramienta estándar para copiar archivos y directorios en Linux. Crea una nueva copia dejando el archivo original en su lugar. Su sintaxis básica es:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

Puedes copiar un archivo a otro archivo, uno o más archivos a un directorio, o un árbol completo de directorios con la opción adecuada.

### Copia básica de archivos

Para copiar un archivo, especificas el archivo fuente y el directorio o ruta de destino.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

En este ejemplo, `mycoolfile` es el archivo fuente, y `/home/pete/Documents/cooldocs` es el directorio de destino. También puedes copiar un archivo y darle un nuevo nombre en el destino.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

Si el destino es un directorio existente, el archivo copiado mantiene su nombre original. Si el destino es un nombre de archivo, `cp` crea una copia con ese nuevo nombre.

### Copiar múltiples archivos a un directorio

Para copiar varios archivos al mismo directorio, lista todas las fuentes primero y coloca el directorio de destino al final.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

El último argumento debe ser un directorio cuando proporcionas más de una fuente.

### Uso de comodines para copias masivas

Los comodines son caracteres especiales que te ayudan a seleccionar múltiples archivos basados en patrones, proporcionando gran flexibilidad.

- `*`: Coincide con cualquier secuencia de caracteres.
- `?`: Coincide con cualquier carácter individual.
- `[]`: Coincide con cualquiera de los caracteres encerrados en los corchetes.

Por ejemplo, para copiar todas las imágenes JPEG desde tu ubicación actual al directorio `Pictures`:

```bash
$ cp *.jpg /home/pete/Pictures
```

Puedes previsualizar los archivos que coinciden antes de copiar:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

### Copiar directorios recursivamente

Si intentas copiar un directorio usando `cp` sin opciones, recibirás un error. Para copiar un directorio y todo su contenido, incluidos subdirectorios, debes usar la bandera `-r` (recursiva).

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

Este comando copia el directorio `Pumpkin` y todo lo que contiene a tu directorio `Documents`.

También puedes ver `-R`, que tiene el mismo propósito recursivo en sistemas Linux típicos:

```bash
$ cp -R website /home/pete/backups/
```

### Manejo de sobrescrituras de archivos

Por defecto, `cp` sobrescribirá un archivo en el destino si tiene el mismo nombre. Para evitar la pérdida accidental de datos, usa la bandera `-i` (interactiva), que solicita confirmación antes de sobrescribir.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

Por otro lado, si quieres forzar una sobrescritura sin pedir confirmación, usa la opción `-f`. Esto es útil en scripts donde la interacción del usuario no es posible.

```bash
$ cp -f mycoolfile /home/pete/Pictures
```

Otra opción de seguridad útil es `-n`, que significa "no sobrescribir". Evita sobrescribir un archivo existente en el destino.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

### Preservar atributos de archivo con -p

Cuando copias un archivo, sus metadatos, como la hora de modificación y la propiedad, normalmente se actualizan. Para preservar estos atributos originales, usa la opción `-p`.

La opción `cp -p` es particularmente útil para copias de seguridad o cuando migras archivos donde preservar las marcas de tiempo es importante.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

Esto copia `mycoolfile` preservando su modo, propiedad donde sea posible, y marcas de tiempo.

### Copias de archivo con -a

La opción `-a` significa archivo. Se usa comúnmente para copias de directorios estilo respaldo porque preserva muchos atributos y copia recursivamente.

```bash
$ cp -a project/ project-backup/
```

Para muchas copias de seguridad diarias, `cp -a` es más conveniente que combinar varias opciones manualmente.

### Copiar solo archivos más nuevos con -u

La opción `-u` copia solo cuando el archivo fuente es más nuevo que el archivo destino o cuando el archivo destino no existe.

```bash
$ cp -u *.txt /home/pete/Documents/
```

Esto es útil cuando actualizas una carpeta sin reescribir archivos que ya están al día.

### Opciones comunes de cp

Aquí están las opciones que usarás con más frecuencia:

- `-r` o `-R`: Copiar directorios recursivamente.
- `-i`: Preguntar antes de sobrescribir un archivo.
- `-f`: Forzar la sobrescritura eliminando primero el destino si es necesario.
- `-n`: No sobrescribir archivos existentes.
- `-p`: Preservar modo, propiedad donde sea posible y marcas de tiempo.
- `-a`: Modo archivo, útil para preservar árboles de directorios.
- `-u`: Copiar solo cuando la fuente es más nueva que el destino.
- `-v`: Mostrar cada archivo mientras se copia.

### Preguntas comunes

**¿Por qué cp sobrescribió mi archivo?** Por defecto, `cp` reemplaza un archivo destino con el mismo nombre. Usa `cp -i` para preguntar primero o `cp -n` para evitar sobrescribir.

**¿Por qué cp no puede copiar un directorio?** Un directorio requiere copia recursiva. Usa `cp -r source-dir destination-dir`.

**¿Cuál es la diferencia entre cp y mv?** `cp` crea una copia y mantiene el original. `mv` mueve o renombra el original.

**¿Debo usar cp -r o cp -a para copias de seguridad?** Usa `cp -r` para una copia recursiva simple. Usa `cp -a` cuando quieres una copia estilo respaldo que preserve más atributos de archivo.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of copying files and directories in Linux:

1. **[Linux cp Command: File Copying](https://labex.io/es/labs/linux-linux-cp-command-file-copying-209744)** - Practice basic usage, advanced options like recursive copying, preserving attributes, and using wildcards to efficiently copy files and directories.
2. **[Organizing Files and Directories](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practice essential Linux file management skills by using `cp`, `mv`, and `rm` commands to organize a project structure, move files, and clean up unnecessary directories.

These labs will help you apply the concepts in real scenarios and build confidence with file copying and management in Linux.

## Quiz Question

¿Qué bandera necesitas especificar para copiar un directorio?

## Quiz Answer

-r
