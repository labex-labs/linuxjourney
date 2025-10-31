---
index: 8
lang: "es"
title: "less"
meta_title: "less - Línea de Comandos"
meta_description: "Domina el comando less de Linux para una visualización eficiente de archivos de texto. Esta guía cubre cómo usar el comando less, navegar, realizar una búsqueda unix less y cómo salir de less."
meta_keywords: "comando less, less comando, salir less, búsqueda unix less, linux less, ver archivos de texto, navegar archivos, línea de comandos linux"
---

## Lesson Content

Cuando se visualizan archivos de texto que son demasiado grandes para caber en una sola pantalla, el `comando less` es una herramienta invaluable. Como dice el viejo dicho de Unix: "less is more" (menos es más). (Esto es un juego de palabras con el hecho de que también existe un comando `more` con funcionalidad similar). La utilidad `less` muestra el texto en formato paginado, lo que le permite navegar por un archivo página por página sin cargar el archivo completo en la memoria.

### Primeros pasos con el comando Less

Para empezar a ver un archivo, simplemente use el `comando less` seguido del nombre del archivo. Esto abrirá el archivo en la interfaz de `less`.

```bash
less /home/pete/Documents/text1
```

Una vez que esté dentro del visor `less`, sus comandos estándar de shell no funcionarán. En su lugar, utiliza un conjunto específico de teclas para navegar e interactuar con el texto.

### Navegación y Controles

Puede usar varias teclas para moverse por el documento:

- **Teclas de Flecha y de Página**: Use `Page Up`, `Page Down`, `Up` (Arriba) y `Down` (Abajo) para navegar línea por línea o página por página.
- **Ir al Inicio**: Presione `g` para moverse directamente al principio del archivo de texto.
- **Ir al Final**: Presione `G` (Shift + g) para saltar al final del archivo de texto.
- **Menú de Ayuda**: Si olvida los comandos mientras está en `less`, simplemente presione `h` para mostrar un resumen útil.

### Búsqueda Unix con Less

Una característica poderosa de `less` es su capacidad para buscar texto. Para realizar una `búsqueda unix less`, escriba `/` seguido del texto que desea encontrar y luego presione Enter. Esto resaltará todas las ocurrencias de su término de búsqueda.

- `/termino_busqueda`: Busca hacia adelante "termino_busqueda".
- `?termino_busqueda`: Busca hacia atrás "termino_busqueda".
- `n`: Salta a la siguiente ocurrencia del término de búsqueda.
- `N`: Salta a la ocurrencia anterior.

### Cómo Salir de Less

Cuando haya terminado de ver el archivo, debe saber cómo `salir de less` y volver a su indicador de comandos.

- **Salir**: Simplemente presione `q` para salir del visor `less` y volver a su shell.

Dominar el `comando less` es una habilidad fundamental para cualquiera que trabaje en la línea de comandos de Linux, haciendo que la inspección de archivos sea mucho más eficiente.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la visualización y navegación de archivos de texto en Linux:

1. **[Comando Linux less: Paginación de Archivos](https://labex.io/es/labs/linux-linux-less-command-file-paging-214301)** - Aprenda el comando 'less' de Linux para la visualización y navegación eficiente de archivos de texto, incluyendo búsqueda, números de línea y coincidencia de patrones.
2. **[Comando Linux more: Desplazamiento de Archivos](https://labex.io/es/labs/linux-linux-more-command-file-scrolling-214299)** - Aprenda el comando 'more' de Linux para la visualización eficiente de archivos de texto, cubriendo el uso básico, el inicio desde líneas específicas y la personalización de la visualización.
3. **[Visualización de Archivos de Registro y Configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Aprenda habilidades esenciales de la línea de comandos de Linux para ver y navegar eficientemente por archivos de texto, incluidos registros del sistema y archivos de configuración, utilizando comandos como `cat`, `more` y `less`.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la manipulación y navegación de archivos de texto.

## Quiz Question

¿Cómo se sale del comando `less`? Por favor, proporcione la tecla de un solo carácter como respuesta. Nota: la respuesta es una letra inglesa sensible a mayúsculas y minúsculas.

## Quiz Answer

q
