---
lang: "es"
title: "alias"
description: "Aprende a crear y gestionar aliases de Linux para comandos comunes. Descubre la configuración de alias temporales y permanentes en .bashrc. ¡Mejora tu eficiencia en la línea de comandos!"
keywords: "alias de Linux, alias de bash, comando unalias, .bashrc, tutorial de Linux, línea de comandos, Linux para principiantes, guía de Linux"
---

## Lesson Content

A veces, escribir comandos puede volverse muy repetitivo, o si necesitas escribir un comando largo muchas veces, lo mejor es tener un alias que puedas usar para eso. Para crear un alias para un comando, simplemente especificas un nombre de alias y lo asignas al comando.

```bash
alias foobar='ls -la'
```

Ahora, en lugar de escribir `ls -la`, puedes escribir `foobar`, y ejecutará ese comando, algo bastante útil. Ten en cuenta que este comando no guardará tu alias después de reiniciar, por lo que deberás agregar un alias permanente en:

```plaintext
~/.bashrc
```

o archivos similares si quieres que persista después de reiniciar.

Puedes eliminar aliases con el comando `unalias`:

```bash
unalias foobar
```

## Exercise

Create a couple of aliases, then remove them.

## Quiz Question

¿Qué comando se usa para crear un alias?

## Quiz Answer

alias
