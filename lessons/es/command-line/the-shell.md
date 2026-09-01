---
lesson_id: "the-shell"
course_id: "command-line"
lang: "es"
order_index: 1
title: "La shell"
description: "Aprende qué es la shell de Linux y cómo se ejecutan las órdenes."
meta_title: "La Shell - Línea de Comandos"
meta_description: "Aprende qué es la shell de Linux, cómo funciona el prompt de Bash y cómo ejecutar tu primer comando con ejemplos amigables para principiantes."
meta_keywords: "shell de linux, shell bash, línea de comandos, terminal linux, prompt de shell, comando echo, comandos básicos de linux"
---

## Qué es la shell de Linux

¡Bienvenido a tu viaje por Linux! El primer paso es entender la shell de Linux. Una shell es un programa que acepta las órdenes que escribes, solicita al sistema operativo que las ejecute y después muestra el resultado en la terminal.

Si has utilizado una interfaz gráfica, estarás acostumbrado a hacer clic en ventanas, menús y botones. En la línea de comandos, en cambio, escribes instrucciones precisas. Las aplicaciones llamadas «Terminal», «Consola» o «Konsole» suelen abrir una sesión de shell.

La terminal es la ventana o aplicación donde escribes, mientras que la shell es el programa que se ejecuta en su interior.

La shell resulta útil porque es rápida, se puede automatizar con scripts y está disponible en casi todos los sistemas Linux. A medida que aprendas más órdenes, podrás combinarlas para inspeccionar archivos, gestionar directorios, buscar texto, instalar software y automatizar tareas repetitivas.

:::single-choice{#distinguish-shell-and-terminal} ¿Qué afirmación describe correctamente la relación entre una terminal y una shell?

::option[La terminal proporciona la ventana y la shell se ejecuta en su interior.]{#shell-runs-in-terminal .correct explanation="La terminal es la interfaz que utilizas y la shell es el programa que procesa órdenes en su interior."}
::option[La terminal acepta las órdenes y la shell solo muestra el resultado.]{#terminal-accepts-commands explanation="Esta opción invierte sus funciones. La terminal proporciona la interfaz, mientras que la shell acepta y ejecuta las órdenes."}
::option[La terminal y la shell son dos nombres para el mismo programa.]{#terminal-equals-shell explanation="Trabajan juntas, pero no son el mismo programa. Una terminal abre una sesión dentro de la cual se ejecuta una shell."}
:::

## Interacción con la shell Bash

En este curso nos centraremos en Bash, abreviatura de Bourne Again Shell. Bash es una de las shells de Linux más comunes y constituye una buena base aunque más adelante utilices `zsh`, `fish` u otra shell.

Al abrir una terminal, te recibirá el prompt de la shell. Su aspecto puede variar, pero suele mostrar el nombre de usuario, el nombre del equipo y el directorio actual.

```plaintext
pete@icebox:/home/pete $
```

El símbolo `$` indica que la shell está lista para aceptar la entrada de un usuario normal. No debes escribir este símbolo al introducir órdenes; lo muestra la propia shell. Si ves `#` en su lugar, normalmente estás trabajando como root, un usuario con más poder y también más riesgos.

:::single-choice{#interpret-dollar-prompt} ¿Qué indica el símbolo `$` al final del prompt del ejemplo?

::option[La shell se ejecuta con los privilegios del usuario root.]{#root-user-ready explanation="Un prompt de root suele terminar en `#`, no en `$`. El acceso como root conlleva más poder y también más riesgos."}
::option[La shell espera la entrada de un usuario normal.]{#normal-user-ready .correct explanation="El símbolo `$` identifica un prompt de usuario normal e indica que la shell está lista para recibir una orden."}
::option[La siguiente orden debe comenzar con un signo de dólar.]{#type-dollar-first explanation="El símbolo `$` forma parte del prompt. Debes escribir la orden que aparece después sin copiar ese símbolo."}
:::

Las órdenes suelen seguir este patrón:

```bash
command options arguments
```

Por ejemplo, en `echo Hello World`, `echo` es la orden y `Hello World` es el texto que se le pasa.

:::single-choice{#identify-command-name} En `echo Hello World`, ¿qué parte es el nombre de la orden?

::option[`Hello`]{#hello-command explanation="`Hello` aparece después del nombre de la orden, por lo que forma parte del texto que se pasa a `echo`."}
::option[`World`]{#world-command explanation="`World` también es texto que se pasa a `echo`, no el nombre de la orden que se ejecuta."}
::option[`echo`]{#echo-command .correct explanation="`echo` nombra el programa que debe ejecutar la shell. Las palabras que le siguen se pasan al programa como argumentos."}
:::

## Tu primera orden de Linux

Empecemos con una de las órdenes de Linux más básicas para principiantes: `echo`. Esta orden muestra en la terminal el texto que le proporciones.

```bash
$ echo Hello World
Hello World
```

Prueba algunos ejemplos más:

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

Las comillas son útiles cuando quieres que la shell trate varias palabras como un único fragmento de texto.

:::single-choice{#group-words-with-quotes} ¿Qué orden hace que la shell trate `Hello from Bash` como un único fragmento de texto entre comillas?

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="Las comillas agrupan las tres palabras en un único argumento que se pasa a `echo`."}
::option[`echo Hello from Bash`]{#unquoted-words explanation="Esta orden muestra las mismas palabras, pero la shell las trata como argumentos separados porque no están entre comillas."}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="Al entrecomillar toda la línea, la shell busca una orden con ese nombre completo en vez de ejecutar `echo` con texto."}
:::

Para practicar estas habilidades, explora la completa [![Ruta de aprendizaje de la shell](https://labex.io/cdn-cgi/image/width=20,height=20,quality=80,format=auto,onerror=redirect/https://file.labex.io/path/FaVTnI4iqZP0.png)Ruta de aprendizaje de la shell](https://labex.io/es/learn/shell).

## Consejos habituales para principiantes

- Pulsa `Enter` para ejecutar una orden.
- Usa la tecla `Up Arrow` para recuperar una orden anterior.
- En Linux, las órdenes y los nombres de archivo distinguen entre mayúsculas y minúsculas.
- Los espacios importan. `echo hello` y `echohello` son diferentes.
- Si una orden parece haberse bloqueado, `Ctrl-C` suele cancelarla.

## Resumen

Ahora puedes explicar la función de una shell e interactuar con un prompt básico.

1. Distinguir entre una terminal y una shell.
2. Identificar un prompt de órdenes.
3. Ejecutar una orden sencilla con `echo`.
