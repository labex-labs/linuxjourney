---
index: 17
lang: "es"
title: "whatis"
meta_title: "whatis - Línea de Comandos"
meta_description: "Aprende el comando whatis de Linux con ejemplos para obtener descripciones de comandos en una línea desde las páginas man y entender múltiples secciones del manual."
meta_keywords: "comando whatis, linux whatis, descripción de comando linux, resumen página man, ayuda línea de comandos, apropos"
---

## Lesson Content

Al explorar la línea de comandos de Linux, encontrarás una gran cantidad de comandos. Es natural olvidar qué hace un comando específico. Afortunadamente, hay una utilidad sencilla que te puede ayudar.

### Qué es el comando whatis

El comando `whatis` muestra una descripción concisa, en una sola línea, de un comando directamente desde su página del manual. Es una forma rápida de obtener un recordatorio de la función principal de un comando sin leer toda la página man.

### Cómo usar el comando whatis

Usar `whatis` es sencillo. Escribe `whatis` seguido del comando sobre el que quieres saber.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### Entendiendo la salida

La descripción que proporciona `whatis` proviene de la sección `NAME` de la página del manual del comando. Si un nombre tiene varias páginas del manual en diferentes secciones, `whatis` puede mostrar más de una línea.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

El número entre paréntesis es la sección de la página man.

### Whatis vs Man vs Apropos

- `whatis ls`: Muestra una descripción en una línea para un nombre de comando exacto.
- `man ls`: Abre la página completa del manual.
- `apropos keyword`: Busca en las descripciones de las páginas man una palabra clave.

Por ejemplo:

```bash
$ apropos password
```

Usa `whatis` cuando conoces el nombre del comando pero olvidaste qué hace.

### Preguntas comunes

**¿Por qué whatis dice "nothing appropriate"?** El comando puede no tener una página man instalada, o la base de datos man puede necesitar actualización.

**¿Muestra whatis las opciones del comando?** No. Usa `man COMMAND` o `COMMAND --help` para ver las opciones.

**¿Es whatis lo mismo que which?** No. `whatis` describe un comando. `which` muestra la ruta del ejecutable.

## Exercise

¡La práctica hace al maestro! Aunque no hay un laboratorio específico para el comando `whatis`, entender cómo encontrar información sobre comandos y archivos es crucial. Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión sobre cómo localizar comandos y archivos en Linux:

1. **[Comando Linux which: Localización de Comandos](https://labex.io/es/labs/linux-linux-which-command-command-locating-215210)** - Practica usando el comando `which` para localizar archivos ejecutables y entender la prioridad de comandos en el PATH de tu sistema.
2. **[Comando Linux whereis: Encontrar Archivos y Comandos](https://labex.io/es/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - Aprende a usar `whereis` para encontrar el binario, el código fuente y las páginas del manual de comandos, profundizando en cómo están estructurados los comandos.
3. **[Descubre Recursos Críticos del Sistema](https://labex.io/es/labs/linux-discover-critical-system-resources-388032)** - Este desafío combina `which`, `whereis` y `find` para ayudarte a navegar eficientemente el sistema de archivos y descubrir recursos importantes del sistema.

Estos laboratorios te ayudarán a aplicar los conceptos de descubrimiento de comandos y archivos en escenarios reales y a ganar confianza con utilidades esenciales de Linux.

## Quiz Question

What command can you use to see a small description of a command? Please answer in English, paying attention to lowercase.

## Quiz Answer

whatis
