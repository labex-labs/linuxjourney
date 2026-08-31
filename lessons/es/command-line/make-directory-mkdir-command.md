---
lesson_id: "make-directory-mkdir-command"
course_id: "command-line"
lang: "es"
order_index: 12
title: "mkdir (Crear directorio)"
description: "Aprende a crear directorios individuales, múltiples y anidados con las opciones de `mkdir`."
meta_title: "mkdir (Crear Directorio) - Línea de Comandos"
meta_description: "Aprende el comando mkdir de Linux con ejemplos para crear un directorio, múltiples directorios, directorios anidados y configurar permisos."
meta_keywords: "comando mkdir, linux mkdir, crear directorio linux, hacer directorio linux, mkdir -p, mkdir -m, crear carpeta linux"
---

Mientras trabajas con archivos, necesitarás organizarlos en directorios. La herramienta principal para esta tarea es el comando `mkdir`, que significa crear directorio.

La sintaxis básica es:

```bash
mkdir [OPTIONS] DIRECTORY...
```

## Creación de un directorio

El uso más básico de `mkdir` es crear un solo directorio nuevo. Si el directorio no existe ya, este comando lo crea en tu ubicación actual.

```bash
$ mkdir documents
```

Si ya existe un elemento llamado `documents`, `mkdir` muestra un error en vez de sustituirlo. Utiliza `ls -ld documents` para inspeccionar el elemento existente.

:::single-choice{#create-one-directory}
¿Qué orden crea un directorio llamado `documents` en el directorio de trabajo actual?

::option[`mkdir documents`]{#mkdir-documents .correct explanation="`mkdir` crea el directorio solicitado en la ruta relativa `documents`."}
::option[`touch documents`]{#touch-documents explanation="`touch` crea un archivo normal vacío cuando la ruta no existe. No crea un directorio."}
::option[`cd documents`]{#cd-documents explanation="`cd` intenta entrar en un directorio existente. No crea uno que falte."}
:::

## Creación de varios directorios

También puedes crear varios directorios a la vez listando sus nombres, separados por espacios. Esta es una forma eficiente de configurar múltiples carpetas rápidamente.

```bash
$ mkdir books paintings
```

:::single-choice{#create-separate-directories}
¿Qué orden crea dos directorios hermanos llamados `books` y `paintings`?

::option[`mkdir books/paintings`]{#nested-paintings explanation="Esta ruta describe `paintings` dentro de `books`, no dos directorios hermanos. También falla si `books` no existe."}
::option[`mkdir "books paintings"`]{#spaced-directory explanation="Las comillas combinan las palabras en una sola ruta, por lo que se solicita un único directorio cuyo nombre contiene un espacio."}
::option[`mkdir books paintings`]{#two-directories .correct explanation="Los operandos separados indican a `mkdir` que cree `books` y `paintings` como dos directorios."}
:::

## Creación de directorios padre ausentes

A veces necesitas crear un directorio y sus directorios padres simultáneamente. La opción `-p` es perfecta para esto. Evita errores si los directorios padres no existen.

```bash
$ mkdir -p books/hemingway/favorites
```

Esta orden crea las partes ausentes de la ruta. Tampoco muestra un error solo porque el directorio final ya exista, aunque sí pueden producirse otros errores, como la falta de permisos.

:::single-choice{#create-nested-path}
Todavía no existe ninguna parte de `projects/app/src`. ¿Qué orden crea la ruta de directorios completa?

::option[`mkdir -p projects/app/src`]{#mkdir-parents .correct explanation="La opción `-p` crea cada directorio padre ausente antes de crear el directorio final."}
::option[`mkdir projects/app/src`]{#mkdir-no-parents explanation="Sin `-p`, `mkdir` no puede crear `src` cuando los directorios intermedios no existen."}
::option[`mkdir -m projects/app/src`]{#mkdir-mode-missing explanation="La opción `-m` necesita un argumento de modo y no solicita la creación de los directorios padre ausentes."}
:::

## Configuración del modo inicial

Usa `-m` para establecer permisos mientras creas un directorio.

```bash
$ mkdir -m 755 public
```

Más adelante estudiarás los modos de permisos. En este ejemplo, el modo `755` concede al propietario permisos de lectura, escritura y búsqueda, mientras que el grupo y los demás reciben permisos de lectura y búsqueda.

Añade `-v` para mostrar un mensaje por cada directorio creado:

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

:::single-choice{#set-directory-mode}
¿Qué orden crea `public` con el modo de permisos `755`?

::option[`mkdir -p 755 public`]{#parents-755 explanation="La opción `-p` trata las palabras restantes como rutas de directorio, por lo que esta orden no establece el modo `755`."}
::option[`mkdir -v 755 public`]{#verbose-755 explanation="La opción `-v` muestra mensajes de creación. No interpreta `755` como un modo de permisos."}
::option[`mkdir -m 755 public`]{#mode-public .correct explanation="La opción `-m` recibe el modo solicitado y `public` es la ruta del directorio que se debe crear."}
:::

Para practicar la creación y organización de directorios, prueba estos laboratorios:

1. **[Comando Linux mkdir: Creación de Directorios](https://labex.io/es/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprende a usar el comando `mkdir` en Linux para crear directorios, establecer permisos y organizar tu sistema de archivos. Este laboratorio cubre uso básico y avanzado, incluyendo la creación de directorios anidados.
2. **[Configurando una Nueva Estructura de Proyecto](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practica tus habilidades de gestión de directorios en Linux creando una estructura específica de proyecto y navegando a través de ella usando comandos esenciales como `mkdir` y `cd`.

## Resumen

Ahora puedes crear estructuras de directorios con nombres, directorios padre y modos definidos de forma deliberada.

1. Crear uno o varios directorios con una sola orden.
2. Reconocer un error causado por una ruta ya existente.
3. Construir directorios padre ausentes con `-p`.
4. Establecer el modo de un directorio nuevo con `-m`.
