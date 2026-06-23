---
index: 12
lang: "es"
title: "mkdir (Crear Directorio)"
meta_title: "mkdir (Crear Directorio) - Línea de Comandos"
meta_description: "Aprende el comando mkdir de Linux con ejemplos para crear un directorio, múltiples directorios, directorios anidados y configurar permisos."
meta_keywords: "comando mkdir, linux mkdir, crear directorio linux, hacer directorio linux, mkdir -p, mkdir -m, crear carpeta linux"
---

## Lesson Content

Mientras trabajas con archivos, necesitarás organizarlos en directorios. La herramienta principal para esta tarea es el comando `mkdir`, que significa crear directorio.

La sintaxis básica es:

```bash
mkdir [OPTIONS] DIRECTORY...
```

### Creando un Directorio Único

El uso más básico de `mkdir` es crear un solo directorio nuevo. Si el directorio no existe ya, este comando lo crea en tu ubicación actual.

```bash
$ mkdir documents
```

### Creando Múltiples Directorios

También puedes crear varios directorios a la vez listando sus nombres, separados por espacios. Esta es una forma eficiente de configurar múltiples carpetas rápidamente.

```bash
$ mkdir books paintings
```

### Creando Directorios Anidados

A veces necesitas crear un directorio y sus directorios padres simultáneamente. La opción `-p` es perfecta para esto. Evita errores si los directorios padres no existen.

```bash
$ mkdir -p books/hemingway/favorites
```

Este único comando crea `books`, `hemingway` y `favorites` si no existen ya.

### Configurando Permisos de Directorio

Usa `-m` para establecer permisos mientras creas un directorio.

```bash
$ mkdir -m 755 public
```

Aprenderás más sobre permisos más adelante, pero este ejemplo crea un directorio que el propietario puede escribir y otros pueden leer y entrar.

### Opciones Comunes de mkdir

- `-p`: Crear directorios padres según sea necesario.
- `-m MODE`: Establecer permisos para el nuevo directorio.
- `-v`: Imprimir un mensaje para cada directorio creado.

Ejemplo:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### Preguntas Comunes

**¿Por qué mkdir dice "File exists"?** Un archivo o directorio con ese nombre ya existe. Usa `ls` para inspeccionarlo.

**¿Cómo creo directorios anidados?** Usa `mkdir -p parent/child/grandchild`.

**¿Puede mkdir crear archivos?** No. Usa `touch` para crear archivos vacíos.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión sobre la creación y gestión de directorios:

1. **[Comando Linux mkdir: Creación de Directorios](https://labex.io/es/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprende a usar el comando `mkdir` en Linux para crear directorios, establecer permisos y organizar tu sistema de archivos. Este laboratorio cubre uso básico y avanzado, incluyendo la creación de directorios anidados.
2. **[Configurando una Nueva Estructura de Proyecto](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practica tus habilidades de gestión de directorios en Linux creando una estructura específica de proyecto y navegando a través de ella usando comandos esenciales como `mkdir` y `cd`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza creando y organizando directorios en Linux.

## Quiz Question

¿Qué comando se usa para crear un directorio? Por favor responde usando solo el comando en inglés en minúsculas.

## Quiz Answer

mkdir
