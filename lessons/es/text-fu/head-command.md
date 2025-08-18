---
lang: "es"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Aprende a usar el comando 'head' de Linux para ver el principio de los archivos. Entiende opciones como -n para el conteo de líneas. Tutorial esencial de comandos de Linux."
meta_keywords: "comando head, Linux head, ver inicio de archivo, tutorial Linux, comandos Linux, Linux para principiantes, head -n, guía Linux"
---

## Lesson Content

Supongamos que tenemos un archivo muy largo; de hecho, tenemos muchos para elegir. Adelante, `cat /var/log/syslog`. Deberías ver páginas y páginas de texto. ¿Qué pasaría si solo quisiera ver las primeras líneas de este archivo de texto? Bueno, podemos hacerlo con el comando `head`. Por defecto, el comando `head` te mostrará las primeras 10 líneas de un archivo.

```bash
head /var/log/syslog
```

También puedes modificar el número de líneas a lo que elijas. Digamos que quisiera ver las primeras 15 líneas en su lugar.

```bash
head -n 15 /var/log/syslog
```

La bandera `-n` significa "número de líneas".

## Exercise

¿Qué hace el siguiente comando y por qué?

```bash
head -c 15 /var/log/syslog
```

## Quiz Question

¿Qué bandera usarías para cambiar el número de líneas que quieres ver para el comando `head`?

## Quiz Answer

-n
