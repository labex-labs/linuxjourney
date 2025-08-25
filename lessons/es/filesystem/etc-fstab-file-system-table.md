---
index: 7
lang: "es"
title: "/etc/fstab"
meta_title: "/etc/fstab - El sistema de archivos"
meta_description: "Aprenda sobre /etc/fstab en Linux, cómo configurar los montajes del sistema de archivos al inicio y gestionar las entradas de los dispositivos. ¡Comprenda fstab para principiantes!"
meta_keywords: "/etc/fstab, Linux fstab, montar sistemas de archivos, arranque de Linux, tutorial fstab, principiante, guía"
---

## Lesson Content

Cuando queremos montar automáticamente sistemas de archivos al inicio, podemos añadirlos a un archivo llamado `/etc/fstab` (pronunciado "eff es tab", no "eff stab"), abreviatura de tabla de sistemas de archivos. Este archivo contiene una lista permanente de los sistemas de archivos que se montan.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

Cada línea representa un sistema de archivos; los campos son:

- UUID - Identificador del dispositivo
- Punto de montaje - Directorio donde se monta el sistema de archivos
- Tipo de sistema de archivos
- Opciones - Otras opciones de montaje; consulte la página man para más detalles
- Dump - Utilizado por la utilidad dump para decidir cuándo hacer una copia de seguridad; por defecto debe ser 0
- Pass - Utilizado por fsck para decidir en qué orden deben comprobarse los sistemas de archivos; si el valor es 0, no se comprobará

Para añadir una entrada, simplemente modifique directamente el archivo `/etc/fstab` utilizando la sintaxis de entrada anterior. Tenga cuidado al modificar este archivo; podría complicarle un poco la vida si se equivoca.

## Exercise

¡La práctica hace al maestro! La experiencia práctica es crucial para comprender cómo gestionar los sistemas de archivos y asegurarse de que se montan correctamente al inicio del sistema. Aquí tiene algunos laboratorios prácticos para reforzar su comprensión de la gestión de sistemas de archivos de Linux y el archivo `/etc/fstab`:

1. **[Gestionar particiones y sistemas de archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Practique la creación de particiones, su formato, su montaje y la configuración del montaje persistente utilizando `/etc/fstab`.
2. **[Crear y activar un archivo de intercambio en Linux](https://labex.io/es/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - Aprenda la tarea administrativa esencial de crear y activar un archivo de intercambio (swap file), que a menudo implica entradas en `/etc/fstab`.

Estos laboratorios le ayudarán a aplicar los conceptos de montaje y configuración de sistemas de archivos en escenarios reales y a generar confianza en la gestión de recursos de disco en Linux.

## Quiz Question

¿Qué archivo se utiliza para definir cómo deben montarse los sistemas de archivos?

## Quiz Answer

/etc/fstab
