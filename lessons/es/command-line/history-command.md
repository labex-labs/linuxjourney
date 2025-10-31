---
index: 9
lang: "es"
title: "historial"
meta_title: "historial - Línea de Comandos"
meta_description: "Domina el comando history en Linux para recordar y gestionar eficientemente tu actividad en la línea de comandos. Aprende a ver el historial, usar atajos como Ctrl-R y gestionar tu historial con opciones como history -c y history -d."
meta_keywords: "historial en linux, history -c linux, history -d linux, history -w linux, comando history unix, historial bash, línea de comandos, Ctrl-R, limpiar comando"
---

## Lesson Content

Su shell mantiene un registro de los comandos que ha introducido previamente. Puede acceder a esta lista, que es increíblemente útil cuando desea encontrar y reutilizar un comando sin tener que volver a escribirlo. El comando `history` es una herramienta fundamental en la mayoría de los entornos Unix y Linux.

### Visualización de su Historial de Comandos

Para ver la lista de comandos que ha utilizado, simplemente escriba el comando `history`. Esta función proporciona un registro detallado de su actividad, lo que facilita el seguimiento de su `history in linux`.

```bash
history
```

### Volver a Ejecutar Comandos Anteriores

El shell proporciona varios atajos para facilitar la reutilización de comandos.

- **Flecha Arriba**: ¿Desea ejecutar el mismo comando que acaba de hacer? Simplemente presione la tecla de flecha hacia arriba para desplazarse hacia atrás a través de su historial.
- **El Atajo `!!`**: Para ejecutar el comando más reciente de nuevo, puede usar `!!`. Por ejemplo, si acaba de ejecutar `cat file1`, escribir `!!` y presionar Enter ejecutará `cat file1` de nuevo.

### Búsqueda en su Historial

Uno de los atajos de historial más potentes es `Ctrl-R`. Esto inicia una búsqueda inversa. Después de presionar `Ctrl-R`, comience a escribir cualquier parte del comando que esté buscando, y el shell mostrará la coincidencia más reciente. Puede presionar `Ctrl-R` repetidamente para recorrer coincidencias más antiguas. Una vez que encuentre el comando que desea, simplemente presione Enter para ejecutarlo.

### Gestión de la Lista de Historial

Más allá de solo ver su historial, también puede gestionarlo directamente.

- **Borrar Historial**: Si desea borrar el historial de comandos para su sesión actual, puede usar el comando `history -c linux`. Esto elimina todas las entradas de la lista de historial en memoria.
- **Escribir en Archivo**: Para guardar el historial de la sesión actual en su archivo de historial (generalmente `~/.bash_history`), puede usar `history -w linux`. Esto es útil para conservar comandos antes de cerrar una sesión.
- **Eliminar una Entrada Específica**: Puede eliminar un solo comando de su historial usando `history -d <offset>`. El desplazamiento es el número que se muestra junto al comando en la salida de `history`. Por ejemplo, `history -d 101` eliminaría la entrada número 101. Esta es una función clave de `history -d linux`.

### Otras Herramientas Útiles de Terminal

A medida que su ventana de terminal se llena, es posible que desee limpiarla. Use el comando `clear` para borrar su pantalla y comenzar con una pantalla nueva.

```bash
clear
```

Otra característica indispensable es la autocompletación con la tecla Tab. Si comienza a escribir el principio de un comando, nombre de archivo o directorio y presiona la tecla Tab, el shell intentará autocompletarlo. Si hay varias posibilidades, puede mostrarle las opciones o no hacer nada. Presionar Tab una segunda vez a menudo listará todas las autocompletaciones posibles.

## Exercise

Si bien no hay laboratorios específicos para este tema, recomendamos explorar la ruta de aprendizaje integral de Linux [Linux Learning Path](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Cuál es el comando para limpiar la terminal? (Por favor, responda solo en letras minúsculas en inglés)

## Quiz Answer

clear
