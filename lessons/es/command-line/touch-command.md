---
index: 5
lang: "es"
title: "touch"
meta_title: "touch - Línea de Comandos"
meta_description: "Aprenda a usar el comando linux touch para crear archivos y gestionar marcas de tiempo. Esta guía cubre el comando touch en linux, incluyendo opciones como linux touch -r y touch -d."
meta_keywords: "linux touch, comando touch en linux, bash touch, touch -d linux, linux touch -r, crear archivos, actualizar marcas de tiempo, gestión de archivos, comandos linux"
---

## Lesson Content

El comando `touch` es una utilidad estándar en sistemas operativos tipo Unix. Aunque su propósito principal es cambiar las marcas de tiempo de los archivos, también se utiliza comúnmente para crear archivos nuevos y vacíos. Exploremos cómo funciona el comando `linux touch`.

### Creación de Archivos Nuevos

La forma más sencilla de crear un archivo vacío es usar el comando `touch` seguido de un nombre de archivo. Si el archivo no existe, `touch` lo creará por usted. Esta es una operación fundamental de `bash touch` para la creación de scripts y tareas diarias.

```bash
touch mysuperduperfile
```

Después de ejecutar este comando, aparecerá un nuevo archivo vacío llamado `mysuperduperfile` en su directorio actual. Puede crear varios archivos a la vez enumerando sus nombres.

```bash
touch archivo1.txt archivo2.txt archivo3.log
```

### Actualización de Marcas de Tiempo de Archivos

La función original del `touch command in linux` es actualizar las marcas de tiempo de acceso y modificación de un archivo o directorio. Si usa `touch` en un archivo existente, actualizará sus marcas de tiempo a la hora actual.

Puede verificar esto usando `ls -l` para revisar la marca de tiempo de un archivo, ejecutando `touch` sobre él y luego revisando de nuevo.

```bash
# Revisar la marca de tiempo original
ls -l mysuperduperfile

# Actualizar la marca de tiempo
touch mysuperduperfile

# Revisar la nueva marca de tiempo
ls -l mysuperduperfile
```

### Control Avanzado de Marcas de Tiempo

El comando `linux touch` también proporciona opciones para una manipulación más precisa de las marcas de tiempo.

#### Uso de un Archivo de Referencia

La opción `linux touch -r` le permite establecer la marca de tiempo de un archivo para que coincida con la de otro archivo (un archivo de referencia). Esto es útil para sincronizar marcas de tiempo entre archivos relacionados.

```bash
# Establecer la marca de tiempo de archivo2.txt para que coincida con la de archivo1.txt
touch -r archivo1.txt archivo2.txt
```

#### Establecer una Fecha Específica

Con la opción `touch -d`, puede establecer la marca de tiempo de un archivo a una fecha y hora específicas. La funcionalidad `touch -d linux` acepta varios formatos de cadena para la fecha.

```bash
# Establecer la marca de tiempo a una fecha y hora específicas
touch -d "2023-01-01 12:30:00" mysuperduperfile
```

Dominar `touch` es un gran paso para aprender a administrar su sistema de archivos de manera eficiente desde la línea de comandos.

## Exercise

¡La práctica hace al maestro! Aquí hay algunos laboratorios prácticos para reforzar su comprensión de la creación y gestión de objetos del sistema de archivos:

1. **[Comando Linux mkdir: Creación de Directorios](https://labex.io/es/labs/linux-linux-mkdir-command-directory-creating-209739)** - Aprenda a usar el comando `mkdir` en Linux para crear directorios, establecer permisos y organizar su sistema de archivos. Esto le ayudará a comprender el concepto más amplio de crear nuevos elementos en el sistema de archivos.
2. **[Configuración de una Nueva Estructura de Proyecto](https://labex.io/es/labs/linux-setting-up-a-new-project-structure-387859)** - Practique sus habilidades de gestión de directorios de Linux creando una estructura de proyecto específica y navegando a través de ella usando comandos esenciales como `mkdir` y `cd`.

Estos laboratorios le ayudarán a aplicar los conceptos de creación y organización del sistema de archivos en escenarios reales y a ganar confianza con los comandos de Linux.

## Quiz Question

¿Cómo se crea un archivo llamado `myfile`? Por favor, responda usando solo el comando en inglés, prestando atención a la sensibilidad a mayúsculas y minúsculas.

## Quiz Answer

touch myfile
