---
index: 7
lang: "es"
title: "cat"
meta_title: "cat - Línea de Comandos"
meta_description: "Aprende el comando cat de Linux con ejemplos para ver archivos, concatenar archivos, numerar líneas, crear archivos y usar redirección de forma segura."
meta_keywords: "comando linux cat, comando cat, ver archivo linux, concatenar archivos, cat -n, cat -b, redirección cat, linux cat"
---

## Lesson Content

Después de aprender a navegar por el sistema de archivos, el siguiente paso es ver el contenido de los archivos. Una herramienta fundamental y versátil para esto es el comando `cat`. El nombre `cat` es una abreviatura de "concatenate" (concatenar), lo que indica su capacidad para enlazar archivos.

### Ver el Contenido de Archivos

El uso más básico del comando `cat` es mostrar el contenido de un solo archivo directamente en tu terminal.

```bash
$ cat myfile.txt
```

Este comando imprimirá todo el contenido de `myfile.txt` en la pantalla. Aunque esto es perfecto para archivos de configuración cortos o fragmentos de texto, no es ideal para ver archivos grandes, ya que el texto se desplazará muy rápido. Cubriremos herramientas más adecuadas para archivos grandes en una lección posterior.

### Concatenar Archivos

Fiel a su nombre, `cat` puede combinar, o concatenar, múltiples archivos y mostrar su salida combinada. Lee los archivos en el orden en que se proporcionan y los imprime secuencialmente.

```bash
$ cat dogfile birdfile
```

Este comando mostrará primero el contenido de `dogfile`, seguido inmediatamente por el contenido de `birdfile`.

Para guardar la salida combinada en un nuevo archivo, usa la redirección:

```bash
$ cat dogfile birdfile > animals
```

### Crear Archivos con Redirección

También puedes usar `cat` con el operador de redirección de salida (`>`) para crear archivos nuevos. Esta es una forma rápida de escribir texto en un archivo directamente desde tu terminal.

```bash
$ cat > newfile.txt
```

Después de ejecutar este comando, puedes escribir tu texto. Presiona `Ctrl+D` en una nueva línea para guardar y salir. Esto creará `newfile.txt` con el texto que ingresaste. Ten cuidado, ya que usar `>` en un archivo existente lo sobrescribirá completamente.

Para agregar texto a un archivo en lugar de sobrescribirlo, usa `>>`.

```bash
$ cat >> notes.txt
```

### Opciones Comunes del Comando cat

El comando `cat` tiene varias opciones para modificar su comportamiento.

- `-n`: Numera todas las líneas de salida, comenzando desde 1.
- `-b`: Numera solo las líneas de salida que no están vacías.
- `-s`: Comprime múltiples líneas en blanco en una sola línea en blanco.
- `-A`: Muestra caracteres no imprimibles, tabulaciones y finales de línea.

Ejemplos:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

### Cuándo No Usar cat

Usa `cat` para archivos cortos. Para archivos largos, usa `less` para poder desplazarte, buscar y salir sin saturar tu terminal.

```bash
$ less /var/log/syslog
```

### Preguntas Comunes

**¿Qué significa cat?** Significa concatenar.

**¿Puede cat editar un archivo?** No de forma interactiva. Puede crear o sobrescribir archivos con redirección, pero un editor de texto es mejor para editar.

**¿Cuál es la diferencia entre > y >>?** `>` sobrescribe un archivo. `>>` agrega al final de un archivo.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing file contents:

1. **[Linux cat Command: File Concatenating](https://labex.io/es/labs/linux-linux-cat-command-file-concatenating-210986)** - Learn the `cat` command for viewing, concatenating, and manipulating text files, enhancing your command-line skills for efficient text file handling.
2. **[Viewing Log and Configuration Files in Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practice using commands like `cat` to efficiently view and navigate text files, including system logs and configuration files, to extract critical information.

These labs will help you apply the concepts in real scenarios and build confidence with file content viewing in Linux.

## Quiz Question

¿Qué comando se usa para mostrar el contenido de un archivo en la línea de comandos? (Nota: Tu respuesta debe ser una sola palabra en inglés, en minúsculas.)

## Quiz Answer

cat
