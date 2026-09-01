---
lesson_id: "text-editors-vim-or-emacs"
course_id: "advanced-text-fu"
lang: "es"
order_index: 2
title: "Editores de texto"
description: "Aprende a elegir y configurar un editor de texto de terminal para la administración y el desarrollo en Linux."
meta_title: "Editores de texto - Text-Fu avanzado"
meta_description: "Conoce editores de texto de Linux como Vim y Emacs, sus modelos de uso y su importancia para trabajar en terminales locales y remotos."
meta_keywords: "editores de texto Linux, Vim, Emacs, órdenes Linux, tutorial Linux, Linux para principiantes, guía Linux"
---

La configuración de Linux, los scripts, el código fuente y los registros suelen almacenarse como texto sin formato. Un editor de terminal permite trabajar con esos archivos desde una terminal local, una sesión SSH remota o un entorno sin escritorio gráfico.

## Elegir un editor para el entorno

No existe un único editor que sea el mejor para todas las personas o tareas. Los editores gráficos, los de terminal y los entornos de desarrollo integrados pueden ser apropiados. Para trabajar en la línea de órdenes, elige un editor que esté instalado, del que sepas salir con seguridad y cuyo modelo básico de edición comprendas.

No des por hecho que Vim o Emacs están instalados. Comprueba la resolución de órdenes en el shell actual:

```bash
$ command -v vim
/usr/bin/vim
$ command -v emacs
/usr/bin/emacs
```

Un resultado vacío con un estado distinto de cero significa que ese nombre no se encontró mediante la búsqueda de órdenes actual. Los sistemas mínimos pueden proporcionar `vi`, mientras que otros incluyen Nano o no tienen ningún editor interactivo.

