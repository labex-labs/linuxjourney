---
index: 11
lang: "es"
title: "Navegación de búfer de Emacs"
meta_title: "Navegación de búfer de Emacs - Text-Fu Avanzado"
meta_description: "Aprenda los comandos de navegación de búfer de Emacs. Cambie, cierre y divida búferes de manera eficiente con este tutorial de Emacs para principiantes. ¡Mejore su flujo de trabajo!"
meta_keywords: "navegación de búfer Emacs, comandos Emacs, C-x b, C-x k, tutorial Linux, guía Emacs, Emacs para principiantes"
---

## Lesson Content

Para moverse entre búferes (o archivos que está visitando), use los siguientes comandos:

### Cambiar búferes

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### Cerrar el búfer

```
C-x k
```

### Dividir el búfer actual

```
C-x 2
```

Esto le permite ver múltiples búferes en una sola pantalla. Para moverse entre estos búferes, use: C-x o

### Establecer un solo búfer como la pantalla actual

```
C-x 1
```

Si alguna vez ha usado un multiplexor de terminal como `screen` o `tmux`, los comandos de búfer le resultarán muy familiares.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la navegación y manipulación de archivos de texto y búferes:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/es/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practique la creación, edición, guardado y navegación de texto dentro de los editores Vim y Nano, que son cruciales para trabajar con búferes.
2. **[Comando cat de Linux: Concatenación de archivos](https://labex.io/es/labs/linux-linux-cat-command-file-concatenating-210986)** - Aprenda a ver, concatenar y manipular archivos de texto, aplicando directamente cómo podría interactuar con el contenido del búfer.
3. **[Visualización de archivos de registro y configuración en Linux](https://labex.io/es/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - Practique el uso de comandos como `cat`, `more` y `less` para ver y navegar eficientemente por archivos de texto, simulando escenarios del mundo real de examen de contenido similar a un búfer.

Estos laboratorios le ayudarán a aplicar los conceptos en escenarios reales y a generar confianza con la manipulación de archivos de texto y búferes en Linux.

## Quiz Question

¿Cómo se elimina un búfer?

## Quiz Answer

C-x k
