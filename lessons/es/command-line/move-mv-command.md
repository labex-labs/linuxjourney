---
index: 11
lang: "es"
title: "mv (Mover)"
meta_title: "mv (Mover) - Línea de Comandos"
meta_description: "Aprende el comando mv de Linux con ejemplos para mover archivos, renombrar archivos y directorios, mover múltiples archivos y evitar sobrescrituras."
meta_keywords: "comando linux mv, comando mv, mover archivos linux, renombrar archivo linux, renombrar directorio linux, mv -i, mv -n, mv -t"
---

## Lesson Content

El comando `mv`, abreviatura de "mover", es una utilidad fundamental en cualquier entorno Linux. Sirve para dos propósitos principales: renombrar archivos o directorios y moverlos a una ubicación diferente.

La sintaxis básica es:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

A diferencia de `cp`, que crea una copia, `mv` cambia dónde se encuentra el elemento original o cómo se llama.

### Renombrar Archivos y Directorios

Uno de los usos más comunes de `mv` es renombrar. La sintaxis es sencilla: especifica el nombre antiguo y el nuevo nombre.

Para renombrar un archivo:

```bash
$ mv oldfile newfile
```

Esta misma lógica se aplica para renombrar directorios:

```bash
$ mv old_directory_name new_directory_name
```

### Mover Archivos y Directorios

La otra función principal del comando `mv` es mover elementos de una ubicación a otra.

Para mover un solo archivo a un directorio diferente:

```bash
$ mv file2 /home/pete/Documents
```

También puedes mover múltiples archivos a la vez. Simplemente lista todos los archivos origen seguidos del directorio destino:

```bash
$ mv file_1 file_2 somedirectory/
```

En sistemas GNU/Linux, una opción útil para esto es `-t`, que permite especificar primero el directorio destino. Esto puede ser más claro al mover muchos archivos.

```bash
$ mv -t somedirectory/ file_1 file_2
```

A diferencia del comando `cp`, no necesitas una opción recursiva para mover un directorio. `mv` maneja directorios por defecto.

### Opciones Importantes para el Comando mv

Por defecto, si mueves un archivo a un destino donde ya existe un archivo con el mismo nombre, `mv` lo sobrescribirá sin advertencia. Para evitar pérdida accidental de datos, puedes usar las siguientes opciones:

- **-i (interactivo)**: Esta es una característica de seguridad crucial. Te pedirá confirmación antes de sobrescribir cualquier archivo existente.

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-b (backup)**: Si tienes la intención de sobrescribir un archivo pero quieres conservar la versión antigua, esta opción crea una copia de seguridad del archivo destino. La copia de seguridad generalmente se renombra con un sufijo tilde (`~`).

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v (verbose)**: Esta opción hace que el comando `mv` imprima lo que está haciendo, mostrando cada archivo que se mueve o renombra.

  ```bash
  $ mv -v file1 file2 somedirectory/
  ```

Otra opción útil es `-n`, que significa no sobrescribir. Evita sobrescribir un archivo destino existente.

```bash
$ mv -n source_file destination_directory
```

### Ejemplos Comunes de mv

Renombrar un archivo:

```bash
$ mv draft.txt final.txt
```

Mover un directorio:

```bash
$ mv project /home/pete/Documents/
```

Mover todos los archivos de texto a una carpeta:

```bash
$ mv *.txt notes/
```

Previsualiza las coincidencias de comodines con `ls` antes de mover muchos archivos.

### Preguntas Comunes

**¿mv copia archivos?** No. `mv` mueve o renombra el elemento original.

**¿Puede mv sobrescribir archivos?** Sí. Usa `mv -i` para preguntar primero o `mv -n` para evitar sobrescribir.

**¿Necesito mv -r para directorios?** No. `mv` mueve directorios sin `-r`.

## Exercise

¡La práctica hace al maestro! La experiencia práctica es crucial para dominar comandos de Linux como `mv`. Estos laboratorios te ayudarán a consolidar tu comprensión de mover y renombrar archivos y directorios en un entorno real:

1. **[Comando Linux mv: Mover y Renombrar Archivos](https://labex.io/es/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - Practica usando el comando `mv` para mover y renombrar archivos y directorios, incluyendo la comprensión de sus diversas opciones y comportamientos.
2. **[Organización de Archivos y Directorios](https://labex.io/es/labs/linux-organizing-files-and-directories-387877)** - Aplica tu conocimiento de `mv` (junto con `cp` y `rm`) en un desafío práctico para organizar la estructura de un proyecto, mover archivos y limpiar directorios.

Estos laboratorios te ayudarán a aplicar los conceptos en escenarios reales y a ganar confianza en la gestión de archivos y directorios usando el comando `mv`.

## Quiz Question

Usando el comando `mv`, ¿cómo renombrarías un archivo llamado `cat` a `dog`? Por favor proporciona el comando completo. Nota: La respuesta es sensible a mayúsculas y debe ingresarse en inglés en minúsculas.

## Quiz Answer

mv cat dog
