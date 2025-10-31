---
index: 2
lang: "es"
title: "pwd (Imprimir Directorio de Trabajo)"
meta_title: "pwd (Imprimir Directorio de Trabajo) - Línea de Comandos"
meta_description: "Domina el comando pwd de Linux para mostrar tu directorio actual. Esta lección explica el significado completo de pwd en Linux y cómo navegar por el árbol de directorios."
meta_keywords: "pwd linux, directorio actual linux, árbol de directorios en linux, significado de pwd en linux, imprimir directorio de trabajo, ruta linux, navegación linux, conceptos básicos de línea de comandos"
---

## Lesson Content

En Linux, un concepto central es que todo se trata como un archivo. Estos archivos están organizados dentro de una estructura jerárquica conocida como el sistema de archivos. Comprender esta estructura es clave para navegar por su sistema de manera efectiva.

### El Árbol de Directorios en Linux

Todo el sistema de archivos comienza a partir de un único directorio de nivel superior llamado directorio raíz, representado por una barra inclinada hacia adelante (`/`). Desde la raíz, el **árbol de directorios en linux** se ramifica en varios subdirectorios, que pueden contener archivos y más subdirectorios.

Aquí hay un ejemplo simplificado de cómo se ve esta estructura:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

### Comprensión de las Rutas de Archivos

La ubicación de cualquier archivo o directorio se describe mediante su ruta. Una ruta es una secuencia de directorios que conduce desde un punto de partida hasta un destino específico. Por ejemplo, si tiene una carpeta llamada `pete` dentro del directorio `/home`, y una carpeta `Movies` dentro de `pete`, la ruta completa sería `/home/pete/Movies`.

### ¿Cuál es la Forma Completa de PWD en Linux?

Al navegar por el sistema de archivos, es esencial conocer su ubicación actual. El comando para esto es `pwd`. La **forma completa de pwd en linux** es "print working directory" (imprimir directorio de trabajo). Su único propósito es mostrar la ruta completa del directorio en el que se encuentra actualmente, comenzando desde la raíz (`/`).

### Uso del Comando linux pwd

Para encontrar su **directorio actual linux**, simplemente escriba el comando **linux pwd** y presione Enter. Imprime la ruta absoluta de su ubicación actual en la línea de comandos.

```bash
pwd
```

¿Dónde estás? ¿Dónde estoy? Pruébalo para ver tu propio directorio de trabajo actual.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la navegación del sistema de archivos de Linux y la identificación de su ubicación actual:

1. **[Comando linux pwd: Visualización de Directorios](https://labex.io/es/labs/linux-linux-pwd-command-directory-displaying-209734)** - Este laboratorio proporciona una descripción general enfocada y el uso práctico del comando `pwd`, alineándose directamente con la introducción de la lección para encontrar su directorio actual.
2. **[Navegación de Directorios en Linux](https://labex.io/es/labs/linux-directory-navigation-387844)** - Ponga a prueba sus habilidades básicas de línea de comandos de Linux navegando a través de varios directorios, solidificando su comprensión de las rutas y la estructura del sistema de archivos.
3. **[Comando linux cd: Cambio de Directorio](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Aprenda a navegar eficientemente por su sistema de archivos usando el comando `cd`, comprendiendo diferentes técnicas para cambiar de directorio y explorar la estructura de archivos.

Estos laboratorios le ayudarán a aplicar los conceptos de jerarquía y navegación del sistema de archivos en escenarios reales y a ganar confianza con los comandos esenciales de Linux.

## Quiz Question

¿Qué comando se utiliza para encontrar el directorio en el que se encuentra actualmente? (Por favor, responda en inglés, usando solo el nombre del comando en minúsculas.)

## Quiz Answer

pwd
