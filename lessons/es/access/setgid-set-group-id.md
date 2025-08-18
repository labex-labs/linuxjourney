---
lang: "es"
title: "Setgid"
meta_title: "Setgid - Permisos"
meta_description: "Aprende sobre los permisos SGID (Set Group ID) en Linux, cómo funcionan y cómo modificarlos. Comprende este concepto crucial de seguridad en Linux."
meta_keywords: "Linux SGID, Set Group ID, permisos de Linux, chmod g+s, seguridad de Linux, Linux para principiantes, tutorial de Linux"
---

## Lesson Content

Similar al bit de permiso set user ID, existe un bit de permiso set group ID (SGID). Este bit permite que un programa se ejecute como si fuera miembro de ese grupo.

Veamos un ejemplo:

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

Ahora podemos ver que el bit de permiso está en el conjunto de permisos de grupo.

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

La representación numérica para SGID es 2.

## Exercise

No exercises for this lesson.

## Quiz Question

¿Qué número representa el SGID?

## Quiz Answer

2
