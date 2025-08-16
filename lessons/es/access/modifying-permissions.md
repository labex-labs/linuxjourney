---
title: "Modificando Permisos"
description: "Aprende a usar el comando chmod para modificar los permisos de archivos en Linux. Comprende los modos simbólico y numérico para una gestión segura de archivos. ¡Empieza a aprender ahora!"
keywords: "comando chmod, permisos Linux, permisos de archivo, tutorial chmod, seguridad Linux, Linux para principiantes, guía Linux, chmod numérico"
---

## Lesson Content

Cambiar permisos se puede hacer fácilmente con el comando `chmod`.

Primero, elige qué conjunto de permisos quieres cambiar: usuario, grupo u otros. Puedes añadir o quitar permisos con un `+` o un `-`. Veamos algunos ejemplos.

### Adding permission bit on a file

```bash
chmod u+x myfile
```

El comando anterior se lee así: cambia el permiso en `myfile` añadiendo el bit de permiso de ejecución al conjunto de usuario. ¡Así que ahora el usuario tiene permiso de ejecución en este archivo!

### Removing permission bit on a file

```bash
chmod u-x myfile
```

### Adding multiple permission bits on a file

```bash
chmod ug+w
```

Hay otra forma de cambiar permisos usando el formato numérico. Este método te permite cambiar permisos de una sola vez. En lugar de usar r, w o x para representar permisos, usarás una representación numérica para un solo conjunto de permisos. Así que no hay necesidad de especificar el grupo con `g` o el usuario con `u`.

Las representaciones numéricas se muestran a continuación:

- 4: read permission
- 2: write permission
- 1: execute permission

Veamos un ejemplo:

```bash
chmod 755 myfile
```

¿Puedes adivinar qué permisos le estamos dando a este archivo? Desglosemos esto: `755` cubre los permisos para todos los conjuntos. El primer número (7) representa los permisos de usuario, el segundo número (5) representa los permisos de grupo, y el último 5 representa los permisos de otros.

Espera un minuto, 7 y 5 no estaban listados arriba. ¿De dónde sacamos estos números? Recuerda, ahora estamos combinando todos los permisos en un solo número, así que tendrás que usar algo de matemáticas.

7 = 4 + 2 + 1, así que 7 son los permisos de usuario, y tiene permisos de lectura, escritura y ejecución.

5 = 4 + 1, el grupo tiene permisos de lectura y ejecución.

5 = 4 + 1, y todos los demás usuarios tienen permisos de lectura y ejecución.

Una cosa a tener en cuenta: no es una buena idea cambiar los permisos a la ligera. Podrías exponer un archivo sensible para que cualquiera lo modifique. Sin embargo, muchas veces querrás cambiar los permisos legítimamente; solo toma precauciones al usar el comando `chmod`.

## Exercise

Cambia algunos permisos básicos de archivos de texto y observa cómo cambian los bits al hacer un `ls -l`.

## Quiz Question

¿Qué número representa el permiso de lectura cuando se usa el formato numérico?

## Quiz Answer

4
