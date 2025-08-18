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

Verá algunos comandos `dd` que usan la opción `count`. Usualmente, con `dd`, si desea copiar un archivo que es de 1 megabyte, generalmente querrá ver ese archivo como 1 megabyte cuando termine de copiarse. Digamos que ejecuta el siguiente comando:

```bash
dd if=/home/pete/backup.img of=/dev/sdb bs=1M count=2
```

Nuestro archivo `backup.img` es de 10M; sin embargo, en este comando estamos diciendo que copie 1M 2 veces, por lo que solo se copian 2M, dejando nuestros datos copiados incompletos. `count` puede ser útil en muchas situaciones, pero si solo está copiando datos, puede omitir `count` e incluso `bs` para el caso. Si realmente desea optimizar sus transferencias de datos, entonces querrá comenzar a usar esas opciones.

`dd` es extremadamente potente; puede usarlo para hacer copias de seguridad de cualquier cosa, incluyendo unidades de disco completas, restaurar imágenes de disco y más. Tenga cuidado, esa poderosa herramienta puede tener un precio si no está seguro de lo que está haciendo.

## Exercise

Use the `dd` command to make a backup of your drive and set the output to a `.img` file.

## Quiz Question

¿Cuál es la opción `dd` para el tamaño de bloque?

## Quiz Answer

bs
