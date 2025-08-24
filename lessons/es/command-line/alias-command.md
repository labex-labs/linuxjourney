---
index: 18
lang: "es"
title: "alias"
meta_title: "alias - Línea de Comandos"
meta_description: "Aprende a crear y gestionar alias de Linux para comandos comunes. Descubre cómo configurar alias temporales y permanentes en .bashrc. ¡Mejora tu eficiencia en la línea de comandos!"
meta_keywords: "Linux alias, bash alias, comando unalias, .bashrc, tutorial de Linux, línea de comandos, Linux para principiantes, guía de Linux"
---

## Lesson Content

A veces, escribir comandos puede volverse muy repetitivo, o si necesitas escribir un comando largo muchas veces, lo mejor es tener un alias que puedas usar para eso. Para crear un alias para un comando, simplemente especificas un nombre de alias y lo asignas al comando.

```bash
alias foobar='ls -la'
```

Ahora, en lugar de escribir `ls -la`, puedes escribir `foobar`, y ejecutará ese comando, algo bastante ingenioso. Ten en cuenta que este comando no guardará tu alias después de reiniciar, por lo que deberás agregar un alias permanente en:

```plaintext
~/.bashrc
```

o archivos similares si quieres que persista después de reiniciar.

Puedes eliminar alias con el comando `unalias`:

```bash
unalias foobar
```

## Exercise

Crea un par de alias y luego elimínalos.

Para practicar más a fondo los conceptos básicos de la línea de comandos de Linux, explora estos laboratorios interactivos:

- [Linux Directory Navigation](https://labex.io/es/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/es/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

¿Qué comando se utiliza para crear un alias?

## Quiz Answer

alias
