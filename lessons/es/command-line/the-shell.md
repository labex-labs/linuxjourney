---
index: 1
lang: "es"
title: "La Shell"
meta_title: "La Shell - Línea de Comandos"
meta_description: "Aprende qué es la shell de Linux, cómo funciona el prompt de Bash y cómo ejecutar tu primer comando con ejemplos amigables para principiantes."
meta_keywords: "shell de linux, shell bash, línea de comandos, terminal linux, prompt de shell, comando echo, comandos básicos de linux"
---

## Lesson Content

### Qué es la Shell de Linux

¡Bienvenido a tu viaje por Linux! El primer paso es entender la shell de Linux. Una shell es un programa que acepta los comandos que escribes, le pide al sistema operativo que los ejecute y luego imprime el resultado en tu terminal.

Si has usado una interfaz gráfica, estás acostumbrado a hacer clic en ventanas, menús y botones. En la línea de comandos, en cambio, escribes instrucciones precisas. Las aplicaciones llamadas "Terminal", "Consola" o "Konsole" suelen abrir una sesión de shell para ti.

La shell es útil porque es rápida, se puede automatizar con scripts y está disponible en casi todos los sistemas Linux. A medida que aprendes más comandos, puedes combinarlos para inspeccionar archivos, gestionar directorios, buscar texto, instalar software y automatizar tareas repetitivas.

### Interactuando con la Shell Bash

Para este curso, nos enfocaremos en Bash, abreviatura de Bourne Again Shell. Bash es una de las shells de Linux más comunes y es una buena base incluso si luego usas `zsh`, `fish` u otra shell.

Cuando abres una terminal, te recibe el prompt de la shell. Su apariencia puede variar, pero a menudo muestra tu nombre de usuario, el nombre del equipo y el directorio actual.

```plaintext
pete@icebox:/home/pete $
```

El símbolo `$` indica que la shell está lista para aceptar tu entrada como usuario normal. No debes escribir este símbolo al ingresar comandos; lo muestra la shell. Si ves `#` en su lugar, normalmente estás trabajando como el usuario root, que tiene más poder y más riesgos.

Los comandos suelen seguir este patrón:

```bash
command options arguments
```

Por ejemplo, en `echo Hello World`, `echo` es el comando y `Hello World` es el texto que se le pasa.

### Tu Primer Comando en Linux

Comencemos con uno de los comandos más básicos para principiantes: `echo`. Este comando muestra el texto que le proporcionas de vuelta en la terminal.

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

Las comillas son útiles cuando quieres que la shell trate varias palabras como un solo texto.

### Consejos Comunes para Principiantes

- Presiona `Enter` para ejecutar un comando.
- Usa la tecla `Flecha Arriba` para recuperar un comando anterior.
- Los comandos y nombres de archivo distinguen mayúsculas y minúsculas en Linux.
- Los espacios importan. `echo hello` y `echohello` son diferentes.
- Si un comando parece estar bloqueado, `Ctrl-C` suele cancelarlo.

### Preguntas Comunes

**¿La shell es lo mismo que la terminal?** No exactamente. La terminal es la ventana o aplicación donde escribes. La shell es el programa que se ejecuta dentro de ella.

**¿Debo escribir el `$` que aparece en los ejemplos?** No. El `$` es un marcador del prompt. Escribe solo el comando que aparece después.

**¿Por qué aprender Bash si existen otras shells?** Bash está ampliamente disponible, bien documentada y es común en tutoriales y scripts.

## Exercise

Recomendamos explorar la completa [![Shell Learning Path](https://labex.io/_ipx/f_webp&q_100&s_20x20/https://file.labex.io/path/FaVTnI4iqZP0.png)Shell Learning Path](https://labex.io/es/learn/shell) para practicar habilidades y conceptos relacionados.

## Quiz Question

¿Cuál es la salida exacta en pantalla cuando escribes `echo Hello World`? Por favor responde en inglés, prestando mucha atención a mayúsculas y espacios.

## Quiz Answer

Hello World
