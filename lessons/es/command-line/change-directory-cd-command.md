---
index: 3
lang: "es"
title: "cd (Cambiar Directorio)"
meta_title: "cd (Cambiar Directorio) - Línea de Comandos"
meta_description: "Aprende el comando cd de Linux con ejemplos para rutas absolutas, rutas relativas, atajos al directorio home, directorios padres y navegación al directorio anterior."
meta_keywords: "comando cd, comando cd linux, cambiar directorio, cd directorio padre, cd home, cd directorio anterior, ruta absoluta, ruta relativa"
---

## Lesson Content

Para moverte por el sistema de archivos de Linux, usas rutas para especificar tu destino. La herramienta principal para esto es el comando `cd`, abreviatura de cambiar directorio. Cambia el directorio de trabajo actual del shell.

La sintaxis básica es:

```bash
cd [DIRECTORY]
```

### Entendiendo las Rutas

Hay dos formas de especificar una ruta: absoluta y relativa.

- **Ruta absoluta**: La ruta completa que comienza desde el directorio raíz (`/`). Por ejemplo: `/home/pete/Desktop`.

- **Ruta relativa**: Una ruta basada en tu ubicación actual. Si estás en `/home/pete/Documents` y quieres acceder a un subdirectorio llamado `taxes`, puedes usar `taxes/`.

### Usando el Comando cd

Para cambiar a un directorio específico usando una ruta absoluta, escribe:

```bash
$ cd /home/pete/Pictures
```

Este comando te mueve directamente al directorio `Pictures`.

Puedes confirmar tu ubicación con `pwd`:

```bash
$ pwd
/home/pete/Pictures
```

### Navegando a un Subdirectorio

Si ya estás en un directorio y quieres moverte a un subdirectorio, usa una ruta relativa. Por ejemplo, si tu ubicación actual es `/home/pete/Pictures` y contiene una carpeta llamada `Hawaii`, puedes navegar dentro de ella con:

```bash
$ cd Hawaii
```

Fíjate que solo usamos el nombre de la carpeta. Esto es porque ya estábamos en su directorio padre, `/home/pete/Pictures`.

### Atajos Esenciales para Navegar

Navegar con rutas completas puede ser tedioso. Afortunadamente, el shell proporciona varios atajos para hacer que moverse sea mucho más rápido.

- `.` (directorio actual): Representa el directorio en el que te encuentras actualmente.
- `..` (directorio padre): Te mueve un nivel arriba, al directorio que contiene al actual.
- `~` (directorio home): Un atajo a tu directorio personal home, como `/home/pete`.
- `-` (directorio anterior): Te lleva de vuelta al último directorio en el que estuviste.

Puedes usar estos atajos con `cd`:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

Experimenta con estos atajos para volverte más eficiente en la línea de comandos.

### Ejemplos Prácticos de cd

Ve a tu directorio home:

```bash
$ cd
```

Sube dos niveles:

```bash
$ cd ../..
```

Ve a un directorio cuyo nombre contiene espacios citándolo:

```bash
$ cd "Vacation Photos"
```

Regresa al directorio anterior:

```bash
$ cd -
/home/pete/Documents
```

### Preguntas Comunes

**¿Por qué cd dice "No such file or directory"?** La ruta no existe desde tu ubicación actual, o el nombre fue escrito incorrectamente. Usa `ls` para listar los directorios disponibles.

**¿Por qué cd dice "Permission denied"?** No tienes permiso para entrar en ese directorio.

**¿Qué pasa cuando ejecuto cd sin argumentos?** Te lleva a tu directorio home.

**¿Funciona cd con archivos?** No. `cd` cambia a directorios, no a archivos regulares.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of Linux directory navigation:

1. **[Linux cd Command: Directory Changing](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Learn the Linux `cd` command to efficiently navigate your file system, including various techniques for changing directories, understanding paths, and exploring the file structure.
2. **[Linux Directory Navigation](https://labex.io/es/labs/linux-directory-navigation-387844)** - Put your basic Linux command-line skills to the test by navigating through directories using essential commands.
3. **[Setting Up a New Project Structure](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts in real scenarios and build confidence with navigating the Linux filesystem.

## Quiz Question

If you are in `/home/pete/Pictures` and want to navigate to the parent directory (`/home/pete`), what is the full command you should use? Please answer in English, paying attention to case and spacing.

## Quiz Answer

cd ..
