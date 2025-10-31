---
index: 9
lang: "es"
title: "Uso del Disco"
meta_title: "Uso del Disco - El Sistema de Archivos"
meta_description: "Aprenda a verificar el uso del disco y el espacio libre en Linux con los comandos df y du. Esta guía cubre cómo analizar el espacio en disco, incluido el uso de inodos con df -i linux, y encontrar qué archivos están ocupando espacio."
meta_keywords: "comando df, comando du, uso de disco Linux, verificar espacio libre, df -i linux, gestión de disco, tutorial Linux, utilización de disco, uso del sistema de archivos"
---

## Lesson Content

Gestionar el espacio en disco es una tarea fundamental para cualquier usuario o administrador de Linux. Dos comandos esenciales para este propósito son `df` y `du`. Exploremos cómo usarlos para monitorear eficazmente la utilización de su disco.

### Comprobación del Espacio del Sistema de Archivos con df

El comando `df` (disk free o espacio libre en disco) informa sobre la cantidad de espacio en disco utilizado y disponible en sus sistemas de archivos montados actualmente. Proporciona una visión general de alto nivel de su almacenamiento.

Para obtener un informe en un formato legible para humanos (por ejemplo, GB, MB, KB), use la opción `-h`:

```bash
pete@icebox:~$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1       6.2G  2.3G  3.6G  40% /
```

Esta salida muestra el dispositivo del sistema de archivos, el tamaño total, el espacio utilizado, el espacio disponible, el porcentaje de uso y dónde está montado.

### Análisis del Uso de Inodos

Además del espacio en bloques, los sistemas de archivos también utilizan inodos para almacenar metadatos sobre los archivos (como permisos, propiedad y ubicación). En raras ocasiones, puede quedarse sin inodos incluso si tiene espacio libre en disco. Para verificar el uso de inodos, puede usar el comando `df -i`. Ejecutar `df -i` en Linux le da una imagen clara de la asignación de inodos.

```bash
pete@icebox:~$ df -i
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda1      4128768 128768 4000000    4% /
```

### Resumen del Uso de Directorios con du

Cuando nota que un disco se está llenando, querrá identificar qué archivos o directorios están consumiendo más espacio. Para esta tarea, el comando `du` (disk usage o uso de disco) es la herramienta perfecta.

Ejecutar `du` sin argumentos muestra el uso de disco para cada subdirectorio en su ubicación actual. Usar la opción `-h` proporciona un resumen legible para humanos:

```bash
du -h
```

También puede especificar una ruta, como `du -h /home/pete`, para analizar un directorio específico. Ejecutarlo en el directorio raíz (`du -h /`) puede producir muchas salidas, por lo que a menudo es mejor verificar directorios específicos que sospeche que son grandes.

### df vs du Un Resumen Rápido

La sintaxis de `df` y `du` es tan similar que puede ser fácil confundirlas. Aquí hay una forma sencilla de recordar la diferencia:

- Use `df` para verificar cuánto **d**isco está **l**ibre en sus sistemas de archivos.
- Use `du` para verificar el **u**so de **d**isco de archivos y directorios específicos.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la gestión y utilización del espacio en disco en Linux:

1. **[Administrar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practique la creación, formateo y montaje de sistemas de archivos, que son las estructuras subyacentes reportadas por `df` y `du`.
2. **[Crear y Activar un Archivo de Intercambio (Swap) en Linux](https://labex.io/es/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Aprenda a administrar la memoria virtual en disco, un aspecto crítico de la gestión de recursos del sistema que afecta el espacio en disco.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza en la gestión de recursos de disco.

## Quiz Question

Qué comando se utiliza para mostrar cuánto espacio libre hay en su disco? Por favor, responda en letras minúsculas en inglés.

## Quiz Answer

df
