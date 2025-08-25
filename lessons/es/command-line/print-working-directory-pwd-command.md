---
index: 2
lang: "es"
title: "pwd (Imprimir Directorio de Trabajo)"
meta_title: "pwd (Imprimir Directorio de Trabajo) - Línea de Comandos"
meta_description: "Aprende a usar el comando 'pwd' en Linux para imprimir tu directorio de trabajo actual. Comprende las rutas del sistema de archivos de Linux y la navegación para principiantes."
meta_keywords: "comando pwd, directorio Linux, directorio actual, ruta Linux, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

Todo en Linux es un archivo. A medida que te adentres en Linux, entenderás esto, pero por ahora, tenlo en cuenta. Cada archivo está organizado en un árbol de directorios jerárquico. El primer directorio en el sistema de archivos se llama apropiadamente directorio raíz. El directorio raíz tiene muchas carpetas y archivos, que pueden almacenar más carpetas y archivos, etc. Aquí hay un ejemplo de cómo se ve el árbol de directorios:

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

La ubicación de estos archivos y directorios se conoce como rutas. Si tuvieras una carpeta llamada `home` con una carpeta dentro de ella llamada `pete` y otra carpeta dentro de esa carpeta llamada `Movies`, esa ruta se vería así: `/home/pete/Movies`. Bastante simple, ¿verdad?

La navegación del sistema de archivos, al igual que en la vida real, es útil si sabes dónde estás y a dónde vas. Para ver dónde estás, puedes usar el comando `pwd`. Este comando significa "print working directory" (imprimir directorio de trabajo) y simplemente te muestra en qué directorio te encuentras. Ten en cuenta que la ruta se origina en el directorio raíz.

```bash
pwd
```

¿Dónde estás? ¿Dónde estoy? Inténtalo.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de la navegación del sistema de archivos de Linux y la identificación de tu ubicación actual:

1. **[Comando Linux pwd: Visualización de directorios](https://labex.io/es/labs/linux-linux-pwd-command-directory-displaying-209734)** - Este laboratorio proporciona una visión general enfocada y el uso práctico del comando `pwd`, alineándose directamente con la introducción de la lección para encontrar tu directorio actual.
2. **[Navegación de directorios en Linux](https://labex.io/es/labs/linux-directory-navigation-387844)** - Pon a prueba tus habilidades básicas de línea de comandos de Linux navegando a través de varios directorios, solidificando tu comprensión de las rutas y la estructura del sistema de archivos.
3. **[Comando Linux cd: Cambio de directorio](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Aprende a navegar eficientemente por tu sistema de archivos usando el comando `cd`, comprendiendo diferentes técnicas para cambiar de directorio y explorar la estructura de archivos.

Estos laboratorios te ayudarán a aplicar los conceptos de jerarquía y navegación del sistema de archivos en escenarios reales y a generar confianza con los comandos esenciales de Linux.

## Quiz Question

¿Cómo encuentro en qué directorio me encuentro actualmente?

## Quiz Answer

pwd
