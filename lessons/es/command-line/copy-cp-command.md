---
index: 10
lang: "es"
title: "cp (Copiar)"
meta_title: "cp (Copiar) - Línea de Comandos"
meta_description: "Aprende a usar el comando cp de Linux para copiar archivos y directorios. Entiende opciones como -r y comodines. ¡Comienza tu viaje en Linux hoy mismo!"
meta_keywords: "comando cp, copiar archivos Linux, tutorial Linux, Linux para principiantes, cp -r, comodines Linux, guía Linux"
---

## Lesson Content

Empecemos a hacer algunas copias de estos archivos. Al igual que copiar y pegar archivos en otros sistemas operativos, el shell nos ofrece una forma aún más sencilla de hacerlo.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile` es el archivo que quieres copiar, y `/home/pete/Documents/cooldocs` es donde estás copiando el archivo.

Puedes copiar múltiples archivos y directorios, así como usar comodines. Un comodín es un carácter que puede ser sustituido por una selección basada en patrones, dándote más flexibilidad con las búsquedas. Puedes usar comodines en cada comando para mayor flexibilidad.

- `*` el comodín de los comodines, se usa para representar todos los caracteres individuales o cualquier cadena.
- `?` usado para representar un carácter
- `[]` usado para representar cualquier carácter dentro de los corchetes

```bash
cp *.jpg /home/pete/Pictures
```

Esto copiará todos los archivos con la extensión `.jpg` en tu directorio actual al directorio `Pictures`.

Un comando útil es usar la bandera `-r`; esto copiará recursivamente los archivos y directorios dentro de un directorio.

Intenta hacer un `cp` en un directorio que contenga un par de archivos a tu directorio `Documents`. No funcionó, ¿verdad? Bueno, eso es porque necesitarás copiar también los archivos y directorios internos con el comando `-r`.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Una cosa a tener en cuenta, si copias un archivo a un directorio que tiene el mismo nombre de archivo, el archivo será sobrescrito con lo que estés copiando. Esto no es bueno si tienes un archivo que no quieres que se sobrescriba accidentalmente. Puedes usar la bandera `-i` (interactiva) para que te pregunte antes de sobrescribir un archivo.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

Copia un par de archivos; ten cuidado de no sobrescribir nada importante.

Para practicar con el comando `cp`, prueba este laboratorio interactivo:

- [Linux cp Command: File Copying](https://labex.io/es/labs/linux-linux-cp-command-file-copying-209744)

## Quiz Question

¿Qué bandera necesitas especificar para copiar un directorio?

## Quiz Answer

-r
