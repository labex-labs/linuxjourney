---
index: 14
lang: "es"
title: "find"
meta_title: "find - Línea de Comandos"
meta_description: "Aprende a usar el comando 'find' de Linux para localizar archivos y directorios. Descubre opciones básicas de búsqueda y mejora tus habilidades de gestión de archivos en Linux."
meta_keywords: "comando find de Linux, encontrar archivos Linux, búsqueda de directorios Linux, tutorial comando find, gestión de archivos Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

Con todos estos archivos que tenemos en el sistema, puede ser un poco agitado tratar de encontrar uno específico. Bueno, ¡hay un comando que podemos usar para eso: `find`!

```bash
find /home -name puppies.jpg
```

Con `find`, tendrás que especificar el directorio en el que buscarás y lo que estás buscando. En este caso, estamos tratando de encontrar un archivo con el nombre de `puppies.jpg`.

Puedes especificar qué tipo de archivo estás tratando de encontrar.

```bash
find /home -type d -name MyFolder
```

Puedes ver que configuré el tipo de archivo que estoy tratando de encontrar como `d` para directorio, y sigo buscando por el nombre de `MyFolder`.

Una cosa genial a tener en cuenta es que `find` no se detiene en el directorio que estás buscando; también buscará dentro de cualquier subdirectorio que ese directorio pueda tener.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión sobre cómo encontrar archivos y directorios en Linux:

1. **[Comando find de Linux: Búsqueda de archivos](https://labex.io/es/labs/linux-linux-find-command-file-searching-219191)** - Este laboratorio proporciona una introducción al comando `find`, una utilidad versátil para buscar y localizar archivos y directorios basándose en varios criterios. Practicarás el uso de `find` para localizar archivos específicos.
2. **[Descubrir recursos críticos del sistema](https://labex.io/es/labs/linux-discover-critical-system-resources-388032)** - Aprende comandos esenciales de Linux para localizar archivos y ejecutables, incluyendo `find`. Practicarás la navegación eficiente del sistema de archivos y el descubrimiento de recursos críticos del sistema.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza en el uso efectivo del comando `find`.

## Quiz Question

¿Qué opción debo especificar para `find` si quiero buscar por nombre?

## Quiz Answer

-name