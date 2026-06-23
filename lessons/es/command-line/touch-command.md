---
index: 5
lang: "es"
title: "touch"
meta_title: "touch - Línea de Comandos"
meta_description: "Aprende el comando touch de Linux con ejemplos para crear archivos vacíos, actualizar marcas de tiempo, establecer fechas, usar archivos de referencia y evitar sobrescrituras."
meta_keywords: "comando linux touch, comando touch, crear archivo linux, actualizar marca de tiempo linux, touch -d, touch -r, touch -c"
---

## Lesson Content

El comando `touch` es una utilidad estándar en sistemas operativos tipo Unix. Aunque su propósito principal es cambiar las marcas de tiempo de los archivos, también se usa comúnmente para crear archivos nuevos y vacíos.

La sintaxis básica es:

```bash
touch [OPTIONS] FILE...
```

### Creación de Archivos Nuevos

La forma más sencilla de crear un archivo vacío es usar `touch` seguido del nombre del archivo. Si el archivo no existe, `touch` lo crea.

```bash
$ touch mysuperduperfile
```

Después de ejecutar este comando, aparecerá un nuevo archivo vacío llamado `mysuperduperfile` en tu directorio actual. Puedes crear varios archivos a la vez listando sus nombres.

```bash
$ touch file1.txt file2.txt file3.log
```

Esto es útil cuando configuras la estructura de un proyecto o creas archivos de marcador de posición antes de agregar contenido.

### Actualización de Marcas de Tiempo de Archivos

La función original de `touch` es actualizar las marcas de tiempo de acceso y modificación de un archivo o directorio. Si usas `touch` en un archivo existente, actualiza sus marcas de tiempo a la hora actual.

Puedes verificar esto usando `ls -l` para revisar la marca de tiempo de un archivo, ejecutando `touch` sobre él, y luego revisando nuevamente.

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### Control Avanzado de Marcas de Tiempo

El comando `touch` también ofrece opciones para una manipulación más precisa de las marcas de tiempo.

Usa un archivo de referencia con `-r` para copiar las marcas de tiempo de un archivo a otro.

```bash
$ touch -r file1.txt file2.txt
```

Establece una fecha y hora específica con `-d`:

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

Usa `-c` cuando quieras actualizar un archivo solo si ya existe. Con `-c`, `touch` no creará un archivo faltante.

```bash
$ touch -c existing-file.txt
```

### Opciones Comunes de touch

- `-a`: Cambiar solo la hora de acceso.
- `-m`: Cambiar solo la hora de modificación.
- `-c`: No crear el archivo si no existe.
- `-d "FECHA"`: Usar una cadena de fecha específica.
- `-r ARCHIVO`: Usar la marca de tiempo de otro archivo como referencia.
- `-t MARCA`: Usar una marca de tiempo en formato numérico compacto.

Por ejemplo, esto cambia solo la hora de modificación:

```bash
$ touch -m notes.txt
```

### Preguntas Comunes

**¿touch añade texto a un archivo?** No. `touch` crea un archivo vacío o actualiza marcas de tiempo. Usa un editor, `echo` o `cat` para añadir texto.

**¿touch sobrescribe un archivo existente?** No. Actualiza las marcas de tiempo pero no reemplaza el contenido del archivo.

**¿Por qué usar touch en scripts?** Es una forma rápida de asegurar que un archivo exista o de marcar que una tarea ocurrió en un momento determinado.

## Exercise

Practice makes perfect! Here are some hands-on labs to reinforce your understanding of creating and managing file system objects:

1. **[Linux mkdir Command: Directory Creating](https://labex.io/es/labs/linux-linux-mkdir-command-directory-creating-209739)** - Learn how to use the `mkdir` command in Linux to create directories, set permissions, and organize your file system. This will help you understand the broader concept of creating new items in the file system.
2. **[Setting Up a New Project Structure](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practice your Linux directory management skills by creating a specific project structure and navigating through it using essential commands like `mkdir` and `cd`.

These labs will help you apply the concepts of file system creation and organization in real scenarios and build confidence with Linux commands.

## Quiz Question

¿Cómo se crea un archivo llamado `myfile`? Por favor responde usando solo el comando en inglés, prestando atención a las mayúsculas y minúsculas.

## Quiz Answer

touch myfile
