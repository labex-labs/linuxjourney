---
index: 14
lang: "es"
title: "find"
meta_title: "find - Línea de Comandos"
meta_description: "Aprende el comando find de Linux con ejemplos para buscar por nombre, tipo, tamaño, tiempo de modificación y ejecutar acciones sobre archivos coincidentes."
meta_keywords: "comando linux find, comando find, encontrar archivos linux, find por nombre, find por tipo, find por tamaño, find mtime, find exec"
---

## Lesson Content

Con innumerables archivos en un sistema, puede ser difícil localizar uno específico. El comando `find` busca en árboles de directorios usando criterios como nombre, tipo, tamaño y tiempo de modificación.

### Usando el comando find

La sintaxis básica es:

```bash
find [PATH] [EXPRESSION]
```

Especificas el directorio donde buscar y los criterios de lo que buscas.

Por ejemplo, para buscar un archivo llamado `puppies.jpg` dentro del directorio `/home` y todos sus subdirectorios, usarías:

```bash
$ find /home -name puppies.jpg
```

Las búsquedas son recursivas por defecto, así que `find /home` busca dentro de `/home` y sus subdirectorios.

### Buscar por Nombre y Tipo

Uno de los usos más comunes de `find` es buscar por nombre de archivo. La opción `-name` coincide con nombres exactos o con patrones al estilo shell.

```bash
$ find . -name "*.txt"
```

También puedes especificar el tipo de elemento que buscas. La opción `-type` se usa para este propósito. Por ejemplo, si quieres encontrar un directorio en lugar de un archivo, puedes usar `d`.

```bash
$ find /home -type d -name MyFolder
```

En este comando, establecemos el tipo a `d` para directorio y buscamos un elemento llamado `MyFolder`. Para buscar específicamente archivos regulares, usarías `-type f`.

### Buscar por Tamaño y Tiempo

Puedes buscar por tamaño de archivo:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

El primer comando encuentra archivos mayores a 10 megabytes. El segundo encuentra archivos menores a 1 kilobyte.

También puedes buscar por tiempo de modificación:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime -7` significa modificado en los últimos 7 días. `-mtime +30` significa modificado hace más de 30 días.

### Ejecutar Acciones sobre los Resultados

Por defecto, `find` imprime las rutas coincidentes. Puedes agregar acciones como `-print`, `-delete` o `-exec`.

Imprimir coincidencias explícitamente:

```bash
$ find . -name "*.log" -print
```

Ejecutar `ls -l` en cada coincidencia:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

El marcador `{}` es reemplazado por cada ruta coincidente. El punto y coma escapado marca el fin del comando.

Ten cuidado con acciones destructivas como `-delete`. Primero ejecuta la misma búsqueda sin `-delete` para confirmar las coincidencias.

### Opciones comunes de find

- `-name PATTERN`: Coincidir por nombre de archivo.
- `-iname PATTERN`: Coincidir por nombre de archivo, ignorando mayúsculas y minúsculas.
- `-type f`: Coincidir archivos regulares.
- `-type d`: Coincidir directorios.
- `-size +10M`: Coincidir archivos mayores a 10 megabytes.
- `-mtime -7`: Coincidir archivos modificados en los últimos 7 días.
- `-maxdepth N`: Limitar la profundidad de búsqueda de `find`.

### Preguntas comunes

**¿Por qué find muestra "Permiso denegado"?** Tu usuario no puede leer algunos directorios. Busca en una ruta más específica o usa los privilegios adecuados.

**¿Por qué debo poner entre comillas patrones como "*.txt"?** Ponerlo entre comillas evita que el shell expanda el comodín antes de que `find` lo reciba.

**¿Es find recursivo?** Sí. Busca en subdirectorios por defecto.

## Exercise

Practice is key to mastering the `find command in linux`. These hands-on labs will help you reinforce your understanding of finding files and directories:

1. **[Linux find Command: File Searching](https://labex.io/es/labs/linux-linux-find-command-file-searching-219191)** - This lab provides an introduction to the `find` command, a versatile utility for searching and locating files and directories based on various criteria. You'll practice using `find` to locate specific files.
2. **[Discover Critical System Resources](https://labex.io/es/labs/linux-discover-critical-system-resources-388032)** - Learn essential Linux commands for locating files and executables, including `find`. You'll practice efficiently navigating the file system and discovering critical system resources.

These labs will help you apply the concepts in real scenarios and build confidence with using the `find` command effectively.

## Quiz Question

¿Qué opción debes especificar para el comando `find` para buscar por nombre? Por favor responde usando solo la opción en inglés, prestando atención al formato requerido (por ejemplo, -option).

## Quiz Answer

-name
