---
title: "tr (Traducir)"
description: "Aprenda a usar el comando 'tr' de Linux para traducir y eliminar caracteres. Comprenda la traducción de caracteres con ejemplos y ejercicios. ¡Comience su viaje en Linux!"
keywords: "comando tr, Linux tr, traducir caracteres, eliminar caracteres, tutorial de Linux, Linux para principiantes, guía de Linux"
---

## Lesson Content

El comando `tr` (translate) le permite traducir un conjunto de caracteres a otro conjunto de caracteres. Intentemos un ejemplo de traducción de todos los caracteres en minúscula a caracteres en mayúscula.

```bash
$ tr a-z A-Z
hello
HELLO
```

Como puede ver, convertimos los rangos de `a-z` en `A-Z`, y todo el texto que escribimos en minúsculas se convierte en mayúsculas.

## Exercise

Pruebe el siguiente comando. ¿Qué sucede?

```bash
$ tr -d ello
hello
```

## Quiz Question

¿Qué comando se utiliza para traducir caracteres?

## Quiz Answer

tr
