---
title: "historial"
description: "Aprenda a usar el comando history de Linux, el atajo !! y Ctrl-R para una recuperación eficiente de comandos. ¡Mejore su productividad en la terminal con estos consejos esenciales!"
keywords: "historial de Linux, historial de bash, Ctrl-R, comando clear, tutorial de Linux, línea de comandos, guía para principiantes"
---

## Lesson Content

En su shell, hay un historial de los comandos que ingresó previamente. De hecho, puede revisar estos comandos. Esto es bastante útil cuando desea encontrar y ejecutar un comando que usó anteriormente sin tener que escribirlo de nuevo.

```bash
history
```

¿Quiere ejecutar el mismo comando que hizo antes? Simplemente presione la flecha hacia arriba.

¿Quiere ejecutar el comando anterior sin escribirlo de nuevo? Use `!!`. Si escribió `cat file1` y quiere ejecutarlo de nuevo, puede simplemente escribir `!!` y ejecutará el último comando que ejecutó.

Otro atajo del historial es `Ctrl-R`. Este es el comando de búsqueda inversa. Si presiona `Ctrl-R` y comienza a escribir partes del comando que desea, le mostrará las coincidencias. Puede navegar por ellas presionando la tecla `Ctrl-R` de nuevo. Una vez que encuentre el comando que desea usar de nuevo, simplemente presione la tecla Enter.

Nuestra terminal se está desordenando un poco, ¿no? Hagamos una pequeña limpieza. Use el comando `clear` para limpiar su pantalla.

```bash
clear
```

Ahí, eso se ve mejor, ¿verdad?

Mientras hablamos de cosas útiles, una de las características más útiles en cualquier entorno de línea de comandos es el autocompletado con tabulador. Si comienza a escribir el principio de un comando, archivo, directorio, etc., y presiona la tecla Tab, se autocompletará según lo que encuentre en el directorio que está buscando, siempre y cuando no tenga otros archivos que comiencen con esas letras. Por ejemplo, si intentara ejecutar el comando `chrome`, puede escribir `chr` y presionar Tab, y se autocompletará a `chrome`.

## Exercise

Navegue por su historial de comandos anteriores con las teclas Arriba y Abajo. Juegue con la búsqueda inversa `Ctrl-R`.

## Quiz Question

¿Cuál es el comando para limpiar la terminal?

## Quiz Answer

clear
