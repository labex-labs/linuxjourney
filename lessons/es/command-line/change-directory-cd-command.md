---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "es"
order_index: 3
title: "cd (Cambiar directorio)"
description: "Aprende a usar `cd` con rutas y atajos para desplazarte por el sistema de archivos de Linux."
meta_title: "cd (Cambiar Directorio) - Línea de Comandos"
meta_description: "Aprende el comando cd de Linux con ejemplos para rutas absolutas, rutas relativas, atajos al directorio home, directorios padres y navegación al directorio anterior."
meta_keywords: "comando cd, comando cd linux, cambiar directorio, cd directorio padre, cd home, cd directorio anterior, ruta absoluta, ruta relativa"
---

Para moverte por el sistema de archivos de Linux, utilizas rutas que indican el destino. La herramienta principal para hacerlo es la orden `cd`, abreviatura de change directory (cambiar directorio). Esta orden cambia el directorio de trabajo actual de la shell.

El destino debe ser un directorio, no un archivo normal. Si el directorio no existe, escribes mal su nombre o careces de permiso para entrar, `cd` muestra un error en vez de cambiar de ubicación.

La sintaxis básica es:

```bash
cd [DIRECTORY]
```

## Cómo entender las rutas

Hay dos formas de especificar una ruta: absoluta y relativa.

- **Ruta absoluta**: La ruta completa que comienza desde el directorio raíz (`/`). Por ejemplo: `/home/pete/Desktop`.

- **Ruta relativa**: Una ruta basada en tu ubicación actual. Si estás en `/home/pete/Documents` y quieres acceder a un subdirectorio llamado `taxes`, puedes usar `taxes/`.

