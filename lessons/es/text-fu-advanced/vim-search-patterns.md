---
lang: "es"
title: "Patrones de búsqueda de Vim"
description: "Aprenda los patrones de búsqueda de Vim: búsqueda hacia adelante (/) y hacia atrás (?). Navegue por los resultados con 'n' y 'N'. ¡Mejore sus habilidades con Vim hoy mismo!"
keywords: "búsqueda Vim, comandos Vim, editor de texto Linux, tutorial Vim, guía Vim, Vim para principiantes"
---

## Lesson Content

Para buscar una expresión, simplemente escriba la tecla `/` y luego su término de búsqueda mientras esté en una sesión de Vim. Una vez que presione Enter, puede presionar `n` para avanzar o `N` para retroceder en sus resultados de búsqueda.

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

El comando de búsqueda `?` buscará el archivo de texto hacia atrás. Así, en el ejemplo anterior, la última palabra "pretty" aparecería primero.

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

Juegue con la tecla de búsqueda. Abra un archivo de texto en Vim con: `vim [textfile]` ¡y empiece a buscar!

## Quiz Question

¿Qué tecla se utiliza para buscar en Vim?

## Quiz Answer

/
