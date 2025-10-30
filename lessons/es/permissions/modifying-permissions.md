---
index: 2
lang: "es"
title: "Modificación de Permisos"
meta_title: "Modificación de Permisos - Permisos"
meta_description: "Aprende a usar el comando chmod para modificar los permisos de archivos en Linux. Comprende los modos simbólico y numérico para una gestión segura de archivos. ¡Empieza a aprender ahora!"
meta_keywords: "comando chmod, permisos de Linux, permisos de archivos, tutorial chmod, seguridad de Linux, Linux para principiantes, guía de Linux, chmod numérico"
---

## Lesson Content

Cambiar permisos se puede hacer fácilmente con el comando `chmod`.

Primero, elige qué conjunto de permisos quieres cambiar: usuario, grupo u otros. Puedes añadir o quitar permisos con un `+` o un `-`. Veamos algunos ejemplos.

### Añadir bit de permiso en un archivo

```bash
chmod u+x myfile
```

El comando anterior se lee así: cambiar el permiso en `myfile` añadiendo el bit de permiso de ejecución al conjunto de usuario. ¡Así que ahora el usuario tiene permiso de ejecución en este archivo!

### Quitar bit de permiso en un archivo

```bash
chmod u-x myfile
```

### Añadir múltiples bits de permiso en un archivo

```bash
chmod ug+w
```

Hay otra forma de cambiar permisos usando el formato numérico. Este método te permite cambiar todos los permisos a la vez. En lugar de usar r, w o x para representar permisos, usarás una representación numérica para un solo conjunto de permisos. Así que no hay necesidad de especificar el grupo con `g` o el usuario con `u`.

Las representaciones numéricas se ven a continuación:

- 4: permiso de lectura
- 2: permiso de escritura
- 1: permiso de ejecución

Veamos un ejemplo:

```bash
chmod 755 myfile
```

¿Puedes adivinar qué permisos le estamos dando a este archivo? Desglosemos esto: `755` cubre los permisos para todos los conjuntos. El primer número (7) representa los permisos de usuario, el segundo número (5) representa los permisos de grupo, y el último 5 representa los otros permisos.

Espera un minuto, 7 y 5 no estaban listados arriba. ¿De dónde sacamos estos números? Recuerda, ahora estamos combinando todos los permisos en un solo número, así que tendrás que hacer algunos cálculos.

7 = 4 + 2 + 1, así que 7 son los permisos de usuario, y tiene permisos de lectura, escritura y ejecución.

5 = 4 + 1, el grupo tiene permisos de lectura y ejecución.

5 = 4 + 1, y todos los demás usuarios tienen permisos de lectura y ejecución.

Una cosa a tener en cuenta: no es una buena idea cambiar los permisos a la ligera. Podrías exponer un archivo sensible para que cualquiera lo modifique. Sin embargo, muchas veces querrás cambiar los permisos legítimamente; solo toma precauciones al usar el comando `chmod`.

## Exercise

¡La práctica hace al maestro! Aquí tienes algunos laboratorios prácticos para reforzar tu comprensión de los permisos de archivos en Linux:

1. **[Grupo de Usuarios y Permisos de Archivos de Linux](https://labex.io/es/labs/linux-linux-user-group-and-file-permissions-18002)** - Aprende conceptos esenciales de gestión de usuarios y grupos de Linux, incluyendo la comprensión de los permisos de archivos y la manipulación de la propiedad de los archivos. Este laboratorio proporciona experiencia práctica en la seguridad de un entorno Linux multiusuario.
2. **[Añadir Nuevo Usuario y Grupo](https://labex.io/es/labs/linux-add-new-user-and-group-17987)** - En este desafío, simularás la adición de nuevos miembros del equipo a un entorno de servidor, creando nuevas cuentas de usuario, configurando grupos personalizados y gestionando las membresías de grupo, lo que a menudo implica establecer los permisos adecuados.

Estos laboratorios te ayudarán a aplicar los conceptos de permisos de usuario, grupo y otros en escenarios reales y a ganar confianza en la gestión de accesos en Linux.

## Quiz Question

¿Qué número representa el permiso de lectura cuando se utiliza el formato numérico?

## Quiz Answer

4
