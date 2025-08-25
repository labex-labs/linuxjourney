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

Puedes copiar múltiples archivos y directorios, así como usar comodines. Un comodín es un carácter que puede sustituirse por una selección basada en patrones, lo que te da más flexibilidad con las búsquedas. Puedes usar comodines en cada comando para mayor flexibilidad.

- `*` el comodín de los comodines, se usa para representar todos los caracteres individuales o cualquier cadena.
- `?` se usa para representar un carácter
- `[]` se usa para representar cualquier carácter dentro de los corchetes

```bash
cp *.jpg /home/pete/Pictures
```

Esto copiará todos los archivos con la extensión `.jpg` en tu directorio actual al directorio `Pictures`.

Un comando útil es usar la bandera `-r`; esto copiará recursivamente los archivos y directorios dentro de un directorio.

Intenta hacer un `cp` de un directorio que contiene un par de archivos a tu directorio `Documents`. ¿No funcionó, verdad? Bueno, eso es porque necesitarás copiar también los archivos y directorios internos con el comando `-r`.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

Una cosa a tener en cuenta, si copias un archivo a un directorio que tiene el mismo nombre de archivo, el archivo será sobrescrito con lo que estés copiando. Esto no es bueno si tienes un archivo que no quieres que se sobrescriba accidentalmente. Puedes usar la bandera `-i` (interactiva) para que te pregunte antes de sobrescribir un archivo.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión sobre cómo copiar archivos y directorios en Linux:

1. **[Comando cp de Linux: Copia de archivos](https://labex.io/es/labs/linux-linux-cp-command-file-copying-209744)** - Practica el uso básico, opciones avanzadas como la copia recursiva, la preservación de atributos y el uso de comodines para copiar archivos y directorios de manera eficiente.
2. **[Organización de archivos y directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Practica habilidades esenciales de gestión de archivos en Linux usando los comandos `cp`, `mv` y `rm` para organizar una estructura de proyecto, mover archivos y limpiar directorios innecesarios.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a desarrollar confianza con la copia y gestión de archivos en Linux.

## Quiz Question

¿Qué bandera necesitas especificar para copiar un directorio?

## Quiz Answer

-r
