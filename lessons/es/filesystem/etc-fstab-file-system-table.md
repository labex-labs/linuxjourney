---
lang: "es"
title: "/etc/fstab"
meta_title: "/etc/fstab - El Filesystem"
meta_description: "Aprenda sobre /etc/fstab en Linux, cómo configurar montajes de sistemas de archivos al inicio y gestionar entradas de dispositivos. ¡Comprenda fstab para principiantes!"
meta_keywords: "/etc/fstab, Linux fstab, montar sistemas de archivos, arranque de Linux, tutorial de fstab, principiante, guía"
---

## Lesson Content

Cuando queremos montar automáticamente sistemas de archivos al inicio, podemos añadirlos a un archivo llamado `/etc/fstab` (pronunciado "eff es tab," no "eff stab"), abreviatura de tabla de sistemas de archivos. Este archivo contiene una lista permanente de los sistemas de archivos que se montan.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

Cada línea representa un sistema de archivos; los campos son:

- UUID - Device identifier
- Mount point - Directorio donde se monta el sistema de archivos
- Filesystem type
- Options - Otras opciones de montaje; ver la página man para más detalles
- Dump - Usado por la utilidad dump para decidir cuándo hacer una copia de seguridad; por defecto, debe ser 0
- Pass - Usado por fsck para decidir en qué orden deben ser comprobados los sistemas de archivos; si el valor es 0, no será comprobado

Para añadir una entrada, simplemente modifique directamente el archivo `/etc/fstab` usando la sintaxis de entrada anterior. Tenga cuidado al modificar este archivo; podría complicar un poco su vida si se equivoca.

## Exercise

Añada la unidad USB en la que hemos estado trabajando como una entrada en `/etc/fstab`. Cuando reinicie, debería seguir viéndola montada.

## Quiz Question

¿Qué archivo se utiliza para definir cómo deben montarse los sistemas de archivos?

## Quiz Answer

/etc/fstab
