---
index: 12
lang: "es"
title: "mkdir (Crear Directorio)"
meta_title: "mkdir (Crear Directorio) - Línea de Comandos"
meta_description: "Aprenda a usar el comando mkdir en Linux para crear un nuevo directorio. Esta guía cubre el comando de crear carpeta en Linux, incluyendo cómo crear múltiples directorios y directorios padre desde la línea de comandos."
meta_keywords: "crear directorio linux, comando mkdir en linux, crear directorio en linux, crear directorio línea de comandos, comando crear carpeta linux, mkdir, crear directorio, linux"
---

## Lesson Content

A medida que trabajas con archivos, necesitarás organizarlos en directorios. La herramienta principal para esta tarea es el comando `mkdir`, que significa "Make Directory" (Crear Directorio). Este comando te permite **crear un directorio en Linux** directamente desde tu terminal o **símbolo del sistema**.

### Creación de un Directorio Único

El uso más básico del **comando mkdir en Linux** es crear un nuevo directorio único. Si el directorio no existe, este comando lo creará en tu ubicación actual. Por ejemplo, para crear un directorio llamado `documents`:

```bash
mkdir documents
```

### Creación de Múltiples Directorios

También puedes crear varios directorios a la vez enumerando sus nombres, separados por espacios. Esta es una forma eficiente de configurar varias carpetas rápidamente.

```bash
mkdir books paintings
```

### Creación de Directorios Anidados

A veces necesitas crear un directorio y sus directorios padres simultáneamente. La opción `-p` (parent/padre) es perfecta para esto. Esta potente característica del **comando para crear carpetas en Linux** evita errores si los directorios padres no existen. Por ejemplo, para crear el directorio `favorites` dentro de `hemmingway`, que está dentro de `books`:

```bash
mkdir -p books/hemmingway/favorites
```

Este único comando crea `books`, `hemmingway` y `favorites` si no existen, demostrando una capacidad clave cuando necesitas **crear un directorio en Linux**.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la creación y gestión de directorios:

1. **[Comando mkdir de Linux: Creación de Directorios](https://labex.io/es/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprende a usar el comando `mkdir` en Linux para crear directorios, establecer permisos y organizar tu sistema de archivos. Este laboratorio cubre el uso básico y avanzado, incluida la creación de directorios anidados.
2. **[Configuración de una Nueva Estructura de Proyecto](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practica tus habilidades de gestión de directorios de Linux creando una estructura de proyecto específica y navegando a través de ella usando comandos esenciales como `mkdir` y `cd`.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza en la creación y organización de directorios en Linux.

## Quiz Question

¿Qué comando se utiliza para crear un directorio? Por favor, responda usando solo el comando en inglés en minúsculas.

## Quiz Answer

mkdir
