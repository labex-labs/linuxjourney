---
title: "ayuda"
description: "Aprende a usar el comando 'help' en Bash para obtener asistencia rápida en la línea de comandos. Comprende los comandos integrados y encuentra opciones para programas Linux."
keywords: "comando help de Linux, Bash help, ayuda de línea de comandos, comandos de Linux, Linux para principiantes, tutorial de Linux, tutorial de Bash"
---

## Lesson Content

Linux tiene algunas herramientas integradas excelentes para ayudarte a entender cómo usar un comando o verificar qué opciones están disponibles para un comando. Una herramienta, `help`, es un comando Bash integrado que proporciona ayuda para otros comandos Bash (por ejemplo, `echo`, `logout`, `pwd`).

```bash
help echo
```

Esto te dará una descripción y las opciones que puedes usar cuando quieras ejecutar `echo`. Para otros programas ejecutables, es una convención tener una opción llamada `--help` o algo similar.

```bash
echo --help
```

No todos los desarrolladores que distribuyen ejecutables se ajustarán a este estándar, pero probablemente sea tu mejor opción para encontrar ayuda sobre un programa.

## Exercise

Run `help` on the `echo` command, `logout` command, and `pwd` command.

## Quiz Question

¿Cómo se obtiene ayuda rápida en la línea de comandos para los comandos Bash integrados?

## Quiz Answer

help
