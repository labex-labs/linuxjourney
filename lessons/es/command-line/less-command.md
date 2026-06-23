---
index: 8
lang: "es"
title: "less"
meta_title: "less - Línea de Comandos"
meta_description: "Aprende el comando less de Linux con ejemplos para ver archivos grandes, desplazarte, buscar, saltar a líneas, seguir logs y salir de less."
meta_keywords: "comando less, linux less, ver archivo grande linux, buscar en less, salir de less, less -N, less +F, visor de texto linux"
---

## Lesson Content

Cuando ves archivos de texto que son demasiado grandes para caber en una sola pantalla, el comando `less` es una herramienta invaluable. Como dice el viejo dicho de Unix, "menos es más". Esto es un juego de palabras porque también existe un comando `more` con funcionalidad similar.

La utilidad `less` muestra texto en un formato paginado, permitiéndote navegar por un archivo sin saturar tu terminal.

### Comenzando con el comando Less

Para empezar a ver un archivo, usa `less` seguido del nombre del archivo.

```bash
$ less /home/pete/Documents/text1
```

Una vez dentro del visor `less`, tus comandos estándar de shell no funcionarán. En su lugar, usas un conjunto específico de teclas para navegar e interactuar con el texto.

### Navegación y Controles

Puedes usar varias teclas para moverte por el documento:

- **Teclas de Flecha y de Página**: Usa `Page Up`, `Page Down`, `Up` y `Down` para navegar línea por línea o página por página.
- **Ir al Inicio**: Presiona `g` para moverte directamente al comienzo del archivo de texto.
- **Ir al Final**: Presiona `G` (Shift + g) para saltar al final del archivo de texto.
- **Mover media página**: Presiona `u` para subir y `d` para bajar.
- **Menú de Ayuda**: Si olvidas los comandos mientras estás dentro de `less`, solo presiona `h` para mostrar un resumen útil.

### Buscar en Less

Una característica poderosa de `less` es su capacidad para buscar texto. Escribe `/` seguido del texto que quieres encontrar y luego presiona Enter.

- `/término_de_búsqueda`: Busca hacia adelante "término_de_búsqueda".
- `?término_de_búsqueda`: Busca hacia atrás "término_de_búsqueda".
- `n`: Salta a la siguiente ocurrencia del término de búsqueda.
- `N`: Salta a la ocurrencia anterior.

### Cómo salir de Less

Cuando termines de ver el archivo, necesitas saber cómo `salir de less` y volver a tu línea de comandos.

- **Salir**: Simplemente presiona `q` para salir del visor `less` y regresar a tu shell.

### Opciones útiles de less

Puedes iniciar `less` con opciones:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: Mostrar números de línea.
- `+G`: Abrir al final del archivo.
- `+F`: Seguir nuevo contenido a medida que se agrega, similar a `tail -f`.

Mientras sigues un archivo con `+F`, presiona `Ctrl-C` para dejar de seguir y volver a la navegación normal, luego presiona `q` para salir.

### Preguntas Comunes

**¿Es less mejor que cat?** Usa `cat` para archivos cortos y `less` para archivos largos o archivos que necesitas buscar.

**¿Cómo busco sin distinguir mayúsculas?** Inicia `less` con `-i`, o escribe búsquedas normalmente cuando el patrón no tiene letras mayúsculas en muchos sistemas.

**¿Puede less abrir la salida de un comando?** Sí. Pasa la salida por un pipe, como `dmesg | less`.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of viewing and navigating text files in Linux:

1. **[Linux less Command: File Paging](https://labex.io/es/labs/linux-linux-less-command-file-paging-214301)** - Learn the Linux 'less' command for efficient text file viewing and navigation, including search, line numbers, and pattern matching.
2. **[Linux more Command: File Scrolling](https://labex.io/es/labs/linux-linux-more-command-file-scrolling-214299)** - Learn the Linux 'more' command for efficient text file viewing, covering basic usage, starting from specific lines, and customizing display.
3. **[Viewing Log and Configuration Files in Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Learn essential Linux command-line skills for efficiently viewing and navigating text files, including system logs and configuration files, using commands like `cat`, `more`, and `less`.

These labs will help you apply the concepts in real scenarios and build confidence with text file manipulation and navigation.

## Quiz Question

¿Cómo se sale del comando `less`? Por favor, proporciona la tecla de un solo carácter como tu respuesta. Nota: la respuesta es una letra inglesa sensible a mayúsculas.

## Quiz Answer

q
