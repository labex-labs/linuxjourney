---
title: "cp (Copiar)"
description: "Aprende a usar el comando cp de Linux para copiar archivos y directorios. Entiende opciones como -r y wildcards. ¡Comienza tu viaje en Linux hoy mismo!"
keywords: "comando cp, copiar archivos Linux, tutorial Linux, Linux para principiantes, cp -r, wildcards Linux, guía Linux"
---

## Lesson Content

Comencemos a hacer algunas copias de estos archivos. Al igual que copiar y pegar archivos en otros sistemas operativos, la shell nos ofrece una forma aún más sencilla de hacerlo.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` es el archivo que quieres copiar, y `/home/pete/Documents/cooldocs` es donde estás copiando el archivo.

Puedes copiar múltiples archivos y directorios, así como usar wildcards. Un wildcard es un carácter que puede sustituirse por una selección basada en patrones, dándote más flexibilidad con las búsquedas. Puedes usar wildcards en cada comando para mayor flexibilidad.

- `*` el wildcard de wildcards, se usa para representar todos los caracteres individuales o cualquier cadena.
- `?` se usa para representar un carácter
- `[]` se usa para representar cualquier carácter dentro de los corchetes

```bash
cp *.jpg /home/pete/Pictures
```

Esto copiará todos los archivos con la extensión `.jpg` en tu directorio actual al directorio `Pictures`.

Un comando útil es usar la flag `-r`; esto copiará recursivamente los archivos y directorios dentro de un directorio.

Intenta hacer un `cp` de un directorio que contenga un par de archivos a tu directorio `Documents`. No funcionó, ¿verdad? Bueno, eso es porque necesitarás copiar también los archivos y directorios internos con el comando `-r`.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Una cosa a tener en cuenta, si copias un archivo a un directorio que tiene el mismo filename, el archivo será sobrescrito con lo que estés copiando. Esto no es bueno si tienes un archivo que no quieres que se sobrescriba accidentalmente. Puedes usar la flag `-i` (interactive) para que te pregunte antes de sobrescribir un archivo.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

Copia un par de archivos; ten cuidado de no sobrescribir nada importante.

## Quiz Question

¿Qué flag necesitas especificar para copiar un directorio?

## Quiz Answer

-r