:::single-choice{#editors-check-availability} ¿Qué orden comprueba si el shell actual puede resolver un ejecutable llamado `vim`?

::option[`vim --install`]{#editors-vim-install explanation="Vim no usa esta orden como comprobación portable de instalación y la instalación de paquetes depende de la distribución."}
::option[`file ~/.vimrc`]{#editors-file-vimrc explanation="Esto clasifica una ruta de configuración si existe; no determina si se puede resolver `vim`."}
::option[`command -v vim`]{#editors-command-v-vim .correct explanation="La orden integrada del shell comprueba la resolución de órdenes e imprime la forma resuelta cuando está disponible."}
:::

## Comprender el modelo de Vim

Vim es un editor modal. La misma tecla puede tener significados diferentes según el modo actual:

- El modo Normal interpreta las teclas como órdenes de navegación y edición.
- El modo Insertar introduce el texto escrito.
- El modo de línea de órdenes acepta órdenes como guardar o salir.

Este modelo hace eficiente la edición repetitiva con el teclado después de practicar, pero los usuarios nuevos deben tener presente el modo activo. Las lecciones posteriores presentan Vim una operación cada vez.

:::single-choice{#editors-vim-modal-meaning} ¿Qué significa que Vim sea modal?

::option[Cada archivo se abre en una ventana gráfica independiente.]{#editors-vim-windows explanation="Las ventanas y los búferes son conceptos distintos. Modal se refiere a cómo cambia el comportamiento de las teclas según el estado del editor."}
::option[Vim solo puede editar un tipo de archivo de texto a la vez.]{#editors-vim-file-type explanation="Vim admite muchos tipos de archivo. La palabra modal describe su modelo de interacción, no una restricción de archivos."}
::option[Las teclas realizan acciones diferentes según el modo activo.]{#editors-vim-modes .correct explanation="Por ejemplo, una tecla puede ejecutar una orden en el modo Normal, pero insertar texto en el modo Insertar."}
:::

## Comprender el modelo de Emacs

Emacs suele usar combinaciones de teclas y órdenes con nombre dentro de un entorno extensible. Los archivos se visitan en búferes, y los modos principales y secundarios adaptan el comportamiento a distintos contenidos y tareas. Emacs puede ejecutarse en una terminal o en un marco gráfico.

Tanto Vim como Emacs admiten mucho más que la edición básica mediante configuración y extensiones. Empieza por abrir, modificar, guardar y cerrar un archivo de texto sin formato antes de añadir personalizaciones.

:::single-choice{#editors-emacs-buffer} En la terminología de Emacs, ¿dónde se guarda normalmente el texto editable de un archivo visitado?

::option[En un búfer.]{#editors-emacs-buffer-answer .correct explanation="Emacs visita un archivo en un búfer, que contiene el texto que se está viendo o editando."}
::option[En la tabla de alias del shell.]{#editors-emacs-alias-table explanation="Los alias pertenecen a la resolución de órdenes del shell y no almacenan texto del editor."}
::option[Únicamente en el historial de desplazamiento de la terminal.]{#editors-emacs-scrollback explanation="El historial de la terminal registra la salida mostrada, mientras que Emacs gestiona el texto editable en búferes."}
:::

## Establecer un editor preferido

Muchos programas de la línea de órdenes consultan `VISUAL` o `EDITOR` cuando necesitan iniciar un editor. Por ejemplo, elige Vim para las órdenes iniciadas desde la sesión actual de Bash y sus procesos hijos:

```bash
$ export VISUAL=vim
$ export EDITOR="$VISUAL"
```

Estas variables expresan una preferencia; no instalan el programa. Usa una orden que exista realmente y añade las exportaciones al archivo de inicio apropiado del shell solo después de probarlas.

:::single-choice{#editors-editor-variable} ¿Qué hace `export EDITOR=vim`?

::option[Indica a los procesos hijos futuros que `vim` es el valor del editor preferido.]{#editors-export-preference .correct explanation="`export` coloca la preferencia en el entorno heredado por las órdenes iniciadas desde el shell actual."}
::option[Instala Vim para todos los usuarios del sistema.]{#editors-install-vim explanation="Asignar una variable de entorno no instala paquetes ni modifica los sistemas de otros usuarios."}
::option[Hace que todos los programas obedezcan las combinaciones de teclas de Vim.]{#editors-global-bindings explanation="Los programas pueden consultar la variable para iniciar un editor, pero esta no sustituye su propio modelo de interacción."}
:::

## Practicar sin poner en riesgo archivos importantes

Aprende con un archivo desechable en un directorio de tu propiedad:

```bash
$ printf 'first line\nsecond line\n' > editor-practice.txt
$ vim editor-practice.txt
```

No empieces con la configuración del sistema ni con datos de otro usuario. Haz una copia de seguridad antes de modificar un archivo importante, comprende cómo guardar y salir, y revisa el resultado con una orden de solo lectura como `cat` o `diff`.

:::single-choice{#editors-first-practice-file} ¿Cuál es el archivo inicial más seguro para practicar con un editor desconocido?

::option[Un archivo crítico de configuración del arranque abierto como root.]{#editors-boot-file explanation="Un cambio accidental podría impedir el inicio normal y el acceso elevado aumenta el impacto de los errores."}
::option[Un archivo de texto desechable en un directorio de tu propiedad.]{#editors-disposable-file .correct explanation="Un archivo de práctica limita las consecuencias de las ediciones accidentales mientras aprendes a navegar, guardar y salir."}
::option[Un archivo compartido de producción sin copia de seguridad.]{#editors-production-file explanation="Practicar sin revisión sobre datos compartidos puede perjudicar a otras personas y no ofrece una vía sencilla de recuperación."}
:::

Para practicar cómo abrir, editar y guardar archivos de texto desde la terminal, prueba este laboratorio práctico:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación y edición de archivos, el guardado y la navegación con vi/vim y nano, habilidades esenciales para cualquier usuario de Linux.

## Resumen

Ahora puedes elegir un editor de terminal y preparar un flujo de práctica seguro.

1. Comprueba si una orden de editor está disponible.
2. Reconoce el modelo de interacción modal de Vim.
3. Reconoce los búferes y modos extensibles de Emacs.
4. Establece una preferencia de editor sin confundirla con una instalación.
5. Practica con texto desechable antes de editar archivos importantes.
