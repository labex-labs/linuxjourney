---
index: 9
lang: "es"
title: "tail"
meta_title: "tail - Text-Fu"
meta_description: "Aprende a usar el comando `tail` en Linux para ver el final de los archivos y monitorear logs. Descubre `tail -f` para actualizaciones en tiempo real. ¡Comienza tu viaje en Linux!"
meta_keywords: "comando tail, Linux tail, tail -f, ver logs, tutorial Linux, Linux para principiantes, guía Linux"
---

## Lesson Content

Similar al comando `head`, el comando `tail` te permite ver las últimas 10 líneas de un archivo por defecto.

```bash
tail /var/log/syslog
```

Junto con `head`, puedes cambiar el número de líneas que deseas ver.

```bash
tail -n 10 /var/log/syslog
```

Otra gran opción que puedes usar es la bandera `-f` (follow); esta seguirá el archivo a medida que crece. Pruébalo y ve qué sucede.

```bash
tail -f /var/log/syslog
```

Tu archivo `syslog` cambiará continuamente mientras interactúas con tu sistema, y usando `tail -f` puedes ver todo lo que se está añadiendo a ese archivo.

## Exercise

Look at the man page of `tail` and read some of the other commands we didn't discuss.

```bash
man tail
```

## Quiz Question

¿Cuál es la bandera utilizada para seguir un archivo en `tail`?

## Quiz Answer

-f
