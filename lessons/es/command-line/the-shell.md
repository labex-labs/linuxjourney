---
lang: "es"
title: "El Shell"
meta_title: "El Shell - Command Line"
meta_description: "Aprende sobre el shell de Linux, Bash y comandos básicos como 'echo'. Comprende los prompts del shell y comienza tu viaje en Linux con esta guía para principiantes."
meta_keywords: "shell de Linux, Bash, comando echo, tutorial de Linux, línea de comandos, Linux para principiantes, prompt del shell, guía de Linux"
---

## Lesson Content

El mundo es tu ostra, o mejor dicho, el shell es tu ostra. ¿Qué es el shell? El shell es básicamente un programa que toma tus comandos del teclado y los envía al sistema operativo para que los ejecute. Si alguna vez has usado una GUI, probablemente hayas visto programas como "Terminal" o "Consola"; estos son solo programas que inician un shell para ti. A lo largo de todo este curso, aprenderemos sobre las maravillas del shell.

En este curso, usaremos el programa de shell Bash (Bourne Again Shell). Casi todas las distribuciones de Linux usarán Bash como shell predeterminado. Hay otros shells disponibles, como `ksh`, `zsh` y `tsch`, pero no nos adentraremos en ninguno de ellos.

¡Vamos a empezar! Dependiendo de la distribución, tu shell prompt podría cambiar, pero en su mayor parte, debería adherirse al siguiente formato:

```plaintext
username@hostname:current_directory
pete@icebox:/home/pete $
```

¿Notas el `$` al final del prompt? Diferentes shells tendrán diferentes prompts. En nuestro caso, el `$` es para un usuario normal que usa Bash, Bourne o Korn shell. No añades el símbolo del prompt cuando escribes el comando; solo debes saber que está ahí.

Comencemos con un comando simple, `echo`. El comando `echo` simplemente imprime los argumentos de texto en la pantalla.

```bash
echo Hello World
```

## Exercise

Try some other Linux commands and see what they output:

1. `$ date`
2. `$ whoami`

## Quiz Question

¿Qué debería mostrarse en la pantalla cuando escribes `echo Hello World`?

## Quiz Answer

Hello World
