---
index: 4
lang: "es"
title: "ls (Listar Directorios)"
meta_title: "ls (Listar Directorios) - Línea de Comandos"
meta_description: "Aprende el comando Linux ls con ejemplos para listar archivos, archivos ocultos, salida en formato largo, tamaños legibles, ordenamiento y combinación de opciones."
meta_keywords: "comando ls, linux ls, listar archivos linux, listar directorios, ls -a, ls -l, ls -lh, ls -r, archivos ocultos"
---

## Lesson Content

Ahora que sabemos cómo movernos por el sistema de archivos, ¿cómo descubrimos qué está disponible para nosotros? El comando `ls` lista archivos y directorios para que puedas inspeccionar tu ubicación actual o una ruta diferente.

### Uso Básico del Comando ls

Por defecto, el comando `ls` listará los directorios y archivos en tu directorio actual. Sin embargo, también puedes especificar una ruta para listar el contenido de otro directorio.

```bash
$ ls
$ ls /home/pete
```

También puedes listar un archivo específico:

```bash
$ ls /etc/hosts
/etc/hosts
```

### Ver Archivos Ocultos

No todos los archivos en un directorio son visibles por defecto. En Linux, los nombres de archivo que comienzan con un punto (`.`) están ocultos. Puedes verlos con la opción `-a`, que significa todos.

```bash
$ ls -a
.  ..  .bashrc  Documents  Pictures
```

### Obtener Información Detallada

Otra opción esencial de `ls` es `-l` para formato largo. Muestra permisos de archivo, número de enlaces, propietario, grupo, tamaño, hora de modificación y nombre.

```bash
$ ls -l
```

Aquí hay un ejemplo de la salida:

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

Para tamaños de archivo más fáciles de leer, añade `-h` para salida legible para humanos:

```bash
$ ls -lh
```

### Ordenar en Orden Inverso

A veces puedes querer cambiar el orden de clasificación. La opción `-r` lista archivos y directorios en orden inverso.

```bash
$ ls -r
```

Puedes ordenar por tiempo de modificación con `-t`, luego invertirlo con `-r`:

```bash
$ ls -lt
$ ls -ltr
```

### Combinando Flags del Comando

Los comandos tienen flags, también llamados opciones, para añadir más funcionalidad. Como vimos con `-a` y `-l`, puedes combinarlos en un solo comando como `ls -la`. El orden de los flags a menudo no importa, así que `ls -al` funciona igual.

```bash
$ ls -la
```

Combinaciones útiles incluyen:

```bash
$ ls -lh
$ ls -la
$ ls -ltr
```

### Opciones Comunes de ls

- `-a`: Muestra todos los archivos, incluidos los ocultos.
- `-l`: Usa formato largo.
- `-h`: Muestra tamaños legibles para humanos con `-l`.
- `-r`: Invierte el orden de clasificación.
- `-t`: Ordena por tiempo de modificación.
- `-S`: Ordena por tamaño de archivo.
- `-d`: Lista el directorio en sí en lugar de su contenido.

### Preguntas Comunes

**¿Por qué algunos nombres de archivo comienzan con un punto?** Los archivos con punto están ocultos por defecto y a menudo almacenan configuraciones, como `.bashrc`.

**¿Cómo listo solo un directorio en sí?** Usa `ls -d directory/`.

**¿Cómo veo los archivos más nuevos al final?** Usa `ls -ltr`.

**¿Por qué ls muestra colores?** Muchos sistemas configuran `ls` para colorear tipos de archivo mediante un alias o configuración de entorno.

## Exercise

Practice makes perfect! Here is a hands-on lab to reinforce your understanding of the `ls` command:

- **[Linux ls Command: Content Listing](https://labex.io/es/labs/linux-linux-ls-command-content-listing-219205)** - Practice using the `ls` command to efficiently list and analyze file and directory contents. You'll learn various options for detailed listings, hidden file display, human-readable sizes, and sorting techniques to enhance your command-line skills.

This lab will help you apply the concepts in a real scenario and build confidence with directory listing in Linux.

## Quiz Question

¿Qué comando usarías para ver archivos ocultos? Por favor responde en inglés, prestando atención a la sensibilidad de mayúsculas y minúsculas.

## Quiz Answer

ls -a