:::single-choice{#recognize-absolute-cd-path} ¿Qué afirmación describe correctamente una ruta absoluta?

::option[Comienza en el directorio que esté usando la shell en ese momento]{#begins-at-current-directory explanation="Una ruta que depende de la ubicación actual de la shell es relativa. No tiene por qué comenzar en la raíz."}
::option[Contiene únicamente el nombre del directorio final, sin sus directorios padre]{#contains-final-name-only explanation="Un único nombre de destino suele interpretarse en relación con el directorio actual. Una ruta absoluta incluye el recorrido desde `/`."}
::option[Comienza en el directorio raíz, representado por `/`]{#begins-at-root .correct explanation="Una ruta absoluta comienza en la raíz del sistema de archivos. La `/` inicial hace que su punto de partida no dependa del directorio actual."}
:::

## Uso de la orden cd

Para cambiar a un directorio específico usando una ruta absoluta, escribe:

```bash
$ cd /home/pete/Pictures
```

Este comando te mueve directamente al directorio `Pictures`.

Puedes confirmar tu ubicación con `pwd`:

```bash
$ pwd
/home/pete/Pictures
```

:::single-choice{#verify-changed-directory} ¿Qué orden confirma la ubicación actual de la shell después de ejecutar `cd`?

::option[`cd`]{#cd-command explanation="`cd` cambia el directorio actual, pero normalmente no muestra la ruta completa resultante. Utiliza `pwd` para confirmarla."}
::option[`ls`]{#ls-command explanation="`ls` muestra el contenido de un directorio. Puede ayudar a inspeccionar una ubicación, pero `pwd` informa de la propia ubicación."}
::option[`pwd`]{#pwd-command .correct explanation="`pwd` imprime el directorio de trabajo actual. Te permite comprobar adónde ha desplazado `cd` la shell."}
:::

## Navegación a un subdirectorio

Si ya estás en un directorio y quieres moverte a un subdirectorio, usa una ruta relativa. Por ejemplo, si tu ubicación actual es `/home/pete/Pictures` y contiene una carpeta llamada `Hawaii`, puedes navegar dentro de ella con:

```bash
$ cd Hawaii
```

Fíjate que solo usamos el nombre de la carpeta. Esto es porque ya estábamos en su directorio padre, `/home/pete/Pictures`.

## Atajos esenciales de navegación

Navegar con rutas completas puede ser tedioso. Afortunadamente, el shell proporciona varios atajos para hacer que moverse sea mucho más rápido.

- `.` (directorio actual): Representa el directorio en el que te encuentras actualmente.
- `..` (directorio padre): Te mueve un nivel arriba, al directorio que contiene al actual.
- `~` (directorio home): Un atajo a tu directorio personal home, como `/home/pete`.
- `-` (directorio anterior): Te lleva de vuelta al último directorio en el que estuviste.

Puedes usar estos atajos con `cd`:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

:::single-choice{#move-to-parent-directory} Desde `/home/pete/Pictures`, ¿qué orden te lleva a `/home/pete`?

::option[`cd .`]{#cd-current explanation="`.` representa el directorio actual. Esta orden deja la shell en `/home/pete/Pictures`."}
::option[`cd -`]{#cd-previous explanation="`-` vuelve al directorio de trabajo anterior, que no tiene por qué ser el padre. Utiliza `..` cuando el destino está un nivel por encima."}
::option[`cd ..`]{#cd-parent .correct explanation="`..` representa el padre del directorio actual. Desde `Pictures`, su padre es `/home/pete`."}
:::

:::single-choice{#return-to-previous-directory} ¿Qué orden vuelve al directorio que se utilizó inmediatamente antes del actual?

::option[`cd -`]{#previous-directory .correct explanation="`cd -` cambia al directorio de trabajo anterior. Ese directorio puede estar en cualquier lugar del sistema de archivos."}
::option[`cd ..`]{#parent-directory explanation="`cd ..` sube al directorio padre. El padre y el directorio anterior no siempre son la misma ubicación."}
::option[`cd ~`]{#home-directory explanation="`cd ~` te lleva al directorio personal. No registra el directorio que visitaste inmediatamente antes."}
:::

Experimenta con estos atajos para volverte más eficiente en la línea de comandos.

## Ejemplos prácticos de cd

Ve a tu directorio home:

```bash
$ cd
```

Ejecutar `cd` sin indicar un directorio también te lleva al directorio personal.

Sube dos niveles:

```bash
$ cd ../..
```

Ve a un directorio cuyo nombre contiene espacios citándolo:

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces} ¿Qué orden trata `Vacation Photos` como un único nombre de directorio?

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="Sin comillas, la shell pasa `Vacation` y `Photos` como argumentos separados, no como un único nombre de directorio."}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="Al entrecomillar toda la línea, la shell la trata como un único nombre de orden. La orden debe quedar fuera de las comillas de la ruta."}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="Las comillas agrupan las dos palabras en un único argumento de ruta para `cd`."}
:::

Regresa al directorio anterior:

```bash
$ cd -
/home/pete/Documents
```

Para reforzar tu comprensión de la navegación por directorios de Linux, prueba estos laboratorios prácticos:

1. **[Orden cd de Linux: cambiar directorio](https://labex.io/es/labs/linux-linux-cd-command-directory-changing-209733)** - Aprende a utilizar `cd` para navegar con eficacia por el sistema de archivos mediante distintas rutas y técnicas de desplazamiento.
2. **[Navegación por directorios de Linux](https://labex.io/es/labs/linux-directory-navigation-387844)** - Pon a prueba tus conocimientos básicos de la línea de comandos desplazándote por distintos directorios.
3. **[Configurar la estructura de un proyecto nuevo](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practica la gestión de directorios creando una estructura de proyecto y recorriéndola con órdenes como `mkdir` y `cd`.

## Resumen

Ahora puedes utilizar `cd` para desplazarte entre directorios mediante rutas completas y atajos de la shell.

1. Distinguir las rutas absolutas de las relativas.
2. Cambiar de directorio y comprobar el resultado con `pwd`.
3. Ir a los directorios padre, personal y anterior.
4. Entrar en directorios cuyos nombres contienen espacios.
5. Reconocer errores habituales de rutas y permisos.
