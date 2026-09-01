---
lesson_id: "vim-text-editor"
course_id: "advanced-text-fu"
lang: "es"
order_index: 3
title: "Vim (Vi Improved)"
description: "Aprende qué es Vim, su relación con vi y cómo abrir archivos, la ayuda y un tutorial guiado."
meta_title: "Vim (Vi Improved) - Text-Fu avanzado"
meta_description: "Descubre Vim, el potente y ligero editor de texto cuyo nombre significa Vi Improved. Aprende a abrir archivos, consultar la ayuda y practicar con seguridad."
meta_keywords: "Vim, Vi Improved, editor de texto Linux, tutorial Vim, editor vi, órdenes Linux"
---

Vim es un editor de texto configurable cuyo nombre significa **Vi Improved** (Vi mejorado). Conserva el modelo de edición modal asociado al editor `vi` original y añade funciones como deshacer en varios niveles, compatibilidad con sintaxis, scripts y un amplio sistema de ayuda.

## Relacionar Vim y vi

`vi` describe tanto un editor histórico como una interfaz de órdenes habitual. En un sistema Linux, `vi` puede iniciar Vim en un modo orientado a la compatibilidad; en otro, puede iniciar una implementación diferente de vi. No des por hecho que todas las órdenes `vi` ofrecen todas las funciones de Vim.

Comprueba qué resuelve el shell actual:

```bash
$ command -v vim
/usr/bin/vim
$ command -v vi
/usr/bin/vi
```

La ruta resuelta no permite por sí sola determinar si `vi` y `vim` son la misma implementación. `type -a vi vim` y la salida de versión del editor pueden proporcionar más detalles.

:::single-choice{#vim-name-origin} ¿Qué significa el nombre Vim?

::option[Visual Input Manager]{#vim-visual-input explanation="Esta expansión no es el origen del nombre del editor."}
::option[Virtual Interface Mode]{#vim-virtual-interface explanation="Vim usa modos, pero esta frase no es lo que representa su nombre."}
::option[Vi Improved]{#vim-vi-improved .correct explanation="Vim comenzó como un editor mejorado compatible con vi, algo que refleja su nombre."}
:::

:::single-choice{#vim-check-command} ¿Qué orden comprueba si Bash puede resolver actualmente el nombre `vim`?

::option[`vim --create`]{#vim-create-option explanation="Esta no es la comprobación de resolución del shell ni la forma de instalar o descubrir Vim."}
::option[`command -v vim`]{#vim-command-resolution .correct explanation="La orden integrada del shell muestra la orden que se usaría para ese nombre, si hay alguna disponible."}
::option[`file ~/.vimrc`]{#vim-file-vimrc explanation="Esto examina un posible archivo de configuración y no determina si el ejecutable de Vim está disponible."}
:::

## Abrir Vim y archivos

Inicia Vim con un búfer sin nombre:

```bash
$ vim
```

Proporciona una ruta para editar ese archivo:

```bash
$ vim filename.txt
```

Si `filename.txt` existe y puede leerse, Vim carga su contenido en un búfer. Si la ruta no existe, Vim abre un búfer nuevo asociado a ese nombre; no se crea ningún archivo hasta que guardas correctamente el búfer.

Vim no evita los permisos del sistema de archivos. Abrir un archivo no garantiza que tu cuenta pueda guardar cambios en su ruta.

:::single-choice{#vim-open-missing-path} ¿Qué ocurre normalmente cuando `vim draft.txt` indica una ruta que todavía no existe?

::option[Vim abre un búfer nuevo y crea el archivo únicamente cuando se guarda.]{#vim-new-buffer .correct explanation="La ruta se recuerda para el búfer, mientras que la creación en disco se aplaza hasta que se guarda correctamente."}
::option[Vim crea un archivo vacío en disco antes de abrir la interfaz.]{#vim-immediate-create explanation="El búfer nuevo se asocia a la ruta, pero el archivo no se crea hasta que se guarda correctamente."}
::option[Vim se niega a iniciar porque todas las rutas deben existir previamente.]{#vim-refuse-missing explanation="Vim puede abrir un búfer nuevo para una ruta inexistente y permitirte crear un archivo."}
:::

## Usar recursos de aprendizaje integrados

Si la instalación de Vim incluye `vimtutor`, ejecútalo desde el shell para iniciar una lección práctica interactiva:

```bash
$ vimtutor
```

Dentro de Vim, entra en el modo Normal con `Esc`, escribe `:help` y pulsa Intro para abrir el sistema de ayuda. Puedes añadir un tema concreto después de la orden:

```vim
:help user-manual
:help :write
```

Las etiquetas de ayuda son precisas, por lo que la puntuación puede importar. Usa `Ctrl+]` sobre un enlace de ayuda para seguirlo y `Ctrl+T` para volver.

:::single-choice{#vim-guided-tutorial} ¿Qué orden del shell inicia el tutorial guiado de Vim cuando está instalado?

::option[`vim --quiz`]{#vim-quiz-option explanation="Vim no usa esta opción como interfaz estándar de su tutorial guiado."}
::option[`vimtutor`]{#vim-tutor-command .correct explanation="`vimtutor` abre una copia del tutorial interactivo diseñado para practicar con seguridad."}
::option[`help vim`]{#vim-shell-help explanation="`help` de Bash documenta órdenes integradas del shell; no inicia el tutorial interactivo de Vim."}
:::

## Practicar con un archivo desechable

Empieza con un archivo en un directorio de tu propiedad:

```bash
$ printf 'alpha\nbeta\n' > vim-practice.txt
$ vim vim-practice.txt
```

Las lecciones siguientes presentan las búsquedas, la navegación, la inserción, la edición y el guardado. Hasta que sepas salir con seguridad, recuerda que `Esc` vuelve al modo Normal y que `:q!`, seguido de Intro, descarta los cambios no guardados de la ventana actual. Usa esta orden únicamente cuando quieras descartar esos cambios.

:::single-choice{#vim-abandon-practice-changes} En un archivo de práctica desechable, ¿qué orden de Vim cierra la ventana actual y descarta sus cambios sin guardar?

::option[`:w`]{#vim-write-only explanation="`:w` guarda el búfer, pero no cierra la ventana actual."}
::option[`:wq`]{#vim-write-quit explanation="`:wq` guarda los cambios antes de salir, por lo que no los descarta."}
::option[`:q!`]{#vim-quit-force .correct explanation="`!` indica a Vim que ignore el aviso de búfer modificado y salga sin guardar esos cambios."}
:::

Para practicar cómo abrir, editar y guardar con Vim, prueba este laboratorio práctico:

1. **[Editar archivos de texto en Linux con Vim y Nano](https://labex.io/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Practica la creación y edición de archivos, el guardado y la navegación con Vim y Nano en un entorno Linux real.

## Resumen

Ahora puedes identificar Vim, abrir un búfer y encontrar recursos de aprendizaje seguros.

1. Explica la relación entre Vim y vi sin dar por hecha una implementación.
2. Comprueba si la orden `vim` está disponible.
3. Abre un archivo existente o un búfer nuevo con nombre.
4. Inicia `vimtutor` o abre la ayuda integrada de Vim.
5. Descarta los cambios no guardados de una práctica solo cuando sea intencionado.
