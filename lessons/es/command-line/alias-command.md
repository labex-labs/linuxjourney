---
index: 18
lang: "es"
title: "alias"
meta_title: "alias - Línea de Comandos"
meta_description: "Aprende el comando alias en Linux con ejemplos para crear alias temporales, guardar alias en .bashrc, listar alias y eliminarlos con unalias."
meta_keywords: "comando alias linux, comando alias, alias bash, alias .bashrc, comando unalias, atajo de comando linux, alias de shell"
---

## Lesson Content

Escribir comandos largos o repetitivos puede ser tedioso. Un alias es un atajo de shell que te permite definir un nombre personalizado para un comando o secuencia de comandos.

### Creando un Alias Temporal

Para crear un alias temporal que dure solo durante tu sesión actual de terminal, simplemente especifica un nombre y asígnale la cadena del comando.

Por ejemplo, crea un alias llamado `ll` para `ls -la`:

```bash
$ alias ll='ls -la'
```

Ahora, en lugar de escribir `ls -la`, puedes simplemente escribir `ll`, y ejecutará el mismo comando. Esta es una forma simple pero poderosa de personalizar tu shell.

### Haciendo un Alias Permanente

Un alias temporal desaparecerá una vez que cierres tu terminal o reinicies tu sistema. Para hacer un `alias de comando en linux` permanente, necesitas agregarlo al archivo de configuración de tu shell. Para el shell Bash, este archivo suele ser `~/.bashrc`.

1. Abre el archivo en un editor de texto: `nano ~/.bashrc`
2. Agrega tu definición de alias al archivo, tal como la escribiste en la línea de comandos:

```bash
alias ll='ls -la'
alias update='sudo apt update && sudo apt upgrade'
```

3. Guarda el archivo y sal del editor.

Para que los cambios tengan efecto, debes cerrar y volver a abrir tu terminal o indicarle al shell que recargue el archivo de configuración usando el comando `source`:

```bash
$ source ~/.bashrc
```

Tu alias ahora estará disponible cada vez que inicies una nueva sesión de Bash.

### Eliminando un Alias

Si ya no necesitas un alias, puedes eliminarlo con el comando `unalias`. Esto lo eliminará de tu sesión actual.

```bash
$ unalias ll
```

Para eliminar un alias permanente, también debes borrar su definición del archivo `~/.bashrc`.

### Listando Alias Existentes

Ejecuta `alias` sin argumentos para listar los alias en tu shell actual.

```bash
$ alias
alias ll='ls -la'
alias grep='grep --color=auto'
```

Usa `type` para ver qué se ejecutará cuando ingreses un comando:

```bash
$ type ll
ll is aliased to 'ls -la'
```

### Ejemplos Útiles de Alias

```bash
$ alias la='ls -la'
$ alias ..='cd ..'
$ alias grep='grep --color=auto'
```

Mantén los alias cortos y predecibles. Evita reemplazar comandos destructivos con comportamientos sorprendentes a menos que estés muy seguro.

### Preguntas Comunes

**¿Los alias funcionan en scripts?** Usualmente no, no por defecto. Los scripts deberían usar comandos completos o funciones.

**¿Dónde deben ir los alias de Bash?** Ponlos en `~/.bashrc` para sesiones interactivas de Bash.

**¿Qué pasa si un alias entra en conflicto con un comando real?** El alias usualmente tiene prioridad en el uso interactivo del shell. Usa `command nombre` o `\nombre` para evitar un alias.

## Exercise

Aunque no hay laboratorios específicos para este tema, recomendamos explorar la completa [Ruta de Aprendizaje de Linux](https://labex.io/es/learn/linux) para practicar habilidades y conceptos relacionados con Linux.

## Quiz Question

What command is used to create an alias? Please answer in lowercase English.

## Quiz Answer

alias
