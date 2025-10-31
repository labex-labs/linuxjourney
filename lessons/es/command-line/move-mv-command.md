---
index: 11
lang: "es"
title: "mv (Mover)"
meta_title: "mv (Mover) - Línea de Comandos"
meta_description: "Guía completa del comando mv en Linux. Aprenda a usar el comando bash mv para mover y renombrar archivos y directorios, usar opciones como linux mv -t y prevenir sobrescrituras accidentales."
meta_keywords: "comando mv, comando mv en linux, linux mv, bash mv, mv -r linux, linux mv -t, mover archivos, renombrar archivos, línea de comandos linux"
---

## Lesson Content

El comando `mv`, abreviatura de "move" (mover), es una utilidad fundamental en cualquier entorno Linux. Sirve para dos propósitos principales: renombrar archivos o directorios y moverlos a una ubicación diferente. Su funcionalidad es similar en muchos aspectos al comando `cp`.

### Renombrar Archivos y Directorios

Uno de los usos más comunes del `mv command in linux` es para renombrar. La sintaxis es sencilla: especificas el nombre antiguo y el nombre nuevo.

Para renombrar un archivo:

```bash
mv archivo_antiguo archivo_nuevo
```

Esta misma lógica se aplica al renombrar directorios:

```bash
mv nombre_directorio_antiguo nombre_directorio_nuevo
```

### Mover Archivos y Directorios

La otra función principal del comando `mv` es mover elementos de una ubicación a otra.

Para mover un solo archivo a un directorio diferente:

```bash
mv archivo2 /home/pete/Documentos
```

También puedes mover varios archivos a la vez. Simplemente enumera todos los archivos de origen seguidos del directorio de destino:

```bash
mv archivo_1 archivo_2 /un_directorio
```

Una opción útil para esto es `linux mv -t`, que te permite especificar el directorio de destino primero. Esto puede ser más claro al mover muchos archivos.

```bash
mv -t /un_directorio archivo_1 archivo_2
```

A diferencia del comando `cp`, no necesitas la opción `-r` para mover un directorio. El comando `bash mv` maneja los directorios por defecto. Aunque algunos usuarios buscan `mv -r linux`, esta opción no es necesaria para mover directorios con `mv`.

### Opciones Importantes para el Comando mv

Por defecto, si mueves un archivo a un destino donde ya existe un archivo con el mismo nombre, `mv` lo sobrescribirá sin advertencia. Para prevenir la pérdida accidental de datos, puedes usar las siguientes opciones:

- **-i (interactivo)**: Esta es una característica de seguridad crucial. Te pedirá confirmación antes de sobrescribir cualquier archivo existente.

  ```bash
  mv -i archivo_origen directorio_destino
  ```

- **-b (backup)**: Si tienes la intención de sobrescribir un archivo pero deseas conservar la versión antigua, esta opción crea una copia de seguridad del archivo de destino. La copia de seguridad generalmente se renombra con el sufijo tilde (`~`).

  ```bash
  mv -b archivo1 directorio_con_archivo1
  ```

- **-v (verbose)**: Esta opción hace que el comando `mv` imprima lo que está haciendo, mostrando cada archivo que se mueve o renombra.

  ```bash
  mv -v archivo1 archivo2 /un_directorio
  ```

Dominar el `mv command` es esencial para una gestión eficiente de archivos en la línea de comandos.

## Exercise

¡La práctica hace al maestro! La experiencia práctica es crucial para dominar comandos de Linux como `mv`. Estos laboratorios te ayudarán a solidificar tu comprensión de mover y renombrar archivos y directorios en un entorno real:

1.  **[Comando mv de Linux: Mover y Renombrar Archivos](https://labex.io/es/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Practica el uso del comando `mv` para mover y renombrar archivos y directorios, incluida la comprensión de sus diversas opciones y comportamientos.
2.  **[Organización de Archivos y Directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Aplica tu conocimiento de `mv` (junto con `cp` y `rm`) en un desafío práctico para organizar una estructura de proyecto, mover archivos y limpiar directorios.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza con la gestión de archivos y directorios usando el comando `mv`.

## Quiz Question

Usando el comando `mv`, ¿cómo renombrarías un archivo llamado `cat` a `dog`? Por favor, proporciona el comando completo. Nota: La respuesta distingue entre mayúsculas y minúsculas y debe introducirse en inglés minúsculas.

## Quiz Answer

mv cat dog
