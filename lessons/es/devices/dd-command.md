---
index: 7
lang: "es"
title: "dd"
meta_title: "dd - Dispositivos"
meta_description: "Aprenda el comando dd de Linux para copiar datos e imágenes de disco. Comprenda sus opciones como if, of y bs. ¡Comience su viaje de gestión de datos en Linux!"
meta_keywords: "comando dd, Linux dd, copiar datos, imágenes de disco, tutorial de Linux, principiante, guía, copia de seguridad de datos"
---

## Lesson Content

La herramienta `dd` es súper útil para convertir y copiar datos. Lee la entrada de un archivo o flujo de datos y la escribe en un archivo o flujo de datos.

Considere el siguiente comando:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1024
```

Este comando está copiando el contenido de `backup.img` a `/dev/sdb`. Copiará los datos en bloques de 1024 bytes hasta que no haya más datos para copiar.

- `if=file` - Archivo de entrada; lee de un archivo en lugar de la entrada estándar.
- `of=file` - Archivo de salida; escribe en un archivo en lugar de la salida estándar.
- `bs=bytes` - Tamaño de bloque; lee y escribe esta cantidad de bytes de datos a la vez. Puede usar diferentes métricas de tamaño denotando el tamaño con una `k` para kilobyte, `m` para megabyte, etc., por lo que 1024 bytes es 1k.
- `count=number` - Número de bloques a copiar.

Verá algunos comandos `dd` que usan la opción `count`. Usualmente, con `dd`, si desea copiar un archivo de 1 megabyte, generalmente querrá ver ese archivo como 1 megabyte cuando termine de copiarse. Digamos que ejecuta el siguiente comando:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Nuestro archivo `backup.img` es de 10M; sin embargo, en este comando estamos diciendo que copie 1M 2 veces, por lo que solo se copian 2M, dejando nuestros datos copiados incompletos. `count` puede ser útil en muchas situaciones, pero si solo está copiando datos, puede omitir `count` e incluso `bs` para el caso. Si realmente desea optimizar sus transferencias de datos, entonces querrá comenzar a usar esas opciones.

`dd` es extremadamente potente; puede usarlo para hacer copias de seguridad de cualquier cosa, incluyendo unidades de disco completas, restaurar imágenes de disco y más. Tenga cuidado, esa poderosa herramienta puede tener un precio si no está seguro de lo que está haciendo.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la manipulación de datos y la gestión de discos en Linux:

1. **[Crear y Restaurar una Copia de Seguridad con tar en Linux](https://labex.io/es/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - Practique la creación y restauración de copias de seguridad del sistema de archivos, una habilidad crítica relacionada con la integridad y recuperación de datos, para la cual también se puede usar `dd`.
2. **[Administrar Particiones y Sistemas de Archivos de Linux](https://labex.io/es/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - Aprenda a administrar particiones y sistemas de archivos de disco, incluyendo la creación, el formato y el montaje, que son conceptos fundamentales al trabajar con herramientas como `dd` para la creación de imágenes de disco.

Estos laboratorios le ayudarán a aplicar los conceptos de manejo de datos y operaciones de disco en escenarios reales y a desarrollar confianza con las tareas de administración del sistema.

## Quiz Question

¿Cuál es la opción de `dd` para el tamaño de bloque?

## Quiz Answer

bs
