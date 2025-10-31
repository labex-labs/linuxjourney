---
index: 18
lang: "es"
title: "alias"
meta_title: "alias - Línea de Comandos"
meta_description: "Aprenda a crear y gestionar un alias de comando en Linux para optimizar su flujo de trabajo. Esta guía cubre la creación de alias temporales y permanentes usando el comando alias y el archivo .bashrc."
meta_keywords: "alias linux, comando alias linux, alias de comando en linux, alias de comando linux, alias bash, comando unalias, .bashrc, línea de comandos, tutorial linux"
---

## Lesson Content

Escribir comandos largos o repetitivos puede ser tedioso. Afortunadamente, puedes crear un atajo, o un **alias de Linux**, para hacer que tu experiencia en la línea de comandos sea más eficiente. El comando `alias` te permite definir un nombre personalizado para cualquier comando o secuencia de comandos.

### Creación de un Alias Temporal

Para crear un alias temporal que dure durante tu sesión de terminal actual, simplemente especificas un nombre y lo asignas al comando.

Por ejemplo, para crear un alias llamado `ll` para el comando `ls -la`, usarías la sintaxis del `comando alias linux` de esta manera:

```bash
alias ll='ls -la'
```

Ahora, en lugar de escribir `ls -la`, puedes escribir solo `ll`, y ejecutará el mismo comando. Esta es una forma sencilla pero poderosa de personalizar tu shell.

### Hacer un Alias Permanente

Un alias temporal desaparecerá una vez que cierres la terminal o reinicies el sistema. Para hacer permanente un `alias de comando en linux`, necesitas agregarlo al archivo de configuración de tu shell. Para el shell Bash, este archivo es típicamente `~/.bashrc`.

1. Abre el archivo en un editor de texto: `nano ~/.bashrc`
2. Agrega la definición de tu alias al archivo, tal como lo escribiste en la línea de comandos:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Guarda el archivo y sal del editor.

Para que los cambios surtan efecto, debes cerrar y volver a abrir la terminal o indicarle al shell que recargue el archivo de configuración usando el comando `source`:

```bash
source ~/.bashrc
```

Tu **alias de comando de Linux** ahora estará disponible cada vez que inicies una nueva sesión de terminal.

### Eliminar un Alias

Si ya no necesitas un alias, puedes eliminarlo con el comando `unalias`. Esto lo eliminará de tu sesión actual.

```bash
unalias ll
```

Para eliminar un alias permanente, también debes borrar su definición del archivo `~/.bashrc`.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) integral para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

¿Qué comando se utiliza para crear un alias? Por favor, responde en inglés en minúsculas.

## Quiz Answer

alias
