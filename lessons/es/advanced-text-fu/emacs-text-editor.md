---
lesson_id: "emacs-text-editor"
course_id: "advanced-text-fu"
lang: "es"
order_index: 9
title: "Emacs"
description: "Aprende a iniciar Emacs, interpretar su notación de teclas y distinguir búferes, ventanas y marcos."
meta_title: "Emacs - Text-Fu avanzado"
meta_description: "Aprende los fundamentos de GNU Emacs, un editor de texto potente y extensible: búferes, ventanas, marcos, notación de teclas y tutorial integrado."
meta_keywords: "Emacs, editor de texto Linux, tutorial Emacs, búferes Emacs, órdenes Linux, principiante, guía"
---

GNU Emacs es un editor de texto extensible cuyo comportamiento puede personalizarse con Emacs Lisp. Admite la edición de texto sin formato, modos de programación, gestión de archivos y búferes y muchos paquetes opcionales. Puedes aprender sus órdenes básicas de edición sin adoptar todas las extensiones.

## Comprobar e iniciar Emacs

No des por hecho que Emacs está instalado. Comprueba cómo lo resuelve el shell:

```bash
$ command -v emacs
/usr/bin/emacs
```

Inicia Emacs con su selección normal de pantalla:

```bash
$ emacs
```

En una sesión gráfica, esto puede crear un marco gráfico. Usa `-nw`, abreviatura de *no window system*, cuando Emacs deba permanecer dentro de la terminal actual:

```bash
$ emacs -nw
```

:::single-choice{#emacs-terminal-start}
¿Qué orden inicia Emacs dentro de la terminal actual en vez de usar un sistema de ventanas gráfico?

::option[`emacs -w`]{#emacs-window-option explanation="Esta no es la forma documentada para prescindir del sistema de ventanas que se presenta aquí."}
::option[`emacs -nw`]{#emacs-no-window .correct explanation="La opción `-nw` indica a Emacs que no use un sistema de ventanas gráfico y se ejecute en la terminal."}
::option[`command -v emacs`]{#emacs-check-only explanation="Esto comprueba la resolución de la orden y no inicia el editor."}
:::

## Abrir un archivo

Proporciona una ruta para visitar un archivo al iniciar Emacs:

```bash
$ emacs notes.txt
```

Si el archivo existe, Emacs lo lee en un búfer. Si no existe, crea un búfer nuevo asociado a esa ruta; el archivo solo se crea después de guardarlo correctamente. Los permisos del sistema de archivos siguen determinando si se puede escribir.

:::single-choice{#emacs-open-file-buffer}
¿Qué hace normalmente `emacs notes.txt` cuando `notes.txt` todavía no existe?

::option[Abre un búfer nuevo asociado a esa ruta.]{#emacs-new-file-buffer .correct explanation="El búfer puede contener texto nuevo para `notes.txt`, mientras que la creación del archivo real se aplaza hasta guardarlo."}
::option[Crea el archivo en disco antes de iniciar el editor.]{#emacs-immediate-file explanation="Emacs puede asociar un búfer nuevo a la ruta sin crear el archivo en disco hasta que se guarde correctamente."}
::option[Se niega a iniciar porque todos los archivos visitados deben existir.]{#emacs-refuse-new-file explanation="Emacs permite crear archivos nuevos mediante búferes asociados a rutas inexistentes."}
:::

## Comprender búferes, ventanas y marcos

Emacs usa objetos relacionados pero distintos:

- Un **búfer** contiene texto u otro estado del editor. El contenido de un archivo visitado reside en un búfer.
- Una **ventana** es un área dentro de un marco de Emacs que muestra un búfer.
- Un **marco** es una pantalla de nivel superior de Emacs, como un marco gráfico o de terminal.

Pueden existir varios búferes sin ser visibles y dos ventanas pueden mostrar el mismo búfer. Cerrar una ventana no necesariamente elimina su búfer ni borra un archivo.

:::single-choice{#emacs-buffer-definition}
¿Qué es un búfer de Emacs?

::option[Un marco gráfico de aplicación de nivel superior.]{#emacs-buffer-frame explanation="Un marco es el objeto de visualización de nivel superior; un búfer contiene contenido o estado del editor."}
::option[Un objeto que contiene texto editable u otro estado del editor.]{#emacs-buffer-content .correct explanation="El contenido de los archivos visitados y muchas vistas que no son archivos residen en búferes de Emacs."}
::option[Un archivo del historial del shell con órdenes anteriores.]{#emacs-buffer-history explanation="El historial del shell está separado del almacenamiento de los búferes de Emacs."}
:::

## Leer la notación de teclas de Emacs

La documentación de Emacs usa una notación compacta:

- `C-x` significa mantener pulsado Control y pulsar `x`.
- `M-x` significa mantener pulsado Meta y pulsar `x`; Alt suele actuar como Meta en terminales y escritorios modernos.
- `C-x C-f` es una secuencia: pulsa Control+x y después Control+f.

La terminal concreta puede interceptar o reasignar algunas teclas. Pulsar `Esc` seguido de otra tecla puede sustituir a menudo una combinación con Meta.

:::single-choice{#emacs-key-sequence-notation}
¿Cómo se introduce la secuencia de teclas de Emacs escrita como `C-x C-f`?

::option[Mantén Control para `x` y después mantén Control para `f`.]{#emacs-control-x-f .correct explanation="Cada prefijo `C-` se aplica a la tecla siguiente y las dos combinaciones se introducen en secuencia."}
::option[Escribe los caracteres literales `C-x C-f` en el búfer.]{#emacs-literal-key-text explanation="La notación describe eventos de teclas de control, no texto que deba insertarse."}
::option[Mantén Control, `x` y `f` simultáneamente como una única combinación.]{#emacs-simultaneous-x-f explanation="La notación contiene dos combinaciones sucesivas, no una sola combinación de tres teclas."}
:::

## Iniciar el tutorial integrado

Dentro de Emacs, escribe `C-h t` para abrir el tutorial interactivo. Enseña desplazamiento, inserción, guardado y salida en un búfer de práctica seguro. `C-h` es el prefijo de ayuda; `C-h C-h` muestra ayuda sobre cómo usar la ayuda.

Si Emacs muestra un menú o un búfer de bienvenida, el tutorial sigue siendo un punto de partida más estructurado que experimentar con un archivo importante.

:::single-choice{#emacs-open-tutorial}
¿Qué secuencia de teclas de Emacs abre el tutorial integrado?

::option[`C-x C-s`]{#emacs-save-buffer explanation="Esta secuencia guarda el búfer actual; no abre el tutorial."}
::option[`C-x C-c`]{#emacs-exit-sequence explanation="Esta secuencia inicia la salida de Emacs en vez de comenzar una lección."}
::option[`C-h t`]{#emacs-help-tutorial .correct explanation="El prefijo de ayuda `C-h` seguido de `t` inicia el tutorial de Emacs."}
:::

## Resumen

Ahora puedes iniciar Emacs e interpretar los conceptos fundamentales de su interfaz.

1. Comprueba si la orden `emacs` está disponible.
2. Elige entre ejecución gráfica o en la terminal con `-nw`.
3. Visita una ruta existente o nueva en un búfer.
4. Distingue búferes, ventanas y marcos.
5. Lee la notación de teclas y abre el tutorial integrado.
