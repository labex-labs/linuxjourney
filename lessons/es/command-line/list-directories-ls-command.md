---
index: 4
lang: "es"
title: "ls (Listar Directorios)"
meta_title: "ls (Listar Directorios) - Línea de Comandos"
meta_description: "Aprenda a usar el potente comando ls en Linux. Esta guía cubre cómo listar el contenido de directorios, ver archivos ocultos con ls -a, obtener listados detallados con ls -l y usar el comando ls -r para ordenar inversamente. Una lección perfecta para dominar el cmd ls."
meta_keywords: "comando ls, listar directorios, cmd ls, comando ls -r, comando ls, linux ls -r, comando linux ls, archivos ocultos, comandos Linux, Linux para principiantes"
---

## Lesson Content

Ahora que sabemos cómo movernos por el sistema de archivos, ¿cómo averiguamos qué tenemos disponible? Sin la herramienta adecuada, es como moverse a oscuras. Afortunadamente, el maravilloso `command linux ls` está aquí para ayudar listando el contenido de los directorios.

### Uso Básico del Comando ls

Por defecto, el comando `ls` listará los directorios y archivos en tu directorio actual. Sin embargo, también puedes especificar una ruta para listar el contenido de un directorio diferente.

```bash
ls
ls /home/pete
```

El `command ls` es una herramienta versátil que puede mostrarte información detallada sobre los archivos y directorios que estás viendo.

### Visualización de Archivos Ocultos

Ten en cuenta que no todos los archivos en un directorio son visibles por defecto. En Linux, los nombres de archivo que comienzan con un punto (`.`) están ocultos. Puedes verlos usando el `cmd ls` con el indicador `-a`, que significa "all" (todos).

```bash
ls -a
```

### Obtención de Información Detallada

Otro indicador esencial de `ls` es `-l` de "long" (largo). Esta opción proporciona una lista detallada de archivos en formato largo. Esto te mostrará información detallada, comenzando desde la izquierda: permisos del archivo, número de enlaces, nombre del propietario, grupo del propietario, tamaño del archivo, marca de tiempo de la última modificación y el nombre del archivo o directorio.

```bash
ls -l
```

Aquí tienes un ejemplo de la salida:

```plaintext
pete@icebox:~$ ls -l
total 80
drwxr-x--- 7 pete penguingroup   4096 Nov 20 16:37 Desktop
drwxr-x--- 2 pete penguingroup   4096 Oct 19 10:46  Documents
drwxr-x--- 4 pete penguingroup   4096 Nov 20 09:30 Downloads
drwxr-x--- 2 pete penguingroup   4096 Oct  7 13:13   Music
drwxr-x--- 2 pete penguingroup   4096 Sep 21 14:02 Pictures
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Public
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Templates
drwxr-x--- 2 pete penguingroup   4096 Jul 27 12:41   Videos
```

### Ordenación en Orden Inverso

A veces querrás cambiar el orden de clasificación. El `ls -r command` lista archivos y directorios en orden alfabético inverso. La opción `linux ls -r` es particularmente útil cuando quieres ver los últimos elementos de una lista larga primero.

```bash
ls -r
```

### Combinación de Indicadores de Comando

Los comandos tienen indicadores (también llamados argumentos u opciones) para añadir más funcionalidad. Como vimos con `-a` y `-l`, puedes combinarlos en un solo comando como `ls -la`. El orden de los indicadores generalmente no importa, por lo que `ls -al` funcionaría de manera idéntica. También puedes añadir el indicador inverso: `ls -lar`.

```bash
ls -la
```

## Exercise

¡La práctica hace al maestro! Aquí tienes un laboratorio práctico para reforzar tu comprensión del comando `ls`:

- **[Comando ls de Linux: Listado de Contenido](https://labex.io/es/labs/linux-linux-ls-command-content-listing-219205)** - Practica el uso del comando `ls` para listar y analizar eficientemente el contenido de archivos y directorios. Aprenderás varias opciones para listados detallados, visualización de archivos ocultos, tamaños legibles por humanos y técnicas de ordenación para mejorar tus habilidades en la línea de comandos.

Este laboratorio te ayudará a aplicar los conceptos en un escenario real y a ganar confianza con el listado de directorios en Linux.

## Quiz Question

¿Qué comando usarías para ver archivos ocultos? Por favor, responde en inglés, prestando atención a las mayúsculas y minúsculas.

## Quiz Answer

ls -a
