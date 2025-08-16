---
lang: "es"
title: "pwd (Imprimir Directorio de Trabajo)"
description: "Aprende a usar el comando 'pwd' en Linux para imprimir tu directorio de trabajo actual. Comprende las rutas del sistema de archivos de Linux y la navegación para principiantes."
keywords: "comando pwd, directorio Linux, directorio actual, ruta Linux, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

Todo en Linux es un archivo. A medida que te adentres en Linux, entenderás esto, pero por ahora, solo tenlo en cuenta. Cada archivo está organizado en un árbol de directorios jerárquico. El primer directorio en el sistema de archivos se llama apropiadamente directorio raíz. El directorio raíz tiene muchas carpetas y archivos, que pueden almacenar más carpetas y archivos, etc. Aquí hay un ejemplo de cómo se ve el árbol de directorios:

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

La navegación del sistema de archivos, al igual que en la vida real, es útil si sabes dónde estás y a dónde vas. Para ver dónde estás, puedes usar el comando `pwd`. Este comando significa "print working directory" (imprimir directorio de trabajo) y simplemente te muestra en qué directorio te encuentras. Ten en cuenta que la ruta se origina desde el directorio raíz.

```bash
pwd
```

¿Dónde estás? ¿Dónde estoy? Inténtalo.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Cómo encuentro en qué directorio me encuentro actualmente?

## Quiz Answer

pwd
