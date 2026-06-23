---
index: 9
lang: "es"
title: "history"
meta_title: "history - Línea de Comandos"
meta_description: "Aprende el comando history de Linux con ejemplos para ver el historial de comandos, volver a ejecutar comandos, búsqueda inversa, eliminar entradas y limpiar la terminal."
meta_keywords: "comando history linux, historial bash, history -c, history -d, history -w, Ctrl-R, historial de comandos, comando clear"
---

## Lesson Content

Tu shell mantiene un registro de los comandos que has ingresado previamente. Puedes acceder a esta lista cuando quieras encontrar y reutilizar un comando sin tener que volver a escribirlo. El comando `history` es una herramienta fundamental en Bash y muchos entornos de shell similares a Unix.

### Ver tu historial de comandos

Para ver la lista de comandos que has usado, escribe `history`.

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

Cada línea tiene un número de historial seguido por el comando.

### Volver a ejecutar comandos anteriores

El shell ofrece varios atajos para facilitar la reejecución de comandos.

- **Flecha arriba**: ¿Quieres ejecutar el mismo comando que acabas de usar? Simplemente presiona la tecla de flecha hacia arriba para recorrer hacia atrás tu historial.
- **El atajo `!!`**: Para ejecutar el comando más reciente nuevamente, puedes usar `!!`. Por ejemplo, si acabas de ejecutar `cat file1`, escribir `!!` y presionar Enter ejecutará `cat file1` otra vez.
- **Ejecutar por número**: Usa `!102` para ejecutar el comando número 102 de tu historial.
- **Ejecutar por prefijo**: Usa `!cat` para ejecutar el comando más reciente que comenzó con `cat`.

### Buscar en tu historial

Uno de los atajos más poderosos del historial es `Ctrl-R`. Esto inicia una búsqueda inversa. Después de presionar `Ctrl-R`, comienza a escribir cualquier parte del comando que buscas, y el shell mostrará la coincidencia más reciente. Puedes presionar `Ctrl-R` repetidamente para recorrer coincidencias más antiguas. Una vez que encuentres el comando que quieres, solo presiona Enter para ejecutarlo.

Si quieres editar el comando encontrado antes de ejecutarlo, presiona la tecla de flecha derecha o izquierda en lugar de Enter.

### Gestionar la lista de historial

Más allá de solo ver tu historial, también puedes gestionarlo directamente.

- **Borrar la lista de historial actual**: `history -c` elimina todas las entradas de la lista de historial en memoria.
- **Guardar el historial en un archivo**: `history -w` guarda el historial de la sesión actual en tu archivo de historial, usualmente `~/.bash_history`.
- **Eliminar una entrada específica**: `history -d <offset>` elimina un comando por su número de historial.

Ejemplos:

```bash
$ history -d 101
$ history -w
```

Ten cuidado con los comandos de expansión de historial como `!!` y `!102`. Usa primero `history` para confirmar qué se ejecutará.

### Otras herramientas útiles del terminal

A medida que tu ventana de terminal se llena, puede que quieras limpiarla. Usa el comando `clear` para borrar tu pantalla y comenzar con una pantalla limpia.

```bash
$ clear
```

Otra característica indispensable es la autocompletación con tabulador. Si comienzas a escribir el inicio de un comando, nombre de archivo o directorio y presionas la tecla Tab, el shell intentará autocompletarlo. Si hay múltiples posibilidades, puede mostrarte las opciones o no hacer nada. Presionar Tab una segunda vez a menudo listará todas las posibles completaciones.

### Preguntas comunes

**¿Dónde se almacena el historial de Bash?** Usualmente en `~/.bash_history`, aunque el comportamiento exacto depende de la configuración del shell.

**¿El historial incluye cada comando inmediatamente?** No siempre. Algunos shells escriben el historial cuando una sesión termina, a menos que esté configurado de otra forma.

**¿Puede el historial contener datos sensibles?** Sí. Evita escribir contraseñas, tokens o secretos directamente en los comandos.

**¿Cuál es la diferencia entre history -c y clear?** `history -c` borra el historial de comandos en memoria. `clear` solo limpia la pantalla del terminal.

## Exercise

While there are no specific labs for this topic, we recommend exploring the comprehensive [Linux Learning Path](https://labex.io/es/learn/linux) to practice related Linux skills and concepts.

## Quiz Question

What is the command to clear the terminal? (Please answer in lowercase English letters only)

## Quiz Answer

clear
