---
index: 9
lang: "es"
title: "history"
meta_title: "history - Línea de Comandos"
meta_description: "Aprende a usar el comando history de Linux, el atajo !! y Ctrl-R para una recuperación eficiente de comandos. ¡Mejora tu productividad en la terminal con estos consejos esenciales!"
meta_keywords: "historial de Linux, historial de bash, Ctrl-R, comando clear, tutorial de Linux, línea de comandos, guía para principiantes"
---

## Lesson Content

En tu shell, hay un historial de los comandos que ingresaste previamente. Puedes revisar estos comandos. Esto es bastante útil cuando quieres encontrar y ejecutar un comando que usaste anteriormente sin tener que escribirlo de nuevo.

```bash
history
```

¿Quieres ejecutar el mismo comando que hiciste antes? Simplemente presiona la flecha hacia arriba.

¿Quieres ejecutar el comando anterior sin escribirlo de nuevo? Usa `!!`. Si escribiste `cat file1` y quieres ejecutarlo de nuevo, puedes simplemente escribir `!!` y ejecutará el último comando que corriste.

Otro atajo del historial es `Ctrl-R`. Este es el comando de búsqueda inversa. Si presionas `Ctrl-R` y empiezas a escribir partes del comando que quieres, te mostrará las coincidencias. Puedes navegar a través de ellas presionando la tecla `Ctrl-R` de nuevo. Una vez que encuentres el comando que quieres usar de nuevo, simplemente presiona la tecla Enter.

Nuestra terminal se está desordenando un poco, ¿no? Hagamos una pequeña limpieza. Usa el comando `clear` para limpiar tu pantalla.

```bash
clear
```

Ahí, eso se ve mejor, ¿verdad?

Mientras hablamos de cosas útiles, una de las características más útiles en cualquier entorno de línea de comandos es la completación por tabulación. Si empiezas a escribir el comienzo de un comando, archivo, directorio, etc., y presionas la tecla Tab, se autocompletará basándose en lo que encuentre en el directorio que estás buscando, siempre y cuando no tengas otros archivos que empiecen con esas letras. Por ejemplo, si intentaras ejecutar el comando `chrome`, puedes escribir `chr` y presionar Tab, y se autocompletará a `chrome`.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Cuál es el comando para limpiar la terminal?

## Quiz Answer

clear
