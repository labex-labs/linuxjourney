---
index: 7
lang: "es"
title: "paste"
meta_title: "paste - Text-Fu"
meta_description: "Aprende a usar el comando paste de Linux para fusionar líneas de archivos. Descubre delimitadores y combina archivos con este tutorial esencial del comando de Linux."
meta_keywords: "comando paste de Linux, tutorial del comando paste, fusionar líneas de archivos, comandos de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

El comando `paste` es similar al comando `cat`; fusiona líneas en un archivo. Creemos un nuevo archivo con el siguiente contenido:

```
sample2.txt
The
quick
brown
fox
```

Combinemos todas estas líneas en una sola línea:

```bash
paste -s sample2.txt
```

El delimitador predeterminado para `paste` es TAB, por lo que ahora hay una línea con TABs separando cada palabra.

Cambiemos este delimitador (`-d`) a algo un poco más legible:

```bash
paste -d ' ' -s sample2.txt
```

Ahora todo debería estar en una línea delimitada por espacios.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión del procesamiento de texto y la manipulación de datos en Linux:

1. **[Procesamiento de Texto Simple](https://labex.io/es/labs/linux-simple-text-processing-18004)** - Aprende a usar comandos potentes como `tr`, `col`, `join` y `paste` para manipular y analizar datos de texto de manera eficiente.
2. **[Redirección de Flujo de Datos](https://labex.io/es/labs/linux-data-stream-redirection-17995)** - Aprende el arte de la redirección de flujo en Linux y cómo manipular las entradas, salidas y flujos de error estándar, lo cual es fundamental para entender cómo operan comandos como `paste`.
3. **[Control de Secuencia y Tuberías](https://labex.io/es/labs/linux-sequence-control-and-pipeline-17994)** - Aprende a controlar las secuencias de ejecución de comandos y a utilizar tuberías, mejorando tu capacidad para combinar `paste` con otros comandos para tareas de datos complejas.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con el procesamiento y manejo de datos en Linux.

## Quiz Question

¿Qué bandera usas con `paste` para que todo quede en una sola línea?

## Quiz Answer

-s
